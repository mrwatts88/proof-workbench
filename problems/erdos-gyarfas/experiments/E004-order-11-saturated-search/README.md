# E004 — Exhaustive small-order search for {C4,C8}-free minimum-degree-3 graphs

- Date: 2026-07-23
- Problem: `P-002`
- Evidence class: exhaustive per stated order

## Question

Does any graph on \(11\), \(12\), or \(13\) vertices have minimum degree at
least \(3\) while containing neither a \(4\)-cycle nor an \(8\)-cycle? At
orders \(n\le15\) such a graph would be exactly a counterexample to `C001`,
because a \(C_{16}\) needs \(16\) vertices; the subclass in which every
nonedge also has a simple path of length \(3\) or \(7\) is the saturated
form supplied by `A005/L008`, and the program classifies it separately.

## Logical scope

The search is exhaustive for the stated orders. Coverage has two proved
layers, written out in `A006`:

1. Degree sequences: minimum degree \(3\), even degree sum, and the
   \(C_4\)-free codegree bound \(\sum_v\binom{d(v)}2\le\binom n2\) (two
   common neighbours of one pair form a \(C_4\)). No other sequence filter
   is applied. The sequence counts \(12\), \(29\), and \(59\) at orders
   \(11\), \(12\), \(13\) were each re-derived by hand; the order-\(13\)
   hand count initially missed the budget-exact sequence
   \((7,7,4,3^{10})\), whose \(\sum\binom d2\) equals \(\binom{13}2=78\),
   before agreeing at \(59\).
2. Labelled completion: one fixed nonincreasing placement per sequence; the
   least unfinished vertex receives its full remaining neighbourhood; an
   edge is rejected exactly when it closes a simple path of length \(3\) or
   \(7\), equivalently exactly when it would create a \(C_4\) or \(C_8\).
   Leaves are exactly the \(\{C_4,C_8\}\)-free graphs with the target
   degrees, each generated once. Vertex \(0\)'s neighbourhood is canonically
   restricted to per-block prefixes of equal-degree blocks; permutations
   inside blocks fix the placement, so emptiness of the restricted search
   proves emptiness up to relabelling.

Zero survivors at order \(n\le15\) therefore excludes every counterexample
of that exact order. This finite result does not prove the universal
conjecture. The saturation classification never activated because no leaf
existed at the orders searched, so `L008` is not a dependency of the
conclusions drawn so far.

## Environment

- Tool and version: CPython 3.14.2, standard library only
- Exact arithmetic: integer bit masks and exact counts; no floating point
- Random seed: none; deterministic exhaustive backtracking
- Run without interpreter optimization flags, so `assert` checks are live

## Inputs and search space

- Orders \(11\), \(12\), and \(13\) (see Results for the per-sequence node
  counts).
- The whole-graph cycle detector is the one validated in `E001`/`E002`; the
  per-leaf checks re-verify degrees, \(C_4\)-freeness by the independent
  codegree criterion, and \(C_8\)-freeness by the independent whole-graph
  detector, and classify saturation by exact simple-path search across every
  nonedge. At the searched orders no leaf existed, so these re-checks were
  vacuous and correctness rests on the validation anchors below.
- Always-on self-checks: ring-graph cycle detection, exact-length path
  detection, saturation on \(C_5\) (positive), \(C_6\), the cube, and
  \(K_5\) (vacuous positive), the `L016` double-theta graph at \(k=4\)
  (no \(C_4,C_8,C_{16}\); the length-\(15\) witness path present), the
  order-\(11\) sequence list against the hand-derived list, and the
  canonical-neighbourhood restriction in the near-cubic case.

## Reproduction

```sh
python3 problems/erdos-gyarfas/experiments/E004-order-11-saturated-search/saturated.py --validate
python3 problems/erdos-gyarfas/experiments/E004-order-11-saturated-search/saturated.py 11 12 13
```

## Results

Validation anchors:

