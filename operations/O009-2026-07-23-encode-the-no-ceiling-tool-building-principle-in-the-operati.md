# O009 — Encode the no-ceiling tool-building principle in the operating contract

- Date: 2026-07-23
- Classification: repository operation (not mathematical research)

## Scope

Process documentation only. During S007's closing discussion the user
identified a gap between agent behavior and the written contract: route
framing had treated missing mathematical tools as exogenous ("whenever and
from whomever the tool comes"), a capability-deference bias with no basis in
the contract. The user directed that no ceiling be placed on the project's
ambitions that is "purely a thought or a decision or an idea about our
capabilities," while keeping calibration intact. This operation encodes that
principle in the harness-neutral contract so it does not live only in one
harness's private memory. Affected files: `AGENTS.md` (Strategic autonomy),
`process/workflow.md` (strategy-audit section), `PROJECT_STATE.md`
(repository-wide decisions). No problem dossier is touched by this
operation; the corresponding `P-002` next-action amendment is recorded
separately as research session `S008`.

## Work performed

- `AGENTS.md`, Strategic autonomy: added one paragraph — missing tools are
  research targets, not exogenous events; when the recorded obstacle is that
  no known technique applies, the strategy audit must weigh at least one
  internal tool-building attempt (new mechanism, construction, or lemma)
  with a falsifiable first move and an explicit kill condition;
  capability-based deference is never a selection reason; ambition does not
  license inflation — estimates and claim strengths stay calibrated.
- `process/workflow.md`, §4 strategy audit: added the matching operational
  instruction at the point where routes are compared.
- `PROJECT_STATE.md`: added one bullet under repository-wide decisions.
- Design choice: the principle lives in `AGENTS.md` as the single source of
  truth, with `workflow.md` carrying only the audit-time application, per
  the no-restatement rule; the calibration guardrail is stated inside the
  same paragraph so the principle cannot be quoted as license for estimate
  inflation.

## Verification

- `python3 scripts/proofctl.py validate` — passed (2 problem dossiers).
- `python3 -m unittest tests.test_proofctl` — 11 tests, OK (no tooling code
  changed; run as the standing post-process-change check).
- Inspection: the three edits are additive paragraphs/bullets; no existing
  rule was reworded, weakened, or restated across files.

## Dossier impact

None. No statement, claim, obligation, proof, review, or status changed.
The `P-002` next-action amendment motivated by the same directive is
research bookkeeping and is recorded in `sessions/S008`, not here.

## Handoff

- Result: the no-ceiling tool-building principle is contract law, not
  memory; strategy audits must now weigh internal tool-building attempts
  whenever the obstacle is a missing technique.
- Remaining operational follow-up: none.
- Files a later operator should read: `AGENTS.md` (Strategic autonomy),
  `process/workflow.md` §4.
- Commit and push status: committed and pushed as the operational commit
  for O009 (separate from the S008 research commit).
