# S014 — Dissect the five band-6 taut witnesses and survey all taut pinched pairs through order 14: hunt the first C8-forcing mechanism

- Date: 2026-07-24
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1
- Work / claim status: `active` / `open`
- Strongest established facts: `L022` (counterexamples \(\ge19\)
  vertices); `L025`–`L029` atom/rung/lobe program; `L030` (taut
  \(s_{\min}=3\) rung closed \(C_4\)-only); `C028` (five taut pinched
  witnesses at orders 12–13, all \(S=\{6,\dots,11\}\), each with a
  \(C_8\)); `C029` (all-pair \(S\subseteq\{3,4,5\}\) scan empty through
  order 14).
- Open obligations in scope: `G013` (1-atoms; taut 2-atoms with
  \(s_{\min}\ge4\)), `G007`, `G003`.
- Inherited next action: the taut \(s_{\min}=4\) rung — extend the
  `L030` collapse to depth-2 middles, or find a taut pinched
  \(s_{\min}\in\{4,5\}\) gadget at orders 14–16.
- User input this session: consider prioritizing the five band-6
  witnesses — compare shared structure, isolate why each forces a
  \(C_8\) — explicitly flagged as a consideration, not a command, with
  an instruction not to bias toward it.
- Session goal: locate the first genuinely power-specific forcing
  mechanism, or produce the evidence that none exists at band 6.
- Falsifiable next move: full taut-pinched catalogue over all terminal
  pairs through order 14 (any band); one \(s_{\min}\in\{4,5\}\) hit
  fires the inherited pivot immediately.

## Strategy audit

- Why the inherited route might work: the `L030` collapse closed
  \(s_{\min}=3\) cheaply and depth-2 middles are its natural
  continuation. Fastest kill: exhibit a taut \(C_4\)-free pinched
  gadget with \(s_{\min}\in\{4,5\}\). **Resume reading found the search
  half of this route is not actually done:** `C029` certifies emptiness
  for \(S\subseteq\{3,4,5\}\) only (`E012` aborted on any length-6
  path), so the rung's real target \(S\subseteq\{4,\dots,7\}\) has
  never been searched beyond `C028`'s sub-cubic-terminal survey at
  orders 12–13. `STATE.md`'s "s_min in {4,5} empty through 14 over all
  terminal pairs" overstates `C029`; a band-4/5 gadget at order
  \(\le14\) would doom the depth-2 proof attempt, so the search must
  precede the proof effort regardless of route choice.
- Why the witness route might work: the five known taut pinched gadgets
  are the only concrete objects in the whole dossier where structure
  visibly forces a power cycle. Resume reading surfaced an unrecorded
  regularity: **all five have the identical cycle spectrum
  \(\{3,5,6,7,8,9,10,11\}\)** and identical \(S=\{6,\dots,11\}\),
  across two different orders — suggesting one structural family, not
  five accidents, hence a shared, extractable forcing mechanism.
  Fastest kill: compute the \(C_8\) censuses; if they are heterogeneous
  and the \(C_8\)s die under in-class local surgery, the shared-mechanism
  hope is dead and the same data redirects to disproof-material hunting.
- Mechanistically distinct alternative: minimal 1-atom structure theory
  (the degree-2 vertex and parity-shift smoothing). Deferred — no new
  lever identified, and it lacks the concreteness the witnesses supply.
- Selected route and reason: a two-part session. Part 1 (`E013`): the
  exhaustive all-band taut-pinched catalogue over **all** admissible
  terminal pairs, orders 6–14 — this is simultaneously the inherited
  route's missing search half (first real coverage of
  \(s_{\min}\in\{4,5\}\)) and the witness route's catalogue completion
  (are the five the whole story through 14?). Part 2: dissect every
  band-6 witness — \(C_8\) census and coverage, BFS-layer structure,
  family relations, in-class surgery — targeting a candidate forcing
  statement (taut + \(C_4\)-free + pinched at \(d(a,b)=6\) forces a
  \(C_8\)) with a proof shape or a refutation direction. Reason:
  expected research value, not deference — the depth-2 \(C_4\)-only
  collapse is a mechanism already known to die by band 6 (`C028`),
  while the recorded reason the outlook sits at 2% is that the power
  fight has never been engaged; the decisive new evidence for
  reprioritizing is the `C029` coverage gap plus the identical-spectra
  regularity, both found at resume, not the user's framing.
- Pivot criterion: an `E013` hit at \(s_{\min}\in\{4,5\}\) → branch on
  power-freeness at once (power-free = 2-atom = disproof protocol;
  else power-relativized rung analysis). Dissection shows heterogeneous
  or surgery-fragile \(C_8\)s → drop the band-6 forcing conjecture,
  switch to hunting \(C_8\)-free taut pinched band-6 gadgets at orders
  15–16 or back to the \(s_{\min}=4\) collapse.

## Work performed

- Built `E013` (`catalogue.py`): the first all-band taut-pinched scan
  over every admissible terminal pair of the `E010` stream, orders 6–14,
  in strict (ratio \(<2\)) and closed (ratio \(\le2\)) modes; plus a
  full dissection stack (exact cycle census, through-path edge systems,
  interference tests, cut vertices, two-terminal isomorphism
  cross-anchored against nauty labelg, pendant reduction/lift builders).
  88 anchors.
