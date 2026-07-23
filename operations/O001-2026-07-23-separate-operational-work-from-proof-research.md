# O001 — Separate operational work from proof research

- Date: 2026-07-23
- Classification: repository operation (not mathematical research)

## Scope

Add an explicit classification boundary between mathematical research and
repository operations. This affects agent instructions, workflow documentation,
record conventions, and `proofctl.py`; it does not alter any theorem.

- Added the `operations/` record family and `proofctl.py operation <title>`.
- Defined `O###` records for process, tooling, dashboard, publication, and
  infrastructure work.
- Made agents classify work before selecting a dossier: mathematical, operational,
  or mixed. Mixed work must keep its two records separate.
- Reclassified the earlier LaTeX/dashboard and PDF-workflow writeups as `O002`
  and `O003` rather than graph-proof sessions.

## Verification

- `python3 scripts/proofctl.py operation ...` created independent root records
  without changing a problem manifest or index.
- The test suite and repository validator are run at closure.

## Dossier impact

None. `P-001`'s mathematical statement, proof, reviews, claims, obligations, and
completion status are unchanged. The old records were only relocated because they
described tooling work rather than mathematical research.

## Handoff

- Result: agents now have an explicit route for out-of-band work.
- Remaining operational follow-up: none.
- Files a later operator should read: `AGENTS.md`, `process/workflow.md`,
  `process/records.md`, and `operations/README.md`.
- Commit and push status: included in this operation's closure commit and push.
