#!/usr/bin/env node

/**
 * inject-last-updated.js
 *
 * Injects `last_update.date` into the frontmatter of every doc page under
 * the configured docs root. The date reflects the most recent git commit
 * that touched the page file OR any shared file it imports (recursively).
 *
 * Files in EXCLUDED_DIRS are skipped as pages but are still tracked as
 * dependencies when imported by other pages.
 *
 * Usage:
 *   node scripts/inject-last-updated.js
 *
 * Wire into package.json:
 *   "start": "yarn convert && node scripts/inject-last-updated.js && docusaurus start"
 *   "build": "yarn convert && node scripts/inject-last-updated.js && docusaurus build"
 */

const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");

// ---------------------------------------------------------------------------
// Configuration
// ---------------------------------------------------------------------------

/** Root of the docs folder, relative to this script's location. */
const DOCS_ROOT = path.resolve(__dirname, "../docs");

/** Root of the repo (where .git lives). */
const REPO_ROOT = path.resolve(__dirname, "../docs");

/**
 * Subdirectory names to exclude from page processing.
 * Files inside these dirs are still resolved as import dependencies.
 */
const EXCLUDED_DIRS = [
  ".github",
  ".idea",
  "assets",
  "shared",
  "use-cases",
];

/**
 * Import alias mappings → real filesystem paths.
 * Add or adjust entries to match your tsconfig/docusaurus path aliases.
 */
const ALIASES = {
  "@docs": path.resolve(DOCS_ROOT, "..") + "/docs",
  "@site": path.resolve(DOCS_ROOT, ".."),
};

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

/**
 * Return the most recent git commit date for a file, or null if untracked.
 * @param {string} absPath Absolute path to the file.
 * @returns {Date|null}
 */
function gitDate(absPath) {
  try {
    const rel = path.relative(REPO_ROOT, absPath);
    const out = execSync(`git log -1 --format=%ci -- "${rel}"`, {
      cwd: REPO_ROOT,
      stdio: ["pipe", "pipe", "pipe"],
    })
      .toString()
      .trim();
    return out ? new Date(out) : null;
  } catch {
    return null;
  }
}

/**
 * Resolve an import path found in a source file to an absolute filesystem path.
 * Handles @docs/, @site/, and relative (./  ../) imports.
 * Returns null if the path cannot be resolved.
 *
 * @param {string} importPath  The raw import string, e.g. '@docs/shared/foo.mdx'
 * @param {string} sourceFile  Absolute path of the file containing the import.
 * @returns {string|null}
 */
function resolveImport(importPath, sourceFile) {
  let resolved = null;

  if (importPath.startsWith("./") || importPath.startsWith("../")) {
    resolved = path.resolve(path.dirname(sourceFile), importPath);
  } else {
    for (const [alias, target] of Object.entries(ALIASES)) {
      if (importPath.startsWith(alias + "/")) {
        resolved = path.join(target, importPath.slice(alias.length + 1));
        break;
      }
    }
  }

  if (!resolved) return null;

  // If the path has no extension, try common doc extensions.
  if (!path.extname(resolved)) {
    for (const ext of [".mdx", ".md"]) {
      if (fs.existsSync(resolved + ext)) return resolved + ext;
    }
    return null;
  }

  return fs.existsSync(resolved) ? resolved : null;
}

/**
 * Extract all import paths from the content of an MDX/MD file.
 * Matches:  import Foo from 'path'  and  import Foo from "path"
 *
 * @param {string} content
 * @returns {string[]}
 */
function extractImports(content) {
  const re = /import\s+[^'"]*from\s+['"]([^'"]+)['"]/g;
  const imports = [];
  let match;
  while ((match = re.exec(content)) !== null) {
    imports.push(match[1]);
  }
  return imports;
}

/**
 * Recursively collect all transitive import dependencies of a file.
 * Returns a Set of absolute paths (excluding the root file itself).
 *
 * @param {string} absPath
 * @param {Set<string>} [visited]
 * @returns {Set<string>}
 */
function collectDeps(absPath, visited = new Set()) {
  if (visited.has(absPath)) return visited;
  visited.add(absPath);

  let content;
  try {
    content = fs.readFileSync(absPath, "utf8");
  } catch {
    return visited;
  }

  for (const imp of extractImports(content)) {
    const resolved = resolveImport(imp, absPath);
    if (resolved && !visited.has(resolved)) {
      collectDeps(resolved, visited);
    }
  }

  return visited;
}

