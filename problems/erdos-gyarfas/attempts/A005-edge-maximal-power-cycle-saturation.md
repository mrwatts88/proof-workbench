# A005 — Edge-maximal power-cycle saturation

- Date opened: 2026-07-23
- Problem: `P-002`
- Status: completed
- Portfolio role: primary global reframing, now delimited; its reductions
  remain live assets while single-witness forcing is retired

## Intended mechanism

Replace a hypothetical counterexample by a supergraph on the same vertex set
which is maximal subject to having no power-of-two cycle. Every missing edge
then has a certificate: its endpoints are joined by a path whose length is one
less than a power of two. Unlike cubic domination or one induced path, this
condition simultaneously constrains every nonedge of the graph.

## Entry assumptions

- `D001`–`D004`.
- Conditionally, a counterexample to `C001` exists.
- `C008` only for the observation that a power-cycle-free graph has average
  degree below some absolute threshold.
- `C009` only for the large-girth stress test.

## Targeted obligations

- `G003`: find a global power-of-two cycle-forcing mechanism.
- `G007`: find a restriction which excludes the large-girth cubic obstruction
  to the retired local route.

## Plan and decisive tests

1. Prove the exact saturation reduction without importing a maximality
   convention that is incompatible with edge addition.
2. Test whether the resulting condition is automatic in connected cubic graphs
   of girth at least \(17\).
3. Inspect the witness paths for endpoints of induced two-edge paths, where the
   absence of \(C_4\) supplies the largest number of constrained nonedges.
4. Pivot if saturation yields only non-bipartiteness and no bounded-overlap,
   density, or variable-cycle-length consequence.

## Deductions

### `L008` — Edge-maximal saturation reduction

If a counterexample to `C001` exists, then there is a counterexample \(H\) with
the following properties:

1. \(H\) is maximal, among graphs on its fixed vertex set, subject to having no
   power-of-two cycle;
2. for every nonedge \(xy\), there is an integer \(k\ge2\) and a simple
   \(x,y\)-path in \(H\) of length \(2^k-1\);
3. \(H\) is connected and non-bipartite;
4. \(H\) has average degree below the absolute threshold in `C008`.

Moreover, \(H\) may be chosen with the minimum possible counterexample order.
For such a choice, every nonempty subgraph of \(H\) which omits at least one
vertex has a vertex of degree at most \(2\).

**Proof.** Start with a counterexample \(G\), choosing one of minimum order if
the final assertion is wanted. Repeatedly add a missing edge whenever doing so
does not create a power-of-two cycle. The process terminates because the vertex
set is finite. The terminal graph \(H\) is still simple, has minimum degree at
least \(3\), and contains no power-of-two cycle, so it remains a counterexample
on the same vertex set.

Let \(xy\) be a nonedge of \(H\). By maximality, \(H+xy\) has a cycle of length
\(2^k\) for some \(k\ge2\). This cycle must use the new edge \(xy\), since
\(H\) has no such cycle. Removing \(xy\) from the cycle leaves a simple
\(x,y\)-path in \(H\) of length \(2^k-1\).

If \(H\) were disconnected, an edge between two components could be added
without creating any cycle, contrary to maximality. Thus \(H\) is connected.
If \(H\) were bipartite with classes \(A,B\), the minimum-degree condition
would force each class to contain at least two vertices. Two vertices in the
same class are nonadjacent, but every path between them has even length,
contradicting the odd length \(2^k-1\) supplied above. Thus \(H\) is
non-bipartite. The average-degree conclusion is the contrapositive of `C008`.

Finally, if the starting counterexample has minimum order, so does \(H\). A
nonempty subgraph omitting a vertex and having minimum degree at least \(3\)
would itself be a smaller counterexample, because deleting vertices and edges
creates no cycles. This is impossible. \(\square\)

All witness lengths in item 2 are congruent to \(3\pmod 4\). This modular
strength is retained explicitly; replacing the conclusion by merely “an odd
path” would discard most of the saturation information.

### `L009` — The saturation condition passes the large-girth separation test

