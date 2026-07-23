# Integrated proof or disproof candidate

- Statement version: 0.2
- Candidate status: self-contained proof candidate; not yet adversarially reviewed

## Dependency outline

- `L001`: every degree is even.
- `L002`: nonadjacent vertices have equal degree, using `L001`.
- `L003`: without a universal vertex, the complement is connected.
- `L004`: `L002` and `L003` force regularity.
- `L005`: the adjacency-matrix identity rules out a regular counterexample.
- `C001`: follows by contradiction from `L005`, with the singleton boundary case
  handled separately.

## Argument

### 1. Boundary case and contradiction setup

If \(\lvert V\rvert=1\), its sole vertex is adjacent to every other vertex
vacuously. Hence assume, for contradiction, that \(G\) has no vertex adjacent to
every other vertex. In particular, \(\lvert V\rvert>1\).

### 2. Every degree is even (`L001`)

Fix \(v\in V\). For each \(u\in N(v)\), the unique common neighbor of \(u\) and
\(v\) is precisely the unique neighbor of \(u\) in the induced graph
\(G[N(v)]\). Thus every vertex of \(G[N(v)]\) has degree one. Its vertices pair
into disjoint edges, so
\[
  d(v)=\lvert N(v)\rvert
\]
is even.

### 3. Nonadjacent vertices have equal degree (`L002`)

Let \(u,v\) be nonadjacent, and let \(w\) be their unique common neighbor. For
each \(x\in N(u)\setminus\{w\}\), let \(f(x)\) be the unique common neighbor of
\(x\) and \(v\). Then \(f(x)\in N(v)\), and \(f(x)\ne u\) because \(u\) is not
adjacent to \(v\).

This map is injective. Indeed, if distinct \(x_1,x_2\) had
\(f(x_1)=f(x_2)=y\), then \(u\) and \(y\) would be two distinct common
neighbors of \(x_1,x_2\). Consequently
\[
  d(u)-1\le d(v).
\]
The symmetric construction gives \(d(v)-1\le d(u)\). Since both degrees are even
by `L001`, \(d(u)=d(v)\).

### 4. A counterexample has connected complement (`L003`)

Under the contradiction assumption, every vertex has a nonneighbor, so
\(\overline G\) has no isolated vertex. Suppose \(\overline G\) were
disconnected. Let \(X\) be one component and \(Y=V\setminus X\). Both \(X\) and
\(Y\) have at least two vertices, and every vertex of \(X\) is adjacent in \(G\)
to every vertex of \(Y\).

For \(x\in X,y\in Y\), the common neighbors of \(x,y\) are exactly
\[
  \bigl(N_G(x)\cap X\bigr)\ \dot\cup\
  \bigl(N_G(y)\cap Y\bigr).
\]
Their uniqueness implies
\[
  d_{G[X]}(x)+d_{G[Y]}(y)=1
  \qquad(x\in X,\ y\in Y). \tag{1}
\]
Thus the first internal degree is a constant \(a\), the second a constant \(b\),
and \(a+b=1\). If \(a=0\), two distinct vertices of \(X\) have all
\(\lvert Y\rvert\ge2\) vertices of \(Y\) as common neighbors. If \(b=0\), two
distinct vertices of \(Y\) have all \(\lvert X\rvert\ge2\) vertices of \(X\) as
common neighbors. Either case contradicts the hypothesis. Therefore
\(\overline G\) is connected.

### 5. A counterexample is regular (`L004`)

The endpoints of each edge in \(\overline G\) are nonadjacent in \(G\), hence
have equal degree by `L002`. Along complement paths, connectedness propagates
this equality to every vertex. Thus \(G\) is \(k\)-regular for some \(k\).

### 6. The regular case is impossible (`L005`)

Let \(n=\lvert V\rvert\), and let \(A,J,I\) be respectively the adjacency,
all-ones, and identity matrices of order \(n\). For distinct \(u,v\),
\((A^2)_{uv}\) counts their common neighbors and equals one; while
\((A^2)_{uu}=d(u)=k\). Therefore
\[
  A^2=J+(k-1)I. \tag{2}
\]
Writing \(\mathbf 1\) for the all-ones vector, regularity gives
\(A\mathbf 1=k\mathbf 1\). Apply (2) to \(\mathbf 1\):
\[
  k^2=n+k-1. \tag{3}
\]

Because \(n>1\), the hypothesis gives every vertex at least one neighbor; `L001`
then gives \(k\ge2\). Set \(s=\sqrt{k-1}>0\) and
\[
  W=\{z\in\mathbb R^n:\mathbf 1^{\mathsf T}z=0\}.
\]
Since \(G\) is undirected, \(A\) is symmetric. This subspace is invariant under
\(A\), since for \(z\in W\),
\[
  \mathbf 1^{\mathsf T}Az=(A\mathbf 1)^{\mathsf T}z
  =k\mathbf 1^{\mathsf T}z=0.
\]
On \(W\), equation (2) becomes \(A^2=s^2I\). Every \(z\in W\) decomposes as
\[
  z=z_++z_-,
  \qquad z_\pm=\frac12\left(z\pm\frac{Az}{s}\right),
\]
and direct substitution gives \(Az_+=sz_+\), \(Az_-=-sz_-\). Therefore \(W\)
is the direct sum of the \(+s\) and \(-s\) eigenspaces. Let their dimensions be
\(p,q\).

In a basis consisting of \(\mathbf 1\) followed by bases of those two
eigenspaces, \(A\) has diagonal entries \(k\), then \(p\) copies of \(s\), then
\(q\) copies of \(-s\). Trace is basis-independent, while the zero diagonal of
the adjacency matrix gives \(\operatorname{tr}(A)=0\). For completeness, the
basis-independence used here follows from
\(\operatorname{tr}(BC)=\operatorname{tr}(CB)\), since both sides expand to
\(\sum_{i,j}B_{ij}C_{ji}\); hence
\(\operatorname{tr}(S^{-1}AS)=\operatorname{tr}(ASS^{-1})\). Therefore
\[
  0=k+(p-q)s. \tag{4}
\]
If \(p=q\), then \(k=0\), impossible. Otherwise (4) makes \(s\) rational. Since
\(s^2=k-1\) is an integer, \(s\) is a positive integer: in a lowest-terms
expression \(s=a/b\), the divisibility \(b^2\mid a^2\) forces \(b=1\).

Equation (4) now says that \(s\mid k\). But \(k=s^2+1\), so \(s\mid1\).
Therefore \(s=1\), \(k=2\), and (3) gives \(n=3\). The only simple 2-regular
graph on three vertices is \(K_3\), in which every vertex is adjacent to every
other vertex. This contradicts the assumption that no universal vertex exists.

The contradiction proves the required conclusion.

## Unresolved gaps

- `G003`: the candidate requires the mandated adversarial review passes before
  any promotion to `proved`.
- `G004`: reference comparison remains deliberately deferred and was not used.

## Computational dependencies

None.
