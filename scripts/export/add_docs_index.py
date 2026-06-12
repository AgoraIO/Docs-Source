"""
add_docs_index.py

Injects a "## Documentation index" section into product-overview.md files.

Driven entirely from the source docs folder, following the same logic as
bulk_export.py to determine platform handling per product and per file.

For each product:
  - Walks <docs-folder>/docs/<product>/ for .mdx source files
  - Reads _category_.json for category labels and positions
  - Reads .mdx frontmatter for sidebar_position, title, platform_selector,
    and excluded_platforms
  - Uses products.js to determine whether a product has platforms defined
  - Derives the output .md filename using the same rules as bulk_export.py:
      - Platform-specific file  → base_name_<platform>.md (one per platform)
      - Platform-agnostic file  → base_name.md
  - Always links to base_name.md (the platform-selector index for
    multi-platform pages, or the direct file for platform-agnostic pages)
  - Groups entries by category, ordered by _category_.json position
  - Orders files within each category by sidebar_position, then alphabetically
  - Skips product-overview.mdx itself
  - Skips shared/, .github/, use-cases/, assets/ folders (same as bulk_export)
  - Appends the index under ## Documentation index in the output
    product-overview.md file

Usage (standalone):
    python add_docs_index.py --docs-folder /path/to/Docs --output-dir output
    python add_docs_index.py --docs-folder /path/to/Docs --output-dir output --product conversational-ai
    python add_docs_index.py --docs-folder /path/to/Docs --output-dir output --dry-run

Can also be imported and called from bulk_export.py:
    from add_docs_index import add_docs_index_for_product
    add_docs_index_for_product(
        product_id="conversational-ai",
        source_product_dir="/path/to/Docs/docs/conversational-ai",
        output_product_dir="output/conversational-ai",
        platforms=["android", "ios", "web"],  # from products.js; [] if none
        dry_run=False,
    )
"""

import os
import re
import json
import argparse

from export_utils import (
    SKIP_FOLDERS,
    load_product_platforms,
    parse_frontmatter,
    should_skip,
)


# ---------------------------------------------------------------------------
# Category helper
# ---------------------------------------------------------------------------

