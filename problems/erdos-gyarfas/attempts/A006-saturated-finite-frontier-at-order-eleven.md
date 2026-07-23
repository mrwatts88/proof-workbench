# A006 — Saturated finite frontier at order eleven

- Date opened: 2026-07-23
- Problem: `P-002`
- Status: completed
- Portfolio role: primary route after the S005 pivot; exhaust the smallest
  unexcluded orders using the small-order collapse of the power-cycle and
  witness conditions. Closed after clearing orders \(11\)–\(13\): the
  mission clarification in `O008` retired further re-derivation of reported
  computations.

## Intended mechanism

At orders \(n\le15\), both sides of the problem collapse to fixed finite
lists: the only power-of-two cycle lengths that fit are \(4\) and \(8\)
(a \(C_{16}\) needs \(16\) vertices), and the only Mersenne witness lengths
\(2^k-1\) that fit in a simple path are \(3\) and \(7\) (a path of length
\(15\) needs \(16\) vertices). A counterexample of such an order is therefore
*exactly* a graph with minimum degree at least \(3\) containing neither
\(C_4\) nor \(C_8\), and the saturated counterexample supplied by `L008`
additionally has a length-\(3\) or length-\(7\) path across every nonedge.
Both classes are finitely and exactly checkable per order, and excluding
order \(n\) (given `L006` and the orders below \(n\)) lifts the lower bound
on every counterexample's order to \(n+1\).

## Entry assumptions

- `D001`–`D004`.
- `L006`: every counterexample has at least eleven vertices.
- `L008` is available but, as it turned out, not needed for the exclusions
  proved so far: the search space was taken to be the full class of
  \(\{C_4,C_8\}\)-free minimum-degree-\(3\) graphs, of which the saturated
  graphs are a subclass, and that full class was already empty.

## Targeted obligations

- `G009`: settle the order-\(11\) saturated-counterexample search.
- `G003` indirectly: each cleared order sharpens where any counterexample
  must live.

## Plan and decisive tests

1. Build an exhaustive, self-validating generator for the class
   \(\{\delta\ge3,\ \text{no }C_4,\ \text{no }C_8\}\) at a given order,
   reusing the degree-sequence completion scheme validated in `E002`.
2. Anchor it against independent prior counts (`E001`, `E002`), an exact
   symmetry-quotient identity, and a positive control on a class where
   \(C_8\)-free graphs exist, so that over-rejection would be caught.
3. Run order \(11\); while orders clear quickly and exactly, continue
   upward.
4. Stop at the first order that is intractable or that produces survivors,
   and record survivors verbatim if any appear.

## Deductions

### The small-order collapse

Let \(G\) be a counterexample to `C001` with \(|V(G)|=n\le15\). Every cycle
of \(G\) has length at most \(n\le15<16\), so the excluded power-of-two
lengths reduce to \(4\) and \(8\): \(G\) is precisely a graph with
\(\delta(G)\ge3\) and no \(C_4\) or \(C_8\). Conversely any such graph of
order at most \(15\) has no power-of-two cycle at all and is a
counterexample. For the saturated graph \(H\supseteq G\) from `L008` on the
same vertex set, every nonedge witness is a simple path of length \(2^k-1\)
on \(2^k\le n\le15\) vertices, so \(k\in\{2,3\}\) and the witness lengths
collapse to \(\{3,7\}\). \(\square\)

### `L017` — Every counterexample has at least fourteen vertices

**Proof.** By the collapse, a counterexample of order \(11\), \(12\), or
\(13\) would be a graph of that order with minimum degree at least \(3\)
containing neither \(C_4\) nor \(C_8\). The exhaustive search `E004`
enumerates every such labelled graph, in two layers whose coverage is proved
as follows.

*Degree sequences.* In a \(C_4\)-free graph two distinct vertices share at
most one common neighbour, for two shared neighbours \(x,y\) of \(u,v\) give
the \(4\)-cycle \(uxvy\). Counting paths of length two by their centre,
\(\sum_v\binom{d(v)}2\le\binom n2\). Together with \(d(v)\ge3\) for all
\(v\) and an even degree sum, this leaves exactly \(12\) nonincreasing
degree sequences at order \(11\), \(29\) at order \(12\), and \(59\) at
order \(13\); the program enumerates them, and all three counts were
re-derived by hand, the order-\(13\) hand count initially missing the
budget-exact sequence \((7,7,4,3^{10})\) before agreeing at \(59\).

