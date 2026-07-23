# O008 — Scrap the internal-first no-known-solutions discipline repository-wide

- Date: 2026-07-23
- Classification: repository operation (not mathematical research)

## Scope

The user clarified the repository mission and directed that the internal-first
"benchmark" discipline — avoiding known solutions, gating reference
comparison behind separate authorization, and re-deriving reported results for
internal provenance — be scrapped everywhere. The mission is: find genuinely
open conjectures and settle them; lean on all existing verified knowledge to
stand at the published frontier immediately; spend effort passing the
frontier and producing information the mathematical community does not have.

Affected: `AGENTS.md` (mission, discovery delegation, `prior_proof_status`
semantics), `PROJECT_STATE.md` (mission, phase, decisions, risks, next
action), `CLAUDE.md` and `process/harness.md` (explorer delegation),
`.claude/agents/proof-explorer.md` (external literature now default),
`P-001` live records (`STATEMENT.md` provenance, `STATE.md`,
`OBLIGATIONS.md` G004, `PROOF.md`, `problem.json` tags and next action,
`DECISIONS.md` new entry), `P-002` route records (`OBLIGATIONS.md`
G010/G011, `DECISIONS.md` new entry, `STATE.md`, `PROOF.md` gaps, `A006`
closure, `problem.json` next action). Historical, append-only records
(`LOG.md`, sessions, prior decisions, prior operations) were left intact as
history.

## Work performed

- Rewrote the mission in `AGENTS.md` and `PROJECT_STATE.md`: settle open
  conjectures, reach the frontier by import, pass it; re-derivation for its
  own sake is explicitly not a goal.
- Redefined `prior_proof_status` semantics in `AGENTS.md` as target
  selection, not a use restriction; external results of any strength are
  usable through the import rules, while internal claim promotions still
  pass review gates.
- Made external literature available to the `proof-explorer` by default in
  its agent definition, `CLAUDE.md`, and `process/harness.md`; its isolation
  now targets only this repository's inherited framing (anti-anchoring), and
  reviewer independence rules are unchanged.
- Replaced the contamination risk in `PROJECT_STATE.md` with
  import-correspondence and frontier-drift risks, and added a standing
  repository decision that the retired rule must not be reintroduced.
- P-001: neutralized all live gating language ("separately authorized",
  "must avoid", benchmark/solution-embargo tags), recorded the retirement in
  its `DECISIONS.md`, and left the historical fact of independent
  development intact. Next action now: reference comparison optional and
  freely permitted.
- P-002: retired `G010` (orders 14–15 exhaustion) as re-derivation of
  reported computations; closed attempt `A006` accordingly; opened `G011`,
  the deliberate literature novelty check on the edge-maximal saturation
  reduction `L008`–`L016`, which no audited source showed and which is the
  project's candidate novel asset; re-pointed the next action to the
  frontier sweep (import verified bounds, verify the reported 24-vertex
  extremal graphs internally, settle saturation novelty); recorded the route
  decision in `DECISIONS.md`. The S006 resolution estimate was left
  untouched; only its stale "two orders" wording was corrected to three.

## Verification

- `grep -rniE "benchmark|contaminat|consult|known solution|separately
  authorized|reference comparison|does not license"` across the repository:
  remaining hits are historical records (sessions, logs, prior decisions,
  operation files), factual provenance statements, review-independence
  language unrelated to sources, and retirement notices themselves; no live
  prescriptive rule against consulting known solutions remains.
- `python3 scripts/proofctl.py validate` passes (2 dossiers).
- `python3 scripts/proofctl.py index` regenerated; both next actions render.

## Dossier impact

No mathematical statement, claim strength, proof, review, or claim status
changed. Both dossiers' workflow records changed as listed: P-001 next
action and G004 framing; P-002 G010 retired, G011 opened, A006 closed,
next action re-pointed, one decision row appended in each dossier. The
statement-version fields are unchanged; the `P-001` `STATEMENT.md` edit
touched only the provenance prose, not the mathematical statement.

## Handoff

- Result: the internal-first discipline is fully retired; all agent-facing
  documents now state the lean-on-everything, pass-the-frontier mission, and
  the saturation-novelty question (`G011`) is codified as P-002's deciding
  next move.
- Remaining operational follow-up: none.
- Files a later operator should read: `AGENTS.md` (mission), `PROJECT_STATE.md`,
  `problems/erdos-gyarfas/STATE.md`.
- Commit and push status: committed and pushed with this operation's changes.
