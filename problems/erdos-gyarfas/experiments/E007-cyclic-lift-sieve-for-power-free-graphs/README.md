# E007 — Cyclic-lift sieve for power-free graphs

- Date: 2026-07-23
- Problem: `P-002`
- Evidence class: exact walk-class enumeration (DP over arcs × cycle-space
  vectors), exhaustive hyperplane sieve over voltage assignments, exhaustive
  detector ground truth at orders 12–30, and exact cycle counts on the four
  verified order-24 extremal graphs
- Supports: attempt `A008` (lemmas L019–L021), claims `C019`–`C021`

## Question

Attempt A008 asks whether a cyclic voltage lift of a small base multigraph
of minimum degree at least \(3\) can avoid every power-of-two cycle length
up to its order — which would make it a counterexample to `C001`. By Lemma
L019, a lift of \(B\) over \(\mathbb{Z}_m\) with gauge-fixed assignment
\(x\in(\mathbb{Z}_m)^\mu\) is *certified* free of \(L\)-cycles when no
vector in \(V_L(B)\) (the cycle-space vectors of tailless non-backtracking
closed walks of length \(L\)) satisfies \(\nu\cdot x\equiv0\pmod m\);
lengths \(1,2\) encode simplicity of the lift. Which \((B,m,x)\) survive,
and what do the actual lifts contain at the open orders?

## Inputs and search space

All three multigraph bases of cycle rank \(\mu=2\) with minimum degree
\(\ge3\) (a complete list: \(\mu=2\) and \(\delta\ge3\) force
\(|V|\le2\)) plus three canonical simple cubic bases:

| base | vertices | edges | \(\mu\) | lift family |
|---|---|---|---|---|
| `bouquet2` | 1 | two loops | 2 | circulants \(C_m(a,b)\) |
| `theta3` | 2 | three parallel | 2 | bipartite cyclic Haar-type |
| `dumbbell` | 2 | bridge + two loops | 2 | I-graphs / generalized Petersen type |
| `k4` | 4 | \(K_4\) | 3 | — |
| `prism` | 6 | \(K_3\square K_2\) | 4 | — |
| `k33` | 6 | \(K_{3,3}\) | 4 | — |

Voltage space after L020 gauge fixing: \((\mathbb{Z}_m)^\mu\), all
assignments, no sampling. Sieved lengths: \(\{1,2\}\) (simplicity) and all
powers of two up to the stated `lmax`. Truth census: all lift orders in
\([12,30]\), all assignments, both parities of \(m\).

## Results

**1. Walk-class tables and the zero-vector kill.** `|V_L|` per base, with
"zero" marking \(0\in V_L\) (an integer-zero vector: net voltage zero
under *every* abelian assignment of *every* order — Lemma L021's
obstruction, realized):

| base | \(V_4\) | \(V_8\) | \(V_{16}\) | \(V_{32}\) | \(V_{64}\) | \(V_{128}\) | first zero |
|---|---|---|---|---|---|---|---|
| bouquet2 | 21 zero | — | — | — | — | — | **4** |
| dumbbell | 8 | 33 zero | 213 zero | 949 zero | 3957 zero | 16117 zero | **8** |
| theta3 | 12 | 54 | 217 zero | 817 zero | 3169 zero | 12481 zero | **16** |
| k4 | 6 | 24 | 281 zero | 1965 zero | — | — | **16** |
| prism | 6 | 40 | 579 zero | 8319 zero | — | — | **16** |
| k33 | 18 | 90 | 1242 | 16489 zero | — | — | **32** |

Zero-vector witness walks were reconstructed and stored verbatim in
`data/zero-vector-witnesses.txt`; the dumbbell witness is exactly the
commutator \([\,b\,l_1\,\bar b,\;l_0\,]\) of A008's Lemma L021.
Consequence: for each base, every \(m\) with \(n_B\,m\ge\) (first zero
length) is certificate-dead outright; only finitely many small \(m\)
remain per base.

