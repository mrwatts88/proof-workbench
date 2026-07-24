# S018 — Roadmap audit: the 1-atom question is conjecture-complete, and a tiered target structure for the dossier

- Date: 2026-07-24
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1
- Work / claim status: `active` / `open`
- Strongest established facts: `L022`; the assembly programme
  `L025`–`L036`; the pinched catalogue through order 16 (`C035`, S017);
  the bipartite/parity channel empty through order 21 at session open
  (`C034`, S016).
- Open obligations in scope: `G013` (all three sub-questions), `G014`,
  `G007`.
- Inherited next action (S016): finish the order-22 bipartite leg, then
  open the odd-prime-gcd channel.
- User instruction opening this session: judge whether the recorded
  documents describe a good path or need changing; weigh routes by what
  they would deliver — the full conjecture first, a significant
  delimited result (e.g. a bound or a reduction) second — keep cheap
  legs running alongside rather than instead; and update the
  documentation with a roadmap. The user also flagged as strange that
  successive agents keep deferring the 1-atom question.
- Falsifiable next move: test whether the 1-atom question is a
  sub-question at all — is a counterexample plus a pendant vertex a
  1-atom under D-A4?

## Strategy audit

- Why the inherited route might work: the order-22 leg was already
  running and cheap; the gcd channel is the one congruence channel with
  no theory.
- Fastest way to falsify the *architecture* the route sits in: take the
  user's observation seriously as mathematics rather than as a comment
  on agent behaviour. `L026` had already shown that a two-terminal rung
  can be conjecture-complete because a counterexample can be hidden
  inside it. The same test had never been run on the one-terminal
  object, and it is one line.
- Mechanistically distinct alternative: none needed — the audit came
  back positive immediately (see Results), which reprices every route in
  the portfolio and therefore had to be resolved before any route was
  selected.
- Selected route and reason: the architecture audit, then the roadmap
  rewrite the user asked for, with the order-22 leg left running as
  background (it completed mid-session and was folded in).
- Pivot criterion: if the pendant construction had failed, the session
  would have reverted to the inherited next action unchanged.

## Work performed

- **Proved `L036` (`A018` T1).** A 1-atom under D-A4 exists **iff** a
  counterexample exists: attach one pendant vertex to a connected
  counterexample. The pendant lies on no cycle, so the spectrum is
  unchanged and power-freeness is preserved; the pendant is the unique
  vertex of degree \(<3\). With `L025` R4 for the converse, the
  unrestricted 1-atom question is conjecture-complete — the
  one-terminal analogue of `L026`, and cheaper (no scaffold needed).
- **Repaired `L029` (`A018` T2).** As recorded, "if no 1-atom exists,
  every minimal counterexample is cubic" is a true but *vacuous*
  implication. `A012` T4's proof only ever produces an exceptional
  vertex of degree 2 (it deletes an edge \(xy\) with \(\deg x\ge4\),
  \(\deg y=3\)), and its second branch uses no 1-atom at all. So the
  reduction is restated with **tight** 1-atoms and is then non-vacuous:
  0.1 holds iff no cubic counterexample and no tight 1-atom exist.
- **Withdrew `A012` Remark T4.1 (`A018` T3).** Its claim that
  minimum-order 1-atoms are tight fails exactly when the pendant-reduct
  is a *cubic* counterexample: T4's edge deletion needs a degree-\(\ge4\)
  vertex, and "directly as a counterexample" is not available as a
  contradiction inside a statement about minimum-order 1-atoms. Recorded
  as an open defect, not repaired.
- **Corrected `A016` M6's ceiling.** The recorded form ("closing every
  channel plus the 1-atom question yields the cubic reduction, not 0.1")
  is circular, since one half *is* 0.1. Non-circular form: closing every
  assembly channel and proving no *tight* 1-atom exists yields exactly
  the cubic reduction.
- **Opened `G015`** — the cubic reduction as the programme's named
  proof-side deliverable, with two independent non-circular routes: R1
  (no tight 1-atom, then `L029`) and R2 (strengthen the imported
  \(4/7\) cubic-density bound `C006` to 1, bypassing the atom
  formalism).
