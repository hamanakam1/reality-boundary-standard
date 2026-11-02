#!/usr/bin/env python3
"""Derive an informative requirement catalog and offline explorer from STANDARD.md."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIREMENT = re.compile(r"^\*\*(RBS-[A-Z]+-[0-9]{2})\.\*\* (.+)$")
KEYWORDS = re.compile(r"\b(?:MUST NOT|SHOULD NOT|MUST|SHOULD|MAY)\b")


def slug(text):
    """GitHub-style heading slug for the headings used in this repository."""
    text = re.sub(r"<[^>]*>", "", text).replace("`", "").replace("*", "")
    return "".join(c for c in text.lower() if c in " -_" or unicodedata.category(c)[0] in "LN").replace(" ", "-")


def catalog(source):
    text = source.decode("utf-8")
    version = re.search(r"^\*\*Version:\*\* (\S+)", text, re.M)
    if not version:
        raise ValueError("standard version is missing")
    rows, seen = [], set()
    section = anchor = None
    lines = text.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        if line.startswith("## "):
            section = line[3:]
            anchor = slug(section)
        match = REQUIREMENT.fullmatch(line)
        if match:
            identifier, body = match.groups()
            line_number = index + 1
            if identifier in seen:
                raise ValueError("duplicate requirement: " + identifier)
            if section is None:
                raise ValueError("requirement outside a section: " + identifier)
            seen.add(identifier)
            # A wrapped requirement paragraph belongs to the same requirement.
            while index + 1 < len(lines) and lines[index + 1].strip():
                if lines[index + 1].startswith(("#", "**RBS-")):
                    raise ValueError("requirement paragraphs need a blank separator")
                index += 1
                body += " " + lines[index].strip()
            rows.append({"id": identifier, "family": identifier.split("-")[1],
                         "section": section, "anchor": anchor, "source_line": line_number,
                         "keywords": sorted(set(KEYWORDS.findall(body))), "text": body})
        elif line.startswith("**RBS-"):
            raise ValueError("malformed requirement at line " + str(index + 1))
        index += 1
    if not rows:
        raise ValueError("no requirements found")
    return {"standard_version": version.group(1), "source": "standard/STANDARD.md",
            "source_sha256": hashlib.sha256(source).hexdigest(), "normative": False,
            "notice": "Derived navigation aid. STANDARD.md controls; keywords are not applicability decisions.",
            "requirements": rows}


def generated_files(root=ROOT):
    data = catalog((root / "standard/STANDARD.md").read_bytes())
    encoded = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    # Escape script terminators even if a future requirement contains HTML.
    embedded = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c").replace("&", "\\u0026")
    template = (root / "tools/explorer.template.html").read_text(encoding="utf-8")
    if template.count("__RBS_CATALOG__") != 1:
        raise ValueError("explorer template must contain exactly one catalog placeholder")
    return {"standard/requirements.json": encoded,
            "docs/explorer.html": template.replace("__RBS_CATALOG__", embedded)}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report drift without writing")
    args = parser.parse_args(argv)
    try:
        for name, content in generated_files().items():
            path = ROOT / name
            if args.check:
                if not path.is_file() or path.read_bytes() != content.encode("utf-8"):
                    raise ValueError(name + " is stale; run python3 tools/build_catalog.py")
            else:
                path.write_text(content, encoding="utf-8", newline="\n")
        print("Requirement catalog and explorer: " + ("current" if args.check else "generated"))
        return 0
    except (OSError, UnicodeError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
