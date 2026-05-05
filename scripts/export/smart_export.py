"""
smart_export.py

Incremental export: only re-exports pages whose source files (or any of their
transitive dependencies) have changed since the last export run.

Change detection uses git diff against the docs submodule. The last processed
commit hash is stored in .export-state.json alongside this script. In CI the
--from-commit and --to-commit arguments are used instead.

Usage (local):
    python smart_export.py
        --docs-folder D:/Git/AgoraDocs/Docs
        --output-dir D:/Git/AgoraTools/markdown-service/public/en

    # Override dep-map location
    python smart_export.py
        --docs-folder D:/Git/AgoraDocs/Docs
        --output-dir D:/Git/markdown-service/public/en
        --dep-map D:/Git/AgoraDocs/Docs/data/dep-map.json

    # Dry run — show what would be exported without writing files
    python smart_export.py
        --docs-folder D:/Git/AgoraDocs/Docs
        --output-dir D:/Git/markdown-service/public/en
        --dry-run

Usage (CI):
    python smart_export.py
        --docs-folder .
        --output-dir ../markdown-service/public/en
        --from-commit ${{ github.event.before }}
        --to-commit ${{ github.sha }}
"""

import os
import re
import json
import argparse
import subprocess
from datetime import datetime, timezone

from export_utils import (
    load_product_platforms,
    parse_frontmatter,
    should_skip,
    run_mdx2md,
    create_platform_index_file,
    write_error_log,
)

try:
    from add_docs_index import add_docs_index_for_product
    _DOCS_INDEX_AVAILABLE = True
except ImportError:
    _DOCS_INDEX_AVAILABLE = False

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".export-state.json")

# ---------------------------------------------------------------------------
# State file helpers
# ---------------------------------------------------------------------------

def read_state() -> dict:
    """Read .export-state.json. Returns {} if missing or invalid."""
    if not os.path.isfile(STATE_FILE):
        return {}
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}


def write_state(state: dict) -> None:
    """Write .export-state.json."""
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)
    print(f"💾 State saved → {STATE_FILE}")


# ---------------------------------------------------------------------------
# Git helpers
# ---------------------------------------------------------------------------

def git(args: list, cwd: str) -> str:
    """Run a git command in cwd and return stdout. Raises on error."""
    result = subprocess.run(
        ["git"] + args,
        cwd=cwd,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"git {' '.join(args)} failed:\n{result.stderr.strip()}"
        )
    return result.stdout.strip()


def get_head_commit(submodule_root: str) -> str:
    """Return the current HEAD commit hash of the submodule."""
    return git(["rev-parse", "HEAD"], cwd=submodule_root)


def get_commit_before_days(submodule_root: str, days: int) -> str:
    """
    Return the most recent commit hash that is at least `days` days old.
    Falls back to the first commit if no such commit exists.
    """
    try:
        return git(
            ["rev-list", "-1", f"--before={days} days ago", "HEAD"],
            cwd=submodule_root,
        )
    except RuntimeError:
        # Fall back to the very first commit
        return git(["rev-list", "--max-parents=0", "HEAD"], cwd=submodule_root)


def get_changed_files(submodule_root: str, from_commit: str, to_commit: str) -> tuple:
    """
    Return (changed, deleted) lists of file paths relative to the submodule
    root that changed between from_commit and to_commit.

    Only .md and .mdx files are returned.
    """
    try:
        output = git(
            ["diff", "--name-status", from_commit, to_commit],
            cwd=submodule_root,
        )
    except RuntimeError as e:
        print(f"⚠️  git diff failed: {e}")
        return [], []

    changed = []
    deleted = []

    for line in output.splitlines():
        if not line.strip():
            continue
        parts = line.split("\t", 1)
        if len(parts) != 2:
            continue
        status, path = parts[0].strip(), parts[1].strip()
        path = path.replace("\\", "/")

        if not (path.endswith(".md") or path.endswith(".mdx")):
            continue

        if status == "D":
            deleted.append(path)
        else:
            # A = added, M = modified, R = renamed (git shows R100\told\tnew)
            # For renames, parts[1] may be "old\tnew" — take the new path
            if "\t" in path:
                path = path.split("\t")[-1].strip()
            changed.append(path)

    return changed, deleted


# ---------------------------------------------------------------------------
# Dep map helpers
# ---------------------------------------------------------------------------