*Labelled completion.* For each sequence, vertices carry nonincreasing
target degrees, and the least unfinished vertex repeatedly receives its full
remaining neighbourhood among the not-yet-full vertices. Every labelled
graph with those exact degrees arises from exactly one choice path: when a
vertex \(v\) becomes least unfinished, each finished vertex has already
realized all its incident edges, so the unrealized neighbours of \(v\) all
have larger index. An edge is rejected exactly when it closes a simple path
of length \(3\) or \(7\) between its endpoints, which is precisely when it
would create a \(C_4\) or a \(C_8\); rejection loses no admissible leaf
because a forbidden cycle in the partial graph persists in every completion,
and no forbidden leaf survives because its cycle's last-added edge would
have been rejected. The leaves are therefore exactly the
\(\{C_4,C_8\}\)-free graphs with the target degrees. Finally, any graph in
the class can be relabelled to nonincreasing degrees and, by permuting
vertices inside blocks of equal target degree, so that the neighbourhood of
vertex \(0\) meets each block in a prefix; the generator's canonical
restriction of vertex \(0\)'s neighbourhood therefore preserves coverage up
to isomorphism, and emptiness of the restricted search proves emptiness of
the class.

The search returned zero completed graphs at order \(11\) (\(231{,}646\)
search nodes over \(12\) sequences), zero at order \(12\)
(\(6{,}535{,}800\) nodes over \(29\) sequences), and zero at order \(13\)
(\(44{,}397{,}061\) nodes over \(59\) sequences). Hence no counterexample of
order \(11\), \(12\), or \(13\) exists, and by `L006` every counterexample
has at least fourteen vertices. \(\square\)

The generator's detectors and rejection logic are validated in `E004`
against five anchors: the independent `E001` count of all \(19{,}355\)
labelled cubic graphs on \(8\) vertices; the independent `E002` count of
\(937{,}440\) labelled \(C_4\)-free cubic graphs on \(10\) vertices, every
one containing a \(C_8\); the exact symmetry quotient
\(937{,}440/\binom93=11{,}160\) under the canonical-neighbourhood
restriction; consistency of incremental \(C_8\) rejection with independent
whole-graph detection at order \(10\); and a positive control on the
\(C_8\)-free cubic graphs of order \(8\), a nonempty class where incremental
rejection and independent leaf classification must and do agree, at exactly
the \(35\) labelled copies of \(K_4\sqcup K_4\).

### Standalone corollary

For \(n\le13\), every graph on \(n\) vertices with minimum degree at least
\(3\) contains a \(4\)-cycle or an \(8\)-cycle. The primary literature
reports cubic graphs on \(24\) vertices with neither, so the smallest order
admitting a \(\{C_4,C_8\}\)-free graph of minimum degree \(3\) lies between
\(14\) and \(24\); locating it is a natural continuation with direct
consequences for the conjecture at orders up to \(15\).

## Failure analysis

- The S005 idea that saturation would *accelerate* the finite search was
  wrong in its generative form: the witness condition constrains only
  completed graphs, so it cannot prune the generation tree, and at the
  orders cleared so far the plain \(\{C_4,C_8\}\)-free class was already
  empty, so the saturation filter never had anything to filter. `L008` was
  not needed for `L017`. Saturation's finite-frontier value would begin only
  at an order where \(\{C_4,C_8\}\)-free graphs exist, as a proved way to
  discard survivors; none has appeared yet.
- The cleared orders remain far below the reported prior computational
  bounds in the literature, including at least \(30\) vertices for a cubic
  counterexample. As with `L005`–`L006`, no novelty is claimed for `L017`;
  the reported computations were not reproduced here, and the internal chain
  `L006` + `E004` is self-contained.

## Salvageable results

- Incremental \(C_8\) rejection makes exhaustion far cheaper than
  anticipated: order \(11\) needed only \(231{,}646\) nodes against the
  \(4{,}252{,}251\) nodes of the order-\(10\) \(C_4\)-only run in `E002`.
  The constraint pair \(\{C_4,C_8\}\) is very strong at small orders.
- The validated generator, anchors, and collapse argument extend unchanged
  through order \(15\); beyond that, \(C_{16}\) enters both lists and the
  tooling needs a redesign.

## Exit state

- Status: completed. Orders \(11\)–\(13\) are exhausted and yielded `L017`;
  extension to \(14\)–\(15\) is retired by the mission clarification in
  `O008`, since reported prior computations already exceed those orders and
  re-deriving them adds no new information.
- Promoted records: `L017`, `C011` in `CLAIMS.md`.
- Next action: none within this route. The frontier effort moves to the
  source-frontier import (`G004`) and the saturation novelty check
  (`G011`); the validated `E004` tooling remains available for verifying
  imported extremal graphs internally.