def load_category(folder: str) -> dict:
    """
    Load _category_.json from a folder.
    Returns a dict with 'label' and 'position'.
    Falls back to title-cased folder name and position 999 if absent.
    """
    category_file = os.path.join(folder, "_category_.json")
    defaults = {
        "label": os.path.basename(folder).replace("-", " ").title(),
        "position": 999,
    }

    if not os.path.isfile(category_file):
        return defaults

    try:
        with open(category_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        return {
            "label": data.get("label", defaults["label"]),
            "position": data.get("position", defaults["position"]),
        }
    except (json.JSONDecodeError, OSError):
        return defaults


# ---------------------------------------------------------------------------
# Path helpers
# ---------------------------------------------------------------------------

def build_rel_link(
    mdx_abs: str,
    base_name: str,
    source_product_dir: str,
    output_product_dir: str,
) -> str:
    """
    Build the relative link from the output overview directory to the output
    .md file that corresponds to this source .mdx file.

    The link always points to base_name.md — either the platform-selector
    index (for platform-specific pages) or the direct file (for
    platform-agnostic pages). This matches what bulk_export.py produces.

    The output file mirrors the source subdirectory structure:
        source: <source_product_dir>/get-started/quickstart.mdx
        output: <output_product_dir>/get-started/quickstart.md

    The link is relative from the overview folder, since product-overview.md
    lives in <output_product_dir>/overview/.
    """
    # Subdirectory of the source file relative to the product root
    rel_dir = os.path.relpath(os.path.dirname(mdx_abs), source_product_dir)

    # Absolute path of the output .md file
    output_file_abs = os.path.normpath(
        os.path.join(output_product_dir, rel_dir, f"{base_name}.md")
    )

    # product-overview.md lives in <output_product_dir>/overview/
    overview_dir = os.path.normpath(os.path.join(output_product_dir, "overview"))

    rel_link = os.path.relpath(output_file_abs, overview_dir)
    return rel_link.replace("\\", "/")


# ---------------------------------------------------------------------------
# Core: build index tree for one product
# ---------------------------------------------------------------------------

def get_or_create_node(tree: dict, folder_abs: str, source_product_dir: str) -> dict:
    """
    Return the tree node for folder_abs, creating all ancestor nodes along
    the path from source_product_dir if they do not yet exist.

    Each node has the shape:
        {
            "label":    str,       # from _category_.json
            "position": float,     # from _category_.json
            "entries":  list,      # file entries at this level
            "children": dict,      # subfolder_abs -> child node
        }

    Nodes are created lazily so that folders with no .mdx files (but with
    sub-folders that do have files) still appear correctly in the tree.
    """
    # Build the chain of folders from product root down to folder_abs
    rel = os.path.relpath(folder_abs, source_product_dir)
    parts = rel.replace("\\", "/").split("/") if rel != "." else []

    node = tree
    current_path = source_product_dir

    for part in parts:
        current_path = os.path.join(current_path, part)
        current_path_norm = os.path.normpath(current_path)

        if current_path_norm not in node["children"]:
            cat_info = load_category(current_path_norm)
            node["children"][current_path_norm] = {
                "label": cat_info["label"],
                "position": cat_info["position"],
                "entries": [],
                "children": {},
            }

        node = node["children"][current_path_norm]

    return node


def collect_entries(
    source_product_dir: str,
    output_product_dir: str,
    platforms: list,
) -> dict:
    """
    Walk source_product_dir and return a tree of nodes representing the full
    folder hierarchy, mirroring the Docusaurus sidebar structure.

    Tree shape (root node — not rendered itself):
        {
            "label":    "",
            "position": 0,
            "entries":  [],        # files at the product root level (rare)
            "children": {
                "/abs/path/overview": {
                    "label":    "Overview",
                    "position": 1,
                    "entries":  [
                        {"title": "Release notes", "rel_link": "...",
                         "sort_key": (3.0, "release-notes.mdx")},
                        ...
                    ],
                    "children": {},
                },
                "/abs/path/rest-api": {
                    "label":    "REST API",
                    "position": 5,
                    "entries":  [...],
                    "children": {
                        "/abs/path/rest-api/agent": {
                            "label":    "Agent",
                            "position": 1,
                            "entries":  [...],
                            "children": {},
                        },
                        ...
                    },
                },
                ...
            },
        }

    Mirrors bulk_export.py logic for platform_selector handling:
    - platform_selector defaults to True but is forced False when the product
      has no platforms defined in products.js.
    - We always link to base_name.md regardless — either the platform-selector
      index or the direct platform-agnostic file.
    """
    source_product_dir = os.path.normpath(source_product_dir)

    # Root sentinel node — represents the product folder itself, not rendered
    root = {
        "label": "",
        "position": 0,
        "entries": [],
        "children": {},
    }

    for current_dir, dirs, files in os.walk(source_product_dir):
        # Deterministic traversal
        dirs.sort()

        # Skip excluded folders
        if should_skip(current_dir):
            # Also prevent os.walk from descending into them
            dirs[:] = [d for d in dirs if d not in SKIP_FOLDERS]
            continue

        # Prune skip folders from further traversal
        dirs[:] = [d for d in dirs if d not in SKIP_FOLDERS]

        mdx_files = sorted(
            f for f in files
            if f.endswith(".mdx") or f.endswith(".md")
        )
        if not mdx_files:
            continue

        # Get (or create) the node for this directory
        node = get_or_create_node(root, current_dir, source_product_dir)

        for filename in mdx_files:
            mdx_abs = os.path.normpath(os.path.join(current_dir, filename))
            base_name = os.path.splitext(filename)[0]

            # Skip the product-overview source file itself
            if base_name == "product-overview":
                continue

            # Parse source frontmatter — same fields bulk_export.py reads
            fm = parse_frontmatter(mdx_abs)
            title = fm.get("title", "") or ""
            description = fm.get("description", "") or ""
            sidebar_position = fm.get("sidebar_position", 999)

            # Fall back title to humanised filename
            if not title:
                title = base_name.replace("-", " ").replace("_", " ").title()

            # Normalise sidebar_position for sorting
            try:
                pos = float(sidebar_position)
            except (TypeError, ValueError):
                pos = 999.0

            # Derive the relative link to the output file
            rel_link = build_rel_link(
                mdx_abs, base_name, source_product_dir, output_product_dir
            )

            # Collapse multiline YAML descriptions (block scalars) to a
            # single line, normalising internal whitespace
            description = " ".join(description.split())

            node["entries"].append({
                "title": title,
                "description": description,
                "rel_link": rel_link,
                "sort_key": (pos, filename),
            })

    # Sort entries within every node (recursive)
    def sort_node(node: dict):
        node["entries"].sort(key=lambda e: e["sort_key"])
        for child in node["children"].values():
            sort_node(child)

    sort_node(root)
    return root


def sorted_children(node: dict) -> list:
    """Return a node's children sorted by position then label."""
    return sorted(
        node["children"].values(),
        key=lambda c: (c["position"], c["label"]),
    )


# ---------------------------------------------------------------------------
# Markdown rendering
# ---------------------------------------------------------------------------

def render_node(node: dict, indent: int, lines: list):
    """
    Recursively render a tree node into lines at the given indent level.

    indent=0 produces top-level bullets:
        - **Overview**
          - [Release notes](./release-notes.md)

    indent=1 produces nested bullets under a parent:
          - **Agent**
            - [Interrupt](../rest-api/agent/interrupt.md)
    """
    prefix = "  " * indent

    # Render the category label as a bold bullet
    lines.append(f"{prefix}- **{node['label']}**")

    child_prefix = "  " * (indent + 1)

    # File entries at this level
    for entry in node["entries"]:
        line = f"{child_prefix}- [{entry['title']}]({entry['rel_link']})"
        if entry.get("description"):
            line += f": {entry['description']}"
        lines.append(line)

    # Recurse into child folders, sorted by position then label
    for child in sorted_children(node):
        render_node(child, indent + 1, lines)


def build_index_markdown(root: dict) -> str:
    """
    Render the full documentation index from the root tree node.

    ## Documentation index

    - **Overview**
      - [Release notes](./release-notes.md)
    - **REST API**
      - **Agent**
        - [Interrupt the agent](../rest-api/agent/interrupt.md)
        - [Join](../rest-api/agent/join.md)
      - **Channel**
        - [List agents](../rest-api/channel/list.md)
    - **Get started**
      - [SDK quickstart](../get-started/get-started-sdk.md)
    ...
    """
    top_level = sorted_children(root)
    # Also include any files sitting directly at the product root
    root_entries = root.get("entries", [])

    if not top_level and not root_entries:
        return ""

    lines = ["## Documentation index", ""]

    # Files at the product root (uncommon but handled)
    for entry in root_entries:
        line = f"- [{entry['title']}]({entry['rel_link']})"
        if entry.get("description"):
            line += f": {entry['description']}"
        lines.append(line)

    # Top-level category nodes
    for child in top_level:
        render_node(child, indent=0, lines=lines)

    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# File injection
# ---------------------------------------------------------------------------

def inject_index_into_file(
    file_path: str, index_markdown: str, dry_run: bool = False
) -> bool:
    """
    Append index_markdown to file_path.
    If a ## Documentation index section already exists, replace it.
    Returns True on success.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except (OSError, IOError) as e:
        print(f"  ❌ Could not read {file_path}: {e}")
        return False

    # Remove any existing index section
    content = re.sub(r"\n## Documentation index\n.*$", "", content, flags=re.DOTALL)

    # Ensure exactly one blank line before the new section
    content = content.rstrip("\n") + "\n\n"
    content += index_markdown

    if dry_run:
        print(f"  [dry-run] Would write index to {file_path}")
        return True

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    except (OSError, IOError) as e:
        print(f"  ❌ Could not write {file_path}: {e}")
        return False


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def add_docs_index_for_product(
    product_id: str,
    source_product_dir: str,
    output_product_dir: str,
    platforms: list,
    dry_run: bool = False,
) -> bool:
    """
    Build and inject a documentation index for one product.

    Parameters
    ----------
    product_id : str
        Product identifier, for example 'conversational-ai'. Used in messages.
    source_product_dir : str
        Absolute path to the source docs folder for this product,
        for example /path/to/Docs/docs/conversational-ai
    output_product_dir : str
        Absolute path to the output folder for this product,
        for example output/conversational-ai
    platforms : list
        List of platform strings from products.js, for example
        ['android', 'ios', 'web']. Pass [] for products with no platforms.
    dry_run : bool
        If True, print what would be done without writing any files.

    Returns True if the overview file was found and updated successfully.
    """
    output_product_dir = os.path.normpath(output_product_dir)

    # Locate the output product-overview.md
    overview_file = None
    for root, _, files in os.walk(output_product_dir):
        for f in files:
            if f == "product-overview.md":
                overview_file = os.path.join(root, f)
                break
        if overview_file:
            break

    if not overview_file:
        print(f"  ⚠️  No product-overview.md found in {output_product_dir}")
        return False

    print(f"  📄 Found overview: {overview_file}")

    categories = collect_entries(
        source_product_dir=os.path.normpath(source_product_dir),
        output_product_dir=output_product_dir,
        platforms=platforms,
    )

    # Tree is empty if the root has no children and no direct entries
    if not categories["children"] and not categories["entries"]:
        print(f"  ⚠️  No index entries found for {product_id}")
        return False

    index_md = build_index_markdown(categories)

    success = inject_index_into_file(overview_file, index_md, dry_run=dry_run)
    if success and not dry_run:
        def count_entries(node):
            return len(node["entries"]) + sum(
                count_entries(c) for c in node["children"].values()
            )
        def count_nodes(node):
            return len(node["children"]) + sum(
                count_nodes(c) for c in node["children"].values()
            )
        total = count_entries(categories)
        groups = count_nodes(categories)
        print(f"  ✅ Injected index ({groups} groups, {total} entries)")

    return success


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Inject a documentation index into product-overview.md files."
    )
    parser.add_argument(
        "--docs-folder",
        required=True,
        help="Path to the Docs root folder (same as bulk_export --docs-folder).",
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        help="Base output directory containing exported .md files "
             "(same as bulk_export --output-dir).",
    )
    parser.add_argument(
        "--product",
        default="",
        help="Optional: process only this product "
             "(for example 'conversational-ai'). "
             "Default: process all products found in products.js.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be done without modifying any files.",
    )
    args = parser.parse_args()

    docs_folder = os.path.abspath(args.docs_folder)
    output_dir = os.path.abspath(args.output_dir)

    if not os.path.isdir(docs_folder):
        print(f"❌ Docs folder not found: {docs_folder}")
        return
    if not os.path.isdir(output_dir):
        print(f"❌ Output directory not found: {output_dir}")
        return

    products_file = os.path.join(docs_folder, "data", "v2", "products.js")
    if not os.path.isfile(products_file):
        print(f"❌ products.js not found at {products_file}")
        return

    product_platforms = load_product_platforms(products_file)

    # Determine which products to process
    if args.product:
        if args.product not in product_platforms:
            print(
                f"⚠️  '{args.product}' not found in products.js — proceeding anyway."
            )
        product_ids = [args.product]
    else:
        product_ids = sorted(product_platforms.keys())

    if args.dry_run:
        print("🔍 Dry run — no files will be modified.\n")

    success_count = 0
    fail_count = 0

    for product_id in product_ids:
        source_product_dir = os.path.join(docs_folder, "docs", product_id)
        output_product_dir = os.path.join(output_dir, product_id)

        # Skip products with no source or no output folder
        if not os.path.isdir(source_product_dir):
            continue
        if not os.path.isdir(output_product_dir):
            continue

        platforms = product_platforms.get(product_id, [])
        print(f"\n📦 Processing: {product_id} ({len(platforms)} platforms)")

        ok = add_docs_index_for_product(
            product_id=product_id,
            source_product_dir=source_product_dir,
            output_product_dir=output_product_dir,
            platforms=platforms,
            dry_run=args.dry_run,
        )

        if ok:
            success_count += 1
        else:
            fail_count += 1

    print("\n" + "-" * 50)
    print(f"✅ Succeeded: {success_count}")
    print(f"❌ Failed / skipped: {fail_count}")


if __name__ == "__main__":
    main()