"""
bulk_export.py

Walks the entire docs folder and exports every .mdx page to .md.
For smart incremental exports (only files changed since last run),
use smart_export.py instead.

Usage:
    python bulk_export.py --docs-folder D:/Git/AgoraDocs/Docs
    python bulk_export.py --docs-folder D:/Git/AgoraDocs/Docs --process-help
    python bulk_export.py --docs-folder D:/Git/AgoraDocs/Docs --start-folder conversational-ai
"""

import os
import argparse

from export_utils import (
    load_product_platforms,
    parse_frontmatter,
    should_skip,
    run_mdx2md,
    create_platform_index_file,
    write_error_log,
)

# ---------------------------------------------------------------------------
# Optional dependency: docs index injection
# ---------------------------------------------------------------------------
# add_docs_index.py must be in the same directory as bulk_export.py.
# If absent, the rest of bulk_export works normally.

try:
    from add_docs_index import add_docs_index_for_product
    _DOCS_INDEX_AVAILABLE = True
except ImportError:
    _DOCS_INDEX_AVAILABLE = False


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Export all Agora MDX docs to plain markdown."
    )
    parser.add_argument(
        "--docs-folder",
        required=True,
        help="Path to the Docs root folder, e.g. D:/Git/AgoraDocs/Docs",
    )
    parser.add_argument(
        "--start-folder",
        default="",
        help="Optional subfolder inside docs/ to start from (default: whole docs)",
    )
    parser.add_argument(
        "--output-dir",
        default="output",
        help="Base output folder for generated .md files (default: output)",
    )
    parser.add_argument(
        "--skip-platform-index",
        action="store_true",
        help="Skip creating platform index files",
    )
    parser.add_argument(
        "--continue-on-error",
        action="store_true",
        help="Continue processing even when individual exports fail (default behavior)",
    )
    parser.add_argument(
        "--process-help",
        action="store_true",
        help="Process docs-help/ instead of docs/ (no platform processing)",
    )
    parser.add_argument(
        "--no-overview-index",
        action="store_true",
        help="Skip injecting a documentation index into product-overview.md files",
    )
    args = parser.parse_args()

    docs_folder = os.path.abspath(args.docs_folder)
    output_base = os.path.abspath(args.output_dir)

    # Derive images output directory from output_base
    images_dir = os.path.normpath(os.path.join(output_base, "..", "images"))

    # Resolve mdx2md.py location (same directory as this script)
    scripts_dir = os.path.dirname(os.path.abspath(__file__))

    # Overview index injection
    inject_overview_index = not args.no_overview_index
    if inject_overview_index and not _DOCS_INDEX_AVAILABLE:
        print(
            "⚠️  add_docs_index.py not found alongside bulk_export.py — "
            "overview index injection will be skipped. "
            "Place add_docs_index.py in the same directory to enable it, "
            "or pass --no-overview-index to suppress this warning."
        )
        inject_overview_index = False

    if args.process_help:
        start_path = os.path.join(docs_folder, "docs-help", args.start_folder)
        product_platforms = {}
    else:
        start_path = os.path.join(docs_folder, "docs", args.start_folder)
        products_file = os.path.join(docs_folder, "data", "v2", "products.js")
        product_platforms = load_product_platforms(products_file)

    failed_exports = []

    print(f"Mode: {'Help files' if args.process_help else 'Documentation'}")
    if not args.process_help:
        print(f"Loaded product → platforms mapping from {products_file}")
    print(f"Starting export from: {start_path}")
    print(f"Output directory: {output_base}")
    print(f"Platform processing: {'Disabled' if args.process_help else 'Enabled'}")
    print(f"Platform index creation: {'Disabled' if args.skip_platform_index or args.process_help else 'Enabled'}")
    print(f"Overview index injection: {'Disabled' if not inject_overview_index else 'Enabled'}")
    print(f"Continue on error: {'Enabled' if args.continue_on_error else 'Enabled (default)'}")
    print("-" * 60)

    processed_files = 0
    successful_exports = 0
    index_files_created = 0
    overview_indexes_injected = 0

    if args.process_help:
        # Help mode: simple processing, no products or overview index
        for root, _, files in os.walk(start_path):
            for filename in files:
                if not (filename.endswith(".mdx") or filename.endswith(".md")):
                    continue

                mdx_file = os.path.join(root, filename)
                if should_skip(mdx_file):
                    continue

                rel_path = os.path.relpath(mdx_file, os.path.join(docs_folder, "docs-help"))
                output_dir = os.path.join(output_base, "help", os.path.dirname(rel_path))
                os.makedirs(output_dir, exist_ok=True)

                base_name = os.path.splitext(os.path.basename(mdx_file))[0]
                output_file = os.path.join(output_dir, f"{base_name}.md")
                processed_files += 1

                if run_mdx2md(mdx_file, None, output_file, docs_folder, failed_exports, scripts_dir, images_dir):
                    successful_exports += 1

    else:
        # Docs mode: walk per product, flush overview index at product boundaries
        current_product_id = None
        current_output_product_dir = None
        current_platforms = []
        current_source_product_dir = None

        def flush_overview_index():
            if not inject_overview_index or current_product_id is None:
                return
            print(f"\n📋 Injecting documentation index for: {current_product_id}")
            ok = add_docs_index_for_product(
                product_id=current_product_id,
                source_product_dir=current_source_product_dir,
                output_product_dir=current_output_product_dir,
                platforms=current_platforms,
            )
            nonlocal overview_indexes_injected
            if ok:
                overview_indexes_injected += 1

        for root, _, files in os.walk(start_path):
            for filename in files:
                if not (filename.endswith(".mdx") or filename.endswith(".md")):
                    continue

                mdx_file = os.path.join(root, filename)
                if should_skip(mdx_file):
                    continue

                rel_path = os.path.relpath(mdx_file, os.path.join(docs_folder, "docs"))
                parts = rel_path.replace("\\", "/").split("/")
                product_id = parts[0]

                if product_id not in product_platforms:
                    print(f"⚠️ Skipping {mdx_file}, no product mapping")
                    continue

                # Detect product boundary
                if product_id != current_product_id:
                    flush_overview_index()
                    current_product_id = product_id
                    current_platforms = product_platforms[product_id]
                    current_output_product_dir = os.path.normpath(
                        os.path.join(output_base, product_id)
                    )
                    current_source_product_dir = os.path.normpath(
                        os.path.join(docs_folder, "docs", product_id)
                    )

                platforms = product_platforms[product_id]
                fm = parse_frontmatter(mdx_file)
                excluded = fm.get("excluded_platforms", [])
                platform_selector = fm.get("platform_selector", True)

                if not platforms and platform_selector:
                    platform_selector = False

                output_dir = os.path.join(output_base, os.path.dirname(rel_path))
                os.makedirs(output_dir, exist_ok=True)

                base_name = os.path.splitext(os.path.basename(mdx_file))[0]

                if not platform_selector:
                    output_file = os.path.join(output_dir, f"{base_name}.md")
                    processed_files += 1
                    if run_mdx2md(mdx_file, None, output_file, docs_folder, failed_exports, scripts_dir, images_dir):
                        successful_exports += 1
                else:
                    successful_platforms = []

                    for p in platforms:
                        if p in excluded:
                            print(f"  └─ Skipping {p} (excluded)")
                            continue

                        output_file = os.path.join(output_dir, f"{base_name}_{p}.md")
                        processed_files += 1

                        if run_mdx2md(mdx_file, p, output_file, docs_folder, failed_exports, scripts_dir, images_dir):
                            successful_exports += 1
                            successful_platforms.append(p)

                    if not args.skip_platform_index and len(successful_platforms) > 1:
                        if create_platform_index_file(mdx_file, successful_platforms, output_dir, base_name, docs_folder):
                            index_files_created += 1

        # Flush index for the final product
        flush_overview_index()

    write_error_log(failed_exports, output_base)

    print("-" * 60)
    print("📊 Export Summary:")
    print(f"   📄 Total exports attempted: {processed_files}")
    print(f"   ✅ Successful exports: {successful_exports}")
    print(f"   ❌ Failed exports: {len(failed_exports)}")
    if not args.process_help:
        print(f"   📑 Platform index files created: {index_files_created}")
        if inject_overview_index:
            print(f"   📋 Overview indexes injected: {overview_indexes_injected}")

    if failed_exports:
        print("\n❌ Failed Exports:")
        for error in failed_exports:
            platform_info = f" (platform: {error['platform']})" if error['platform'] else ""
            print(f"   • {os.path.basename(error['file'])}{platform_info}")
        print(f"\n📋 See export_errors.log in {output_base} for detailed error information")
        print("🔧 Common fixes:")
        print("   • Check if product/platform dictionaries are missing keys")
        print("   • Verify all imported .mdx files exist")
        print("   • Check for syntax errors in MDX files")
        print("   • Ensure all required assets/images are available")
    else:
        print("\n🎉 All exports completed successfully!")


if __name__ == "__main__":
    main()