```text
Python 3.14.2
self-checks passed
V1 n=8 cubic, no rejection: complete=19355 (E001: 19355)
V2 n=10 cubic, C4 rejection only: c4_free=937440 with_C8=937440 no_C8=0 (E002: 937440, 937440, 0)
V3 n=10 cubic, C4 rejection, canonical N(0): c4_free=11160 (expected 937440/84 = 11160)
V4 n=10 cubic, C4+C8 rejection, canonical N(0): leaves=0 (expected 0)
V5 n=8 cubic: incremental C8-free=35 independent C8-free=35 (must agree; >= 35)
validation anchors passed
```

Order 11:

```text
n=11: feasible_sequences=12 symmetry=on
  degrees=4,3,3,3,3,3,3,3,3,3,3 nodes=70175 c4c8_free=0 saturated=0
  degrees=6,3,3,3,3,3,3,3,3,3,3 nodes=3484 c4c8_free=0 saturated=0
  degrees=5,4,3,3,3,3,3,3,3,3,3 nodes=15745 c4c8_free=0 saturated=0
  degrees=7,4,3,3,3,3,3,3,3,3,3 nodes=351 c4c8_free=0 saturated=0
  degrees=6,5,3,3,3,3,3,3,3,3,3 nodes=286 c4c8_free=0 saturated=0
  degrees=4,4,4,3,3,3,3,3,3,3,3 nodes=52438 c4c8_free=0 saturated=0
  degrees=6,4,4,3,3,3,3,3,3,3,3 nodes=1057 c4c8_free=0 saturated=0
  degrees=5,5,4,3,3,3,3,3,3,3,3 nodes=1599 c4c8_free=0 saturated=0
  degrees=5,4,4,4,3,3,3,3,3,3,3 nodes=6986 c4c8_free=0 saturated=0
  degrees=4,4,4,4,4,3,3,3,3,3,3 nodes=34789 c4c8_free=0 saturated=0
  degrees=5,4,4,4,4,4,3,3,3,3,3 nodes=9847 c4c8_free=0 saturated=0
  degrees=4,4,4,4,4,4,4,3,3,3,3 nodes=34889 c4c8_free=0 saturated=0
n=11 totals: nodes=231646 c4c8_free=0 saturated=0
```

Order 12:

