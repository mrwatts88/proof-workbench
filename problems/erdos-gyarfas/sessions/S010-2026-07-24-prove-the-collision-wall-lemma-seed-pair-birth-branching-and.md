# S010 — Prove the collision-wall lemma: seed-pair birth, branching, and the four-junction gluing

- Date: 2026-07-24
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1
- Work / claim status: `active` / `open`
- Strongest established facts: `L001`–`L022` (order bound \(\ge19\);
  saturation package; lift machinery `L019`–`L021`); certificate program
  closed exhaustively on tested bases/groups (`C020`–`C022`).
- Open obligations in scope: `G012` (collision-wall lemma, primary);
  `G002`/`G003`/`G007` (global mechanism); `G004` (1997 body only).
- Inherited next action: attempt the collision-wall lemma — every
  assignment over every finite group on every connected min-degree-3 base
  admits an identity-voltage tailless nb closed walk of length \(2^k\)
  for every \(2^k\ge C\log_2\lvert\Gamma\rvert+C_B\); only the
  first/last-arc diversity bookkeeping was open.
- Session goal: prove it, or extract the structured counterexample family
  that blocks it.
- Falsifiable next move: write the composition construction in full;
  each junction condition either closes or names the exact configuration
  that resists.

## Strategy audit

- Why the inherited route might work: the construction was already
  explicit up to bookkeeping (`A009`), the coset-confinement escape was
  already ruled out (undirectedness forces confinement period \(\le2\)),
  and the E008 data matches the predicted wall with margin.
- Fastest way to falsify it: exhibit an assignment whose same-voltage
  walk pairs at some target length all share their first or last arc — a
  value-confinement family. The drafting phase confronted this directly:
  a fiber whose pairs all share first or last arcs is forced to be
  all-same-first or all-same-last (a dichotomy checked while drafting),
  and pure counting cannot exclude adversarial fibers, which is exactly
  why the final proof abandons fiber pigeonhole at the target length in
  favor of one seed collision plus deterministic steering.
- Mechanistically distinct alternative or reframing: the proof-side
  controlled-start consecutive-even-lengths lemma directly (deferred —
  W7's even-length interval conclusion now feeds it with a stronger
  starting point than anything it would have derived alone).
- Selected route and reason: the inherited route, unchanged — highest
  expected value (closes `G012`, closes the lift chapter as a theorem,
  and its proof-side reading is the strongest quantitative fact yet for
  `G007`), and the session start immediately found the missing idea
  (branch-and-steer with the four-junction gluing), removing the reason
  it was ever "bookkeeping-blocked."
- Pivot criterion: an unfixable gap in exact-length steering or junction
  legality; none fired.

## Work performed

- Opened attempt `A010` and proved the collision-wall lemma in full:
  - **W1** branching bound (\(\ge2\) continuations per arc, so
    \(2^{L-1}\) walks per first arc);
  - **W2** no nonempty continuation-closed arc set is reverse-free
    (arc-end counting at head-vertices; loops handled by the two-end
    accounting);
  - **W3** the arc digraph of a connected min-degree-3 multigraph is
    strongly connected (weak connectivity by two local moves; the
    reversal anti-automorphism maps sink components to source
    components; W2 forces a reverse pair inside a sink component,
    collapsing the condensation);
  - **W4** the nb period is 1 or 2, equal to 2 exactly for bipartite
    bases (loops and parallel pairs directly; simple case via the
    longest-path endpoint's three chords, whose three cycle lengths
    satisfy \((i{+}1)+(j{-}i{+}2)-(j{+}1)=2\) — no Bondy–Vince import
    needed);
  - **W5** uniform exact-length reachability \(R_B\) (class function
    well-defined mod \(p\); closed-walk length semigroup has gcd \(p\)
    and finite Frobenius bound);
  - **W6** seed pair by pigeonhole at
    \(\ell^*=\lfloor\log_2(2m\lvert\Gamma\rvert)\rfloor+2\) with maximal
    common prefix trimming (distinct firsts, shared last, equal voltages,
    length in \([2,\ell^*-1]\));
  - **W7** the main theorem: branch the seed along two continuations,
    steer both to a common vertex with two distinct final arcs at
    exact lengths (W5), and glue
    \(\Omega=U\cdot\mathrm{rev}(Y)\cdot Y'\cdot\mathrm{rev}(U')\); four
    junction checks close structurally; voltage telescopes to identity
    in any group; length is exactly the target. Thresholds: every
    \(L\equiv0\bmod4\) (every even \(L\) if non-bipartite) with
    \(L\ge4\ell^*+4R_B+8\); for powers,
    \(2^k\ge4\log_2\lvert\Gamma\rvert+C_B\) with
    \(C_B=4\lceil\log_2m\rceil+4R_B+24\) and absolute constant \(C=4\);
  - **W8** corollary: effective certificate death for all large groups
    on every base — the closing theorem `G012` asked for.
