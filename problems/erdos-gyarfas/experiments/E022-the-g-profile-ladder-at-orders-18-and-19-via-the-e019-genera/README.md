# E022 — the \(\mathcal G\)-profile ladder at orders 18 and 19

- Date: 2026-07-24
- Problem: `P-002`
- Evidence class: **exhaustive finite exclusion at orders 18 and 19** for the
  \(\mathcal G\)-profile (`G015`, search side), on the `E019` instrument
- Owner: session `S022` (worker leg W2). This is an owned experiment record, not
  a session record; it writes no ledger and draws no ledger consequence.

## Question

Does the class \(\mathcal G\) of `L039` have a member of order 18 or of
order 19?

Graph part of the target: connected, \(C_4\)-free, \(C_8\)-free, **exactly two**
vertices of degree 2 (call them \(a,b\)), every other degree \(\ge3\), and
**power-free** (no \(C_4\), \(C_8\) or \(C_{16}\); \(32>19\)). Membership in
\(\mathcal G\) additionally requires the \(S\)-condition
\(S(H,a,b)\cap\{2,6,14\}=\emptyset\), where \(S(H,a,b)\) is the set of lengths of
simple \(a\)–\(b\) paths (\(\mathbb P-2\) truncated to path lengths \(\le16\)).

A power-free member of the profile satisfying the \(S\)-condition is the reduct
of a tight 1-atom of order \(n+1\) and **disproves statement 0.1** (`L025` R4).
`E019` settled orders 14–17 (all empty); this record adds 18 and 19.

Two subsidiary questions are answered by the same run, because the generated
class contains the relevant graphs outright:

- the **0-bucket** of the degree-2 histogram is the class of \(\{C_4,C_8\}\)-free
  graphs of minimum degree \(\ge3\) at that order (`C040`'s class);
- the **1-bucket** is the shape of a tight 1-atom (`L041`).

## Logical scope

1. The order-18 and order-19 scans are **exhaustive for the stated class**
   modulo the generation layer. Every \(\mathcal G\)-candidate of order \(n\) is
   connected, \(C_4\)-free and \(C_8\)-free (power-free \(\Rightarrow\) both,
   since \(4,8\le n\)), has minimum degree 2, and has at least
   \(\lceil(3n-2)/2\rceil\) edges (degree sum \(\ge4+3(n-2)\)) — 26 at order 18,
   28 at order 19 — so it lies in the generator's stream
   `genc48 -q -c -f -d2 n mine:C(n,2)`.
2. Emptiness of the power-free profile at an order is a **finite exclusion at
   that order only**. It proves nothing at order \(\ge20\). At neither order was
   the \(S\)-condition consumed: at 18 no graph reached it (empty profile), and
   at 19 the single profile member was removed by the \(C_{16}\) test before it,
   so the \(S\)-condition is not part of either verdict. (Its value on that one
   graph is recorded below as data.)
3. **Only the unconditional filters reduce the reported class**: the degree
   profile, power-freeness, and the \(S\)-condition (`L039`). Structure facts
   from `L042` (2-connectivity, non-bipartiteness, …) are conditional on (R) and
   are recorded on the boundary exemplar as data only; nothing was pruned by
   them.
4. The generation layer (nauty's canonical construction path, plus `E019`'s
   `prune_c8` PREPRUNE plugin) is **imported** and anchored empirically, exactly
   as in `E010`–`E019`; it is not re-derived here. The plugin's own \(C_8\)
   rejection *is* independently re-verified on 100% of the output by the `E015`
   cycle detector, and `--verify-all` adds a second, separate \(C_4\)/\(C_8\)
   re-check per graph.
5. The bucket statements in §Results are exhaustive for **minimum degree
   \(\ge2\)** only. Graphs with a degree-1 vertex are outside the `-d2` stream;
   `C027`'s wider class was not re-run here (that is `E019`'s `subcubic`
   command).
6. No bound-lifting inference is drawn in this record. The `L041` case analysis
   that converts profile-emptiness at order \(n\) into tight-1-atom and
   \(\mathcal G\)-member floors belongs to the orchestrating session.

## Environment

- **Instrument: `E019`'s, referenced and not rebuilt.** `ladder.py` imports
  `E019/scan.py` from its file path and rebinds only that module's `DATA`
  constant; `GENC48` and `GENG` stay pointed at `E019/build`. No file in the
  `E019` tree was written — `sys.dont_write_bytecode` is set before the import
  so not even a `__pycache__` entry is created there, and `ladder.load_scan`
  asserts that the listing of `E019/data` is unchanged across the import.
