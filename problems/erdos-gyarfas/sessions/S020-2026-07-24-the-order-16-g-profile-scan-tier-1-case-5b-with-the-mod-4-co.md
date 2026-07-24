# S020 — the order-16 G-profile scan (Tier 1, case 5b) with the mod-4 congruence hunt alongside

- Date: 2026-07-24
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1
- Work / claim status: `active` / `open`
- Strongest established facts: `L039`–`L042` (S019) — the (3,3) bijection
  onto the congruence class \(\mathcal G\), the engine + peel, the
  five-case analysis: the conditional cubic reduction holds modulo
  excluding case (5b); every tight 1-atom has order \(\ge17\); the
  residual object is 2-connected, non-bipartite, arithmetically squeezed.
  `C027` (stream-level emptiness through 15), `C034` (bipartite class
  empty through 23), `C035` (order 16 pair-level only — the stream-level
  question at 16 is open).
- Open obligations in scope: `G015` (exclude case (5b)); `G013`(a) (the
  tight 1-atom question).
- Inherited next action: the order-16 \(\mathcal G\)-profile scan
  (decisive at one order) with the mod-4 congruence hunt alongside.
- Session goal: run the scan to completion and harvest it; develop the
  mod-4 congruence question against the `L042` residual object while it
  runs.
- Falsifiable next move: enumerate every connected \(C_4\)-free graph of
  order 16 with exactly two degree-2 vertices (all others \(\ge3\)) and
  test power-freeness; on any power-free survivor, test
  \(S\cap\{2,6,14\}=\emptyset\).

## Strategy audit

- Why the inherited route might work: the scan is decisive at one order in
  both directions — a hit satisfying the \(S\)-condition is a tight 1-atom
  (disproof of 0.1 via `L025` R4); emptiness lifts `L041`'s atom bound to
  \(\ge18\) and shrinks the case-(5b) window. Cost is modest: the profile
  class extrapolates to \(\sim10^7\) graphs at order 16 (E016 A6 growth
  \(\times\sim10\)/order), far below `C035`'s \(10^9\)-graph pair scan,
  and power-freeness is decidable per graph before any path enumeration.
- Fastest way to falsify it: none needed — the move is itself a
  falsification instrument; its own kill is geng-stream size grossly
  exceeding the extrapolation (abort threshold: stream count from a
  pre-run `geng -u` far above \(10^8\) graphs for the -d2 superset).
- Mechanistically distinct alternative or reframing: (i) the mod-4
  congruence hunt (proof-side; the records order it *alongside*, and it is
  run here as the companion leg, not instead); (ii) the chain-cancellation
  tension of `L042` (deferred — no new lever since S019); (iii) Tier 3
  legs (bipartite order 24, gcd scan) — background-only by the S018
  process rule, not selectable as primary.
- Selected route and reason: the inherited one — Tier 1, serves `G015`
  directly, decisive at one order, cheap, and the only move on the board
  that can *disprove 0.1 outright this session*. The mod-4 hunt runs in
  the scan's wall-clock shadow.
- Pivot criterion: a hit in the scan (immediate switch to the disproof
  protocol, `L025` R4: verify, reproduce, promote); stream size past the
  abort threshold (switch to a split/staged plan or the Tier 4
  generator); the mod-4 kill condition firing (record it and let case
  (5b) reduce to search alone).

## Work performed