```text
n=12: feasible_sequences=29 symmetry=on
  degrees=3,3,3,3,3,3,3,3,3,3,3,3 nodes=3725036 c4c8_free=0 saturated=0
  degrees=5,3,3,3,3,3,3,3,3,3,3,3 nodes=128244 c4c8_free=0 saturated=0
  degrees=7,3,3,3,3,3,3,3,3,3,3,3 nodes=7650 c4c8_free=0 saturated=0
  degrees=4,4,3,3,3,3,3,3,3,3,3,3 nodes=991141 c4c8_free=0 saturated=0
  degrees=6,4,3,3,3,3,3,3,3,3,3,3 nodes=37053 c4c8_free=0 saturated=0
  degrees=8,4,3,3,3,3,3,3,3,3,3,3 nodes=565 c4c8_free=0 saturated=0
  degrees=5,5,3,3,3,3,3,3,3,3,3,3 nodes=46262 c4c8_free=0 saturated=0
  degrees=7,5,3,3,3,3,3,3,3,3,3,3 nodes=477 c4c8_free=0 saturated=0
  degrees=6,6,3,3,3,3,3,3,3,3,3,3 nodes=368 c4c8_free=0 saturated=0
  degrees=5,4,4,3,3,3,3,3,3,3,3,3 nodes=121653 c4c8_free=0 saturated=0
  degrees=7,4,4,3,3,3,3,3,3,3,3,3 nodes=1591 c4c8_free=0 saturated=0
  degrees=6,5,4,3,3,3,3,3,3,3,3,3 nodes=2453 c4c8_free=0 saturated=0
  degrees=5,5,5,3,3,3,3,3,3,3,3,3 nodes=4264 c4c8_free=0 saturated=0
  degrees=4,4,4,4,3,3,3,3,3,3,3,3 nodes=368702 c4c8_free=0 saturated=0
  degrees=6,4,4,4,3,3,3,3,3,3,3,3 nodes=12131 c4c8_free=0 saturated=0
  degrees=5,5,4,4,3,3,3,3,3,3,3,3 nodes=24089 c4c8_free=0 saturated=0
  degrees=6,6,4,4,3,3,3,3,3,3,3,3 nodes=756 c4c8_free=0 saturated=0
  degrees=6,5,5,4,3,3,3,3,3,3,3,3 nodes=2377 c4c8_free=0 saturated=0
  degrees=5,5,5,5,3,3,3,3,3,3,3,3 nodes=6002 c4c8_free=0 saturated=0
  degrees=5,4,4,4,4,3,3,3,3,3,3,3 nodes=69908 c4c8_free=0 saturated=0
  degrees=7,4,4,4,4,3,3,3,3,3,3,3 nodes=3517 c4c8_free=0 saturated=0
  degrees=6,5,4,4,4,3,3,3,3,3,3,3 nodes=4957 c4c8_free=0 saturated=0
  degrees=5,5,5,4,4,3,3,3,3,3,3,3 nodes=13008 c4c8_free=0 saturated=0
  degrees=4,4,4,4,4,4,3,3,3,3,3,3 nodes=322830 c4c8_free=0 saturated=0
  degrees=6,4,4,4,4,4,3,3,3,3,3,3 nodes=17568 c4c8_free=0 saturated=0
  degrees=5,5,4,4,4,4,3,3,3,3,3,3 nodes=35764 c4c8_free=0 saturated=0
  degrees=5,4,4,4,4,4,4,3,3,3,3,3 nodes=76853 c4c8_free=0 saturated=0
  degrees=4,4,4,4,4,4,4,4,3,3,3,3 nodes=327081 c4c8_free=0 saturated=0
  degrees=4,4,4,4,4,4,4,4,4,4,3,3 nodes=183500 c4c8_free=0 saturated=0
n=12 totals: nodes=6535800 c4c8_free=0 saturated=0
```

Order 13:

