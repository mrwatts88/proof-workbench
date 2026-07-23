# E001 — Small graph and cubic census

- Date: 2026-07-23
- Problem: `P-002`
- Evidence class: exploratory

## Question

Do any labelled simple graphs on at most seven vertices with minimum degree at
least \(3\), or any labelled cubic graphs on at most eight vertices, avoid every
power-of-two cycle available at their order?

## Logical scope

The two stated finite search spaces are exhaustive and use no random sampling.
Their negative result rules out counterexamples only in those spaces. It does not
prove the universal conjecture, and the restriction to cubic graphs at order
eight is not asserted to be a general reduction. The hand proof `A001/L003`
independently proves the stronger statement that every possible counterexample
has at least nine vertices.

## Environment

- Tool and version: CPython 3.14.2
- Dependencies: Python standard library only
- Exact arithmetic / floating point: integer bit masks and exact integer counts
- Random seed: none; enumeration is deterministic

## Inputs and search space

- Every labelled simple graph on \(n=4,5,6,7\) is encoded by a bit mask on the
  \(\binom n2\) possible edges. Masks with too few edges are skipped, and the
  remainder are filtered by the exact degree condition.
- Every labelled cubic graph on even \(n=4,6,8\) is generated once by completing
  all still-undecided neighbors of the least-index unfinished vertex. Residual
  degree and parity checks prune impossible branches.
- A \(4\)-cycle is detected by a pair of vertices with two common neighbors.
  Longer requested cycle lengths are checked by an exact simple-path search.
- Built-in assertions check the detector on the cycle graphs \(C_4,C_6,C_8\).

## Reproduction

```sh
python3 problems/erdos-gyarfas/experiments/E001-small-cubic-graph-census/census.py
```

## Results

```text
Python 3.14.2
cycle-detector self-checks passed
all labelled simple graphs with minimum degree at least 3
n=4: tested=1, cubic=1, avoiding_power_cycle=0
n=5: tested=26, cubic=0, avoiding_power_cycle=0
n=6: tested=1858, cubic=70, avoiding_power_cycle=0
n=7: tested=236926, cubic=0, avoiding_power_cycle=0
all labelled cubic graphs
n=4: tested=1, avoiding_power_cycle=0
n=6: tested=70, avoiding_power_cycle=0
n=8: tested=19355, avoiding_power_cycle=0
```

## Interpretation

No graph in either exact finite search space is a counterexample. This is
recorded as tested evidence `C002`, not as support strong enough to prove a
universal statement.

## Independent checks

- The general graph-mask enumeration and the residual-degree cubic generator
  overlap at orders \(4\) and \(6\), and both count respectively \(1\) and \(70\)
  labelled cubic graphs.
- The mathematical argument `A001/L003` independently excludes every graph of
  minimum degree at least \(3\) through order \(8\); it does not rely on this
  program or on the census counts.
