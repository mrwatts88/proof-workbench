# E015 — Exhaustive bipartite power-free gadget hunt past the general order-15 wall

- Date: 2026-07-24 (S016; order-22 leg completed and folded in during S018)
- Problem: `P-002`
- Evidence class: exhaustive finite search over a proved-complete class
  (`A017` T3/T4/T5), plus implementation and generator cross-validation

## Question

`A017` T3 (the bipartite assembly criterion) says that **any** connected
bipartite power-free graph with at most two sub-cubic vertices — degrees
\(\ge1\) summing to \(\ge3\) if there are two, degree 1 or 2 if there is one —
disproves statement 0.1, with no path enumeration and no external import. `A017`
T4 says bipartite generation is a **complete** instrument for `L034`'s
congruence channels (i) (all-odd \(S\)) and (iii) (\(S\subseteq2+4\mathbb Z\)),
modulo the standing 1-atom relativization.

So: **does such a graph exist?** Equivalently — does the parity channel of the
assembly interface contain a witness at any order the search can reach? The
general \(\{C_4,\dots\}\)-free stream is exhausted at order 15 (`C027`); this
class is far sparser, so the same question can be pushed several orders further.

## Logical scope

- A **hit disproves statement 0.1** outright (`A017` T3, whose only inputs are
  `L025` R1/R4 and elementary parity). The script stops and exits 2.
- An **empty run at order \(n\)** proves: no connected bipartite \(C_4\)-free
  graph of order \(n\) with at most two sub-cubic vertices (each of degree
  \(\ge2\)) is power-free. By the pendant reduction (`A014` T1, restated as
  `A017` T3 case B2), an empty run at all orders \(\le N\) also excludes every
  witness of order \(\le N+1\) that has a degree-1 vertex, since stripping the
  pendant lands in the scanned class one order down and preserves bipartiteness,
  \(C_4\)-freeness, the spectrum, and the sub-cubic count.
- The empty result is *not* a proof of any universal statement. It is a finite
  exclusion for the parity channels (and, in its min-degree-3 sub-case, an
  internal verification of "no bipartite counterexample" at those orders).
- Splits skipped by the `A017` T5 counting bound are proved empty, so skipping
  them keeps the run exhaustive; the bound is machine-checked against genbg
  itself at orders 8–14 (anchor A6).
- The scan says nothing about `L034` channel (ii) (odd-prime \(\gcd\)), which
  `A017` T4's scope caveat shows is *not* bipartite-forced.

## Environment

- CPython 3.14.2 and PyPy 7.3.23 (Python 3.11.15); all anchors pass under both.
- nauty 2.9.3 (`/opt/homebrew/bin`): `genbg`, `geng`, `labelg`.
- Standard library only; integer bitmask arithmetic throughout; no randomness.
- Graph primitives (`g6_decode`, `degrees`, `has_c4`, `from_edges`) copied
  verbatim from `E012/scan_pairs.py`, which was anchored against the independent
  `E010` pipeline.

## Inputs and search space

Class scanned at order \(n\): connected, bipartite, \(C_4\)-free, minimum degree
\(\ge2\), at most two vertices of degree 2.

Generation: `genbg -q -c -Z1 -d2 p q mine:0` for every split \(p+q=n\),
\(p\le q\), admitted by the `A017` T5 bound \(3q-4\le\binom p2\) and
\(3p-4\le\binom q2\). Here `-Z1` ("two vertices in the second class have at most
one common neighbour") is exactly \(C_4\)-freeness for bipartite graphs (checked
by an assertion on every retained graph), and
\(\text{mine}=\lceil(3n-2)/2\rceil\) comes from the degree sum
\(3(n-2)+2+2\).

Per graph: degree profile → reject if more than two vertices are sub-cubic;
2-colouring; exact existence tests for cycles of length 8 and 16 (and 32 when
\(n\ge32\)); exact count of 8-cycles; for two-terminal members, whether the two
sub-cubic vertices lie in the same colour class (all-even through-set) or in
opposite classes (all-odd).

Cycle tests use a DFS with min-vertex canonicalization, fixed direction, and
BFS-distance pruning; correctness is cross-validated against an independent
brute-force enumerator (below).

## Reproduction

