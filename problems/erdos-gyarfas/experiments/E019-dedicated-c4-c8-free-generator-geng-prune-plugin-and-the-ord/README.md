# E019 — the dedicated {C4,C8}-free generator (geng PRUNE plugin) and the order-17 G-profile scan

- Date: 2026-07-24
- Problem: `P-002`
- Evidence class: **instrument construction** (`G014` item 6) + **exhaustive
  finite exclusion at order 17** for the \(\mathcal G\)-profile, plus
  cross-instrument reproductions of `C027`/`C036`/`C013`(order 24)
- Owner: session `S021` (search-side leg)

## Question

Two questions, one per half.

1. **The instrument (`G014` item 6).** `C036`/`E018` closed the order-16
   \(\mathcal G\)-profile scan by filtering geng's whole \(C_4\)-free stream
   (346,573,602 graphs, 2,893.5 CPU-s) and found the \(C_8\) filter 100%
   decisive, as it has been at every order ever scanned in this profile. So:
   can Markström's design — a canonical construction path with **incremental
   \(C_8\) rejection** — be built here, verified, and made to replace the
   filter-the-stream instrument?
2. **The order-17 leg (`G015` live move (iii)).** Does the class
   \(\mathcal G\) of `L039` have a member of order 17? Graph part:
   connected, \(C_4\)-free, exactly two vertices of degree 2 (\(a,b\)), all
   other degrees \(\ge3\), **power-free** (no \(C_4/C_8/C_{16}\) at this
   order); membership additionally requires
   \(S(H,a,b)\cap\{2,6,14\}=\emptyset\) (\(\mathbb P-2\) truncated to path
   lengths \(\le16\)). A hit satisfying the \(S\)-condition is the reduct of
   a tight 1-atom of order 18 and **disproves statement 0.1** (`L025` R4);
   emptiness lifts `L041`'s tight-1-atom bound from \(\ge18\) (`C036`) to
   \(\ge19\).

## Logical scope

1. The order-17 scan is **exhaustive for the stated class** modulo the
   generation layer. Every \(\mathcal G\)-candidate of order 17 is connected,
   \(C_4\)-free and \(C_8\)-free (power-free \(\Rightarrow\) both, since
   \(4,8\le17\)), has minimum degree 2, and has \(\ge25\) edges (degree sum
   \(\ge4+3\cdot15=49\)), so it lies in the generator's stream
   `genc48 -q -c -f -d2 17 25:136`. Emptiness is a finite exclusion at
   order 17 for this profile; it proves nothing at order \(\ge18\). It does
   **not** consume the \(S\)-condition (no survivor reached that filter).
2. **Only the unconditional filters reduce the reported class**: the degree
   profile, power-freeness, and the \(S\)-condition (`L039`). Structure facts
   from `L042` (2-connectivity, non-bipartiteness, …) are conditional on (R)
   and are recorded on survivors as data only; nothing was pruned by them.