**2. Sieve verdict — every cyclic group, every assignment, no survivor.**
The remaining small-\(m\) windows were sieved exhaustively (both parities;
`data/sieve-completions-small-even-m.txt`), and independently the odd
range \(m\le127\) in full for theta3 and dumbbell (orders to 254;
`data/sieve-theta3-odd-m-3-127.txt`, `data/sieve-dumbbell-odd-m-3-127.txt`)
and \(m\le15\) for k4 (`data/sieve-k4-odd-m-3-15.txt`). **Zero surviving
assignments anywhere.** Combined with the zero-vector kill, the
certificate verdict covers every \(m\ge2\) for all six bases (`C020`).

**3. Truth-level census at the open orders.** For every base and every
\(m\) with lift order in \([12,30]\) — all assignments, both parities,
simple lifts only — actual presence of \(C_4/C_8/C_{16}\) was tested with
the validated `E004` detectors (`data/truth-census-orders-12-30.txt`).
**Every simple lift contains a \(C_4\), \(C_8\), or \(C_{16}\)**; at
orders \(\le30\) these are the only power lengths \(\le\) order, so no
counterexample to `C001` exists anywhere in the cyclic-lift universe of
these six bases through order 30 (`C021`). Notables: every simple
circulant \(C_m(a,b)\), \(m\le30\), contains a \(C_4\) (the abelian
commutator made concrete); the 48 \(K_4\)-lifts at \(m=7\) (order 28)
avoiding both \(C_4\) and \(C_8\) all contain \(C_{16}\) — the lift
construction lands squarely in Markström's near-miss class (`C014`).

**4. Calibration of the order-24 extremal graphs.** Exact 16-cycle counts
for the four verified extremal graphs (`C018`): \(315/330/207/228\)
sixteen-cycles; every edge lies on at least \(70\) of them; no edge (a
fortiori no vertex) lies on all (`data/calibration-order24-c16.txt`,
`C019`). The \(C_{16}\) obstruction at the extremal boundary is massively
redundant — local surgery cannot remove it.

## Logical scope

The sieve verdict (`C020`) concerns the L019 *certificate*: no cyclic
voltage assignment on these six bases can be walk-certified power-free.
It does not by itself prove that every such lift *contains* a power
cycle. The truth census (`C021`) is stronger but finite: at orders 12–30
every simple lift genuinely contains \(C_4\), \(C_8\), or \(C_{16}\);
this is exhaustive for the stated families, exact, and not sampled.
Neither result bears on non-abelian voltage groups, on other bases, or on
`C001` beyond the stated families; the zero-vector mechanism is
abelianization-specific and vanishes over non-abelian groups, which is
exactly why those are the successor tool (obligation `G012`).

## Method and code

`lifts.py`, standard library only. Components: base multigraphs with arcs
and BFS-tree gauge fixing (L020); `walk_vectors` — exact DP over states
(arc, partial cycle-space vector), start arcs restricted to non-tree arcs
(a tailless nb closed walk cannot lie in a forest, and the tailless
condition is rotation-invariant); `sieve` — per-vector solution
enumeration marking \(\nu\cdot x\equiv0\) hyperplanes in
\((\mathbb{Z}_m)^\mu\); `build_lift`/`verify_lift` — explicit derived
graphs checked with `E004` detectors plus 2-connectivity and girth;
`truth_census` — exhaustive detector runs; `calibrate` — canonical
per-direction cycle counting (each cycle counted from its minimum vertex,
both directions, halved).

## Environment

- Tool and version: CPython 3.14.2 (anchors, calibration) and PyPy 7.3.23
  / Python 3.11.15 (anchors re-run, all sieve and truth legs); macOS
  26.5.1 arm64
- Dependencies: Python standard library; detectors imported from the
  validated `E004` module; graph6 codec from `e005lib` (unused in the
  main legs)
- Exact arithmetic / floating point: exact integer arithmetic throughout
- Random seed: none (fully deterministic)