There is a finite connected bipartite cubic graph \(B\) of girth at least
\(17\). It satisfies the connected-cubic conclusions used in `L007`, contains
an induced \(P_{13}\), and has no \(C_4,C_8,C_{16}\), but it does not satisfy
the nonedge-path conclusion of `L008`.

**Proof.** Let \(G\) be the finite Hamiltonian cubic graph of girth at least
\(17\) supplied by `C009`. If \(G\) is bipartite, take \(B=G\). Otherwise take
its canonical bipartite double cover, with vertices \((v,0),(v,1)\) and edges
\((u,i)(v,1-i)\) above every edge \(uv\) of \(G\). The cover is finite, simple,
cubic, and bipartite. It is connected because \(G\) is connected and
non-bipartite. A cycle in the cover projects to a nonbacktracking closed walk
of the same length in \(G\), and such a walk contains a cycle no longer than
itself; hence the cover also has girth at least \(17\).

Starting at any vertex of \(B\), take a nonbacktracking walk of twelve edges.
The girth condition makes its vertices distinct, and any chord would create a
cycle of length at most \(13\). It is therefore an induced \(P_{13}\). As in
`A004`, every connected cubic graph satisfies `L002` and `C004`–`C006`, while
the girth excludes \(C_4,C_8,C_{16}\).

On the other hand, two vertices in the same bipartition class are nonadjacent
and every path between them has even length, so no path of length \(2^k-1\)
joins them. Thus `L008` supplies genuinely new global information not shared by
the large-girth cubic obstruction. \(\square\)

### Witnesses around induced two-edge paths

Let \(u-v-w\) be an induced two-edge path in a saturated graph \(H\) from
`L008`. The endpoints \(u,w\) are a nonedge, so a saturation witness is a
simple \(u,w\)-path \(P\) of length \(2^k-1\).

- If \(v\notin V(P)\), then \(P\cup u v w\) is a cycle of length
  \(2^k+1\).
- If \(v\) lies internally on \(P\), splitting \(P\) at \(v\) and adjoining
  \(uv\) or \(vw\) produces one or two cycles, except when the corresponding
  segment is the edge already present.

This exact dichotomy does not yet force a power-of-two cycle: \(2^k+1\) is odd,
and in the second case the two segment lengths can avoid the Mersenne values.
The first local extraction from saturation is therefore insufficient by
itself.

### `L010` — Edges outside odd cycles form a matching

In a saturated counterexample \(H\) supplied by `L008`, the edges which belong
to no odd cycle form a matching.

**Proof.** Suppose two such edges \(uv\) and \(vw\) share the vertex \(v\). The
vertices \(u,w\) cannot be adjacent, because then the triangle \(uvw\) would
be an odd cycle containing both edges. By `L008`, there is a simple
\(u,w\)-path \(P\) of odd length \(2^k-1\).

If \(v\notin V(P)\), then \(P\cup u v w\) is an odd cycle containing both
edges, a contradiction. If \(v\) lies internally on \(P\), let the two
segments of \(P\) from \(u\) to \(v\) and from \(v\) to \(w\) have lengths
\(a\) and \(b\). Since \(a+b\) is odd, one of \(a,b\) is even. If \(a\) is
even, that segment together with \(uv\) is an odd cycle containing \(uv\);
if \(b\) is even, the analogous odd cycle contains \(vw\). Either conclusion
is a contradiction. \(\square\)

Consequently:

- every vertex of \(H\) lies on an odd cycle, because \(\delta(H)\ge3\) and at
  most one edge incident with a vertex can fail to lie on an odd cycle;
- all bridges of \(H\) form a matching;
- every nontrivial block of \(H\) is non-bipartite. Indeed, every cycle
  containing an edge of a block lies in that block, so all edges of a
  bipartite block would lie on no odd cycle; a nontrivial 2-connected block has
  adjacent edges, contradicting the matching conclusion.

### `L011` — Saturated leaf-block reduction

If a counterexample exists, there is a 2-connected power-cycle-free graph
\(B\), with a possibly distinguished vertex \(x\), such that:

1. every vertex in \(B-\{x\}\) has degree at least \(3\) in \(B\), and
   \(d_B(x)\ge2\) when \(x\) is present;
