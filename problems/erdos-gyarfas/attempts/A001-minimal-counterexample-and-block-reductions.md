# A001 — Minimal-counterexample and block reductions

- Date opened: 2026-07-23
- Problem: `P-002`
- Status: active

## Intended mechanism

Assume a counterexample, replace it by a minimal or 2-connected object without
creating any new cycles, and combine the absence of a \(4\)-cycle with the
minimum-degree hypothesis. The hoped-for mechanism is that these local
restrictions eventually force a cycle of length \(8,16,\ldots\).

## Entry assumptions

- `D001`–`D004` from `STATEMENT.md`.
- For the conditional deductions, \(G\) is a counterexample: it is finite,
  simple, has \(\delta(G)\ge 3\), and has no cycle of length \(2^k\) for any
  \(k\ge 2\).

## Targeted obligations

- `G002`: exploit the 2-connected near-minimum-degree reduction.
- `G003`: turn the absence of \(4\)-cycles into a longer power-of-two cycle.

## Plan and decisive tests

1. Audit the block-cut-tree reduction at bridge blocks and at the exceptional
   cut vertex.
2. Minimize the number of edges and determine whether this really forces a
   cubic graph.
3. Double-count common-neighbor pairs to obtain an exact small-order bound.
4. Examine endpoints of a longest path to see exactly which cycle lengths are
   forced.

## Deductions

### `L001` — Leaf-block reduction

Every counterexample contains a 2-connected subgraph \(B\) in which all vertices
except possibly one have degree at least \(3\) within \(B\), and the possible
exception has degree at least \(2\) within \(B\). The subgraph \(B\) is itself
free of power-of-two cycles.

**Proof.** Work in one connected component \(H\) of the counterexample; it still
has minimum degree at least \(3\). If \(H\) is 2-connected, take \(B=H\).
Here “2-connected” means having at least three vertices and remaining connected
after deletion of any one vertex.

For completeness, define a block of \(H\) to be a maximal 2-connected subgraph
or a bridge edge, and form the bipartite incidence graph \(T\) whose other
vertices are the cut vertices of \(H\). The graph \(T\) is connected because
\(H\) is connected. It is acyclic: an incidence cycle would give, for a block
on a shortest such cycle, a path between its two incident cut vertices whose
internal vertices lie outside the block (any additional intersection would
shorten the incidence cycle). For a bridge block this contradicts that the edge
is a bridge; for a 2-connected block, adjoining that path is an ear and
produces a strictly larger 2-connected subgraph: after deleting any one vertex,
the old block remains connected (if applicable), and each remaining piece of
the added path is still attached at an endpoint. This contradicts maximality.
Thus \(T\) is a finite tree. Every cut-vertex node of \(T\) has degree at least
two, so a leaf of \(T\) is a block node. If \(T\) has just one block, it cannot
be a bridge because \(\delta(H)\ge3\), and \(H\) itself is 2-connected.
Otherwise choose a leaf block. It cannot be a bridge block \(K_2\): its endpoint
which is not the unique incident cut vertex belongs to no other block and would
have degree \(1\) in \(H\), contrary to \(\delta(H)\ge3\). Hence this leaf block
\(B\) is 2-connected.

It contains at most one cut vertex \(x\) of \(H\). Every \(v\in V(B)\setminus
\{x\}\) has all of its incident edges in \(B\), because membership in another
block would make \(v\) a cut vertex. Thus \(d_B(v)=d_H(v)\ge 3\).
The possible exceptional vertex \(x\) has \(d_B(x)\ge 2\), since \(B\) is
2-connected. Finally, every cycle of \(B\) is a cycle of \(H\), so \(B\) has no
power-of-two cycle. \(\square\)

### `L002` — Structure of an edge-minimal counterexample

There is a connected counterexample \(G\) such that every edge has an endpoint
of degree exactly \(3\). In particular, the vertices of degree at least \(4\)
form an independent set.

**Proof.** Choose a counterexample with the fewest edges. If it were
disconnected, any one of its components would still have minimum degree at
least \(3\), would contain no new cycle, and would have fewer edges. Thus it is
connected. If an edge \(uv\) had \(d_G(u),d_G(v)\ge 4\), then \(G-uv\) would
still have minimum degree at least \(3\). Deleting an edge cannot create a
cycle, so \(G-uv\) would be a smaller counterexample, a contradiction.
\(\square\)

