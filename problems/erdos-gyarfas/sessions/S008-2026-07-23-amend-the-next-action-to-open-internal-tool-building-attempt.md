# S008 — Amend the next action to open internal tool-building attempts

- Date: 2026-07-23
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1
- Work / claim status: `active` / `open`
- Strongest established facts: `L001`–`L018`; imports `C004`–`C017`;
  the S007 sweep results and verified extremal graphs
- Open obligations in scope: `G002`, `G003`, `G007`; `G004` (1997 body only)
- Inherited next action (from S007, hours earlier): analyze the four
  order-24 graphs as test material and write the first concrete lemma
  target for the chosen deep route
- Session goal: apply the user's directive — encoded as contract law in
  `O009` — to the recorded route, amending it from positioning to
  attempting; no new mathematics
- Falsifiable next move: not applicable (bookkeeping session; the amended
  action itself carries the falsifiable moves)

## Strategy audit

Compact, since this is a user-directed refinement rather than a new
exploration: the inherited action was compatible with the new
tool-building rule but framed its deliverable as a "lemma target," which
under `O009` undersells what the session should attempt. The refit keeps
the same on-ramp (spectra of the four verified graphs as calibration) and
makes the deliverable a genuine construction attempt: voltage-graph lifts
targeting a 2-connected minimum-degree-3 family whose cycle lengths avoid
all powers of two, with kill conditions named before starting. The
proof-side controlled-start interval lemma stays the alternative; the
order-18 census under PyPy stays capped support. Selection reason: the
falsification route is generate-and-verify — candidates are
machine-checkable instantly by the validated E005/E006 detectors — and
voltage lifts give algebraic control of lifted cycle lengths, so the
attempt has both a real mechanism and a cheap verdict loop. Pivot
condition: either kill condition firing sends effort to the proof-side
lemma with the failure pattern as input.

## Work performed

- Amended `problem.json` `next_action` and `STATE.md`'s best-next-action
  and portfolio framing to the tool-building form.
- Added the corresponding `DECISIONS.md` row.
- No claims, obligations, proofs, experiments, or statuses changed; no
  new mathematics was performed.
- Context: the same directive's process encoding is the separate
  operational record `O009` (AGENTS.md, workflow.md, PROJECT_STATE.md).

## Results

- Records amendment only. No proved or refuted claims, no computations,
  no imports.

## Failed routes and why

- None; nothing was attempted mathematically.

## Adversarial check

- Checked that the amendment does not upgrade any claim, resolve any
  obligation, or move the resolution estimate: posture is not evidence,
  and the estimate stays exactly where S007 left it.
- Checked that the amended action remains small and falsifiable: the
  construction attempt names its kill conditions in advance, and the
  next session's strategy audit retains full authority to override.

## Canonical records changed

- [ ] `STATEMENT.md`
- [x] `STATE.md`
- [ ] `CLAIMS.md`
- [ ] `OBLIGATIONS.md`
- [ ] `PROOF.md`
- [x] `DECISIONS.md`
- [x] `LOG.md`
- [x] `problem.json` and index
- [x] Session-scoped changes committed
- [x] Commit pushed to configured upstream

## Ending checkpoint

- Current frontier: unchanged from S007 (`L018`: counterexamples need at
  least 18 vertices; extremal window \([18,24]\); saturation novelty
  confirmed).
- Remaining blockers: `G002`, `G003`, `G007`; `G004` (1997 body).
- Recalibration decision: route emphasis amended under the `O009`
  tool-building rule at user direction; no mathematical recalibration.
- Best live alternative or reframing: the proof-side controlled-start
  consecutive-even-lengths lemma at minimum degree 3.
- Pivot trigger: a kill condition of the construction attempt firing, or
  any \(\{C_4,C_8\}\)-free graph surfacing at orders 18–23.
- Best next action: as amended — spectra calibration, then the
  voltage-lift construction attempt with pre-named kill conditions.
- Files a new session should read: `STATE.md`, `A007`, the `E005`/`E006`
  READMEs, `references/source-audit-2026-07-23-S007.md`, this session.

## Plain-language recap

This short session changed a plan, not the mathematics. Following the
user's directive — now part of the project's standing rules — that
missing tools should be built here rather than awaited, the recorded next
step was upgraded from "study the extremal graphs and describe what a
useful lemma would look like" to "study them, then actually attempt the
missing construction": building large, robustly connected sparse graphs
whose cycle lengths dodge every power of two, using a lifting technique
that gives real control over cycle lengths, with the conditions that
would prove the attempt failed written down in advance. Nothing about the
conjecture's status changed; the odds estimate is deliberately untouched
because a change of posture is not evidence.

## Proposed next step

Exactly the amended action: compute the full cycle-length fingerprints of
the four verified 24-vertex extremal graphs as calibration, then attempt
voltage-graph lifts of small base graphs aiming at a robustly connected,
minimum-degree-3 family avoiding all power-of-two cycle lengths, with
kill conditions named before starting. If a kill condition fires, the
failure pattern feeds the proof-side alternative (a controlled-start
version of the known consecutive-even-cycle-lengths machinery at degree
3). The capped fallback remains extending the exhaustive census to 18
vertices under PyPy.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 2%
- Previous estimate, if any: 2%
- Reason for change: none — this session changed route posture at user
  direction; posture is not evidence, and inflating the estimate on
  ambition alone is exactly what the new contract paragraph forbids.
- Basis: unchanged from S007 — the falsification-side program is the most
  promising route; the strongest obstacle is that no known technique
  controls full cycle spectra in 2-connected minimum-degree-3 families,
  which is precisely what the amended action now attempts to build.

This is a subjective research outlook, not mathematical evidence or a claim-status
promotion.
