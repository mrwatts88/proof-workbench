# S013 — Close the taut s_min=3 rung: C4-freeness alone excludes taut gadgets with through-set in {3,4,5}

- Date: 2026-07-24
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1
- Work / claim status: `active` / `open`
- Strongest established facts: `L022` (counterexamples \(\ge19\)
  vertices); `L023`–`L024` collision-wall theorem (reviewed `R001`);
  `L025` atom reduction; `L026`–`L029` corrected rung program (taut
  rungs \(s_{\min}\le2\) closed \(C_4\)-only; cubic reduction modulo
  1-atoms); `C027` (atom class empty through order 15); `C028` (taut
  pinched world starts at \(s_{\min}=6\) through order 13).
- Open obligations in scope: `G013` (both sub-questions), `G007`;
  `G002`/`G003` background; `G004` peripheral.
- Inherited next action: attack the taut \(s_{\min}=3\) rung — prove no
  vertex-taut \(C_4\)-free power-free (D)-gadget with
  \(S\subseteq\{3,4,5\}\) exists, or exhibit one (disproof via `L025`
  R3); expectation on record: this is the first rung where
  power-freeness beyond \(C_4\) must carry the argument.
- Session goal: close the rung in either direction.
- Falsifiable next move: attempt the construction first — build a taut
  \(C_4\)-free gadget with \(S\subseteq\{3,4,5\}\) from the constraint
  structure; any successful build kills the impossibility hope
  immediately (and, if power-free, disproves 0.1).

## Strategy audit

- Why the inherited route might work: the \(s_{\min}=2\) rung fell to a
  short \(C_4\)-only forcing chain (`L028`), and `C028`'s survey says the
  \(s_{\min}=3\) target is empty through order 13 even before
  \(C_8\)-freeness is imposed — suggesting either a slightly deeper
  \(C_4\)-only argument or a first genuine power-spectrum argument, with
  \(K_{3,3}-e\) marking the exact shape to beat.
- Fastest way to falsify it: build the gadget. The construction attempt
  was run first and collapsed step by step into forced structure — each
  freedom the builder has is removed by a forbidden length-6/7 path or a
  forced \(C_4\) — terminating in a contradiction dichotomy. The
  falsification attempt became the proof.
