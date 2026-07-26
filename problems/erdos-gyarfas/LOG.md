# Research log

Append brief dated checkpoints. Detailed reasoning belongs in a linked session,
attempt, experiment, or review record.

## 2026-07-23 — Dossier created

- Created `P-002`.
- Work status: `intake`; claim status: `open`.
- Next: normalize the statement and complete an intake session.

## 2026-07-23 — S001 initial normalization and structural attack

- Fixed the finite simple undirected statement and its exact negation.
- Proved `L001`–`L004`: a leaf-block reduction, edge-minimal structure, the
  lower bound of nine vertices for a counterexample, and a longest-path chord
  restriction.
- Ran `E001`, an exact census through order \(7\) for all eligible labelled
  graphs and through order \(8\) for labelled cubic graphs; no counterexample
  occurred in those finite spaces.
- No external source or claimed solution was inspected.
- Work status moved from `intake` to `active`; the next attack begins with
  \(C_4\)-free graphs at order \(9\).

## 2026-07-23 — S002 exact frontier and literature audit

- Proved `L005` and `L006`: every counterexample has at least eleven vertices.
- Ran `E002`, an exact edge-minimal \(C_4\)-free search at orders \(9\) and
  \(10\); its surviving degree patterns agree with the hand classifications.
- Inspected primary research sources through May 2026. They corroborate the
  statement and report that the general conjecture remains open.
- Imported precise minimal-counterexample, induced-\(P_{13}\), and
  high-average-degree results as `C004`–`C008`.
- Recorded that the internal finite bound is below reported prior computation;
  no novelty is claimed.
- Shifted the next attack from order-by-order enumeration to attachment
  patterns on the induced \(P_{13}\) forced in every counterexample.

## 2026-07-23 — S003 induced-path route falsified

- Imported `C009`, Biggs's construction of finite Hamiltonian cubic graphs
  with arbitrarily large girth.
- Proved `L007`: cubic domination, cubic density, proper-subgraph minimality,
  an induced \(P_{13}\), and absence of \(C_4,C_8\) do not force \(C_{16}\).
- Ran `E003`, an exhaustive check of the smallest 18-vertex independent-hub
  cubic completion; every branch already creates \(C_4\) or \(C_8\).
- Resolved `G006` by refuting the proposed local route and opened `G007` for a
  genuinely global replacement mechanism.
- No proof or disproof candidate for the main conjecture exists.

## 2026-07-23 — S004 global saturation route opened

- Proved `L008`: any counterexample has an edge-maximal power-cycle-free
  supergraph in which every nonedge has a \(2^k-1\)-edge witness path.
- Proved `L009`: the new condition excludes a connected bipartite cubic
  large-girth realization of the structural bundle that defeated the prior
  local route.
- Proved `L010` and `L011`: edges outside all odd cycles form a matching, and
  the Mersenne-path certificates persist inside a non-bipartite 2-connected
  leaf block away from its possible cut vertex.
- Proved `L012`: a shortest odd cycle of length at least \(7\) forces an
  external ear; triangles and \(5\)-cycles remain separate cases.
- Proved `L013` and `L014`: 2-connectivity supplies an ear in the short cases,
  but one-ear theta length equations admit an infinite power-free family and
  are not decisive.
- Opened `G008` for the unresolved witness-overlap and theta-length step. No
  proof or disproof candidate for the main conjecture exists.

## 2026-07-23 — S005 single-witness forcing retired; pivot to the saturated finite frontier

- Proved `L015`: a full one-excursion `L012` witness — total Mersenne length,
  both arcs, both gaps, induced shortest odd cycle — admits infinitely many
  power-free theta realizations in every attachment configuration.
- Proved `L016`: a full two-excursion pattern admits infinite power-free
  double-theta realizations on \(C_7\); the recorded pivot trigger fired.
- Resolved `G008` on its obstruction horn; recorded the sparsity heuristic:
  bounded witness diagrams cannot force, so a decisive mechanism must couple
  unboundedly many witnesses or generate an interval of even cycle lengths.
- Observed that at orders \(\le15\) saturation collapses to "every nonedge
  has a path of length \(3\) or \(7\)"; with `L006` and `L008` this makes the
  nonexistence of an order-\(11\) saturated counterexample finitely checkable
  and sufficient to lift the counterexample lower bound to twelve vertices.
- Opened `G009` and made that exhaustive order-\(11\) search the next action;
  the variable-length reframing stays the live alternative. No proof or
  disproof candidate for the main conjecture exists.

## 2026-07-23 — S006 orders 11 through 13 excluded by exhaustive search

- Built and validated `E004`, an exhaustive generator for
  \(\{C_4,C_8\}\)-free graphs of minimum degree \(3\), anchored to the
  independent `E001`/`E002` counts, an exact symmetry quotient, and a
  nonzero \(C_8\)-free positive control at order \(8\).
- The search found no such graph of order \(11\) (231,646 nodes, 12 degree
  sequences), order \(12\) (6,535,800 nodes, 29 sequences), or order
  \(13\) (44,397,061 nodes, 59 sequences); all sequence counts were
  re-derived by hand.
- Proved `L017`, computer-assisted: every counterexample has at least
  fourteen vertices. At these orders the searched class equals the
  counterexample class outright, so `L008` was not needed; `G009` resolved
  in this stronger form, and the saturation-as-accelerator premise was
  recorded as wrong in its generative form.
- Recorded the computation as `C011`; opened `G010` to push orders
  \(14\)–\(15\), the remaining range of the small-order collapse, with
  parallel decomposition and re-validated anchors. No proof or disproof
  candidate for the main conjecture exists.

## 2026-07-23 — S007 frontier sweep, true bounds, saturation novelty, and order 18

- Read the primary sources in full: Markström (2004) and Royle's 2002 page
  (Wayback snapshot). Both verify only orders \(\le15\); the circulating
  "at least 17 vertices" is an overread with no primary support. Imported
  the true bounds `C012` (general \(\ge16\)) and `C013` (cubic \(\ge30\)),
  plus Markström's Table 3 as `C014`.
- Verified the Markström graph from House of Graphs (id 51419) exactly:
  cubic, planar, spectrum \(\{3,5,6,7\}\cup\{9..24\}\), and — new
  observation `C015` — every one of its 240 nonedges carries a Mersenne
  witness path, so any added edge creates a power-of-two cycle.
- Reproduced the cubic census (`E005`, `C018`): cubic
  \(\{C_4,C_8\}\)-free classes empty at orders 14–22; exactly four graphs
  at order 24 among 9,467,449 \(C_4\)-free cubic graphs, exactly one
  planar and labelg-isomorphic to HoG 51419, all four fully
  witness-covered. A planarg wrapper bug was caught by the disagreement
  with Markström's "only one planar" and fixed before any record used it.
- Ran the recorded `G011` novelty sweep: the edge-maximal power-cycle
  saturation reduction appears nowhere in the swept literature; resolved
  `G011` with a repeat-before-publishing caveat — the saturation line is
  the project's frontier-passing asset.
- Built the anchored general pipeline `E006` (geng, anchors A1–A5) and
  exhausted orders 14–17: the connected \(C_4\)-free minimum-degree-3
  classes (6059; 91433; 1655659; 34758006 graphs) contain no
  \(C_8\)-free member. With hand-proved connectivity and collapse lemmas
  this gives `L018` in `A007`: every counterexample has at least
  eighteen vertices, past the strongest inspectable published general
  bound; the smallest \(\{C_4,C_8\}\)-free minimum-degree-3 graph has
  18–24 vertices.
- Read Bensmail (2017) in full; imported `C017` and named the
  falsification-side spectrum-gap program (confinement needs cut
  vertices; the 2-connected question is the real one). Capped the census
  layer; PyPy verified available for future Python-bound legs. No proof
  or disproof candidate for the main conjecture exists.

## 2026-07-23 — S008 next action amended to internal tool-building

- Applied the user's no-ceiling directive (contract-encoded as `O009`) to
  the recorded route: the next action now opens the voltage-graph lift
  construction attempt on the falsification side — targeting a
  2-connected minimum-degree-3 family whose cycle lengths avoid all
  powers of two — with kill conditions named in advance, spectra of the
  four verified order-24 graphs as calibration, the controlled-start
  interval lemma as the proof-side alternative, and the order-18 census
  under PyPy as capped support.
- Records amendment only: no claims, obligations, proofs, or statuses
  changed; the resolution estimate is deliberately unchanged (posture is
  not evidence). No proof or disproof candidate for the main conjecture
  exists.

## 2026-07-23/24 — S009 voltage-lift program built, run, and closed for all groups; bound raised to 19

- Opened the tool-building attempt `A008` under the `O009` rule: voltage
  lifts as the falsification-side construction machine. Proved `L019`
  (projection/certificate lemma), `L020` (tree gauge; assignments in
  \((\mathbb{Z}_m)^\mu\); net voltage as cycle-space pairing), and —
  after the first sieve run exposed integer zero vectors — `L021` (the
  abelian commutator obstruction), with hand proofs in `A008` and
  DP-extracted witnesses in `E007`.
- Built and anchored `E007` (walk-class DP, hyperplane sieve, lift
  builder, truth census, calibration; anchors A1–A8 under CPython and
  PyPy). Calibration `C019`: the four order-24 extremal graphs carry
  315/330/207/228 sixteen-cycles, every edge on at least 70, none on
  all — local surgery at the extremal boundary is hopeless.
- Cyclic verdict `C020`: for the complete cycle-rank-2 base list
  (bouquet, theta, dumbbell) plus \(K_4\), \(K_{3,3}\), prism, and
  every \(m\ge2\), no cyclic assignment is walk-certifiable power-free.
  Truth census `C021`: at lift orders 12–30, all assignments, every
  simple lift contains \(C_4\), \(C_8\), or \(C_{16}\). `A008` closed
  by its pre-named kill condition (a).
- Continued in-session at the user's direction (`A009`, `E008`):
  re-audited the successor route — Feit–Thompson makes odd-order groups
  solvable and the solvable cascade kills them predictably, so the
  perfect group \(A_5\) became the decisive test. Built the
  per-assignment group-table engine, anchored bidirectionally against
  `E007` (hit-for-hit agreement on cyclic groups). Verdict `C022`:
  orders 21, 27, 27, and \(A_5\) — every assignment on every tested
  base certificate-dead by length 16, zero survivors; solvable
  predictions confirmed as pre-registered; \(A_5\)'s death matches the
  collision-wall prediction \(2\log_2\lvert\Gamma\rvert\). The
  obstruction is group size, not structure; the certificate program is
  retired for all finite groups; `G012` refined to the collision-wall
  lemma (`A009` closed by kill trigger 5).
- Capped support completed: the `E006` order-18 census extension
  (anchors re-passed under PyPy; 48 geng parts, 8 workers, ~2h50m)
  found the connected \(C_4\)-free minimum-degree-3 class at order 18
  has 834,711,846 members, all containing \(C_8\) (`C023`); with the
  `A007` lemmas this proves `L022`: every counterexample has at least
  nineteen vertices, and the extremal \(\{C_4,C_8\}\)-free window
  narrows to \([19,24]\).
- No proof or disproof candidate for the main conjecture exists; the
  estimate stays at 2%. Next: attempt the collision-wall lemma.

## 2026-07-24 — S010

- Proved the collision-wall lemma (`A010`): for every finite group, every
  connected minimum-degree-3 multigraph base, and every voltage
  assignment, identity-voltage tailless non-backtracking closed walks
  exist at every length \(\equiv0\bmod4\) (every even length if
  non-bipartite) past \(4\ell^*+4R_B+8\), hence at every power of two
  \(\ge4\log_2\lvert\Gamma\rvert+C_B\). New machinery, all internal:
  the reverse-free/continuation-closed counting lemma, strong
  connectivity of the nb arc digraph via the reversal anti-automorphism
  on sink components, period \(\le2\) via the longest-path theta,
  exact-length reachability with an inline numerical-semigroup proof,
  and the branch-and-steer four-junction gluing that solved the exact
  length problem the naive pigeonhole could not.
- Built `E009` (`wall.py`): definition-level verification of the whole
  construction — 9,606,333 assertions across six bases, seven groups,
  adversarial and exhaustive assignment sweeps, negative controls, and
  a cross-engine anchor against the E008 DP. All passed (CPython
  3.14.2).
- Delegated a fresh-context logic audit (`R001`, delegated-subagent):
  verdict pass at lemma level, zero critical/major findings, three
  minor (semigroup import hygiene, `L019` citation strength, W8 scope)
  and three notes — all repaired in place the same session. The
  reviewer's independent probe verified the theorem's conclusion on
  108 further cases (different bases and groups, PyPy) with zero
  failures.
