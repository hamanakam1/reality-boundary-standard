# Preparation verification

Initially prepared 27 October 2026; locally rechecked and hardened 28 October 2026. Scope: this draft standard, its supporting files, and reference checker 0.1.1. Record schemas remain 0.1.0. This is not a product assessment or full RBS conformance assessment. Machine-readable results are in [LOCAL_VALIDATION.json](LOCAL_VALIDATION.json).

## Checks completed

- The normative standard contains **118 unique requirement identifiers**. Material cross-references were reviewed.
- Relative Markdown file links in the prepared source tree resolve.
- The claim/evidence schema files and synthetic records parse as JSON.
- The supplied synthetic example produces structure PASS and declared-policy PASS with `full_conformance: NOT_ASSESSED` at the specified 2026-10-28 evaluation date.
- **51 behavioral tests pass** for the reference validator, including malformed records, unknown properties, duplicate identifiers/keys, missing evidence, stale/future evidence, synthetic-versus-real metadata, counterevidence chronology, operational-use restrictions, authority fields, and timezone/UTC-range boundaries.
- Independent review identified and corrected conformance-outcome precedence, the distinction between the conservative reference policy and normative research acceptance, and the scope of commercial-pilot requirements.
- Independent code review identified and corrected the synthetic-access metadata inconsistency and a missing counterevidence-cutoff check; focused regression tests cover both.
- The local maintenance review found that invalid timezone minutes were normalized by Python and that UTC range conversion could raise an uncaught overflow. The six added regression tests first reproduced failures against the original checker (10 failing and 6 erroring subcases), then all passed after the parser fix. CLI invalid-input cases return structured JSON with structure FAIL, policy NOT_RUN, full conformance NOT_ASSESSED, and exit code 1.
- A scan for known private engagement identifiers, provider-document links, local preparation paths, and private-key header patterns found no matches in the public source tree. This is a bounded check, not a general secret scanner, licensing audit, or guarantee that every possible identifying detail has been detected.

## Verification commands

```bash
python3 tools/validate_records.py examples/claims.json examples/evidence.json --as-of 2026-10-28
python3 -m unittest discover -s tests -v
```

The checker uses the Python standard library and does not require a network call. The JSON Schema documents are supplied for compatible tooling; the direct checker is not a complete JSON Schema engine. No separate full-schema-engine validation is claimed.

## Remaining publication inputs

Repository owner/organization, initial maintainers/contact, rights holder/license, and authorization for the exact public candidate remain to be recorded. The local candidate may be committed for review; no public repository, remote commit, tag, release, certification service, or external endorsement was created by this preparation.

## Limits

The examples are synthetic. The tests verify the checker’s behavior, not the truth of an operating capability. The review is a preparation review, not independent accreditation. A public adopter must perform its own scoped assessment against the standard using its actual evidence and authority.
