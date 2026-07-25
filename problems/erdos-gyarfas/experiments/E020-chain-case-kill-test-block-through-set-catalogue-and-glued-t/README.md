# E020 — chain-case kill test: block through-set catalogue and glued two-block witnesses for the case-5b cut-vertex constraint system

- Date: 2026-07-24
- Problem: `P-002`
- Evidence class: exhaustive finite exclusion at the stated block orders
  (the kill search) + exact instance calibration (anchors) + descriptive
  frontier data. Serves attempt `A022` (session `S021`, worker leg W1).
- Owner: session `S021`.

## Question

The case-(5b) residual object (`L041`/`L042`, standing hypothesis (R))
with a cut vertex in \(H=B-u\) is a chain of blocks whose through-sets
are forced into the constraint system assembled in `A022`: at every cut,
the prefix and suffix through-sets meet \(\mathbb P-2\) (`A019` W1-T14;
bridge variant \(\mathbb P-1\)) and — by `A022`'s closure batteries —
also meet \((\mathbb P-1)\cup\{1\}\) and \(\mathbb P\cup\{1,2\}\), while
the total \(S\) avoids \(\mathbb P-2\) and meets both \(\mathbb P\) and
\(\mathbb P-1\).

**Pre-registered kill condition (S021 brief, carried from S020's
checkpoint):** exhibit a vertex-taut \(C_4\)-free two-terminal graph
*with a cut vertex*, exactly two degree-2 vertices (the terminals),
power-freeness dropped, realizing the full forced constraint system.
Such a witness would be the chain-case analogue of Petersen\(-e\)
(`C037`) and would kill arithmetic-only exclusion of the chain case.

Constraint levels tested on a candidate witness:

- **L1 "kill"** — the pre-registered system (W1-T14 memberships at every
  cut + total avoidance/memberships + the structural frame: profile,
  \(C_4\)-free, taut, expected cut vertices).
- **L2 "ext"** — adds `A022`'s closure constraints at every cut
  (\((\mathbb P-1)\cup\{1\}\) and \(\mathbb P\cup\{1,2\}\) memberships
  for every prefix and suffix).
- **L3 "full"** — adds the saturation batteries (Mersenne and power
  saturation at the terminals, cut-vertex Mersenne/power saturation on
  non-bridge sides, and the \(d\ge3\) total-saturation batteries where
  applicable).

## Logical scope

1. The block catalogue is **exhaustive** for: 2-connected \(C_4\)-free
   graphs with at most two degree-2 vertices and all other degrees
   \(\ge3\), at orders \(\le13\) over **all** admissible terminal pairs,
   and at order 14 restricted to the **exactly-two-degree-2 profile**
   (its unique terminal pair). Order-14 blocks with one or zero degree-2
   vertices and all blocks of order \(\ge15\) are *not* catalogued
   (CPython budget); the negative result below is scoped accordingly.
2. The kill search is exhaustive over chains assembled from catalogued
   blocks with \(m\le3\) blocks: [end,end], [end,bridge,end],
   [end,mid,end]. Chains with \(m\ge4\) blocks are not searched (no
   realized \(m\le3\) sub-pattern exists to seed them, but this is not a
   proof of \(m\ge4\) emptiness — recorded as a scope hole).
3. Power-freeness is deliberately dropped throughout (as in `E016` A6 /
   `E018` mod4): the catalogue measures what the degree profile,
   \(C_4\)-freeness, 2-connectivity and tautness force, so a hit would
   kill exactly the arithmetic-only route. Emptiness here proves nothing
   about block orders \(\ge15\) and nothing about the real (power-free,
   order-\(\ge16\)) blocks.

## Environment

- nauty 2.9.3 (`geng` from `/opt/homebrew/bin`); CPython 3.14.2 for all
  runs (no PyPy needed at these orders). macOS / darwin 25.5.0, arm64.
- Standard library only; integer bitmask arithmetic; no floating point in
  any verdict path; no randomness.
- Graph primitives copied verbatim from `E018/scan.py` (there from
  `E015/bipscan.py`, anchored against the independent `E010` pipeline);
  `paths_with_essential` copied verbatim from `E018/mod4.py`. All
  re-anchored here (12-check suite) before use.

## Inputs and search space

- Stream per order: `geng -q -c -f -d2 n mine:maxe` with
  `mine` \(=\lceil(3n-2)/2\rceil\) (degree sum \(\ge4+3(n-2)\), valid for
  every \(\le2\)-degree-2 min-degree-2 profile) and `maxe`
  \(=\binom n2\). Filters: \(\le2\) vertices of degree 2 → 2-connected
  (no cut vertices) → per terminal pair: vertex-tautness and the exact
  through-set by simple-path enumeration with the essential-vertex mask.
  Terminal pairs: the unique degree-2 pair (two-degree-2 blocks); the
  degree-2 vertex against all others (one-degree-2); all pairs
  (zero-degree-2).