- **Rewrote the roadmap in `STATE.md`** as five tiers (0: settle 0.1;
  1: `G015`; 2: restricted-class theorems — bipartite EGC and the
  path-spectrum gcd theorem; 3: cheap legs that run but are never
  *selected*; 4: leverage infrastructure — the dedicated generator that
  unlocks both cubic order 30 and bipartite order 31). All threads A–F
  remain live per the standing instruction; the pencil endgame is
  demoted to Tier 3, not dropped. Added a process rule: every strategy
  audit must name the tier its selected route serves.
- **Background leg completed.** The S016 order-22 bipartite run finished
  during this session: 178,549 in class from 55,451,237 generated in
  2,798s, zero \(C_8\)-free, zero power-free; minimum \(C_8\) count 14;
  profiles 155,205 gadgets / 21,579 tight-1-atom candidates / 1,765
  minimum-degree-\(\ge3\) graphs. Folded into `C034`, `STATE.md` and the
  `E015` README, so the parity channel is now empty through order 22
  (23 with a pendant).

## Results

- Proved claims: `L036` (1-atom completeness; the tightness restatement;
  the non-vacuity of the tight version).
- Refuted / corrected in-session: `L029`'s recorded reading (vacuous as
  stated); `A012` Remark T4.1 (withdrawn, unproved); `A016` M6's ceiling
  (circular as stated); `G013`(a)'s description of the 1-atom question as
  "the only sub-question with direct proof-side yield" (it is not a
  sub-question).
- Computational evidence: the order-22 extension of `C034`.
- Provisional insights (not lemmas): the selection-bias diagnosis — a
  strategy audit that ranks routes by cheapest decisive computation will
  reliably promote search legs and bury theorem targets that have no
  cheap move, which is how a conjecture-complete object stayed on the
  live list for six sessions.
- Imported facts needing verification: unchanged; R2 of `G015` adds a
  prerequisite — Carr's \(4/7\) argument must be verified before being
  strengthened.

## Failed routes and why

None abandoned. One recorded target (the unrestricted 1-atom question)
was retired because it was proved to be the conjecture itself, and one
recorded remark was withdrawn as unproved. The inherited next action was
superseded rather than executed, except for its background search leg,
which completed.

## Adversarial check

- The construction was checked directly against D-A4's verbatim text
  (connected; power-free; exactly one vertex of degree \(<3\); that
  vertex of degree 1 or 2) rather than against a remembered version, and
  against `L025` R4's degree-1 assembly for the converse.
- Before concluding that `L029` was vacuous, `A012` T4's proof was
  re-read line by line to find which degree its 1-atom actually has —
  which is what produced the repair rather than a retraction.
- The same re-reading found the independent defect in Remark T4.1, which
  had not been part of the original question.
- The correction was deliberately stated in the direction that *loses*
  the dossier a target, and the surviving reduction was checked for
  non-vacuity (T3) rather than assumed.
- No search result was re-interpreted: every scan ever run over the
  one-sub-cubic-vertex profile covers tight 1-atoms, so `C027`/`C034`
  transfer unchanged.

## Canonical records changed

- [x] `STATEMENT.md` (unchanged; statement version stays 0.1)
- [x] `STATE.md` (established facts, program status, obligations, the new
      tiered roadmap, human-level state, outlook, resume list)
- [x] `CLAIMS.md` (`L036` new; `L029` restated; `C034` extended to order
      22 and reworded; dependency notes)
- [x] `OBLIGATIONS.md` (`G013`(a) rewritten, ceiling corrected, `G015`
      opened)
- [x] `PROOF.md`
- [x] `DECISIONS.md`
- [x] `LOG.md`
- [x] `problem.json` and index
- [x] Session-scoped changes committed
- [x] Commit pushed to configured upstream

## Ending checkpoint

- Current frontier: unchanged for statement 0.1 (\(\ge19\) vertices);
  pinched catalogue through order 16 (S017); parity/bipartite channel
  empty through order 22; the assembly programme's proof-side ceiling
  now correctly stated as the cubic reduction, with the conjecture-complete
  object removed from the live list.
- Remaining blockers: `G015` (new, Tier 1), `G013` (tight 1-atoms; the
  block question; the gcd channel), `G014`, `G007`, `G002`, `G003`.
