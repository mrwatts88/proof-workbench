# A003 — Order-ten structural classification

- Date opened: 2026-07-23
- Problem: `P-002`
- Status: active

## Intended mechanism

Enumerate the degree sequences allowed at order \(10\) by the exact codegree
budget, eliminate five by local capacity, and classify the two surviving
\(C_4\)-free structures far enough to construct an \(8\)-cycle.

## Entry assumptions

- `D001`–`D004`.
- `L002` and the \(C_4\)-free codegree inequality from `A001/L003`.
- For contradiction, an edge-minimal counterexample \(G\) of order \(10\).

## Targeted obligations

- `G003`: force an \(8\)-cycle from the local restrictions.
- `G005`: convert the order-\(10\) census pattern into a proof.

## Plan and decisive tests

1. Derive all feasible degree sequences without relying on enumeration code.
2. Use high-to-low incidence capacity to eliminate all but the cubic and
   \((4,4,3^8)\) sequences.
3. Classify each remaining graph around one neighborhood and exhibit an
   \(8\)-cycle in every case.

## Deductions

### `L006` — Every counterexample has at least eleven vertices

**Proof.** By `L005`, only order \(10\) remains. Choose an edge-minimal
counterexample \(G\) of that order. Since \(G\) is \(C_4\)-free,
\[
  \sum_v\binom{d(v)}2\le\binom{10}{2}=45. \tag{1}
\]
A degree at least \(7\) would make the left side at least
\(\binom72+9\binom32=48\). Thus all degrees lie in
\(\{3,4,5,6\}\). If \(t_i\) counts degree \(i\), (1), relative to ten cubic
vertices, and the handshake parity condition give
\[
  3t_4+7t_5+12t_6\le15,\qquad t_4+t_6\equiv0\pmod2. \tag{2}
\]
Solving (2) yields exactly seven degree sequences:
\[
\begin{split}
 &(3^{10}),\ (4^2,3^8),\ (4^4,3^6),\ (5,3^9),\\
 &(5,4^2,3^7),\ (5^2,3^8),\ (6,4,3^8). \tag{3}
\end{split}
\]

#### Five sequences excluded by capacity

The sequence \((5,3^9)\) is impossible. If \(v\) is its degree-\(5\)
vertex and \(e\) is the number of edges induced by \(N(v)\), then
\(e\le2\), because that induced graph has maximum degree at most \(1\).
The five cubic neighbors require \(10-2e\ge6\) edges to the four remaining
vertices. Each remaining vertex can meet at most one member of \(N(v)\), so
at most four such edges exist.

For each of the other four sequences in (3) having a degree at least \(5\) or
four degree-\(4\) vertices, let \(H\) be the set of degree-above-\(3\)
vertices and let \(L=V(G)\setminus H\). By `L002`, \(H\) is independent.
Put \(r_x=|N(x)\cap H|\) for \(x\in L\), and let
\(R=\sum_{h\in H}d(h)=\sum_{x\in L}r_x\). Since a pair in \(H\) has at
most one common neighbor,
\[
  \sum_{x\in L}\binom{r_x}{2}\le\binom{|H|}{2}, \tag{4}
\]
whereas \(\binom r2\ge r-1\) gives the lower bound \(R-|L|\).
For the four sequences
\[
 (6,4,3^8),\ (5^2,3^8),\ (5,4^2,3^7),\ (4^4,3^6),
\]
the respective lower and upper bounds in (4) are
\[
 2>1,\quad2>1,\quad6>3,\quad10>6.
\]
They are impossible. Only \((3^{10})\) and \((4^2,3^8)\) remain.

#### The cubic sequence

Assume first that \(G\) is cubic. Fix \(v\) with
\(N(v)=\{a,b,c\}\), and set
\(R=V(G)\setminus(\{v\}\cup N(v))\). The graph induced by \(N(v)\) is
a matching, hence has zero or one edge.

If it has no edge, the six edges from \(N(v)\) to the six vertices of \(R\)
have distinct endpoints; otherwise a \(4\)-cycle passes through \(v\). Thus
each vertex of \(R\) has one neighbor in \(N(v)\), and \(G[R]\) is
2-regular. If \(G[R]\) is a \(6\)-cycle, take two vertices at cyclic
distance \(2\). Their neighbors in \(N(v)\) must be distinct, since otherwise
the length-\(2\) path between them closes a \(4\)-cycle. The complementary
length-\(4\) path on the \(6\)-cycle, together with those two distinct
neighbors and \(v\), is an \(8\)-cycle.

The other possibility is that \(G[R]\) is two disjoint triangles. No member of
\(\{a,b,c\}\) can meet two vertices in the same triangle, because the third
triangle vertex would close a \(4\)-cycle. Each of \(a,b,c\) therefore has
one neighbor in each triangle. Write the triangles as
\(\{x_a,x_b,x_c\}\) and \(\{y_a,y_b,y_c\}\), with subscripts recording
the neighbor in \(N(v)\). Then
\[
  v\,a\,x_a\,x_b\,b\,y_b\,y_c\,c\,v
\]
is an \(8\)-cycle.

