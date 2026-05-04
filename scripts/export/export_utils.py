"""
export_utils.py

Shared utility functions for the Agora docs export pipeline.
Imported by bulk_export.py, smart_export.py, and add_docs_index.py.

All scripts in scripts/export/ should import from here rather than
duplicating these functions.
"""

import os
import re
import subprocess
import yaml
from datetime import datetime

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Folders to skip when walking the docs tree as pages.
# Files inside these dirs are still resolved as import dependencies.
SKIP_FOLDERS = {"shared", ".github", "use-cases", "assets"}

# Display names for known platform identifiers.
PLATFORM_DISPLAY_NAMES = {
    "android":      "Android",
    "ios":          "iOS",
    "web":          "Web",
    "flutter":      "Flutter",
    "react-native": "React Native",
    "unity":        "Unity",
    "windows":      "Windows",
    "macos":        "macOS",
    "electron":     "Electron",
}

# ---------------------------------------------------------------------------
# Products.js helper
# ---------------------------------------------------------------------------

def load_product_platforms(products_file: str) -> dict:
    """
    Parse products.js and return { productId: [platforms...] }.

    Parameters
    ----------
    products_file : str
        Absolute path to data/v2/products.js.

    Returns
    -------
    dict
        Mapping of product ID strings to lists of platform strings.
    """
    with open(products_file, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(
        r"id:\s*'([^']+)'.*?platforms:\s*{[^}]*latest:\s*\[([^\]]*)\]",
        re.DOTALL,
    )
    mapping = {}
    for match in pattern.finditer(content):
        product_id = match.group(1)
        platforms_str = match.group(2)
        platforms = re.findall(r"'([^']+)'", platforms_str)
        mapping[product_id] = platforms
    return mapping


# ---------------------------------------------------------------------------
# Frontmatter helper
# ---------------------------------------------------------------------------

def parse_frontmatter(file_path: str) -> dict:
    """
    Extract the YAML frontmatter dict from an .mdx or .md file.

    Returns an empty dict if no frontmatter is found or if parsing fails.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except (OSError, UnicodeDecodeError):
        return {}

    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?", content, re.DOTALL)
    if not match:
        return {}
    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}


# ---------------------------------------------------------------------------
# Path helpers
# ---------------------------------------------------------------------------

def should_skip(path: str) -> bool:
    """
    Return True if the given path falls inside any folder in SKIP_FOLDERS.

    Works with both forward and backslash separators.
    """
    parts = path.replace("\\", "/").split("/")
    return any(p in SKIP_FOLDERS for p in parts)


def get_exported_from_url(mdx_file: str, docs_folder: str, is_help: bool = False) -> str:
    """
    Generate the canonical docs.agora.io URL for a source MDX file.

    Parameters
    ----------
    mdx_file : str
        Absolute path to the source .mdx file.
    docs_folder : str
        Absolute path to the Docs root folder (parent of docs/ submodule).
    is_help : bool
        True when processing files from docs-help/ rather than docs/.
    """
    if is_help:
        docs_path = os.path.join(docs_folder, "docs-help")
        rel_path = os.path.relpath(mdx_file, docs_path)
        normalized_path = rel_path.replace(os.sep, "/")
        if normalized_path.endswith(".mdx"):
            normalized_path = normalized_path[:-4]
        return f"https://docs.agora.io/en/help/{normalized_path}"
    else:
        docs_path = os.path.join(docs_folder, "docs")
        rel_path = os.path.relpath(mdx_file, docs_path)
        normalized_path = rel_path.replace(os.sep, "/")
        if normalized_path.endswith(".mdx"):
            normalized_path = normalized_path[:-4]
        return f"https://docs.agora.io/en/{normalized_path}"


# ---------------------------------------------------------------------------
# mdx2md runner
# ---------------------------------------------------------------------------

def run_mdx2md(
    mdx_file: str,
    platform: str,
    output_file: str,
    docs_folder: str,
    failed_exports: list,
    scripts_dir: str = None,
    images_dir: str = None,
) -> bool:
    if scripts_dir is None:
        scripts_dir = os.path.dirname(os.path.abspath(__file__))

    mdx2md_path = os.path.join(scripts_dir, "mdx2md.py")

    cmd = ["python", mdx2md_path, "--mdxPath", mdx_file]
    if platform:
        cmd.extend(["--platform", platform])
    cmd.extend(["--output-file", output_file])
    cmd.extend(["--docs-folder", docs_folder])
    if images_dir:
        cmd.extend(["--images-dir", images_dir])

    print("Running:", " ".join(cmd))

    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError as e:
        failed_exports.append({
            "file":        mdx_file,
            "platform":    platform,
            "output":      output_file,
            "command":     " ".join(cmd),
            "return_code": e.returncode,
            "stdout":      e.stdout or "No stdout",
            "stderr":      e.stderr or "No stderr",
        })
        print(f"❌ FAILED: {mdx_file} (platform: {platform or 'none'}) - Exit code: {e.returncode}")
        if e.stderr:
            print(f"   Error: {e.stderr.strip()[:200]}...")
        return False
    except Exception as e:
        failed_exports.append({
            "file":        mdx_file,
            "platform":    platform,
            "output":      output_file,
            "command":     " ".join(cmd),
            "return_code": "N/A",
            "stdout":      "N/A",
            "stderr":      str(e),
        })
        print(f"❌ FAILED: {mdx_file} (platform: {platform or 'none'}) - Exception: {e}")
        return False


# ---------------------------------------------------------------------------
# Platform index file
# ---------------------------------------------------------------------------

def create_platform_index_file(
    mdx_file: str,
    platforms: list,
    output_dir: str,
    base_name: str,
    docs_folder: str,
) -> bool:
    """
    Create a platform selector index .md file that links to all
    platform-specific variants of a page.

    Parameters
    ----------
    mdx_file : str
        Absolute path to the source .mdx file.
    platforms : list
        List of platform strings for which exports succeeded.
    output_dir : str
        Absolute path to the output directory for this page.
    base_name : str
        Filename stem of the page (without extension).
    docs_folder : str
        Absolute path to the Docs root folder.
    """
    try:
        fm = parse_frontmatter(mdx_file)
        title = fm.get("title", "Documentation")
        description = fm.get("description", "")
        sidebar_position = fm.get("sidebar_position")

        exported_from = get_exported_from_url(mdx_file, docs_folder, is_help=False)

        index_frontmatter = {
            "title":            title,
            "platform_selector": False,
            "exported_from":    exported_from,
            "exported_on":      datetime.utcnow().isoformat() + "Z",
            "exported_file":    f"{base_name}.md",
        }
        if description:
            index_frontmatter["description"] = description
        if sidebar_position is not None:
            index_frontmatter["sidebar_position"] = sidebar_position

        frontmatter_yaml = yaml.safe_dump(index_frontmatter, sort_keys=False).strip()

        # AI navigation directive
        path_after_en = exported_from.split("/en/", 1)[-1]
        product_slug = path_after_en.split("/")[0]
        directive = (
            f"> For a complete site index fetch https://docs.agora.io/llms.txt."
            f" For all pages in this product fetch"
            f" https://docs.agora.io/en/{product_slug}/overview/product-overview.md"
        )

        index_content = (
            f"---\n{frontmatter_yaml}\n---\n\n"
            f"{directive}\n\n"
            f"# {title}\n\n"
            f"Select your platform:\n\n"
        )

        for platform in sorted(platforms):
            display_name = PLATFORM_DISPLAY_NAMES.get(platform, platform.title())
            platform_file = f"{base_name}_{platform}.md"
            index_content += f"- [{display_name}](./{platform_file})\n"

        index_file_path = os.path.join(output_dir, f"{base_name}.md")
        with open(index_file_path, "w", encoding="utf-8") as f:
            f.write(index_content)

        print(f"✅ Created platform index: {index_file_path}")
        return True

    except Exception as e:
        print(f"❌ Error creating platform index for {mdx_file}: {e}")
        return False


# ---------------------------------------------------------------------------
# Error log
# ---------------------------------------------------------------------------

def write_error_log(failed_exports: list, output_base: str) -> None:
    """
    Write a detailed error log to export_errors.log in the output directory.

    Does nothing if failed_exports is empty.
    """
    if not failed_exports:
        return

    log_file = os.path.join(output_base, "export_errors.log")
    with open(log_file, "w", encoding="utf-8") as f:
        f.write(f"Export Error Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 80 + "\n\n")

        for i, error in enumerate(failed_exports, 1):
            f.write(f"Error #{i}:\n")
            f.write(f"  File:        {error['file']}\n")
            f.write(f"  Platform:    {error['platform'] or 'none'}\n")
            f.write(f"  Output:      {error['output']}\n")
            f.write(f"  Return Code: {error['return_code']}\n")
            f.write(f"  Command:     {error['command']}\n")
            f.write(f"  STDOUT:      {error['stdout']}\n")
            f.write(f"  STDERR:      {error['stderr']}\n")
            f.write("-" * 40 + "\n\n")

    print(f"📋 Detailed error log written to: {log_file}")