def load_dep_map(dep_map_path: str) -> dict:
    """
    Load dep-map.json and return the pages dict.
    Keys and dep values are paths relative to the docs submodule root.
    """
    with open(dep_map_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("pages", {})


def build_reverse_map(dep_map: dict) -> dict:
    """
    Build a reverse index: dep_path -> set of page paths that depend on it.
    This allows fast lookup of which pages are affected when a shared file
    or image changes.
    """
    reverse = {}
    for page, deps in dep_map.items():
        for dep in deps:
            reverse.setdefault(dep, set()).add(page)
    return reverse


def resolve_affected_pages(
    changed_files: list,
    dep_map: dict,
    reverse_map: dict,
) -> set:
    """
    Given a list of changed file paths (relative to submodule root), return
    the set of page paths that need re-exporting.

    - If the changed file is a page key in dep_map, add it directly.
    - If the changed file appears as a dependency in reverse_map, add all
      pages that depend on it.
    - Files not in either map (for example config files) are ignored.
    """
    affected = set()
    for path in changed_files:
        path = path.replace("\\", "/")
        if path in dep_map:
            # The changed file is itself a page
            affected.add(path)
        if path in reverse_map:
            # The changed file is a dependency of one or more pages
            affected.update(reverse_map[path])
    return affected


# ---------------------------------------------------------------------------
# Output file resolution
# ---------------------------------------------------------------------------

def get_output_files_for_page(
    page_rel: str,
    platforms: list,
    fm: dict,
    output_base: str,
) -> list:
    """
    Return the list of output .md file paths that correspond to a source page.

    For platform-selector pages: base_name_platform.md per platform + base_name.md index.
    For platform-agnostic pages: base_name.md only.
    """
    base_name = os.path.splitext(os.path.basename(page_rel))[0]
    rel_dir = os.path.dirname(page_rel)
    output_dir = os.path.normpath(os.path.join(output_base, rel_dir))

    excluded = fm.get("excluded_platforms", [])
    platform_selector = fm.get("platform_selector", True)
    if not platforms:
        platform_selector = False

    if not platform_selector:
        return [os.path.join(output_dir, f"{base_name}.md")]

    files = []
    active_platforms = [p for p in platforms if p not in excluded]
    for p in active_platforms:
        files.append(os.path.join(output_dir, f"{base_name}_{p}.md"))
    # Platform selector index
    files.append(os.path.join(output_dir, f"{base_name}.md"))
    return files


def delete_output_files(output_files: list) -> int:
    """
    Delete a list of output files. Returns count of files actually deleted.
    """
    deleted = 0
    for f in output_files:
        if os.path.isfile(f):
            os.remove(f)
            print(f"  🗑  Deleted: {f}")
            deleted += 1
    return deleted


# ---------------------------------------------------------------------------
# Prompt for initial commit reference
# ---------------------------------------------------------------------------

def prompt_for_from_commit(submodule_root: str) -> str:
    """
    Prompt the user to specify how many days back to look for the base commit.
    Returns the resolved commit hash.
    """
    print("\n⚠️  No previous export state found (.export-state.json is missing).")
    print("   This appears to be the first run of smart_export.py.")
    print("   Please specify how many days ago the last export was performed.")
    print("   (This is used to find the base commit for the diff.)\n")

    while True:
        try:
            days_str = input("   Days since last export: ").strip()
            days = int(days_str)
            if days <= 0:
                print("   Please enter a positive number.")
                continue
            break
        except ValueError:
            print("   Please enter a whole number.")

    commit = get_commit_before_days(submodule_root, days)
    if not commit:
        raise RuntimeError(
            f"Could not find a commit from {days} days ago in {submodule_root}."
        )

    print(f"\n   Using base commit: {commit}")
    return commit


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Incrementally export changed Agora MDX docs to plain markdown."
    )
    parser.add_argument(
        "--docs-folder",
        required=True,
        help="Path to the Docs root folder, e.g. D:/Git/AgoraDocs/Docs",
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        help="Base output folder for generated .md files, "
             "e.g. D:/Git/markdown-service/public/en",
    )
    parser.add_argument(
        "--dep-map",
        default=None,
        help="Path to dep-map.json (default: <docs-folder>/data/dep-map.json)",
    )
    parser.add_argument(
        "--from-commit",
        default=None,
        help="Base commit hash for git diff (CI use). "
             "If omitted, reads from .export-state.json.",
    )
    parser.add_argument(
        "--to-commit",
        default=None,
        help="Target commit hash for git diff (CI use). "
             "Defaults to HEAD of the docs submodule.",
    )
    parser.add_argument(
        "--skip-platform-index",
        action="store_true",
        help="Skip creating platform selector index files.",
    )
    parser.add_argument(
        "--no-overview-index",
        action="store_true",
        help="Skip updating product-overview.md index after export.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be exported/deleted without writing any files.",
    )
    args = parser.parse_args()

    docs_folder      = os.path.abspath(args.docs_folder)
    output_base      = os.path.abspath(args.output_dir)
    submodule_root   = os.path.normpath(os.path.join(docs_folder, "docs"))
    scripts_dir      = os.path.dirname(os.path.abspath(__file__))
    dep_map_path     = os.path.abspath(
        args.dep_map or os.path.join(docs_folder, "data", "dep-map.json")
    )
    products_file    = os.path.join(docs_folder, "data", "v2", "products.js")

    inject_overview_index = not args.no_overview_index
    if inject_overview_index and not _DOCS_INDEX_AVAILABLE:
        print(
            "⚠️  add_docs_index.py not found — overview index injection disabled."
        )
        inject_overview_index = False

    # ------------------------------------------------------------------
    # Validate paths
    # ------------------------------------------------------------------
    for label, path in [
        ("Docs folder",   docs_folder),
        ("Submodule root", submodule_root),
        ("dep-map.json",  dep_map_path),
        ("products.js",   products_file),
    ]:
        if not os.path.exists(path):
            print(f"❌ {label} not found: {path}")
            return

    # Derive images output directory from output_base
    # e.g. public/en -> public/images
    images_dir = os.path.normpath(os.path.join(output_base, ".."))

    # ------------------------------------------------------------------
    # Resolve from/to commits
    # ------------------------------------------------------------------
    to_commit = args.to_commit or get_head_commit(submodule_root)

    if args.from_commit:
        from_commit = args.from_commit
    else:
        state = read_state()
        if state.get("last_commit"):
            from_commit = state["last_commit"]
            print(f"📌 Resuming from commit: {from_commit}")
        else:
            from_commit = prompt_for_from_commit(submodule_root)

    if from_commit == to_commit:
        print("✅ No new commits since last export. Nothing to do.")
        return

    print(f"\n🔍 Diffing {from_commit[:8]}..{to_commit[:8]}")

    # ------------------------------------------------------------------
    # Load dep map and product platforms
    # ------------------------------------------------------------------
    dep_map         = load_dep_map(dep_map_path)
    reverse_map     = build_reverse_map(dep_map)
    product_platforms = load_product_platforms(products_file)

    # ------------------------------------------------------------------
    # Get changed and deleted files from git
    # ------------------------------------------------------------------
    changed_files, deleted_files = get_changed_files(
        submodule_root, from_commit, to_commit
    )

    print(f"   {len(changed_files)} changed file(s), {len(deleted_files)} deleted file(s)")

    # ------------------------------------------------------------------
    # Resolve affected pages
    # ------------------------------------------------------------------
    affected_pages = resolve_affected_pages(changed_files, dep_map, reverse_map)

    # Resolve deleted files to pages they represent or pages that depend on them
    deleted_pages  = resolve_affected_pages(deleted_files, dep_map, reverse_map)
    # Also include deleted files that are themselves pages
    for f in deleted_files:
        f = f.replace("\\", "/")
        if f in dep_map:
            deleted_pages.add(f)

    if not affected_pages and not deleted_pages:
        print("✅ No doc pages affected by these changes. Nothing to export.")
        if not args.from_commit:
            write_state({"last_commit": to_commit, "updated_at": datetime.now(timezone.utc).isoformat()})
        return

    print(f"\n📄 Pages to export : {len(affected_pages)}")
    print(f"🗑  Pages to delete : {len(deleted_pages)}")

    if args.dry_run:
        print("\n🔍 Dry run — no files will be written.\n")
        if affected_pages:
            print("Would export:")
            for p in sorted(affected_pages):
                print(f"  + {p}")
        if deleted_pages:
            print("\nWould delete output files for:")
            for p in sorted(deleted_pages):
                print(f"  - {p}")
        return

    # ------------------------------------------------------------------
    # Delete output files for deleted/removed pages
    # ------------------------------------------------------------------
    total_deleted = 0
    if deleted_pages:
        print("\n🗑  Deleting output files for removed pages...")
        for page_rel in sorted(deleted_pages):
            parts = page_rel.replace("\\", "/").split("/")
            product_id = parts[0]
            platforms = product_platforms.get(product_id, [])

            page_abs = os.path.normpath(os.path.join(submodule_root, page_rel))
            fm = {}  # File is deleted so we can't read frontmatter
            # Use dep_map entry to determine if it was platform-selector
            # Fall back to assuming platform-selector if product has platforms
            output_files = get_output_files_for_page(
                page_rel, platforms, fm, output_base
            )
            total_deleted += delete_output_files(output_files)

    # ------------------------------------------------------------------
    # Export affected pages
    # ------------------------------------------------------------------
    failed_exports = []
    processed_files = 0
    successful_exports = 0
    index_files_created = 0
    affected_products = set()

    print(f"\n🚀 Exporting {len(affected_pages)} page(s)...\n")

    for page_rel in sorted(affected_pages):
        page_rel = page_rel.replace("\\", "/")
        parts = page_rel.split("/")
        product_id = parts[0]

        if product_id not in product_platforms:
            print(f"⚠️  Skipping {page_rel} — no product mapping for '{product_id}'")
            continue

        page_abs = os.path.normpath(os.path.join(submodule_root, page_rel))
        if not os.path.isfile(page_abs):
            print(f"⚠️  Skipping {page_rel} — file not found (may have been deleted)")
            continue

        platforms = product_platforms[product_id]
        fm = parse_frontmatter(page_abs)
        excluded = fm.get("excluded_platforms", [])
        platform_selector = fm.get("platform_selector", True)
        if not platforms:
            platform_selector = False

        rel_dir = os.path.dirname(page_rel)
        output_dir = os.path.normpath(os.path.join(output_base, rel_dir))
        os.makedirs(output_dir, exist_ok=True)

        base_name = os.path.splitext(os.path.basename(page_rel))[0]

        if not platform_selector:
            output_file = os.path.join(output_dir, f"{base_name}.md")
            processed_files += 1
            if run_mdx2md(page_abs, None, output_file, docs_folder, failed_exports, scripts_dir, images_dir):
                successful_exports += 1
                affected_products.add(product_id)
        else:
            successful_platforms = []
            for p in platforms:
                if p in excluded:
                    print(f"  └─ Skipping {p} (excluded)")
                    continue
                output_file = os.path.join(output_dir, f"{base_name}_{p}.md")
                processed_files += 1
                if run_mdx2md(page_abs, p, output_file, docs_folder, failed_exports, scripts_dir, images_dir):
                    successful_exports += 1
                    successful_platforms.append(p)
                    affected_products.add(product_id)

            if not args.skip_platform_index:
                if len(successful_platforms) > 1:
                    if create_platform_index_file(
                        page_abs, successful_platforms, output_dir, base_name, docs_folder
                    ):
                        index_files_created += 1
                elif len(successful_platforms) == 0:
                    # All platforms failed — remove stale index if present
                    index_path = os.path.join(output_dir, f"{base_name}.md")
                    if os.path.isfile(index_path):
                        os.remove(index_path)
                        print(f"  🗑  Removed stale index: {index_path}")

    # ------------------------------------------------------------------
    # Update overview index for affected products
    # ------------------------------------------------------------------
    if inject_overview_index and affected_products:
        print(f"\n📋 Updating documentation index for {len(affected_products)} product(s)...")
        for product_id in sorted(affected_products):
            source_product_dir = os.path.normpath(
                os.path.join(submodule_root, product_id)
            )
            output_product_dir = os.path.normpath(
                os.path.join(output_base, product_id)
            )
            if not os.path.isdir(output_product_dir):
                continue
            print(f"\n  📦 {product_id}")
            add_docs_index_for_product(
                product_id=product_id,
                source_product_dir=source_product_dir,
                output_product_dir=output_product_dir,
                platforms=product_platforms.get(product_id, []),
            )

    # ------------------------------------------------------------------
    # Write error log
    # ------------------------------------------------------------------
    write_error_log(failed_exports, output_base)

    # ------------------------------------------------------------------
    # Save state (local runs only — CI uses explicit commits)
    # ------------------------------------------------------------------
    if not args.from_commit:
        write_state({
            "last_commit": to_commit,
            "updated_at": datetime.now(timezone.utc).isoformat(),
        })

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    print("\n" + "-" * 60)
    print("📊 Export Summary:")
    print(f"   📄 Pages processed      : {processed_files}")
    print(f"   ✅ Successful exports   : {successful_exports}")
    print(f"   ❌ Failed exports       : {len(failed_exports)}")
    print(f"   📑 Platform indexes     : {index_files_created}")
    print(f"   🗑  Output files deleted : {total_deleted}")
    print(f"   📦 Products updated     : {len(affected_products)}")

    if failed_exports:
        print("\n❌ Failed exports:")
        for error in failed_exports:
            platform_info = f" ({error['platform']})" if error['platform'] else ""
            print(f"   • {os.path.basename(error['file'])}{platform_info}")
        print(f"\n📋 See export_errors.log in {output_base} for details.")
    else:
        print("\n🎉 All exports completed successfully!")


if __name__ == "__main__":
    main()