```text
n=13: feasible_sequences=59 symmetry=on
  degrees=4,3,3,3,3,3,3,3,3,3,3,3,3 nodes=12929660 c4c8_free=0 saturated=0
  degrees=6,3,3,3,3,3,3,3,3,3,3,3,3 nodes=223833 c4c8_free=0 saturated=0
  degrees=8,3,3,3,3,3,3,3,3,3,3,3,3 nodes=17140 c4c8_free=0 saturated=0
  degrees=5,4,3,3,3,3,3,3,3,3,3,3,3 nodes=2554742 c4c8_free=0 saturated=0
  degrees=7,4,3,3,3,3,3,3,3,3,3,3,3 nodes=78845 c4c8_free=0 saturated=0
  degrees=9,4,3,3,3,3,3,3,3,3,3,3,3 nodes=869 c4c8_free=0 saturated=0
  degrees=6,5,3,3,3,3,3,3,3,3,3,3,3 nodes=104891 c4c8_free=0 saturated=0
  degrees=8,5,3,3,3,3,3,3,3,3,3,3,3 nodes=764 c4c8_free=0 saturated=0
  degrees=7,6,3,3,3,3,3,3,3,3,3,3,3 nodes=609 c4c8_free=0 saturated=0
  degrees=4,4,4,3,3,3,3,3,3,3,3,3,3 nodes=9388663 c4c8_free=0 saturated=0
  degrees=6,4,4,3,3,3,3,3,3,3,3,3,3 nodes=277428 c4c8_free=0 saturated=0
  degrees=8,4,4,3,3,3,3,3,3,3,3,3,3 nodes=2313 c4c8_free=0 saturated=0
  degrees=5,5,4,3,3,3,3,3,3,3,3,3,3 nodes=604554 c4c8_free=0 saturated=0
  degrees=7,5,4,3,3,3,3,3,3,3,3,3,3 nodes=3601 c4c8_free=0 saturated=0
  degrees=6,6,4,3,3,3,3,3,3,3,3,3,3 nodes=4300 c4c8_free=0 saturated=0
  degrees=7,7,4,3,3,3,3,3,3,3,3,3,3 nodes=135 c4c8_free=0 saturated=0
  degrees=6,5,5,3,3,3,3,3,3,3,3,3,3 nodes=6548 c4c8_free=0 saturated=0
  degrees=8,5,5,3,3,3,3,3,3,3,3,3,3 nodes=459 c4c8_free=0 saturated=0
  degrees=7,6,5,3,3,3,3,3,3,3,3,3,3 nodes=555 c4c8_free=0 saturated=0
  degrees=6,6,6,3,3,3,3,3,3,3,3,3,3 nodes=1593 c4c8_free=0 saturated=0
  degrees=5,4,4,4,3,3,3,3,3,3,3,3,3 nodes=843899 c4c8_free=0 saturated=0
  degrees=7,4,4,4,3,3,3,3,3,3,3,3,3 nodes=19628 c4c8_free=0 saturated=0
  degrees=6,5,4,4,3,3,3,3,3,3,3,3,3 nodes=40994 c4c8_free=0 saturated=0
  degrees=8,5,4,4,3,3,3,3,3,3,3,3,3 nodes=952 c4c8_free=0 saturated=0
  degrees=7,6,4,4,3,3,3,3,3,3,3,3,3 nodes=1021 c4c8_free=0 saturated=0
  degrees=5,5,5,4,3,3,3,3,3,3,3,3,3 nodes=75424 c4c8_free=0 saturated=0
  degrees=7,5,5,4,3,3,3,3,3,3,3,3,3 nodes=3288 c4c8_free=0 saturated=0
  degrees=6,6,5,4,3,3,3,3,3,3,3,3,3 nodes=4703 c4c8_free=0 saturated=0
  degrees=6,5,5,5,3,3,3,3,3,3,3,3,3 nodes=9464 c4c8_free=0 saturated=0
  degrees=4,4,4,4,4,3,3,3,3,3,3,3,3 nodes=3490610 c4c8_free=0 saturated=0
  degrees=6,4,4,4,4,3,3,3,3,3,3,3,3 nodes=129751 c4c8_free=0 saturated=0
  degrees=8,4,4,4,4,3,3,3,3,3,3,3,3 nodes=5167 c4c8_free=0 saturated=0
  degrees=5,5,4,4,4,3,3,3,3,3,3,3,3 nodes=373016 c4c8_free=0 saturated=0
  degrees=7,5,4,4,4,3,3,3,3,3,3,3,3 nodes=7441 c4c8_free=0 saturated=0
  degrees=6,6,4,4,4,3,3,3,3,3,3,3,3 nodes=8094 c4c8_free=0 saturated=0
  degrees=6,5,5,4,4,3,3,3,3,3,3,3,3 nodes=20005 c4c8_free=0 saturated=0
  degrees=5,5,5,5,4,3,3,3,3,3,3,3,3 nodes=88192 c4c8_free=0 saturated=0
  degrees=5,4,4,4,4,4,3,3,3,3,3,3,3 nodes=709099 c4c8_free=0 saturated=0
  degrees=7,4,4,4,4,4,3,3,3,3,3,3,3 nodes=29475 c4c8_free=0 saturated=0
  degrees=6,5,4,4,4,4,3,3,3,3,3,3,3 nodes=61839 c4c8_free=0 saturated=0
  degrees=5,5,5,4,4,4,3,3,3,3,3,3,3 nodes=142644 c4c8_free=0 saturated=0
  degrees=6,5,5,5,4,4,3,3,3,3,3,3,3 nodes=28775 c4c8_free=0 saturated=0
  degrees=5,5,5,5,5,4,3,3,3,3,3,3,3 nodes=103064 c4c8_free=0 saturated=0
  degrees=4,4,4,4,4,4,4,3,3,3,3,3,3 nodes=3407786 c4c8_free=0 saturated=0
  degrees=6,4,4,4,4,4,4,3,3,3,3,3,3 nodes=159119 c4c8_free=0 saturated=0
  degrees=5,5,4,4,4,4,4,3,3,3,3,3,3 nodes=494941 c4c8_free=0 saturated=0
  degrees=6,6,4,4,4,4,4,3,3,3,3,3,3 nodes=11985 c4c8_free=0 saturated=0
  degrees=6,5,5,4,4,4,4,3,3,3,3,3,3 nodes=34591 c4c8_free=0 saturated=0
  degrees=5,5,5,5,4,4,4,3,3,3,3,3,3 nodes=168990 c4c8_free=0 saturated=0
  degrees=5,4,4,4,4,4,4,4,3,3,3,3,3 nodes=719355 c4c8_free=0 saturated=0
  degrees=7,4,4,4,4,4,4,4,3,3,3,3,3 nodes=33049 c4c8_free=0 saturated=0
  degrees=6,5,4,4,4,4,4,4,3,3,3,3,3 nodes=77390 c4c8_free=0 saturated=0
  degrees=5,5,5,4,4,4,4,4,3,3,3,3,3 nodes=180721 c4c8_free=0 saturated=0
  degrees=4,4,4,4,4,4,4,4,4,3,3,3,3 nodes=3467101 c4c8_free=0 saturated=0
  degrees=6,4,4,4,4,4,4,4,4,3,3,3,3 nodes=110370 c4c8_free=0 saturated=0
  degrees=5,5,4,4,4,4,4,4,4,3,3,3,3 nodes=489402 c4c8_free=0 saturated=0
  degrees=5,4,4,4,4,4,4,4,4,4,3,3,3 nodes=428084 c4c8_free=0 saturated=0
  degrees=4,4,4,4,4,4,4,4,4,4,4,3,3 nodes=2077017 c4c8_free=0 saturated=0
  degrees=4,4,4,4,4,4,4,4,4,4,4,4,4 nodes=139113 c4c8_free=0 saturated=0
n=13 totals: nodes=44397061 c4c8_free=0 saturated=0
```