- Recalibration decision: pivoted at the architecture level — the
  portfolio was retiered around a named deliverable rather than around
  cheap decisive searches.
- Best live alternative or reframing: route R2 of `G015` (Carr
  \(4/7\to1\)) if R1 stalls; Tier 2's bipartite EGC.
- Pivot trigger: a proof of either `G015` route (Thread C then becomes
  the whole game); any power-free member of the `E015` class at order
  23+; a `G014` audit overturning an assumed bound.
- Best next action: attack `G015` route R1 — prove no tight 1-atom
  exists, or find one. First concrete move: the structure of a
  minimum-order tight 1-atom (its degree-2 vertex, its \(C_4\)-free
  neighbourhood, and whether `L030`/`L033`-style collapse arguments
  apply to the one-terminal object), with the order-\(\le15\) emptiness
  of `C027` and the bipartite-\(\le22\) emptiness of `C034` as the
  base data. Tier 3 legs (order-23 bipartite, the gcd scan) run in
  background only.
- Files a new session should read: `STATE.md` (roadmap first), `A018`,
  `A017` + `E015/README.md`, `A016`, `CLAIMS.md` `L029`/`L034`–`L036`,
  `OBLIGATIONS.md` `G015`/`G013`.

## Plain-language recap

The user asked why sixteen sessions in a row had put off the "single
defect" question — a graph that would be a counterexample except for one
vertex of too-low degree — even though every summary called it the most
valuable open piece. The answer turned out to be mathematics, not
avoidance. If a counterexample to the conjecture exists, hang one extra
dangling vertex off it: the dangling vertex sits on no cycle, so nothing
about the cycle lengths changes, and you now have a graph with exactly
one low-degree vertex. That is a single-defect graph. The reverse was
already known. So the two questions are the same question — deferring it
was, unknowingly, declining to prove the conjecture that afternoon, and
the dossier had been advertising it as a stepping stone.

The fix is small and clarifying. The reduction the dossier built on it
survives if the defect vertex is required to have degree exactly two,
and that stricter version is exactly what the original proof used. So the
programme's real proof-side prize is now a single named theorem: the
conjecture holds in general if and only if it holds for 3-regular
graphs. That has two independent routes — one internal, one strengthening
a published result that says at least 4/7 of a minimal counterexample is
3-regular — and neither goes through the circular object. The whole
portfolio was reorganised around it into tiers, with the searches
demoted to background work that runs but no longer counts as the
session's job. One of those searches finished mid-session: the
two-colourable hunt is now clean through 22 vertices.

## Proposed next step

Attack the named deliverable: prove that no "tight" single-defect graph
exists — a power-free graph whose one low-degree vertex has exactly two
neighbours — or find one. Finding one would disprove the conjecture
outright; proving none exists would establish that the conjecture reduces
to 3-regular graphs, which is the first result this project would have
that is about the conjecture rather than about its own machinery. The
concrete first move is to work out the forced local structure around
that degree-2 vertex and see whether the collapse arguments that closed
earlier two-terminal cases transfer to the one-terminal object, using the
existing exhaustive emptiness data (all graphs to 15 vertices, all
two-colourable graphs to 22) as the base. Considered and deferred: the
second route to the same theorem (strengthening the published 4/7
result, which first requires verifying that argument); the bottleneck
"pencil endgame", now background; and the remaining arithmetic channel,
also background.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 4%
- Previous estimate, if any: 4% (S016)
- Reason for change: none. The session improved the map rather than the
  terrain. Removing a circular target and naming a reachable one makes
  the remaining work better aimed, but it also makes explicit that six
  sessions of assembly work had a smaller ceiling than recorded; the two
  effects roughly cancel. Nothing proved here moves the conjecture
  itself.
- Basis: most promising routes — the cubic reduction (both routes) on
  the proof side, the 3-regular census at order 30 on the disproof side;
  strongest obstacles — no forcing mechanism exists at minimum degree 3,
  and the reachable theorem is a reduction rather than a resolution;
  evidence — `L036`, the repaired `L029`, and the order-22 extension of
  `C034`.

This is a subjective research outlook, not mathematical evidence or a claim-status
promotion.
