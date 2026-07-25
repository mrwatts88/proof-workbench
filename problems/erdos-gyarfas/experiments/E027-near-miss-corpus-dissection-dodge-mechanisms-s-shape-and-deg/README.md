# E027 — near-miss corpus dissection: dodge mechanisms, S-shape, and degree-2 geometry against the eight profile objects

- Date: 2026-07-25
- Problem: `P-002`
- Evidence class: **computational dissection of recorded data** (the `E026`
  corpus, re-verified per row on a deterministic stride) plus **new
  member-level structure computation** — the mechanism-extraction step of the
  profile-consuming interpolation attempt (`A026` plan step 1, session `S026`)
- Owner: session `S026`. Owned experiment record; writes no ledger.

## Question

The census (`E026`/`C046`) left one viable hypothesis set for the (F-S)
interpolation lemma: the exactly-two profile. Pre-registered questions, fixed
in `dissect.py`'s docstring before production:

- **Q1 (S-shape).** A pair dodges poison \(p\) by DISTANCE (\(\min S>p\)),
  SHORT (\(\max S<p\)), or INTERIOR (\(\min S<p<\max S\), \(p\notin S\)).
  Which mechanisms carry the 9,061 stored dodges? Is the upper-interval
  property (no gaps \(\ge7\) inside \([\min S,\max S]\)) class-wide?
- **Q2 (range).** Distributions of \(\min S\) (asserted \(=d(a,b)\)),
  \(\max S\) vs \(n-1\), sandwich flags at the misses.
- **Q3 (subdivision frame).** A near-miss member is a partial subdivision of
  a smaller two-terminal graph \(H^*\) (suppress non-terminal degree-2
  vertices; corridors become weighted edges); the profile is exactly the
  subdivision-free stratum \(H=H^*\). Where do corridors sit, and does
  \(H^*\) escape the class constraint (carry a \(C_4\)/\(C_8\))?
- **Q4 (odd-adjustment supply).** Do dodge members lack the short odd cycles
  (\(C_3\)/\(C_5\)) that power \(\pm1\) length adjustments?
- **CONTROL.** A deterministic stride sample of ordinary class members at
  18–20 with full path enumeration on every degree-2 pair: the base rates of
  gaps, Hamiltonian pairs, and the `L035` parity law.
- **EXCHANGE (added after Q1–Q4 read; pre-registered before it ran).** The
  first-order chord-exchange calculus on a Hamiltonian \(a\)–\(b\) path:
  rerouting along pairwise interior-disjoint chords realizes length
  \(M-\sum(\sigma_k-1)\) (every generated length is a real path —
  soundness by construction). Does it reproduce the profile objects'
  saturation, and does it respect the dodgers' holes?

## Logical scope

Everything is per the censused classes (`E026` coverage verbatim: 10–19
complete, order 20 the 11/16-part sample + supp14). The corpus rows are the
stored taut gapped pairs — a *selected* set; control rows are the stride
sample. No claim about orders 21+, the uncensused order-20 parts, or any
graph outside the class files. The exchange test is a lower-bound
demonstration on one deterministic Hamiltonian path per object; savings sets
are path-dependent, so "missed" lengths bound the first-order calculus, not
\(S\).

## Environment

- Imports (read-only): `E026/census.py` by its own pattern — the whole
  `E019`/`E021`/`E018` chain loads through it; `E026/data` listed before and
  after the import and asserted unchanged; all output paths rebound to
  `E027/data`. Primitives used: `g6_decode`, `degrees`, `bipartition`,
  `bfs_dist`, `has_cycle_len`, `paths_with_essential`, `has_path_len`,
  `petersen_minus_e`, class-file access.
- New code (this experiment): the S-shape classifiers, chain/corridor
  decomposition, the smoothing construction \(H\mapsto H^*\), triangle
  counter, the Hamiltonian-path DFS, the disjoint-chord savings DP, tallies.
- CPython 3.14.2 and PyPy 7.3.23 (3.11.15); anchors under both; production
  under PyPy at `nice -n 15`, single process (`E024` held 8 cores at nice 0
  throughout and was never touched).
- Stdlib only; deterministic (fixed strides, no randomness; wall clock in
  timing fields only).

