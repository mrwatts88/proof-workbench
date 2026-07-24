# E014 — Band-4 pencil dichotomy verification and the C4-allowed block probe

- Date: 2026-07-24
- Problem: `P-002`
- Evidence class: exhaustive instance verification of proved lemmas
  (falsification search for `A015` T1–T4) plus a hypothesis-necessity probe

## Question

1. **Part A / AG (dichotomy verification).** For every graph in the stated
   streams and every unordered vertex pair at distance exactly 4, verify the
   `A015` pencil package on all x–y paths of length 4 ("4-paths"):
   - a pair of internally disjoint 4-paths exists **iff** an 8-cycle passes
     through both terminals (general graphs, T1′);
   - if no two 4-paths are internally disjoint, all 4-paths share a common
     internal vertex (general graphs, T1);
   - the vertices at distance 2 from both terminals are exactly the middles
     of 4-paths (general, T0);
   - a unique 4-path implies a unique such (2,2)-vertex;
   - under C4-freeness additionally (T2): two distinct 4-paths share at most
     one internal vertex; with ≥ 2 paths the common vertex is unique and
     adjacent to a terminal (no middle pencils); at a fan the middles and
     exits are pairwise distinct and no cross chord `m_i b_j` (i ≠ j) exists.
2. **Part B (hypothesis necessity, C4 allowed).** Among all 2-connected
   graphs with minimum degree ≥ 2 and at most two sub-cubic (= degree-2)
   vertices, scanning every terminal pair that contains all degree-2
   vertices with the `E013` closed-band scanner: do vertex-taut cores with
   \(s_{\max}\le 2\,d(a,b)\) exist that are **strict** (\(s_{\max}\le2d-1\)),
   or **C8-free at band 4**, once C4s are allowed?

## Logical scope

Part A/AG is exhaustive for the stated streams and orders (geng-generated,
same tool caveats as `E010`–`E013`): it can refute but not prove the `A015`
lemmas; the lemmas rest on the hand proofs in `A015`. A failure would print
the offending graph6 string and pair. Part B is an exact finite catalogue
for its class; its positive findings are constructive counterexamples that
delimit hypotheses (they show which statements CANNOT hold without
C4-freeness); emptiness findings there would have been only order-bounded.
Nothing here bears on statement 0.1 directly.

## Environment

- PyPy 7.3.23 (Python 3.11.15); geng from nauty 2.9.3 (`/opt/homebrew/bin`).
- Graph primitives imported from `../E013-…/catalogue.py` (g6_decode,
  degrees, has_c4, bfs_all, cut_vertices, scan_pair_banded, all_cycles),
  anchored there (88 checks, re-passed under PyPy this session).
- Integer bitmask arithmetic; no randomness.

## Inputs and search space

- Part A: `geng -q -c -f n` (connected C4-free, no degree restriction),
  n = 5…11; all unordered pairs at distance 4 (116,187 pairs).
- Part AG: `geng -q -c n` (all connected graphs), n = 5…9; 43,419 pairs.
- Part B: `geng -q -c -d2 n mine:0` with mine = ⌈(3n−2)/2⌉, n = 6…9;
  graphs filtered to ≤ 2 sub-cubic vertices and 2-connectivity; terminal
  pairs = pairs containing every degree-2 vertex (both terminal degrees
  ≥ 2 automatically); per pair the `E013` `scan_pair_banded(closed=True)`
  verdict; spectra by the exact cycle enumerator.
- Fixed anchors: (1) the 6-vertex double-middle gadget (two 4-paths sharing
  two internal vertices, C4 present) — T2(a)'s hypothesis is essential;
  (2) the 7-vertex product fan (four 4-paths pencilled at a middle vertex,
  C4s present) — T2(b)'s hypothesis is essential.

## Reproduction

```sh
pypy3 probe.py a 5 6 7 8 9 10 11    # C4-free verification (T0,T1,T1',T2)
pypy3 probe.py ag 5 6 7 8 9         # general-graph verification (T0,T1,T1')
pypy3 probe.py b 6 7 8 9            # C4-allowed block probe
```

Outputs: `data/verify_c4free.json`, `data/verify_general.json`,
`data/block_probe_no_c4_assumption.json`.

## Results

**Part A (C4-free, orders 5–11).** 22,901 graphs, 116,187 distance-4
pairs, zero assertion failures. Outcomes: 6,883 pairs with internally
disjoint 4-paths (each verified to carry a C8 through both terminals),
23,227 terminal-adjacent pencils (fan sizes 2: 22,332; 3: 885; 4: 10),
86,077 unique-path pairs, and **zero middle pencils** — exactly the T2(b)
prediction. Both anchors pass.

**Part AG (general, orders 5–9).** 273,183 graphs, 43,419 distance-4
pairs, zero failures of T0/T1/T1′. Middle pencils occur (946) but only
with C4s present; disjoint-pair ⟺ C8-through-terminals holds in every
case.

**Part B (C4 allowed, orders 6–9).**

| n | stream | 2-conn, ≤2 sub-cubic | pairs | closed taut hits | strict | with C4 | C8-free |
|---|---|---|---|---|---|---|---|
| 6 | 55 | 44 | 358 | 15 | 6 | 15 | 15 |
| 7 | 467 | 385 | 4,075 | 89 | 2 | 89 | 89 |
| 8 | 7,358 | 6,268 | 89,719 | 101 | 26 | 101 | 34 |
| 9 | 196,904 | 179,303 | 3,578,244 | 919 | 48 | 919 | 46 |

Key specimens (all with C4s):

- \(K_{3,3}-e\) (order 6, terminals its degree-2 pair): **strict block**,
  band 3, \(S=\{3,5\}\) — the smallest strict block; strictness without
  C4-freeness starts at order 6.
- Order 8, e.g. `G?ovTg` pair (1,3): **strict band-4 block with
  \(S=\{4,5,6,7\}\)** — exactly the strict-rung target shape, realized
  with C4s.
- Order 9, e.g. `H?r@d_{` pair (1,6): **band-4 equality core with
  \(S=\{4,\dots,8\}\) and no C8** (spectrum \(\{4,5,7,9\}\)) — the
  equality-power-rung conclusion fails without C4-freeness.

Every closed taut core found at orders ≤ 9 contains a C4 (consistent with
`C031`: the first C4-free block is Petersen−e at order 10).

## Interpretation

- The `A015` pencil package survives an exhaustive falsification search on
  both its general and C4-free forms; ledger row `L033` cites this
  experiment as instance verification.
- Both band-4 block rungs genuinely consume C4-freeness: the strict rung's
  target configuration and a C8-free equality core both exist with C4s at
  orders 8–9. No C4-agnostic proof of either rung can exist, and any proof
  must use C4-freeness beyond its role in the pencil refinements (the
  order-8/9 specimens also contain C4-free-violating fans/pencils only in
  the excluded sense — their 4-path systems are legal for general graphs).
- Ledger update: `C033`.

## Independent checks

- All primitives are the `E013`-anchored implementations (independent of
  the new four_paths enumerator, which is checked against them implicitly:
  middles-vs-(2,2) equality ties the layered enumeration to BFS distances,
  and the C8-through-terminals equivalence ties disjoint-pair detection to
  the independent cycle enumerator on every one of the 159,606 pairs).
- Part B re-derives, in an independent degree regime, facts consistent
  with the E013 catalogue (no C4-free closed taut core below order 10).
- The two fixed anchors are hand-checkable seven- and six-vertex graphs.