- `genc48` provenance: nauty 2.9.3 built by `E019/build.sh` from the
  sha256-checked upstream tarball
  (`9fc4edae04f88a0f5883985be3b39cf7f898fd6cc96e96b9ee25452743cc1b5b`),
  compiled with `-DPREPRUNE=prune_c8 -DSUMMARY=summary_c8`. Binary sha256
  `f0d9ca22a164838d9b2b6287e8d6f8abe6cc901a6cc369fb82de7f2f87ef341e`; reference
  stock `geng` `4407583022…`; `scan.py` sha256
  `968421be062ceb40a969d1b82f7c5127e1a33189933a1c69dfa20c7874efe5d6`;
  `prune_c8.c` sha256 `0cbeb2e3876951cb6e1891da842ab1ea04837502349421307f67b7dc1a5111a4`.
  Recorded by `ladder.py provenance` in `data/provenance.json`.
- `labelg` from the installed nauty 2.9.3 (`/opt/homebrew/bin/labelg`) for
  canonical forms.
- **CPython 3.14.2** and **PyPy 7.3.23 (Python 3.11.15)**; all 146 anchors pass
  under both; production under PyPy 7.3.23.
- macOS 26.5.1 / darwin 25.5.0, arm64, 12 cores. Production: 8 concurrent
  worker processes.
- Standard library only; integer bitmask arithmetic; no floating point except
  wall-clock timings; no randomness; no wall-clock-dependent logic.
- **Contention note** (`process/concurrency.md`): a sibling worker leg of the
  same orchestrated session (`S022` W1) shared the machine throughout,
  advertised as compute-light. In addition, the order-19 16-part production ran
  **concurrently with the single-process order-18 unsplit count** (9 busy
  processes on 12 cores) by design, to overlap the two long jobs. All timings
  below are therefore comparable-run figures, not clean-machine benchmarks; the
  24-part order-19 run, which had the machine to itself apart from the sibling,
  is measurably faster per node than the 16-part one for exactly this reason.
- `data/` totals about 10 MB, of which about 6.4 MB is the verbatim generated
  class (graph6 + edges + degree-2 count + power-free flag, one line per graph).

## Inputs and search space

- Order 18: `genc48 -q -c -f -d2 18 26:153 r/16`, \(r=0,\dots,15\).
- Order 19: `genc48 -q -c -f -d2 19 28:171 r/16`, \(r=0,\dots,15\); and the same
  order re-split `r/24`, \(r=0,\dots,23\), into `data/split24/`.
- `mine` \(=\lceil(3n-2)/2\rceil\) (26, 28); `maxe` \(=\binom n2\) (153, 171) is
  coverage-safe — geng tightens it internally, and Reiman's bound
  \(m\le n(1+\sqrt{4n-3})/4\) gives 41.9 at 18 and 45.3 at 19 for any
  \(C_4\)-free graph. Maximum edge count actually seen in the whole
  \(\{C_4,C_8\}\)-free class: **27** at order 18, **29** at order 19.
