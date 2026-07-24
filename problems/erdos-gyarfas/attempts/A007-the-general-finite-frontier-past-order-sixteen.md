# A007 — The general finite frontier past order sixteen

- Date opened: 2026-07-23
- Problem: `P-002`
- Status: closed (successful)
- Portfolio role: primary (the frontier-passing move selected by the S007
  sweep after `G011` resolved in favor of the internal saturation line)

## Intended mechanism

The strongest inspectable general-order exclusion in the literature is
Royle's 2002 search: no counterexample on at most \(15\) vertices
(`C012`); it has not moved in twenty-four years. The mission directs
effort past the frontier, and the S007 probes showed the relevant search
class is small for modern exhaustive generation: the connected
\(C_4\)-free minimum-degree-\(3\) graphs number only \(6{,}059\) at order
\(14\) and about \(1.7\) million at order \(16\). Exhausting orders
\(14\)–\(17\) with an anchored generator and independent cycle tests
therefore yields a new proved finite bound at negligible cost, while the
survivors (if any) would have been exactly the smallest
\(\{C_4,C_8\}\)-free objects the saturation route wants as test material.

## Entry assumptions

Only the statement's conventions `D001`–`D004` and the negation of `C001`
(a hypothetical counterexample). The computational leg additionally
assumes the correctness of nauty's geng for the delegated generation
class, anchored as recorded in `E006` (see Deductions for how this enters
the lemma's support).

## Targeted obligations

- `G003` (finite side): extend the exact exclusion range.
- `G007`/`G012`: supply the saturation program with the true extremal
  window for \(\{C_4,C_8\}\)-free minimum-degree-\(3\) graphs.

## Plan and decisive tests

1. Run the `E006` pipeline at orders \(14\), \(15\), \(16\), \(17\); each
   order is decisive by itself (survivors or emptiness).
2. Pivot trigger: a verified survivor that is a counterexample (would
   refute `C001` and end the project's search phase), or intractability
   (would stop the extension at the last completed order).

## Deductions

**Lemma A (connectivity; hand proof).** A counterexample of minimum order
is connected. *Proof.* Let \(G\) be a counterexample of minimum order and
suppose it is disconnected. Every connected component has minimum degree
at least \(3\) (degrees are computed within the component, and neighbors
lie in the component), and a component contains no power-of-two cycle
because \(G\) contains none. Any one component is then a counterexample
with strictly fewer vertices than \(G\) (a disconnected graph has at least
two nonempty components), contradicting minimality. ∎

**Lemma B (collapse by order; hand proof).** For \(4\le n\le 15\), a graph
of order \(n\) is a counterexample if and only if it has minimum degree at
least \(3\) and contains neither \(C_4\) nor \(C_8\). For \(16\le n\le
31\), it is a counterexample if and only if it has minimum degree at least
\(3\) and contains none of \(C_4\), \(C_8\), \(C_{16}\). *Proof.* A cycle
of length \(2^k\) requires \(2^k\) distinct vertices, so at order
\(n\le 15\) only lengths \(4\) and \(8\) are realizable, and at
\(n\le 31\) only \(4\), \(8\), \(16\). ∎ (This is the same collapse used
at orders \(\le 15\) in `A006`; the \([16,31]\) window adds \(C_{16}\).)

**Computation (`E006`, exhaustive per order; anchors A1–A5 passed).**
Every connected graph with minimum degree at least \(3\) and no \(C_4\)
was generated at each order (geng `-c -f -d3`, with minimum degree and
\(C_4\)-freeness re-verified independently on every graph), and tested for
\(C_8\):

| order | connected \(C_4\)-free \(\delta\ge3\) graphs | with no \(C_8\) |
|---|---|---|
| 14 | \(6{,}059\) | \(0\) |
| 15 | \(91{,}433\) | \(0\) |
| 16 | \(1{,}655{,}659\) | \(0\) |
| 17 | \(34{,}758{,}006\) | \(0\) |

The \(C_{16}\) test at orders \(16\)–\(17\) never activated: the
\(\{C_4,C_8\}\)-free class was already empty, so the exclusion does not
depend on the \(C_{16}\) detector (it was nonetheless anchored, A4).

**L018 (finite exclusion; computer-assisted).** Every counterexample has
at least eighteen vertices. *Proof.* Suppose a counterexample of
order \(n\le 17\) exists; take one of minimum order
\(m\le n\). By `L017` (computer-assisted via `E004`), \(m\ge 14\). By
Lemma A it is connected. By Lemma B it is a connected graph of minimum
degree at least \(3\) of order \(m\in\{14,\dots,17\}\) with
no \(C_4\) and no \(C_8\) (and, for \(m\ge16\), no \(C_{16}\), which is
not needed). The `E006` census found no such graph. ∎

Support type: like `L017`, this is a computer-assisted lemma. Its
computational leg is `E006` (recorded as `C016`); its exhaustiveness rests
on geng's correctness for the delegated class, anchored against OEIS
A002851 and A006786 published counts, cross-validated at orders
\(11\)–\(13\) against the independent `E004` search, and equipped with
two-sided filter controls. Unlike `L017`, whose generation layer was
internal and hand-proved, the generation layer here is an imported,
widely-validated tool; this dependency is recorded explicitly and `L018`
must not be cited as having a fully internal proof.

**Census corollary (`C016`).** The smallest \(\{C_4,C_8\}\)-free graph of
minimum degree at least \(3\) has at least eighteen vertices; `E005`
holds such (cubic, even witness-covered) graphs at order
\(24\), so the extremal threshold lies in \([18,24]\).
Before this session the interval was \([14,24]\).

## Failure analysis

Not applicable; the route succeeded at every attempted order. The
extension stops where the class stops being cheaply enumerable with the
CPython filter (estimated order \(18\): roughly \(2\times10^8\) graphs —
about an hour of core time under PyPy, which the user has made available
for all Python legs; order \(19\): roughly \(3\times10^9\), where geng
generation itself becomes the dominant cost).

## Salvageable results

- Lemmas A and B are permanent small reductions, reusable at any order.
- The anchored geng pipeline (`E006/frontier.py`) extends to order \(18\)
  and beyond with only a parts/workers change and, past \(18\), a faster
  \(C_8\) filter.
- The emptiness pattern so far — the entire \(\{C_4,C_8\}\)-free class,
  not merely the counterexample class, is empty through order
  \(17\) — sharpens the saturation program's target: the first
  \(\{C_4,C_8\}\)-free graphs of minimum degree \(3\) live somewhere in
  \([18,24]\), and at \(24\) the known ones are cubic and
  carry full Mersenne witness coverage (`C015`).

## Exit state

- Status: closed (successful)
- Promoted records: `L018`, `C016` in `CLAIMS.md`; `E006` census;
  `PROOF.md` dependency outline updated
- Next action: extend to order \(18\) with a faster filter (PyPy on the
  existing pure-Python detectors, or a compiled filter) if the saturation
  program wants the exact threshold, or leave the window \([18,24]\) and
  work the saturation structure directly

## Addendum (2026-07-24, session S009): order-18 extension and L022

The next action above was executed in S009 as the capped support leg:
the unmodified `E006` pipeline, anchors re-passed under PyPy 7.3.23, ran
order \(18\) in 48 `res/mod` parts with 8 workers (~2h50m wall).

**Computation (`E006` extension, recorded as `C023`).** Every connected
graph on \(18\) vertices with minimum degree at least \(3\) and no
\(C_4\) was generated (\(834{,}711{,}846\) graphs; geng `-c -f -d3`,
with degree and \(C_4\)-freeness re-verified independently on every
graph) and tested for \(C_8\): none is \(C_8\)-free. The \(C_{16}\)
detector never activated.

**L022 (finite exclusion; computer-assisted).** Every counterexample has
at least nineteen vertices. *Proof.* Suppose a counterexample of order
\(n\le18\) exists; take one of minimum order \(m\le n\). By `L018`,
\(m\ge18\), so \(m=18\). By Lemma A it is connected. By Lemma B (case
\(16\le m\le31\)) it is a connected graph of minimum degree at least
\(3\) on \(18\) vertices with no \(C_4\) and no \(C_8\) (and no
\(C_{16}\), which is not needed). The order-18 census found no such
graph. ∎

Support type: identical to `L018` — computer-assisted with the
generation layer delegated to anchored geng; all caveats recorded for
`L018` apply verbatim. Consequently the smallest \(\{C_4,C_8\}\)-free
graph of minimum degree at least \(3\) has between \(19\) and \(24\)
vertices (upper end by `E005`/`C018`).

The census growth rate (\(\times24\) from order 17) makes order 19
roughly \(2\times10^{10}\) graphs — beyond this pipeline's practical
range without a compiled filter; the cap recorded in `DECISIONS.md`
stands.