## Interpretation

No graph on \(11\), \(12\), or \(13\) vertices with minimum degree at least
\(3\) avoids both \(C_4\) and \(C_8\). At these orders such a graph would
have been a counterexample outright, so no counterexample of these orders
exists; with `L006` this proves `A006/L017`: every counterexample has at
least fourteen vertices. The saturated subclass was empty a fortiori;
`G009` is settled in this stronger form. Recorded as `C011` (the exhaustive
computation) supporting `L017` (the proved bound). No novelty is claimed:
reported prior computations in the literature exceed these orders.

## Independent checks

- V1 reproduces `E001`'s independent labelled cubic count at order \(8\).
- V2 reproduces `E002`'s independent \(C_4\)-free count at order \(10\) and
  its finding that every such graph contains a \(C_8\), exercising the
  whole-graph \(C_8\) detector on \(937{,}440\) graphs.
- V3 confirms the canonical-neighbourhood restriction by the exact uniform
  quotient \(937{,}440/\binom93=11{,}160\).
- V4 confirms incremental \(C_8\) rejection agrees with V2's leaf
  classification when the true count is zero.
- V5 is the positive control against over-rejection: on order-\(8\) cubic
  graphs, where \(C_8\)-free graphs exist, incremental rejection and
  independent whole-graph classification agree exactly, at \(35\) graphs,
  which is also the hand-computed number of labelled copies of
  \(K_4\sqcup K_4\).
- The self-check suite ties the path detector to the hand-proved `L016`
  double-theta graph from `A005`.