2. \(B\) is non-bipartite;
3. for every nonedge \(uv\) of \(B\) with \(u,v\ne x\), the graph \(B\)
   contains a simple \(u,v\)-path of length \(2^k-1\) for some \(k\ge2\).

**Proof.** Take a saturated counterexample \(H\) from `L008`. If \(H\) is
2-connected, let \(B=H\) and omit \(x\). Otherwise take a leaf block \(B\) in
the block-cut tree and let \(x\) be its unique cut vertex. The proof of `L001`
applies unchanged: the leaf block cannot be a bridge because
\(\delta(H)\ge3\), every vertex other than \(x\) has all its incident edges in
\(B\), and 2-connectivity gives \(d_B(x)\ge2\). By `L010`, \(B\) is
non-bipartite.

Now let \(u,v\in V(B)-\{x\}\) be nonadjacent. They are also nonadjacent in
\(H\), because all edges incident with \(u\) or \(v\) lie in \(B\). Let \(P\)
be their saturation witness from `L008`. A simple \(u,v\)-path cannot leave
\(B\): the only attachment of the leaf block to the rest of \(H\) is \(x\),
so leaving and returning would repeat \(x\). Hence \(P\subseteq B\), proving
the internal saturation conclusion. \(\square\)

`L011` is strictly more informative than applying `L001` alone: it preserves a
global path certificate for every missing edge whose endpoints are not the
exceptional cut vertex. It still does not say that all of \(B\)'s edges or
nonedges have bounded-length witnesses.

### `L012` — A long shortest odd cycle has an external ear

Let \(B\) and the possible exceptional vertex \(x\) be as in `L011`, and let
\(C\) be a shortest odd cycle of \(B\). If \(|C|\ge7\), then some saturation
witness between two vertices of \(C-\{x\}\) is not contained in \(C\).
Consequently, the union of that witness with \(C\) contains a \(C\)-ear: a path
of positive length whose endpoints are distinct vertices of \(C\) and whose
internal vertices lie outside \(C\).

**Proof.** First, \(C\) is induced. A chord would split \(C\) into two cycles,
one of which is odd and strictly shorter than \(C\).

Write \(q=|C|\). For two vertices at cyclic distance \(2\), the two paths
within \(C\) have lengths \(2\) and \(q-2\); the only odd one has length
\(q-2\). For two vertices at cyclic distance \(4\), the corresponding odd arc
has length \(q-4\). The odd integers \(q-2\) and \(q-4\) differ by \(2\), while
two distinct numbers of the form \(2^k-1\), \(k\ge2\), differ by at least
\(4\). Hence at least one of \(q-2,q-4\) is not of the form \(2^k-1\).

Choose a pair at the corresponding cyclic distance whose endpoints avoid
\(x\); among the \(q\ge7\) pairs at that distance, at most two use \(x\).
The pair is nonadjacent. By `L011` it has a Mersenne-length witness \(P\) in
\(B\). Because \(C\) is induced and neither of its two arcs has the witness
length, \(P\) is not contained in \(C\). Between two consecutive occurrences
of vertices of \(C\) along \(P\), some subpath therefore has all internal
vertices outside \(C\). That subpath is a \(C\)-ear. \(\square\)

The restriction \(|C|\ge7\) exposes the genuine exceptional cases rather than
hiding them: on \(C_5\), every distance-two pair is already joined around the
cycle by a 3-edge path, while a triangle has no nonedge among its vertices.
This is a limitation of the *saturation-witness* argument, not of ear
existence itself.

### `L013` — Every shortest odd cycle has an external ear

For every shortest odd cycle \(C\) in the block \(B\) from `L011`, including
when \(|C|=3\) or \(5\), the graph \(B\) has a \(C\)-ear with internal vertices
outside \(C\).

**Proof.** The cycle \(C\) is induced, as in `L012`. The graph \(B\) is not
equal to \(C\): if it were, every vertex of \(C\) would have degree \(2\), while
at least two vertices are different from the possible exceptional vertex
\(x\) and must have degree at least \(3\) by `L011`.

Let \(D\) be a component of \(B-V(C)\). Because \(B\) is 2-connected, \(D\)
has at least two distinct neighbors on \(C\); a unique attachment vertex would
be a cut vertex of \(B\). A shortest path through \(D\) between two distinct
attachment vertices, including the two attachment edges, is a \(C\)-ear.
\(\square\)

