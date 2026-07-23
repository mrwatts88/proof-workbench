# Project state

Last reviewed: 2026-07-23

## Mission

Build a reliable, resumable environment for proving or disproving mathematical
conjectures. The repository should make uncertainty visible and make every status
promotion auditable.

## Current phase

Scaffolding is initialized. No mathematical problem has been admitted yet.

## Active problems

None. See the generated [problem index](problems/INDEX.md).

## Repository-wide decisions

- Each problem is a self-contained dossier under `problems/<slug>/`.
- Workflow maturity and mathematical outcome are tracked separately.
- Atomic claims and unresolved obligations are first-class records.
- A proof is not complete until adversarial reviews and promotion gates pass.
- Session continuity comes from concise handoffs plus detailed append-oriented
  records, not retained chat history.
- Closing a substantive session includes a mandatory canonical-record checkpoint;
  the human shorthand `close session` invokes the whole checkpoint.
- Each closure preserves a plain-language recap and a subjective percentage
  estimate of the chance of eventually settling the exact current statement.
- Computational work must be reproducible and its logical scope must be stated.

## Next action

Admit the first conjecture with `python3 scripts/proofctl.py new`, normalize its
statement, and complete an intake session before choosing a proof strategy.

## Known process risks

- A structurally valid dossier can still contain invalid mathematics.
- Independent review is a reasoning discipline, not something filenames can
  guarantee.
- Handoffs become misleading if agents omit the end-of-session checkpoint.