- Filter chain per generated graph: independent `power_free` re-check (asserts
  \(4\notin\) and \(8\notin\) the present power lengths — an independent
  re-derivation of geng's `-f` and of the plugin) → degree-2 histogram → degree
  profile (exactly two 2s, rest \(\ge3\)) → \(C_{16}\) → full survivor analysis
  (spectrum, \(S(H,a,b)\), \(\mathcal G\)-membership, bipartiteness, cut
  vertices).
- `--verify-all` (on for every production run reported here) additionally
  re-runs `has_c4` and `has_cycle_len(\cdot,8)` on **every** generated graph.

## Reproduction

```sh
# from this directory; the E019 build must already exist (sh ../E019*/build.sh)
python3 ladder.py provenance            # sha256 pins of the imported instrument
sh      anchors.sh                      # 146 checks, CPython then PyPy (the gate)
sh      run18.sh                        # order 18, 16 parts, 8 concurrent
pypy3   ladder.py harvest 18 16         # merge; asserts the coverage identity
pypy3   ladder.py count 18              # independent unsplit generator count
sh      run19.sh                        # order 19, 16 parts, 8 concurrent
pypy3   ladder.py harvest 19 16
sh      run19b.sh                       # order 19 AGAIN, 24 parts -> data/split24
pypy3   ladder.py --data split24 harvest 19 24
pypy3   ladder.py splitcheck 19 16 24   # labelg SET equality between the splits
sh      checks.sh                       # boundary exemplars + brute-force spotchecks
pypy3   summary.py                      # the tables below; class-file integrity
```

Outputs land in `data/` (`provenance.json`, `anchors_*.json`, `anchors_*.log`,
`scan_n1[89]_part*of16.json`, `class_n1[89]_part*of16.txt`,
`scan_n1[89]_harvest.json`, `count_n18.json`, `splitcheck_n19_16vs24.json`,
`spotcheck_n1[89].json`, `exemplars_n1[89].json`, `summary.json`, `run*.log`)
and in `data/split24/` for the 24-part order-19 run.

## Anchors — 146 checks, both interpreters

The process rule recorded in `problem.json` is that `E019`'s 146-check anchor
suite must re-pass under **both** interpreters before any extension run. It was
run through `ladder.py` (so on the same imported code, with output redirected
here) and passed:

| interpreter | result | output |
|---|---|---|
| CPython 3.14.2 | **146 checks passed** | `data/anchors_cpython.json`, `.log` |
| PyPy 7.3.23 (3.11.15) | **146 checks passed** | `data/anchors_pypy.json`, `.log` |

`data/anchors_cpython.json` is **byte-identical** to `E019`'s own
`data/anchors_cpython.json`, i.e. all 23 `labelg` set-equality comparisons
against the independent `geng | C_8`-filter pipeline reproduce the same counts
graph for graph.

**Which `E019` anchors carry over by import.** All of them, and not by
transcription: `ladder.py` executes `E019/scan.py` itself, so the primitives
under test (`g6_decode`, `has_c4`, `has_cycle_len`, `count_cycles_len`,
`cycle_spectrum_bruteforce`, `path_lengths`, `bipartition`, `cut_vertices`,
`profile_pair`, `power_free`, `analyse_survivor`) and the generator paths are
literally the objects the anchors validated — the same file, pinned by sha256
above. The suite covers: the primitive anchors (\(K_4\), \(K_{3,3}-e\),
Petersen, Petersen\(-e\), the 2-closure of Petersen\(-e\), Heawood, \(P_4\),
\(C_5\), graph6 round trips, and `path_lengths` against the recursive `E016`
reference on all 19,593 vertex pairs of the 965 connected graphs of orders 6–7);
the 23 generator set-equality comparisons across five switch variants; the
named-object in/out membership tests; and the res/mod partition checks at
\((n,\text{mod})=(12,7),(13,5),(14,11)\).

Nothing in this record adds a new anchor to that suite. The new verification
work is the per-run cross-checking in §Independent checks.

## Results

### The ladder

Rows 14–17 are `E019`'s, repeated for continuity; 18 and 19 are new.

| n | \(\{C_4,C_8\}\)-free class | profile (exactly two deg-2) | \(C_{16}\)-blocked | power-free survivors | \(\mathcal G\)-members |
|---|---|---|---|---|---|
| 14 | 778 | 0 | 0 | 0 | 0 |
| 15 | 168 | 0 | 0 | 0 | 0 |
| 16 | 7,615 | 0 | 0 | 0 | 0 |
| 17 | 2,580 | 0 | 0 | 0 | 0 |
| **18** | **108,447** | **0** | 0 | **0** | **0** |
| **19** | **74,589** | **1** | **1** | **0** | **0** |

The coverage identity (profile = \(C_{16}\)-blocked + survivors) is asserted per
part and again at harvest; `summary.py` re-asserts it and additionally checks
profile = the 2-bucket of the degree-2 histogram.

**Order 19 is the first order in this dossier at which the \(\mathcal G\)-profile
class is nonempty** — and the \(C_{16}\) test is decisive on its single member.
See §The order-19 boundary exemplar.

### Full production table

| quantity | order 18 (16 parts) | order 19 (16 parts) | order 19 (24 parts) |
|---|---|---|---|
| \(\{C_4,C_8\}\)-free class | 108,447 | 74,589 | 74,589 |
| profile (exactly two deg-2) | 0 | 1 | 1 |
| \(C_{16}\)-blocked | 0 | 1 | 1 |
| power-free survivors | 0 | 0 | 0 |
| \(\mathcal G\)-members | 0 | 0 | 0 |
| power-free members of the class | 77,886 | 26,333 | 26,333 |
| min #degree-2 over the class | 3 | **2** | **2** |
| min #degree-2 over the power-free part | 4 | **5** | **5** |
| max edges in the class | 27 | 29 | 29 |
| max edges in the profile | — (empty) | 28 | 28 |
| labelled tree nodes | 4,583,049,197 | 32,344,309,413 | 32,344,410,453 |
| PREPRUNE rejects | 4,387,747,786 | 31,384,362,748 | 31,384,364,951 |
| generator CPU (sum over parts) | 1,472.0 s | 10,161.2 s | 9,396.4 s |
| Python wall (sum over parts) | 1,479.8 s | 11,226.8 s | 9,449.9 s |
| slowest single part | 219.9 s | 1,329.1 s | 1,237.7 s |
| wall clock, 8 workers | **220 s** | **2,031 s** | **1,473 s** |

(The 16- and 24-part node counts differ by 101,040 out of \(3.2\times10^{10}\),
i.e. \(3\times10^{-6}\): res/mod splitting duplicates a little work near the top
of the tree. The *output* is identical — see §Independent checks.)

Degree-2 histograms over the class (and over its power-free part):

- order 18: `{3:53, 4:759, 5:5001, 6:15854, 7:24644, 8:24754, 9:20123, 10:11235, 11:4188, 12:1504, 13:332}`
  / `{4:1, 5:430, 6:4661, 7:14541, 8:21271, 9:19732, 10:11226, 11:4188, 12:1504, 13:332}`
- order 19: `{2:1, 3:97, 4:1323, 5:7431, 6:18657, 7:21941, 8:14166, 9:7800, 10:3173}`
  / `{5:178, 6:1741, 7:5918, 8:8271, 9:7080, 10:3145}`

### The 0-, 1- and 2-buckets, stated explicitly

| bucket | meaning | order 18 | order 19 |
|---|---|---|---|
| 0 degree-2 vertices | \(\{C_4,C_8\}\)-free, \(\delta\ge3\) (`C040`'s class) | **0** | **0** |
| 1 degree-2 vertex | the tight-1-atom shape (`L041`) | **0** | **0** |
| 2 degree-2 vertices | the \(\mathcal G\)-profile (`L039`) | **0** | **1**, \(C_{16}\)-blocked |
| power-free 0-bucket | a counterexample to statement 0.1 outright | **0** | **0** |
| power-free 1-bucket | a tight 1-atom | **0** | **0** |
| power-free 2-bucket | a \(\mathcal G\)-candidate (then the \(S\)-test) | **0** | **0** |

Coverage for all three buckets is complete at both orders, because minimum
degree \(\ge2\) with at most two degree-2 vertices forces \(m\ge\) `mine`:
at order 18, 0/1/2 degree-2 vertices need \(m\ge27/27/26\) against `mine` \(=26\);
at order 19 they need \(m\ge29/28/28\) against `mine` \(=28\).

**The 0-bucket result agrees with `C040`, from a different search tree.** `C040`
records `genc48 -c -f -d3 n ⌈3n/2⌉:C(n,2)` as empty at orders 18 and 19 (trees
\(7.2\times10^8\) and \(5.2\times10^9\)), and the ledger flags those two orders
as having no *full* stream-side cross-check. The runs here re-derive the same
emptiness as a by-product, from the `-d2` switch set over trees \(6.3\times\) and
\(6.2\times\) larger (\(4.58\times10^9\) and \(3.23\times10^{10}\)) whose output
is 108,447 and 74,589 graphs rather than none. This is a genuine
different-run, different-tree, different-switch corroboration — but it uses the
**same generator binary and the same nauty canonical construction path**, so it
does *not* discharge `C040`'s generation-layer caveat. It is not a stream-side
cross-check.

The same remark applies to the 1-bucket and the tight-1-atom question at 18 and
19: the emptiness is obtained here directly by generation, without `L041`'s case
analysis.

### Proximity: how far is the class from the target profile?

| n | class | power-free members | min #deg-2 over class | min #deg-2 over the power-free part |
|---|---|---|---|---|
| 16 | 7,615 | 7,522 | 3 | 4 |
| 17 | 2,580 | 2,193 | 3 | 4 |
| **18** | 108,447 | 77,886 | **3** | **4** |
| **19** | 74,589 | 26,333 | **2** | **5** |

Two descriptive observations, both new at these orders:

1. **The class reached the target profile at order 19 and \(C_{16}\) stopped it.**
   The crude proximity gap closed — min #degree-2 over the class is exactly 2,
   the target — while the gap over the *power-free* part **widened**, from 4 at
   16/17/18 to 5 at 19.
2. **\(C_{16}\) is now decisive across the whole near-boundary stratum.** At
   order 19, every one of the 1 + 97 + 1,323 = **1,421** class members with at
   most four degree-2 vertices contains a \(C_{16}\) (the power-free histogram
   starts at 5). At order 18, all 53 members of the 3-bucket and 758 of the 759
   members of the 4-bucket are \(C_{16}\)-blocked. `E019` first saw this effect
   at orders 16–17 on a handful of graphs; here it holds over a stratum three
   orders of magnitude larger and, for the first time, **on the profile itself**.

### The order-19 boundary exemplar

The unique order-19 member of the \(\mathcal G\)-profile
(`data/exemplars_n19.json`, found in part 3/16 and, in the other split, in part
23/24):

```
graph6  R???C@?GC_B?@_aAA_aP?W_?BO@Gc?
```

| property | value |
|---|---|
| order / edges | 19 / 28 |
| degree sequence | \(4,3^{16},2^2\) |
| degree-2 vertices \(a,b\) | 7, 8 — **not** adjacent, \(d(a,b)=5\) |
| cycle spectrum | \(\{3,5,6,7,9,10,11,12,13,14,15,16,17,18,19\}\) |
| girth | 3 |
| \(C_4\), \(C_8\) | absent (re-verified by two algorithms) |
| \(C_{16}\) | **present**, 46 of them |
| \(S(H,a,b)\) | \(\{5,6,7,\dots,18\}\) (a full interval) |
| \(S\cap(\mathbb P-2)\) | \(\{6,14\}\) — so \(\mathcal G\)-membership **fails** |
| \(S\cap\mathbb P\) / \(S\cap(\mathbb P-1)\) | \(\{8,16\}\) / \(\{7,15\}\) |
| bipartite | no |
| cut vertices | none (2-connected) |

It is therefore blocked twice over, independently: it is not power-free (46
\(C_{16}\)s), and its through-set hits \(\mathbb P-2\) in two places. Recorded
as data; nothing is concluded from it. It is the natural first object for the
interference dissection the proof side has queued, being the only graph in the
whole 14–19 ladder that reaches the target degree profile.

### Cost and the next rung

| n | tree nodes | growth vs previous order | generator CPU | rate |
|---|---|---|---|---|
| 17 (`E019`) | 580,472,285 | ×6.60 | 226.7 s | \(2.6\times10^6\)/s |
| 18 | 4,583,049,197 | **×7.90** | 1,472.0 s | \(3.11\times10^6\)/s |
| 19 | 32,344,309,413 | **×7.06** | 10,161.2 s | \(3.18\times10^6\)/s |

`E019`'s ×6.5 extrapolation under-predicted both rungs by about 15–20%
(projected \(3.9\times10^9\) and \(2.8\times10^{10}\); actual \(4.58\times10^9\)
and \(3.23\times10^{10}\)) — well inside the pre-registered 3× stop condition,
which never came close to firing. Its wall-clock projections (≈4 min at 18,
≈25 min at 19 on 8 workers) match the measured 220 s and 2,031 s, the latter
under deliberate contention.

Projecting ×7 and \(3.2\times10^6\) nodes/s: **order 20 ≈ \(2.3\times10^{11}\)
nodes ≈ 20 h single-threaded ≈ 2.5–3 h on 8 workers**; order 21
\(\approx1.6\times10^{12}\) ≈ 140 h ≈ 18 h on 8 workers. Order 20 is a
comfortable next rung on this machine; order 21 is an overnight job; order 22 is
out of reach without further pruning.

## Interpretation

Narrowest justified conclusions, in the language `E019` used for order 17.

1. **No power-free graph of order 18 has the two-degree-2-vertex profile; a
   fortiori \(\mathcal G\) has no member of order 18.** The profile class is
   empty at order 18, so the \(S\)-condition is not consumed.
2. **No power-free graph of order 19 has the two-degree-2-vertex profile; a
   fortiori \(\mathcal G\) has no member of order 19.** Here the profile class is
   *not* empty — it has exactly one member — but that member contains 46
   \(C_{16}\)s, so no graph reaches the \(S\)-test and the \(S\)-condition is
   again not consumed. (For the record, the exemplar fails it anyway.)
3. Both statements are finite exclusions **at those orders only**, subject to the
   generation layer, with the same computational-lineage caveats as
   `C027`/`C036`/`C039`.
4. **Descriptive, not concluded:** at order 19 the generated class finally
   reaches the target degree profile and is stopped by \(C_{16}\); the whole
   \(\le4\)-degree-2 stratum at 19 (1,421 graphs) and almost all of it at 18 are
   \(C_{16}\)-blocked. Whatever excludes the profile at these orders is now the
   16-cycle, not the 8-cycle.
5. Any lifting of the tight-1-atom or \(\mathcal G\)-member order floors from
   these facts is the orchestrating session's arithmetic (`L041`) and is
   deliberately absent from this record.

## Independent checks

- **The anchor gate**: `E019`'s 146 checks re-passed under CPython 3.14.2 and
  PyPy 7.3.23 before any production run, with a comparison table byte-identical
  to `E019`'s.
- **Independent unsplit count at order 18.** `ladder.py count 18` ran the
  generator once, unsplit, in a separate single process (`geng -u`, no Python
  filtering): **108,447** graphs from 4,582,989,287 tree nodes, 1,663.6 s —
  **exactly** the 16-part production total. `summary.py` asserts the equality.
- **16-vs-24 split agreement at order 19 (the in-leg partition check).** The
  order-19 scan was re-run split a different way, 24 parts instead of 16, into a
  separate data root. `ladder.py splitcheck 19 16 24` reports: totals equal
  (74,589 = 74,589); each run isomorph-free (74,589 `labelg` canonical forms =
  74,589 lines, on both sides); the two class **sets** equal as `labelg`
  canonical sets; and every aggregate equal (profile, \(C_{16}\)-blocked,
  survivors, max edges, and both degree-2 histograms, bucket by bucket). The
  single profile member appears in part 3 of the 16-split and part 23 of the
  24-split, as it must.
  **The unsplit count at order 19 was not run here** — it is ≈3 h single-process
  and is a named orchestrator follow-up, not part of this leg. The 16-vs-24
  agreement is this leg's partition check and is strictly stronger than a count
  match, being a set equality rather than a total.
- **Per-graph re-verification of the generation layer.** `power_free` (the
  `E015` detector) is run on **every** generated graph at both orders and
  asserts that neither 4 nor 8 is a present power length; `--verify-all` adds
  independent `has_c4` and `has_cycle_len(\cdot,8)` calls on every graph. Across
  the three production runs that is 257,625 graphs (108,447 + 74,589 + 74,589),
  each re-checked twice by code paths independent of geng's `-f` and of the
  plugin. `summary.py` asserts `verify_all` was on in all 56 part tallies.
- **Second-algorithm spectrum spot check** (`ladder.py spotcheck`): the full
  cycle spectrum of every class member with at most four degree-2 vertices —
  **812** graphs at order 18 and **1,421** at order 19, i.e. the entire
  near-miss stratum, 2,233 graphs against `E019`'s 205 — was recomputed by
  `cycle_spectrum_bruteforce`, which shares no code path with `has_cycle_len`.
  In every case \(4,8\notin\) spectrum and the recorded \(C_{16}\) verdict
  agrees. The boundary exemplar is additionally re-verified this way in
  `exemplar.py`.
- **Class-file integrity.** `summary.py` and `splitcheck` re-count the saved
  class files line by line and assert the totals against the part tallies:
  108,447 rows at 18 and 74,589 rows in each order-19 split. No part exceeded
  `scan.py`'s `SAVE_LIMIT`, so the recorded class is the complete generated
  class, not a sample.
- **Coverage identity** (profile = \(C_{16}\)-blocked + survivors) asserted per
  part, at harvest, and again in `summary.py`, which also asserts profile = the
  2-bucket of the degree-2 histogram.
- **The generator's own accounting**: `scan.py` asserts that the number of
  graphs read from the pipe equals the plugin's `SUMMARY` `out=` figure, on
  every part.
- **E019 left untouched**: `ladder.load_scan` snapshots `E019/data` before and
  after importing `scan.py` and asserts the listings agree, and
  `sys.dont_write_bytecode` is set first so no `.pyc` is written there either
  (verified after the run: `E019/__pycache__` still holds only its pre-existing
  CPython 3.14 entry).
- Not independently re-implemented: nauty's canonical construction path and the
  PREPRUNE completeness argument (imported generation layer, anchored as in
  `E010`–`E019`).
