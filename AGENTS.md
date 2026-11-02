# Working on Reality Boundary Standard

- `standard/STANDARD.md` is the normative source. Profiles, examples, templates, explorer, schemas and tools do not silently add or waive requirements.
- Keep stable requirement IDs and record semantic changes with migration impact. Standard, schema and checker versions are independent.
- All shipped claim/evidence examples must remain clearly synthetic. Do not import client material, private source paths, credentials, raw observations or engagement history.
- Preserve separate structure, schema-engine, declared-policy, evidence-review and full-conformance outcomes. No automated pass establishes factual truth or authority.
- Edit `tools/explorer.template.html` and the standard, then run `python3 tools/build_catalog.py`; do not edit generated catalog/explorer files directly.
- Follow `docs/DEVELOPMENT.md` for checks. Refresh `FILE_MANIFEST.json` with `python3 tools/check_repository.py --write-manifest` after intentional edits, then verify without write mode.
- Keep local receipts under ignored `.artifacts/` or outside this repository. Review exact files and history before publishing.
- Resolve the recorded rights/license decision before the initial public push. Do not interpret repository ownership or a local validation receipt as a license grant.
- Do not add automatic deployment, external messages, paid resources or evidence retrieval to CI. The verification workflow has read-only permissions.