This does **not** show that a minimal counterexample is cubic: vertices of degree
at least \(4\) may remain, provided no two are adjacent.

### `L003` — Every counterexample has at least nine vertices

**Proof.** A counterexample has no \(4\)-cycle. Therefore any two vertices have
at most one common neighbor: two distinct common neighbors would be the
opposite vertices of a \(4\)-cycle. Count pairs
\[
  (v,\{x,y\})\quad\text{with }x\ne y\text{ and }x,y\in N(v).
\]
The count by \(v\) is
\[
  \sum_{v\in V(G)}\binom{d(v)}2,
\]
while the common-neighbor observation bounds it above by \(\binom n2\), where
\(n=|V(G)|\). Since \(d(v)\ge 3\), the lower bound is \(3n\). This rules out
\(n\le 6\). At \(n=7\), equality would force every vertex to have degree \(3\),
which is impossible because the degree sum \(21\) is odd.

Suppose \(n=8\). The same inequality is
\[
  \sum_v\binom{d(v)}2\le 28.
\]
A vertex of degree at least \(5\), together with seven degrees of at least \(3\),
would give at least \(10+7\cdot3=31\). Hence every degree is \(3\) or \(4\).
If \(t\) vertices have degree \(4\), the left side is at least \(24+3t\), so
\(t\le1\). The degree sum is \(24+t\), which must be even; therefore \(t=0\),
and \(G\) is cubic.

Fix \(v\) with \(N(v)=\{a,b,c\}\), and let \(R\) be the other four vertices.
The graph induced by \(\{a,b,c\}\) has maximum degree at most \(1\), since a
two-edge path \(a-b-c\) there would give the \(4\)-cycle \(v-a-b-c-v\).
If that induced graph has no edge, \(a,b,c\) require six edges to \(R\).
But no vertex of \(R\) can meet two of \(a,b,c\), again because that would give
a \(4\)-cycle through \(v\), so at most four such edges exist: a contradiction.
If the induced graph has one edge, say \(ab\), then \(a,b,c\) require exactly
four edges to \(R\). These must give every vertex of \(R\) exactly one neighbor
among \(a,b,c\). Cubicity then makes the graph induced by \(R\) 2-regular. A
simple 2-regular graph on four vertices is a \(4\)-cycle, again a contradiction.
Thus \(n\ne8\), proving \(n\ge9\). \(\square\)

### `L004` — Longest-path endpoint restriction

Let \(P=v_0v_1\cdots v_\ell\) be any longest path in a counterexample. Every
neighbor of \(v_0\) lies on \(P\). Moreover,
\[
  v_0v_i\in E(G),\quad i\ge2
  \quad\Longrightarrow\quad
  i\ne 2^k-1\ \text{for all }k\ge2.
\]
Indeed, a neighbor outside \(P\) would extend the path, and an edge \(v_0v_i\)
closes the path segment \(v_0v_1\cdots v_i\) into a cycle of length \(i+1\).
The endpoint \(v_0\) consequently has at least two neighbors \(v_i\) with
\(i\ge2\), but all their indices avoid \(3,7,15,\ldots\).

## Failure analysis

- Edge minimality does not force 3-regularity; it only makes the
  degree-\(\ge4\) vertices independent.
- The block reduction introduces one possible degree-2 vertex, so the original
  conjecture cannot simply be reapplied to the selected block.
- The longest-path argument forces several cycle lengths but does not control
  their indices densely enough to hit a power of two.
- The common-neighbor count exploits only the forbidden \(4\)-cycle and stops
  giving a contradiction once \(n\ge9\).

## Salvageable results

- `L001` gives a precise 2-connected near-minimum-degree target.
- `L002` isolates all high-degree vertices in an edge-minimal counterexample.
- `L003` is a proof, independent of computation, that any counterexample has at
  least nine vertices.
- `L004` translates the conjecture into forbidden Mersenne-index chords at
  endpoints of longest paths.

## Exit state

- Status: active
- Promoted records: `L001`–`L004` in `CLAIMS.md`.
- Next action: combine `L001` and `L002` with exact enumeration of
  \(C_4\)-free graphs beginning at order \(9\), looking for a structural
  invariant that forces an \(8\)- or \(16\)-cycle.