- Mechanistically distinct alternative or reframing: (a) minimal 1-atom
  structure theory (the disproof side's load-bearing unknown); (b)
  order-16 census (finite information, heavy compute, no mechanism); (c)
  direct \(C_8\)-forcing at the \(s_{\min}=6\) witnesses (the eventual
  real fight). All deferred: the inherited rung was the sharpest target
  and it closed within the session.
- Selected route and reason: the inherited rung, executed failure-first.
  It produced `L030` with a mechanism (middle-layer collapse) that is a
  candidate for the next rung.
- Pivot criterion: a construction satisfying all accumulated constraints
  at any stage — none materialized.

## Work performed

- Opened attempt `A013`; proved T1 (codegree rules), T2 (middle coverage
  and the tautness workhorse: every middle vertex sits at distance one
  from \(N(a)\) or \(N(b)\), via the position analysis on length-\(\le5\)
  paths), T3 (degree inventory), T4 (the one-sided middle classes \(P\),
  \(Q\) are empty — no \(P\)–\(P\)/\(Q\)–\(Q\)/\(P\)–\(Q\) edges, then
  two \(R\)-neighbors give a length-6 path), T5 (the middle is a perfect
  matching of degree-3 triples), T6 (X-edges exclude middle contact), T7
  (the middle is empty — the matched-pair analysis kills both the
  \(x_m\ne x_{m'}\) and \(x_m=x_{m'}\) cases by degree starvation), T8
  (three-matchings endgame: each \(x\) triggers either a \(C_4\) block,
  \(\sigma\varphi(x)=\psi\sigma(x)\), or a length-7 path) — the theorem
  `L030` — plus corollaries C1–C3 (taut 2-atoms have \(s_{\min}\ge4\),
  \(s_{\max}\ge6\); 2-atoms with \(s_{\min}=3\) are non-taut, route
  through `L027` lobes, and have order \(\ge19\); ladder status).
- Built experiment `E012` (`scan_pairs.py`): all-terminal-pair
  falsification search over the `E010` stream class, with two proved-
  necessary prefilters (distance, eccentricity) and an exact
  abort-on-length-\(\ge6\) all-simple-paths DFS; 736 anchor checks
  including the T8 endgame dichotomy verified exhaustively on all 218
  three-matchings structures at \(k\in\{2,4\}\), \(K_{3,3}-e\) as the
  positive control, the five `E011` taut pinched gadgets as negative
  controls, and stream totals asserted against `C027` records.
- Ran the scan at orders 6–14 (order 14: 5,605,161 stream graphs,
  241,135 eligible, 1,357,597 pairs, 160.2s CPython).
- Updated `CLAIMS.md` (`L030`, `C029` + dependency notes),
  `OBLIGATIONS.md` (`G013` refined), `PROOF.md`, `DECISIONS.md`,
  `LOG.md`, `STATE.md`, `problem.json`.

## Results

- Proved claims: `L030` — no vertex-taut \(C_4\)-free (D)-gadget has
  \(S\subseteq\{3,4,5\}\); equivalently taut + \(C_4\)-free +
  \(d(a,b)\ge3\) forces an \(a\)–\(b\) path of length \(\ge6\).
  Power-freeness beyond \(C_4\) and the (D) sum clause are never used.
  Corollaries: every taut 2-atom has \(s_{\min}\ge4\) and
  \(s_{\max}\ge6\); every 2-atom with \(s_{\min}\le3\) contains a 1-atom
  or a min-degree-3 power-free graph, with order \(\ge19\) at
  \(s_{\min}=3\).
- Provisional insights: S012's boundary prediction corrected — the
  power-spectrum fight starts not at \(s_{\min}=3\) but somewhere in
  \(s_{\min}\in\{4,5,6\}\); the upper end is pinned by `C028`'s five
  witnesses (taut, \(C_4\)-free, pinched, \(s_{\min}=6\), each with a
  \(C_8\)), so \(C_4\)-only methods provably cannot close \(s_{\min}=6\).
  The collapse mechanism (position analysis → class elimination →
  matching rigidity → endgame dichotomy) is the candidate tool for
  \(s_{\min}=4\), where depth-2 middles are the genuinely new case.
- Computational evidence (`C029`): zero taut hits at orders 6–14 over
  every admissible terminal pair — including the degree-\(\ge3\)-terminal
  slice never examined by `E011`/`C028` (at order 13: 20,432 eligible
  graphs vs 16,106) — and, stronger than the theorem predicts, zero
  non-taut pairs with \(S\subseteq\{3,4,5\}\) either (recorded as an
  observation; by `L026`-type constructions that emptiness is
  conjecture-strength and must not be cited as a lemma). The T8
  dichotomy holds exactly on all 218 small three-matchings structures.
- Imported facts needing verification: none new this session.

## Failed routes and why

None abandoned. The one corrected item is a prediction, not a route:
the S012 expectation that power-freeness must carry \(s_{\min}=3\) is
refuted by `L030` itself; the record now locates the \(C_4\)-only/power
boundary in \(s_{\min}\in\{4,5,6\}\).

## Adversarial check

- The proof was re-derived once as a construction collapse and once as
  the linear T1–T8 chain; every forbidden path was checked edge by edge
  and vertex-distinctness by class partition (\(\{a\},\{b\},X,Z,M\));
  the delicate spots — T2(ii)'s position analysis (why \(v_3\notin
  X\cup Z\)), T4 Step 2's choice quantifiers (\(v\ne u\), \(s\ne w\)),
  T7's two cases (why \(x_{m'}\not\sim m\); why \(x''=x\) gives a
  \(C_4\) but \(x''\ne x\) a length-6 path), and T8's distinctness
  bookkeeping (\(x_j\ne\varphi(x_1)\) is exactly the Case-B assumption)
  — were each rechecked in isolation.
- Hypothesis inventory (T8.1) audited: tautness is used only in T2;
  dropping it is provably fatal (`L026` makes the tautness-free version
  conjecture-complete), and \(K_{3,3}-e\) shows \(C_4\)-freeness is
  indispensable — the theorem's hypotheses are each load-bearing.
- `E012` could have refuted the theorem on 1.36M+ terminal pairs at
  order 14 alone and did not; its anchors include a positive control
  (the scan *does* flag \(K_{3,3}-e\) as taut-\(\{3,5\}\)), an
  exhaustive endgame check (218/218 structures, both dichotomy branches
  realized), negative controls, and stream-total asserts against
  `C027`; the DFS/BFS minimum-length consistency assert ran on every
  completed pair.
- The premature-numbers slip (an order-14 table row drafted before the
  run finished) was caught and blanked before the run completed; the
  committed row was copied from `data/pairs_n14.json` output.

## Canonical records changed

- [ ] `STATEMENT.md` (unchanged; statement version stays 0.1)
- [x] `STATE.md`
- [x] `CLAIMS.md` (`L030`, `C029` + dependency notes)
- [x] `OBLIGATIONS.md` (`G013` refined)
- [x] `PROOF.md` (outline: `L030` added; gap list rescoped)
- [x] `DECISIONS.md` (rung closed; boundary prediction corrected)
- [x] `LOG.md`
- [x] `problem.json` and index
- [x] Session-scoped changes committed
- [x] Commit pushed to configured upstream