Now suppose \(G[N(v)]\) has the single edge \(ab\). Vertices \(a,b\) each
have one neighbor in \(R\), while \(c\) has two; these four endpoints are
distinct. Consequently \(G[R]\) is a connected graph with degree sequence
\((3,3,2,2,2,2)\). It is connected because a component containing a
degree-\(3\) vertex has at least four vertices, while any other component of
minimum degree \(2\) has at least three.

Suppressing the four degree-\(2\) vertices gives a connected multigraph on the
two degree-\(3\) branch vertices. It is either three parallel branch-to-branch
paths (a theta graph), or a loop at each branch joined by one
branch-to-branch path (a dumbbell). In the theta case the three path lengths
sum to \(7\), at most one has length \(1\), and no pair sums to \(4\);
therefore the lengths are \(1,2,4\). In the dumbbell case the two cycles and
joining path have seven edges, forcing two triangles joined by one edge.

Color the four degree-\(2\) vertices by their neighbor among \(a,b,c\); the
multiset of colors is \(a,b,c,c\). In the \(1,2,4\) theta graph, every pair
of degree-\(2\) vertices is joined by some simple path of length \(4\).
For an explicit check, write the paths as \(pq\), \(p\,s\,q\), and
\(p\,x\,y\,z\,q\); the six pairs among \(s,x,y,z\) have length-\(4\)
routes
\[
\begin{array}{c|c}
\{s,x\}:s\,q\,z\,y\,x & \{s,y\}:s\,p\,q\,z\,y\\
\{s,z\}:s\,p\,x\,y\,z & \{x,y\}:x\,p\,q\,z\,y\\
\{x,z\}:x\,p\,s\,q\,z & \{y,z\}:y\,x\,p\,q\,z.
\end{array}
\]
Choose two differently colored vertices and such a path. In the dumbbell
case, some differently colored pair lies in opposite triangles, and it too
has a length-\(4\) path: traverse the other degree-\(2\) vertex of the first
triangle, the joining edge, and enter the second triangle. In either case,
adjoining the two color vertices and \(v\) to this path gives an \(8\)-cycle.

#### The sequence \((4^2,3^8)\)

Let the degree-\(4\) vertices be \(p,q\). They are nonadjacent by `L002`.
Every other vertex is cubic. Put
\(s=|N(p)\cap N(q)|\le1\). Counting the eight incidences from
\(\{p,q\}\) to the eight cubic vertices shows that the number adjacent to
neither high vertex also equals \(s\).

Suppose \(s=1\), and let \(w\) be the common neighbor. In the four-vertex
set \(N(p)\), let \(e\) be the number of induced edges. Its vertices have
eight residual incidences after their edges to \(p\), so \(8-2e\) edges
leave \(N(p)\). Each of the five vertices outside \(N(p)\cup\{p\}\) can
receive at most one such edge, or a \(4\)-cycle through \(p\) results.
Thus \(e\ge2\). Since \(G[N(p)]\) has maximum degree \(1\), \(e=2\) and is a
perfect matching. The vertex \(w\), whose only neighbor besides \(p,q\) is
some cubic vertex \(z\), must therefore have \(z\in N(p)\). Repeating the
same argument at \(q\) forces \(z\in N(q)\), giving a second common neighbor
of \(p,q\), contrary to \(s=1\).

Hence \(s=0\). Every cubic vertex is adjacent to exactly one of \(p,q\), so
the subgraph induced by the eight cubic vertices is 2-regular. Since it has no
\(4\)-cycle, it is either an \(8\)-cycle or the disjoint union of a triangle
and a \(5\)-cycle. The latter is impossible: two vertices of the triangle
share the same high neighbor, and together with the third triangle vertex
they form a \(4\)-cycle. Thus the induced subgraph is itself an \(8\)-cycle.

Both remaining degree sequences force an \(8\)-cycle. This contradicts the
counterexample assumption and proves that every counterexample has at least
eleven vertices. \(\square\)

## Failure analysis

The proof closes order \(10\), but its detailed classification is inherently
small-order. At order \(11\), the same initial budget already leaves twelve
degree sequences, so it is not yet a scalable route to the full conjecture.

## Salvageable results

- `L006` raises the rigorous counterexample lower bound to \(11\).
- The high-to-low incidence inequality (4) rapidly removes degree sequences
  with many or very large high-degree vertices.
- The cubic neighborhood split identifies theta/dumbbell and 2-regular
  remainders as reusable local structures.

## Exit state

- Status: completed
- Promoted records: `L006` in `CLAIMS.md`
- Next action: stop treating one order at a time as the main route; audit known
  structural results and seek a scalable theta/ear mechanism.
