# E017 — Sharpness certificate for the 2/3 cubic-density bound

- Date: 2026-07-24
- Problem: `P-002`
- Session: `S019` (worker W2)
- Evidence class: certificate-based (single explicit graph, exhaustively checked)

## Question

Attempt `A020` proves (W2-T1) that in an order-then-size minimal counterexample
at least \(2/3\) of the vertices have degree exactly \(3\), using only:

- \(\delta(G)\ge3\);
- Carr's Lemma 0.1 / row `C004`: no proper subgraph of \(G\) has minimum degree
  \(\ge3\) (which subsumes `L002`'s independence of the degree-\(\ge4\) set and
  `C005`'s domination statement);
- \(C_4\)-freeness (the weakest consequence of power-freeness).

**Is \(2/3\) the exact ceiling of that hypothesis set?** Equivalently: does a
finite simple graph exist that satisfies all of the above *and* has exactly
\(2/3\) of its vertices of degree \(3\)? If yes, no argument using only those
hypotheses can prove a better constant, and every further improvement must
consume power-freeness beyond \(C_4\).

The candidate is the explicit 15-vertex graph **S15** of `A020` W2-T7, on
\(\mathbb{Z}_5\)-indexed vertices \(a_i,a'_i\) (intended degree 3) and \(b_i\)
(intended degree 4), with edges

```
a_i a'_i ,   a_i b_i ,   a'_i b_i ,   a_i b_{i+1} ,   a'_i b_{i+2}      (i in Z_5)
```

15 vertices, 25 edges.

## Logical scope

Certificate-based and **one-sided by design**. A positive result establishes
exactly one thing: the named hypothesis set does not imply any cubic-density
constant above \(2/3\). It establishes nothing about the Erdős–Gyárfás
conjecture, and S15 is *not* a counterexample to it — S15 contains fifty
8-cycles, which is precisely the hypothesis it fails.

A negative result (some check failing) would refute `A020` W2-T7 and would leave
the \(2/3\) bound possibly improvable by pure counting.

The properties checked are decidable and finite; the run is exhaustive over all
15 vertex deletions, all 25 edge deletions, all 105 vertex pairs, and all simple
cycles. Nothing is sampled.

## Environment

- Tool and version: CPython 3.14.2 and PyPy 7.3.23 (Python 3.11.15); both run to
  completion with identical verdicts.
- Dependencies: Python standard library only (`itertools`, `sys`). No nauty, no
  third-party package, no data file.
- Exact arithmetic / floating point: exact integer and set arithmetic
  throughout; no floating point anywhere.
- Random seed: none; the program is deterministic.

## Inputs and search space

- The single graph S15, constructed in code from the \(\mathbb{Z}_5\) rule above
  (so the definition in `A020` and the object tested are the same text).
- Anchors: \(K_4\), \(K_{3,3}\), \(K_5\), \(C_5\), and the Petersen graph, all
  built in code.
- `no_proper_subgraph_of_min_degree_3` uses the reduction proved in `A020`
  W2-T2: every proper subgraph of \(G\) is contained in \(G-v\) for some vertex
  \(v\) or in \(G-e\) for some edge \(e\); degeneracy is monotone under
  subgraphs; so the property is equivalent to 2-degeneracy of all 15 \(G-v\) and
  all 25 \(G-e\). This is the only pruning used and it is a proved equivalence,
  not a heuristic.
- \(C_4\)-freeness is tested as "maximum codegree \(\le1\)" over all \(\binom{15}{2}=105\)
  vertex pairs, which is equivalent for simple graphs.

## Reproduction

```sh
python3 problems/erdos-gyarfas/experiments/E017-sharpness-certificate-for-the-2-3-cubic-density-bound/verify.py
# and, for the second interpreter:
pypy3 problems/erdos-gyarfas/experiments/E017-sharpness-certificate-for-the-2-3-cubic-density-bound/verify.py
```

Exit status 0 and a final line `all checks passed` is the pass condition; any
failing check is printed with its expected value and forces exit status 1.

## Results

Anchors (11 checks, all passed under both interpreters):

| Anchor | Assertion | Result |
|---|---|---|
| A1 | \(K_4\) cycle counts \(\{3\!:\!4,\ 4\!:\!3\}\), by two independent enumerators | pass |
| A2 | \(K_{3,3}\) cycle counts \(\{4\!:\!9,\ 6\!:\!6\}\), by two independent enumerators | pass |
| A3 | Petersen cycle counts \(\{5\!:\!12,\ 6\!:\!10,\ 8\!:\!15,\ 9\!:\!20\}\) (published values) | pass |
| A4 | degeneracy detector: \(K_4\) and Petersen not 2-degenerate, \(C_5\) 2-degenerate | pass |
| A5 | Lemma 0.1 detector: \(K_5\) fails (its \(K_4\) subgraph), Petersen passes | pass |
| A6 | codegree detector: Petersen has maximum codegree 1 | pass |

S15 certificate (24 checks, all passed under both interpreters; 35 checks in
total with the anchors):

```
n = 15, m = 25
degrees: every a_i, a'_i has degree 3;  every b_i has degree 4
|V_3| = 10 and 3*|V_3| = 2*n exactly           -> the density is exactly 2/3
delta(S15) = 3
V_{>=4} = {b_1..b_5} is independent
every vertex has a neighbour of degree exactly 3
G[V_3] is a perfect matching (5 edges; every V_3-vertex has A-degree 1)
maximum codegree = 1                            -> no 4-cycle
every proper subgraph has minimum degree <= 2   -> Lemma 0.1's conclusion holds
cycle counts by length:
  3:5  5:5  6:15  7:30  8:50  9:65  10:87  11:115  12:110  13:70  14:30  15:8
the only power-of-two cycle length present is 8 (fifty 8-cycles)
e(V_3, V_{>=4}) = 20 = sum of the B-degrees = 2p + q, with (p,q) = (10,0)
the link graph H_1 of A020 W2-T5 is simple with 10 edges: H_1 = K_5
H_1 is not 2-degenerate, and H_1 has fifteen 4-cycles
```

## Interpretation

The narrowest justified conclusion:

> There is a finite simple graph — S15 — with minimum degree 3, no 4-cycle, no
> proper subgraph of minimum degree \(\ge3\), degree-\(\ge4\) vertices forming an
> independent set, every vertex having a neighbour of degree exactly 3, and
> exactly \(2/3\) of its vertices of degree exactly 3.

Consequently the constant \(2/3\) of `A020` W2-T1 **cannot be improved by any
argument that uses only those hypotheses**; this is recorded as `A020` W2-T7.
Since `A020` W2-T6 *does* improve the bound (to \(|V_3|\ge(2n+3)/3\)), the
improvement necessarily consumes power-freeness beyond \(C_4\) — and indeed it
does, through the subdivision descent W2-T5. The last two rows of the
certificate exhibit exactly where S15 fails that descent: its link graph is
\(K_5\), which has 4-cycles, and those lift to 8-cycles of S15.

This experiment supports no claim about the truth of `C001` and no claim about
which graphs are counterexamples. It is a sharpness certificate for a
proof method.

## Independent checks

1. **Two cycle enumerators.** The DFS enumerator used on S15 is cross-checked on
   \(K_4\) and \(K_{3,3}\) against an independent brute-force enumerator that
   ranges over all vertex subsets and all cyclic arrangements; the two agree.
2. **Published anchor.** The DFS enumerator reproduces the Petersen graph's
   cycle census \(\{5\!:\!12,\ 6\!:\!10,\ 8\!:\!15,\ 9\!:\!20\}\).
3. **Two interpreters.** Identical verdicts under CPython 3.14.2 and
   PyPy 7.3.23.
4. **Internal consistency.** \(e(V_3,V_{\ge4})\) is computed twice, once by
   summing over \(V_3\) and once by summing the degrees of \(V_{\ge4}\), and
   once more via the identity \(2p+q\) of `A020` W2-T0; all three agree at 20.
5. **Hand check available.** S15 has the automorphism
   \(a_i\mapsto a_{i+1},\ a'_i\mapsto a'_{i+1},\ b_i\mapsto b_{i+1}\), so its
   15 vertices fall into 3 orbits and its 25 edges into 5 orbits. The
   Lemma 0.1 property therefore reduces to 3 vertex deletions and 5 edge
   deletions, each a short peeling — checkable by hand, as sketched in `A020`
   W2-T7. The \(C_4\)-freeness has a one-paragraph hand proof there as well.
   The full cycle census is the only part for which the machine run is the
   practical evidence, and no deduction in `A020` depends on it beyond the
   single fact that an 8-cycle exists (which is exhibited explicitly in
   `A020`).
