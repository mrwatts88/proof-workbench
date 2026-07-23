# A001 — Maximum-degree and neighborhood structure

- Date opened: 2026-07-23
- Problem: `P-001`
- Status: succeeded — integrated candidate produced

## Intended mechanism

Assume no universal vertex and use the unique-common-neighbor condition to force
successively stronger degree regularity. Once the graph is regular, translate the
condition into an exact adjacency-matrix identity and derive an arithmetic
contradiction.

## Entry assumptions

- `STATEMENT.md` version 0.2.
- For contradiction, no vertex is adjacent to every other vertex.
- No external theorem, reference, or known solution is used.

## Targeted obligations

- `G002`: produce a self-contained proof or disproof of `C001`.

## Plan and decisive tests

1. Inspect the graph induced by the neighbors of one vertex; test whether the
   common-neighbor uniqueness controls its internal degrees.
2. Compare the degrees of two nonadjacent vertices by constructing an injection
   between their neighborhoods.
3. Test whether the complement of a graph with no universal vertex can be
   disconnected.
4. If those tests force regularity, encode length-two walk counts in the
   adjacency matrix and check whether the resulting integer constraints are
   consistent.

## Deductions

### `L001` — Every vertex degree is even

Fix \(v\). For each \(u\in N(v)\), the unique common neighbor of \(u\) and \(v\)
is exactly the unique neighbor of \(u\) inside the induced graph \(G[N(v)]\).
Thus every vertex of \(G[N(v)]\) has degree one. This induced graph is a disjoint
union of edges, so \(\lvert N(v)\rvert=d(v)\) is even.

### `L002` — Nonadjacent vertices have equal degree

Let \(u,v\) be nonadjacent and let \(w\) be their unique common neighbor. For
each \(x\in N(u)\setminus\{w\}\), let \(f(x)\) be the unique common neighbor of
\(x\) and \(v\). Then \(f(x)\in N(v)\), and \(f(x)\ne u\) because \(u\) is not
adjacent to \(v\).

The map \(f:N(u)\setminus\{w\}\to N(v)\) is injective. If distinct \(x_1,x_2\)
had \(f(x_1)=f(x_2)=y\), then both \(u\) and \(y\) would be common neighbors of
\(x_1,x_2\), and \(y\ne u\), contradicting uniqueness. Hence
\[
  d(u)-1\le d(v).
\]
Interchanging \(u,v\) gives \(d(v)-1\le d(u)\). The two degrees are even by
`L001`, so they are equal.

### `L003` — Under the counterexample assumption, the complement is connected

Because no vertex is universal, the complement \(\overline G\) has no isolated
vertex. Suppose it is disconnected. Let \(X\) be the vertex set of one component
and let \(Y=V\setminus X\). Both sets have at least two vertices, and every
cross-pair \(xy\), \(x\in X,y\in Y\), is an edge of \(G\).

For such \(x,y\), their common neighbors are exactly
\[
  \bigl(N_G(x)\cap X\bigr)\ \dot\cup\
  \bigl(N_G(y)\cap Y\bigr).
\]
Therefore
\[
  d_{G[X]}(x)+d_{G[Y]}(y)=1
\]
for every \(x\in X,y\in Y\). It follows that one of the two displayed internal
degrees is constantly zero and the other constantly one. If \(G[X]\) has
internal degree zero, any two distinct vertices of \(X\) have every vertex of
\(Y\) as a common neighbor, at least two of them. If \(G[Y]\) has internal
degree zero, the symmetric contradiction uses two vertices of \(Y\) and all
vertices of \(X\). Thus \(\overline G\) is connected.

### `L004` — Under the counterexample assumption, \(G\) is regular

Consecutive vertices on a path in \(\overline G\) are nonadjacent in \(G\), so
`L002` gives them equal degree. Connectedness from `L003` propagates this equality
to all vertices. Write their common degree as \(k\).

### `L005` — The regular counterexample is impossible

Let \(n=\lvert V\rvert\), let \(A\) be the adjacency matrix, let \(J\) be the
all-ones matrix, and let \(I\) be the identity. Off the diagonal,
\((A^2)_{uv}\) counts common neighbors and equals one; on the diagonal it equals
the degree \(k\). Hence
\[
  A^2=J+(k-1)I. \tag{1}
\]
For the all-ones vector \(\mathbf 1\), regularity gives
\(A\mathbf 1=k\mathbf 1\). Applying (1) to \(\mathbf 1\) gives
\[
  k^2=n+k-1. \tag{2}
\]

The counterexample assumption excludes the singleton case. The hypothesis gives
each vertex a neighbor when \(n>1\), and `L001` makes \(k\) even, so \(k\ge2\).
Put \(s=\sqrt{k-1}>0\) and
\[
  W=\{z\in\mathbb R^n:\mathbf 1^{\mathsf T}z=0\}.
\]
The space \(W\) is invariant under \(A\), because
\(\mathbf 1^{\mathsf T}Az=(A\mathbf 1)^{\mathsf T}z=0\). On \(W\), equation
(1) gives \(A^2=s^2I\). Every \(z\in W\) therefore decomposes as
\[
  z=z_++z_-,\qquad
  z_\pm=\tfrac12(z\pm Az/s),
\]
with \(Az_+=sz_+\) and \(Az_-=-sz_-\). Thus \(W\) is the direct sum of the
\(+s\) and \(-s\) eigenspaces. Let their integer dimensions be \(p,q\).

Using a basis made from \(\mathbf 1\) and bases of these two eigenspaces, while
also using that the diagonal of \(A\) is zero, gives
\[
  0=\operatorname{tr}(A)=k+(p-q)s. \tag{3}
\]
Here basis-independence of trace follows directly from
\(\operatorname{tr}(BC)=\operatorname{tr}(CB)\), obtained by expanding both
traces as \(\sum_{i,j}B_{ij}C_{ji}\).
If \(p=q\), equation (3) says \(k=0\), impossible. Otherwise (3) makes \(s\)
rational. Since \(s^2=k-1\) is an integer, writing \(s\) in lowest terms shows
that \(s\) is a positive integer. Equation (3) then says \(s\mid k\), while
\(k=s^2+1\); hence \(s\mid1\), so \(s=1\) and \(k=2\). Equation (2) now gives
\(n=3\). A simple 2-regular graph on three vertices is \(K_3\), whose vertices
are universal, contradicting the counterexample assumption.

The contradiction proves `C001`.

## Failure analysis

The initial “maximum-degree” framing was not needed: the injection in `L002`
gives exact equality across every nonedge once combined with degree parity.
No failed mathematical step remains in the promoted route.

## Salvageable results

- `L001`–`L004` are purely combinatorial.
- The matrix step uses only the explicit identity (1), invariant subspace
  arithmetic, and trace; it does not invoke an external spectral theorem.
- The proof depends on finiteness in the matrix and complement-path arguments.

## Exit state

- Status: succeeded — awaiting adversarial review
- Promoted records: `L001`–`L005` in `CLAIMS.md`; integrated candidate in
  `PROOF.md`
- Next action: conduct a clean-context statement-correspondence and line-by-line
  logic review of the candidate