- Built experiment `E009` (`wall.py`): definition-level walk checker,
  W3/W4 verification with pre-registered expected periods, empirical
  \(R_B\) with stable-tail requirement, seed-property asserts, the full
  W7 assembly, negative controls, cross-engine anchor against the E008
  DP, exhaustive small sweeps (all assignments on four base×group
  cases). Full run: 9,606,333 assertions, all passing (Python 3.14.2).
- Opened review `R001` (manual record; `proofctl review` gates on
  main-statement candidates) and delegated a fresh-context logic audit
  of A010 to the proof-reviewer subagent.

## Results

- Proved claims (promoted after the R001 pass): `L023` (arc-digraph
  structure package, W2–W5) and `L024` (collision-wall theorem W7 with
  corollary W8, scoped per R001 F2/F3). `G012` resolved with the R001
  F4 mod-4 caveat recorded.
- Review outcome (`R001`, delegated-subagent, fresh context): **pass at
  lemma level** — zero critical, zero major, three minor findings
  (numerical-semigroup import hygiene in W5; `L019` cited above ledger
  strength in W8; W8's closing sentence overstated as "all finite
  groups" where the proof gives per-base closure for
  \(\lvert\Gamma\rvert\ge\Gamma_0(B)\)) and three notes (mod-4 caveat
  for the `G007` handoff; exit-state/ledger mismatch; the branch
  distinctness \(x\ne x'\) carries no load). All six repaired in place
  the same session; repair log appended to R001. The reviewer verified
  E009 reproduces bit-identically and wrote an independent
  conclusion-level probe (different algorithm — product-digraph boolean
  powers; different bases including loop/parallel multigraphs and a
  bipartite multigraph; different groups including \(Q_8\) and
  \(Z_{21}\); PyPy 7.3.23): 108 cases, 3,136 admissible lengths, zero
  violations of W7.
- Provisional insights: the proof-side reading — min-degree-3 forces
  tailless nb closed walks at *every* length \(\equiv0\bmod4\) (every
  even length if non-bipartite) past a constant threshold, balanceable
  in any finite quotient at logarithmic cost; the hard core of `C001`
  from this angle is exactly walk-to-cycle conversion.
- Computational evidence: `E009` (scope: six bases, seven groups, listed
  assignments/lengths; 9,606,333 assertions incl. 64,425 exhaustive-arm
  constructions) plus the R001 probe above.
- No change to the status of `C001`; the main claim remains `open`.

## Failed routes and why

Two drafting dead ends, recorded in A010's failure analysis: pigeonhole
at the target length loses exactness to prefix/suffix trimming; pumping
one short identity walk (powers, or two incommensurable walks via
Frobenius) cannot reach exact powers at logarithmic thresholds. Both
motivated the branch-and-steer design.

## Adversarial check

- The E009 checker validates walks from the raw arc list and the
  definitions alone, independent of construction internals; negative
  controls confirm it rejects backtracking, non-closed, and wrong-length
  walks.
- Junction conditions were re-derived symbolically twice (once in the
  general gluing form, once for the branched pairs) before writing W7.
- The threshold arithmetic was checked in code
  (`ok(N0 >= 2*R_B + 1, ...)` never fired across the sweep).
- Cross-engine anchor: the independently validated E008 DP agrees on
  identity-walk existence at every power above the threshold in its
  range, for every simple sampled assignment.
- A delegated fresh-context logic audit (R001) was initiated rather than
  self-certifying; ledger promotion of `L023`/`L024` and `G012`
  resolution wait on its verdict.

## Canonical records changed

- [ ] `STATEMENT.md` (unchanged; statement version stays 0.1)
- [x] `STATE.md`
- [x] `CLAIMS.md` (`L023`, `L024` + dependency notes)
- [x] `OBLIGATIONS.md` (`G012` resolved; `G007` input recorded)
- [x] `PROOF.md` (dependency outline: collision-wall theorem added)
- [x] `DECISIONS.md` (lift program closed as a theorem; portfolio shift)
- [x] `LOG.md`
- [x] `problem.json` and index
- [x] Session-scoped changes committed
- [x] Commit pushed to configured upstream

## Ending checkpoint

- Current frontier: the voltage-lift program is closed **as a
  theorem** — `L024` (reviewed, `R001`) forces identity-balanced
  tailless nb closed walks at every mod-4 length past
  \(4\log_2\lvert\Gamma\rvert+C_B\) on every min-degree-3 base;
  finite-order frontier unchanged (`L022`, counterexamples \(\ge19\)
  vertices, extremal window \([19,24]\)).
- Remaining blockers: `G002`, `G003`, `G007` (global mechanism — now
  concentrated in the walk-to-cycle interface); `G004` (1997 body).
- Recalibration decision: continued the inherited route to completion,
  then pivoted the portfolio's primary to the proof side (walk-to-cycle
  interface), since falsification now has no live construction tool by
  proof rather than by fashion.
- Best live alternative or reframing: use the saturation constraints
  (`L008`–`L013`) as the extra hypothesis in the transfer lemma; a
  minimal counterexample is far from an arbitrary min-degree-3 graph.
- Pivot trigger: a published consecutive-even-cycle-lengths result at
  minimum degree 3 (import and rebase); or a demonstrated unbounded
  walk/cycle length separation in 2-connected min-degree-3 graphs
  (kills bounded transfer; switch to walk abundance/counting).
- Best next action: the three-step walk-to-cycle opening recorded in
  `problem.json` and `STATE.md` (literature sweep, transfer-lemma
  formulation, failure-first gap measurement).
- Files a new session should read: `STATE.md`, `A010`, `R001`,
  `E009/README.md`, `CLAIMS.md` rows `L023`–`L024`, `OBLIGATIONS.md`
  `G007`/`G012`, this session.

## Plain-language recap

Last session ended with a conjecture about why the project's
counterexample-building machine kept failing: a counting argument — a
group with \(N\) labels can't tell apart exponentially many walks — that
predicted failure for *every* possible symmetry system, but was only
checked on examples. This session turned that heuristic into a proved
theorem. The missing piece was exact length control: the naive
pigeonhole argument produces balanced round trips whose length you
can't choose. The fix was a construction in three moves: find one
colliding pair of same-value walks (forced by counting), split it into
two branches, and steer both branches — using a newly proved fact that
walks in such graphs can reach any position at any sufficiently large
exact length — to a meeting point where a four-way gluing produces a
balanced round trip of exactly the desired length, in any group, with
no commutativity anywhere. Every supporting fact was proved from
scratch, including a small structure theory of turn-restricted walks in
graphs where every junction has three ways out. The proof was then
checked three independent ways: a nine-million-assertion machine
verification of the construction, an adversarial audit by a fresh
reviewer who tried to break every step (verdict: sound, with three
minor bookkeeping repairs, all applied), and the reviewer's own
independently written test on graphs and groups the original tests
never touched. What this buys: the construction chapter of the project
is now closed with mathematical certainty rather than experimental
confidence, and — read in reverse — the theorem is the sharpest fact
yet pointing toward the conjecture: sparse well-connected graphs
cannot avoid balanced round trips at any suitable scale. The whole
difficulty of the conjecture is now concentrated in one clean question:
when does an unavoidable round trip force an actual simple cycle?

## Proposed next step

Start the "walk-to-cycle" question. Concretely: first check what
mathematicians already know about forced cycle lengths in graphs where
every vertex has three neighbors (there is a known result forcing two
cycles with lengths differing by one or two, and a modern literature on
cycle-length intervals — the project should import the strongest of it,
not re-derive it); then write down precisely what conversion lemma
would bridge the proved round-trip theorem to actual cycles; then try
to break that lemma on the graphs most hostile to it (very sparse
graphs with no short cycles at all, and the four known 24-vertex
near-miss graphs). Either the bridge survives its stress test and
becomes the new attack target, or its failure mode reveals what extra
structure a minimal counterexample must be exploited for. The deferred
alternative is to attack the interval-forcing lemma directly without
the walk framing.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 2%
- Previous estimate, if any: 2% (S009)
- Reason for change: none. The session proved and survived review on
  the project's most substantial internal theorem to date — but it is a
  theorem about the tool chapter, and the calibration rule forbids
  upgrading on elegance. The deep obstacles (`G002`/`G003`/`G007`)
  stand exactly as before; what improved is their *clarity*: the hard
  core is now one named interface (walk-to-cycle) with a concrete
  falsifiable next move, rather than a fog.
- Basis: most promising route — the walk-to-cycle transfer under
  saturation constraints, fed by the reviewed walk-interval theorem;
  strongest obstacle — nothing in the dossier or the swept literature
  controls full cycle spectra of 2-connected min-degree-3 graphs at
  unbounded order, and large-girth graphs show the transfer must lose
  length; evidence — the L024 proof and R001 audit, the C019
  redundancy fingerprint, and the standing separation lemmas
  `L014`–`L016`.

This is a subjective research outlook, not mathematical evidence or a claim-status
promotion.
