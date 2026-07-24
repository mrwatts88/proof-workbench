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
