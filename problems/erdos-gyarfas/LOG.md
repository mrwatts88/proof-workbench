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