## Inputs and search space

- Corpus: `E026/data/census_summary.json` `taut_gapped_pairs` (9,061 rows,
  asserted; per-order 8/8/371/24/2,727/167/5,756 at 12–20) and the eight
  exactly-two profile rows from the per-part files + supp14.
- Control strides (members): 600/400/3000 at orders 18/19/20 over the class
  files in part order → 180/186/190 members, 14,098 full enumerations.
- Per corpus row asserted: stored flags consistent; \(\min S=d(a,b)\) by
  BFS; member non-bipartite and both parities in \(S\) (`L035` soundness
  alarm); every 250th row's full \(S\) recomputed by `paths_with_essential`
  (37 rechecks; run-to-run identical).

## Reproduction

```sh
python3 dissect.py anchors   # 35 checks, CPython
pypy3   dissect.py anchors   # 35 checks, PyPy
nice -n 15 pypy3 dissect.py corpus     # Q1-Q4 + frontier (0.8 s)
nice -n 15 pypy3 dissect.py control    # stride control (0.7 s)
nice -n 15 pypy3 dissect.py exchange   # the chord-exchange test
nice -n 15 pypy3 dissect.py report     # contrast tables
```

Outputs in `data/`: `anchors_dissect_{cpython,pypy}.json`,
`corpus_dissection.json`, `corpus_rows_compact.json`, `control_sample.json`,
`exchange_test.json`.

## Anchors — 35 checks, both interpreters

Classifier micro-tests on synthetic \(S\)-sets (a1); Petersen\(-e\) built by
edge list — \(S=\{4,5,7,8\}\) recomputed, taut, classified interior-6 +
short-14, subdivision-free, triangle-free, keeps its \(C_8\)s after
smoothing (a2); the order-14 exemplar from its recorded g6 — \(S=[3,13]
\setminus\{6\}\) found on a taut degree-2 pair, Hamiltonian, no gap \(\ge7\)
(a3); chain decomposition on a hand hexagon-plus-chord (a4); the smoothing
construction on a once-subdivided \(K_4\) — weights, edge-total identity,
simple-part \(C_4\) (a5); triangle counter on \(K_4\)/Petersen\(-e\)/the
hexagon (a6); corpus and profile loading identities incl. the order-19
profile member's recorded g6 and \(S=[5,18]\), plus a full re-verification
of corpus row 0 (a7).

## Results

### Q1/Q2 — the dodge taxonomy (three rigid shapes)

| order | rows | 6-dodge dist/int | 14-dodge short/int | gap\(\ge7\) rows | Ham rows |
|---|---|---|---|---|---|
| 12 | 8 | 0/8 | 8/0 | 0 | 0 |
| 14 | 8 | 0/8 | 8/0 | 0 | 0 |
| 16 | 371 | 0/371 | 371/0 | 221 | 0 |
| 17 | 24 | 0/24 | 24/0 | 0 | 0 |
| 18 | 2,727 | 124/2,603 | 2,691/36 | 1,184 | 36 |
| 19 | 167 | 3/164 | 167/0 | 0 | 0 |
| 20 | 5,756 | 1,099/4,657 | 5,337/419 | 2,394 | 0 |

(6-dodge "short" never occurs; 14-dodge "distance" never occurs.)

- **Shape A (short + 6-hole), 7,380 rows**: \(\max S\le13\), a hole at 6 in
  an otherwise even-rich set (top even-part patterns \([4,8,10,12]\):
  3,394; \([2,8,10,12]\): 1,204; …).
- **Shape A′ (distance), 1,226 rows**: \(\min S=7\) **exactly** — never
  \(\ge8\) — with \(\max S\le13\).
- **Shape B (long-range, mod-4), 455 rows**: \(\max S\ge15\), holes only at
  \(\{6,10,14\}\) (+ odd-part gaps at 7 in 146): pooled gaps \(\ge7\) are
  {7: 146, 10: 395, 11: 48, 14: 455} — never 8, 9, 12, 13. 395 of the 419
  order-20 rows have even part exactly \(\{4,8,12,16\}\): **the even part
  avoids \(2\bmod4\)** — an in-window realization of the `L034`
  channel-(iii) pattern on non-bipartite members (odd lengths present
  throughout; `L035` parity law asserted on all 9,061 rows, zero
  violations).
