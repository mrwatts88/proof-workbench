# Project state

Last reviewed: 2026-07-23

## Mission

Build a reliable, resumable environment for proving or disproving mathematical
conjectures. The repository should make uncertainty visible and make every status
promotion auditable.

## Current phase

The first benchmark conjecture has an internally proved result that passed its
required adversarial review gates. A new active research dossier now targets the
Erdős–Gyárfás conjecture.

## Active problems

- `P-001` — Unique Common Neighbor: proved internally for statement version 0.2;
  no known solution was consulted.
- `P-002` — Erdős–Gyárfás Conjecture: active and open at statement version 0.1;
  internal structural reductions and the order-\(11\) lower bound are proved;
  the primary-literature frontier has been audited.
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
- Repository process and tooling work is recorded separately under `operations/`;
  it does not count as progress on a mathematical dossier.
- Session continuity comes from concise handoffs plus detailed append-oriented
  records, not retained chat history.
- Closing a substantive session includes a mandatory canonical-record checkpoint;
  the human shorthand `close session` invokes the whole checkpoint.
- Each closure preserves a plain-language recap and a subjective percentage
  estimate of the chance of eventually settling the exact current statement.
- Computational work must be reproducible and its logical scope must be stated.

## Next action

For `P-002`, replace the falsified local induced-\(P_{13}\) attachment route
with a genuinely global restriction on a minimal counterexample, and stress-test
it against connected cubic graphs of girth at least \(17\) before attempting a
new power-of-two cycle-forcing argument. No required action remains for
`P-001`; its reference comparison remains optional and separately authorized.

## Known process risks

- A structurally valid dossier can still contain invalid mathematics.
- Independent review is a reasoning discipline, not something filenames can
  guarantee.
- Handoffs become misleading if agents omit the end-of-session checkpoint.
- Benchmark investigations can be contaminated if known solutions are consulted
  before the internal candidate and review phases are complete.