- End-usable block: a catalogued taut pair with at least one terminal of
  block-degree exactly 2 (that terminal is the chain terminal \(a\) or
  \(b\); forced by \(\deg_H(a)=2\), `A022` W1-T1). Mid-usable: any
  catalogued taut pair.
- Pair/triple search over **distinct realized through-sets** with bitmask
  arithmetic; candidate chains would then be **glued** (vertex
  identification at the cut, or a bridge edge) and every constraint
  re-verified directly on the glued graph (`analyze_witness`),
  independently of the set-level search.

## Reproduction (from the repository root)

```sh
python3 problems/erdos-gyarfas/experiments/E020-chain-case-kill-test-block-through-set-catalogue-and-glued-t/blocks.py anchors
python3 problems/erdos-gyarfas/experiments/E020-chain-case-kill-test-block-through-set-catalogue-and-glued-t/blocks.py catalogue 4 5 6 7 8 9 10 11 12
python3 problems/erdos-gyarfas/experiments/E020-chain-case-kill-test-block-through-set-catalogue-and-glued-t/blocks.py catalogue 13
python3 problems/erdos-gyarfas/experiments/E020-chain-case-kill-test-block-through-set-catalogue-and-glued-t/blocks.py catalogue 14 --two-only
python3 problems/erdos-gyarfas/experiments/E020-chain-case-kill-test-block-through-set-catalogue-and-glued-t/blocks.py search
```

Outputs land in `data/` (`catalogue_n*.json`, `search_results.json`).

## Results

**Anchors (12 checks, all pass).** \(K_4\); \(K_{3,3}-e\) (\(S=\{3,5\}\),
spectrum \(\{4,6\}\)); Petersen (spectrum \(\{5,6,8,9\}\)); Petersen\(-e\)
(\(S=\{4,5,7,8\}\), taut, 2-connected, non-bipartite); the `A014` T5
composite rebuilt by `glue_bridge` from two Petersen\(-e\) blocks (order
20, \(S=\{9,\dots,17\}\), spectrum \(\{5,6,8,9\}\), cuts exactly the
bridge ends, taut, Minkowski identity \(S=A+Z\) verified at both cuts);
`chain_eval` and the graph-level verifier agree that the composite fails
the chain system at exactly the recorded points (`A022` W1-T9); the
collision arithmetic \(((\mathbb P-2)+(\mathbb P-2))\cap(\mathbb
P-2)=\emptyset\) and the same-exponent collisions; graph6 encode/decode
roundtrip.

**Block catalogue.**

| n | geng stream | \(\le2\) deg-2 | exactly-two | 2-connected | taut pairs | end-usable |
|---|---|---|---|---|---|---|
| 4–7 | 0 | 0 | 0 | 0 | 0 | 0 |
| 8 | 5 | 1 | 1 | 1 | 1 | 1 |
| 9 | 10 | 3 | 2 | 3 | 10 | 10 |
| 10 | 198 | 31 | 22 | 31 | 283 | 58 |
| 11 | 885 | 178 | 125 | 177 | 1,059 | 564 |
| 12 | 13,759 | 1,497 | 1,139 | 1,478 | 8,193 | 4,431 |
| 13 | 111,379 | 14,580 | 10,966 | 14,467 | 87,419 | 48,185 |
| 14* | 1,706,820 | 175,648 | 130,461 | 129,654 | 129,654 | 129,654 |

\* order 14 restricted to the exactly-two-degree-2 profile (2-connected
and taut-pair counts refer to that profile only). Runtimes (CPython,
single worker): \(\le13\) s per order through 13; 82.7 s at 14.

Calibration hits: the exactly-two-degree-2 counts 1, 2, 22, 125, 1,139,
10,966, 130,461 at orders 8–14 equal the recorded `E016` A6 / `E018` /
`C036` class counts at every order. The streams at orders 4–7 are empty:
**no block exists below order 8**; the unique order-8 block is `GCpdag`
(terminals its two degree-2 vertices, \(T=\{3,4,5,6,7\}\)).

**Fan corroboration.** Every terminal pair of every 2-connected
catalogued block was vertex-taut — 226,619 taut pair instances at orders
8–14 equal the number of pairs tested, zero exceptions (at order 10 all
\(22\cdot1+4\cdot9+5\cdot45=283\) admissible pairs appear). This is the
standard 2-fan fact (`A022` W1-T1 remark): a 2-connected two-terminal
graph is always vertex-taut.

**The kill search: empty at every level.**

| chain shape | set-level search space | passing L1 (kill) | passing L2 (ext) |
|---|---|---|---|
| [end, end] (\(m=2\)) | 9,045 unordered pairs (134 distinct end-\(T\) meeting \(\mathbb P-2\), of 166 end-\(T\) total) | **0** | 0 |
| [end, bridge, end] | same pair space | **0** | 0 |
| [end, mid, end] | those pairs × 176 distinct mid-\(T\) | **0** | 0 |

