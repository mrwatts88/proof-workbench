# E016 — Verification of the 1-atom closure correspondence and the minimality reductions

- Date: 2026-07-24
- Problem: `P-002`
- Evidence class: instance verification of proved lemmas + one small exhaustive census
- Owner: session `S019`, worker W1 (attempt `A019`)

## Question

Six questions, all attached to deductions of `A019`:

1. **A1 (closure calculus, `A019` W1-T1).** For a finite simple graph
   \(H\) and \(a\ne b\in V(H)\), is
   \(\mathrm{Spec}(H+u)=\mathrm{Spec}(H)\cup(S+2)\) (with \(u\) new,
   \(N(u)=\{a,b\}\)), \(\mathrm{Spec}(H+ab)=\mathrm{Spec}(H)\cup(S+1)\),
   and \(\mathrm{Spec}(H/(a{=}b))=\Sigma'\cup S\subseteq
   \mathrm{Spec}(H)\cup S\), where \(S=S(H,a,b)\) is the set of simple
   \(a\)–\(b\) path lengths and \(\Sigma'\) the set of lengths of cycles
   of \(H\) meeting \(\{a,b\}\) at most once?
2. **A2 (case dichotomy, `A019` W1-T6).** Does every *tight-1-atom-shaped*
   graph (connected; exactly one vertex of degree \(<3\), of degree
   exactly 2 — power-freeness dropped) fall into exactly one of the five
   cases of the W1-T6 table, with the reduct predicted by that case
   having the predicted degree profile and order?
3. **A3 (saturation construction, `A019` W1-T12).** In the (3,3)/non-cut
   case, is \(H+az\) tight-1-atom-shaped of order \(|B|-1\) for every
   \(z\ne a,b\) non-adjacent to \(a\) (and of minimum degree \(\ge3\)
   when \(z=b\)), with
   \(\mathrm{Spec}(H+az)=\mathrm{Spec}(H)\cup(P_H(a,z)+1)\)?
4. **A4 (`C027` anchor).** Do the recorded `C027` stream counts at orders
   6–11 reproduce from an independent implementation, and is no member of
   the \(\le2\)-sub-cubic class at those orders power-free?
5. **A5 (fixed anchors).** Do the cycle-spectrum and path-length
   primitives reproduce the recorded spectra of \(K_4\),
   \(K_{3,3}-e\), Petersen and Petersen\(-e\)?
6. **A6 (kill test for the W1-T12 lever).** How often is a connected
   \(C_4\)-free graph with exactly two degree-2 vertices (others
   \(\ge3\)) **Mersenne-saturated** at a degree-2 vertex \(a\) — i.e.
   every \(z\notin N[a]\), \(z\ne a\), is joined to \(a\) by a simple
   path of some length \(2^k-1\)? Power-freeness is dropped, so this
   measures how much the saturation condition alone constrains.

## Logical scope

A1–A3 and A5 are **instance verifications of proved lemmas**: they can
refute a lemma but cannot prove it. A1 did in fact refute the first draft
of W1-T1(3) (see Results), which is the reason the lemma is now stated
with an inclusion rather than an equality in that direction.

A4 is an **exhaustive census over a delegated generation layer** (nauty
`geng`), used only as calibration against `C027`; it establishes nothing
new and is not cited as support for any claim.

A6 is **descriptive frequency data with power-freeness dropped**. It
cannot prove or refute anything; it is a route-selection instrument for
`A019`'s recommended next move. Emptiness or abundance of saturated
members says only what it says at those orders, and the class it
enumerates is *not* the residual object of `A019` case (5b) (which is
additionally power-free and vertex-taut).

Nothing in E016 is a finite exclusion for statement 0.1.

## Environment

- Tool and version: nauty 2.9.3 (`geng`), CPython 3.14.2 (`python3
  --version` reports `Python 3.14.2`), macOS 15 / darwin 25.5.0, arm64.
- Dependencies: standard library only (`subprocess`, `itertools`,
  `time`). No third-party packages.
- Exact arithmetic / floating point: all quantities are integers and
  finite sets of integers; no floating-point arithmetic is used anywhere
  except the wall-clock timings printed for information.
- Random seed: none — the computation contains no randomness, no
  sampling and no heuristic pruning. `geng` output order is fixed by the
  tool.

## Inputs and search space

- **A1.** All connected graphs of orders 4–8 (`geng -q -c n`), and every
  unordered vertex pair of each. \(j=1\) is tested when \(ab\notin
  E(H)\); \(j=0\) additionally when \(a,b\) have no common neighbour
  (the two conditions required for simplicity of the closure).
- **A2, A3.** `geng -q -c -d2 n mine:maxe` for orders 5–9 with
  \(\mathrm{mine}=\lceil(3n-4)/2\rceil\) and \(\mathrm{maxe}=\binom n2\),
  filtered to the tight-1-atom shape. The edge lower bound is safe: a
  tight-1-atom-shaped graph has \(2|E|\ge3(n-1)+2=3n-1\).
- **A4.** `geng -q -c -f -d1 n mine:maxe` for orders 6–11, same `mine`,
  then the filter "at most two vertices of degree \(<3\)". The reported
  *stream* count is the `geng` output count (this is what `C027`
  records); the reported *class* count is after the sub-cubic filter.
- **A6.** `geng -q -c -f -d2 n mine:maxe` for orders 8–13 with
  \(\mathrm{mine}=\lceil(3n-2)/2\rceil\) (two degree-2 vertices, others
  \(\ge3\), so \(2|E|\ge4+3(n-2)=3n-2\)), filtered to exactly two
  degree-2 vertices and no other sub-cubic vertex.

**Boundary cases handled explicitly.** \(ab\in E(H)\) (the \(j=1\) and
\(j=0\) closures are then illegal and are skipped); \(a,b\) with a common
neighbour (\(j=0\) illegal); \(z=b\) in A3 (the lift has minimum degree
3 rather than a sub-cubic vertex, matching W1-T12's case split);
disconnected reducts in A2 (the cut case, where the reduct has exactly
two components).

**A geng parsing trap, recorded because it silently produced empty
streams in the first run.** `geng n m:` is **not** "at least \(m\)
edges": the trailing colon is ignored and the argument is read as the
*exact* edge count \(m\). The upper bound must be written out
(`geng n m:M`). All counts below use the explicit two-sided form.

## Reproduction

```sh
cd problems/erdos-gyarfas/experiments/E016-verification-of-the-1-atom-closure-correspondence-and-the-mi
python3 verify.py all          # or: a1 | a2 | a3 | a4 | a5 | a6
```

Output is reproduced verbatim in `run.log`.

## Results

See `run.log` for the exact console output. Summary:

- **A5** all fixed anchors pass: \(K_4\) spectrum \(\{3,4\}\);
  \(K_{3,3}-e\) spectrum \(\{4,6\}\) with \(S=\{3,5\}\) between the two
  degree-2 vertices; Petersen spectrum \(\{5,6,8,9\}\) and cubic;
  Petersen\(-e\) spectrum \(\{5,6,8,9\}\) with \(S=\{4,5,7,8\}\); the
  2-closure of Petersen\(-e\) has spectrum \(\{5,\dots,10\}\), hence is
  not power-free — exactly as `A019` W1-T3 predicts from \(6\in S+2\).
- **A1** 12,109 connected graphs of orders 4–8, 331,115 vertex pairs: all
  three closure identities hold in the corrected form.
  **Falsification recorded:** the first draft asserted
  \(\mathrm{Spec}(H/(a{=}b))=\mathrm{Spec}(H)\cup S\) and failed at order
  6, because a cycle of \(H\) through *both* \(a\) and \(b\) becomes a
  closed walk meeting the merged vertex twice and contributes no cycle.
  W1-T1(3) is now stated as \(\Sigma'\cup S\) with only the inclusion
  into \(\mathrm{Spec}(H)\cup S\) claimed — which is the direction
  `A019` uses.
- **A2** 67,432 tight-1-atom-shaped graphs at orders 5–9, classified as
  cut/deg-3-side 0, cut/both\(\ge4\) 1, non-cut/(3,\(\ge4\)) 14,257,
  non-cut/(\(\ge4,\ge4\)) 51,578, non-cut/(3,3) 1,596; every predicted
  reduct had the predicted degree profile and order bound, and every
  graph fell in exactly one case (`components(B-u)` never exceeded 2).
- **A3** the (3,3)/non-cut reducts at orders 5–9 and every lift \(H+az\):
  shape and spectrum identity verified.
- **A4** stream counts 4, 5, 36, 84, 918, 4,058 at orders 6–11, matching
  the counts recorded in `C027` exactly; the corresponding
  \(\le2\)-sub-cubic classes have sizes 0, 0, 1, 4, 39, 262 and no member
  is power-free.
- **A6** the connected \(C_4\)-free class with exactly two degree-2
  vertices and all others \(\ge3\) has sizes 1, 2, 22, 125, 1,139, 10,966
  at orders 8–13; **no member is power-free** (independent re-derivation
  of `C027`'s verdict restricted to this profile); Mersenne saturation
  holds at one terminal for 1, 2, 22, 123, 1,136, 10,966 of them and at
  **both** terminals for 1, 2, 22, 123, 1,133, 10,966 — i.e. \(100\%\) at
  order 13 and \(\ge99.5\%\) at orders 11–12.

  A note on an earlier, discarded A6 run: it used
  \(\mathrm{mine}=\lfloor3n/2\rfloor\), which is one too large at even
  orders and therefore under-counted (class sizes 0, 2, 11, 125, 1,064 at
  orders 8–12). Only the corrected run above is reported.

## Interpretation

The narrowest justified conclusions:

1. The closure calculus `A019` W1-T1 survives exhaustive instance testing
   at orders 4–8 in its corrected form, and its uncorrected form is
   refuted. The correspondence `A019` W1-T3 (tight 1-atoms with both
   \(u\)-neighbours cubic and connected reduct \(\leftrightarrow\)
   power-free (2,2)-terminal gadgets whose through-set avoids
   \(\{2,6,14,\dots\}\)) is therefore verified as an identity of spectra
   on every instance tested, and its `C027` order bound (\(\ge16\) for
   the gadget, \(\ge17\) for the atom) is consistent with the reproduced
   stream counts.
2. The case dichotomy `A019` W1-T6 is a correct partition with correct
   degree bookkeeping on all 67,432 shaped instances at orders 5–9.
3. `A019` W1-T12's construction is correct as stated, including its
   \(z=b\) boundary case.
4. `C027`'s recorded stream counts reproduce from an independent
   implementation at orders 6–11 — calibration only.
5. A6 is route-selection data for `A019`'s recommended next move and is
   cited nowhere else. Its verdict: **Mersenne saturation at a degree-2
   vertex is generically satisfied in this class**, so `A019` W1-T12
   cannot carry a proof on its own and was demoted from primary lever.
   The finding is descriptive at orders 8–13 with power-freeness dropped;
   it does **not** say that a power-free saturated member exists, and it
   is not evidence for or against statement 0.1.

No ledger claim is proposed by E016 on its own; it is support for the
`A019` deductions, which are hand proofs.

## Independent checks

- The cycle-spectrum routine is cross-checked against four independently
  known spectra (A5), including two graphs whose spectra are recorded in
  `CLAIMS.md`/`E013` (Petersen\(-e\): \(S=\{4,5,7,8\}\) per `C031`;
  \(K_{3,3}-e\): \(S=\{3,5\}\), spectrum \(\{4,6\}\) per `L025` R6 and
  `E010` anchor A1).
- The generation layer is cross-checked against `C027`'s independently
  recorded stream counts at six consecutive orders (A4).
- The \(j=0\) closure is checked twice per instance: once against the
  exact description \(\Sigma'\cup S\) computed by a second, separately
  written cycle enumerator (`spectrum_missing_one`), and once against the
  weaker inclusion actually used in `A019`.
- Not independently re-implemented: the `geng` generation layer itself
  (imported tool, anchored as above, same caveat as `E010`–`E015`).