- Strict catalogue: exactly six taut pinched (D)-pairs at orders
  \(\le14\), none at order 14 — the five `C028` witnesses plus a **new
  band-5 witness at order 11** (\(S=\{5,6,8,9\}\), spectrum
  \(\{5,6,8,9\}\)). The strict \(s_{\min}=4\) rung target is genuinely
  empty through order 14 (`C030`), repairing the `C029` overstatement.
- Dissection: every witness has exactly one cut vertex and terminal
  degrees (1,2). Proved the **pendant reduction/lift** (`L031`, A014
  T1–T2) and the **chain/block extraction theorem** (`L032`, A014
  T3–T4): taut 2-atoms exist iff a power-free vertex-taut 2-connected
  core with \(s_{\max}\le2\,s_{\min}\) exists. Found and machine-verified
  the sharpness example (A014 T5, anchor A9): two Petersen\(-e\) blocks
  joined by a bridge form a strict taut core of order 20 — killing
  core-level spread-doubling and fixing blocks as the right level.
- Closed catalogue + core extraction (`C031`): five 2-connected blocks
  through order 14 — Petersen\(-e\) (band 4, identified canonically),
  A11/B11 (band 5), C12 (band 5), D14 (band 6, order 14, found this
  session) — all at exact equality \(s_{\max}=2s_{\min}\), no strict
  block; the six witnesses are exactly their distinct pendant lifts
  (bijection machine-verified; labelg cross-check).
- Interference census: every \(C_8\) in every block and witness is the
  symmetric difference of two through-paths (23/23); every block has an
  internally disjoint pair of shortest through-paths; at band 4 that
  pair forces \(C_8\) directly.
- Fixed a real bug found by cross-validation: the isomorphism engine's
  terminal constraint was set-based and could not see orientation; made
  it ordered, added orientation anchors and the labelg cross-anchor.
- Updated `CLAIMS.md` (`L031`/`L032`, `C030`/`C031` + notes),
  `OBLIGATIONS.md` (`G013` → block question), `PROOF.md`,
  `DECISIONS.md`, `LOG.md`, `STATE.md`, `problem.json`.

## Results

- Proved claims: `L031` (pendant reduction/lift bijection; strict pinch
  upstairs = closed ratio downstairs; spectra preserved), `L032` (chain
  decomposition; block extraction; taut 2-atoms ⇔ power-free taut
  2-connected core with \(s_{\max}\le2s_{\min}\); sharpness composite).
- Refuted in-session: naive core-level spread-doubling (the bridge
  composite is a strict taut core) — caught before it was recorded as a
  conjecture, and retained as A014 T5.
- Computational evidence: `C030` (strict catalogue: six witnesses, rung
  \(s_{\min}=4\) empty through 14), `C031` (closed catalogue: five
  equality blocks, no strict block, lift bijection, Petersen\(-e\)
  identification, interference census 23/23).
- Provisional insights (finite observations, not lemmas): every known
  block sits at exact equality; every known \(C_8\) is two-path
  interference; the band-4 disjoint-4-path mechanism; D14's swap
  symmetry predicts exactly one strict band-7 witness at order 15.
- Imported facts needing verification: none new (Petersen facts used
  are classical and were re-verified computationally in-anchor).

## Failed routes and why

The inherited depth-2 collapse attack on the (D)-form \(s_{\min}=4\)
rung was not executed this session: the strategy audit found its search
half unsupported (the `C029` gap) and the witness dissection
higher-value; the rung survives in sharpened block form as next action.
The one killed formulation is core-level spread-doubling (see above).

## Adversarial check

- The lift/witness bijection, the block census, and the Petersen\(-e\)
  identification were each verified by two independent routes (the
  backtracking engine vs nauty labelg canonical forms; witness-side
  extraction vs direct closed-scan discovery). The initial disagreement
  they exposed was a genuine bug (orientation-blind terminal
  constraint), fixed and re-anchored.
- An apparent contradiction — order-13 closed hits should lift to
  order-14 strict witnesses, but the strict-14 scan was empty — was
  chased to ground: those hits have terminal degrees (2,1), so their
  lifts violate condition (D) (terminal degree sum 2). The resolution is
  now part of T1/T2's degree bookkeeping.
- T4's bridge-counting was stress-tested against the composite family
  (equality blocks + bridges realize strictness; all-excess-\(\ge1\)
  chains cannot satisfy the count) before being recorded.
- All scans assert stream totals against `C027`, re-find the `C028`
  witnesses at their recorded pairs, and check strict/closed subset
  consistency at every order; the T5 composite is a permanent anchor.

## Canonical records changed

- [ ] `STATEMENT.md` (unchanged; statement version stays 0.1)
- [x] `STATE.md`
- [x] `CLAIMS.md` (`L031`, `L032`, `C030`, `C031` + dependency notes)
- [x] `OBLIGATIONS.md` (`G013` refined to the block question)
- [x] `PROOF.md` (outline: pendant/block reduction added; `G013` gap
  rescoped)
