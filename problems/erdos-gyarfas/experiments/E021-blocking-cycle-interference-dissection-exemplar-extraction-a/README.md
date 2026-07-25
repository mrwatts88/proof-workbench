# E021 — Blocking-cycle interference dissection: exemplar extraction at orders 14-16 and the two-through-path decomposition test

- Date: 2026-07-24
- Problem: `P-002`
- Evidence class: descriptive structure-mining of finitely many named
  graphs (plus one exhaustive-extraction layer and one exhaustive
  small-order probe; see Logical scope)
- Owner: session `S022`, worker leg W1 (attempt `A023`)

## Question

The pinched-world interference census is perfect: every \(C_8\) of every
equality block and witness in the taut pinched catalogue is the
symmetric difference of two through-paths (`C031`/`C032`/`C035`; 23/23
at the five blocks). Does the same interference structure govern the
**blocking cycles of the objects closest to the case-(5b) target
profile** — the graphs one or two cycles away from being tight-1-atom
reducts?

Per graph and per blocking cycle \(C\), the predicate (matched to
`E013`'s recorded census semantics — `catalogue.py` `dissect`/`cores`:
`e1 ^ e2 == edges` over `itertools.combinations(all_ab_paths(H,a,b),
2)`): for the two-terminal reading \((H,a,b)\),

> \(C\) is a **two-through-path symmetric difference** iff there exist
> two distinct simple \(a\)–\(b\) paths \(P,Q\) of \(H\) with
> \(E(C)=E(P)\,\triangle\,E(Q)\).

All blockers are counted, as in the recorded census; additionally every
blocker is stratified by terminal usage — through **both** terminals /
through exactly **one** / through **neither** — because a cycle through
both terminals decomposes trivially into its two arcs (a structural
fact, asserted by the engine on every such blocker): the informative
content is in the other two strata.

Families:

1. **Family (1)** — the minimum-\(C_8\)-count members of the `E018`
   profile class (connected, \(C_4\)-free, exactly two degree-2
   vertices, all others \(\ge3\)) at orders 14/15/16 (recorded minima
   1/2/1). `E018` recorded only the statistic, so every member with
   \(C_8\) count \(\le3\) is re-extracted here from the same stream.
   Blockers: their \(C_8\)s. Vertex-tautness is recorded for every
   exemplar (the `mod4.py` essential-vertex instrument).
2. **Family (2)** — the three-degree-2 boundary graphs of the
   \(\{C_4,C_8\}\)-free class at orders 16 (4 graphs) and 17 (12
   graphs), from `E019/data/spotcheck_n{16,17}.json` (`graphs` filtered
   to `n_degree_2 == 3`); all \(C_8\)-free and \(C_{16}\)-blocked
   (`C039` — the only decisive \(C_{16}\)s in the dossier). Blockers:
   their \(C_{16}\)s, tested against **all three** degree-2 terminal
   pairs; a blocker is non-interference only if **no** pair decomposes
   it.
3. **Family (0)** (calibration) — the five `E013` equality blocks (P10
   = Petersen\(-e\), A11, B11, C12, D14) re-dissected with the same
   engine, so the strata of the recorded 100% census are on file next
   to the new families.

Supplementary probe (`smallworld`): over the full profile class at
orders 10–12 with power-freeness dropped, is **every cycle of every
length** of every vertex-taut member an interference cycle? This
decides whether the candidate lemma should quantify over blockers or
over all cycles.

## Logical scope

