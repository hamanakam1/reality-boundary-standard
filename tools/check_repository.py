#!/usr/bin/env python3
"""Check derived artifacts, JSON parsing, local Markdown links, and file integrity."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

from build_catalog import ROOT, generated_files, slug
from validate_records import strict_load

EXCLUDED = {".git", ".venv", "__pycache__", ".artifacts", "output", ".playwright-cli", ".pytest_cache"}
MANIFEST = "FILE_MANIFEST.json"


def inventory(root):
    files = []
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        if any(part in EXCLUDED for part in rel.parts) or path.name == ".DS_Store" or path.suffix == ".pyc":
            continue
        if path.is_symlink():
            raise ValueError("symlinks are not permitted in the source package: " + rel.as_posix())
        if path.is_file() and rel.as_posix() != MANIFEST:
            data = path.read_bytes()
            files.append({"path": rel.as_posix(), "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})
    return {"algorithm": "sha256", "scope": "Source files; excludes itself, Git metadata, local environments and generated verification output.", "files": files}


def headings(path):
    found, counts = set(), {}
    for title in re.findall(r"^#{1,6} (.+?)(?: +#+)?$", path.read_text(encoding="utf-8"), re.M):
        base = slug(title)
        suffix = counts.get(base, 0)
        counts[base] = suffix + 1
        found.add(base + (f"-{suffix}" if suffix else ""))
    return found


def link_errors(root):
    errors = []
    for source in root.rglob("*.md"):
        if any(part in EXCLUDED for part in source.relative_to(root).parts):
            continue
        text = re.sub(r"```.*?```", "", source.read_text(encoding="utf-8"), flags=re.S)
        for destination in re.findall(r"!?\[[^\]\n]*\]\(([^)\n]+)\)", text):
            destination = destination.strip("<>")
            uri = urlsplit(destination)
            if uri.scheme or uri.netloc:
                continue
            target = (source.parent / unquote(uri.path)).resolve() if uri.path else source.resolve()
            label = source.relative_to(root).as_posix() + ": " + destination
            if not target.is_relative_to(root.resolve()):
                errors.append("link leaves the source package: " + label)
            elif not target.exists():
                errors.append("missing link target: " + label)
            elif uri.fragment and target.suffix == ".md" and unquote(uri.fragment) not in headings(target):
                errors.append("missing heading anchor: " + label)
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-manifest", action="store_true", help="refresh file hashes after intentional edits")
    args = parser.parse_args(argv)
    try:
        errors = link_errors(ROOT)
        for path in ROOT.rglob("*.json"):
            if not any(part in EXCLUDED for part in path.relative_to(ROOT).parts):
                strict_load(path)
        data = strict_load(ROOT / "standard/requirements.json")
        if len(data["requirements"]) != 118:
            errors.append("0.1.0-draft must retain all 118 requirements")
        for name, content in generated_files().items():
            if not (ROOT / name).is_file() or (ROOT / name).read_bytes() != content.encode("utf-8"):
                errors.append("derived file is stale: " + name)
        manifest = inventory(ROOT)
        if args.write_manifest and not errors:
            (ROOT / MANIFEST).write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        elif not (ROOT / MANIFEST).is_file() or strict_load(ROOT / MANIFEST) != manifest:
            errors.append("file manifest is stale; run python3 tools/check_repository.py --write-manifest")
        if errors:
            print("\n".join(errors), file=sys.stderr)
            return 1
        print(f"Repository checks PASS: {len(data['requirements'])} requirements, {len(manifest['files'])} files; conformance NOT ASSESSED.")
        return 0
    except (OSError, UnicodeError, ValueError, KeyError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
