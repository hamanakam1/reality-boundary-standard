# Requirement explorer

[Open the explorer file](explorer.html). GitHub displays HTML as source; clone or download the repository and open `docs/explorer.html` in a browser to use it interactively. It works as a local file without a server, account, network request, or external asset.

Search matches the requirement ID, section, and text. Space-separated terms must all match. Combine search with a section and literal normative keyword. Select a result to read its full requirement paragraph and follow its source section. `/` focuses search; `Escape` clears the focused search input. Reset clears all filters. The URL fragment retains the selected requirement ID only.

This is informative navigation. [STANDARD.md](../standard/STANDARD.md) controls; applicability and evidence review remain substantive decisions. Keyword presence does not assign an assessment result or waive other obligations.

The explorer and [JSON catalog](../standard/requirements.json) derive from the same source:

```bash
python3 tools/build_catalog.py
python3 tools/build_catalog.py --check
```

The catalog records standard version, source SHA-256, section, source line, requirement paragraph and literal keywords. Edit the standard or `tools/explorer.template.html`, then regenerate both outputs.