Unlike `L012`, this lemma supplies no Mersenne-length witness containing the
ear in the triangle and \(5\)-cycle cases.

### `L014` — One-ear theta lengths are insufficient

The facts that \(C\) is a shortest odd cycle and that one \(C\)-ear exists do
not, by themselves, force a power-of-two cycle.

**Proof.** For every integer \(r\ge2\), take a theta graph whose three
internally disjoint paths between its branch vertices have lengths
\[
  2,\qquad 2r+1,\qquad 4.
\]
Its only cycle lengths are
\[
  2r+3,\qquad 2r+5,\qquad 6.
\]
The first two are odd and the last is not a power of two. The cycle formed by
the paths of lengths \(2\) and \(2r+1\) is a shortest odd cycle, and the
4-edge path is an external ear. Thus the abstract theta length equations admit
an infinite family with no power-of-two cycle. \(\square\)

This example is not a graph satisfying `L011`: its internal path vertices have
degree \(2\). It refutes only the proposed implication from one-ear theta
lengths. Any successful use of `L012` must retain the stronger fact that the
ear occurs inside a full Mersenne-length saturation witness, including the
witness's other intersections with \(C\).

### `L015` — One-excursion witnesses admit power-free families in every configuration

Let \(B\), the possible exceptional vertex \(x\), the shortest odd cycle \(C\)
of length \(q\ge7\), and the `L012` pair \(u,w\in V(C)-\{x\}\) at cyclic
distance \(d\in\{2,4\}\) with \(q-d\) not of the form \(2^j-1\), \(j\ge2\), be
as before, and let \(P\) be a saturation witness for \(u,w\): a simple
\(u,w\)-path of length \(2^k-1\), \(k\ge2\). Assume the vertices of \(P\)
outside \(C\) span exactly one component of \(P-V(C)\).

**Decomposition.** Then \(P=A_1\cdot Q\cdot A_2\), where \(A_1\) is a possibly
trivial arc of \(C\) from \(u\) to a vertex \(a\); \(Q\) is an \(a,b\)-path of
length \(\ell\ge2\) whose internal vertices avoid \(C\); \(A_2\) is a possibly
trivial arc of \(C\) from \(b\) to \(w\); and \(A_1,A_2\) are vertex-disjoint.

*Proof.* \(C\) is induced, as shown in `L012`, so any subpath of \(P\) all of
whose vertices lie on \(C\) uses only edges of \(C\) and follows an arc of
\(C\). Deleting \(V(C)\) from the path \(P\) leaves exactly the interiors of
the maximal off-cycle stretches of \(P\); by hypothesis there is one such
stretch \(Q\). Its two boundary vertices \(a,b\) lie on \(C\) because the ends
\(u,w\) of \(P\) do. The portions of \(P\) before \(a\) and after \(b\) lie
wholly on \(C\) and are arcs \(A_1\ni u\), \(A_2\ni w\); they are disjoint
because \(P\) is simple, and \(\ell\ge2\) because \(Q\) has an internal
vertex. \(\square\)

**Cycle inventory.** \(C\cup P=C\cup Q\) is a theta graph: the two arcs of
\(C\) between \(a\) and \(b\), of lengths \(s\) and \(q-s\), and \(Q\) are
three internally disjoint \(a,b\)-paths, and only \(a,b\) have degree \(3\).
A cycle avoiding both branch vertices would lie in the acyclic interior of one
path; a cycle containing an edge of one of the three segments contains that
whole segment, and at a branch vertex it uses exactly two of the three
segments. Hence \(C\cup Q\) has exactly three cycles, of lengths
\[
  q,\qquad \ell+s,\qquad \ell+q-s .
\]
Since \((\ell+s)+(\ell+q-s)=2\ell+q\) is odd, exactly one of the two new
lengths is even.

**Exact one-witness constraint system.** Writing \(\alpha=|A_1|\ge0\) and
\(\beta=|A_2|\ge0\), the full data of a one-excursion witness satisfies
precisely:

