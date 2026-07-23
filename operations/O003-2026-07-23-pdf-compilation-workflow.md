# O003 — PDF compilation workflow

- Date: 2026-07-23
- Classification: repository operation (not mathematical research)

## Scope

Preserve the earlier repository-only change that standardized Tectonic PDF builds
and required a compiled PDF for a proved dossier.

- Added `proofctl.py typeset <slug>` using Tectonic.
- Added `pdf_file` and `latex_engine` manifest fields and terminal-proof
validation for the compiled artifact.
- Compiled the current TeX source and exposed PDF and TeX links in the dashboard.

- Tectonic 0.16.9 compiled the document successfully.
- Validation and integration tests passed when the feature was introduced.

## Dossier impact

No mathematical statement, proof step, review finding, obligation, or claim status
changed. The completed dossier gained a compiled publication artifact and metadata.

## Handoff

- Result: compiled PDFs are an enforced publication artifact for proved results.
- Remaining operational follow-up: none.
- Files a later operator should read: `Makefile`, `scripts/proofctl.py`, and
  `process/proof-standard.md`.
- Commit and push status: preserved from prior implementation; reclassification
  is included in O001's closure commit and push.
