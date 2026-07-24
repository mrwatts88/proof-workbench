# E018 — order-16 G-profile scan: stream-level power-free search over the two-degree-2-vertex C4-free class

- Date: 2026-07-24
- Problem: `P-002`
- Evidence class: exhaustive finite exclusion (primary instrument) +
  descriptive kill-test data with power-freeness dropped (second
  instrument, `mod4.py`, serving attempt `A021`)
- Owner: session `S020`

## Question

Two questions, one per instrument.

1. **`scan.py` (primary; `L041`'s decisive order).** Does the class
   \(\mathcal G\) of `L039` have a member of order 16? Graph part of the
   class: connected, \(C_4\)-free, exactly two vertices of degree 2
   (call them \(a,b\)), all other degrees \(\ge3\), **power-free** (no
   \(C_4/C_8/C_{16}\) at this order); membership additionally requires
   the through-set condition \(S(H,a,b)\cap\{2,6,14\}=\emptyset\)
   (\(\mathbb P-2\) truncated to path lengths \(\le15\)). `C027` stops
   at order 15 and `C035` is pair-level only, so order 16 was the open
   decisive order: a hit satisfying the \(S\)-condition is the reduct of
   a tight 1-atom of order 17 and **disproves statement 0.1** (`L025`
   R4); emptiness lifts `L041`'s tight-1-atom order bound from \(\ge17\)
   to \(\ge18\).
2. **`mod4.py` (kill test for `A019` exit item 2, attempt `A021`).**
   Among vertex-taut members of the same terminal profile at orders
   10–13 with power-freeness dropped, is the residual object's forced
   membership triple (\(S\cap\mathbb P\ne\emptyset\),
   \(S\cap(\mathbb P-1)\ne\emptyset\), \(S\cap(\mathbb P-2)=\emptyset\))
   realizable, and do its realizations carry any mod-4 confinement of
   \(S\)?

## Logical scope

1. The scan is **exhaustive for the stated class at order 16** modulo
   the generation layer: every \(\mathcal G\)-candidate of order 16 is
   connected, \(C_4\)-free (power-free \(\Rightarrow\) \(C_4\)-free),
   has minimum degree 2, and has \(\ge23\) edges (degree sum
   \(\ge4+3\cdot14=46\)), hence lies in the stream
   `geng -q -c -f -d2 16 23:120`. Emptiness is a finite exclusion at
   order 16 for this profile; it proves nothing at order \(\ge17\) and
   nothing pair-level beyond the profile. It does **not** consume the
   \(S\)-condition (no survivor ever reached that filter).
2. The mod-4 probe is descriptive frequency data with power-freeness
   dropped; it can fire a pre-registered kill condition (it did) but
   proves no universal statement. It is `A021`'s instrument, in the
   same role `E016` A6 played for `A019` W1-T12.

## Environment

- nauty 2.9.3 (`geng`, `labelg` from `/opt/homebrew/bin`); PyPy 7.3.23
  (Python 3.11.15) for all production runs; CPython 3.14.2 additionally
  for the anchor suite (both interpreters pass all 26 anchors).
  macOS 15 / darwin 25.5.0, arm64, 12 cores.
- Standard library only; integer bitmask arithmetic throughout; no
  floating point except wall-clock timings; no randomness.
- Graph primitives (`g6_decode`, `degrees`, `has_c4`, `bfs_dist`,
  `has_cycle_len`, `count_cycles_len`, `cycle_spectrum_bruteforce`,
  `power_free`, `bipartition`) copied verbatim from `E015/bipscan.py`,
  where they are anchored against the independent `E010` pipeline and
  the recorded spectra of `CLAIMS.md`; `path_lengths` is `E016`'s
  enumerator rewritten on bitmasks and re-anchored here (see below).
- Contention note (`process/concurrency.md`): the production run shared
  the machine with an interactive browser session (~2–3 cores); 8
  workers were used, leaving headroom. Timings below are comparable-run
  wall/CPU figures, not clean-machine benchmarks.

## Inputs and search space

- Stream: `geng -q -c -f -d2 16 23:120 r/24`, \(r=0,\dots,23\)
  (`mine` \(=\lceil(3n-2)/2\rceil=23\); `maxe` \(=\binom{16}2\) is
  coverage-safe — geng itself tightens it to 33, and the Reiman bound
  \(m\le n(1+\sqrt{4n-3})/4=35.2\) independently guarantees no
  \(C_4\)-free graph above 35 edges; maximum edge count actually seen:
  31).
- Filter chain, cheapest first: degree profile (exactly two 2s, rest
  \(\ge3\)) → contains a \(C_8\)? → contains a \(C_{16}\)? → full
  survivor analysis (independent `power_free` re-check including
  \(C_4\), spectrum, \(S(H,a,b)\), \(\mathcal G\)-membership,
  bipartiteness, cut vertices).
- `--stats` additionally counts \(C_8\)s per profile member
  (`count_cycles_len`, no early exit) for the min-\(C_8\) statistic.
- Calibration orders 8–15 use the identical chain (plus per-member
  \(C_8\) counting); the mod-4 probe (`mod4.py`) adds an
  essential-vertex mask to the path enumeration (vertex-taut iff the
  mask is full) and tabulates memberships × residues.

## Reproduction

```sh
python3 scan.py anchors     # 26 checks, CPython
pypy3   scan.py anchors     # 26 checks, PyPy
pypy3   scan.py calibrate 8 9 10 11 12 13   # asserts E016 A6 equality
pypy3   scan.py calibrate 14 15             # new orders; C027 predicts empty
sh run16.sh                                 # 24 parts, 8 concurrent workers
pypy3   scan.py harvest 16 24               # merge, assert, verdict
pypy3   mod4.py 10 11 12 13                 # the A021 kill test
geng -u -c -f -d2 16 23:120                 # independent stream count
```

Outputs land in `data/` (`calibrate_n*.json`, `scan_n16_part*of24.json`,
`scan_n16_harvest.json`, `mod4_n*.json`).

## Results

**Anchors (26 checks, both interpreters).** \(K_4\), \(K_{3,3}-e\)
(spectrum \(\{4,6\}\), \(S=\{3,5\}\)), Petersen (spectrum
\(\{5,6,8,9\}\), 12 pentagons, 10 hexagons), Petersen\(-e\)
(\(S=\{4,5,7,8\}\), profile pair caught, \(C_8\)-blocked), the
2-closure of Petersen\(-e\) (spectrum \(\{5,\dots,10\}\), not
power-free — `L039`'s prediction from \(6\in S+2\)); `path_lengths`
agrees with the recursive `E016` reference on all 19,593 vertex pairs
of the 965 connected graphs of orders 6–7; order-8 class = exactly one
graph, not power-free (`E016` A6).

**Calibration (orders 8–15).** Class sizes 1, 2, 22, 125, 1,139,
10,966 at orders 8–13 — **equal to `E016` A6 at every order** — and
130,461 at 14, 1,826,839 at 15 (new data). Every member contains a
\(C_8\); no survivor at any order \(\le15\), independently re-deriving
`C027`'s verdict on this profile. Minimum \(C_8\) count per class:
1, 3, 3, 3, 3, 3, **1**, **2** at orders 8–15. Runtimes (PyPy, single
worker): \(\le0.5\)s through 13, 6.7s at 14, 94.8s at 15.

**Production scan (order 16).**

| quantity | value |
|---|---|
| geng stream (24 parts, disjoint by res/mod) | 346,573,602 |
| profile class (exactly two degree-2, rest \(\ge3\)) | 29,713,305 |
| blocked by a \(C_8\) | 29,713,305 (**100%**) |
| \(C_8\)-free, blocked by \(C_{16}\) only | 0 |
| power-free survivors | **0** |
| \(\mathcal G\)-members at order 16 | **0** |
| minimum \(C_8\) count over the class | **1** |
| maximum edge count seen | 31 (bound 33) |
| CPU (sum over parts) / wall | 2,893.5 s / ~7 min (8 workers) |

The \(C_{16}\) test was never decisive — no profile member of order 16
is even \(C_8\)-free. Part totals and the coverage assertion
(profile = \(C_8\)-blocked + \(C_{16}\)-blocked + survivors) are in
`data/scan_n16_harvest.json`.

**Independent stream count.** `geng -u -c -f -d2 16 23:120` (no
res/mod split) reproduces the summed part total exactly:
`>Z 346573602 graphs generated in 517.83 sec` — the 24-part split is
complete.

**Mod-4 probe (orders 10–13; `A021` T3).** Vertex-tautness is generic
in the profile class (22/22, 124/125, 1,120/1,139, 10,853/10,966).
Taut members realizing the full membership triple: 2 at order 10
(residue sets \(\{0,1,3\}\)), 0 at 11, 3 at 12 and 55 at 13 (all with
full residue set \(\{0,1,2,3\}\)). All 60 are non-bipartite and
2-connected; no taut member at any probed order has
\(S\subseteq\mathbb P-2\). One order-10 witness is **Petersen minus an
edge** (`labelg` canonical-form equality; spectrum \(\{5,6,8,9\}\)).

## Interpretation

Narrowest justified conclusions:

1. **No power-free graph of order 16 has the two-degree-2-vertex
   profile; a fortiori \(\mathcal G\) has no order-16 member.** With
   `L041`'s case analysis (cases (1)/(3) impossible, (2) \(\ge39\),
   (4) \(\ge20\), (5) needs a \(\mathcal G\)-reduct of order
   \(n_0-1\ge17\)): **every tight 1-atom has order \(\ge18\)**, and
   every \(\mathcal G\)-member has order \(\ge17\). Unconditional (no
   (R) needed), same computational lineage caveats as `C027`/`L022`.
   Ledger row: `C036`.
2. The stream-level emptiness of `C027` now extends to order 16 **for
   this one profile** (the \(\le2\)-sub-cubic class at 16 in full
   remains unscanned; `C035` remains pair-level for the rest).
3. The channel is nonetheless *close* in the crude counting sense: the
   minimum \(C_8\) count over the 29.7M-member class is **1** (orders
   14/15: 1/2) — single-\(C_8\) blocking occurs, in sharp contrast to
   the bipartite class (minimum 13–19 at all orders, `C034`). A
   dedicated \(\{C_4,C_8\}\)-free generator (`G014` item 6) would
   enumerate exactly the survivors of the always-decisive filter and is
   the right instrument from order 17 on.
4. The mod-4 kill condition of `A019` exit item 2 **fired** (ledger row
   `C037`; analysis in `A021`): the forced-membership profile of the
   case-(5b) residual object is realizable by vertex-taut \(C_4\)-free
   cores from order 10 (Petersen\(-e\)), with both admissible residue
   patterns and no invariant — no congruence-type theorem on those
   hypotheses alone can exclude case (5b).

## Independent checks

- The full filter chain reproduces `E016` A6's six class counts exactly
  (orders 8–13) and `C027`'s emptiness verdict on the profile through
  order 15, from an independently written driver.
- `path_lengths` (new bitmask implementation) is verified against the
  `E016` recursive reference on every vertex pair of every connected
  graph of orders 6–7, and against the recorded \(S\)-sets of
  \(K_{3,3}-e\) and Petersen\(-e\).
- Survivor analysis re-checks power-freeness independently of the
  filter chain (including \(C_4\), i.e. not trusting geng `-f`); the
  identity profile = \(C_8\) + \(C_{16}\) + survivors is asserted at
  harvest.
- The geng stream total is reproduced by an independent `geng -u` run
  over the undivided class (no res/mod split).
- The two order-16 verdict-relevant detectors (`has_cycle_len` for
  \(C_8/C_{16}\)) are the `E015` detectors, cross-validated there
  against a brute-force enumerator; the 26-check anchor suite passes
  under both interpreters before and independently of production.
- Not independently re-implemented: geng itself (imported generation
  layer, anchored as in `E010`–`E016`).