1. \(\alpha+\ell+\beta=2^k-1\) with \(\ell\ge2\);
2. the even member of \(\{\ell+s,\ \ell+q-s\}\) is not a power of two, and the
   odd member is at least \(q\), because \(C\) is a shortest odd cycle in the
   power-cycle-free graph \(B\);
3. the placement relations on \(C\): \(A_1\) and \(A_2\) are disjoint arcs
   containing \(u\) and \(w\) at cyclic distance \(d\), and \(s\) is an
   \(a,b\)-arc length. Up to reversing \(P\) and reflecting \(C\), the
   placements fall into the types: **T1**, both arcs trivial
   (\(a=u\), \(b=w\)); **T2**, exactly one arc trivial, with \(a\) on the far
   side of \(u\) from \(w\) (*aligned*) or between \(u\) and \(w\)
   (*crossed*); **T3**, both arcs nontrivial, aligned or crossed by the same
   dichotomy.

**Families.** In every type the system has infinitely many solutions, realized
by the standalone theta graphs \(C\cup Q\), which contain every vertex, edge,
and cycle that the one-witness constraints mention. Vertices of \(C\) are
numbered \(c_0,\ldots,c_{q-1}\) with \(u=c_0\), \(w=c_d\).

| Type | \(q\) | \(d\) | placement | \(\ell\) | cycle lengths | valid for |
|---|---|---|---|---|---|---|
| T1 | \(7\) | \(2\) | \(a=c_0\), \(b=c_2\), \(s=2\) | \(2^k-1\) | \(7,\ 2^k+1,\ 2^k+4\) | \(k\ge3\) |
| T1, \(d=4\) | \(9\) | \(4\) | \(a=c_0\), \(b=c_4\), \(s=4\) | \(2^k-1\) | \(9,\ 2^k+3,\ 2^k+4\) | \(k\ge3\) |
| T2 aligned | \(11\) | \(2\) | \(A_1=c_0c_{10}c_9c_8\), \(b=c_2\), \(s=5\) | \(2^k-4\) | \(11,\ 2^k+1,\ 2^k+2\) | \(k\ge4\) |
| T2 crossed | \(11\) | \(2\) | \(A_1=c_0c_1\), \(b=c_2\), \(s=1\) | \(2^k-2\) | \(11,\ 2^k-1,\ 2^k+8\) | \(k\ge4\) |
| T3 aligned | \(11\) | \(2\) | \(A_1=c_0c_{10}\), \(A_2=c_3c_2\), \(s=7\) | \(2^k-3\) | \(11,\ 2^k+1,\ 2^k+4\) | \(k\ge4\) |
| T3 crossed | \(11\) | \(2\) | \(A_1=c_0c_1\), \(A_2=c_5c_4c_3c_2\), \(s=4\) | \(2^k-5\) | \(11,\ 2^k-1,\ 2^k+2\) | \(k\ge4\) |

*Verification.* In each row \(q-d\in\{5,9\}\) is not of the form \(2^j-1\);
at \(q=9\) the arc \(q-2=7\) is Mersenne, so \(d=4\) is exactly the choice
`L012` makes there. The totals \(\alpha+\ell+\beta\) equal
\(2^k-1\): row by row,
\(0+(2^k-1)+0\), \(0+(2^k-1)+0\), \(3+(2^k-4)+0\), \(1+(2^k-2)+0\),
\(1+(2^k-3)+1\), \(1+(2^k-5)+3\). The listed \(s\) values are the
\(a,b\)-arc lengths on \(C\), and the two theta lengths are
\(\ell+s\) and \(\ell+q-s\). In every row the odd new length
(\(2^k+1\), \(2^k+3\), or \(2^k-1\)) is at least \(q\) in the stated range of
\(k\), and the even new length lies strictly between consecutive powers of
two: \(2^k<2^k+2,\,2^k+4<2^{k+1}\) for \(k\ge3\), and
\(2^k<2^k+8<2^{k+1}\) for \(k\ge4\). Each theta graph is simple
(\(\ell\ge2\)), its cycle \(C\) is induced and is a shortest odd cycle, and
\(u,w\) are nonadjacent. \(\square\)

