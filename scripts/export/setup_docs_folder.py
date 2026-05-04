#!/usr/bin/env python3
"""
setup_docs_folder.py

Creates a temporary parent directory structure that the export scripts
expect, regardless of whether they are running locally from Docs-Source
or in CI.

The export scripts (build_dep_map.py, smart_export.py, bulk_export.py)
expect a --docs-folder argument pointing to a directory with this layout:

    <docs-folder>/
    ├── docs/          ← symlink (or junction on Windows) to the repo root
    └── data/
        └── v2/
            └── products.js

This script:
1. Creates <repo-root>/../agora-docs-tmp/
2. Creates a symlink/junction: agora-docs-tmp/docs -> <repo-root>
3. Copies products.js into agora-docs-tmp/data/v2/products.js
4. Prints the docs-folder path so it can be captured by the caller

Usage (local):
    python scripts/export/setup_docs_folder.py \\
        --products-file D:/Git/AgoraDocs/Docs/data/v2/products.js

    # Capture the output path in bash
    DOCS_FOLDER=$(python scripts/export/setup_docs_folder.py \\
        --products-file D:/Git/AgoraDocs/Docs/data/v2/products.js)

Usage (CI — products.js already fetched into data/v2/):
    DOCS_FOLDER=$(python scripts/export/setup_docs_folder.py)

    # Or with explicit products file location
    DOCS_FOLDER=$(python scripts/export/setup_docs_folder.py \\
        --products-file data/v2/products.js)
"""

import os
import sys
import shutil
import argparse

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Fixed name for the temp parent directory, created one level above the repo root
TEMP_DIR_NAME = "agora-docs-tmp"


# ---------------------------------------------------------------------------
# Platform-aware symlink / junction
# ---------------------------------------------------------------------------

def create_link(source: str, target: str) -> None:
    """
    Create a symlink (Unix) or directory junction (Windows) from target -> source.
    Removes any existing link or directory at target first.
    """
    if os.path.exists(target) or os.path.islink(target):
        if os.path.islink(target):
            os.unlink(target)
        elif os.path.isdir(target):
            # On Windows a junction appears as a directory
            os.rmdir(target)

    if os.name == "nt":
        # Windows: use mklink /J for directory junctions (no admin required)
        import subprocess
        result = subprocess.run(
            ["cmd", "/c", "mklink", "/J", target, source],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            raise RuntimeError(
                f"Failed to create junction {target} -> {source}:\n{result.stderr}"
            )
    else:
        os.symlink(source, target)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Set up temporary docs-folder structure for export scripts."
    )
    parser.add_argument(
        "--products-file",
        default=None,
        help=(
            "Path to products.js. "
            "Defaults to data/v2/products.js relative to the repo root, "
            "which is where the CI workflow fetches it."
        ),
    )
    parser.add_argument(
        "--temp-dir-name",
        default=TEMP_DIR_NAME,
        help=f"Name of the temp directory (default: {TEMP_DIR_NAME})",
    )
    args = parser.parse_args()

    # Repo root = two levels up from this script (scripts/export/setup_docs_folder.py)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.normpath(os.path.join(script_dir, "..", ".."))

    # Temp parent dir sits one level above the repo root
    temp_dir = os.path.normpath(
        os.path.join(repo_root, "..", args.temp_dir_name)
    )

    # Resolve products.js path
    if args.products_file:
        products_src = os.path.abspath(args.products_file)
    else:
        # Default: data/v2/products.js inside the repo (CI fetches it here)
        products_src = os.path.join(repo_root, "data", "v2", "products.js")

    if not os.path.isfile(products_src):
        print(
            f"❌ products.js not found at: {products_src}\n"
            f"   Pass --products-file to specify the correct path.",
            file=sys.stderr,
        )
        sys.exit(1)

    # ------------------------------------------------------------------
    # Create temp directory structure
    # ------------------------------------------------------------------
    os.makedirs(temp_dir, exist_ok=True)

    # Create docs/ link -> repo root
    docs_link = os.path.join(temp_dir, "docs")
    try:
        create_link(repo_root, docs_link)
    except RuntimeError as e:
        print(f"❌ Failed to create docs link: {e}", file=sys.stderr)
        sys.exit(1)

    # Copy products.js into data/v2/
    products_dest_dir = os.path.join(temp_dir, "data", "v2")
    os.makedirs(products_dest_dir, exist_ok=True)
    products_dest = os.path.join(products_dest_dir, "products.js")
    shutil.copy2(products_src, products_dest)

    # Also copy dep-map.json if it exists in the repo
    dep_map_src = os.path.join(repo_root, "data", "dep-map.json")
    if os.path.isfile(dep_map_src):
        data_dest_dir = os.path.join(temp_dir, "data")
        os.makedirs(data_dest_dir, exist_ok=True)
        shutil.copy2(dep_map_src, os.path.join(data_dest_dir, "dep-map.json"))

    # ------------------------------------------------------------------
    # Print the docs-folder path — this is what callers capture
    # ------------------------------------------------------------------
    # Normalize to forward slashes for cross-platform consistency
    print(temp_dir.replace("\\", "/"))


if __name__ == "__main__":
    main()