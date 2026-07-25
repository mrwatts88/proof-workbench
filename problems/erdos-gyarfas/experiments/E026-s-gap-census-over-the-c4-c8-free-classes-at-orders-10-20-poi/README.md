# E026 — the S-gap census over the \(\{C_4,C_8\}\)-free classes at orders 10–20

- Date: 2026-07-25
- Problem: `P-002`
- Evidence class: **computational census, exhaustive over the stated on-disk
  classes** (complete at orders 10–19; a recorded per-part-complete sample at
  order 20) — the first kill test of (F-S) and the gap-vs-order measurement of
  the saturation mechanism (`A025` T5, session `S025`)
- Owner: session `S025`. Owned experiment record; writes no ledger.

## Question

(F-S) (`A025` T4) claims: in the window \([18,35]\), every vertex-taut
(5b)-profile pair \((H,a,b)\) with \(4,8\notin\mathrm{Spec}(H)\) has
\(S\cap\{6,14\}\ne\emptyset\). Pre-registered outcomes (`A025` T5):

- **(i)** no vertex-taut member of the on-disk 18–20 classes escapes both
  poison lengths ⟹ (F-S) survives its first kill test where the residual
  object lives, and the gap-vs-order curve against orders 10–16 measures the
  saturation mechanism;
- **(ii)** a vertex-taut escapee **with the exactly-two profile** kills (F-S)
  as stated and becomes calibration object #3;
- **(iii)** the same scan re-reads the class's \(C_{16}\) status for (F-T).

**Design refinement (recorded in `S025`).** The exactly-two stratum of the
on-disk 18–20 classes is fully known (the eight profile objects, all
\(S\ni6,14\)), so a member-only census would be vacuous. The census therefore
quantifies over **every unordered pair of degree-2 vertices** of every class
member: the exactly-two stratum is (F-S)'s hypothesis class proper, and the
wider pair census is the mechanism measurement the redirect asked for — any
vertex-taut gapped pair shows exactly which hypotheses fail to force the
poisons.

## Definitions

For a member \(H\) with degree-2 vertices \(D_2\), \(|D_2|=\) `ndeg2`, and a
pair \(\{a,b\}\subseteq D_2\): \(S=S(H,a,b)\) is the set of simple \(a\)–\(b\)
path lengths; the recorded bits are \(2\in S\), \(6\in S\), \(14\in S\). A pair
is **gapped** when \(6\notin S\) and \(14\notin S\) (the poison escape;
\(30>n-1\) cannot occur at these orders). A gapped pair with also
\(2\notin S\) is a **full \(\mathbb P-2\) dodge** (the closure \(B=H+u\) is
then power-cycle-free through \(u\), by \(\mathrm{Spec}(B)\supseteq S+2\)).
Tautness: every vertex of \(H\) lies on some simple \(a\)–\(b\) path (the
essential mask of the `E018` enumerator covers \(V\)).

## Sources (all pre-existing, read-only)

| orders | files | members |
|---|---|---|
| 10–16 | `E019/data/class_n{10..16}.txt` | 14, 0, 94, 10, 778, 168, 7,615 |
| 17 | `E019/data/class_n17_part{0..15}of16.txt` | 2,580 |
| 18–19 | `E022/data/class_n1[89]_part{0..15}of16.txt` | 108,447 / 74,589 |
| 20 | `E022/data/class_n20_part{r}of16.txt`, \(r\in\{0,1,2,4,5,8,9,10,11,12,15\}\) | **572,519** |
| 20 supp | `E022/data/profile_n20_part14.g6` (the four recorded part-14 profile members) | 4 |

**Order-20 coverage caveat.** Only the 11 parts that stayed under `scan.py`'s
`SAVE_LIMIT` have class files; parts 3/6/7/13/14 (1,996,962 graphs of the
2,569,481-graph class) are **not censused** apart from the four recorded
part-14 profile members (the `supp14` stratum, kept out of the class tallies).
Order-20 rows are a per-part-complete **sample**, never a class total.
**Correction recorded here:** the `S022` caveat's figure "572,530 saved" was a
line count including the 11 class-file headers; the authoritative
`scan_n20_part*of16.json` tallies sum to **572,519** over the on-disk parts
(anchor c15c) and to 2,569,481 over all 16 (c15d).