Two delimiting remarks. First, the constraints are not vacuous: in the T2
crossed row the instance \(k=3\) would force the even cycle length
\(2^3+8=16\), so that sporadic parameter choice genuinely cannot occur in a
counterexample. The classification eliminates isolated tuples but never a
whole family. Second, as in `L014`, every family member has internal vertices
of degree \(2\), so none satisfies `L011`; the graphs refute the proposed
forcing implication and are not counterexamples to `C001`.

**Conclusion.** Retaining the entire one-excursion witness — its total
Mersenne length, both cycle arcs, both gaps, the shortest-odd-cycle bound, and
the non-Mersenne arc choice from `L012` — still admits infinitely many
power-free length patterns in every configuration type. One-excursion witness
data cannot force a power-of-two cycle.

### `L016` — A two-excursion witness pattern also admits infinite power-free families

For every \(k\ge4\), let \(G_k\) be the graph obtained from a \(7\)-cycle
\(C=c_0c_1\cdots c_6\) by adding two vertex-disjoint paths \(Q_1\) from
\(c_0\) to \(c_4\) and \(Q_2\) from \(c_5\) to \(c_2\), each of length
\(2^{k-1}-1\), internally disjoint from \(C\) and from each other. Then:

1. \(P=Q_1\cdot c_4c_5\cdot Q_2\) is a simple \(c_0,c_2\)-path of length
   \((2^{k-1}-1)+1+(2^{k-1}-1)=2^k-1\) whose vertices outside \(C\) form
   exactly two components, the interiors of \(Q_1\) and \(Q_2\); the ends
   \(c_0,c_2\) are nonadjacent at cyclic distance \(2\), and \(q-2=5\) is not
   Mersenne;
2. \(G_k\) has exactly seven cycles, of lengths
   \(7\); \(2^{k-1}+3\) twice; \(2^{k-1}+2\) twice; \(2^k+1\); \(2^k+2\);
3. \(G_k\) contains no power-of-two cycle, and \(C\) is a shortest odd cycle.

**Proof.** Suppressing degree-\(2\) vertices, \(G_k\) contracts to the
multigraph on the four branch vertices \(c_0,c_2,c_4,c_5\) whose six edges
are the four arcs of \(C\) they determine — \(c_0c_2\) through \(c_1\)
(length \(2\)), \(c_2c_4\) through \(c_3\) (length \(2\)), \(c_4c_5\)
(length \(1\)), \(c_5c_0\) through \(c_6\) (length \(2\)) — together with
\(Q_1=c_0c_4\) and \(Q_2=c_2c_5\) of length \(2^{k-1}-1\) each. This is
\(K_4\). A cycle of \(G_k\) containing an edge of a segment contains the whole
segment, so cycles of \(G_k\) correspond exactly to cycles of \(K_4\): four
triangles and three quadrilaterals. Their lengths are:

- \(\{c_0,c_2,c_4\}\): \(2+2+(2^{k-1}-1)=2^{k-1}+3\);
- \(\{c_0,c_2,c_5\}\): \(2+(2^{k-1}-1)+2=2^{k-1}+3\);
- \(\{c_0,c_4,c_5\}\): \((2^{k-1}-1)+1+2=2^{k-1}+2\);
- \(\{c_2,c_4,c_5\}\): \(2+1+(2^{k-1}-1)=2^{k-1}+2\);
- arcs only: \(2+2+1+2=7\), the cycle \(C\);
- \(Q_2\) and \(Q_1\) with arcs \(c_0c_2\), \(c_4c_5\):
  \(2+(2^{k-1}-1)+1+(2^{k-1}-1)=2^k+1\);
- \(Q_1\) and \(Q_2\) with arcs \(c_2c_4\), \(c_5c_0\):
  \((2^{k-1}-1)+2+(2^{k-1}-1)+2=2^k+2\).

For \(k\ge4\) the odd lengths \(7\), \(2^{k-1}+3\), \(2^k+1\) are all at least
\(7\) with the minimum attained only by \(C\), and the even lengths
\(2^{k-1}+2\) and \(2^k+2\) lie strictly between consecutive powers of two.
Hence no cycle length is a power of two and \(C\) is a shortest odd cycle. At
\(k=4\) the seven lengths are \(7,11,11,10,10,17,18\). \(\square\)