## Reproduction

```sh
python3 lifts.py anchors
pypy3   lifts.py anchors
python3 lifts.py calibrate
pypy3   lifts.py sieve theta3 3 127 --lmax 128
pypy3   lifts.py sieve dumbbell 3 127 --lmax 128
pypy3   lifts.py sieve k4 3 15 --lmax 32
pypy3   lifts.py sieve theta3 2 7 --all-m --lmax 8      # small-m closure
pypy3   lifts.py sieve dumbbell 2 3 --all-m --lmax 4
pypy3   lifts.py sieve k4 2 3 --all-m --lmax 8
pypy3   lifts.py sieve prism 2 2 --all-m --lmax 8
pypy3   lifts.py sieve k33 2 5 --all-m --lmax 16
pypy3   lifts.py sieve bouquet2 2 3 --all-m --lmax 4
pypy3   lifts.py vectors dumbbell 8                     # witnesses
pypy3   lifts.py vectors theta3 16
pypy3   lifts.py vectors k4 16
pypy3   lifts.py vectors k33 32
pypy3   lifts.py vectors prism 32
pypy3   lifts.py truth theta3 6 15                      # ground truth
pypy3   lifts.py truth dumbbell 6 15
pypy3   lifts.py truth k4 3 7
pypy3   lifts.py truth prism 2 5
pypy3   lifts.py truth k33 2 5
pypy3   lifts.py truth bouquet2 12 30
```

## Interpretation

The cyclic (and, by the zero-vector mechanism, any abelian) voltage-lift
tool cannot produce a counterexample candidate from any base of cycle
rank 2 or from \(K_4\), \(K_{3,3}\), or the prism: the certificate is
impossible for every \(m\), and at the open orders 18–30 the lifts
themselves all contain short power cycles. This fires kill condition (a)
of A008 for the abelian version of the tool, with the obstruction
identified structurally: commutator words have zero net voltage over
every abelian group and occur at power-of-two lengths (8, 16, 32 on the
tested bases). See A008's failure analysis and obligation `G012` for what
survives: non-abelian voltage groups, where the commutator obstruction
vanishes at its root.

## Independent checks

- A1: theta3 \(V_2\) equals the six parallel-edge patterns, by hand.
- A2: DP `walk_vectors` equals independent brute-force enumeration for
  all lengths \(\le8\) on theta3, dumbbell, bouquet2, k4.
- A3: k4 triangle/quadrilateral classes exclude the zero vector and are
  negation-symmetric.
- A4: bouquet2 has the commutator zero vector at length 4, with a
  reconstructed witness walk of length 4.
- A5: the dumbbell lift \(m=5\), \(x=(1,2)\) is the Petersen graph
  (order 10, cubic, 2-connected, girth 5, no \(C_4\), has \(C_8\)), and
  the \(C_8\) shows as an L019 hyperplane hit at length 8.
- A6: the theta3 lift \(m=3\), \(x=(1,2)\) is \(K_{3,3}\) (bipartite, has
  \(C_4\)), with the matching hyperplane hit at length 4.
- A7: the zero assignment on k4 over \(\mathbb{Z}_3\) (three disjoint
  \(K_4\)'s, \(C_4\) present) is killed by the sieve.
- A8: sieve marking equals a naive quadratic orthogonality check on
  theta3 at \(m=7\) (prime) and \(m=9,12\) (composite, exercising the
  gcd \(>1\) solution-enumeration paths).
- Cross-experiment consistency: every sieve/truth row at orders \(\le17\)
  returned zero power-free lifts, as `L017`/`L018` require; the k4
  \(m=7\) survivors of \(\{C_4,C_8\}\) at order 28 all contain
  \(C_{16}\), as `C013` requires.
- The soundness direction of L019 is asserted at runtime: any sieve-clean
  lift found to contain a sieved cycle length would raise; none did.
- All anchors pass identically under CPython 3.14.2 and PyPy 7.3.23.
