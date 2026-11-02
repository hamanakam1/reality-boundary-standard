# Contributing

Read the standard and conformance procedure before proposing normative changes. Submit the exact problem, relevant requirement IDs, expected behavior, examples/counterexamples, and compatibility effects.

Use primary sources for factual technical assertions. Cite the source, relevant version/date, and the specific claim it supports. Do not copy long proprietary excerpts or expose a customer's private evidence. Anonymization must preserve the logical boundary without leaving identifying metadata or secrets.

Run the checks in [DEVELOPMENT.md](docs/DEVELOPMENT.md) for changes to schemas, fixtures, or tools. Test a new policy against both a valid bounded claim and the misleading claim it is meant to catch. A language lint should not automatically reject a legitimate scoped zero observation or a fictional quotation clearly labeled as such. Regenerate the catalog/explorer and file manifest after intentional source edits.

Update CHANGELOG.md for substantive changes. Follow the governance procedure for normative changes and retain stable IDs. Describe what changed, why, and how the reviewer can assess it.

Contributors retain their copyright. By submitting material intended for inclusion, you offer it under the license applying to that material in [LICENSING.md](LICENSING.md) and confirm that you have authority to do so. Preserve attribution, identify third-party material and compatible rights, and do not contribute private evidence. Prose uses CC-BY-4.0; software, record schemas, synthetic JSON examples and configuration use MIT. Generated files retain the scope split for copied standard paragraphs. No copyright assignment is requested.

Use the issue forms for a change proposal, correction/tool defect, or adoption report. Normative changes need affected IDs, concrete failure mode, proposed wording, alternatives, feasible review evidence, adoption cost and migration impact. An adoption report should explain which decision improved or became harder, not simply count completed forms.
