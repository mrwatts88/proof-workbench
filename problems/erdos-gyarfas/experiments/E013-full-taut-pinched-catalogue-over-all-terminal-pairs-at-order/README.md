# E013 — Full taut-pinched catalogue over all terminal pairs at orders 6–14, closed-ratio core catalogue, and the block dissection

- Date: 2026-07-24 (orders 6–14, S014; order-15 extension in S015; an
  order-16 closed scan was launched in S015 and its harvest is recorded
  in the follow-up session's addendum below when present)
- Problem: `P-002`
- Evidence class: exhaustive finite catalogue (strict and closed ratio) plus
  instance verification of the `A014` reduction theory and the \(C_8\)
  interference census

## Question

1. **Strict catalogue.** Which taut pinched pairs exist at orders 6–14?
   For every graph of the `E010` geng stream (connected, \(C_4\)-free, min
   degree \(\ge1\), \(\ge\lceil(3n-4)/2\rceil\) edges — hence at most two
   sub-cubic vertices) and every admissible terminal pair (containing all
   sub-cubic vertices, degree sum \(\ge3\)), is the pair vertex-taut with all
   through-path lengths in \([d,2d-1]\), \(d=d(a,b)\)? Unlike `E012` (which
   certified only \(S\subseteq\{3,4,5\}\)), no band is excluded: this is the
   first search able to see the taut \(s_{\min}\in\{4,5\}\) rung targets
   (\(s_{\max}\in\{6,7\}\) or \(\{8,9\}\)), which `C029` did **not** cover.
2. **Closed catalogue.** The same with the ratio relaxed to
   \(s_{\max}\le2d\) (excess \(e\le0\)): by the pendant reduction (`A014`
   T1/T2) this is the **core catalogue** from which every strict-pinched
   taut (D)-gadget arises as a pendant lift.
3. **Dissection.** For every strict witness and every 2-connected core:
   cycle census, \(C_8\) inventory (terminal avoidance, layer spans,
   coverage), through-path system, essential edges, the interference census
   (which \(C_8\)s are two-path symmetric differences), cut vertices,
   pairwise isomorphism, core extraction, lift completeness.

## Logical scope

Coverage is exhaustive for the stated class at orders \(6\)–\(14\): a
(D)-gadget with at most two sub-cubic vertices of order \(n\) lies in the
geng stream (edge bound from the degree sum \(\ge3(n-2)+3\ge3n-4\) — for
cores \(\ge3n-2\)), and every admissible pair of every stream graph is
scanned. The two per-pair filters are proved necessary conditions of the
taut target (eccentricity: a vertex on a path of length \(\le L\) has
\(d(a,v)+d(v,b)\le L\); the DFS abort proves a too-long path exists via a
masked reachability certificate), so no taut hit is lost; **non-taut pinched
pairs are not fully counted** (the eccentricity filter may reject them) and
the non-taut tallies are partial by design. The catalogue can refute but not
prove the universal theorems (`L028`/`L030` instance-checked); the `A014`
reduction theorems rest on hand proofs, with every instance here verified.
Order 15+ is not covered.

## Environment

- CPython 3.14.2; geng and labelg from nauty 2.9.3 (`/opt/homebrew/bin`),
  geng invoked exactly as in `E010`/`E011`/`E012`
  (`geng -q -c -f -d1 n mine:0`, `mine`\(=\lceil(3n-4)/2\rceil\)).
- Standard library only. Graph primitives (graph6 decoder, degree/C4
  detectors, BFS) copied verbatim from `E012/scan_pairs.py` (anchored there
  bidirectionally against the independent `E010` pipeline). New machinery:
  banded all-simple-paths DFS with masked-reachability abort, exact simple
  cycle enumerator, two-terminal isomorphism by profile-pruned backtracking
  (cross-anchored against nauty `labelg` canonical forms), cut-vertex
  finder, pendant lift/reduction builders.
- Integer bitmask arithmetic throughout; no randomness.

## Inputs and search space

The `E010` stream at orders 6–14 (totals asserted against `C027`: 4; 5; 36;
84; 918; 4,058; 52,331; 389,734; 5,605,161). Per graph: admissible pairs as
in `E012`. Per pair: eccentricity prefilter at ceiling \(2d-1\) (strict) or
\(2d\) (closed), then the exact banded DFS (abort limit ceiling\(+1\)) with
masked-reachability pruning; tautness read off the essential-vertex mask on
completion. Fixed anchors: \(K_{3,3}-e\), K4, C6, Petersen, P4, a pendant
triangle, the five `E011` witnesses, and the A9 bridge composite.

## Reproduction

```sh
python3 catalogue.py anchors      # 88 checks
python3 catalogue.py run 6 7 8 9 10 11 12 13 14
python3 catalogue.py runclosed 6 7 8 9 10 11 12 13 14
python3 catalogue.py cores
python3 catalogue.py dissect
```

Outputs land in `data/catalogue_n{n}.json`, `data/catalogue_closed_n{n}.json`,
`data/cores.json`, `data/dissect.json`. Runtimes: \(\le11\)s per order
through 13; 167.6s (strict) and 160.4s (closed) at order 14.

## Results

Anchors: all 88 pass — positive controls (\(K_{3,3}-e\) caught taut band-3
\(\{3,5\}\); the five `E011` witnesses caught with recorded \(S\) and
spectra), cycle-census controls (K4, C6, Petersen: spectrum \(\{5,6,8,9\}\),
12 pentagons, 10 hexagons), isomorphism controls including ordered-terminal
orientation cases, and the bridge composite (A9: two Petersen\(-e\) blocks
+ bridge = strict taut core, order 20, band 9, \(S=\{9,\dots,17\}\),
spectrum \(\{5,6,8,9\}\), cuts = the bridge ends).

**Strict catalogue (ratio \(<2\)).** Exactly **six** taut pinched pairs
exist at orders \(\le14\), none at order 14:

| n | eligible graphs | pairs | taut hits | bands |
|---|---|---|---|---|
| 6–10 | 43 | 310 | 0 | — |
| 11 | 256 | 1,300 | 1 | 5 |
| 12 | 2,143 | 9,808 | 3 | 6 |
| 13 | 20,432 | 101,216 | 2 | 6 |
| 14 | 241,135 | 1,357,597 | 0 | — |

The order-12/13 hits at sub-cubic pairs are exactly the five `C028`
witnesses (asserted). The order-11 hit is new: terminal degrees \((1,2)\),
\(S=\{5,6,8,9\}\), spectrum \(\{5,6,8,9\}\) — the pendant lift of
Petersen\(-e\). **The strict \(s_{\min}=4\) rung target
(\(S\subseteq\{4,\dots,7\}\)) is empty through order 14 over all terminal
pairs** — the first genuine coverage of that rung. Zero non-taut
completions occurred at any order. Every taut hit contains a \(C_8\)
(consistent with `C027`).

**Closed catalogue (\(e\le0\)).** Strict subsets agree with the strict runs
at every order (asserted). Closed taut hits: n=9: 1; n=10: 1; n=11: 17;
n=12: 6; n=13: 22; n=14: 7 — every one at exact excess \(e=0\) except the
six strict lifts above. All are pendant-type (a degree-1 terminal; types
\((1,2)\)/\((1,3)\)) except **five (2,2)-terminal 2-connected cores — the
blocks**:

| block | order | band | \(S\) | spectrum | \(C_8\)s | swap-aut | witnesses (lifts) |
|---|---|---|---|---|---|---|---|
| P10 = Petersen\(-e\) | 10 | 4 | \(\{4,5,7,8\}\) | \(\{5,6,8,9\}\) | 7 | yes | 1 (order 11) |
| A11 | 11 | 5 | \(\{5,\dots,10\}\) | \(\{3,5,\dots,11\}\) | 3 | no | 2 (order 12) |
| B11 | 11 | 5 | \(\{5,\dots,10\}\) | \(\{3,5,\dots,11\}\) | 3 | yes | 1 (order 12) |
| C12 | 12 | 5 | \(\{5,\dots,10\}\) | \(\{3,5,\dots,11\}\) | 5 | no | 2 (order 13) |
| D14 | 14 | 6 | \(\{6,\dots,12\}\) | \(\{3,5,\dots,13\}\) | 5 | yes | (order 15, predicted 1) |

Canonical graph6 strings in `data/cores.json` (labelg form) and
`data/catalogue_closed_n14.json` (D14: `M?AA@AOqAcB_HOIG?`, terminals
(6,7)). **No strict block exists through order 14; every block sits at
exact equality \(s_{\max}=2\,s_{\min}\).**

**Cores/lifts.** The six strict witnesses are exactly the distinct pendant
lifts of P10, A11, B11, C12 (bijection machine-verified; the asymmetric
A11/C12 give two non-isomorphic lifts each, the swap-symmetric P10/B11 one
each; deduplication cross-checked against `labelg`: 4 distinct canonical
forms; P10 confirmed isomorphic to Petersen minus an edge; its
\(S=\{4,5,7,8\}\) is Petersen's cycle-through-edge spectrum shifted by
\(-1\), its 7 \(C_8\)s are Petersen's 15 minus the 8 through the deleted
edge).

**Interference census.** In every witness and every block, **every \(C_8\)
is the symmetric difference of two through-paths** (23/23 across the seven
distinct graphs dissected: 3+3+3+5+5 witness-level, 7 P10, 5 D14). Every
block has \(\ge1\) pair of internally disjoint shortest through-paths; at
band 4 (P10) two disjoint 4-paths form a \(C_8\) directly
(\(4+4-2\cdot0\)); at bands 5–6 disjoint shortest pairs give
\(C_{10}/C_{12}\) and the \(C_8\)s come from overlapping pairs. No graph in
the catalogue has an inessential edge.

## Interpretation

- The `C029`-era summary "\(s_{\min}\in\{4,5\}\) empty through 14" is now
  actually established — it previously rested on a scan that aborted on any
  length-6 path and could not see those rung targets. The strict rung
  boundary is corrected and complete through order 14: rungs
  \(s_{\min}\le4\) empty, five witnesses at \(s_{\min}\in\{5,6\}\), all
  pendant lifts.
- The strict taut world at small orders is entirely pendant-derived: the
  disproof interface concentrates on 2-connected cores with \(e\le0\)
  (`A014` T4), empirically all at \(e=0\), each blocked from power-freeness
  only by \(C_8\), each \(C_8\) a two-path interference.
- Claim-ledger updates: `C030` (strict catalogue), `C031` (closed
  catalogue, blocks, dissection); instance support for `L031`/`L032`.

## Independent checks

Stream totals asserted against `C027` at every order; the strict scan
re-found the five `C028` witnesses at their recorded pairs; strict/closed
subset consistency asserted at every order; the isomorphism engine is
cross-anchored against nauty `labelg` on the six extracted cores (4
distinct, matching the labelg canonical-form count); the graph primitives
were anchored in `E011`/`E012` against the independent `E010` pipeline; the
DFS/BFS minimum-length assert ran on every completed pair; the
bridge-composite anchor A9 checks the reduction theory's sharpness example
end to end.

## S015 extension — order 15 (ledger row `C032`)

Environment: PyPy 7.3.23 (Python 3.11.15); the 88 anchors re-passed under
PyPy before the runs (and re-passed under both PyPy and CPython 3.14.2
after the script change noted below). Same geng invocation as above.

```sh
pypy3 catalogue.py run 15        # 315.4s
pypy3 catalogue.py runclosed 15  # 302.5s
pypy3 catalogue.py cores
pypy3 catalogue.py dissect
```

Results (`data/catalogue_n15.json`, `data/catalogue_closed_n15.json`,
regenerated `data/cores.json` / `data/dissect.json`):

- Stream total 61,813,970 (asserted against `C027`); 3,384,284 eligible
  graphs; 22,022,137 admissible pairs per mode.
- **Strict:** exactly one taut pinched pair at order 15 — band 7,
  \(S=\{7,\dots,13\}\), terminal degrees (1,2), graph6
  `N??CA?oID@P_@cPOHO?`, pair (3,7). Its pendant reduction is a
  (2,2)-core of order 14 verified **terminal-respecting-isomorphic to
  D14** two ways: by the `cores` lift machinery (seventh witness joins
  the bijection; five distinct cores; D14 swap-symmetric with a single
  lift) and by a direct `isomorphic_two_terminal` check against the
  recorded closed-14 hit (`M?AA@AOqAcB_HOIG?`, terminals (6,7)). This
  confirms `C031`'s prediction of exactly one strict band-7 witness at
  order 15. Zero non-taut completions; every hit contains a \(C_8\).
- **Closed:** 20 taut hits — 19 at band 7 (18 at boundary
  \(s_{\max}=14\), plus the strict lift) and one at band 4
  (\(S=\{4,\dots,8\}\), terminal degrees (1,4), boundary). **All 20 are
  pendant-type** (a degree-1 terminal): no new (2,2)-core, so the block
  catalogue is unchanged through order 15 — five equality blocks, no
  strict block. Closed hits at orders \(\le15\) occupy bands 4–7 only;
  no closed hit at any band \(\le3\) exists.
- Boundary pendant hits reduce to excess-\(+1\) cores
  (\(e(H)=e(\mathrm{core})-1\)), so they are not block-question
  objects; the band-4 closed world through 15 is exactly three objects
  (pendant pairs at orders 9 and 15, and Petersen\(-e\), the only
  core, disjoint-type).
- Interference census extends: every \(C_8\) in every witness and every
  core remains a two-through-path symmetric difference.

Script change for the extension: the `cores` command's two hardcoded
expectations were updated from the S014 values (six witnesses,
`set(range(6))`) to seven; nothing else changed, and all 88 anchors
re-pass under both interpreters after the edit.

An order-16 closed scan (`runclosed 16`; no `C027` reference total
exists at 16, so the stream total will itself be new data) was launched
in S015 and left running at session close; its harvest — including the
strict/closed derivation via the boundary flag and any block/dissection
updates — is deliberately excluded from `C032` and will be recorded by
a short dedicated follow-up session.
