# E010 — Atom search: two-terminal power-free gadgets at small orders

Runs the decisive failure-first test of attempt `A011`: an exhaustive search
for **atoms**, the finite objects whose existence would disprove statement
0.1 via ring/doubling assemblies (`A011` R3/R4, promoted as `L025`).

- **1-atom**: connected, power-free, exactly one vertex of degree < 3 (degree
  1 or 2), all other degrees ≥ 3. One 1-atom of order \(n\) yields a
  counterexample of order \(2n\) (degree-2 case, edge-doubling) or \(3n\)
  (degree-1 case, triangle assembly).
- **2-atom**: connected, power-free, exactly two sub-cubic vertices \(a,b\)
  (each degree ≥ 1, degree sum ≥ 3), all others ≥ 3, and all simple
  \(a\)–\(b\) path lengths inside a window of multiplicative ratio < 2
  (\(s_{\max}<2s_{\min}\)). One 2-atom yields counterexamples of unbounded
  order (rings placed in a dyadic gap).

## Class searched and coverage

For each order \(n\): connected graphs, minimum degree ≥ 1, at most two
vertices of degree < 3, no \(C_4\), no \(C_8\) (no \(C_{16}\) either once
\(n\ge16\)). Coverage argument (`A011`): an atom with both terminals of
degree ≥ 3 would be a minimum-degree-3 power-free graph, excluded through
order 18 by `L022`/`C023`; an atom with one sub-cubic vertex is a 1-atom;
hence this class contains every atom on \(\le n\) vertices.

Generation: `geng -c -f -d1 n mine:0` with the valid edge lower bound
`mine` \(=\lceil(3n-4)/2\rceil\) implied by the degree profile. Downstream of
geng everything is re-verified: degrees from the decoded adjacency, \(C_4\)
by the independent codegree test, \(C_8\)/\(C_{16}\) by the `E004` detector
(anchored there and in `E005`/`E006`). Path-length sets by DFS over simple
paths with a BFS shortest-distance cross-check.

## Anchors (all 12 checks pass; `python3 atoms.py anchors`)

- A1: geng connected cubic counts at \(n=8,10,12\) equal OEIS A002851
  (5, 19, 85).
- A2: the pipeline restricted to zero sub-cubic vertices at \(n=14\)
  reproduces the recorded `C016` class size (6059 connected \(C_4\)-free
  minimum-degree-3 graphs) with zero \(\{C_4,C_8\}\)-free survivors,
  matching the `L017`/`L018` frontier.
- A3: \(K_{3,3}-e\) reports \(S=\{3,5\}\) (ratio \(5/3<2\)) and spectrum
  \(\{4,6\}\) — the Bondy–Vince gadget, a 2-atom in every respect except
  its \(C_4\).
- A4: the \(L=3\) ring of \(K_{3,3}-e\) has spectrum exactly
  \(\{4,6,9,11,13,15\}\) — the published spectrum of Bondy–Vince's
  Figure 1 (`C024`), an external anchor for both the ring builder and the
  spectrum detector.
- A5: Petersen spectrum \(\{5,6,8,9\}\) and an edge-deletion distance probe
  for the path machinery.

## Results

| n | geng stream (C4-free, min deg ≥ 1, edge bound) | ≤ 2 sub-cubic | power-free members | atoms |
|---|---|---|---|---|
| 6 | 4 | 0 | 0 | 0 |
| 7 | 5 | 0 | 0 | 0 |
| 8 | 36 | 1 | 0 | 0 |
| 9 | 84 | 4 | 0 | 0 |
| 10 | 918 | 39 | 0 | 0 |
| 11 | 4,058 | 262 | 0 | 0 |
| 12 | 52,331 | 2,256 | 0 | 0 |
| 13 | 389,734 | 21,197 | 0 | 0 |
| 14 | 5,605,161 | 248,106 | 0 | 0 |
| 15 | 61,813,970 | 3,470,555 | 0 | 0 |

**Every order through 15 is empty: not a single connected
\(\{C_4,C_8\}\)-free graph with at most two sub-cubic vertices exists, of
any kind — so no 1-atom, no 2-atom, and (a fortiori) no 2-atom candidate
even at ratio ≥ 2.** The "power-free members" column counts every graph
reaching the power-freeness filter, including kinds that would not be atoms
(`excluded-(1,1)`, ratio ≥ 2 candidates); all are zero.

Logical scope: exact exclusion for orders \(\le15\) only; it is a finite
exclusion for the assembly constructions of `L025` (1-atom doublings need
gadget order ≥ 16, hence counterexample order ≥ 32; rings need gadget order
≥ 16), not evidence about the universal statement. Orders 6–14 ran under
CPython 3.14.2; order 15 under PyPy 7.3.23 (anchors re-passed under PyPy
before the run).

## Calibration profile (subcommand `profile`)

Same stream, graphs with exactly two sub-cubic vertices, power-freeness NOT
required — how common is pinched through-spread when only \(C_4\) is
forbidden?

| n | examined | ratio < 2 | of those, C8-free | min ratio |
|---|---|---|---|---|
| 12 | 1,690 | 22 | 0 | 1.0 |
| 13 | 16,106 | 116 | 0 | 1.0 |

Ratio < 2 — including perfect rigidity, a single through-length
(bridge-joined blob pairs, \(S=\{1\}\)) and near-misses like \(S=\{2,3\}\)
and the interval \(S=\{6,\dots,11\}\) (ratio 1.83) — is geometrically
common. Every such graph contains a \(C_8\) (at these orders that also
follows from the main table: the power-free class is empty outright). The
decision-relevant reading: **path geometry does not force spread doubling
on its own; power-freeness is the binding constraint** — supporting the
spread-doubling lemma target R5(b) of `A011` as a real phenomenon rather
than an artifact of the search class.

## Reproduction

```
python3 atoms.py anchors
python3 atoms.py run 6 7 8 9 10 11 12 13 14
pypy3 atoms.py run 15
python3 atoms.py profile 12 13
python3 atoms.py ring <graph6> <a> <b> <L>   # assemble/verify a ring
```

Outputs land in `data/atoms_n{n}.json` (geng command line, stream and class
counts, and every power-free finding verbatim). geng is nauty 2.9.3
(`/opt/homebrew/bin/geng`), the same anchored binary as `E006`.