## Ending checkpoint

- Current frontier: finite exclusions unchanged (`L022`); disproof
  interface: 1-atoms (order \(\ge16\)) and taut 2-atoms with
  \(s_{\min}\ge4\), \(s_{\max}\ge6\); taut ladder closed \(C_4\)-only
  through \(s_{\min}=3\), provably not closable \(C_4\)-only at
  \(s_{\min}=6\); target empty through order 14 over all terminal pairs.
- Remaining blockers: `G013` (both sub-questions), `G007`, `G002`,
  `G003`.
- Recalibration decision: continued — the inherited route closed as a
  theorem; its boundary prediction was corrected in passing.
- Best live alternative or reframing: direct \(C_8\)-forcing at the
  \(s_{\min}=6\) witnesses; then 1-atom structure theory; order-16
  census deferred.
- Pivot trigger: a taut pinched \(s_{\min}\in\{4,5\}\) gadget found
  (branch on power-freeness: disproof protocol vs power-relativized
  rung); or the depth-2 cascade stalling after honest effort (switch to
  \(C_8\)-forcing or 1-atom theory).
- Best next action: attack the taut \(s_{\min}=4\) rung — prove no taut
  \(C_4\)-free (D)-gadget has \(S\subseteq\{4,5,6,7\}\) (extend the
  collapse to depth-2 middles), or find a \(C_4\)-free taut pinched
  \(s_{\min}\in\{4,5\}\) gadget at orders 14–16.
- Files a new session should read: `STATE.md`, `A013`, `A012`, `A011`,
  `E012/README.md`, `CLAIMS.md` rows `L025`–`L030`/`C027`–`C029`,
  `OBLIGATIONS.md` `G013`, this session.

## Plain-language recap

The project's disproof strategy needs a small two-terminal graph that
avoids power-of-two cycles while keeping every terminal-to-terminal
path in a narrow band of lengths. Last session proved the two narrowest
bands impossible for "taut" gadgets — those where every vertex actually
serves some terminal-to-terminal path — and predicted that the next
band, path lengths 3 through 5, would be the first fight where the
power-of-two structure itself must be used. This session settled that
next band, and the prediction was wrong in an informative way: lengths
3-through-5 is *also* impossible using only the absence of 4-cycles.
The proof is a collapse argument: the path-length ceiling squeezes the
gadget's middle region class by class until nothing remains but a rigid
skeleton — three perfect matchings knitting the two terminal
neighborhoods — and that skeleton always contains either a 4-cycle or a
path of length 7, both fatal. A machine search over every terminal
choice in every candidate graph up to 14 vertices (5.6 million graphs,
1.36 million terminal pairs, including terminal types no earlier search
covered) found nothing, exactly as the theorem demands, and verified
the proof's final dichotomy exhaustively on all 218 of its small
endgame structures.

The larger picture sharpened: the known "honest" gadgets at band 6–11
show the 4-cycle-only free ride must end by band-start 6, so the real
confrontation with the power-of-two spectrum now sits in band-starts 4
and 5 — one step away, with a working mechanism in hand.

## Proposed next step

Attack the band-start-4 case: prove that no taut, 4-cycle-free gadget
can keep all its connection paths at lengths 4 through 7, or find one
at 14–16 vertices. This extends this session's collapse mechanism to
its first genuinely new configuration — middle vertices sitting two
steps deep from both terminal neighborhoods — and either outcome is
decisive for the map: a proof pushes the 4-cycle-only regime to its
provable limit; a found gadget (if power-free, it disproves the
conjecture outright; if not) marks exactly where the 8-cycle fight
begins. Considered and deferred: proving directly that the known
band-6 gadgets must always contain an 8-cycle (the real power fight,
guided by five concrete examples), and structure theory for the
"1-atom" object that still gates the conjecture's reduction to
3-regular graphs.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 2%
- Previous estimate, if any: 2% (S012)
- Reason for change: none. The session closed its rung cleanly and one
  step cheaper than predicted, but the mechanism that closed it is
  provably insufficient at \(s_{\min}=6\), so the conjecture's core
  difficulty — extracting a forced power cycle from power-freeness —
  has still not been engaged. Boundary-mapping progress, not
  penetration.
- Basis: most promising routes — the \(s_{\min}=4\) rung with the
  collapse mechanism in hand, and \(C_8\)-forcing at the five concrete
  \(s_{\min}=6\) witnesses; strongest obstacle — nothing yet forces
  cycle-length spread from power-freeness at any generality (`L026`
  shows the shortcuts are illusions); evidence — `L030`, `C029`'s
  clean 14-vertex sweep, `C028`'s witness catalogue.

This is a subjective research outlook, not mathematical evidence or a claim-status
promotion.
