#!/usr/bin/env python3
"""
build_dep_map.py

Walks the docs submodule and builds a dependency map for every page file.
Each page entry lists all files it depends on transitively — imported MDX/MD
files and referenced images — so that smart_export.py can determine which
pages need re-exporting when any file in their dependency chain changes.

Output: <docs-folder>/data/dep-map.json

Usage:
    python build_dep_map.py --docs-folder D:/Git/AgoraDocs/Docs

    # Rebuild only if dep-map.json is older than 24 hours
    python build_dep_map.py --docs-folder D:/Git/AgoraDocs/Docs --max-age-hours 24

    # Preview without writing
    python build_dep_map.py --docs-folder D:/Git/AgoraDocs/Docs --dry-run
"""

import os
import re
import json
import argparse
import time
from datetime import datetime, timezone

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# Subdirectory names to exclude from page processing.
# Files inside these dirs are still resolved as import/image dependencies.
EXCLUDED_DIRS = {
    ".github",
    ".idea",
    "assets",
    "shared",
    "use-cases",
}

# Import alias mappings: alias prefix -> relative path from docs-submodule root.
# The actual filesystem path is built at runtime from DOCS_SUBMODULE_ROOT.
ALIAS_SUBPATHS = {
    "@docs": "",          # @docs/foo -> <submodule>/foo
    "@site": "..",        # @site/foo -> <docs-folder>/foo
}

# Regex patterns
IMPORT_RE = re.compile(r"""import\s+[^'"]*from\s+['"]([^'"]+)['"]""")
IMAGE_RE  = re.compile(r"""!\[[^\]]*\]\(([^)]+)\)""")

# ---------------------------------------------------------------------------
# Path helpers
# ---------------------------------------------------------------------------

def build_alias_map(docs_submodule_root: str) -> dict:
    """
    Build a dict mapping each alias prefix to an absolute filesystem path.
    """
    alias_map = {}
    for alias, subpath in ALIAS_SUBPATHS.items():
        alias_map[alias] = os.path.normpath(
            os.path.join(docs_submodule_root, subpath)
        )
    return alias_map


def resolve_import(import_path: str, source_file: str, alias_map: dict, docs_submodule_root: str):
    """
    Resolve an import path to an absolute filesystem path.

    Handles:
    - @docs/... and @site/... aliases
    - Relative paths (./  ../)

    Returns None if the path cannot be resolved or the file does not exist.
    """
    resolved = None

    if import_path.startswith("./") or import_path.startswith("../"):
        resolved = os.path.normpath(
            os.path.join(os.path.dirname(source_file), import_path)
        )
    else:
        for alias, target in alias_map.items():
            if import_path.startswith(alias + "/"):
                rel = import_path[len(alias) + 1:]
                resolved = os.path.normpath(os.path.join(target, rel))
                break

    if resolved is None:
        return None

    # If no extension, try common doc extensions
    if not os.path.splitext(resolved)[1]:
        for ext in (".mdx", ".md"):
            candidate = resolved + ext
            if os.path.isfile(candidate):
                return candidate
        return None

    return resolved if os.path.isfile(resolved) else None


def resolve_image(image_path: str, source_file: str, docs_submodule_root: str):
    """
    Resolve an image path to an absolute filesystem path.

    Handles:
    - http/https URLs -> skip (returns None)
    - /images/... absolute paths -> <submodule>/assets/images/...
    - ./  ../ relative paths -> relative to source_file

    Returns None if external, unresolvable, or file does not exist.
    """
    if image_path.startswith("http://") or image_path.startswith("https://"):
        return None

    if image_path.startswith("/"):
        # Absolute path: /images/foo.png -> assets/images/foo.png
        resolved = os.path.normpath(
            os.path.join(docs_submodule_root, "assets", image_path.lstrip("/"))
        )
    else:
        # Relative path: resolve from the containing file
        resolved = os.path.normpath(
            os.path.join(os.path.dirname(source_file), image_path)
        )

    return resolved if os.path.isfile(resolved) else None


def to_rel(abs_path: str, docs_submodule_root: str) -> str:
    """
    Convert an absolute path to a forward-slash path relative to the
    docs submodule root.
    """
    return os.path.relpath(abs_path, docs_submodule_root).replace("\\", "/")


def is_excluded_page(abs_path: str, docs_submodule_root: str) -> bool:
    """
    Return True if the file falls inside any excluded directory and should
    not appear as a page key in the dep map.
    """
    rel = os.path.relpath(abs_path, docs_submodule_root)
    parts = rel.replace("\\", "/").split("/")
    return any(part in EXCLUDED_DIRS for part in parts)


# ---------------------------------------------------------------------------
# Dependency collection
# ---------------------------------------------------------------------------

