# Reference record validator

**Record format version:** 0.1.0  
**Checker version:** 0.1.1  
**Associated standard:** Reality Boundary Standard 0.1.0-draft  
**Implementation:** Python 3 standard library; no installation or network access required

## What this tool does

The checker validates the declared shape and a conservative set of policy relationships in claim and evidence records. It is a small, direct implementation for the included record format. It is **not a general JSON Schema evaluator**, a fact-checking service, a security scanner, or an RBS conformance assessor.

The companion schemas use the [JSON Schema 2020-12 vocabulary](https://json-schema.org/draft/2020-12). They describe the record structure for other compatible tools. The Python checker directly implements the documented record checks; it does not load those schema files or claim to implement all JSON Schema keywords. A separate JSON Schema implementation can validate the schemas and records, subject to that implementation’s support for format assertions. Such a result is still only structural validation.

The format version identifies the record contract. The standard version identifies the proposed normative document. They are intentionally recorded separately so a future editorial standard change need not imply that record bytes changed.

## Run the supplied synthetic demonstration

From the repository root:

```bash
python3 tools/validate_records.py examples/claims.json examples/evidence.json --as-of 2026-10-27
python3 -m unittest discover -s tests -v
```

All included claim and evidence examples are explicitly marked `synthetic: true`. They include a fictional bounded-zero test, a supported proposal rationale, and a speculative archive entry. The fictitious executed test is a demonstration of how to record a claim; it is not an actual application test. The tool reports `SYNTHETIC_DEMONSTRATION` when all input records are synthetic.

The example review deadlines intentionally make freshness visible. Running the same fixture against a later date after its review deadline returns `INCOMPLETE`. That is expected behavior, not a reason to silently extend deadlines.

## Input contract

Both files contain top-level JSON arrays. At least one claim is required. An empty evidence array is allowed when no supplied claim requires evidence, for example an unverified speculative record with no operational use.

Claim fields include:

- Identity and classification: `schema_version`, `id`, `synthetic`, `statement`, `claim_class`, `truth_status`, and `deployment_status`.
- Scope and ownership: `scope`, `owner`, `as_of`, and `review_by`.
- Support: `evidence_ids`, `conflicting_evidence_ids`, `limitations`, and `classification_rationale`.
- Verification: `method`, `acceptance`, `actual_result`, `reproduction`, and `execution_status` inside `verification`.
- Operating authority: `operational`, `authority`, and `authority_not_applicable_reason`.
- Permitted reliance: `usage`.
- History: `decision_history`.

Evidence records include provenance, source URI and access class, disclosed review, capture time, review deadline, declared scope, method, summary, optional digest, claim relationships, transformations, and limitations. A URI is a reference only. The checker never retrieves it, executes it, or follows embedded instructions.

`authority: null` is permitted for a static non-action claim only when `authority_not_applicable_reason` explains that choice. An operational action claim needs a declared actor, actions, scope, budget, revocation mechanism, and rollback or recovery description. Presence checks do not verify that those controls exist or that the actor has legal authority.

Unknown properties are rejected at every defined object boundary. Extension fields require an explicitly supported record-format revision; they cannot smuggle in alternate authority or status semantics.

## Meaning of the usage flags

The reference checker applies a **conservative operational-claim profile**:

- `customer_promise: true` means that this record is being relied on as an **established current operational capability** in a customer commitment.
- `production_dependency: true` means that production relies on this claim as an **established operational capability**.
- `research_only: true` means that the claim is restricted to investigation or exploration and must not simultaneously be represented as established operational reliance.

These meanings do not prohibit an explicitly qualified pilot, an experiment with accepted uncertainty, or a conditional future contractual milestone. Those cases need separate decision and authorization records describing the uncertainty and conditions. RBS-PRM-05 permits appropriately accepted research uncertainty; this small checker does not evaluate that acceptance process.

A `SUPPORTED` proposal can therefore describe a supported design rationale while its implementation remains unexecuted. The record cannot use that rationale alone to claim an established operational capability. Separate the implemented-performance claim and collect its evidence.

A checker policy failure is not automatically an RBS normative nonconformance finding. It identifies a violation of this declared reference profile or a record inconsistency. A full assessment evaluates the actual normative requirements, applicability, evidence, and decision records.

## Checks performed

| Area | Direct checks |
|---|---|
| File parsing | Readable UTF-8 JSON, rejection of duplicate object keys and non-finite JSON constants. |
| Shape | Required fields, field types, exact enums, supported record version, unknown-field rejection, required nonempty values, duplicate reference items. |
| Identity | Duplicate claim/evidence IDs and nonexistent references. |
| Relationships | Reciprocal declared support/counterevidence links and valid history references. |
| Classification | Supported claims declare supporting evidence; disputed/contradicted claims declare counterevidence. |
| Observations and demonstrations | Evidence declares the same system/environment/version; execution and actual result are recorded; demonstrations provide reproduction or access instructions. |
| Operational reliance | Established capability reliance requires a supported observed/demonstrated claim; research-only cannot conflict with that reliance. |
| Authority | Null authority has a non-action rationale; action claims declare controls; a not-applicable rationale cannot coexist with applicable authority. |
| Production scope | Production claims identify a version; proposed/research/speculative/unknown operational capabilities are separated from production action claims. |
| Time | Timestamps include time zones; calendar dates are valid; review deadlines are explicit; future collection and inconsistent chronology are flagged. Supporting evidence and counterevidence must both respect the claim's evidence cutoff. |
| Freshness | Overdue claim/evidence reviews produce `INCOMPLETE`, not a silent pass. |
| Restricted evidence | A restricted pointer can be used with a disclosed review; unreviewed restricted evidence produces `INCOMPLETE`. |
| Synthetic boundary | Both a synthetic source type and synthetic source access require `synthetic: true`; synthetic evidence cannot establish a record declared as a real observed/demonstrated claim. |

Scope matching checks declared strings only. They do not verify that the test environment actually corresponds to the claim. Review history and timestamp comparisons likewise depend on supplied records; a false timestamp remains false even if it is well formatted.

## Outputs and exit status

Output is a JSON object containing distinct `structure` and `policy` results. `full_conformance` is **always `NOT_ASSESSED`**.

| Result | Meaning | Process exit |
|---|---|---:|
| Structure `PASS`, policy `PASS` | Implemented direct checks passed for the supplied records and date. | 0 |
| Structure `FAIL` | Input or record format failed; policy is `NOT_RUN`. | 1 |
| Policy `FAIL` | One or more declared-policy inconsistencies were found. | 1 |
| Policy `INCOMPLETE` | No declared-policy failure, but freshness or restricted-evidence review needs resolution. | 2 |

When failures and incompleteness coexist, `FAIL` takes precedence and the `incomplete` array remains present. No skipped policy assessment is represented as a pass. Command-line usage errors also use the conventional nonzero exit from the argument parser.

`--as-of` is required so the freshness decision is reproducible. It is interpreted as a UTC calendar date for review deadlines and future-date checks. Within-day evidence-cutoff comparisons use the full timestamp and time-zone offset.

Timestamps must use the explicit-offset spelling accepted by the checker (`Z` or `±HH:MM`). Offset hours are 00–23 and minutes are 00–59; invalid components are rejected rather than normalized. The calendar value and its conversion to UTC must both fit Python's datetime range. UTC underflow or overflow is reported as a structural failure, so policy checks do not run. Valid offsets and representable range endpoints remain accepted. These are direct-checker limits, not a claim that the checker implements every ISO 8601 or JSON Schema date-time variation.

## What passing does not establish

A pass does not show that evidence is authentic, independent, relevant beyond its declared links, or sufficient for the proposition. It does not prove that a test ran, that a deployment exists, that an authority grant is valid, that a retry is safe, or that a customer outcome occurred. Digest strings are format-checked but bytes are not rehashed. URLs are syntax-checked but not fetched. Reviewer fields are inspected for consistency but reviewers are not authenticated.

The tool does not infer physical possibility, truth, model quality, safety, legal status, regulatory compliance, privacy, tenant isolation, market demand, unit economics, or external approval. It does not scan arbitrary prose for forbidden words. A valid scoped statement reporting zero observed events is allowed. Private evidence may remain private when its access and review limitations are disclosed.

Use [the conformance procedure](../standard/CONFORMANCE.md) for a full scoped assessment. Keep actual claim verification and review separate from this structural demonstration.

## Test scope

The unit suite exercises useful boundary failures: unsupported operational reliance; supported proposal rationale; absent or mismatched evidence; required counterevidence; stale and future records; same-day cutoff inconsistency; missing action controls; restricted evidence review; synthetic/real separation; invalid types and unknown fields; duplicate keys; and nonzero CLI failures.

The suite verifies behavior of the checker. It does not certify the sample scenario, validate the physical claims in the speculative archive, or establish full coverage of every possible malformed input. Changes to the record format or policy should add a test for the actual failure being addressed and update both schemas and this document.