The same scope limitation applies: \(c_1,c_3,c_6\) and the path interiors
have degree \(2\), so \(G_k\) does not satisfy `L011`. The lemma refutes
forcing from full two-excursion witness data; it is not a counterexample to
`C001`.

### Sparsity remark on finite witness patterns

*Heuristic, not a claim.* In `L014`–`L016` every even cycle length is an
affine expression \(c+\ell\) with unit coefficient in a free segment length,
the offset \(c\) being fixed by the configuration. Because the gap between
consecutive powers of two grows without bound, each such family contains
infinitely many power-free choices, and any witness diagram with a bounded
number of segments has this shape. Heuristically, no fixed finite pattern of
witnesses can force a power-of-two cycle; a decisive mechanism must either
couple an unbounded number of witnesses — the saturated graph constrains all
of its nonedges simultaneously — or generate an interval of even cycle
lengths. This intuition guides route selection only; it resolves nothing and
must not be cited in a proof.

## Failure analysis

- `C008` supplies an upper bound on the average degree of \(H\), not the lower
  bound needed for an immediate density contradiction.
- A witness for an induced two-edge path may run through its middle vertex;
  even when it avoids that vertex, it closes a cycle of length \(2^k+1\), not a
  forbidden power of two.
- `L014` shows that the three cycle lengths of a shortest odd cycle plus one
  arbitrary ear admit infinite power-free families. Ear existence and parity
  alone are therefore insufficient.
- `L015` closes the proposed refinement of `L014`: even the *full*
  one-excursion witness — total Mersenne length, both arcs, both gaps, the
  shortest-odd-cycle bound — admits infinite power-free families in every
  configuration type. `L016` does the same for a two-excursion pattern. The
  recorded pivot condition for single-witness forcing is therefore met.
- The saturation reduction is global, but by the sparsity remark its decisive
  use cannot come from any bounded witness diagram. The surviving mechanisms
  are coupling unboundedly many witnesses at once, or generating an interval
  of even cycle lengths.

## Salvageable results

- `L008` gives a clean equivalent target class for a failure-first attack.
- `L009` verifies that the new condition is not another property automatically
  shared by the cubic large-girth family.
- `L010` forces odd cycles to cover all but a matching of the edges.
- `L011` combines saturation with the 2-connected leaf-block reduction and
  prevents witness paths between nonexceptional block vertices from escaping
  through the cut vertex.
- `L012` forces an external ear from every shortest odd cycle of length at
  least \(7\), leaving triangles and \(5\)-cycles as the explicit short cases.
- `L013` supplies an external ear in the triangle and \(5\)-cycle cases from
  2-connectivity, but without a Mersenne-witness certificate.
- `L014` rules out one-ear theta length equations as a sufficient mechanism.
- `L015`–`L016` complete that separation for full one- and two-excursion
  witness data, so future work need not revisit any bounded single-witness
  pattern.
- The two-edge-path dichotomy identifies witness overlap, rather than path
  existence, as the immediate obstruction.
- At orders \(n\le15\) the saturation witnesses collapse to lengths
  \(3\) and \(7\), because a path of length \(15\) needs \(16\) vertices, and
  the only excludable power cycles are \(C_4\) and \(C_8\). Combined with the
  minimum-order addendum of `L008` and the order bound `L006`, this makes
  "no saturated counterexample of order \(11\)" a finitely checkable
  statement whose truth would lift every counterexample's order to \(12\).
  This is the strongest concrete use of saturation now visible.

## Exit state

- Status: completed
- Promoted records: `L008`–`L016` in `CLAIMS.md`
- Outcome: saturation is established as a genuine global reduction
  (`L008`–`L013`) and definitively delimited as a forcing mechanism at the
  single-witness level (`L014`–`L016`). `G008` is resolved on its obstruction
  horn; the forcing gap `G007` remains open.
- Next action: run an exhaustive order-\(11\) search for saturated
  counterexamples — minimum degree \(3\), no \(C_4\) or \(C_8\), and a simple
  path of length \(3\) or \(7\) across every nonedge; either prove none
  exists, lifting the counterexample lower bound to twelve vertices, or
  record the survivors.
