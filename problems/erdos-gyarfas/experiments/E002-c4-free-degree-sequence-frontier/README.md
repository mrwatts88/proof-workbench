# E002 — C4-free degree-sequence frontier

- Date: 2026-07-23
- Problem: `P-002`
- Evidence class: exploratory

## Question

After imposing every necessary condition proved for an edge-minimal
counterexample—minimum degree \(3\), no \(4\)-cycle, and no edge between two
vertices of degree above \(3\)—do any graphs of order \(9\) or \(10\) also
avoid an \(8\)-cycle? Which degree and neighborhood patterns survive?

## Logical scope

The search is exhaustive for edge-minimal counterexamples at the two stated
orders. Any counterexample can be made edge-minimal without changing its vertex
set, and `A001/L002` proves the high-degree independence condition. Degree
sequences are rejected only by the proved \(C_4\)-free codegree inequality,
parity, or the necessary capacity of a high vertex into the cubic vertices.

The program generates labelled graphs for one fixed nonincreasing placement of
each degree sequence. Any graph can be relabelled into such a placement, so zero
survivors excludes all isomorphism types; the printed graph counts are not
counts of isomorphism classes. This finite result does not prove the universal
conjecture. Independent hand arguments `A002/L005` and `A003/L006` prove the
same order exclusions without using the program.

## Environment

- Tool and version: CPython 3.14.2
- Dependencies: Python standard library only
- Exact arithmetic / floating point: integer bit masks and exact counts
- Random seed: none; deterministic exhaustive backtracking

## Inputs and search space

- Orders \(9\) and \(10\).
- Nonincreasing degree sequences with all degrees at least \(3\), even degree
  sum, and
  \(\sum_v\binom{d(v)}2\le\binom n2\).
- Edges between two target-degree-above-\(3\) vertices are forbidden by
  `L002`.
- The least unfinished vertex receives all its remaining neighbors in one
  backtracking step. Residual parity and capacity prune impossible branches.
- An edge is rejected exactly when it closes an existing path of length \(3\),
  which is equivalent to creating a \(4\)-cycle at that step.
- Complete graphs are checked for connectivity and for a simple \(8\)-cycle.
- The first-neighbor ordering in the cycle search affects duplicate work only,
  not existence.

## Reproduction

```sh
python3 problems/erdos-gyarfas/experiments/E002-c4-free-degree-sequence-frontier/frontier.py 9 10
```

## Results

```text
Python 3.14.2
self-checks passed
n=9: feasible_sequences=2
  degrees=4,3,3,3,3,3,3,3,3 nodes=47006 c4_free=0 connected=0 with_C8=0 avoiding_C8=0
  degrees=4,4,4,3,3,3,3,3,3 nodes=16 c4_free=0 connected=0 with_C8=0 avoiding_C8=0
n=10: feasible_sequences=7
  degrees=3,3,3,3,3,3,3,3,3,3 nodes=4252251 c4_free=937440 connected=937440 with_C8=937440 avoiding_C8=0
    profile=cubic:N0_internal_edges=0 count=211680
    profile=cubic:N0_internal_edges=1 count=725760
  degrees=5,3,3,3,3,3,3,3,3,3 nodes=241213 c4_free=0 connected=0 with_C8=0 avoiding_C8=0
  degrees=4,4,3,3,3,3,3,3,3,3 nodes=227385 c4_free=10080 connected=10080 with_C8=10080 avoiding_C8=0
    profile=4,4:shared_low_neighbours=0 count=10080
  degrees=6,4,3,3,3,3,3,3,3,3 nodes=29 c4_free=0 connected=0 with_C8=0 avoiding_C8=0
  degrees=5,5,3,3,3,3,3,3,3,3 nodes=57 c4_free=0 connected=0 with_C8=0 avoiding_C8=0
  degrees=5,4,4,3,3,3,3,3,3,3 nodes=22 c4_free=0 connected=0 with_C8=0 avoiding_C8=0
  degrees=4,4,4,4,3,3,3,3,3,3 nodes=16 c4_free=0 connected=0 with_C8=0 avoiding_C8=0
```

## Interpretation

No order-\(9\) or order-\(10\) graph satisfies all necessary conditions for an
edge-minimal counterexample. At order \(10\), only cubic graphs and the sequence
\((4^2,3^8)\) survive the \(C_4\)-free generation, and every one has an
\(8\)-cycle. The neighborhood profiles led directly to the structural cases in
`A003/L006`.

This is recorded as tested evidence `C003`. The stronger assertion that every
counterexample has at least eleven vertices is recorded as proved `L006`
because `A002` and `A003` supply independent mathematical arguments.

## Independent checks

- `A002/L005` independently derives and excludes the two order-\(9\) degree
  sequences.
- `A003/L006` independently derives all seven order-\(10\) degree sequences,
  eliminates five by capacity, and explicitly constructs an \(8\)-cycle in
  both surviving structural cases.
- Self-checks distinguish adding an edge across paths of lengths \(2\) and \(3\)
  and verify positive/negative \(8\)-cycle boundary examples.