- The **extraction layer is exhaustive** for the stated class: the
  stream `geng -q -c -f -d2 n mine:maxe` (mine
  \(=\lceil(3n-2)/2\rceil\): 20:91 / 22:105 / 23:120 at 14/15/16; order
  16 in `E018`'s 24-part res/mod split) covers every connected
  \(C_4\)-free graph with exactly two degree-2 vertices and the rest
  \(\ge3\) at these orders, and the per-order stream totals, class
  sizes and minima are asserted equal to `E018`'s records. So "the
  minimum \(C_8\) count is 1/2/1" and "these are **all** members with
  \(\le3\) \(C_8\)s" are exhaustive statements at orders 14–16.
- The **dissection itself is descriptive structure-mining of finitely
  many named graphs**: 11 + 20 + (order-16 exemplars) family-(1)
  graphs and 4 + 12 family-(2) graphs. It proves **no universal
  statement** — not about the class at other orders, not about
  power-free graphs, not about statement 0.1. Its verdicts are exact
  for the graphs dissected.
- The `smallworld` probe is exhaustive over the profile class at orders
  10–12 (power-freeness dropped) and proves nothing beyond those
  orders.
- Family (2)'s stratification is nearly forced by order: a \(C_{16}\)
  at order 16 is Hamiltonian (stratum "both" for every pair,
  trivially decomposable); at order 17 it misses exactly one vertex.
  The family-(2) census is therefore dominated by the trivial stratum
  and is recorded as such; the informative rows are the order-17
  readings whose missed vertex is a terminal.

## Environment

- macOS 15 / darwin 25.5.0, arm64, 12 cores.
- PyPy 7.3.23 (Python 3.11.15) for all production runs; CPython 3.14.2
  additionally for the anchor suite (both pass all 45 checks).
- nauty 2.9.3 `geng` from `/opt/homebrew/bin` (the `E018` `GENG`
  constant, resolved on PATH).
- **Machine-contention note** (`process/concurrency.md`): this leg ran
  as worker W1 of the orchestrated session S022 while sibling worker W2
  held 8 generator processes on the same 12-core machine. W1 used at
  most **4 concurrent processes**, and only for the order-16
  extraction (`run16x4.py`); everything else single-process. All
  timings below are contended-machine figures, not benchmarks.
- Standard library only; deterministic; no randomness; wall clock only
  in timing fields.
- **Primitives are imported, not copied**: `E018/scan.py` is loaded by
  file path under the module name `scan` (its `DATA` constant
  redirected to `E021/data` immediately after load, before any call;
  the module has no import-time side effects), `E018/mod4.py` supplies
  `paths_with_essential` (the vertex-tautness instrument of
  `A021`/`C037`), and `E013/catalogue.py` supplies the census
  machinery itself (`all_cycles`, `all_ab_paths`, `isomorphic`, ...;
  its `DATA` likewise redirected). No primitive was re-implemented.
  `sys.dont_write_bytecode` is set before the loads so the imports
  leave no bytecode caches in the sibling experiment directories
  (three cache files written by the pre-guard anchor runs were
  removed; the post-guard anchor re-runs, 45/45 under both
  interpreters, confirm nothing reappears).

## Inputs and search space

- Family (1) stream: `E018`'s `geng_args(n)` verbatim —
  `geng -q -c -f -d2 n mine:maxe` with mine \(=\lceil(3n-2)/2\rceil\),
  maxe \(=\binom n2\); order 16 split `r/24`, \(r=0..23\), run at most
  4 parts concurrently. Collection threshold: \(C_8\) count \(\le3\)
  (covers the recorded minima 1/2/1 with headroom; the count histogram
  is recorded in full, so the threshold's position in the distribution
  is visible).
- Family (2): the 16 boundary graphs from `E019`'s spotcheck files
  (already exhaustive for `n_degree_2 == 3` at orders 16–17 by
  `C039`'s generation layer).
- A \(C_8\)-free family-(1) profile member, if one appeared, would
  contradict `C036`'s lineage and is trapped by an explicit assertion
  (full survivor analysis + hard failure).

## Reproduction

```sh
pypy3   dissect.py anchors        # 45 checks; also passes under python3
pypy3   dissect.py extract 14     # asserts stream/class/min vs E018
pypy3   dissect.py extract 15
pypy3   run16x4.py                # 24 parts, at most 4 concurrent workers
pypy3   dissect.py harvest16      # merge, assert totals vs E018
pypy3   dissect.py dissect        # families (0), (1), (2)
pypy3   dissect.py smallworld 10 11 12
pypy3   dissect.py tautgeneral 4 5 6 7
```

Outputs land in `data/`: `extract_n14.json`, `extract_n15.json`,
`extract_n16_part*of24.json`, `extract_n16.json`,
`interference_family{0,1,2}.json`, `smallworld_full_spectrum.json`,
`tautgeneral.json`.

## Anchors

45 checks, passed under both interpreters before production:

- **Toolchain (through the `E018` import):** Petersen\(-e\) profile
  pair, \(S=\{4,5,7,8\}\), exactly 7 \(C_8\)s (`C031`), spectrum
  \(\{5,6,8,9\}\), \(C_4\)-free, vertex-taut with full essential mask
  (`mod4` instrument); \(K_{3,3}-e\) profile pair and \(S=\{3,5\}\);
  Petersen 12 pentagons / 10 hexagons; order-8 profile class = exactly
  one member, \(C_8\)-blocked with count 1 (`E016` A6 / `E018`).
- **Census (the dissection engine against `E013`'s records):** on all
  five equality blocks (adjacency and terminals read from
  `E013/data/cores.json`), the engine reproduces the recorded
  \(C_8\) counts (3/3/5/7/5), the recorded 23/23 decomposable
  verdict, and the **exact** recorded `symdiff_combos` dictionaries
  (length-pair × shared-edge-count multiplicities) — plus core 3
  isomorphic to an independently built Petersen\(-e\), and the
  `E018` counter equal to the `E013` enumerator on every block.
- **\(C_{16}\) machinery:** the 16-cycle graph has exactly one
  \(C_{16}\), decomposed by the antipodal arc pair (1 decomposing
  pair, stratum "both").
- **Stratum controls:** a \(C_8\) with a pendant 2-path, read from the
  tip to a cycle vertex, is a one-terminal blocker decomposed via the
  attachment vertex (positive); a \(C_8\) hung by a bridge off a
  two-path theta between the terminals is stratum "neither" and **not**
  decomposable (negative — the engine can say no).
- **Data cross-check:** one family-(2) spotcheck graph's recorded
  spectrum reproduced by the `E013` enumerator (all 16 are re-checked
  during `dissect`).
- **Per-run assertions:** every dissected graph re-checks
  `path_lengths` (`E018`) = `all_ab_paths` lengths (`E013`) =
  `paths_with_essential` lengths (`mod4`) — three instruments, one
  answer — and `count_cycles_len` (`E018`) = the `E013` enumerator's
  count; every stratum-"both" blocker is asserted decomposable (the
  arc-decomposition theorem); family-(2) spectra are asserted equal to
  `E019`'s recorded spectra, with \(4,8\notin\) spectrum,
  \(16\in\) spectrum.

## Results

### Extraction (family 1) — every agreement check passed

| n | stream (= `E018`) | class (= `E018`) | min \(C_8\) (= `E018`) | count histogram, low end | exemplars \(\le3\) | time |
|---|---|---|---|---|---|---|
| 14 | 1,706,820 | 130,461 | 1 | 1:**1**, 2:0, 3:10 | 11 | 6.0 s |
| 15 | 20,629,645 | 1,826,839 | 2 | 2:**3**, 3:17 | 20 | 73.9 s |
| 16 | 346,573,602 | 29,713,305 | 1 | 1:**3**, 2:6, 3:94 (4:149, 5:490, 6:924) | 103 | 2,365.7 CPU-s, 616 s wall on 4 workers |

No \(C_8\)-free profile member appeared at any order (the trap assertion
never fired — consistent with `C027`/`C036`). 134 exemplars total.

### The dissection — **every blocker in every family decomposes**

**Family (0), calibration (five equality blocks; recorded census
reproduced exactly, including the full combos dictionaries):**

| block | order | \(C_8\)s | strata both/one/neither | decomposable |
|---|---|---|---|---|
| P10 = Petersen\(-e\) | 10 | 7 | 2 / 4 / 1 | 7/7 |
| A11 | 11 | 3 | 0 / 1 / 2 | 3/3 |
| B11 | 11 | 3 | 0 / 2 / 1 | 3/3 |
| C12 | 12 | 5 | 0 / 4 / 1 | 5/5 |
| D14 | 14 | 5 | 0 / 4 / 1 | 5/5 |

Of the 23 recorded-census \(C_8\)s only 2 are in the trivial stratum:
the pinched-world 100% was substantive, not arc-driven.

**Family (1), min-\(C_8\) exemplars (blockers = their \(C_8\)s):**

| n | exemplars | taut | \(C_8\)s | both (dec) | one (dec) | neither (dec) | non-interference |
|---|---|---|---|---|---|---|---|
| 14 | 11 | 11/11 | 31 | 0 (0) | 6 (6) | 25 (25) | **0** |
| 15 | 20 | 20/20 | 57 | 0 (0) | 5 (5) | 52 (52) | **0** |
| 16 | 103 | 103/103 | 297 | 5 (5) | 71 (71) | 221 (221) | **0** |

385/385 blockers decomposable; 380 of them lie in the informative
strata (one/neither). Every exemplar is vertex-taut; 132/134 are
2-connected (the two cut-vertex exemplars occur at orders 15 and 16 —
consistent with `C038`'s chain floor: taut + cut vertex is impossible
below order 15); 0/134 bipartite. Every decomposition satisfies
\(x+y-2s=8\) (asserted over all 18,299 decomposing pair-incidences);
length differences \(y-x\in\{0,2,4,6\}\); shared-edge counts \(s\) run
0–11 with mode 7, and only 5 incidences have \(s=0\) (the
disjoint-union type of `L033`) — the generic interference is
heavy-overlap window-rerouting. Two exemplars (both order 14) have
\(S\cap\{2,6,14\}=\emptyset\); one of them,
`M?AA@?WcKWHOWOL??` (terminals (6,7), \(S=[3,13]\setminus\{6\}\),
spectrum \(\{3,5,\dots,14\}\), 2-connected, non-bipartite, 52
through-paths), satisfies the **full forced membership triple** of
`L042` while vertex-taut — an order-14 Petersen\(-e\)-strength
realization datum with only 3 \(C_8\)s, all stratum-neither, all
decomposable.

**Family (2), three-degree-2 boundary graphs (blockers = their
\(C_{16}\)s; all three terminal pairs):**

| n | graphs | \(C_{16}\)s | (blocker, pair) readings | both | one | neither | non-interference |
|---|---|---|---|---|---|---|---|
| 16 | 4 | 8 | 24 | 24 (24 dec) | 0 | 0 | **0** |
| 17 | 12 | 160 | 480 | 396 (396 dec) | 84 (**84 dec**) | 0 | **0** |

Every blocker decomposes for **every** pair, not merely some pair. The
stratification is order-forced (a \(C_{16}\) at order 16 is
Hamiltonian; at 17 it misses one vertex, so "neither" cannot occur);
the informative content is the 84 order-17 one-terminal readings —
all decomposable, each in 7–40 ways. All 16 graphs are vertex-taut for
all three pairs.

### `smallworld` — the tautness dichotomy (exhaustive, orders 10–12)

Full profile class, power-freeness dropped, **every cycle of every
length** tested:

| n | class | taut | taut cycles (non-dec) | non-taut members | non-taut cycles (non-dec) | non-taut members with a non-dec cycle |
|---|---|---|---|---|---|---|
| 10 | 22 | 22 | 729 (**0**) | 0 | — | — |
| 11 | 125 | 124 | 6,749 (**0**) | 1 | 27 (26) | 1/1 |
| 12 | 1,139 | 1,120 | 101,404 (**0**) | 19 | 1,141 (1,122) | 19/19 |

On this 1,286-member sample the biconditional is **exact**: a member
has all cycles decomposable iff it is vertex-taut. (The necessity
direction is a one-line lemma — see `A023` T2: an interference cycle
lies inside the essential subgraph, since its vertices lie on the two
witnessing paths.)

### `tautgeneral` — hypothesis probe (exhaustive, all connected graphs, orders 4–7)

All 19,476 vertex pairs of all connected graphs of orders 4–7; among
the 12,313 **vertex-taut** pairs, all 723,926 (pair, cycle) instances
tested: **zero non-decomposable** — with no degree condition and no
\(C_4\)-freeness anywhere. The interference property appears to rest
on vertex-tautness alone.

### Timings and cross-interpreter check

Anchors: 45/45 under PyPy 7.3.23 and CPython 3.14.2. Dissection run:
6.0 s under PyPy; re-run under CPython 3.14.2 produced **byte-identical
`graphs` payloads** for all three family JSONs (production copies are
the PyPy run). `smallworld` 10.5 s, `tautgeneral` ~80 s (PyPy).

## Interpretation

Narrowest justified conclusions.

1. **Exhaustive at orders 14–16:** the minimum \(C_8\) count over the
   profile class is 1/2/1, and the 134 collected graphs are *all*
   members with \(\le3\) \(C_8\)s (stream, class and minima asserted
   equal to `E018`'s independent records).
2. **The dissection verdict (descriptive, named graphs):** all 385
   family-(1) \(C_8\)s and all 168 family-(2) \(C_{16}\)s — 553
   blockers, 380 + 84 of them in informative strata — are
   two-through-path symmetric differences; family (2) decomposes for
   every terminal pair. **No non-interference blocker exists at the
   frontier**; the recorded pivot trigger ("a non-interference blocking
   \(C_8/C_{16}\) among the boundary exemplars") did **not** fire, and
   the pinched-world interference model survives its cheapest kill test
   at exactly the closest known objects to the case-(5b) target.
3. **Every family-(1) exemplar is vertex-taut** — tautness, generic in
   the class at 10–13 (`C037`), is universal at the min-\(C_8\)
   frontier 14–16.
4. **The tautness dichotomy (exhaustive at 10–12, in-class):**
   interference-completeness (every cycle a two-through-path symmetric
   difference) holds for every vertex-taut member and fails for every
   non-taut member of the sample. Together with the order-4–7
   general-graph probe (zero failures over 723,926 instances with no
   side conditions), this isolates **vertex-tautness** as the exact
   hypothesis of the candidate lemma recorded in `A023`.
5. **What none of this proves:** no universal statement at any
   unscanned order; nothing about power-free graphs (all dissected
   objects are blocked by construction); nothing about statement 0.1.
   The candidate lemma and the forcing program built on it are recorded
   in `A023` at conjecture strength with this experiment as their
   evidence inventory.

## Independent checks

- The extraction layer's stream totals, class sizes and minima are
  asserted equal to `E018`'s independently produced records at all
  three orders (stream 1,706,820 / 20,629,645 / 346,573,602; class
  130,461 / 1,826,839 / 29,713,305; min \(C_8\) 1/2/1).
- The dissection engine reproduces `E013`'s recorded census on all five
  equality blocks exactly (counts, verdicts, and the full
  `symdiff_combos` multiplicity dictionaries).
- Every dissected graph passes the three-instrument path-set agreement
  and the two-instrument cycle-count agreement described under Anchors.
- Family-(2) inputs are re-verified against `E019`'s recorded spectra
  (which were themselves second-algorithm re-checks of the generator).
- Not independently re-implemented: geng itself (imported generation
  layer, anchored as in `E010`–`E018`).
