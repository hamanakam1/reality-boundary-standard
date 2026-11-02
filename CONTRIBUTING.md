# Contributing

Read the standard and conformance procedure before proposing normative changes. Submit the exact problem, relevant requirement IDs, expected behavior, examples/counterexamples, and compatibility effects.

Use primary sources for factual technical assertions. Cite the source, relevant version/date, and the specific claim it supports. Do not copy long proprietary excerpts or expose a customer's private evidence. Anonymization must preserve the logical boundary without leaving identifying metadata or secrets.

Run the checks in [DEVELOPMENT.md](docs/DEVELOPMENT.md) for changes to schemas, fixtures, or tools. Test a new policy against both a valid bounded claim and the misleading claim it is meant to catch. A language lint should not automatically reject a legitimate scoped zero observation or a fictional quotation clearly labeled as such. Regenerate the catalog/explorer and file manifest after intentional source edits.

Update CHANGELOG.md for substantive changes. Follow the governance procedure for normative changes and retain stable IDs. Describe what changed, why, and how the reviewer can assess it.

Licensing remains pending the initial publication decision. Do not accept external code or content into a public release without compatible rights and a recorded contribution policy.

Use the issue forms for a change proposal, correction/tool defect, or adoption report. Normative changes need affected IDs, concrete failure mode, proposed wording, alternatives, feasible review evidence, adoption cost and migration impact. An adoption report should explain which decision improved or became harder, not simply count completed forms.
