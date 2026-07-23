# O002 — LaTeX publication and live dashboard

- Date: 2026-07-23
- Classification: repository operation (not mathematical research)

## Scope

Preserve the earlier repository-only change that added a LaTeX source requirement,
provenance-aware manifest fields, and the generated README dashboard.

- Added `prior_proof_status` and `latex_file` manifest fields.
- Made `proofctl.py index` regenerate the README status table and validate it.
- Added the standalone TeX rendition of the completed graph proof.

- Validation and the integration tests passed when the feature was introduced.
- The dashboard displays work status, claim status, prior-proof provenance, and
  publication links.

## Dossier impact

No mathematical statement, proof step, review finding, obligation, or claim status
changed. The completed dossier gained publication metadata only.

## Handoff

- Result: LaTeX source and live status tracking are repository capabilities.
- Remaining operational follow-up: none.
- Files a later operator should read: `README.md`, `scripts/proofctl.py`, and
  `process/proof-standard.md`.
- Commit and push status: preserved from prior implementation; reclassification
  is included in O001's closure commit and push.