No glued witness was ever constructed because no set-level candidate
passed. **The pre-registered kill condition did not fire at these block
orders.**

**The failure mechanism is single-point.** Over all 9,045 unordered
pairs of realized end through-sets meeting \(\mathbb P-2\) (through
order 14): every pair's Minkowski sum meets \(\mathbb P-2\), and in
**every single case it contains 14** \(=2^4-2\) (6 is also hit in 6,710
pairs, 2 in 1,378; 30 in none — the maximum reachable sum is
\(13+13=26<30\)). The totals' \(\mathbb P\)/\(\mathbb P-1\) memberships
never got to act. Realized end through-sets at these orders are fat
near-intervals reaching \(\max T=n-1\); the only order-14 set meeting
\(\mathbb P-2\) that avoids both 7 and 8 is \(\{1,5,6,9,10,11,12,13\}\),
and its element 1 pairs with 13 into 14. So at block orders \(\le14\)
the two constraints "each side meets \(\mathbb P-2\)" (`A019` W1-T14)
and "the total avoids \(\mathbb P-2\)" are *jointly unsatisfiable over
realized through-sets* — the forbidden sum 14 is the sole binding site.

**The abstract frontier (machine-verified set arithmetic; no
realizability claim).** The safe zone \([15,29]\) between 14 and 30 has
width 15, so the arithmetic first admits solutions one order past the
catalogue:

- \(T_1=\{7,8,12,13,14\}\) (needs a block of order \(\ge15\)) with
  \(T_2=\{8,11,12,13,14,15\}\) (order \(\ge16\)) passes **kill and ext**
  levels: \(S=\{15,16,18,\dots,29\}\) avoids \(\mathbb P-2\), meets
  \(\mathbb P\) at 16 and \(\mathbb P-1\) at 15, and every per-side
  membership holds with exponent-disjoint witnesses (Mersenne exponents
  3 vs 4, power/\(\mathbb P-2\) exponent crossings 3 vs 4 — exactly the
  dodging pattern `A022` W1-T6 forces).
- \(T=\{6,9,10,11,12,13\}\) against itself (an order-\(\ge14\) block
  shape with a gap over \(\{7,8\}\); not realized at \(\le14\)) passes
  the pre-registered kill level and fails ext (no Mersenne, no power,
  no 1 or 2 in \(T\)).

So the next falsifiable rung for the kill question is the order-15/16
block catalogue ((2,2)-profile first, under PyPy), testing whether
\(\{7,8,12,13,14\}\)-shaped through-sets are realized.

## Interpretation

Narrowest justified conclusions:

1. No vertex-taut \(C_4\)-free two-degree-2 chain witness for the
   case-(5b) cut-vertex constraint system — at any of the three levels,
   even the pre-registered one — can be assembled from blocks of order
   \(\le13\) (any profile) together with order-14 blocks of the
   exactly-two-degree-2 profile, in chains of \(m\le3\) blocks. In this
   range the kill condition is **refuted**, with a single identified
   mechanism (the forced 14 in the pairwise Minkowski sum).
2. Every vertex-taut member of the (5b) terminal profile class with a
   cut vertex is a chain of blocks of order \(\ge8\) (`A022`
   W1-T1/W1-T10), so no such member exists below order 15 — which
   retro-explains `C037`'s observation that all sixty membership-triple
   witnesses at orders 10–13 are 2-connected, and predicts the exact
   coincidence of cut-vertex and non-taut counts in `E018`'s class data
   (0/1/19/113 at orders 10–13, matching class minus taut exactly).
3. The kill question itself remains **open**: the arithmetic admits
   near-interval solutions from block orders 15–16 on, and nothing here
   bears on the real residual object, whose blocks have order \(\ge16\)
   and are power-free.

## Independent checks

- The catalogue chain reproduces the recorded exactly-two-degree-2 class
  counts (`E016` A6 / `E018` / `C036`) at every order 8–14 from an
  independently written driver.
- The `A014` T5 composite is rebuilt by the gluing machinery and matches
  its recorded order, through-set, spectrum, cut vertices and tautness
  (`E013` anchor A9 data), and the set-level and graph-level constraint
  evaluators agree on its failure pattern.
- `paths_with_essential` / `path_lengths` are the `E018`-anchored
  enumerators; the 12-anchor suite passes before every production run.
- The glued-witness verifier recomputes prefixes, suffixes and the
  Minkowski identity from the graph alone (never trusting the set-level
  search); on the composite anchor both agree.
- The coincidence "cut vertex \(\Leftrightarrow\) non-taut" predicted by
  the chain floor was checked against `E018/data/mod4_n{10..13}.json`
  (independent data produced for `A021`).
- Not independently re-implemented: geng itself (imported generation
  layer, anchored as in `E010`–`E018`).