## Environment

- Instruments imported, not rebuilt: `E019/scan.py` by `E022`'s `load_scan`
  pattern (`DATA` rebound here; `E019/data` listed before/after the import and
  asserted unchanged; generator binaries untouched and **never invoked** — the
  census only reads recorded class files) and `E021/dissect.py` (→ `E018
  scan.py`/`mod4.py`, `E013 catalogue.py`) by `E025`'s pattern, for
  `paths_with_essential`.
- New code (this experiment only): the exact-length existence DFS
  (`has_path_len`: iterative, over simple paths, admissible pruning by
  full-graph BFS distance from \(b\) — a partial path of length \(k\) at \(v\)
  cannot finish in exactly \(L\) edges if \(k+\mathrm{dist}(v,b)>L\); a parity
  shortcut for bipartite members, which never fired: the censused classes
  contain **zero** bipartite members) and the tallying/harvest layer.
- CPython 3.14.2 and PyPy 7.3.23 (3.11.15); anchors under both; production
  under PyPy.
- macOS / darwin 25.5.0, arm64, 12 cores. **Contention note
  (`process/concurrency.md`): `E024` (the order-21 rung, launched at `S023`
  close) held 8 cores at nice 0 throughout the whole session.** Production
  here was deliberately throttled to 3 workers at `nice -n 15`
  (`run_census.sh`); all timings are heavy-contention figures, and `E024` was
  never paused, touched, or read beyond its status file.
- Stdlib only; deterministic (no randomness, no wall-clock logic; the stride
  constants are fixed in source).

## Reproduction

```sh
sh   anchors.sh          # E021 45-check suite + 57 new checks, CPython then PyPy
pypy3 census.py census-small                    # orders 10-17
sh   run_census.sh       # orders 18/19/20 (16+16+11 parts, 3 workers), supp14, harvest
pypy3 census.py analyze  # secondary cuts over the taut gapped rows
```

Outputs in `data/`: `anchors_census_{cpython,pypy}.json` + logs,
`census_n{10..17}.json`, `census_n{18,19}_part{r}of16.json`,
`census_n20_part{r}of16.json` (11 parts), `census_n20supp14.json`,
`census_summary.json`, `analysis.json`, `run_census.log`,
`run1_tallies.json`.

Two full production runs were executed: the first stored every gapped row
(540,127 of them, ~350 MB) and was trimmed to taut-only rows for the committed
form; `run1_tallies.json` preserves the first run's complete per-order
tallies, and the second run reproduced **every** tally exactly (see
§Independent checks).

## Anchors — 45 + 57 checks, both interpreters

`anchors.sh` runs, under CPython **and** PyPy, first the `E021` 45-check suite
through the import (the toolchain anchors: the Petersen\(-e\) census values,
the `E013` cores reproduction, the C16/tail/bridge-hung dissection controls,
…) and then 57 new checks:

- **Named calibration objects** (the census must find the recorded dodges):
  Petersen\(-e\) — \(S=\{4,5,7,8\}\), vertex-taut, **gapped** (c1–c3); the
  order-14 exemplar `M?AA@?WcKWHOWOL??` — \(S=[3,13]\setminus\{6\}\),
  vertex-taut, **gapped** (c4–c6).
- **Named frontier objects** (the census must find them saturated): the
  order-19 profile member — \(S=[5,18]\), taut, not gapped (c7–c9); all seven
  recorded order-20 profile members — \(S\), tautness, and \(C_{16}\) count
  each asserted equal to `t5_n20_profile.json` / `collect_n20_part14.json`
  field by field (c10–c11, 28 checks).
- **Exact-length DFS controls**: the \(P_{15}\) end pair (length 14 yes, 6 no)
  and the \(C_{16}\) distance-2 pair (\(S=\{2,14\}\), 6 refused by exhaustion,
  not parity) (c12–c13).
- **Cross-algorithm sweep** (c14): on every degree-2 pair of the full
  order-12/14/15 classes and the first 400 order-16 members, three
  independently written enumerators agree — `E019 path_lengths` = `E018
  paths_with_essential` as full sets, and the new bits equal their membership
  verdicts.