3. The generation layer (nauty's canonical construction path) is **imported**,
   exactly as in `E010`–`E018`, and is anchored empirically rather than
   re-derived; see "Completeness" and "Anchors" below. The plugin's own
   \(C_8\) rejection is verified independently on 100% of the output by the
   `E015` cycle detector.
4. The extra tables (degree-2 histograms, power-free counts, the cubic and
   bipartite probes) are **descriptive data and feasibility measurements**.
   They fire no kill condition and prove no universal statement.

## Environment

- **nauty 2.9.3**, built from source in this experiment. Source: the exact
  tarball Homebrew verifies for its `nauty` formula
  (<https://pallini.di.uniroma1.it/nauty2_9_3.tar.gz>), obtained with
  `brew fetch --build-from-source nauty`;
  sha256 `9fc4edae04f88a0f5883985be3b39cf7f898fd6cc96e96b9ee25452743cc1b5b`
  (re-checked by `build.sh` on every run). Compiler: Apple clang 17.0.0
  (clang-1700.6.4.2), `gcc -O3 -march=native` as chosen by nauty's own
  `configure`; word size `-DMAXN=WORDSIZE -DWORDSIZE=32`, i.e. the same build
  recipe as nauty's stock `geng` target.
- `labelg` from the installed nauty 2.9.3 (`/opt/homebrew/bin`) for canonical
  forms; the installed `geng` is the instrument `E010`–`E018` used, and the
  freshly built `build/nauty2_9_3/geng` is the reference side of every
  cross-check here.
- CPython 3.14.2 and PyPy 7.3.23 (Python 3.11.15); **all 146 anchors pass
  under both**; production under PyPy 7.3.23.
- macOS 26.5.1 / darwin 25.5.0, arm64 (Mac15,6), 12 cores.
- Standard library only; integer bitmask arithmetic throughout; no floating
  point except wall-clock timings; no randomness; no wall-clock-dependent
  logic.
- Contention note (`process/concurrency.md`): the order-17 production used 8
  workers; the cubic/bipartite probes ran as single background jobs
  afterwards. A sibling proof-side worker leg shared the machine (compute
  light). Timings are comparable-run figures, not clean-machine benchmarks.
- `build/` (imported nauty source tree + compiled binaries) is git-ignored;
  `build.sh` reproduces it from the sha256-checked tarball.

## The instrument

`prune_c8.c` is a nauty **PREPRUNE** plugin. `build.sh` compiles nauty's own
`geng.c` with

```
-DPREPRUNE=prune_c8 -DSUMMARY=summary_c8
```

producing `build/genc48`, which behaves exactly like `geng` except that no
graph containing an 8-cycle is ever produced or extended. \(C_4\) rejection
is geng's native `-f`.

`prune_c8(g,n,maxn)` returns nonzero iff **the newest vertex of `g` lies on an
8-cycle**: it relabels `g` so the newest vertex is index 0, runs one
multi-source BFS in \(g-0\) from \(N(0)\) for distance pruning, and then, for
each pair \(a<b\) of neighbours of 0, searches for a simple six-edge \(a\)–\(b\)
path avoiding 0. Exact, deterministic, no heuristics.

### Completeness

geng builds each output graph by adding vertices \(0,1,2,\dots\) in order, and
(nauty 2.9.3 `geng.c`, "PRUNE feature", lines 180–187) *each graph in that
construction sequence is an induced subgraph of all later graphs in the
sequence*. `PREPRUNE(gx,k,maxn)` is called on every candidate extension `gx`
of order \(k\) — `geng.c` `accept1` line 1748, `accept1b` line 1851, `accept2`
line 1979, the three gates through which every extension and every final
output graph passes — and a nonzero return discards `gx` together with its
entire subtree. Containing an 8-cycle is **monotone under passing to
subgraphs**, so if a target graph \(G\) of order `maxn` is \(C_8\)-free then
every graph in its construction sequence is \(C_8\)-free, no call on that path
ever returns nonzero, and \(G\) is produced exactly as it would be without the
plugin. Conversely every emitted graph passed the call at order `maxn`, and by
induction its parent was already \(C_8\)-free, so an 8-cycle could only run
through the newest vertex — which is precisely what the call tests. The plugin
never touches geng's canonical construction path or its isomorphism rejection;
it only deletes whole subtrees. Hence **the output is geng's usual
isomorph-free stream intersected with "no \(C_8\)", each isomorphism class
exactly once** — no over-generation and no dedup step. This is an imported
completeness property of nauty, anchored below by full `labelg` set equality
against the independent `geng -f | C_8`-filter pipeline, by res/mod partition
checks, and by named-object membership tests; nauty's canonicity itself is not
re-implemented, exactly as in `E010`–`E018`.

## Inputs and search space

- Production stream: `genc48 -q -c -f -d2 17 25:136 r/16`, \(r=0,\dots,15\).
  `mine` \(=\lceil(3n-2)/2\rceil=25\); `maxe` \(=\binom{17}2=136\) is
  coverage-safe (geng tightens it internally; the Reiman bound
  \(m\le n(1+\sqrt{4n-3})/4=38.5\) independently guarantees no \(C_4\)-free
  graph above 38 edges; maximum edge count actually seen in the whole
  \(\{C_4,C_8\}\)-free class at 17: **25**).
- Filter chain per generated graph: independent `power_free` re-check
  (asserts \(4\notin\), \(8\notin\) present — an independent re-derivation of
  geng's `-f` and of the plugin) → degree-2 histogram → degree profile
  (exactly two 2s, rest \(\ge3\)) → \(C_{16}\) → full survivor analysis
  (spectrum, \(S(H,a,b)\), \(\mathcal G\)-membership, bipartiteness, cut
  vertices).
- `--verify-all` additionally re-runs `has_c4` and `has_cycle_len(·,8)` on
  every generated graph; it was on for every run reported here.

## Reproduction

```sh
sh build.sh                          # fetch-check, configure, build geng + genc48
python3 scan.py anchors              # 146 checks, CPython
pypy3   scan.py anchors              # 146 checks, PyPy
pypy3   scan.py run 10 11 12 13 14 15 16 --verify-all   # one order per call
pypy3   scan.py count 17             # unsplit generator count (independent total)
sh      run17.sh                     # 16 parts, 8 concurrent workers
pypy3   scan.py harvest 17 16        # merge, assert coverage identity, verdict
pypy3   scan.py spotcheck 17 4        # second-algorithm re-verification
pypy3   scan.py spotcheck 16 4
pypy3   scan.py subcubic 12 13 14 15 16 17   # C027's own class, two orders on
pypy3   scan.py crosscheck mindeg3 12 13 14 15 16 17  # stream-vs-generator, -d3 path
pypy3   scan.py cubic24              # external anchor vs E005 / Markström Table 3
pypy3   scan.py probe cubic 14 16 18 20 22 24
pypy3   scan.py probe bip   14 16 18 20 22 23 24
pypy3   scan.py probe mindeg3 14 15 16 17 18 19
pypy3   scan.py probe subcubic2 14 15 16 17
```

Outputs land in `data/` (`anchors_*.json`, `scan_n*.json`,
`scan_n17_part*of16.json`, `scan_n17_harvest.json`, `class_n*.txt`,
`count_n17.json`, `spotcheck_n*.json`, `subcubic_n*.json`,
`cubic24_check.json`, `probe_*.json`).

## Anchors — 146 checks, both interpreters

**Primitive anchors** (the `E018` suite, re-run on the copied primitives, plus
Heawood): \(K_4\) (spectrum \(\{3,4\}\), has a \(C_4\)); \(K_{3,3}-e\)
(spectrum \(\{4,6\}\), degree-2 pair \((2,5)\), \(S=\{3,5\}\)); Petersen
(cubic, spectrum \(\{5,6,8,9\}\), \(C_4\)-free, 12 pentagons, 10 hexagons);
Petersen\(-e\) (\(S=\{4,5,7,8\}\), spectrum \(\{5,6,8,9\}\),
\(C_8\)-blocked); the 2-closure of Petersen\(-e\) (spectrum \(\{5,\dots,10\}\),
not power-free — `L039`'s prediction from \(6\in S+2\)); Heawood (cubic,
spectrum \(\{6,8,10,12,14\}\), **21** \(C_8\)s, bipartite — matching `E015`);
cut vertices and bipartition on \(P_4\)/\(C_5\); graph6 round trips;
`path_lengths` agrees with the recursive `E016` reference on **all 19,593**
vertex pairs of the 965 connected graphs of orders 6–7.

**Generator set-equality anchors.** For five class variants (chosen to cover
the distinct extension tables geng uses — plain squarefree, squarefree with
`-D`, and the bipartite path `makeb6graph`) and every order listed,
`genc48`'s output and the independent pipeline
`geng (same switches) | has_cycle_len(·,8)` were canonicalized with `labelg`
and compared **as sets**, not merely as counts; and every generated graph was
re-tested for \(C_4\)- and \(C_8\)-freeness. All 23 comparisons are exact and
nonzero; `genc48`'s output is also asserted isomorph-free (canonical set size
= line count).

| variant | switches | n | `genc48` | stock geng stream | geng ∩ \(C_8\)-free | set-equal |
|---|---|---|---|---|---|---|
| d2 | `-c -f -d2` | 8 | 17 | 28 | 17 | yes |
| d2 | `-c -f -d2` | 9 | 55 | 112 | 55 | yes |
| d2 | `-c -f -d2` | 10 | 151 | 533 | 151 | yes |
| d2 | `-c -f -d2` | 11 | 500 | 3,126 | 500 | yes |
| d2 | `-c -f -d2` | 12 | 1,644 | 22,707 | 1,644 | yes |
| d1 | `-c -f -d1` | 6 | 19 | 19 | 19 | yes |
| d1 | `-c -f -d1` | 7 | 57 | 57 | 57 | yes |
| d1 | `-c -f -d1` | 8 | 175 | 186 | 175 | yes |
| d1 | `-c -f -d1` | 9 | 642 | 740 | 642 | yes |
| d1 | `-c -f -d1` | 10 | 2,430 | 3,389 | 2,430 | yes |
| sub3 | `-c -f -d2 -D3` | 8 | 6 | 14 | 6 | yes |
| sub3 | `-c -f -d2 -D3` | 9 | 12 | 37 | 12 | yes |
| sub3 | `-c -f -d2 -D3` | 10 | 31 | 105 | 31 | yes |
| sub3 | `-c -f -d2 -D3` | 11 | 66 | 290 | 66 | yes |
| sub3 | `-c -f -d2 -D3` | 12 | 166 | 956 | 166 | yes |
| sub3 | `-c -f -d2 -D3` | 13 | 428 | 3,178 | 428 | yes |
| bipd1 | `-c -f -b -d1` | 8 | 29 | 30 | 29 | yes |
| bipd1 | `-c -f -b -d1` | 9 | 62 | 64 | 62 | yes |
| bipd1 | `-c -f -b -d1` | 10 | 164 | 177 | 164 | yes |
| bipd2 | `-c -f -b -d2` | 10 | 3 | 6 | 3 | yes |
| bipd2 | `-c -f -b -d2` | 11 | 1 | 7 | 1 | yes |
| bipd2 | `-c -f -b -d2` | 12 | 6 | 29 | 6 | yes |
| bipd2 | `-c -f -b -d2` | 13 | 5 | 57 | 5 | yes |

**Named-object anchors.** Petersen and Petersen\(-e\) are **not** generated
(both carry a \(C_8\)) but **are** present in the unpruned `geng -c -f -d2 10`
stream; Heawood is **not** generated at order 14; \(C_5,C_6,C_7\) and
\(C_9,\dots,C_{13}\) are each generated as the unique 2-regular member of
their order; \(C_8\) is **not** generated but **is** in the unpruned stream;
\(K_4\) is excluded by `-f` on both sides.

**res/mod partition anchors.** `genc48`'s split output is exactly the unsplit
output as a multiset at \((n,\text{mod})=(12,7),(13,5),(14,11)\); and at
order 17 the 16-part production total (2,580) equals the independent unsplit
`count 17` total (2,580).

**External anchor — the cubic order-24 census.** `scan.py cubic24` regenerates
every connected cubic \(\{C_4,C_8\}\)-free graph of order 24 in one step:
**4 graphs**, `labelg`-set-equal to `E005`'s independently produced
`data/survivors_n24.g6`, and equal to Markström's Table 3 count of 4 (`C014`);
all four carry a \(C_{16}\), as `E005` records. Cost: 522 s from a
1,316,000,543-node tree, against the "hours" `E005` needed for the same census
by filtering geng's cubic stream.

## Results

### The instrument versus the stream (same verdicts, two instruments)

`-c -f -d2 n`, `mine` \(=\lceil(3n-2)/2\rceil\), `maxe` \(=\binom n2\):

| n | \(\{C_4,C_8\}\)-free class | labelled tree nodes | pruned | generator CPU |
|---|---|---|---|---|
| 10 | 14 | 1,958 | 410 | 0.00 s |
| 11 | 0 | 8,440 | 2,626 | 0.01 s |
| 12 | 94 | 51,065 | 26,815 | 0.05 s |
| 13 | 10 | 273,420 | 171,341 | 0.22 s |
| 14 | 778 | 1,919,443 | 1,478,824 | 1.16 s |
| 15 | 168 | 11,647,469 | 9,704,091 | 6.16 s |
| 16 | 7,615 | 87,946,522 | 79,148,541 | 38.57 s |
| 17 | **2,580** | 580,472,285 | 539,616,286 | 226.65 s |

At order 16 this is the **same verdict** as `E018` from a 45,000× smaller
output stream (7,615 against 346,573,602 graphs) and about 75× less CPU
(38.6 s against 2,893.5 s). The tree grows by a factor \(\approx6.5\) per
order (measured: 5.35, 7.02, 6.07, 7.55, 6.60), and the generator runs at
\(\approx2.6\times10^6\) tree nodes per second.

**What that buys the search ladder.** Projecting the same rate: order 18
\(\approx3.9\times10^9\) nodes, \(\approx26\) min single-threaded and
\(\approx4\) min on 8 workers; order 19 \(\approx2.8\times10^{10}\),
\(\approx3\) h and \(\approx25\) min; order 20 \(\approx2\times10^{11}\),
\(\approx21\) h and \(\approx2.8\) h. So the \(\mathcal G\)-profile ladder is
affordable to about order 20 on this machine, where `E018`'s instrument was
already at its limit at 16. (`E018` projected \(\approx6\times10^9\) stream
graphs for order 17 alone.)

### Profile-emptiness reproduction and the order-17 production run

| n | class | profile (exactly two deg-2) | \(C_{16}\)-blocked | power-free survivors | \(\mathcal G\)-members |
|---|---|---|---|---|---|
| 14 | 778 | **0** | 0 | 0 | 0 |
| 15 | 168 | **0** | 0 | 0 | 0 |
| 16 | 7,615 | **0** | 0 | 0 | 0 |
| **17** | **2,580** | **0** | 0 | **0** | **0** |

Orders 14–16 reproduce `C027` (through 15) and `C036` (at 16) from a
completely different instrument. Order 17 is new. The coverage identity
(profile = \(C_{16}\)-blocked + survivors) is asserted per part and at
harvest; the 16-part total matches the independent unsplit count exactly.
Production: 16 parts, 8 concurrent workers, 305.9 CPU-s, \(\approx\)40 s wall.

**The \(C_{16}\) test again never became decisive for the profile** — but only
because the profile class is empty; see the next table, where \(C_{16}\) *is*
decisive for the graphs nearest the profile.

### Proximity: how far is the class from the target profile?

`E018`'s proximity statistic was "minimum number of \(C_8\)s over the profile
class" (1 at order 16). With \(C_8\) now built into generation, the natural
statistic is the **number of degree-2 vertices** — the target is exactly 2.

| n | class | power-free members | min #deg-2 over class | min #deg-2 over the power-free part |
|---|---|---|---|---|
| 10 | 14 | 14 | 4 | 4 |
| 12 | 94 | 94 | 4 | 4 |
| 13 | 10 | 10 | 4 | 4 |
| 14 | 778 | 778 | 4 | 4 |
| 15 | 168 | 168 | 4 | 4 |
| 16 | 7,615 | 7,522 | **3** | 4 |
| 17 | 2,580 | 2,193 | **3** | 4 |

Degree-2 histograms (class / power-free part):

- order 16: `{3:4, 4:86, 5:415, 6:1217, 7:2130, 8:1961, 9:1062, 10:568, 11:172}`
  / `{4:65, 5:378, 6:1194, 7:2123, 8:1960, 9:1062, 10:568, 11:172}`
- order 17: `{3:12, 4:103, 5:316, 6:577, 7:876, 8:696}`
  / `{4:8, 5:148, 6:485, 7:858, 8:694}`

Two observations, both descriptive:

1. **The \(C_{16}\) filter is decisive exactly at the boundary.** At orders
   16 and 17 every \(\{C_4,C_8\}\)-free graph with only 3 degree-2 vertices
   (4 of them at 16, 12 at 17) contains a \(C_{16}\); at 17 only 8 of the 103
   with 4 degree-2 vertices survive it. This is the first place in this
   dossier where \(C_{16}\) does the work — it was never decisive in `E015`,
   `E018`, or `C027`.
2. **No connected \(\{C_4,C_8\}\)-free graph of order 16 or 17 with minimum
   degree \(\ge2\) has two or fewer degree-2 vertices at all** (the histograms
   have no `0`, `1` or `2` bucket). Coverage for those three buckets is
   complete, because \(\le2\) degree-2 vertices and minimum degree \(\ge2\)
   force \(m\ge\lceil(3n-2)/2\rceil=\) `mine` (0 degree-2 vertices need
   \(m\ge24\) at 16 and \(\ge26\) at 17; 1 needs \(\ge24\) and \(\ge25\); 2
   needs \(\ge23\) and \(\ge25\)). So at orders 16 and 17 the whole
   \(\le2\)-degree-2 class is empty, not only the exactly-two profile — which
   is what `C036` had to leave open at 16 (`C035` was pair-level there) and
   what `C027` established stream-level only through order 15. A tight 1-atom
   sits in the `1` bucket and a minimum-degree-3 counterexample in the `0`
   bucket, so this re-derives their exclusion at 16 and 17 **directly**, by
   generation, without `L041`'s case analysis (for tight 1-atoms) and without
   `L022`'s order-18 census route (for counterexamples). It is corroboration
   of those bounds by a different instrument, not a new bound. The `subcubic`
   command extends the same statement to minimum degree \(\ge1\), i.e. to
   `C027`'s own class; see below.

### `C027`'s own class, two orders further (`scan.py subcubic`)

`C027`'s class is *connected, \(C_4\)-free, minimum degree \(\ge1\), at most
two sub-cubic vertices* (degree 1 or 2), exhausted through order 15 by
filtering geng's stream. The same class, generated \(\{C_4,C_8\}\)-free
(`-c -f -d1 n mine:maxe`, \(\text{mine}=\lceil(3n-4)/2\rceil\), the bound
forced by two degree-1 vertices) and then filtered on the sub-cubic count:

| n | mine | \(\{C_4,C_8\}\)-free class | \(\le2\) sub-cubic | power-free | wall |
|---|---|---|---|---|---|
| 12 | 16 | 2,515 | **0** | 0 | 0.1 s |
| 13 | 18 | 1,939 | **0** | 0 | 0.3 s |
| 14 | 19 | 24,184 | **0** | 0 | 2.0 s |
| 15 | 21 | 18,982 | **0** | 0 | 10.2 s |
| **16** | 22 | 272,596 | **0** | 0 | 73.5 s |
| **17** | 24 | 229,259 | **0** | 0 | 409.2 s |

Orders 12–15 reproduce `C027`; **16 and 17 are new for the full class**
(minimum degree \(\ge1\), not only \(\ge2\)). Every member of `C027`'s class
at those orders would be \(C_8\)-containing — here it is simply never
generated, and the surviving \(\{C_4,C_8\}\)-free graphs all have three or
more sub-cubic vertices.

## Interpretation

Narrowest justified conclusions.

1. **No power-free graph of order 17 has the two-degree-2-vertex profile; a
   fortiori \(\mathcal G\) has no member of order 17.** With `L041`'s case
   analysis (cases (1)/(3) impossible, (2) \(\ge39\), (4) \(\ge20\), (5) needs
   a \(\mathcal G\)-reduct of order \(n_0-1\ge18\)): **every tight 1-atom has
   order \(\ge19\)**, and every \(\mathcal G\)-member has order \(\ge18\).
   Unconditional (no (R) needed); same computational-lineage caveats as
   `C027`/`C036`.
2. **`C027`'s class is empty at orders 16 and 17 too.** No connected
   \(\{C_4,C_8\}\)-free graph of order 16 or 17 with minimum degree \(\ge1\)
   and at most two sub-cubic vertices exists — a two-order extension of
   `C027`'s stream-level exhaustion, obtained directly rather than through
   `C035`'s pair-level argument. Two consequences already known by other
   routes are re-derived here directly, as cross-checks rather than new
   bounds: no tight 1-atom at 16 or 17 (previously via `L041`'s case analysis
   plus `C036`), and no \(\{C_4,C_8\}\)-free graph of minimum degree \(\ge3\)
   at 16 or 17 (previously `L022`, which gives \(\ge19\) — strictly stronger).
3. `G014` item 6 is **discharged as an instrument**: the design is built,
   anchored 23 ways against the independent pipeline plus named objects and an
   external census, and it is roughly two orders of magnitude cheaper than
   filtering geng's stream. Markström's method is imported as a *design*; no
   external result is imported by it.
4. The channel remains close in the crude counting sense — 3 degree-2 vertices
   against the target 2 at both 16 and 17 — but the blocking mechanism has
   changed: it is now \(C_{16}\), not \(C_8\), that kills the nearest misses.
5. **Flagged for the orchestrator, not concluded here.** A feasibility
   measurement with the same engine (design-analysis section, Tier 3) found
   **no \(\{C_4,C_8\}\)-free graph of minimum degree \(\ge3\) at orders 14–19**,
   which if audited would put every counterexample to statement 0.1 at order
   \(\ge20\), improving `L022`'s \(\ge19\). It was not a commissioned leg, its
   orders 18–19 have no stream-side cross-check, and it must be verified
   before any ledger row. The engine could reach orders 20–21 in about 45 min
   and 5 h on 8 workers.

## Design analysis for the neighbouring legs (measurements, no production runs)

### Tier 0 — cubic order 30 (`C013`'s census stops at 28)

Same engine, switches `-c -f -d3 -D3 n 3n/2:3n/2`, plus a \(C_{16}\)
post-filter on the (tiny) output. Measured:

| n | cubic \(\{C_4,C_8\}\)-free | tree nodes | generator CPU |
|---|---|---|---|
| 14 | 0 | 9,063 | 0.0 s |
| 16 | 0 | 85,345 | 0.0 s |
| 18 | 0 | 843,516 | 0.4 s |
| 20 | 0 | 9,022,828 | 3.8 s |
| 22 | 0 | 104,644,797 | 42.1 s |
| 24 | **4** | 1,316,000,543 | 511.3 s |

The order-24 line reproduces Markström's Table 3 exactly and is set-equal to
`E005`'s four graphs. Growth per two orders: ×9.4, ×9.9, ×10.7, ×11.6, ×12.6 —
call it ×13 and ×14 for the next two steps. Projections (single-threaded, this
machine): order 26 \(\approx1.8\times10^{10}\) nodes, \(\approx1.9\) h; order
28 \(\approx2.6\times10^{11}\), \(\approx28\) h; **order 30
\(\approx4\times10^{12}\) nodes, \(\approx18\) days single-threaded,
\(\approx2.3\) days on 8 workers** with the res/mod split (whose correctness
under pruning is already anchored). Orders 26 and 28 are cheap enough to run
first as reproductions of the remaining `C013`/`C014` lines (23 and 251),
which would upgrade them from reported to internally reproduced.

Whether a girth-capable cubic generator beats this: `genreg`/`minibaum` are
specialized for regular graphs and would generate the cubic tree far faster,
but their built-in constraint is **girth**, and \(\{C_4,C_8\}\)-free is not a
girth condition (cubic \(C_4\)-free graphs may contain triangles, \(C_5\)s,
\(C_6\)s, \(C_7\)s — indeed all four order-24 survivors have girth 3). Using
`genreg -g5` would exclude legitimate members; using it with no girth bound
means generating all \(\approx8.5\times10^{11}\) cubic graphs of order 30 and
filtering, which is exactly what Markström did to 28 and is *worse* than the
pruned tree above. The right move is either this engine, or `minibaum`/`genreg`
patched with the same incremental \(C_8\) rejection (the same 60 lines, in a
different host). Neither is needed at order 26/28 first.

### Tier 2 — the bipartite class at order 24+ (`C034`/`E015`)

Same engine plus geng's `-b`: `genc48 -c -f -b -d2 n mine:maxe`, with `E015`'s
sub-cubic-count filter (at most two degree-2 vertices) applied in Python
afterwards. Note the class differs slightly from `E015`'s genbg stream in
shape only: `genbg -Z1` is \(C_4\)-freeness for bipartite graphs, and geng's
`-b -f` is the same condition; the `A017` T5 split-counting bound is not
needed because geng does not enumerate by part sizes.

Measured (generator only, `-u`, `mine` \(=\lceil(3n-2)/2\rceil\)):

| n | bipartite \(\{C_4,C_8\}\)-free | tree nodes | generator CPU | `E015` genbg wall for the same order |
|---|---|---|---|---|
| 14 | 0 | 14,353 | 0.0 s | \(\le3\) s |
| 16 | 0 | 147,246 | 0.3 s | \(\le3\) s |
| 18 | 0 | 1,900,375 | 3.1 s | \(\le3\) s |
| 20 | 0 | 28,357,873 | 36.3 s | 38 s |
| 22 | 0 | 481,555,031 | 476.7 s | 2,798 s |

An order-23 probe was launched but **did not finish** (killed after roughly
3,000 s of contended wall clock); no order-23 or order-24 figure is claimed
here. Even orders only.

The engine's output is empty at every completed order — it never even produces
a bipartite \(\{C_4,C_8\}\)-free graph with the profile edge bound, so the
sub-cubic-count filter never engages, which is the same verdict `C034` reached
at far greater cost. **The crossover is at order 20–22**: below it genbg's
specialized bipartite enumeration is competitive or better, and at 22 the
pruned engine is \(\approx5.9\times\) faster on wall clock (476.7 s against
`E015`'s 2,798 s — different languages and machine loads, so treat the ratio
as indicative). The gap should widen because genbg's cost tracks the whole
bipartite \(C_4\)-free stream (55.5M graphs at 22, 260.8M at 23) while the
pruned tree tracks the far sparser \(\{C_4,C_8\}\)-free world. Extrapolating
the measured \(\times17.0\) per two even orders: order 24
\(\approx8\times10^9\) nodes, \(\approx2.3\) h single-threaded,
\(\approx20\) min on 8 workers with the anchored res/mod split, against
`E015`'s own projection of \(\approx4\times\) its order-23 cost
(\(\approx5.8\) h) for genbg. So the Tier 2 leg should switch instruments at
order 24, and orders 24–26 look reachable in hours rather than days — but
the odd orders behave differently in this class and the unfinished order-23
probe is a warning that the even-order growth rate should not be assumed to
interpolate. What the engine needs beyond what is already built: nothing but
the existing `-b` switch (its code path, `makeb6graph`, is anchored here at
seven (variant, order) pairs) plus the `E015` sub-cubic-count post-filter;
`A017` T5's split-counting bound becomes unnecessary because geng does not
enumerate by part sizes.

### Tier 3 — the general minimum-degree-3 search (measured because it is the same engine; not a commissioned leg)

`genc48 -c -f -d3 n mine:maxe`, \(\text{mine}=\lceil3n/2\rceil\), generates
exactly the class in which a counterexample must live (`L022`: the smallest
\(\{C_4,C_8\}\)-free graph of minimum degree \(\ge3\) has order 19–24; the
published external frontier `C012` is "at least 16").

| n | \(\{C_4,C_8\}\)-free, \(\delta\ge3\) | tree nodes | generator CPU |
|---|---|---|---|
| 14 | 0 | 361,418 | 0.3 s |
| 15 | 0 | 2,282,222 | 1.7 s |
| 16 | 0 | 15,026,134 | 9.7 s |
| 17 | 0 | 102,595,800 | 59.9 s |
| 18 | 0 | 722,197,250 | 401.3 s |
| **19** | **0** | 5,233,244,788 | 2,657.0 s |

**Read carefully.** Coverage is complete for this class: minimum degree
\(\ge3\) forces \(m\ge\lceil3n/2\rceil=\) `mine`, `maxe` \(=\binom n2\) is
coverage-safe, and a disconnected example would have a connected component of
smaller order in the same class, excluded at every smaller order here and by
`C027`/`C012` below 14. So, **subject to the generation layer**, no
\(\{C_4,C_8\}\)-free graph of minimum degree \(\ge3\) exists on at most 19
vertices, which would put the smallest one at order \(\ge20\) and every
counterexample to statement 0.1 at order \(\ge20\) — one better than `L022`'s
\(\ge19\), and four past the published `C012`. **This is reported as worker
output for audit, not as a ledger row**; it was produced as a by-product of a
feasibility measurement, it needs the orchestrator's verification before it
can be claimed, and it rests entirely on the generator's completeness. The
directly relevant validations are: the full filter-the-stream cross-check on
this exact switch set (`scan.py crosscheck mindeg3`) at orders 12–17, where
stock geng's stream (57 / 503 / 6,059 / 91,433 / 1,655,659 / **34,758,006**
graphs) filtered by the `E015` \(C_8\) detector gives the same empty set as
`genc48` — at order 17 that is a 34.8-million-graph independent
re-derivation, and it cost 1,069.6 s against the generator's 59.5 s; and the
**positive control** at minimum degree 3 — the cubic order-24 census, where
the same code path emits exactly the 4 correct graphs. Orders 18 and 19,
where the new information is, have **no** stream-side cross-check: the
order-18 reference stream would be \(\approx8\times10^8\) graphs and the
order-19 one \(\approx2\times10^{10}\).

Cost of pushing further: the tree grows \(\approx7.2\times\) per order, so
order 20 \(\approx3.9\times10^{10}\) nodes \(\approx5.5\) h single-threaded
(\(\approx45\) min on 8 workers with the anchored res/mod split), order 21
\(\approx3\times10^{11}\) \(\approx42\) h (\(\approx5.3\) h on 8). Orders 20–21
are therefore a cheap next leg if the orchestrator wants the counterexample
bound moved; order 24 (where the first cubic examples appear) is
\(\gtrsim10^{14}\) nodes and out of reach for this engine without further
pruning.

## Independent checks

- Full `labelg` **set** equality (not merely counts) with the independent
  `geng | C_8`-filter pipeline at 23 (variant, order) pairs across five class
  variants, all nonzero; plus `genc48`'s own isomorph-freeness asserted at each.
- Every generated graph is re-tested by `power_free` (which tests \(C_4\),
  \(C_8\), \(C_{16}\) with the `E015` detector), independently of geng's `-f`
  and of the plugin; `--verify-all` adds `has_c4` and `has_cycle_len(·,8)`.
- **Second-algorithm spot check** (`scan.py spotcheck`): the full cycle
  spectrum of every class member with at most 4 degree-2 vertices — 115 graphs
  at order 17, 90 at order 16, i.e. every near miss — was recomputed by the
  brute-force cycle enumerator `cycle_spectrum_bruteforce`, which shares no
  code path with `has_cycle_len`; \(4,8\notin\) spectrum in all 205 cases, and
  the \(C_{16}\) verdicts agree exactly.
- res/mod splitting under pruning is verified to be a partition at three
  (order, mod) pairs, and the order-17 16-part total is reproduced by an
  independent unsplit run.
- The cubic order-24 census is set-equal to `E005`'s independently produced
  file and equal to Markström's published Table 3 count — the **positive
  control** for the minimum-degree-3 code path (a nonzero class, at a large
  order, matched exactly).
- **Full filter-the-stream cross-check** (`scan.py crosscheck mindeg3`) on the
  `-c -f -d3` switch set at orders 12–17: stock geng's stream (57 / 503 /
  6,059 / 91,433 / 1,655,659 / 34,758,006 graphs) filtered by the `E015`
  \(C_8\) detector gives exactly `genc48`'s output (both empty) at each
  order; the two instruments are compared as `labelg` canonical sets. The
  order-17 leg is a 34.8-million-graph reproduction and took 1,069.6 s against
  the generator's 59.5 s.
- Orders 14–16 reproduce `C027`'s and `C036`'s emptiness verdicts from a
  different instrument; the primitive suite reproduces `E018`'s named-object
  anchors and `E015`'s Heawood \(C_8\) count.
- The 146-check anchor suite passes under CPython 3.14.2 and PyPy 7.3.23
  before and independently of production.
- Not independently re-implemented: nauty's canonical construction path
  (imported generation layer, anchored as in `E010`–`E018`).