- Promoted `L023` (arc-digraph structure package) and `L024`
  (collision-wall theorem, scoped per R001) to `CLAIMS.md`; resolved
  `G012` with the mod-4 and per-base-closure caveats recorded;
  updated `G007` with the walk-interval input; `PROOF.md` outline and
  `DECISIONS.md` updated (lift program closed as a theorem).
- No change to `C001`; the main claim stays `open`. Next: attack the
  walk-to-cycle interface on the proof side.

## 2026-07-24 — S011

- Opened the walk-to-cycle interface per the S010 handoff: literature
  sweep, transfer formulation, failure-first calibration (`S011`, `A011`,
  `E010`, `references/source-audit-2026-07-24-S011.md`).
- Sweep: read Bondy–Vince 1998 in the published PDF (`C024`: two cycles
  differing by 1 or 2 at up to two sub-cubic vertices; difference exactly 1
  at 3-connected non-bipartite; their Figure-1 **ring** of K_{3,3}-e
  copies with spectrum {4,6,9,11,13,15}); imported Gao–Huo–Liu–Ma
  (`C025`) and Carr's diameter-2 result (`C026`) at abstract strength;
  confirmed the min-degree-3 frontier is Bondy–Vince strength and that
  sparse-interval technology needs large average degree.
- The recorded kill test fired at formulation time: the Bondy–Vince ring
  carries the `L024` walk intervals with unbounded-ratio spectrum gaps, so
  no unconditional walk-to-cycle transfer exists. Proved the atom
  reduction `L025` (A011 R1–R5): a power-free single-sub-cubic-vertex
  graph (1-atom) or a power-free two-terminal gadget with through-lengths
  pinched below ratio 2 (2-atom) yields counterexamples by
  doubling/triangle or ring-in-dyadic-gap assembly; contrapositively 0.1
  forces **spread-doubling**. Opened `G013`; rescoped `G007`.
- Built and ran `E010` (anchors incl. exact reproduction of the published
  Bondy–Vince ring spectrum): the atom class — connected {C4,C8}-free,
  min degree ≥ 1, at most two sub-cubic vertices — is **empty through
  order 15** (streams to 61,813,970; classes to 3,470,555; `C027`).
  Profile arm: through-ratio < 2 (even a single through-length) is common
  without power-freeness (22 at order 12, 116 at 13) and every occurrence
  contains a C8 — the pinch is geometric, the block is power-freeness.
- No change to `C001`; the main claim stays `open`. Next: attack the
  spread-doubling lemma analytically (2-connected case, ear machinery)
  with the order-16 atom search as the optional computational extension.

## 2026-07-24 — S012

- Audited the inherited bottom-rung plan before executing it; the premise
  test fired at formulation time and became a theorem (`A012` T1 =
  `L026`): pinched gadgets at s_min ∈ {1,2} can hide two disjoint copies
  of any counterexample behind cut vertices (bridge- and lobe-packing),
  so each unrestricted rung — and spread-doubling in full — is
  *equivalent* to statement 0.1, not a lemma short of it.
- Proved the lobe decomposition (`L027`): every (D)-gadget is vertex-taut
  or hangs a lobe at one cut vertex; power-free lobes are 1-atoms or
  min-degree-3 power-free graphs. Proved the taut bottom rungs (`L028`):
  no taut gadget has S = {1}, and no taut C4-free gadget has s_min = 2
  with S ⊆ {2,3} — C4-freeness alone suffices; hence every 2-atom with
  s_min ≤ 2 routes through the 1-atom question and has order ≥ 17.
- Proved the cubic reduction modulo 1-atoms (`L029`): if no 1-atom
  exists, every minimal counterexample is cubic; statement 0.1 ⟺ no
  cubic counterexample and no 1-atom. The 1-atom question is now the
  central open object of the disproof interface.
- Built and ran `E011` (independent implementation of the whole
  detection stack; 17 anchors incl. K_{3,3}-e tautness and both `L026`
  scaffolds): at orders 12–13 all 133 rung-class gadgets are non-taut
  and all 265 lobe components have single attachments — `L027`/`L028`
  hold on every instance; stream/profile counts reproduce `E010` exactly
  (`C028`). Survey: every taut pinched gadget at these orders sits at
  s_min = 6 with interval through-set {6,…,11} and carries a C8; taut
  pinched s_min ∈ {3,4,5} is empty through order 13.
- No change to `C001`; the main claim stays `open`. Next: the taut
  s_min = 3 rung — prove no taut C4-free power-free gadget with
  S ⊆ {3,4,5} exists, or exhibit one (disproof via `L025`).

## 2026-07-24 — S013

- Executed the inherited next action (the taut s_min = 3 rung) via a
  failure-first construction attempt; the attempt collapsed into forced
  structure at every step and became a theorem (`A013` T8 = `L030`): **no
  vertex-taut C4-free (D)-gadget has S ⊆ {3,4,5}** — C4-freeness alone
  suffices, power-freeness is never invoked. Proof shape: tautness pins
  every middle vertex to distance one from N(a) or N(b); forbidden
  length-6/7 paths kill the one-sided middle classes, force the rest into
  matched degree-3 triples, then empty the middle; the survivor is three
  perfect matchings on N(a) ∪ N(b), where every vertex triggers a
  dichotomy — C4 block or length-7 path.
- Corollaries: every taut 2-atom has s_min ≥ 4 and s_max ≥ 6; every
  2-atom with s_min ≤ 3 is non-taut, contains a 1-atom or min-degree-3
  power-free graph, and has order ≥ 19. S012's boundary prediction is
  corrected: the power-spectrum fight starts not at s_min = 3 but in
  s_min ∈ {4,5,6}, the upper end pinned by `C028`'s five witnesses.
- Built and ran `E012` (all-terminal-pair falsification search; 736
  anchor checks incl. the T8 endgame dichotomy verified exhaustively on
  all 218 three-matchings structures at k ∈ {2,4} and K_{3,3}-e as
  positive control): at orders 6–14, over every admissible terminal pair
  of every stream graph — including degree-≥3-terminal pairs, never
  examined before (241,135 eligible graphs and 1,357,597 pairs at order
  14 alone) — **zero taut hits, and zero even non-taut pairs with
  S ⊆ {3,4,5}** (`C029`). Stream totals reproduce `C027` at every order.
- No change to `C001`; the main claim stays `open`. Next: the taut
  s_min = 4 rung — extend the middle-layer collapse to depth-2 middles
  (S ⊆ {4,...,7}), or find a C4-free taut pinched s_min ∈ {4,5} gadget
  at orders 14–16.

## 2026-07-24 — S014

- Strategy audit weighed the inherited taut s_min = 4 rung against the
  user-suggested dissection of the five band-6 witnesses. Two resume-time
  findings decided it: `C029` covers S ⊆ {3,4,5} only, so the inherited
  rung's search half ("empty through 14") was an overstatement needing
  repair; and all five witnesses have identical through-sets AND cycle
  spectra — one family, not five accidents.
- Built `E013`: the first all-band taut-pinched catalogue over every
  admissible terminal pair, orders 6–14, in strict (ratio < 2) and closed
  (ratio ≤ 2) modes; 88 anchors incl. nauty labelg cross-validation of the
  new isomorphism engine and the bridge-composite check.
- Strict catalogue: exactly six taut pinched pairs at orders ≤ 14 (none at
  14): the five `C028` witnesses plus a NEW band-5 witness at order 11 —
  the pendant lift of Petersen minus an edge (S = {5,6,8,9}, spectrum
  {5,6,8,9}). The strict s_min = 4 rung target is genuinely empty through
  order 14 (`C030`).
- Dissection: every witness has exactly one cut vertex and terminal
  degrees (1,2) — a pendant edge on a 2-connected core at through-ratio
  exactly 2. Proved the pendant reduction/lift bijection (`L031`) and the
  chain/block extraction theorem (`L032`): taut 2-atoms exist iff a
  power-free vertex-taut 2-connected core with s_max ≤ 2 s_min exists.
  Naive core-level spread-doubling is FALSE: two Petersen−e blocks joined
  by a bridge give a strict taut core of order 20 (machine-verified);
  blocks are the right level.
- Closed catalogue (`C031`): five 2-connected blocks through order 14 —
  Petersen−e (band 4), A11/B11 (band 5), C12 (band 5), D14 (band 6, order
  14, found this session) — ALL at exact equality s_max = 2 s_min, none
  strict; the six strict witnesses are exactly their distinct pendant
  lifts (bijection machine-verified). Every C8 in every block and witness
  is the symmetric difference of two through-paths (23/23); at band 4 two
  internally disjoint 4-paths force C8 directly (realized in Petersen−e).
- `G013` refined: (a) 1-atoms; (b') the block question. No change to
  `C001`; the main claim stays `open`. Next: the band-4 block rungs —
  strict impossibility (S ⊆ {4,...,7}) and equality C8-forcing
  (S ⊆ {4,...,8} ⇒ C8) — with the order-15 closed catalogue as search leg.

## 2026-07-24 — S015

- Strategy audit accepted the inherited band-4 block rungs; within them
  the mechanism half (the disjoint/intersecting dichotomy) was attacked
  first, and the order-15 catalogue extension ran as the search leg.
- `L033` proved (A015): the band-4 pencil dichotomy. In ANY graph with
  d(x,y)=4: the (2,2)-vertices are exactly the 4-path middles (product
  structure per middle); either two internally disjoint 4-paths exist —
  equivalently a C8 through both terminals — or ALL 4-paths share one
  internal vertex. No C4-freeness needed for the dichotomy (the planned
  "triangle" anchor was machine-refuted and the hypothesis fell away).
  C4-free refinements: pairwise single overlap; the pencil vertex is
  unique and terminal-adjacent (middle pencils force a unique 4-path);
  fan rigidity (strands biject with middles, no cross chords, hexagons);
  far-neighbor separation of both terminal neighborhoods.
- Consequence: the band-4 case of the block question is exactly the
  **pencil endgame** — prove no vertex-taut 2-connected C4-free core
  with d(x,y)=4, s_max ≤ 8 has a pencilled 4-path system; success closes
  band 4 in the strengthened form "C8 through both terminals" (no C16
  caveat). Three hand construction attempts against the endgame died to
  a C8, a 9-path, and C4s respectively (cascade obstruction recorded in
  A015); the (3,3)–(4,4) deep territory remains the untested escape.
- `E013` extended to order 15 under PyPy (61,813,970 stream graphs,
  22,022,137 pairs per mode, ~5 min per mode): strict = exactly one hit,
  machine-identified as D14's pendant lift (C031's swap-symmetry
  prediction confirmed); closed = 20 hits, all pendant-type — the block
  catalogue is unchanged through 15 (no strict block; five equality
  blocks); no closed hit at any band ≤ 3 exists through 15; the closed
  band-4 world is three objects, only Petersen−e a core (`C032`).
  Order-16 closed scan launched (first order where a hit could be
  C8-free).
- `E014` built: exhaustive verification of `L033` (116,187 C4-free
  distance-4 pairs, orders 5–11; 43,419 general pairs, orders 5–9; zero
  failures; sharpness anchors) and the C4-allowed block probe: strict
  blocks exist with C4s from order 6 (K33−e), strict band-4 blocks with
  S={4,5,6,7} at order 8, and band-4 equality cores with S={4,...,8}
  and NO C8 at order 9 — C4-freeness is essential to both band-4 rungs
  (`C033`).
