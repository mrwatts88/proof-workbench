# Project state

Last reviewed: 2026-07-23

## Mission

Build a reliable, resumable environment for proving or disproving mathematical
conjectures. The repository should make uncertainty visible and make every status
promotion auditable.

## Current phase

The first benchmark conjecture has an internally proved result that passed its
required adversarial review gates.

## Active problems

- `P-001` — Unique Common Neighbor: proved internally for statement version 0.2;
  no known solution was consulted.
- See the generated [problem index](problems/INDEX.md).

## Repository-wide decisions

- Each problem is a self-contained dossier under `problems/<slug>/`.
- Workflow maturity and mathematical outcome are tracked separately.
- Atomic claims and unresolved obligations are first-class records.
- A proof is not complete until adversarial reviews and promotion gates pass.
- Agents initiate and delegate those reviews automatically when a candidate
  appears; humans do not schedule the review lifecycle.
- Every internally proved result has a standalone LaTeX source, and the generated
  README dashboard displays both current status and prior-proof provenance.
- A proved result also has a committed PDF compiled by Tectonic, with the source,
  PDF, and compiler version recorded in its dossier.
- Session continuity comes from concise handoffs plus detailed append-oriented
  records, not retained chat history.
- Closing a substantive session includes a mandatory canonical-record checkpoint;
  the human shorthand `close session` invokes the whole checkpoint.
- Each closure preserves a plain-language recap and a subjective percentage
  estimate of the chance of eventually settling the exact current statement.
- Computational work must be reproducible and its logical scope must be stated.

## Next action

No required action remains for `P-001`. Reference comparison is optional and
requires separate authorization.

## Known process risks

- A structurally valid dossier can still contain invalid mathematics.
- Independent review is a reasoning discipline, not something filenames can
  guarantee.
- Handoffs become misleading if agents omit the end-of-session checkpoint.
- Benchmark investigations can be contaminated if known solutions are consulted
  before the internal candidate and review phases are complete.