/**
 * Given a page file, return the most recent git date across the file
 * and all its transitive import dependencies.
 *
 * @param {string} absPath
 * @returns {Date|null}
 */
function effectiveDate(absPath) {
  const deps = collectDeps(absPath);
  let latest = null;

  for (const dep of deps) {
    const d = gitDate(dep);
    if (d && (!latest || d > latest)) latest = d;
  }

  return latest;
}

/**
 * Format a Date as YYYY-MM-DD.
 * @param {Date} date
 * @returns {string}
 */
function formatDate(date) {
  return date.toISOString().split("T")[0];
}

/**
 * Read the existing last_update.date from frontmatter, if present.
 * Returns null if not found.
 *
 * @param {string} content
 * @returns {string|null}
 */
function readExistingDate(content) {
  const fmMatch = content.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!fmMatch) return null;
  const dateMatch = fmMatch[1].match(/^\s*last_update:\s*\r?\n\s*date:\s*(\S+)/m);
  return dateMatch ? dateMatch[1] : null;
}

/**
 * Write `last_update:\n  date: YYYY-MM-DD` into the frontmatter of content.
 * Replaces an existing last_update block if present, otherwise appends before
 * the closing `---`.
 *
 * @param {string} content
 * @param {string} dateStr  YYYY-MM-DD
 * @returns {string}
 */
function injectDate(content, dateStr) {
  const newBlock = `last_update:\n  date: ${dateStr}`;

  // Replace existing last_update block
  if (/^\s*last_update:\s*\r?\n\s*date:\s*\S+/m.test(content)) {
    return content.replace(
      /^(\s*last_update:\s*\r?\n\s*date:\s*)\S+/m,
      `$1${dateStr}`
    );
  }

  // Replace flat `last_update: value`
  if (/^\s*last_update:\s*\S+/m.test(content)) {
    return content.replace(/^\s*last_update:\s*\S+/m, newBlock);
  }

  // Append before closing ---
  return content.replace(/^(---\r?\n[\s\S]*?)(^---)/m, `$1${newBlock}\n$2`);
}

/**
 * Return true if a file path falls inside any of the excluded directories.
 *
 * @param {string} absPath
 * @returns {boolean}
 */
function isExcluded(absPath) {
  const rel = path.relative(DOCS_ROOT, absPath);
  const parts = rel.split(path.sep);
  return parts.some((part) => EXCLUDED_DIRS.includes(part));
}

/**
 * Recursively collect all .md/.mdx files under a directory.
 *
 * @param {string} dir
 * @returns {string[]}
 */
function collectDocFiles(dir) {
  const results = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      results.push(...collectDocFiles(full));
    } else if (/\.(md|mdx)$/.test(entry.name)) {
      results.push(full);
    }
  }
  return results;
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

async function main() {
  const allFiles = collectDocFiles(DOCS_ROOT);
  const pageFiles = allFiles.filter((f) => !isExcluded(f));

  let updated = 0;
  let skipped = 0;
  let noGit = 0;

  for (const file of pageFiles) {
    const date = effectiveDate(file);

    if (!date) {
      noGit++;
      const rel = path.relative(DOCS_ROOT, file);
      console.log(`  ⚠  ${rel} — no git history, skipping`);
      continue;
    }

    const dateStr = formatDate(date);
    const content = fs.readFileSync(file, "utf8");
    const existing = readExistingDate(content);

    if (existing === dateStr) {
      skipped++;
      continue;
    }

    const updated_content = injectDate(content, dateStr);
    fs.writeFileSync(file, updated_content, "utf8");

    const rel = path.relative(DOCS_ROOT, file);
    const deps = collectDeps(file);
    const depNote = deps.size > 1 ? ` (+ ${deps.size - 1} dep(s))` : "";
    console.log(`  ✅ ${rel}${depNote} → ${dateStr}`);
    updated++;
  }

  console.log(
    `\n✔ Done. ${updated} file(s) updated, ${skipped} already current, ${noGit} untracked.\n`
  );
}

main();