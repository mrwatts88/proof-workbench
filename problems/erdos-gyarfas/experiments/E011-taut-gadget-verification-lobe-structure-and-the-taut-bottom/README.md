# E011 — Taut-gadget verification: lobe structure and the taut bottom rungs

- Date: 2026-07-24
- Problem: `P-002`
- Evidence class: instance-level verification of proved lemmas (`A012` T2/T3)
  plus an exhaustive small-order survey

## Question

Do the `A012` deductions hold on every real graph in reach, and what do the
taut pinched gadgets actually look like at small orders? Specifically:

- **T3 check:** in the class of connected C4-free graphs with exactly two
  sub-cubic vertices \(a,b\) (degree sum \(\ge3\), taken as terminals — a
  (D)-gadget), every member with \(S=\{1\}\) or \(2\in S\subseteq\{2,3\}\)
  must be **non-taut** (some vertex on no simple \(a\)–\(b\) path). One taut
  member would refute `A012` T3.
- **T2 check:** in every non-taut member, each connected component of the
  inessential vertices must have **exactly one** essential neighbor (its
  lobe attachment) and all its vertices of degree \(\ge3\). One
  two-attachment component would refute the lobe decomposition.
- **T1 scaffolds:** the two rung-completeness constructions, built with
  Petersen stand-ins for the hypothetical counterexample, must have exactly
  the combinatorics the T1 proofs assert.
- **Survey:** record every taut pinched (ratio \(<2\)) gadget verbatim — by
  T3 these must all have \(s_{\min}\ge3\); they are the enemy shapes for the
  next rung.

## Logical scope

The theorems rest on the `A012` hand proofs; this experiment can refute them
(one violating instance) but not prove them. The survey is exhaustive for the
enumerated class at orders 12–13 only. Petersen is *not* power-free, so the
scaffold anchors validate the T1 constructions' combinatorics (through-sets,
essential sets, spectrum confinement, degrees), while power-freeness in T1
itself comes from the hypothetical counterexample ingredient.

## Environment

- Tool and version: CPython 3.14.2; geng from nauty 2.9.3
  (`/opt/homebrew/bin/geng`), the same anchored binary and invocation
  (`geng -c -f -d1 n mine:0`, `mine`\(=\lceil(3n-4)/2\rceil\)) as `E010`.
- Dependencies: none beyond the standard library; all graph machinery
  (graph6 decoder, C4/cycle detectors, path and essential-vertex DFS,
  lobe-component analysis) is implemented in `verify_taut.py` independently
  of `E004`/`E005`/`E010`.
- Exact arithmetic / floating point: integer bitmask arithmetic throughout
  (the through-ratio comparison uses one float division, decision-irrelevant
  since \(S\) is recorded exactly).
- Random seed: none (deterministic enumeration).

## Inputs and search space

The `E010` stream: connected C4-free graphs, minimum degree \(\ge1\), edge
count \(\ge\lceil(3n-4)/2\rceil\), orders 12–13; downstream filter: exactly
two sub-cubic vertices with degree sum \(\ge3\), C4-freeness re-verified by
an independent codegree test. Fixed graphs: \(K_{3,3}-e\), Petersen, and the
two T1 scaffolds (orders 20 and 23).

## Reproduction

```sh
python3 verify_taut.py anchors
python3 verify_taut.py run 12 13
```

Outputs land in `data/taut_n{n}.json` (counts, all taut pinched findings
verbatim, violation lists — empty).

## Results

Anchors: all 17 pass, including \(K_{3,3}-e\) **taut** with \(S=\{3,5\}\),
spectrum \(\{4,6\}\); both scaffolds exact (A2: \(S=\{1\}\), essential set
\(=\) terminals, two single-attachment lobes, spectrum \(\{5,6,8,9\}\); A3:
\(S=\{2\}\), essential set \(\{a,w,b\}\), lobes at \(a\) and \(w\), spectrum
\(\{5,6,8,9\}\), degrees \(a,b,w=2,1,3\)).

| n | stream | examined | rung class | taut among them | non-taut | lobes | multi-attachment | ratio<2 | taut pinched |
|---|---|---|---|---|---|---|---|---|---|
| 12 | 52,331 | 1,690 | 19 | **0** | 38 | 38 | **0** | 22 | 3 |
| 13 | 389,734 | 16,106 | 114 | **0** | 227 | 227 | **0** | 116 | 2 |

Stream totals, examined counts, ratio\(<2\) counts, and
C8-free-among-pinched counts (0 and 0) reproduce the `E010` records exactly
(asserted in the script), anchoring both independent pipelines at once.

**Every taut pinched gadget found — all five — has
\(S=\{6,7,8,9,10,11\}\)** (a full interval at ratio \(11/6\)) and spectrum
\(\{3,5,6,7,8,9,10,11\}\) (contains \(C_8\)). The pinched population splits
exactly: \(22=19+3\) and \(116=114+2\) — every pinched gadget at these
orders is either in the (entirely non-taut) bottom-rung class or taut with
\(s_{\min}=6\).

## Interpretation

- T3 and T2 hold on every instance in reach: 133 bottom-rung-class gadgets,
  all non-taut; 265 lobe components, all single-attachment with internal
  degrees \(\ge3\). No refutation.
- Through order 13 the C4-free class contains **no taut pinched gadget with
  \(s_{\min}\in\{3,4,5\}\)**: the taut \(s_{\min}=3\) rung's target is empty
  here even before C8-freeness is imposed, while \(K_{3,3}-e\) (order 6)
  shows the shape is realizable the moment \(C_4\) is allowed. This suggests
  the next rung may, like T3, need only C4-freeness — an exact finite
  observation, not evidence about the universal statement.
- Claim-ledger update: `C028`.

## Independent checks

The script is a second, independent implementation of the whole detection
stack; its agreement with `E010`'s recorded counts on identical streams is a
bidirectional cross-validation of both. The five taut pinched findings were
re-examined via their recorded graph6 strings, through-sets, and spectra in
the JSON output.
