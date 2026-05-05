#!/usr/bin/env python3
"""
inject_last_updated.py
 
Injects or updates `last_update.date` in the frontmatter of MDX pages
that were affected by recent commits.
 
Uses git diff to find changed files, resolves affected pages via dep-map.json,
then uses a single git log call per page to get the most recent commit date
across the page and all its dependencies.
 
Designed to run in CI against the Docs-Source repo where MDX files live
at the repo root (no docs/ prefix).
 
Usage:
    python scripts/inject_last_updated.py \\
        --repo-root /path/to/repo \\
        --dep-map /path/to/dep-map.json \\
        --from-commit <sha> \\
        --to-commit <sha>
 
    # Dry run
    python scripts/inject_last_updated.py \\
        --repo-root /path/to/repo \\
        --dep-map /path/to/dep-map.json \\
        --from-commit <sha> \\
        --to-commit <sha> \\
        --dry-run
"""
 
import os
import re
import json
import argparse
import subprocess
from datetime import datetime, timezone
 
 
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
 
 
def get_changed_files(repo_root: str, from_commit: str, to_commit: str) -> tuple:
    """
    Return (changed, deleted) lists of file paths relative to repo root
    that changed between from_commit and to_commit.
    Only .md and .mdx files are returned.
    """
    try:
        output = git(
            ["diff", "--name-status", from_commit, to_commit],
            cwd=repo_root,
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
            if "\t" in path:
                path = path.split("\t")[-1].strip()
            changed.append(path)
 
    return changed, deleted
 
 
def get_latest_date_for_page(repo_root: str, page_path: str, deps: list) -> str:
    """
    Get the most recent git commit date across the page file and all its
    dependencies in a single git log call.
 
    Returns date as YYYY-MM-DD string, or None if no commits found.
    """
    all_paths = [page_path] + deps
 
    # Filter to only paths that exist on disk
    existing_paths = [
        p for p in all_paths
        if os.path.isfile(os.path.join(repo_root, p))
    ]
 
    if not existing_paths:
        return None
 
    try:
        output = git(
            ["log", "-1", "--format=%ci", "--"] + existing_paths,
            cwd=repo_root,
        )
        if not output:
            return None
        # Parse the date portion from the git log output
        date_str = output.strip().split(" ")[0]
        return date_str  # YYYY-MM-DD
    except RuntimeError:
        return None
 
 
# ---------------------------------------------------------------------------
# Dep map helpers
# ---------------------------------------------------------------------------
 
def load_dep_map(dep_map_path: str) -> dict:
    """Load dep-map.json and return the pages dict."""
    with open(dep_map_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("pages", {})
 
 
def build_reverse_map(dep_map: dict) -> dict:
    """Build reverse index: dep_path -> set of page paths that depend on it."""
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
    Resolve changed files to the set of page paths that need updating.
    """
    affected = set()
    for path in changed_files:
        path = path.replace("\\", "/")
        if path in dep_map:
            affected.add(path)
        if path in reverse_map:
            affected.update(reverse_map[path])
    return affected
 
 
# ---------------------------------------------------------------------------
# Frontmatter injection
# ---------------------------------------------------------------------------
 
def read_existing_date(content: str) -> str:
    """Read the existing last_update.date from frontmatter, or None."""
    fm_match = re.match(r"^---\r?\n([\s\S]*?)\r?\n---", content)
    if not fm_match:
        return None
    date_match = re.search(
        r"^\s*last_update:\s*\r?\n\s*date:\s*(\S+)",
        fm_match.group(1),
        re.MULTILINE,
    )
    return date_match.group(1) if date_match else None
 
 
def inject_date(content: str, date_str: str) -> str:
    """
    Write last_update.date into the frontmatter.
    Replaces existing last_update block if present, otherwise appends before
    closing ---.
    """
    new_block = f"last_update:\n  date: {date_str}"
 
    # Replace existing last_update block
    if re.search(r"^\s*last_update:\s*\r?\n\s*date:\s*\S+", content, re.MULTILINE):
        return re.sub(
            r"^(\s*last_update:\s*\r?\n\s*date:\s*)\S+",
            f"\\g<1>{date_str}",
            content,
            flags=re.MULTILINE,
        )
 
    # Replace flat last_update: value
    if re.search(r"^\s*last_update:\s*\S+", content, re.MULTILINE):
        return re.sub(
            r"^\s*last_update:\s*\S+",
            new_block,
            content,
            flags=re.MULTILINE,
        )
 
    # Append before closing ---
    return re.sub(
        r"^(---\r?\n[\s\S]*?)(^---)",
        f"\\g<1>{new_block}\n\\g<2>",
        content,
        flags=re.MULTILINE,
    )
 
 
# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
 
def main():
    parser = argparse.ArgumentParser(
        description="Inject last_update dates into MDX frontmatter."
    )
    parser.add_argument(
        "--repo-root",
        required=True,
        help="Path to the root of the Docs-Source repo checkout.",
    )
    parser.add_argument(
        "--dep-map",
        required=True,
        help="Path to dep-map.json.",
    )
    parser.add_argument(
        "--from-commit",
        required=True,
        help="Base commit hash for git diff.",
    )
    parser.add_argument(
        "--to-commit",
        required=True,
        help="Target commit hash for git diff.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be updated without writing any files.",
    )
    args = parser.parse_args()
 
    repo_root    = os.path.abspath(args.repo_root)
    dep_map_path = os.path.abspath(args.dep_map)
    from_commit  = args.from_commit
    to_commit    = args.to_commit
 
    # ------------------------------------------------------------------
    # Validate
    # ------------------------------------------------------------------
    if not os.path.isdir(repo_root):
        print(f"❌ Repo root not found: {repo_root}")
        return
    if not os.path.isfile(dep_map_path):
        print(f"❌ dep-map.json not found: {dep_map_path}")
        return
 
    # ------------------------------------------------------------------
    # Load dep map
    # ------------------------------------------------------------------
    dep_map     = load_dep_map(dep_map_path)
    reverse_map = build_reverse_map(dep_map)
 
    # ------------------------------------------------------------------
    # Get changed files
    # ------------------------------------------------------------------
    changed_files, _ = get_changed_files(repo_root, from_commit, to_commit)
    print(f"🔍 {len(changed_files)} changed file(s) between "
          f"{from_commit[:8]}..{to_commit[:8]}")
 
    # ------------------------------------------------------------------
    # Resolve affected pages
    # ------------------------------------------------------------------
    affected_pages = resolve_affected_pages(changed_files, dep_map, reverse_map)
 
    if not affected_pages:
        print("✅ No pages affected — nothing to inject.")
        return
 
    print(f"📄 {len(affected_pages)} page(s) to update\n")
 
    if args.dry_run:
        print("🔍 Dry run — no files will be written.\n")
        for p in sorted(affected_pages):
            print(f"  + {p}")
        return
 
    # ------------------------------------------------------------------
    # Inject dates
    # ------------------------------------------------------------------
    updated  = 0
    skipped  = 0
    no_date  = 0
    errors   = 0
 
    for page_rel in sorted(affected_pages):
        page_rel  = page_rel.replace("\\", "/")
        page_abs  = os.path.join(repo_root, page_rel)
        deps      = dep_map.get(page_rel, [])
 
        if not os.path.isfile(page_abs):
            print(f"  ⚠️  {page_rel} — file not found, skipping")
            errors += 1
            continue
 
        # Get most recent date in one git log call
        date_str = get_latest_date_for_page(repo_root, page_rel, deps)
 
        if not date_str:
            print(f"  ⚠️  {page_rel} — no git history, skipping")
            no_date += 1
            continue
 
        # Read file and check existing date
        try:
            with open(page_abs, "r", encoding="utf-8") as f:
                content = f.read()
        except (OSError, UnicodeDecodeError) as e:
            print(f"  ⚠️  {page_rel} — read error: {e}")
            errors += 1
            continue
 
        existing = read_existing_date(content)
        if existing == date_str:
            skipped += 1
            continue
 
        # Inject the date
        new_content = inject_date(content, date_str)
 
        try:
            with open(page_abs, "w", encoding="utf-8") as f:
                f.write(new_content)
        except OSError as e:
            print(f"  ⚠️  {page_rel} — write error: {e}")
            errors += 1
            continue
 
        dep_count = len(deps)
        dep_note  = f" (+ {dep_count} dep(s))" if dep_count else ""
        print(f"  ✅ {page_rel}{dep_note} → {date_str}")
        updated += 1
 
    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    print(f"\n{'─' * 50}")
    print(f"✔  Updated : {updated}")
    print(f"·  Skipped : {skipped} (date already current)")
    print(f"⚠️  No date : {no_date}")
    print(f"❌ Errors  : {errors}")
 
 
if __name__ == "__main__":
    main()