- **The 14-dodge is overwhelmingly SHORT**: \(\max S\le13\) on 8,606 of
  9,061 rows; the minimal full dodges have \(\max S=13\) **exactly** at
  every order 16–20 (the shortness dodge parks one below the poison).

### The full-dodge frontier (2, 6, 14 all absent — the residual-relevant rows)

6,934 rows. Minimum ndeg2 per order: 5/7/5/6/**5**/6/**4** at
12/14/16/17/18/19/20. The single order-20 ndeg2-4 full dodge is an
**adjacent-terminals** pair (\(S=\{1\}\cup[8,13]\)); the non-adjacent
frontier is ndeg2 = 5. Shape B needs ndeg2 \(\ge7\) everywhere. The six
order-20 ndeg2-4 gapped rows (incl. that full dodge) sit on members whose
**other five degree-2 pairs are all saturated** (\(S=[4..6,19]\) full
intervals) — **the dodge is pair-local, not member-local**; their members
have full spectra \([3,16{-}18]\setminus\{4,8\}\) and triangles. The
adjacent-terminals dodge reduces recursively: \(S\setminus\{1\} = 2 +
S'(H-a-b;\,a',b')\) for the outward neighbour pair — an off-terminal
distance dodge two vertices down.

### Q3 — the subdivision frame

- Corridors are **short**: pooled corridor weights {2: 47,662, 3: 2,006,
  4: 10} — the dodges use many single subdivisions, never long corridors.
- **8,978 of 9,061 rows (99.1%) smooth to a reduced graph whose simple part
  carries a \(C_4\) or \(C_8\)** — near-misses are subdivisions of
  class-violating graphs. All 83 exceptions are nonsimple (parallel
  corridors, theta-hubs) and all are short-14 rows; **100% of shape-B rows
  have class-violating reductions**.
- The profile objects are subdivision-free by construction (shrink 0,
  asserted), so the class constraint acts on the irreducible graph itself.

### Q4 — odd-cycle supply (mechanism candidate killed)

100% of dodge-carrying members have triangles (C3 counts positive
everywhere; C5/C6/C7 nearly always present). "Dodgers lack odd-cycle
reroute material" is **refuted** — the discriminator is not cycle supply.

### CONTROL — base rates for ordinary taut pairs

| order | members | taut pairs | gap\(\ge7\) | gapped | Hamiltonian |
|---|---|---|---|---|---|
| 18 | 180 | 1,790 | 226 (12.6%) | 4 | 390 (21.8%) |
| 19 | 186 | 2,466 | 412 (16.7%) | 0 | 638 (25.9%) |
| 20 | 190 | 3,525 | 617 (17.5%) | 2 | 1,007 (28.6%) |

Gap positions concentrate at 7–9 and nearly vanish by 13–14 (13: 9 rows;
14: 2 rows; of 7,781 taut pairs). So: the upper-interval property is **not**
class-wide (12–17% violation), but holes at \(\ge13\) are rare
(\(\sim\)0.1%); saturation anchors at the top. The profile-8's joint
property (gap-free **and** Hamiltonian) has control base rate \(\approx\)
0.2–0.25 per pair — eight-for-eight is far outside the base rates
(\(\sim0.22^8\approx5\times10^{-6}\) under independence; a heuristic
contrast, not a test statistic).

### EXCHANGE — the first-order chord calculus validates

On each profile object, one Hamiltonian \(a\)–\(b\) path was found (DFS,
deterministic) and the disjoint-chord savings DP run:

- **Span law confirmed**: no span-3 and no span-7 chord exists on any of
  the eight objects (asserted — chord + path arc would be a \(C_4\)/
  \(C_8\)); observed spans \(\{2,4,5,6,9,12,13,14,17\}\).
- **Coverage**: the calculus generates 11–15 of the 14–17 lengths of
  \([\min S, n-1]\); **every miss lies in \([4,9]\)** — the top of \(S\)
  down to 10 is completely generated on all eight objects, in particular
  **14 is generated on all eight**. One object is fully generated.
- **Soundness**: every generated length is asserted \(\in S\) (they are
  real paths), on the profile objects and on all 36 Hamiltonian corpus
  rows.
- **The dodgers' chord geometry explains their holes**: the 36 Hamiltonian
  dodge rows (order 18, shape B) carry exactly two span-2 chords and
  otherwise spans \(\equiv1,2\pmod4\) (span multisets
  \([2,2,5,6,9,10,10{-}11,13,14]\)); their savings generators
  \(\sigma-1\in\{1,4,5,8,9,10,12,13\}\) never disjointly sum to
  \(\equiv3\pmod4\) — exactly the residue class of savings that would hit
  lengths \(\{14,10,6\}\) from \(M=17\). The calculus fills no interval on
  any dodger (0 of 36).

## Interpretation

Narrowest justified conclusions; everything per censused class only.

1. **The lemma must be pair-local and profile-consuming.** Members carrying
   a dodge pair simultaneously carry fully saturated pairs, full spectra,
   and triangles — no member-level hypothesis separates dodgers from the
   profile. What separates them is where the *pair's* corridors sit:
   ndeg2 = 4 members realize the dodge at order 20 (adjacent variant; 5
   non-adjacent), so the profile hypothesis is load-bearing by a margin of
   **two subdivision vertices** at the frontier.
2. **The dodge economy has exactly three shapes** (A: short + 6-hole; A′:
   distance-7; B: long-range mod-4 even part), all rigid: \(\max S=13\)
   walls, \(\min S=7\) walls, even part \(\subseteq4\mathbb Z\). Any (F-S)
   proof must kill A/A′ (short-range exclusion: profile + window
   \(\Rightarrow\max S\ge14\), or \(6\in S\) when short) and B (long-range
   poison forcing: \(\max S\ge14\Rightarrow14\in S\) or \(6\in S\)).
3. **The subdivision frame is the mechanism**: dodges ride on corridors
   whose internal vertices evade the third-edge requirement; 99.1% of
   dodge rows reduce to class-violating graphs. On the profile the
   {C4,C8}-exclusion binds the irreducible graph — visibly as the **span
   law** (no chord of span 3 or 7 on a Hamiltonian path) and its pair
   analogues.
4. **The chord-exchange calculus is the right formal engine for the
   long-range half**: first-order disjoint-chord surgery on a single
   Hamiltonian path already reproduces the entire top-of-\(S\) saturation
   (everything \(\ge10\), including both poisons' window images) on all
   eight profile objects, and its span arithmetic exactly captures how
   shape B dodges. The missing tool sharpens from "a lower-bound theory
   for through-path length sets" (`A025` T4) to: **the span/savings
   combinatorics of chord systems of longest paths under
   \(C_4/C_8\)-exclusion** (plus a separate short-range exclusion for
   shape A, where the ear structure over a \(\le13\)-position longest path
   with all-branching internal vertices is the object).
5. Caveats: the corpus is a selected set (gapped rows only); order-20 rows
   sample 11/16 parts; the exchange test is one path per object; the
   short-range half has **no** mechanism yet beyond the forced-structure
   observations; nothing here bears on orders 21+ or on whether (F-S) is
   true — the frontier trend (dodge at ndeg2 4 by order 20) is consistent
   with (F-S) failing at some higher order, which `E024`+census will test.

## Independent checks

- Anchors under both interpreters (35 checks each), including named-object
  ties to three prior experiments' recorded values.
- Every corpus row's stored fields re-validated structurally; min \(S\) =
  BFS distance on all 9,061 rows; every 250th row fully re-enumerated by
  the independent `E018` enumerator (37 rows, identical).
- The `L035` parity law asserted on all corpus rows and all control taut
  pairs (zero violations — a soundness alarm that never fired).
- Exchange soundness: every calculus-generated length asserted present in
  the recorded \(S\) (8 profile objects + 36 dodgers).
- The smoothing construction verified by edge-count identity per row and
  by the once-subdivided-\(K_4\) hand anchor.
- Not independently re-derived: the class files and the `E026` census
  layer (inherited at recorded strength with their caveats).