```sh
python3 bipscan.py anchors        # 20,082 checks
python3 bipscan.py crosscheck 14  # genbg class == geng (E010 stream) class
python3 bipscan.py run 12 13 14 15 16 17 18 19 20 21 22
python3 verify_parity.py all      # A017 T0/T1/T2 exhaustively, small orders
python3 verify_parity.py class    # T3's two-terminal reading on the class
```

Outputs land in `data/scan_n{n}.json` (full per-graph records when the class
has at most 5,000 members, otherwise histograms plus the minimum-\(C_8\)
exemplars). Runtimes (CPython, on a loaded machine): \(\le3\)s per order
through 19, 38s at 20, 146s at 21, 2,798s at 22.

## Results

**No power-free member exists at any scanned order (12–22).** Every single graph in the
class contains an 8-cycle — the C8-free count is zero at every order, so the
\(C_{16}\) test never even becomes decisive.

| n | in class | generated | power lengths present | min #\(C_8\) | profiles (2,2 / 2 / none) |
|---|---|---|---|---|---|
| 12 | 0 | 0 | — | — | — |
| 13 | 0 | 0 | — | — | — |
| 14 | 2 | 2 | \(\{8\}\) | 13 | 1 / 0 / 1 |
| 15 | 1 | 1 | \(\{8\}\) | 21 | 1 / 0 / 0 |
| 16 | 6 | 37 | \(\{8,16\}\) | 20 | 5 / 0 / 1 |
| 17 | 8 | 63 | \(\{8,16\}\) | 27 | 7 / 1 / 0 |
| 18 | 75 | 4,109 | \(\{8,16\}\) | 23 | 62 / 8 / 5 |
| 19 | 197 | 9,086 | \(\{8,16\}\) | 26 | 172 / 22 / 3 |
| 20 | 2,715 | 456,735 | \(\{8,16\}\) | 18 | 2,333 / 332 / 50 |
| 21 | 10,865 | 1,637,741 | \(\{8,16\}\) | 24 | 9,588 / 1,208 / 69 |
| 22 | 178,549 | 55,451,237 | \(\{8,16\}\) | 14 | 155,205 / 21,579 / 1,765 |

Order 22 was launched in S016 and completed during S018 (2,798s; splits
\((9,13)\): 1 member, \((10,12)\): 15,849, \((11,11)\): 162,699). The next
leg is order 23 — splits \((11,12)\) and \((10,13)\) — which at the order-22
rate is a few hours; past that genbg stops being the right instrument and the
dedicated \(\{C_4,C_8\}\)-free generator is the tool-building move.

("profiles" counts members by their sub-cubic degree multiset: `2,2` = a
two-terminal gadget, `2` = a bipartite 1-atom candidate, `none` = minimum degree
\(\ge3\), i.e. a bipartite counterexample candidate outright.)

Three sub-results follow from the same run, at the orders covered:

1. **Parity channel.** No power-free bipartite two-terminal gadget exists, so
   `L034`'s channels (i) and (iii) are empty here — and by `A017` T4 that is the
   whole of those channels, not a sub-case.
2. **Bipartite tight 1-atoms.** The `2` column is the bipartite instance of
   `G013` sub-question (a) as rewritten in S018: since the stream has minimum
   degree 2, these are *tight* 1-atoms (exceptional vertex of degree exactly 2),
   which `L036` identifies as the surviving object — the unrestricted 1-atom
   question is conjecture-complete. None exists at these orders (33 candidate
   shapes at orders 17–19, 21,579 at order 22, all containing a \(C_8\)).
3. **Bipartite EGC.** The `none` column is the bipartite instance of statement
   0.1 itself: no bipartite counterexample exists at these orders. This is
   verified internally, so the corresponding unverified external import
   (`G014` item 2) is not needed for any step here.

The first specimen of the class is instructive: at order 14 the class is exactly
two graphs — the **Heawood graph** (cubic, 21 eight-cycles; identified by
`labelg` canonical form) and a 20-edge graph with two degree-2 vertices **in
opposite colour classes** (all-odd through-set) carrying 13 eight-cycles. So the
parity channel's shape catalogue is not empty; what is empty is its power-free
part, and by a wide margin: the minimum number of \(C_8\)s over the whole class
never drops below 13.

## Interpretation