def collect_deps(
    abs_path: str,
    alias_map: dict,
    docs_submodule_root: str,
    visited: set = None,
) -> set:
    """
    Recursively collect all transitive dependencies of a file:
    - Imported MDX/MD files
    - Referenced images

    Returns a set of absolute paths (excluding the root file itself).
    """
    if visited is None:
        visited = set()

    if abs_path in visited:
        return visited

    visited.add(abs_path)

    try:
        with open(abs_path, "r", encoding="utf-8") as f:
            content = f.read()
    except (OSError, UnicodeDecodeError):
        return visited

    # Resolve imports
    for match in IMPORT_RE.finditer(content):
        import_path = match.group(1)
        resolved = resolve_import(import_path, abs_path, alias_map, docs_submodule_root)
        if resolved and resolved not in visited:
            collect_deps(resolved, alias_map, docs_submodule_root, visited)

    # Resolve images
    for match in IMAGE_RE.finditer(content):
        image_path = match.group(1).strip()
        resolved = resolve_image(image_path, abs_path, docs_submodule_root)
        if resolved and resolved not in visited:
            visited.add(resolved)
            # Images don't have their own imports/images to follow

    return visited


# ---------------------------------------------------------------------------
# File walker
# ---------------------------------------------------------------------------

def collect_page_files(docs_submodule_root: str) -> list:
    """
    Recursively collect all .md/.mdx files under the docs submodule root
    that are not in excluded directories.
    """
    pages = []
    for root, dirs, files in os.walk(docs_submodule_root):
        # Prune excluded dirs from traversal for efficiency,
        # but we still need to visit them for dependency resolution —
        # so we prune only at the top level of the submodule.
        rel_root = os.path.relpath(root, docs_submodule_root)
        if rel_root == ".":
            # At the submodule root: don't prune, but filter results
            pass

        for filename in files:
            if not filename.endswith((".md", ".mdx")):
                continue
            abs_path = os.path.join(root, filename)
            if not is_excluded_page(abs_path, docs_submodule_root):
                pages.append(abs_path)

    return sorted(pages)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def build_dep_map(docs_folder: str, dry_run: bool = False, max_age_hours: float = None) -> dict:
    """
    Build the dependency map and optionally write it to disk.

    Returns the dep map dict.
    """
    docs_submodule_root = os.path.normpath(os.path.join(docs_folder, "docs"))
    output_path = os.path.normpath(os.path.join(docs_folder, "data", "dep-map.json"))

    if not os.path.isdir(docs_submodule_root):
        raise FileNotFoundError(f"Docs submodule not found: {docs_submodule_root}")

    # Check age of existing dep map
    if max_age_hours is not None and os.path.isfile(output_path):
        age_seconds = time.time() - os.path.getmtime(output_path)
        age_hours = age_seconds / 3600
        if age_hours < max_age_hours:
            print(
                f"ℹ  dep-map.json is {age_hours:.1f}h old "
                f"(threshold: {max_age_hours}h) — skipping rebuild."
            )
            with open(output_path, "r", encoding="utf-8") as f:
                return json.load(f)

    alias_map = build_alias_map(docs_submodule_root)

    print(f"📂 Docs submodule : {docs_submodule_root}")
    print(f"📄 Output         : {output_path}")
    print(f"🔍 Scanning pages ...")

    page_files = collect_page_files(docs_submodule_root)
    print(f"   Found {len(page_files)} page files\n")

    dep_map = {}
    errors = []

    for abs_path in page_files:
        page_key = to_rel(abs_path, docs_submodule_root)

        try:
            all_deps = collect_deps(abs_path, alias_map, docs_submodule_root)
            # Remove the page file itself from its own dep list
            all_deps.discard(abs_path)

            dep_list = sorted(
                to_rel(d, docs_submodule_root) for d in all_deps
            )

            dep_map[page_key] = dep_list

            dep_count = len(dep_list)
            if dep_count:
                print(f"  ✅ {page_key} ({dep_count} dep(s))")
            else:
                print(f"  ·  {page_key} (no deps)")

        except Exception as e:
            errors.append((page_key, str(e)))
            print(f"  ⚠️  {page_key} — error: {e}")

    # Build metadata
    output = {
        "_meta": {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "docs_submodule": docs_submodule_root,
            "total_pages": len(dep_map),
            "excluded_dirs": sorted(EXCLUDED_DIRS),
            "errors": errors,
        },
        "pages": dep_map,
    }

    if dry_run:
        print(f"\n🔍 Dry run — dep map not written.")
        print(f"   {len(dep_map)} pages mapped, {len(errors)} error(s).")
    else:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
        print(f"\n✅ dep-map.json written → {output_path}")
        print(f"   {len(dep_map)} pages mapped, {len(errors)} error(s).")

    return output


def main():
    parser = argparse.ArgumentParser(
        description="Build dep-map.json for the Agora docs submodule."
    )
    parser.add_argument(
        "--docs-folder",
        required=True,
        help="Path to the Docs root folder, e.g. D:/Git/AgoraDocs/Docs",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Scan and print results without writing dep-map.json",
    )
    parser.add_argument(
        "--max-age-hours",
        type=float,
        default=None,
        help="Skip rebuild if dep-map.json is newer than this many hours",
    )
    args = parser.parse_args()

    build_dep_map(
        docs_folder=os.path.abspath(args.docs_folder),
        dry_run=args.dry_run,
        max_age_hours=args.max_age_hours,
    )


if __name__ == "__main__":
    main()