- **Inventory** (c15–c16): every class-file total equals the recorded figure;
  the 18/19/20 totals equal the `scan_*.json` tally sums (572,519 / 2,569,481
  at 20); the supp14 identities equal `collect_n20_part14.json`'s.

## Results

### The census ladder (pre-registered outcome (i) holds; (ii) never fired)

| order | members | pairs | gap6 | gap14 | gap-both | **taut-gapped** | exactly-two members |
|---|---|---|---|---|---|---|---|
| 10 | 14 | 124 | 12 | 124\* | 12 | 0 | 0 |
| 11 | 0 | 0 | — | — | — | — | 0 |
| 12 | 94 | 1,450 | 204 | 1,450\* | 204 | **8** | 0 |
| 13 | 10 | 60 | 0 | 60\* | 0 | 0 | 0 |
| 14 | 778 | 16,008 | 1,984 | 16,008\* | 1,984 | **8** | 0 |
| 15 | 168 | 2,190 | 74 | 1,806 | 74 | 0 | 0 |
| 16 | 7,615 | 195,823 | 19,664 | 165,064 | 18,669 | **371** | 0 |
| 17 | 2,580 | 50,353 | 3,358 | 29,249 | 2,448 | **24** | 0 |
| 18 | 108,447 | 3,088,672 | 298,538 | 1,665,618 | 203,121 | **2,727** | 0 |
| 19 | 74,589 | 1,643,389 | 138,981 | 410,376 | 52,551 | **167** | **1** |
| 20 | 572,519 | 13,756,281 | 1,379,539 | 1,397,305 | 261,064 | **5,756** | **3** |
| 20 supp | 4 | 4 | 0 | 0 | 0 | 0 | **4** |

\* at \(n\le14\), \(14>n-1\): the 14-gap is trivial (every pair has it), which
is why the two-poison dodge is measured jointly and why the order-14
calibration exemplar's dodge was always only about the 6.

18,754,354 pairs over 767,004 members. **Verdict lines:**

- **(F-S) kill candidates: 0.** No exactly-two member of any censused class
  carries a gapped pair. The eight profile objects (1 at 19, 3+4 at 20) are
  re-verified saturated: every one has \(6,14\in S\) (and \(C_{16}\)s, counts
  matching the records).
- **Vertex-taut gapped pairs in the wider class: 9,061** (all stored with
  full \(S\), tautness, \(C_{16}\) status). The dodge does **not** die with
  order: as a fraction of pairs it stays in the 0.01–0.2% band with no
  monotone decay through 20.

### The mechanism cut (`analyze`)

| order | taut-gapped | distinct members | min ndeg2 | full \(\mathbb P{-}2\) dodges (min ndeg2) | on power-free member | 2-connected |
|---|---|---|---|---|---|---|
| 12 | 8 | 8 | 5 | 8 (5) | 8\* | 8 |
| 14 | 8 | 8 | 7 | 8 (7) | 8\* | 8 |
| 16 | 371 | 290 | 5 | 265 (5) | 339 | 337 |
| 17 | 24 | 24 | 6 | 24 (6) | 20 | 24 |
| 18 | 2,727 | 2,196 | 5 | 2,245 (5) | 2,118 | 2,425 |
| 19 | 167 | 163 | 6 | 167 (6) | 80 | 167 |
| 20 | 5,756 | 3,794 | **4** | 4,217 (**4**) | 2,846 | 4,938 |

\* trivial below 16 (no \(C_{16}\) fits).

- **The dodge approaches the profile from above but never reaches it**: the
  minimum number of degree-2 vertices on a member carrying a taut gapped pair
  is 5 (order 18), 6 (19), **4** (order 20; ndeg2 histogram
  \(\{4{:}6,\,5{:}84,\,6{:}708,\,7{:}1732,\,8{:}1994,\,9{:}1025,\,10{:}199,\,11{:}8\}\));
  no taut gapped pair sits on a member with \(\le3\) degree-2 vertices at any
  order (with the caveat that the \(\le3\)-strata are thin — hundreds of
  members, versus half a million censused at 20).