- The narrowest justified conclusion: the parity/bipartite channel of the
  assembly interface is **empty through the scanned orders**, five-plus orders
  past the general \(\{C_4,C_8\}\)-free wall of `C027`, and the obstruction is
  uniformly \(C_8\) — never \(C_{16}\), never a near miss. Recorded as `C034`.
- The margin matters as much as the emptiness: in the pinched channel the
  equality blocks (`C031`) are blocked from power-freeness by a *handful* of
  \(C_8\)s (3–7), whereas here the minimum is 13 and rises with order. The
  parity channel is, empirically, further from a witness than the pinched one —
  which lowers rather than raises the prior on Thread B's disproof leg.
- Method note: the collapse to a pure forbidden-cycle test (no path
  enumeration, no tautness test) is what makes these orders reachable at all;
  it comes entirely from `A017` T2/T3.

## Theorem verification (`verify_parity.py`)

The falsification test named in `A017`'s plan — a vertex-taut two-terminal
graph with parity-constant through-set that is **not** bipartite would refute
T2 — was run exhaustively over every connected graph of order \(\le7\) (994
graphs, all 39,690 ordered terminal pairs) and every connected \(C_4\)-free
graph of orders 8–9 (926 graphs — the full geng counts 186 and 740 — 63,696
pairs), with through-sets and essential-vertex masks computed by explicit
simple-path enumeration:

| check | statement | instances where the hypothesis held |
|---|---|---|
| V1 | bipartite \(\Rightarrow\) \(S\) parity-constant, all-odd iff opposite classes | 2,500 + 6,288 |
| **V2** | **taut + parity-constant \(\Rightarrow\) bipartite (T2; the kill condition)** | **690 + 262, zero failures** |
| V3 | taut \(\Rightarrow\) cut vertices separate, block chain, Minkowski sum, blocks taut (T0) | 24,642 + 9,320 (8,128 cut-vertex separations) |
| V4 | 2-connected + non-bipartite \(\Rightarrow\) both parities (T1, the fan lemma) | 21,060 + 6,136 |
| V5 | sharpness: parity-constant + non-bipartite pairs are all non-taut | 1,704 + 9,084 |

V5 is the quantitative form of the sharpness example: 10,788 pairs are
parity-constant in a non-bipartite graph, and **every one of them** is
non-taut — exactly the lobe configuration `L027` routes to the 1-atom
question. Tautness is not a technical convenience in T2; it is the whole
hypothesis.

V6 re-verifies T3's two-terminal reading directly on 2,581 members of the
search class at orders 12–20: the through-set computed by explicit path
enumeration is parity-constant and its parity matches the colour-class
prediction in every case.

## Independent checks

- **Implementation cross-validation.** `has_cycle_len` is checked against an
  independent brute-force cycle enumerator on *every* connected graph of order
  \(\le7\) (994 graphs, all lengths) and on 1,000+ connected bipartite graphs of
  orders 8–11; plus known spectra for \(C_6\), \(K_{3,3}\), \(Q_3\), the
  Petersen graph (\(\{5,6,8,9\}\), matching `E013`'s recorded anchor) and the
  Heawood graph (\(\{6,8,10,12,14\}\)); plus pure cycles \(C_8,C_{12},C_{16},
  C_{20}\) and the bipancyclic hypercube \(Q_4\) (every even length 4–16) for
  the long-cycle tests the scan actually depends on. 20,082 assertions, passing
  under both CPython 3.14.2 and PyPy 7.3.23.
- **Generator cross-validation.** `crosscheck 14` regenerates the class from the
  completely different `E010`/`E013` route — `geng -q -c -f -d1 14 19:0`,
  filtered to bipartite + \(C_4\)-free + degree profile — canonicalizes both
  sides with `labelg`, and asserts set equality: 2 graphs on both sides.
- **T5 bound validation.** Every split rejected by the counting bound at orders
  8–14 is confirmed empty by running genbg on it anyway (anchor A6).
- **Named-object identification.** The unique cubic member at order 14 is
  confirmed isomorphic to the Heawood graph by `labelg` canonical form — an
  external landmark the class had to contain (the (3,6)-cage).
- **Consistency with the recorded frontier.** Orders 12–15 are inside `C027`'s
  exhausted range, and the scan returns empty there, as `C027` requires.
