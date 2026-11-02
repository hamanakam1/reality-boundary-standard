# Adopt RBS for one decision

This guide is informative. The [standard](../standard/STANDARD.md) and [assessment procedure](../standard/CONFORMANCE.md) control normative interpretation. You can use the method without a new service, database, model, or agent framework.

## 1. Pick a claim that matters

Choose a statement someone will use for a decision: a performance number, a privacy promise, a recovery claim, or authority for an agent to act. Record where readers encounter it. Correct unsupported public wording while the broader inventory is still incomplete.

Split “our agent runs locally, keeps all data private, and deploys safely” into separate claims about execution location, data movement, and deployment behavior. Each needs its own scope and evidence.

## 2. Write the record

Copy the [claim template](../templates/claim-record.md). Record the exact statement; three classification axes; system and version; population and conditions; owner; evidence cutoff; review triggers; evidence and counterevidence; uncertainty; and next verification step.

For consequential wording, include the permitted statement and the stronger statement the evidence does not support. A measurement needs units, denominator, sampling method, interval, baseline, and uncertainty. An operational action needs actual authority, limits, revocation, and recovery.

## 3. Attach evidence at its actual boundary

Prefer an immutable source revision, test receipt, artifact digest, or versioned observation. Say who collected it, when, how, what was transformed, and which claim it supports. Shared-origin reports are not independent corroboration.

A restricted source may stay restricted. Supply an appropriate review arrangement and disclose its limits. Do not publish private payloads merely to populate an evidence directory.

## 4. Review applicability

Use the [applicability guide](APPLICABILITY.md) and the full standard. Create a matrix if the decision needs a substantive assessment:

```bash
python3 tools/new_assessment.py /tmp/export-assessment.csv \
  --scope "Export API v2, staging, two test roles" --as-of 2026-11-01
```

The output includes all 118 requirements with `applicability=UNREVIEWED` and `result=UNKNOWN`. It records a UTC cutoff day; put the exact cutoff timestamp, artifact revisions, intended decisions, reviewer limits, and review triggers in the [assessment narrative](../templates/conformance-assessment.md).

Decide applicability row by row. A not-applicable decision needs the absent condition and a reconsideration trigger. A recommendation exception needs a reason and consequences; it cannot waive a mandatory obligation in the same paragraph. The CSV is editable and is not a validator input or a completed assessment.

## 5. Check records if useful

The optional JSON format supports exchange and limited checks. Inspect the [synthetic records](../examples/claims.json) and [checker documentation](VALIDATOR.md). The schema does not include every narrative obligation, so JSON alone does not establish that the minimum claim record is complete.

```bash
python3 tools/validate_records.py examples/claims.json examples/evidence.json --as-of 2026-10-27
```

Use the actual decision date for real records. Exit `2` means policy review is incomplete, such as overdue evidence. The checker never opens evidence URLs, verifies authority, or judges factual sufficiency.

## 6. Issue the right outcome

For structural checks only, say records passed the named checker at the stated cutoff and full conformance is not assessed. For substantive assessment, follow the [four outcomes and precedence rules](../standard/CONFORMANCE.md#6-assessment-outcomes-and-wording).

A deployment, model update, incident, revoked permission, or contradictory test can require a fresh decision before reusing a claim. Preserve the old record as historical evidence. The [release-review walkthrough](../examples/release-review/README.md) illustrates this process with synthetic material.