- [x] `DECISIONS.md` (block reframing; `C029` overstatement repair;
  route-selection record)
- [x] `LOG.md`
- [x] `problem.json` and index
- [x] Session-scoped changes committed
- [x] Commit pushed to configured upstream

## Ending checkpoint

- Current frontier: finite exclusions unchanged (`L022`); disproof
  interface: 1-atoms (order \(\ge16\)) and the block question
  (power-free taut 2-connected core, \(s_{\max}\le2s_{\min}\), order
  \(\ge16\)); exact catalogue through 14: six strict witnesses = lifts
  of four equality blocks, plus D14; no strict block known.
- Remaining blockers: `G013` (both sub-questions), `G007`, `G002`,
  `G003`.
- Recalibration decision: pivoted (within `G013`) — the witness
  dissection replaced the inherited depth-2 collapse for the recorded
  audit reasons; the rung ladder survives in sharpened block form.
- Best live alternative or reframing: 1-atom structure theory; the
  band-5 equality analogue of the power rung.
- Pivot trigger: a strict block found (kills the strict rung, reweights
  toward disproof); a \(C_8\)-free equality block found (disproof
  protocol: \(C_{16}\) check, lift, ring); both band-4 attacks stalling.
- Best next action: the band-4 block rungs — strict impossibility
  (\(S\subseteq\{4,\dots,7\}\)) and equality \(C_8\)-forcing
  (\(S\subseteq\{4,\dots,8\}\Rightarrow C_8\)) — with the order-15
  closed catalogue (PyPy) as the search leg.
- Files a new session should read: `STATE.md`, `A014`,
  `E013/README.md`, `A013`/`A012`/`A011` background, `CLAIMS.md`
  `L025`–`L032`/`C027`–`C031`, `OBLIGATIONS.md` `G013`, this session.

## Plain-language recap

The project's disproof strategy needs a small two-terminal graph that
avoids power-of-two cycles while keeping every terminal-to-terminal
path length within a factor of two. Five such near-misses were known;
the user suggested dissecting them to find what forces the fatal
8-cycle in each. The dissection found something better than a shared
quirk: a shared anatomy. Every near-miss is a one-edge antenna glued
onto a two-terminal "engine" whose path lengths span exactly a factor
of two — and one of the engines is the famous Petersen graph with one
edge removed. Two new theorems make this anatomy the whole story: the
antenna trick is fully reversible, and any candidate gadget chops at
its bottlenecks into a chain of engines, so the entire question
collapses onto single well-connected engines with path-spread at most
two. An exhaustive machine catalogue (every candidate graph up to 14
vertices, every choice of terminals, seven million pair-checks) found
exactly five engines — including a sixth near-miss and a new engine no
earlier search could see — and every one sits at spread exactly two,
kept from disproving the conjecture by precisely one thing: an 8-cycle
that always arises as the overlay of two terminal-to-terminal paths.
The session also caught and repaired an overstatement in the previous
records (a search had been credited with more coverage than it had) and
found, mid-session, a trap in its own emerging theory: gluing two
Petersen engines with a bridge beats the naive spread conjecture, which
is why the theorems are stated at the level of single well-connected
engines. What remains is a clean fight with a lab: prove every engine
must contain an 8-cycle, or find a bigger engine that dodges it.

## Proposed next step

Attack the smallest open engine case, path-spread band 4: prove that no
well-connected engine keeps all its paths at lengths 4-to-7 (the strict
case, empty in all searches so far), and prove that any engine with
paths 4-to-8 must contain an 8-cycle (the power case, where the
Petersen engine is the guide and the known mechanism — two
non-overlapping length-4 paths always closing into an 8-cycle — is the
candidate proof idea). In parallel, extend the exhaustive engine
catalogue to 15 vertices. Either proof extends the ladder with the
first genuinely power-specific rung; a counterexample engine at 15+
vertices would be concrete disproof material. Considered and deferred:
structure theory for the "1-atom" (the other gate of the conjecture's
reduction to 3-regular graphs), and the band-5 analogue of the power
case.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 3%
- Previous estimate, if any: 2% (S013)
- Reason for change: the taut half of the disproof interface is now a
  single sharply-searchable object (the block question) with an exact
  small catalogue, an identified extremal structure (Petersen minus an
  edge), and a concrete candidate mechanism for the first
  power-specific rung (two-path interference). For the first time the
  power fight has both a clean statement and a laboratory. The increase
  is small because the equality phenomenon and the \(C_8\)-forcing are
  finite observations that may fail at order 15+, the block question is
  open in both directions, and the 1-atom question is untouched.
- Basis: most promising routes — the band-4 block rungs with the
  interference mechanism, and the order-15 catalogue; strongest
  obstacle — nothing yet forces cycle-length spread or a power cycle
  from power-freeness at any generality; evidence — `L031`/`L032`,
  the exact `C030`/`C031` catalogue, and the 23/23 interference census.

This is a subjective research outlook, not mathematical evidence or a claim-status
promotion.