- **`E018` built and anchored.** New scanner (`scan.py`) over the exact
  case-(5b) terminal profile, reusing the `E015` primitives verbatim
  (anchored there) plus a new bitmask `path_lengths` (anchored against
  the `E016` recursive reference on all 19,593 pairs of the connected
  graphs of orders 6–7, and against the recorded \(S\)-sets of
  \(K_{3,3}-e\) and Petersen\(-e\)). 26-check anchor suite passed under
  CPython 3.14.2 **and** PyPy 7.3.23 before any production run.
  Calibration: class counts equal `E016` A6 at orders 8–13; orders
  14–15 new (130,461; 1,826,839 — all \(C_8\)-blocked, re-deriving
  `C027`'s verdict on this profile).
- **The order-16 \(\mathcal G\)-profile scan** (the inherited primary,
  `L041`'s decisive order): 24 geng parts, 8 concurrent PyPy workers,
  2,893.5 CPU-s (~7 min wall; machine shared with a ~2–3-core browser
  session — recorded per `process/concurrency.md`). Result in
  `C036`; per-part JSON + harvest in `E018/data/`. Coverage verified
  two ways (part-sum = independent unsplit `geng -u` = 346,573,602;
  harvest identity asserted).
- **The mod-4 congruence hunt** (`A021`, the recorded proof-side
  companion, run in the scan's wall-clock shadow): the chain-calculus
  identity and its mod-2 exactness (T1), the theta-graph boundary case
  (T2), the pre-registered kill test over the vertex-taut profile
  class at orders 10–13 (`mod4.py`, T3), the labelg identification of
  the order-10 witness as Petersen\(-e\), and the modulus-independent
  reading (T4). Result in `C037`.
- Ledger reconciliation: `C036`/`C037` rows + dependency notes;
  `PROOF.md` bound updated (\(\ge17\to\ge18\)) and the `L042`
  "congruence-type tools" reading corrected; `G015`/`G013`(a) live
  moves rewritten; `STATE.md` rewritten; pivot triggers advanced.

## Results

- **Computational evidence (exhaustive, `C036`):** the order-16 profile
  class (29,713,305 graphs) has no power-free member — every member
  contains a \(C_8\); \(\mathcal G\) is empty at order 16.
  **Consequence via `L041` (proved case analysis): every tight 1-atom
  has order \(\ge18\).** No disproof: the decisive order cleared in
  the safe direction. Proximity datum: minimum \(C_8\) count 1
  (orders 14/15: 1/2) — single-\(C_8\) blocking exists.
- **Computational evidence + analysis (`C037`/`A021`):** the
  congruence-obstruction route against case (5b) is dead at every
  modulus. The forced-membership hypothesis set is *realized*
  (Petersen\(-e\) at order 10; 60 witnesses through 13; both residue
  patterns), so it admits no refutation from within; and `A021` T1
  (proved) shows the cycle space controls path arithmetic mod 2 only.
  Petersen\(-e\) recorded as the standing calibration object.
- **Provisional insight:** the discriminating layer for case (5b) is
  the \(C_8\) interference/confinement structure (the band-4 pencil is
  the model — the one `L042` constraint Petersen\(-e\) violates),
  never residue arithmetic. The surviving proof-side lever is the
  chain-cancellation tension (Minkowski-additive, untouched by the
  kill).
- No imported facts; nothing here consumes `C004`–`C006`.

## Failed routes and why

The mod-4 congruence hunt — killed by its own pre-registered test at
the first order the test could fire, on the dossier's most-studied
gadget. First decisive failure: `A021` T1's leak term
\(2|E(P)\cap E(Q)|\) (no mechanism), confirmed by T3 (the hoped-for
conclusion is false anyway). Salvage: T1 as a reusable ceiling
statement — any future congruence attempt must name a non-chain
mechanism first — plus the taut-class residue data and the
calibration object. Full postmortem in `A021`.

## Adversarial check

- Coverage of the scan challenged two ways: the 24-part split total
  reproduced exactly by an independent unsplit `geng -u` run
  (346,573,602), and the harvest asserts the filter-chain identity
  (profile = \(C_8\)-blocked + \(C_{16}\)-blocked + survivors) per
  part and globally. The edge range was challenged before launch: the
  Reiman bound guarantees no \(C_4\)-free graph on 16 vertices above
  35 edges, `maxe` was set coverage-safe at 120, geng itself tightened
  to 33, and the maximum edge count actually seen was 31.
- The filter chain was required to reproduce known data before
  production: `E016` A6 equality at six orders, `C027` emptiness
  through 15, and the fixed-anchor spectra/\(S\)-sets (including the
  `L039` closure prediction on Petersen\(-e\)); anchors passed under
  both interpreters per the standing PyPy rule.
- The kill-test verdict was challenged for over-reach: the witnesses
  drop power-freeness, so the recorded conclusion is confined to
  "no theorem from the forced hypotheses *alone*" (`C037`'s dependency
  note states this scope explicitly); the labelg identification of the
  order-10 witness was verified by canonical-form equality, not by
  eyeballing; and the survivor-analysis code path (unreachable in an
  empty scan) was exercised via the anchor suite's synthetic checks
  (Petersen\(-e\) \(S\)-set, closure spectrum, `analyse_survivor`
  assertions on the order-8 class member at calibration).
- Checked that the \(\ge18\) consequence does not silently assume (R):
  `L041`'s case analysis gives it unconditionally (cases (1)/(3)
  impossible, (2)/(4) give \(\ge39\)/\(\ge20\) via `L022`, case (5)
  needs an order-\(\ge17\) \(\mathcal G\)-reduct after `C036`).

## Canonical records changed

- [ ] `STATEMENT.md` — unchanged (no statement change)
- [x] `STATE.md`
- [x] `CLAIMS.md` (`C036`, `C037`, dependency notes)
- [x] `OBLIGATIONS.md` (`G015`, `G013`(a))
- [x] `PROOF.md` (bound \(\ge18\); the corrected case-(5b) reading)
- [ ] `DECISIONS.md` — unchanged (no statement/architecture change: the
  route retirement is inside `G015`'s recorded move list, per its own
  pre-registered kill condition)
- [x] `LOG.md`
- [x] `problem.json` and index
- [x] Session-scoped changes committed
- [x] Commit pushed to configured upstream

## Ending checkpoint

- Current frontier: every tight 1-atom has order \(\ge18\); \(\mathcal
  G\) empty through order 16; congruence obstructions dead at every
  modulus; case (5b) carries `G015` with two live levers (chain
  cancellation; the generator-powered order-17 rung).
- Remaining blockers: no proof mechanism yet that makes power-freeness
  itself fight on an unbounded congruence-channel object; the order-17
  raw stream (~6e9) is too big for the geng+filter pattern to stay the
  right tool.
- Recalibration decision: continued (Tier 1 retained; within it, the
  proof-side lever pivoted from congruence to chain cancellation —
  forced by the kill, not chosen by taste).
- Best live alternative or reframing: the disjoint long-link descent
  (`A020` W2-T8(c)), where R1 and R2 meet on the link graph.
- Pivot trigger: a chain-cancellation theorem (concentrates case (5b)
  on 2-connected \(H\)); an order-17 hit with the \(S\)-condition
  (immediate disproof); the generator build stalling (fall back to raw
  geng order 17 in split legs).
- Best next action: quantify the chain-cancellation tension (proof
  side) and build the `G014` item-6 \(\{C_4,C_8\}\)-free generator
  (search side) — as recorded in `problem.json`.
- Files a new session should read: `STATE.md` (resume list), `A021`,
  `A019`, `E018/README.md`.

## Plain-language recap

The programme's live question had narrowed to one dangerous
configuration: a graph with a single "defect" vertex of degree 2 whose
removal leaves a two-terminal graph with very particular arithmetic —
its terminal-to-terminal path lengths must include a power of two and a
number one less than a power of two, while avoiding every number two
less than a power of two. Last session left two moves against it: an
exhaustive computer search at the one graph size (16 vertices) where
the configuration could first exist, and a hunt for a
"remainders modulo 4" argument that would rule it out by pure
arithmetic, the way an even/odd argument had already ruled out its
two-colourable version.

This session played both moves to completion. The search examined all
346,573,602 candidate graphs on 16 vertices (with the total verified by
an independent second count) and found that among the 29,713,305 with
the right degree pattern, every single one contains a cycle of length
8 — so none is a counterexample seed, and the dangerous configuration
is now known to need at least 18 vertices. Two details matter beyond
the headline. First, some of those graphs are blocked by exactly *one*
length-8 cycle — this family comes within a single cycle of disproving
the conjecture, closer than any other family we have scanned — which is
why the next search order should be attempted only with a purpose-built
generator that never creates length-8 cycles in the first place.
Second, the modulo-4 hunt is not merely stalled but provably hopeless:
the Petersen graph with one edge deleted — a ten-vertex graph we know
intimately — satisfies *every* arithmetic condition the dangerous
configuration is forced to satisfy. Since a graph realizing all those
conditions exists, no argument built from remainders alone can ever
derive a contradiction from them. What separates Petersen-minus-an-edge
from an actual counterexample is one concrete length-8 cycle, so future
proof attempts must work with how actual cycles interfere — the
surviving lever is a "cancellation" tension along the chain structure
of the two-terminal graph — and every candidate argument now has a
free sanity test: it must fail on Petersen-minus-an-edge.

## Proposed next step

Two-track, as recorded in `problem.json` and `STATE.md`. Proof track:
work the chain-cancellation tension — the two-terminal graph's path
arithmetic must cancel forbidden lengths across every cut, and the
first falsifiable target is to bound how long its chain of blocks can
be (or show it has none, i.e. is 2-connected). Search track: build the
dedicated generator that grows C4-free-and-C8-free graphs directly
(the design reference is already recorded), because the length-8 test
eliminated 100% of candidates at every order we have ever scanned —
then the 17-vertex order becomes affordable and decisive the same way
16 was. Considered and deferred: running order 17 by brute force
(~6 billion graphs — possible in split legs but the wrong instrument),
and any further congruence hunting (provably dead, see above).

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 5%
- Previous estimate, if any: 5% (S019)
- Reason for change: none — decisively informative but symmetric. One
  of the two named proof levers died (cheaply, by its own
  pre-registered test) and the decisive search order returned empty;
  against that, the atom bound rose an order with coverage verified
  two ways, the class showed single-\(C_8\) blocking (the closest
  approach to a witness in the dossier), and the surviving lever plus
  a free calibration object make the remaining work sharper.
- Basis: most promising route — chain cancellation on the proof side
  and the generator-powered order-17 rung on the search side, inside a
  deliverable (`G015`) that is one configuration away from closing;
  strongest obstacle — the dossier still has no mechanism that makes
  power-freeness fight on an unbounded object, and the kill test
  proved that congruence arithmetic cannot substitute for one;
  evidence — `C036`, `C037`, `A021` T1–T4, and the min-\(C_8\)=1
  statistic.

This is a subjective research outlook, not mathematical evidence or a claim-status
promotion.