- **Full \(\mathbb P-2\) dodges are the majority** of taut gapped pairs
  (6,934 of 9,061), down to ndeg2 = 4.
- **5,419 of the taut gapped rows sit on power-free members**
  (\(C_{16}\)-free — the class-line flag, re-verified per row), and most rows
  are on 2-connected members. In particular, at orders 18–20 there exist
  2-connected \(\{C_4,C_8,C_{16}\}\)-free graphs, vertex-taut with respect to
  a degree-2 pair, with \(S\cap\{2,6,14\}=\emptyset\) — **every hypothesis of
  the case-(5b) residual object except the exactly-two profile,
  simultaneously, with the full dodge, in-window.**

## Interpretation

Narrowest justified conclusions; everything is per censused class only.

1. **(F-S) survives its first kill test** (pre-registered outcome (i) for the
   hypothesis stratum): no vertex-taut exactly-two member with
   \(S\cap\{6,14\}=\emptyset\) exists in any censused class at orders 10–20.
   The statement's hypothesis class has exactly eight known realizations
   (orders 19–20), all saturated. At order 20 this is asserted for the
   572,519-graph sample plus the four recorded part-14 members, not for the
   full class.
2. **The tautness-only form of the saturation mechanism is refuted.** 9,061
   vertex-taut pairs in the same classes, at the same orders, escape both
   poisons — so tautness + \(\{C_4,C_8\}\)-freeness + window order do **not**
   force \(S\cap\{6,14\}\ne\emptyset\). Any interpolation lemma proving (F-S)
   must consume the exactly-two profile (equivalently: minimum degree \(\ge3\)
   off the terminals) — exactly the hypothesis `A025` T4 listed, and now the
   only one the dodge data leaves available.
3. **The same holds for (F-T)'s wider-class analogue**: escaping the poisons
   and the 16-cycle *simultaneously* is common off the profile (5,419 rows on
   power-free members). The double blocking seen on all eight profile objects
   is a phenomenon of the exactly-two stratum specifically, not of the class.
4. **Gradient datum** (mechanism-shaping, not a conclusion): the dodge's
   distance from the profile shrinks as order grows (min ndeg2 5 → 4 by order
   20) while the exactly-two wall stands; the stored near-miss corpus is the
   raw material for the profile-consuming lemma attempt.
5. Nothing here bears on orders 21–35, on the five uncensused order-20 parts,
   or on any class the generator stream does not cover (`E019`/`E022`
   generation-layer caveats are inherited verbatim).

## Independent checks

- **Anchor gate**: 45 + 57 checks under CPython 3.14.2 and PyPy 7.3.23 before
  production (§Anchors); the calibration pair must be (and is) *found* as
  gapped + taut, the eight profile objects as saturated, field for field
  against three prior experiments' records.
- **Continuous cross-algorithm checking through production**: every gapped
  pair and every exactly-two member is recomputed in full by the `E018`
  enumerator with its 6/14 verdicts asserted against the bit search — 540,135
  full-enumeration agreements per run (540,127 gapped pairs + 8 profile
  members) — plus a deterministic stride sample of non-gapped pairs (3,867
  further full enumerations, first-five-per-part included; 2,642 of the
  sampled pairs are taut, so the sample exercises the taut branch heavily).
- **Class-line integrity per member**: the degree-2 count column and the edge
  count are recomputed and asserted on every line; the `power_free` flag is
  asserted trivially 1 below order 16, re-verified by `has_cycle_len` on
  every 500th member at orders \(\ge16\) (1,510 rechecks) and on **every**
  gapped row.
- **Run-to-run reproduction**: the trimmed second production run reproduced
  the first run's tallies exactly — all 17 tally fields at every order, the
  supp14 stratum, 540,127 gapped pairs, 9,061 taut gapped pairs, 0 kill
  candidates (`run1_tallies.json` vs the second run's
  `census_summary.json`, asserted).
- **Inventory ties**: class-file totals vs the authoritative `scan_*.json`
  tallies (c15c/c15d), including the 572,519/572,530 header correction.
- Not independently re-derived: the class files themselves (the `E019`
  generation layer with its recorded caveats) and `labelg`-level isomorph
  freeness (inherited from the producing runs).