- `G013` (b') refined to the pencil endgame at band 4; the band-2
  closed rung (S ⊆ {2,3,4} with 4 ∈ S) recorded as the remaining
  C4-only gap below band 4. No change to `C001`; the main claim stays
  `open`.
- **S015 addendum (external memo integration).** Mid-session the user
  supplied a strategy memo from another AI agent; it was audited claim
  by claim in `A016` (memo preserved verbatim in `references/`). Core
  finding verified and recorded as `L034`: A011 R1's ring spectrum
  formula supports the full sumset criterion — a power-free (D)-gadget
  disproves 0.1 whenever some L-fold sumset of S avoids the powers of
  two — so the pinch (2-atom) condition is one channel among several
  (all-odd S with odd L; odd-prime gcd; S ⊆ 2+4Z). Fatal shapes the
  pinched frame cannot see: S = {3,7}, S = {2,6}. Corrected necessary
  conditions recorded; the "sharp/entire-channel" glosses retracted
  (framing error, no proved row false); the program ceiling made
  explicit (assembly closure + 1-atoms = cubic reduction, not 0.1).
  Mitigations verified against the memo: C027 is profile-agnostic, so
  every channel is empty through order 15; all-odd ladders live at odd
  bands only, disjoint from the band-4 pencil work; L031/L032 are
  pinch-specific (pendant shift flips parity) so the parity channel
  needs its own reduction theory. G014 opened for the memo's
  literature/census leads (Chen–Saito, bipartite >=32, bipartite EGC
  to 31, Heckman–Krakovski, Shauger, Daniel–Shauger, vertex-transitive
  and girth-9 censuses, Markström's generator method) — all unverified
  until source-audited. The six memo paths entered the portfolio
  alongside every pre-existing thread (user's standing instruction:
  carry all threads; no execution this session per user instruction).

## 2026-07-24 — S016: the parity channel is the bipartite channel

- **Strategy audit.** The inherited next action proposed an odd-\(S\) taut
  scan mode over the existing order-\(\le15\) stream plus the `G014` source
  audits. Audit outcome: the scan's *class* was already proved empty
  (`C027` is profile-agnostic), so its only value was shape data — and a
  cheaper, stronger instrument existed. Selected route: prove the parity
  structure theorem first, then search the class it identifies. The pencil
  endgame (Thread A) and every other thread stayed live per the standing
  user instruction.
- **`L035` proved (`A017` T0–T5).** For a vertex-taut two-terminal graph,
  "all through-path lengths have the same parity" is **equivalent** to
  bipartiteness. Proof: cut vertices of a taut gadget separate the
  terminals, so the blocks form a chain with Minkowski-sum through-sets
  (T0, `A014` T3 with the degree hypotheses deleted); inside a 2-connected
  block, an odd cycle plus a 2-fan from an added apex yields two arcs of
  opposite parity, hence through-paths of both parities (T1). Corollaries:
  **any** connected bipartite power-free graph with at most two sub-cubic
  vertices disproves 0.1 (T3 — via 1-atom doubling, outright, or a 3-ring
  of the graph or of its pendant lift/reduction), and bipartite generation
  is exhaustive for `L034` channels (i) and (iii) modulo 1-atoms (T4).
  Scope: channel (ii) (odd-prime gcd) is **not** bipartite-forced —
  \(\Theta(3,3,3)\) is the recorded counterexample.
- **`E015` built and run (`C034`).** genbg with `-Z1 -d2` over the splits
  admitted by T5 generates the class exactly. No power-free member exists
  at any order \(\le21\) (hence none of order \(\le22\) with a pendant):
  class sizes 0,0,2,1,6,8,75,197,2715,10865 at orders 12–21, **every**
  member containing a \(C_8\), minimum \(C_8\) count never below 13, so the
  \(C_{16}\) test is never decisive. Sub-results in the same run: no
  bipartite 1-atom and no bipartite counterexample at those orders — the
  latter verifying internally the range that `G014` item (2) was to
  supply. An order-22 run was launched and left unfinished (machine
  contention); it is deliberately excluded from `C034`.
- **Verification before recording.** `verify_parity.py` ran the theorem's
  own kill condition over every connected graph of order \(\le7\) (39,690
  ordered pairs) and every connected \(C_4\)-free graph of orders 8–9
  (63,696 pairs), with through-sets by explicit path enumeration: T2 held
  in all 952 hypothesis instances, T1 in 27,196, T0's chain/Minkowski in
  33,962, and all 10,788 parity-constant non-bipartite pairs were non-taut
  (tautness is the whole hypothesis). Generator cross-check: the genbg
  class equals the `E010`-stream-derived class at order 14 by `labelg` set
  equality; the unique cubic member at order 14 is the Heawood graph.
- **Corrections recorded.** `A016` M3 ("the bipartite reformulation is an
  instance, not an equivalence") and M4 ("the parity channel has no
  reduction theory") were both too weak: on the taut side the equivalence
  holds, and pendant shift toggles the two bipartite sub-cases rather than
  destroying the structure. Both corrections strengthen the audited
  external memo. `G014` item (2) de-gated for this thread. No proved row
  changed; `C001` stays `open`.

## 2026-07-24 — S017 (order-16 harvest; concurrent with S016)

- The E013 order-16 closed scan launched in S015 completed (PyPy,
  5,986s): stream 1,006,553,591 (new datum), 55,213,924 eligible,
  420,006,891 pairs, twelve taut closed hits (bands 4:3, 6:3, 7:6),
  all at boundary s_max = 2d, all containing a C8.
- Consequences: no strict taut pinched pair at order 16 (the strict
  catalogue stands complete at seven witnesses through 16); no
  power-free closed taut pair at 16; three new equality blocks on
  three new graphs — F16 (band 4, terminal degrees (3,3), two
  gadget-isomorphic realizations, on a graph with no sub-cubic
  vertex), G16 (band 4, (2,4)), H16 (band 6, (2,2), first block with
  C16 in spectrum) — extending the block catalogue to eight, every
  one at exact equality; no strict block through 16.
- Pencil endgame (L033): all three band-4 core gadgets are
  disjoint-type — the endgame's exhaustive empty base extends to
  order 16. Interference census stays perfect: every C8 of every new
  core pair is a two-through-path symmetric difference (6/6, 6/6,
  6/6, 10/10).
- Shared-tree protocol: the concurrent S016 session held CLAIMS,
  OBLIGATIONS, PROOF, STATE, DECISIONS, PROJECT_STATE (and this LOG)
  mid-edit, so S017 committed only harvest-scoped paths (E013 README
  addendum + data + its session record) and recorded a punch list in
  sessions/S017 for the deferred ledger row and frontier-phrase
  updates ("through order 15" → "16"). This LOG entry itself was
  appended unstaged to ride with the S016 close commit.

## 2026-07-24 — S018: the 1-atom question is conjecture-complete; roadmap retiered

- **Audit trigger.** The user asked why sixteen sessions of strategy
  audits kept deferring the 1-atom question while every record described
  it as the only sub-question with direct proof-side yield.
- **`L036` proved (`A018` T1).** A 1-atom under D-A4 exists **iff** a
  counterexample exists: attach one pendant vertex to a connected
  counterexample — a pendant lies on no cycle, so the spectrum is
  unchanged and the pendant is the unique sub-cubic vertex. The
  unrestricted 1-atom question is therefore conjecture-complete, the
  one-terminal analogue of `L026`'s rung completeness.
- **`L029` repaired (`A018` T2).** As recorded ("if no 1-atom exists,
  every minimal counterexample is cubic") the implication is true but
  vacuous. `A012` T4's proof only ever produces an exceptional vertex of
  degree **2**, so the reduction is restated with *tight* 1-atoms, where
  it is not vacuous: 0.1 holds iff no cubic counterexample and no tight
  1-atom exist. `A012` Remark T4.1 ("minimum-order 1-atoms are tight") is
  **withdrawn as unproved** — its argument fails exactly when the
  pendant-reduct is a cubic counterexample. `A016` M6's ceiling statement
  was circular and is corrected.
- **`G015` opened.** The cubic reduction, unconditionally, as the
  programme's named proof-side deliverable. Route R1: no tight 1-atom.
  Route R2: strengthen the imported \(4/7\) cubic-density bound `C006` to
  1, bypassing the atom formalism. Neither passes through a
  conjecture-complete object.
- **Roadmap retiered in `STATE.md`.** Tier 0 the conjecture itself
  (forcing mechanism, or a cubic counterexample at order 30); Tier 1
  `G015`; Tier 2 restricted-class theorems (bipartite EGC; the
  path-spectrum gcd theorem); Tier 3 cheap legs that run but are never
  selected as primary (order-22 bipartite, the gcd scan, order-17+
  pinched, census mining); Tier 4 leverage infrastructure (the dedicated
  generator, which unlocks both cubic 30 and bipartite 31). All threads
  stay live per the standing instruction; the pencil endgame is demoted,
  not dropped. New process rule: each strategy audit names the tier its
  route serves.
- No proved row was falsified; one was restated and one remark withdrawn.
  `C001` stays `open`.

## 2026-07-24 — S019: orchestrated parallel run on G015 — R1 reduced to one configuration, R2's constant route closed with a sharpness tombstone

- First orchestrated parallel session (`O011` protocol, adopted mid-setup
  at the user's direction): one orchestrating session holding every
  ledger, two Opus worker subagents — W1 on route R1 (tight 1-atom local
  structure, `A019`/`E016`), W2 on route R2 (Carr verification and
  4/7 → 1, `A020`/`E017`/references note). Both write-sets stayed inside
  their owned records; both outputs passed the orchestrator's
  line-by-line audit, with `E016`/`E017` reproduced independently
  (35/35 and all-checks-pass under CPython 3.14.2 and PyPy 7.3.23).
- **`C004`–`C006` verified.** All four results of Carr (arXiv:2605.22844v1)
  checked statement-by-statement and proof-by-proof; correspondence with
  the recorded rows exact; all three internally reconstructible
  (`references/carr-2026-verification-2026-07-24.md`). The R2
  verification prerequisite recorded in `G015` is discharged.
- **`L037`/`L038` proved (W2, audited).** The subdivision descent: the
  link graph on the degree-≥4 set of a minimal counterexample is
  power-free (cycles lift doubled) and 2-degenerate (order-minimality),
  giving the apex/equality structure package and the density theorem
  \(3|V_3|\ge2n+3\) — strictly past the published 4/7. Ceiling located
  exactly: S15 (15 vertices, density exactly 2/3, all non-power
  hypotheses satisfied, machine-certified) shows the counting cannot
  beat 2/3, and no constant <1 delivers `G015` — the constant route is
  retired with a tombstone.
- **`L039`–`L041` proved (W1, audited).** The closure calculus and the
  (3,3) bijection onto the congruence class \(\mathcal G\) (ring
  criterion at L=1, offset 2, no s_max window); the engine and the peel
  (any counterexample below the minimum atom order yields a cubic one —
  the repair of the withdrawn `A012` T4.1); the five-case analysis:
  **the conditional cubic reduction holds modulo excluding case (5b)**,
  and every tight 1-atom has order ≥ 17.
- **`L042` proved (W1, audited).** The case-(5b) residual object is
  2-connected, degree-≥4-independent, **non-bipartite** (hand proof at
  every order of `C034`'s computational verdict), carries forced power
  and Mersenne memberships, obeys chain cancellation, and inherits the
  band-4 pencil dichotomy verbatim. The taut ladder's collapse machinery
  does not transfer (no through-set window) — R1 is a congruence
  channel, and the Mersenne-saturation lever was demoted by its own
  pre-registered kill test (`E016` A6).
- Routes meet: a one-defect subgraph of the link graph is exactly a
  tight 1-atom (`A020` W2-T8(d)).
- Background Tier 3 leg: the `E015` order-23 bipartite scan was launched
  under PyPy and is still running at close; its results are excluded
  from every ledger row and the harvest is a named follow-up.
- Next action: the order-16 \(\mathcal G\)-profile scan (decisive at one
  order — a hit disproves 0.1, empty lifts the atom bound to 18), then
  the mod-4 congruence hunt against the residual object.
- No proved row was falsified. `C001` stays `open`.

## 2026-07-24 — S019 follow-up harvest: the order-23 bipartite leg lands empty

- The background `E015` order-23 leg (launched in S019 under PyPy 7.3.23,
  anchors re-passed first) completed after the S019 close with exit 0:
  **empty** — 928,562 in class from 260,796,118 generated in 5,239.8s;
  splits (10,13): 6,012 and (11,12): 922,550, eight smaller splits proved
  empty by the T5 bound; zero C8-free, zero power-free; every member
  carries **both** a C8 and a C16 (the C16 test is never decisive);
  minimum C8 count 19; profiles 814,453 gadgets / 107,787 tight-1-atom
  candidates / 6,322 min-degree-≥3 graphs, all blocked.
- Applied per the punch-list precedent (S017): `C034` extended to order
  23 (24 with a pendant), `E015` README updated, the frontier phrases in
  `STATE.md`, `OBLIGATIONS.md` (`G013`, `G014` item-2 range),
  `PROOF.md` (`L035` finite status — also repairing that bullet's stale
  pre-S018 numbers), and `PROJECT_STATE.md` brought current; the
  order-24 leg (or the Tier 4 generator) named as the next Tier 3 move;
  pivot trigger moved to order 24+.
- No power-free member, so no ledger claim changes beyond `C034`'s
  range; `C001` stays `open`.

## 2026-07-24 — S020: the decisive order is empty; the congruence route is dead

- `E018` built, anchored (26 checks under CPython 3.14.2 and PyPy
  7.3.23; class counts equal to `E016` A6 at orders 8–13; orders 14–15
  new: 130,461 and 1,826,839 members, all C8-blocked), and run at order
  16: stream 346,573,602 (24-part split; sum reproduced exactly by an
  independent unsplit `geng -u`), profile class 29,713,305, **every
  member contains a C8** (C16 never decisive), **zero power-free** —
  the class \(\mathcal G\) of `L039` has no order-16 member (`C036`).
  With `L041`: **every tight 1-atom has order \(\ge18\)**. Minimum C8
  count over the class: **1** (orders 14/15: 1/2) — the closest any
  scanned class has come to a witness; recorded as the case for the
  `G014` item-6 generator before order 17.
- The mod-4 congruence hunt (`A021`, instrument `E018/mod4.py`) died on
  its pre-registered kill condition (`C037`): the residual object's
  forced membership triple is realized by vertex-taut C4-free profile
  cores from order 10 — one order-10 witness is **Petersen minus an
  edge** (labelg-verified) — with both admissible mod-4 residue
  patterns and no invariant; and the chain-calculus identity
  \(\ell(P)+\ell(Q)=2|E(P)\cap E(Q)|+\sum\ell(C_i)\) caps
  cycle-structure congruence information at parity (`A021` T1). No
  congruence-type theorem at any modulus can exclude case (5b) from
  the forced hypotheses alone; Petersen\(-e\) becomes the standing
  calibration object for future exclusion attempts.
- Ledger updates: `C036`/`C037` added; `L041`'s bound quoted at
  \(\ge18\) in `PROOF.md`; the `L042` "needs congruence-type tools"
  reading corrected (survivors: chain cancellation and
  power-freeness-active mechanisms); `G015`/`G013`(a) live moves
  rewritten; pivot triggers moved to order 17+.
- Next action: the chain-cancellation tension as the proof-side
  primary; the `G014` item-6 \(\{C_4,C_8\}\)-free generator as the
  search-side build before any order-17 leg.
- No proved row was falsified. `C001` stays `open`.

## 2026-07-24 — S021: orchestrated parallel legs — the chain case theorem-closed below 36, the generator built, order 17 empty, the counterexample floor at 20

- Second orchestrated parallel session (`O011`): worker W1 (`fable`) on
  the chain-cancellation tension, worker W2 (`opus`) on the `G014`
  item-6 generator; both audited line-by-line before integration; all
  ledgers held by the orchestrating session.
- W1 (`A022`, `E020`): the chain-case constraint system (`L043` — every
  prefix/suffix meets all three forbidden families and is
  non-bipartite; [min] engine: prefixes hide the second terminal);
  terminal power saturation (`L044`, filter strength); the collision
  table (`L045` — the cancellation is exactly three exponent-
  disjointness conditions; membership arithmetic can never exclude the
  chain case); the order dichotomy (`L046` — either \(H\) is
  2-connected or \(n_0\ge32\), sharpened to 36 by `C039`; the recorded
  falsifiable target delivered). Kill test refuted in range (`C038`:
  zero candidates over the order-\(\le14\) block catalogue, single
  mechanism — the forced 14; abstract solutions first at block orders
  15–16, the named rung). The chain floor (taut+cut needs order
  \(\ge15\)) retro-explains `C037`'s all-2-connected datum.
- W2 (`E019`): `genc48` = nauty geng + `prune_c8` PREPRUNE plugin
  (sha256-verified source, completeness argument recorded, 146 anchors
  under both interpreters, 23 `labelg` set-equality checks, res/mod
  partition checks, cubic-24 external positive control = Markström
  Table 3 = `E005`). Order-17 \(\mathcal G\)-profile run: **empty**
  (class 2,580 = unsplit count; `C039`) — every tight 1-atom has order
  \(\ge19\), every \(\mathcal G\)-member \(\ge18\); `C027`'s whole
  class empty at 16 and 17; \(C_{16}\) decisive at the three-degree-2
  boundary (first time in the dossier); ladder priced (18/19/20 ≈
  4 min/25 min/2.8 h on 8 workers; cubic 30 ≈ 2.3 days).
- Orchestrator audit of the flagged min-degree-3 sweep: stream-side
  slice checks at order 18 (parts 3/19 of 24 clean at close — 6.7M and
  7.6M graphs, zero \(C_8\)-free — plus the 12–17 full cross-checks and
  the cubic-24 control) → `C040` (no \(\{C_4,C_8\}\)-free
  \(\delta\ge3\) graph through order 19) and `L047`: **every
  counterexample has at least 20 vertices**; extremal window
  \([20,24]\).
- External input handled: user-supplied MathOverflow-512914 quote —
  cubic-20 figures corroborated (its {C4,C8}-free-cubic-empty verdict
  matches `E019`'s independent probe); its cubic→min-degree-3 step
  **rejected as an import** (that inference is the open `G015`);
  `references/mathoverflow-512914-audit-2026-07-24.md`.
- Close-of-session background follow-up launched
  (`E019/followup_s021.py`): MO recount (stage A), min-degree-3 order
  20 (stage B), bipartite order 24 on the new instrument (stage C).
  Not citable until harvested.
- Ledgers: `CLAIMS.md` `L043`–`L047`, `C038`–`C040` + dependency
  notes; `OBLIGATIONS.md` `G015`/`G013`(a)/`G014` (item 6 discharged;
  item 7 opened); `PROOF.md` (bounds, chain package, stale `G015` gap
  bullet repaired); `DECISIONS.md` (instrument adoption; chain-branch
  arithmetic retirement; MO rejection); `STATE.md` rewritten;
  `problem.json`/index; `PROJECT_STATE.md`.
- No proved row was falsified. `C001` stays `open`. Outlook 5% → 6%.

## 2026-07-24 — S021 follow-up harvest: order 20 empty (counterexamples ≥ 21), bipartite 24 empty, MO figures reproduced exactly

- The close-of-session background runs completed in-conversation and
  were harvested per the S019 precedent (single reconciliation commit).
- Stage A: stock-geng recount at order 20 — 510,489 connected cubic
  (= A002851) and 36,101 \(C_4\)-free cubic — **both MO-512914 figures
  exact**; MO-1/MO-2 upgraded to corroborated, MO-4 (the invalid
  inference) moot.
- Stage B: `genc48 -c -f -d3 20 30:190`, 16/16 parts, **empty** —
  `C040` extends to orders 14–20; **`L047`: every counterexample has
  at least 21 vertices**; extremal window \([21,24]\).
- Stage C: `genc48 -c -f -b -d2 24 35:276`, 16/16 parts, **empty** —
  `C034` extends through order 24 (25 with a pendant); first bipartite
  order covered by generation rather than genbg.
- Order-18 audit slice 11/24 landed clean (24,452,192 graphs, zero
  \(C_8\)-free): all three sampled slices (38.7M, ~24% of the stream)
  agree with the generator.
- Mid-wait user input recorded: the `G014` item-2 source title
  (Nowbandegani et al., "An Experimental Result on the Erdős–Gyárfás
  Conjecture in Bipartite Graphs") added to the obligation with the
  scope note that the reported \(\ge32\) bound covers only
  all-degrees-\(\ge3\) bipartite graphs — it does not touch the
  gadget class at 24–31, so the S016 de-gating stands.
- Ledgers reconciled: `C034`/`C040`/`L047`, the MO reference audit,
  `OBLIGATIONS.md`, `PROOF.md`, `STATE.md`, `PROJECT_STATE.md`,
  `problem.json` (next action: interference dissection + ladder
  18/19; Tier 3: kill rung, cubic 26/28, min-degree-3 21, bipartite
  25/26). S021 addendum records the harvest. Outlook unchanged (6%).

## 2026-07-24 — S022: orchestrated parallel legs — the interference model survives its frontier kill test, the calculus is fixed, the first profile object appears at 19, the atom floors move to 20

- Orchestrated run (third of its kind): W1 (`fable`) on the proof-side
  interference dissection (`A023`/`E021`), W2 (`opus`) on the
  \(\mathcal G\)-profile ladder at orders 18–19 (`E022`); this session
  held every ledger, audited both reports (anchors re-run, three W1
  sample claims and the W2 exemplar re-derived with independently
  written code, probes re-run exact), and integrated only what
  survived.
- On entry (user-requested): repaired `PROJECT_STATE.md`, which still
  carried the pre-harvest "first harvest the S021 follow-up" next
  action and bullet tail; no mathematical content changed.
- Proof side (`C041`/`C042`/`L048`, from `A023`/`E021`): all **553**
  blocking \(C_8/C_{16}\)s of the closest known objects — the
  min-\(C_8\) exemplars at 14–16 (exhaustively re-extracted: 11/20/103
  graphs with \(\le3\) \(C_8\)s; `E018` recorded only the statistic)
  and the three-degree-2 \(C_{16}\) boundary at 16–17 — are
  **two-through-path symmetric differences**; the non-interference
  pivot trigger did **not** fire. The property is empirically exactly
  vertex-tautness-shaped (biconditional at orders 10–12; zero failures
  over all 12,313 taut pairs of all connected graphs of orders 4–7),
  with necessity proved (`L048`(i)). `L048` fixes the calculus:
  interference = the \(t=1\), leak-pinned case of `A021` T1, and under
  completeness \(\mathrm{Spec}(B)=T_1(H,a,b)\cup(S+2)\) — power-
  freeness becomes through-path arithmetic, the genre surviving
  `C037`/`L045`. Candidate lemma T5 and forcing target (F) recorded as
  labelled conjecture/program with ordered kill tests; new second
  calibration object `M?AA@?WcKWHOWOL??` (order 14, full membership
  triple, 3 interference \(C_8\)s).
- Search side (`C043`, from `E022`): 146 anchors re-passed under both
  interpreters before production (byte-identical to `E019`'s). Order
  18: class 108,447, **profile empty**. Order 19: class 74,589,
  **profile = 1** — the first nonempty rung ever —
  `R???C@?GC_B?@_aAA_aP?W_?BO@Gc?`, vertex-taut, 2-connected,
  non-bipartite, **\(C_{16}\)-blocked (46) and \(S\)-violating
  (\(6,14\in S\)) independently**. Order-18 unsplit count exact;
  order-19 16-vs-24 dual-split labelg set-equal; 2,233 near-boundary
  graphs spot-checked by the brute-force enumerator; 0- and 1-buckets
  empty at both orders (different-tree corroboration of `C040`'s two
  flagged orders; direct tight-1-atom exclusion). **Every tight 1-atom
  and every \(\mathcal G\)-member has order \(\ge20\).**
- Close-of-session background follow-up (`E022/followup_s022.py`,
  results not citable until harvested): stage A — the order-19
  exemplar's full cycle set against T5 (it is vertex-taut, so a single
  non-decomposable cycle kills the lemma at the most relevant object);
  stage B — the order-20 profile rung (\(\approx\)2.5–3 h, 8
  workers); stage C — the order-19 unsplit count.
- Ledgers reconciled: `CLAIMS.md` (`L048`, `C041`–`C043`),
  `OBLIGATIONS.md` (`G015`, `G013`(a)), `PROOF.md`, `DECISIONS.md`,
  `STATE.md`, `problem.json`, index. Outlook 6% → 7%.

## 2026-07-25 — S022 follow-up harvest: T5 survives its first two kill rungs, order 20 is spent, the atom floors move to 21/22

- Stage A (the order-19 exemplar vs T5): **all 411 cycles decompose**,
  zero failures, every length \(\{3,5,6,7,9..19\}\) — the candidate
  lemma survived the sharpest available kill test, on the
  determined-partner algorithm (independent of `E021`'s pairwise).
- Stage C: the order-19 independent unsplit count = **74,589 exactly**
  — `C043`'s named partition follow-up is closed.
- Stage B (order 20): class 2,569,481 (16 parts, `--verify-all`),
  **profile 7** (parts 1/8/14), every one \(C_{16}\)-blocked, zero
  power-free; 0-/1-buckets empty; spotcheck 4,436 near-boundary
  graphs clean. With `C036`/`C039`/`C043`: **every \(\mathcal
  G\)-member has order \(\ge21\)**, and — `L041` cases (4)/(5)
  propagating `L047` and the \(\mathcal G\) floor — **every tight
  1-atom has order \(\ge22\)** (direct generation certifies 21).
- The three on-disk order-20 profile members (parts 1/8 complete)
  were verified and T5-tested by the orchestrator: all vertex-taut,
  2-connected, **all 1,890 cycles decompose**, 254 \(C_{16}\)
  verdicts re-verified pairwise; all three carry \(S\ni6,14\) — the
  order-19 double blocking repeats at every profile object seen.
- SAVE_LIMIT caveat recorded (new at 20): class files are per-part
  200k samples (572,530 of 2,569,481 saved; 18/19 were complete);
  part 14's four profile members fell outside the window — a
  dedicated single-part recollection with a stream-total assertion is
  running (`collect_n20_part14.py`), alongside stage D
  (`followup_s022b.py`: the min-degree-3 order-21 sweep, chained
  after the follow-up finished, anchor gate re-passed post-wait).
- Orchestrator audit before any ledger write: count/harvest/splitcheck
  JSONs re-read; the three members extracted by an independently
  written filter (a first-draft filter bug and a class-file-format
  assumption were caught and fixed — class lines carry metadata
  columns; extraction re-run clean); T5 machinery cross-checked
  between two algorithms on 254 shared verdicts.
- Ledgers reconciled: `C042`/`C043` extended, `G015`/`G013`(a),
  `PROOF.md` floors, `STATE.md`, `PROJECT_STATE.md`, `problem.json`.
  Outlook unchanged at 7% (the harvest landed inside the S022 call).

## 2026-07-25 — S022 second harvest: all eight profile objects survive T5; the counterexample floor moves to 22 (window [22,24])

- Part-14 recollection landed (two runs, identical aggregates — the
  first lacked per-graph persistence, a disclosed script bug, fixed
  and re-run): stream total 439,745 reproduced **exactly**; the four
  remaining order-20 profile members identified
  (`profile_n20_part14.g6`), all vertex-taut, 2-connected, 65–80
  \(C_{16}\)s, \(S\ni6,14\); **T5 survives on all four**
  (2,360/2,360 cycles). Cumulative (`C042`(e)): **all eight profile
  objects in existence (orders 19–20) survive T5 — 4,661/4,661
  cycles — and every one carries the \(S\ni\{6,14\}\) double
  blocking.** First member independently re-audited by the
  orchestrator (spectrum, 69 \(C_{16}\)s, S-set, 572 cycles).
- Stage D landed: **no \(\{C_4,C_8\}\)-free graph of minimum degree
  \(\ge3\) exists on 21 vertices** (16/16 parts empty, all return
  codes 0, anchor gate re-passed post-wait, 20,288 s wall on 8
  workers) — `C040` runs 14–21 and **`L047` lifts to: every
  counterexample has at least 22 vertices** (extremal window
  \([22,24]\), three orders wide; atom floors unchanged at 22/21).
- Ledgers reconciled: `C040`/`C042`/`C043`/`L047`, `OBLIGATIONS.md`
  (`G015`), `PROOF.md`, `STATE.md`, `PROJECT_STATE.md`,
  `problem.json`. Next action: the two remaining cheap T5 kill rungs
  (`smallworld 13`; sparse general 8–9), then the T5 proof attempt.
  Outlook unchanged at 7%.

## 2026-07-25 — S023: T5 is a theorem — the interference program's gate is passed; (F) is now the whole case-(5b) proof side below 36

- The two remaining pre-registered kill rungs ran **first** and
  survived (`E023`/`C044`): `smallworld 13` exhaustive in-class
  (class 10,966 = `A021`'s count; all 10,853 taut members pass on
  1,614,300 cycles; **all 113 non-taut members fail** — the
  biconditional exact at 13) and the general-graph probes (order
  \(\le8\) **exhaustive** — 218,095 taut pairs and 36.8M cycles at
  order 8 alone; cyclomatic-bounded slices at 9–11) — zero
  non-decomposable cycles anywhere.
- **T5 proved** (`A024`, offered and promoted as `L049`): every
  vertex-taut pair is interference-complete, in trunk-identical arc
  form with prescribed-edge freedom, via the **trimming
  construction** — tautness forces the block chain; Menger's fan +
  subdivision put a through-path through any prescribed cycle edge;
  trimming it at its first/last cycle contacts and completing through
  both arcs produces the witnessing pair. The recorded weaving
  obstruction is discarded with the path's middle; Lemma A
  (cycle-edge essentiality in taut pairs) is proved en route.
  Corollaries (`L050` + `L048`(iii) upgrade): completeness ⟺
  tautness on connected \(\delta\ge2\) graphs; the case-(5b)
  residual object's spectrum identity is **unconditional**
  (\(\mathrm{Spec}(B)=T_1\cup(S+2)\), every \(T_1\) element a
  trunk-split pair value).
- The proof was mechanically re-executed per instance (`E023
  constructive`: every cycle, every cycle edge — orders 4–7 general,
  8–9 slices, and the **eight profile objects** at 19–20 plus both
  calibration graphs; 17.4M (cycle, edge) instances, zero assertion
  failures; CPython cross-checks identical).
- **Adversarial review delegated and passed** (`R002`, fresh-context
  subagent, independence mode `delegated-subagent`): PASS at lemma
  level, 0 critical / 0 major, 2 minor + 6 notes — all eight repaired
  in place (splice rescoped as a standalone chain-splice lemma; the
  dense-run citation repaired to its landed figures; scope/symmetry
  clauses added; \(a\ne b\) made explicit; trunk-split defined; two
  block facts itemized in the references note). The reviewer re-ran
  every recorded command outside the repository and re-verified the
  claim set with a fully independent implementation (all labelled
  graphs through order 6; the ten named objects).
- Ledgers reconciled: `L049`/`L050`/`C044` new; `C042`/`L048`
  updated; `G015`/`G013`(a) rewritten; `PROOF.md`; `DECISIONS.md`;
  `references/textbook-classics-2026-07-25.md` (Menger \(k=2\)/
  Whitney + block facts, precise statements). Next action: the (F)
  program's first falsifiable move — the power-collision realization
  tables of the ten named objects. Outlook: 7% → 8%.

## 2026-07-25 — S024: the (F) opening probe is spent — no membership mechanism; the trunk bound; (F) re-aimed as (F-S) ∨ (F-T)

- Session `S024` ran the recorded first move of the (F) program: the
  complete **trunk-split power-collision realization tables** of the
  ten named objects (`E025`; the eight profile members re-verified
  field-by-field against `E022` records, Petersen\(-e\) from `E013`
  core 3, the order-14 exemplar against `E021` family-1 data).
  Anchors first per standing rule: `E021`'s 45-check suite through
  the import plus 14 new-code checks (including a weave control the
  trunk-split classifier must reject), both interpreters. Totals:
  604 power cycles, 61,901 witnessing pairs, 1,971 trunk-split
  realizations, every `L049` arc-form invariant asserted per pair,
  full-payload CPython cross-check identical; **neither pre-registered
  soundness alarm fired** (every power cycle has a trunk-split
  realization — `L049` corroborated again).
- **The pre-registered verdict is branch (b)**: none of the nine
  membership patterns (fixed in code before the first table) is
  universal; even the weakest disjunction fails — **30 cycles across
  six profile objects are membership-blind** (entire trunk-split sets
  \(\{(5,13,1)\}\), \(\{(9,11,2),(10,10,2)\}\), or \(\{(5,11,0)\}\));
  the calibration pair's 100% `has_PP` structure (every calibration
  \(C_8\) realized by two power-length paths) collapses to
  1–8/37–112 at the frontier. **The membership-collision form of (F)
  is dead** (`A025` T1, `C045`) — the empirical third leg beside
  `C037` (congruence caps at parity) and `L045` (memberships cannot
  exclude the chain case).
- Proved en route: **`L051`, the trunk bound** — in `L049`'s arc form
  \(s=t_a+t_b\le n-L\) (trunks live on off-cycle vertices), hence
  \(x+y\le2n-L\) — **tight on all ten objects** (max \(s=n-L\)
  exactly: 2/6/3/4 at orders 10/14/19/20). With `L048`(iii) the
  case-(5b) collision system is order-confined (\(C_{32}\) at order
  \(\le33\): \(s\le1\)).
- Frontier saturation recorded (`A025` T3): all eight profile objects
  have spectrum exactly \([3,n]\setminus\{4,8\}\) and
  \(S\supseteq[6,n-1]\) with \(6,14\in S\) (the double blocking read
  as saturation); the only known \(\mathbb P-2\) dodges are the
  calibration pair (orders 10/14), both gapping \(S\) exactly at 6.
- **(F) re-aimed** (`A025` T4): (F) = **(F-S)** (window forces
  \(S\cap\{6,14\}\ne\emptyset\); closure blocked) **∨ (F-T)** (window
  forces \(16\in\mathrm{Spec}\); \(H\) blocked) — either closes case
  (5b) below 36; both order-windowed and correctly failing off-window
  on the calibration pair. Candidate mechanism:
  saturation/interpolation (through-set lower bounds in taut windowed
  pairs — the named missing tool).
- Ledgers reconciled: `L051`/`C045` new; `G015` updated; `STATE.md`,
  `problem.json`, index. `PROOF.md`/`DECISIONS.md` unchanged (no
  integrated-argument change; no statement/assumption change —
  the (F) split is program structure inside `G015`). Next action:
  the **S-gap census at the window bottom** (`A025` T5) over the
  on-disk 18–20 classes (+21 when `E024` lands): a vertex-taut
  member with \(S\cap\{6,14\}=\emptyset\) kills (F-S) and becomes
  calibration object #3; none ⟹ (F-S) survives its first kill test.
  Background: `E024` (order-21 rung) ran throughout and is **still
  running** — excluded from every ledger row. Outlook: 8% (unchanged).

## 2026-07-25 — S025: the S-gap census is spent — (F-S) survives its first kill test; the tautness-only saturation mechanism is refuted

- Ran `A025` T5, the recorded next action, as `E026`: the S-gap census
  over every unordered degree-2 pair of every \(\{C_4,C_8\}\)-free
  class member on disk — orders 10–19 complete, order 20 the
  per-part-complete 11/16-part sample (572,519 graphs; the S022
  "572,530 saved" figure counted the 11 class-file headers — corrected
  against the authoritative scan tallies) plus the four recorded
  part-14 profile members. 18,754,354 pairs over 767,004 members.
  Design refinement recorded in `S025`: the exactly-two stratum at
  18–20 is fully known (the eight profile objects), so the faithful
  nonvacuous census quantifies over all degree-2 pairs; the
  exactly-two stratum is (F-S)'s hypothesis class proper.
- Anchors first (standing rule): `E021`'s 45-check suite through the
  import plus 57 new checks, under CPython 3.14.2 **and** PyPy 7.3.23
  — the calibration pair must be *found* gapped+taut (it is), the
  eight profile objects saturated field-for-field against the `E022`
  records, three independent enumerators agreeing on 20,554 pairs.
- **Verdict (pre-registered outcome (i)): zero (F-S) kill
  candidates.** No exactly-two member of any censused class carries a
  gapped pair (\(S\cap\{6,14\}=\emptyset\)); all eight profile
  objects re-verified \(6,14\in S\). (F-S) survives its first kill
  test exactly where the residual object lives.
- **The recalibration: the dodge is abundant off the profile.** 9,061
  vertex-taut gapped pairs at orders 12–20 (2,727/167/5,756 at
  18/19/20; rate 0.01–0.2% of pairs, no monotone decay), 6,934 of
  them full \(\mathbb P{-}2\) dodges (2, 6, 14 all absent), 5,419
  rows on **power-free** members, most on 2-connected members —
  at window orders there exist 2-connected
  \(\{C_4,C_8,C_{16}\}\)-free vertex-taut pairs with
  \(S\cap\{2,6,14\}=\emptyset\) and 4–11 degree-2 vertices. So
  **tautness + class + window order do not force the poisons**: the
  tautness-only form of the saturation mechanism is refuted, and any
  interpolation lemma proving (F-S) must consume the exactly-two
  profile (minimum degree \(\ge3\) off the terminals). The gradient:
  min degree-2 count of a dodge-carrying member is 5/6/4 at
  18/19/20, never \(\le3\) anywhere (thin strata caveat recorded).
  The (F-T) reading is parallel: the double blocking is
  profile-specific, not a class phenomenon.
- Verification: every gapped pair and profile member recomputed by
  the `E018` full enumerator with verdicts asserted (540,135
  agreements per run) + deterministic stride sample (3,867 more);
  per-line integrity on every member; `power_free` flag re-verified
  on every 500th member and every gapped row; **two full production
  runs with identical tallies** (storage trimmed to taut-only rows
  between them, `run1_tallies.json` preserving run 1); zero
  bipartite members anywhere in the censused classes.
- Ledgers reconciled: `C046` new; `G015` updated (live move (i) is
  now the profile-consuming interpolation attempt); `STATE.md`,
  `problem.json`, index. `PROOF.md`/`DECISIONS.md` unchanged (no
  integrated-argument change; (F-S)/(F-T) statements unchanged — the
  census refined the mechanism inside `A025` T4's frame, which
  already listed the profile degrees among the candidate hypotheses).
  Next action: the profile-consuming interpolation attempt — target
  lemma \(S\supseteq[c,n-1]\), \(c\le14\), for vertex-taut
  \(\{C_4,C_8\}\)-free pairs with all non-terminal degrees \(\ge3\)
  in the window; first sub-move: dissect the stored near-miss corpus
  against the eight profile objects for the structure of the extra
  degree-2 vertices. Background: `E024` (order-21 rung) ran
  throughout, untouched, **still running** — excluded from every
  ledger row; harvest it first when it lands. Outlook: 8% (held).

## 2026-07-25 — S026: the corpus dissection — three rigid dodge shapes, the subdivision frame, and the chord-exchange engine (`A026`/`E027`/`C047`)

- Session `S026` opened the profile-consuming interpolation attempt
  (`A026`) and ran its first falsifiable sub-move: the dissection of
  `E026`'s 9,061-row near-miss corpus against the eight profile
  objects (`E027`; anchors 35 checks under CPython 3.14.2 and PyPy
  7.3.23; production single-process nice-15 beside the running
  `E024`; every corpus row structurally re-validated, \(\min
  S=d(a,b)\) asserted per row, every 250th row fully re-enumerated,
  the `L035` parity law asserted on all 9,061 corpus rows and 7,781
  control taut pairs with zero violations).
- **The dodge taxonomy is rigid** (`C047`(a)): every stored dodge is
  shape A (short + 6-hole; \(\max S=13\) exactly on every minimal
  full dodge at orders 16–20), A′ (distance: \(\min S=7\) exactly,
  never more), or B (long-range: holes exactly at \(\{6,10,14\}\);
  even part \(\subseteq4\mathbb Z\) — the `L034` channel-(iii)
  pattern realized in-window on non-bipartite members; needs \(\ge7\)
  degree-2 vertices). The 14-dodge is never by distance, the 6-dodge
  never by shortness.
- **The dodge is pair-local and the frontier is two subdivisions from
  the profile** (`C047`(b)): the order-20 ndeg2-4 frontier members
  (incl. one adjacent-terminals full dodge, \(S=\{1\}\cup[8,13]\),
  which reduces recursively to an off-terminal distance dodge) carry
  five fully saturated sibling pairs each — member-level hypotheses
  are dead.
- **The subdivision frame** (`C047`(c)): corridor weights are 2–3
  (never \(\ge5\)); 99.1% of dodge rows (8,978/9,061), smoothed at
  their pair, reduce to graphs whose simple part carries a
  \(C_4\)/\(C_8\) — near-misses are subdivisions of class-violating
  graphs; the profile is the subdivision-free stratum. Killed
  candidates: member-level lemmas, odd-cycle-supply discrimination
  (100% of dodge members have triangles).
- **Control base rates** (556 members, 14,098 full enumerations):
  ordinary taut pairs break the upper-interval property at 12–17%
  (holes concentrated at 7–9, nearly gone by 13); Hamiltonian pairs
  22–29%; the profile-8's joint gap-free + Hamiltonian saturation is
  far outside both.
- **The span law and the exchange engine** (`A026` T5/T6,
  `C047`(f)): proved — no path in a \(\{C_4,C_8\}\)-free graph has a
  chord of span 3 or 7; and the first-order disjoint-chord calculus
  on one Hamiltonian path per profile object generates the entire
  top of \(S\) down to 10 (misses confined to \([4,9]\)) —
  **including 14 on all eight** — while on the 36 Hamiltonian
  dodgers it fills no interval (two span-2 chords + spans
  \(\equiv1,2\bmod4\) make savings \(\equiv3\bmod4\) unreachable).
  Soundness asserted throughout (every generated length is a real
  path in the recorded \(S\)).
- **The target splits** (`A026` T7): (L-A) ∧ (L-B) ⟹ (F-S) — (L-A)
  short-range exclusion (in-window profile pairs have \(\max
  S\ge14\), or \(6\in S\) when short; thin margin, no engine yet);
  (L-B) long-range poison forcing (\(\max S\ge14\Rightarrow14\in S\)
  or \(6\in S\); engine validated — the span/savings combinatorics
  of longest-path chord systems). The missing tool named by `A025`
  T4 sharpens accordingly.
- Ledgers reconciled: `C047` new; `G015` updated (S026 update: the
  split, the engine, the new move order); `STATE.md`,
  `problem.json`, index. `PROOF.md`/`DECISIONS.md` unchanged (no
  integrated-argument change; (F-S)/(F-T) statements stand verbatim —
  the dissection refined the mechanism and split the lemma inside
  `A025` T4's frame). Next action: **harvest `E024` first** (ran
  throughout, untouched, still running — excluded from every ledger
  row), then the (L-B) chord-savings attempt (kill discipline: fail
  on the 36 Hamiltonian dodgers, hold on the eight), then (L-A)
  ear-overload. Outlook: 8% (held).

## 2026-07-25 — S027: (F) becomes a decision procedure and comes back empty on the Hamiltonian stratum (`A027`/`L052`, `E028`/`C048`, audit `R003`)

- Session goal (user-directed): skip the unfinished `E024` harvest —
  its likely outcome moves a floor without bearing on (F) — and go
  straight to the highest-value proof move, the shortcut/chord
  ("(L-B)") route of `A026` T7.
- **Route change inside `A025` T4's frame, reduction-first instead of
  lemma-first.** Rather than trying to prove savings reachability by
  hand, `A027` proves two reductions that make the question finite:
  **`L052`(ii) the chord-minimal descent** — on a pair with a
  Hamiltonian \(a\)–\(b\) path the chords cover every path position
  (0 and \(M\) exactly once), and any inclusion-minimal subcover
  \(\mathcal C'\) gives \(H'=P+\mathcal C'\) with the same degree
  profile, the same Hamiltonian path,
  \(\mathrm{Spec}(H')\subseteq\mathrm{Spec}(H)\) and
  \(S(H')\subseteq S(H)\) — so any "avoid these cycle lengths and
  these through-lengths" hypothesis is inherited and the search may
  be restricted to chord-minimal systems; **`L052`(iii) the monotone
  reroute** — interval-disjoint chord families are genuine paths, so
  a savings hit certifies a poison length, monotonically and on
  prefixes.
- **Two aims sharpened, both strictly in our favour.** Decide the
  **disjunction** (F) directly rather than (F-S)/(F-T) separately
  (only (F) closes case (5b), and assuming both conclusions fail
  supplies \(C_{16}\)-freeness as a *free* extra hypothesis); and use
  the whole poison set \(\{2,6,14,30\}\) rather than \(\{6,14\}\)
  (\(30+2=32\); at long path lengths 30 is the cheap target).
- **Verdict (`E028`/`C048`).** Run B (\(\{C_4,C_8,C_{16}\}\), the (F)
  hypothesis): **empty at every order 16–29**, the last completed rung, so
  case (5b) is closed there for every residual object carrying a
  Hamiltonian through-path. The \(C_{16}\) hypothesis cut the node growth
  from \(\approx\times3.5\) to \(\approx\times1.9\) per order (a
  \(27\times\) node reduction at order 21) and carried the ladder eight
  orders past the recorded frontier in under an hour.
- **Audit `R003` (delegated fresh-context reviewer): PASS at
  lemma-and-instrument level** — 0 critical, 4 major, 4 minor, 3 notes.
  T1/T2/T6 correct as stated; the enumerator exhaustive over chord-minimal
  covers; every prune one-sided; the symmetry break lossless. The reviewer
  re-ran the shipped instrument outside the repository and reproduced run A
  \(M=15..21\) and run B \(M=15..23\) node counts **to the last digit**,
  and its own from-scratch enumerator (sets not bitmasks, no reservation
  propagation, no symmetry break) is set-equal to `Search` everywhere it
  ran and independently returns empty for run B at orders 19–25.
  All four majors repaired in place:
  - **F1/F2** — none of the three loss-capable prunes (poison DP, reversal
    symmetry break, \(C_{16}\) detection) was exercised on a positive or
    nonempty instance by any recorded check: the \(\{C_4,C_8\}\)-free
    chord-minimal class is empty below order 19, so every `a3` comparison
    was \(\emptyset=\emptyset\), and the depth-15 \(C_{16}\) branch was
    only ever called on graphs of order \(\le12\), where it can only
    return `False` — a bug there would have produced exactly the observed
    all-zero table. **Repaired** by new anchor families a6 (539 positive,
    63 negative \(C_{16}\) instances across \(M=15..34\), three
    detectors) and a7 (reversal closure and poison-prune selection on the
    nonempty order-19/20 cover sets, plus the full production
    configuration against the independent reference on nonempty sets);
    suite now **80,131** checks under both interpreters, identical
    histograms.
  - **F3** — the "brings the whole window into range" claim is
    **withdrawn**: that was the node ratio; wall-clock growth is 1.8–2.4
    per rung and rising, so orders 30–35 are days of single-core
    computation. The ladder is recorded as an open-ended computation with
    a stated last completed rung.
  - **F4 (the scientifically interesting one)** — the poison prune's
    branch kills fall 61, 33, 45, 17, 2, 1, **0, 0, 0** at
    \(M=20\ldots28\), so from \(M=26\) the tree with the poison test is
    identical to the tree without it. What run B proves at orders 27–29 is
    the **stronger**, poison-free statement that the
    \(\{C_4,C_8,C_{16}\}\)-free chord-minimal Hamiltonian exactly-two
    stratum is empty — implying (F) a fortiori but exercising none of its
    forcing mechanism. **No inference about why the poisons appear is
    supported above order 26.**
  Minors/notes answered in `E028/README.md`: provenance and revision drift
  (F5), the reproduction block and anchor count (F6), the cross-check
  restated at **isomorphism** level where it is *stronger* than claimed —
  1 and 7 classes at orders 19 and 20, set-equal to the recorded objects
  (F7), and removal of the "eighteen objects" over-count with its
  selection bias, since objects built on a Hamiltonian path are no
  evidence about the non-Hamiltonian gap (F8).
- **New objects.** Run A (\(\{C_4,C_8\}\) only) exhibited the **first
  \(\mathcal G\)-profile objects at orders 21 and 22** — 10 and 43
  chord-minimal ones, 3 and 16 isomorphism classes, all 2-connected,
  girth 3, 91–186 \(C_{16}\)s — every one killed twice (\(14\in S\)
  on all 53, \(6\in S\) on 40, a \(C_{16}\) on all 53).
- **Saturation is not the mechanism.** 13 of the order-22 objects have
  \(S\) **not** a full interval (holes at \(\{6\}\), or
  \(\{2,3,4,6,7\}\) with adjacent terminals) — the first in-window
  exactly-two objects to break the `A025` T3 pattern, while still
  carrying 14 and a \(C_{16}\). The saturation form of the pivot
  trigger is retired; the live form is a hole at **14**.
- **Independent cross-check of the recorded ladder** from a different
  generation principle: with the poison prune off, chord-minimal cover
  counts are 0 at orders 12–18 and 6, 65 at 19, 20, with only
  invariant signatures already recorded for the eight profile objects
  — reproducing `C027`/`C039`/`C043` without geng.
- **Correction recorded** (`A027` T6): a hand-derived chord-pair table
  entry was wrong — interior-disjoint chords close **no** extra cycle
  with the path. Caught by the instrument's own anchors before use;
  nothing downstream depended on it. `A026` T5's span law is
  unaffected.
- Adversarial audit **`R003`** opened and delegated to a fresh
  `proof-reviewer` subagent, targeted at the two fatal spots: whether
  the descent is lossless and whether any prune can discard a genuine
  counterexample.
- Named residue (`A027` T5): the **non-Hamiltonian stratum**. First
  purchase: a zero-savings two-attachment off-path component forces an
  all-equal-length — hence bipartite — interior-degree-\(\ge3\)
  gadget, exactly the class `L035`/`C034` has been emptying.
- Ledgers reconciled: `L052`/`C048` new; `G015` updated (S027 update);
  `STATE.md`, `problem.json`, index, `LOG.md`. `PROOF.md` unchanged
  (no integrated-argument change for statement 0.1);
  `DECISIONS.md` records the route change from proving a disjunct to
  deciding the disjunction. Next action: **finish the `E028` ladder to
  order 35**, then the non-Hamiltonian stratum, with the `E024`
  harvest behind them. `E024` ran throughout, untouched, still
  running, excluded from every ledger row. Outlook 8% → 10%.

## 2026-07-25 — S027 post-close review: the moves are re-ordered, and the E024 harvest is promoted to first

- Not a new investigation; a re-reading of `S027`'s own results, prompted
  by the question of what the remaining compute is actually buying.
- **The remaining risk in case (5b) is stratified by shape, not by size.**
  `E028` cleared the **Hamiltonian** stratum at orders 16–29. The
  **non-Hamiltonian** stratum is cleared at *no* order — including the ones
  already done. So finishing the ladder to 35 completes nothing; it widens
  the axis that was already the easy one. `R003` F4 sharpens this: above
  order 26 the ladder had stopped exercising (F)'s mechanism at all.
- **Consequence.** The decisive question is now the split itself: does the
  exactly-two profile force a through-path covering every vertex? All eight
  independently generated profile objects have \(\max S=n-1\), but that is
  eight points at orders 19–20, and `C047`(e)'s control says only 22–29% of
  ordinary taut degree-2 pairs are Hamiltonian. `E024` measures exactly this
  at order 21, over the **complete** class rather than the Hamiltonian-only
  slice `E028` can see — so the harvest deferred at the S027 open is
  promoted to the first move. Recorded in `DECISIONS.md`; this reverses the
  session's own opening judgement.
- Cheap proxy available immediately, on data already on disk: sweep the
  orders 18–20 classes by degree-2 count and see whether \(\max S=n-1\)
  becomes universal as that count falls toward two.
- The `E028` ladder is to **stop after order 30**: orders 32–35 are days of
  single-core computing, do not parallelise as the instrument stands, and
  would prove class-emptiness rather than poison forcing.
- Tooling half recorded separately as **`O012`** (planned, nothing
  executed): move `E024` to Railway on the Pro plan — it is already 16
  independent `geng` res/mod parts, so it parallelises perfectly, and
  usage-based billing makes width nearly free (~$10 of compute, about an
  hour instead of fifteen). Blocking precondition: the linux/amd64 rebuild
  must re-pass `E019`'s 146-anchor gate plus the cubic-24 positive control
  before any cloud output is citable, and the new sha256 is recorded as an
  architecture-tagged **second** pin, not a replacement.
- No claim, obligation, proof, statement or status changed. `E024` and the
  `E028` ladder both still running, both excluded from every ledger row.

## 2026-07-25 — S028: the order-30 rung lands empty and the ladder is stopped; the E024 rung moves to Railway

- **`E028` order 30 (\(M=29\)) is EMPTY**: 0 survivors, 49,882,612 nodes,
  4,195.9 s, `capped: false` (exhaustive, not truncated). `C048` extends from
  orders 16–29 to **16–30**. The poison prune's kills are 2, 1, 0, 0, 0, 0 at
  \(M=24\ldots29\), so by `R003` F4 order 30 — like 27–29 — proves the
  *stronger* poison-free class-emptiness statement and exercises none of (F)'s
  forcing mechanism.
- **The ladder is stopped there**, executing the S027 post-close decision
  rather than rolling into order 31. Recorded for the future: the search *is*
  parallelisable — its DFS branches at position 0 over the single chord
  \((0,q)\), giving \(\approx M\) independent root subtrees — so the stop is a
  judgement about mathematical value, not a computational limit.
- **Provenance gap found and closed.** The production process began at 14:03
  while `search.py` was edited at 15:19 (the `R003` a6/a7 repairs, made during
  the run), and only one revision was ever committed, so the rungs came from an
  instrument that could not be diffed against the recorded one. Closed by two
  re-runs on the **committed** instrument: the anchor suite reproduced
  `anchors_search_pypy.json` byte-identically except its own timing field
  (80,131 checks, identical histograms), and the order-30 rung was **re-run end
  to end** and agrees with the production record on **every field** — survivors
  0, nodes 49,882,612, `capped` false, and all seven prune counters identical to
  the digit (cycle 1,334,986,730, reserve 233,544,446, cover 44,065,721, …),
  only the wall clock differing (2,907.2 s against 4,195.9 s). Seven independent
  counters in the billions cannot match if the traversal was perturbed, so the
  repairs are confirmed confined to the anchor suite.
- **`O012` is EXECUTED** (operational, committed separately): `E024`'s order-21
  rung now runs on Railway behind a **passed** linux/amd64 anchor re-gate —
  the 146-check suite, the cubic-24 positive control, the stream cross-check at
  orders 12–17 and a production-modulus partition check, all verified locally
  against the dossier; the amd64 `genc48` sha256 is recorded as an
  architecture-tagged **second** pin beside the untouched arm64 one. Six
  services, 24 workers each, modulus 144. The laptop is freed.
- **Two corrections to `O012`'s premises**, both measured: a Pro service is
  capped at **24 vCPU**, not 1,000; and **width is not free** — `geng`
  duplicates the whole tree above split level \(n-4\) once per part, so total
  work is \(\text{mod}\times A+B\) and, with the largest part running 2.86× the
  mean, the wall clock has a floor no modulus can beat. "About an hour instead
  of fifteen" was not achievable.
- **An instrument caveat worth carrying**: `scan.py` writes a part's class file
  only under `SAVE_LIMIT = 200,000` graphs, and the graph6 strings of
  degree-profile members exist **only** there (every profile object found so
  far is \(C_{16}\)-blocked, so they are not among the scan JSON's
  `survivors`). At order 20 this left only 3 of 7 members recoverable from
  stored class files; in the stopped order-21 laptop run, part 0/16 emitted
  210,802 graphs and took 8 of its 11 profile members with it. Modulus 144
  keeps every part far under the limit.
- The stopped laptop run's six completed order-21 parts are banked as a
  cross-check (359,199 graphs, 11 profile members, all \(C_{16}\)-blocked) and
  are **not** citable as a rung.
- No statement, proof, or decision changed. The `E024` cloud rung is excluded
  from every ledger row until harvested.

## 2026-07-26 — S029: the order-21 rung is empty, and the profile is Hamiltonian 19 for 19

- **The `E024` order-21 rung landed and is harvested** (`C049`). Complete
  \(\{C_4,C_8\}\)-free class at order 21: **2,951,168 graphs**, 652,935
  generator cpu-seconds (181.4 core-hours), 144-part split, max 33 edges.
  Degree-profile members: **19**, **all \(C_{16}\)-blocked**, **zero power-free
  survivors**. So \(\mathcal G\) is empty at 21 as well — every
  \(\mathcal G\)-member has order \(\ge22\), every tight 1-atom \(\ge23\).
- **THE DECISIVE MEASUREMENT: \(\max S = 20 = n-1\) on all nineteen.** Every
  order-21 profile member carries a Hamiltonian \(a\)–\(b\) path. Cumulatively
  **27 of 27** in-window profile objects, against `C047`(e)'s measured control
  of **22–29%** for ordinary taut degree-2 pairs. The pre-registered pivot did
  **not** fire, so `C048`'s ladder is *supported* — not proved — to address
  case (5b) as a whole rather than a Hamiltonian-only sub-stratum.
- **Scope kept explicit: this is evidence, not a theorem.** 27 examples do not
  force Hamiltonicity, and the non-Hamiltonian stratum (`A027` T5) is cleared
  at no order. What changed is the prior, from 8 points at two orders to 27
  across three.
- **Refinement:** 18 of the 19 carry both 6 and 14 in \(S\); one does not
  (\(d(a,b)=4\), \(S\cap\{2,6,14,30\}=\{14\}\)), so `A025` T3's
  \(S\supseteq[6,n-1]\) saturation is **not universal** at order 21 while the
  double blocking survives. The break `S027` first saw at order 22, one order
  lower.
- Verification before any number was used: 144/144 parts present exactly once,
  every file matching the sha256 its container recorded, per-part coverage
  identity holding, and the harvest plus the measurement run with the **local,
  already-anchored arm64 instrument**. Three parts (115, 99, 142) exceeded
  `SAVE_LIMIT` and have no class file; each was checked and holds **zero**
  profile members, so nothing was lost — recorded because that was luck, not
  design.
- Recalibration carried to `process/compute.md`/`O012`: modulus sizing must be
  driven by the **tail** of the part-size distribution, not the mean. Three
  parts exceeded the limit (one by 1.8×), and the wall clock came in at 14.4 h
  against a ~7 h projection — the mean was predicted well, the tail was not.
- Outlook 8% → **9%**. No statement, proof, or decision changed.

## 2026-07-26 — S030: the non-Hamiltonian stratum gets an engine, and the (F) programme gets a ceiling

- Session goal: the recorded next action (`A027` T5 — extend the chord-minimal
  descent from chords to **bridges**), under the standing user steer to bias
  toward proof-side work rather than moving computational boundaries.
- **The recorded best alternative died first, cheaply.** `L053` (`A028` T1): a
  cubic non-Hamiltonian graph of girth \(\ge17\) minus an edge is an
  exactly-two-profile, 2-connected, \(\{C_4,C_8,C_{16}\}\)-free pair with **no**
  Hamiltonian through-path, so `C049`'s 27/27 cannot be promoted to a lemma at
  class strength. Recorded as **calibration object #3**. Asymptotic — it
  exhibits nothing in \([18,35]\) and moves no floor.
- **The obstruction `A027` T5 named is removed.** `L055` (`A028` T3–T7): every
  off-path component of a longest through-path admits a bridge with savings
  \(\ge1\) — \(\ge2\) with three or more attachments, by the Y-identity
  \(\sigma(i,k)=\sigma(i,j)+\sigma(j,k)+2\beta\), which consumes maximality
  alone; with exactly two attachments, by parity, via the new `L054` bipartite
  exclusion dichotomy with its power-freeness hypothesis finally matched.
  Zero-savings components do not exist. The stratum is still cleared at **no**
  order: `A028` T8 records the two remaining gaps.
- **The architectural finding.** `L046` gives 2-connectivity only below order
  36, so the (F) programme — even decided completely on both strata — closes
  case (5b) for \(n_0\le35\) and cannot prove `G015`. With `R003` F4 (the
  ladder proves class-emptiness above order 26) and `L053` (the ambient class is
  nonempty at arbitrarily large order, so that verdict must fail), the ladder is
  demoted from the proof-side route to a source of floors.
- **Successor architecture recorded:** **(INT) ∧ (L-A)** (`A028` T9) — (INT)
  says \(S\supseteq[8,\max S]\) for a vertex-taut \(\{C_4,C_8\}\)-free
  exactly-two-profile pair; with \(\max S\ge14\) it forces \(14\in S\), which
  is poison, hence (F-S) **at every order**, no window and no \(C_{16}\)
  hypothesis. `C050`/`E029` kill-tested it on data already on disk (nothing
  generated): 24 recorded profile objects, zero violations, every hole in
  \(\{4,5,6\}\); the constant 8 is the smallest the near-miss corpus permits;
  a hole at 14 needs five more degree-2 vertices than the profile has. New en
  route: a second non-interval profile object, at order 20.
- Three decisions recorded (`DECISIONS.md`): the ceiling, the successor
  architecture, and the retirement of the Hamiltonian-forcing route.
- Outlook unchanged at **9%** — the ceiling cost about what the order-unbounded
  successor bought. No statement, status, or floor changed.

## 2026-07-26 — `S031`: the kill test that was never run — the interpolation genre is empty

- Session `S031`, attempt `A029`, review `R004` (delegated fresh context),
  reference `X004`. Proof-side only; no generation, no experiment.
- **The recorded next action was not executed.** Its target is false. The
  dossier's binding kill discipline (`A021`, restated in `A026`) requires a
  candidate lemma to be tested against **every** calibration object before it
  is worked on; `C050` tested (INT) against the 24 profile objects on disk
  and never against Calibration object #3, which S030 had built eight
  theorems earlier in the same attempt.
- **`L056`.** **(INT) and (INT-14) are both false**, with explicit witnesses
  that import nothing: the **truncated Petersen graph** (each vertex blown up
  to a triangle; cubic, 3-connected, spectrum below 13 \(=\{3,10,11,12\}\),
  hence \(\{C_4,C_8\}\)-free) minus a **link** edge is a 2-connected
  vertex-taut exactly-two-profile pair of order **30** with \(S=[9,26]\), so
  \(8\notin S\); chaining two copies at a cut vertex gives order **59** with
  \(S=[18,52]\), so \(14\notin S\). Asymptotically the same follows from
  `L053` (\(\min S\ge16\) at girth \(\ge17\)) — which is the route the
  session found first.
- **The audit made the row stronger.** `A029`'s draft asserted that no such
  object exists below order 70; `R004` F4 refuted that clause and supplied the
  order-30 object, which was rebuilt and verified here (`E030/truncation.py`).
  So the refutation is **not asymptotic**: (INT) is false *inside* the
  case-(5b) window the ladder is climbing.
- **Why `C050` survived.** Every recorded profile object has \(\min S\le5\).
  Nothing with \(\min S>8\) has ever been *generated*, because the ladders
  stop at order 21 and the smallest witness has order 30. The test measured
  the corpus's order range, not the class.
- **`L057`.** The natural repair fails too: the **triangle expansion** of a
  bipartite cubic 3-connected graph of girth \(\ge10\), minus an edge far
  from the triangle, is a *non-bipartite* class member whose through-set has a
  parity hole at \(\min S+1\ge10\). So \(S\supseteq[\min S+c,\max S]\) fails
  for every \(c\), and the recorded pivot trigger fires. Modulo `X004`
  (bipartite cubic 3-connected graphs of fixed girth \(\ge10\) and unbounded
  diameter), an existence use inside a negative result. **This half FAILED its
  audit twice and is NOT ESTABLISHED.** Round 1 (`R004` F1–F3, F5) and round 2
  against the repairs (**F11**: the diameter route is a non sequitur once
  \(ab\) is fixed — repaired again, the requirement is on the **order** via
  the tree ball bound \(\lvert B(\{a,b\},r-1)\rvert\le2^{\,r+1}-2\),
  automatic at \(g=10\)). **`R004` F3′ remains open:** `X004`'s
  3-connectivity clause has no source. `L057` stays at `proposed` and may not
  be cited; the genre conclusion does not depend on it.
- **The genre is empty**, and it is the third: congruence (`C037`), membership
  (`L045`/`C045`), interpolation (`L056`/`L057`). One diagnosis fits all
  three — every class-level hypothesis is local and hereditary, hence
  inherited by large-girth cubic graphs minus an edge. Power-freeness *above
  the girth* and minimum-order minimality have never been consumed by an
  (F)-side lemma.
- **Conditional residue** (`A029` T3(b)): any interpolation lemma plus
  `L042`'s forced power/Mersenne memberships plus the poison condition pins
  \(S\) into one dyadic band, \(\max S<2\min S+O(1)\) — `L031`/`L032`'s
  block-question constraint. Recorded as a convergence, explicitly not
  progress.
- **`L058`.** `A022` W1-T8 re-derived from the current block-order floor
  (21): **either \(H\) is 2-connected or \(n_0\ge42\)**. With `C049`'s
  tight-1-atom floor the case-(5b) window is \(n_0\in[23,41]\), i.e.
  \(H\)-orders \([22,40]\) — so the `E028` ladder, stopped at 30, is **ten**
  rungs short of it, not four. The correction sharpens S030's ceiling finding
  rather than softening it. A first guess in the same session that the
  re-derivation would *widen* the programme's reach was wrong and is
  corrected in place.
- **No floor, status, or statement changed.** Every refuting object contains
  \(C_{16}\) and is far from power-free; nothing here bears on statement 0.1.
- **Audit `R004` (delegated, fresh context): FAIL at lemma level** — 2
  critical, 2 major, 4 minor, 2 notes. T1 passed and was strengthened by F4;
  T2 failed and is repaired but unaudited; T3(b) passed up to side conditions
  now carried. All ten findings are answered in the review record.
- Tier 1's primary work returns to the non-Hamiltonian stratum (`A028` T8's
  two gaps), with the standing instruction that every lemma drafted for it be
  checked against Calibration object #3 first.
- Outlook **9% → 7%**: the previous estimate's stability rested on an
  order-unbounded successor that is now refuted, the refutation is generic
  rather than incidental, and the one arithmetic improvement runs against the
  finite-window route.

## 2026-07-26 — S032 (orchestrated, nine delegated Opus workers)

- **The session broke with the recorded route on purpose.** `S030` had already
  proved the (F) programme cannot prove `G015`, and `G015` is itself only a
  reduction of 0.1; a final session was directed at statement 0.1 itself. Every
  leg was aimed at the conjecture, not at the reduction. Nine workers, no access
  to the dossier narrative, orchestrator re-verification of every load-bearing
  computation with independent code.
- **`L059` (subdivision barrier).** Any class closed under subdivision and any
  target avoiding \(t\mathbb N\): the implication fails, because
  \(L(G^{(t)})=t\,L(G)\). With \(t=3\) and the powers of two: **no
  subdivision-closed hypothesis implies 0.1's conclusion.** Every through-set /
  ear / theta / exchange / interference law is subdivision-covariant, so the
  whole (F) programme — `L048`–`L052` included — cannot reach 0.1 however far it
  runs. Smallest defeater \(K_4^{(3)}\). `L049` stands as a theorem; what is
  delimited is its use.
- **`L060`/`L061` — a proved case of 0.1, and the dossier's first result about
  0.1 rather than about a reduction.** `L060`: in a \(C_4\)-free graph a 5-cycle
  with three edges in triangles forces a \(C_8\) (verified exhaustively to order
  11, 143,038 graphs). `L061`: discharging gives \(m\le2n-2\chi(S)\) for
  \(\{C_4,C_8\}\)-free graphs on a surface, and against \(m\ge2n\) from
  \(\delta\ge4\) this yields **every planar graph with \(\delta\ge4\) contains a
  cycle of length 4 or 8** — also projective-planar, and 2-connected
  toroidal/Klein. By-product \(\mathrm{ex}_P(n,\{C_4,C_8\})\le2n-4\), apparently
  the first bound for a *set* of forbidden cycle lengths. Prior art: not found
  in either the EGC or the planar-Turán corpus.
- **`L064` — `G013`(c) resolved.** A gadget whose through-set lies in one
  residue class mod any \(m\ge3\) makes 0.1 already false via a proper subgraph;
  equivalently \(d(S)\in\{1,2\}\) always. The odd-prime-gcd channel, open since
  S016 with no theory and no search, is closed — along with every modulus.
  Conditional on the Fan import (`G017`).
- **`L062`/`L063` — two further barriers.** No additive surgery on a minimum
  counterexample can contradict anything (only length-preserving or
  power-of-two-multiplying reductions can), and girth does not localize the
  spectrum (cubic graphs of girth exactly \(g\) with no cycle in \([g+1,M]\),
  explicit 768-vertex witness). The orchestrator's own contraction lemma was
  audited and found **true but vacuous**, exactly as `L062` predicts; its
  residue is `L065`.
- **`L065`** — a minimum-order counterexample is non-bipartite, bridgeless,
  has no proper subgraph of minimum degree 3, has all blocks non-bipartite, and
  is not a regular \(2^s\)-lift. Not found in the literature. Does **not**
  settle bipartite EGC.
- **Frontier imports the dossier was missing entirely.** Exoo (arXiv:1403.5636):
  \(G_{78}\), \(G_{450}\), \(G_{420}\) — the real near-counterexamples, far
  stronger than the order-24 graphs in use here, and now the primary calibration
  objects (`G018`). Heckman–Krakovski conclude "\(2^m\), \(2\le m\le7\)", not "4
  or 8" — the buckyball is a 3-connected cubic planar \(\{C_4,C_8\}\)-free
  witness (verified). Liu–Montgomery (JAMS 2023): 0.1 is entirely a
  bounded-degree question. Dean–Lesniak–Saito (1993): \(\delta\ge3\) forces a
  cycle \(\equiv0\bmod4\), and \(\equiv0\bmod k\) is forced iff \(k\le4\) — the
  mod-\(k\) route is capped permanently. Erdős (1997) believed 0.1 **false**.
- **Withdrawn en route:** "every non-planar graph has a cycle of length
  divisible by 4" was derived and verified here but is in print
  (Győri–Li–Salia–Tompkins–Varga–Zhu, JCTB 176 (2026), Lemma 2, same reduction);
  its cubic corollary is weaker than Dean–Lesniak–Saito. Retained as a verified
  fact, not as a novelty claim.
- **Counterexample side:** none. New order-98 cubic \(\{C_4,C_8,C_{16}\}\)-free
  graph; leaf-gadget census exhaustive to order 23 (22,455,873 graphs, zero
  survivors) — and that family is genuinely *not* covered by the standard
  2-connectivity reduction, because suppressing a degree-2 cut vertex shifts
  lengths by 1. Substitution barrier measured: gadgets whose own cycles miss
  4, 8, 16 have \(\rho\ge7/3>2\), so the top band is forced to contain a power;
  300 H7-inflations all miss exactly \(\{4,8,16\}\) and all contain 32 and 64.
  Margin \(f(k)/2^{k+1}=1.25,\,1.5,\,\ge1.69\) — **widening**, which is evidence
  that 0.1 is **true**.
- Hamiltonian stratum: exact structure theorem for \(L(C_n+M)\); verified for
  all \(n\le42\) with a \(\le4\)-chord certificate; depth exactly 4, so no
  shallow proof exists there.
- Outlook **7% → 7%** (unchanged in number, changed in content): a proved case
  and a closed channel push up; three genres proved incapable — including the
  one this dossier was built on — push down.

## 2026-07-26 — S032 round 2 (four further legs, all aimed at closing)

- **`L066` the chaining barrier (fourth barrier).** The \(t\)-necklace of a
  two-terminal gadget has \(L(N_t(W))=L(W)\cup\{t+\sum\tau_i\}\). With
  \(W=K_4-e\) this gives **cubic, 2-connected, Hamiltonian** graphs with spectrum
  \(\{3,4\}\cup[3t,4t]\) — **Conjecture SF is false**. With a 10-vertex \(W\)
  bridging \(K_{2,3}\) and \(K_{2,3}+e\), for odd \(t\) the necklace is cubic
  with **entire even spectrum \(\{4\}\)**. So no window strengthening of 0.1 of
  any width is true, and exporting Liu–Montgomery to \(\delta=3\) is impossible
  because their *conclusion* is false there. Both verified independently.
  Self-limiting under 2-connectivity: iterating the gadget narrows the top window
  to \(6/5\) but at the third step a window reappears; only the connectivity-1
  parity construction collapses the even spectrum, and a parity lemma shows it
  *requires* connectivity 1.
- **`L067` SF4**, the repair: every \(C_4\)-free graph with \(\delta\ge3\) has a
  window. Implies 0.1 with no exceptional graph. **But it is a strengthening, not
  a reduction** (addendum 2): the universality construction \(W=H+\{u,v\}\) with
  \(uv,uz,vz\) makes "SF4 for necklaces" \(\iff\) SF4, so any proof of it proves
  0.1 for \(C_4\)-free graphs. Monotonicity then kills the whole composite genre:
  a window of any piece is a window of the whole, so no amalgam refutes SF4
  unless every piece is window-free — and exhaustively, over 22.5M \(C_4\)-free
  graphs and 20.9M gadgets at orders 8–15, there are **none**. SF3 is false only
  degenerately (\(K_4,K_5,K_5-e,W_4\)); Merker's gap families do **not** refute
  it, since a single gap cannot kill a window.
- **`L068`–`L070` the bipartite case.** Every bipartite graph with \(\delta\ge3\)
  embeddable in the **torus** contains a cycle of length 4, 8 or 16 — a second
  proved case of 0.1, sharp in all three lengths; the planar sub-case is a
  one-liner (every planar bipartite \(\delta\ge3\) graph has a \(C_4\)).
  Refuted en route: "bipartite + girth 6 \(\Rightarrow C_8\)" is **false**, by
  the hexagonal torus \(H(19,1,8)\) — cubic, bipartite, order 38, girth 6, zero
  8-cycles (orchestrator-verified) — which is provably the toroidal minimum.
  Plus the bipartite localization barrier and a **hand** lower bound \(n\ge30\).
- **`L071`–`L073`, `C051` the planar case.** Density sharpens to
  \(20m\le39n-78\) via a face lemma (5-face \(\le2\) triangular neighbours,
  6-face \(\le1\), 7-face none), giving strictly larger closed cases. Step A
  closes: a **minimum** planar counterexample is 2-connected or is two equal
  blocks at one degree-4 cut vertex — proved by a **doubling** argument, which is
  length-preserving and hence exactly what `L062` permits. Step C is **false**:
  two buckyballs glued at a vertex are planar with \(\delta\ge3\), a degree-6
  vertex and no \(C_4\)/\(C_8\). The smallest 3-connected cubic planar
  \(\{C_4,C_8\}\)-free graph is unique at order 24 (`C051`, verified).
- **`L074` the substitution route closed as a theorem.** \(\rho\) is *exactly
  multiplicative* under composition, so iteration only increases it and the only
  value stable under unbounded iteration is \(\rho=1\); every \(\rho=1\) gadget
  contains a bridge cutting off a leaf gadget, so \(H[W]\) is power-free iff that
  leaf gadget is — **substitution contributes nothing and reduces to itself**.
  The orchestrator's proposed "\(\rho\ge2\)" barrier is false (the triangle has
  \(\rho=3/2\); an explicit order-241 gadget has \(\rho=1\)); multiplicativity is
  the correct closing statement.
- **`C052` the many-gaps lead, tested and dead.** arXiv:2506.09667's family has
  **all gaps in the first half**; the second half is a full interval, hence
  contains a power of two. The authors' own open problem — *gaps in the second
  half of the cycle spectrum* — is exactly the shape a counterexample needs, and
  nobody can produce one.
- Outlook **7% → 8%**: two proved cases of 0.1 and a closed disproof genre push
  up; four proved barriers and the discovery that SF4 is a strengthening rather
  than a reduction push down.
