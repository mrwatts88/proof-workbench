# A028 — the non-Hamiltonian stratum: no class-level Hamiltonian forcing, bipartite exclusion, and the positive-savings theorem

- Date opened: 2026-07-26
- Problem: `P-002`
- Status: active
- Portfolio role: primary (Tier 1, `G015` case (5b), proof side; session
  `S030`). Executes the recorded next action — `A027` T5, the bridge
  generalisation of the chord-minimal descent — and, en route, settles the
  recorded "best live alternative" negatively.

## Intended mechanism

`A027` T5 named one obstruction and one first purchase.

- **Obstruction.** For a longest \(a\)–\(b\) path \(P\) that is *not*
  Hamiltonian, the descent's links are **bridges** \((i,j,w)\) rather than
  chords, and "a bridge with \(w=j-i\) covers two positions and yields savings
  0, so covering no longer forces savings."
- **First purchase (provisional).** A zero-savings two-attachment component has
  a singleton through-set, hence (via `L049`) a bipartite gadget — "the
  transfer needs the power-freeness hypothesis matched, which is not done
  here."

This attempt matches the power-freeness hypothesis, discharges the purchase,
and then removes the obstruction outright: **no component is zero-savings**,
for two independent reasons depending on its number of attachments.

It also asks the question the recorded next action deferred — *should* the
non-Hamiltonian stratum be handled, or can the 27/27 Hamiltonicity measurement
(`C049`) be promoted to a lemma? The answer is negative and cheap, and it is
recorded first because it changes what the rest of the attempt is for.

## Entry assumptions

Statement 0.1 verbatim. Consumed at recorded strength: `L035` T2 (parity
structure) and T3 (bipartite assembly criterion), `L049`/`L050`
(interference-completeness ⟺ vertex-tautness), `L048`(iii) (spectrum identity),
`L042` (residual-object structure), `L046` (2-connected below 36), `L052`/`A027`
T1–T2 (the chord-minimal descent and the monotone reroute), `C034` (bipartite
class empty through order 24), `C046`/`C047` (census and dissection),
`C048`/`C049` (the ladder and the order-21 rung). External: `X001`–`X003` of
`references/large-girth-non-hamiltonian-cubic-2026-07-26.md`.

## Targeted obligations

- `G015`: exclude case (5b) — the non-Hamiltonian half, which no computation
  has touched at any order.
- `G013`(a): structure theory for the tight-1-atom question.

## Plan and decisive tests

1. **Cheapest falsification of the session's premise.** If the exactly-two
   profile plus the class hypotheses *did* force a Hamiltonian through-path,
   the whole stratum would be empty and this attempt pointless. Test that
   first, from the literature, before doing any work on bridges. (It does not;
   T1.)
2. **Cheapest falsification of the bridge route.** If a zero-savings component
   can exist under the residual object's full hypotheses, the descent has no
   engine. (It cannot; T3–T5.)
3. **Pivot trigger.** If the savings theorem holds but the descent still cannot
   be made minimal (T8), the route's value is a structure theorem rather than a
   decision procedure, and the session must say so and re-aim.

## Notation

A **profile pair** is a triple \((H,a,b)\): \(H\) finite and simple, \(a\ne b\),
\(d_H(a)=d_H(b)=2\), and \(d_H(v)\ge3\) for every other vertex. \(S=S(H,a,b)\)
is the set of lengths of simple \(a\)–\(b\) paths (**through-set**),
\(\mathrm{Spec}(H)\) the set of cycle lengths. \(\mathbb P=\{4,8,16,32,\dots\}\).
*Power-free* means \(\mathrm{Spec}(H)\cap\mathbb P=\emptyset\).

Fix a **longest** \(a\)–\(b\) path \(P=v_0v_1\cdots v_M\) (\(v_0=a\),
\(v_M=b\), \(M=\max S\)) and write \(W=V(H)\setminus V(P)\). For a component
\(K\) of \(H[W]\), its **attachments** are the positions \(p\) with
\(N(v_p)\cap K\ne\emptyset\); a **bridge** \((i,j,w)\) is a \(v_i\)–\(v_j\) path
of length \(w\) whose interior lies in \(K\); its **savings** is
\(\sigma=(j-i)-w\).

The case-(5b) residual object is a profile pair which is 2-connected (below
order 36, `L046`), vertex-taut (`L042`), \(C_4\)-free, and **power-free**
(\(H=B-u\subseteq B\) with \(B\) a tight 1-atom, and power-freeness is
hereditary). Every hypothesis used below is one of these.

---

## Deductions

### T1 (there is no class-level Hamiltonian forcing) — proved

> For every \(N\) there is a profile pair \((H,a,b)\) with \(|V(H)|\ge N\) such
> that \(H\) is **2-connected**, has **girth \(\ge17\)** — in particular
> contains no \(C_4\), \(C_8\) or \(C_{16}\) — and has **no Hamiltonian
> \(a\)–\(b\) path**, i.e. \(\max S<|V(H)|-1\).

*Proof.* By `X002` (Haythorpe) — independently by `X003` (Kochol's snarks of
arbitrarily large girth, which are non-Hamiltonian because a cubic graph with a
Hamiltonian cycle is 3-edge-colourable) — choose a cubic, 3-edge-connected,
non-Hamiltonian simple graph \(F\) of girth \(\ge17\) with \(|V(F)|\ge N\). For
a cubic graph vertex connectivity equals edge connectivity, so \(F\) is
3-connected. Pick \(e=ab\in E(F)\) and set \(H=F-e\).

\(d_H(a)=d_H(b)=2\) and every other vertex keeps degree 3, so \((H,a,b)\) is a
profile pair. \(H\subseteq F\) has girth \(\ge17\), so \(4,8,16\notin
\mathrm{Spec}(H)\). Deleting one edge lowers connectivity by at most one, so
\(H\) is 2-connected. Finally, a Hamiltonian \(a\)–\(b\) path of \(H\) together
with \(e\) would be a Hamiltonian cycle of \(F\); \(F\) has none. ∎

**What this settles.** The hypotheses actually available at the class level —
exactly-two degree profile, \(\{C_4,C_8,C_{16}\}\)-freeness, 2-connectivity,
and (by `L050`, since \(H\) here is 2-connected with \(\delta\ge2\))
vertex-tautness — **do not force a Hamiltonian through-path**. So `S029`'s
recorded best live alternative, "turn 27/27 into a lemma", is refuted *at that
strength*: any Hamiltonian-forcing lemma must additionally consume
power-freeness, the poison condition \(S\cap(\mathbb P-2)=\emptyset\),
minimum-order minimality, or an explicit order bound. That is exactly the
`C037` calibration discipline, and \(F-e\) is recorded as

> **Calibration object #3** — a cubic non-Hamiltonian graph of girth \(\ge17\)
> minus an edge. Any proposed proof that the profile forces a Hamiltonian
> through-path must fail on it.

**Scope, stated honestly.** A cubic graph of girth 17 has order in the
thousands, so T1 is an **asymptotic** statement. It does not exhibit a
non-Hamiltonian profile member in the window \([18,35]\), and it is fully
consistent with `C049`'s 27/27 at orders 19–21. What it removes is the *route*,
not the *pattern*: the pattern is real and small-order, and the route through
it is closed.

**Second consequence — the ladder's top cannot stay empty.** `R003` F4 recorded
that above order 26 `E028` run B proves class-emptiness rather than poison
forcing. T1 shows the **ambient** class (profile + \(\{C_4,C_8,C_{16}\}\)-free)
is nonempty at arbitrarily large order, so the class-emptiness mechanism is a
small-order phenomenon that must fail at some order, after which only poison
forcing — the mechanism that stopped firing at order 26 — can carry a rung.
(Whether the *Hamiltonian* sub-class is nonempty at large order is **not**
claimed here: it would follow from the existence of Hamiltonian cubic graphs of
girth \(\ge17\), which is expected from the standard random-cubic model but is
not imported. Flagged as an expectation, not a result.)

### T2 (the bipartite exclusion dichotomy) — proved

> Let \(X\) be a finite **power-free** graph and let \(Y\subseteq X\) be a
> connected subgraph with at most two vertices of degree \(\le2\) *in \(Y\)*,
> those degrees being \(\ge1\) and summing to \(\ge3\) if there are two. If
> \(Y\) is **bipartite**, then statement 0.1 is **false**, and `L035` T3
> constructs an explicit counterexample from \(Y\).

*Proof.* \(Y\subseteq X\) inherits power-freeness, so \(Y\) satisfies every
hypothesis of `L035` T3 verbatim. ∎

Three usable forms:

- **(a) Dichotomy.** Either 0.1 is false with a witness in hand, or no
  power-free graph contains such a \(Y\). A construction that produces such a
  \(Y\) is therefore a **disproof route**, not a dead end.
- **(b) In range, an outright exclusion.** If \(|V(Y)|\le24\) then `C034`
  (bipartite class empty through order 24, 25 with a pendant) excludes \(Y\)
  with no appeal to 0.1 at all.
- **(c) Inside `G015`.** The `G015` setting already assumes a counterexample
  exists, so form (a) alone is not a contradiction there; form (b) is, and so
  is the observation that a counterexample of order \(<n_0\) yields a *cubic*
  one by `L040`, which is `G015`'s conclusion. Both are recorded; (b) is the
  one used below in the window.

This is the promised matching of the power-freeness hypothesis for `A027` T5's
first purchase.

### T3 (two attachments: mixed parity, hence positive savings) — proved

> Let \((H,a,b)\) be a **power-free 2-connected** profile pair, \(P\) a longest
> \(a\)–\(b\) path, and \(K\) a component of \(H-V(P)\) with **exactly two**
> attachments \(i<j\). Put \(D=j-i\), \(G_K=H[K\cup\{v_i,v_j\}]\) with terminals
> \(v_i,v_j\), and let \(S_K\) be its through-set. Then
>
> (i) \(S_K\ne\emptyset\) and \(2\le w\le D\) for every \(w\in S_K\);
> (ii) \(G_K\) is vertex-taut;
> (iii) either \(S_K\) contains **both parities**, or statement 0.1 is false
> (T2, with the witness built from \(G_K\) or from \(H[K]\));
> (iv) in the first case \(K\) admits a bridge of savings \(\ge1\), and in fact
> savings of **both parities** are realised.

*Proof.* **(i)** \(K\) is connected and has neighbours at both \(v_i\) and
\(v_j\), so a \(v_i\)–\(v_j\) path through \(K\) exists; it has at least one
interior vertex, so \(w\ge2\). If some such path \(Q\) had \(w>D\) then
\(P[0,i]+Q+P[j,M]\) would be an \(a\)–\(b\) path (simple, because \(Q\)'s
interior lies in \(K\), disjoint from \(V(P)\)) of length \(i+w+(M-j)>M\),
contradicting maximality of \(P\).

**(ii)** Let \(u\in K\). Since \(H\) is 2-connected, the fan version of Menger's
theorem gives two paths from \(u\) to \(\{v_i,v_j\}\) meeting only at \(u\) and
ending at \(v_i\) and \(v_j\) respectively. \(K\)'s only neighbours outside
\(K\) are \(v_i\) and \(v_j\), so each of these paths stays inside \(K\) until
its final vertex. Their union is a \(v_i\)–\(v_j\) path of \(G_K\) through
\(u\).

**(iii)** By (ii) and `L035` T2, \(S_K\) is parity-constant **iff** \(G_K\) is
bipartite. Suppose it is bipartite. \(G_K\) is connected and power-free
(\(G_K\subseteq H\)). Every vertex of \(K\) has *all* its \(H\)-neighbours
inside \(G_K\), so its degree in \(G_K\) is \(\ge3\); hence the only vertices of
degree \(\le2\) in \(G_K\) are \(v_i,v_j\), of degrees \(d_i=|N(v_i)\cap K|\ge1\)
and \(d_j=|N(v_j)\cap K|\ge1\).

- If \(d_i+d_j\ge3\), T2 applies to \(Y=G_K\).
- If \(d_i=d_j=1\), let \(u,u'\) be the unique \(K\)-neighbours of \(v_i,v_j\).
  Pass to \(Y=H[K]\): connected, bipartite, power-free. Every
  \(x\in K\setminus\{u,u'\}\) is adjacent to neither \(v_i\) nor \(v_j\), so
  \(d_Y(x)=d_H(x)\ge3\). If \(u\ne u'\) then \(d_Y(u)=d_H(u)-1\ge2\) and
  likewise for \(u'\), so \(Y\) has exactly two vertices of degree \(\le2\),
  degrees \(\ge2\) each, sum \(\ge4\): T2 applies. If \(u=u'\) then
  \(d_Y(u)=d_H(u)-2\ge1\) and \(u\) is the only vertex of degree \(\le2\)
  (and \(|K|\ge2\), since \(d_H(u)\ge3\) forces a neighbour inside \(K\)): T2
  applies in its one-sub-cubic-vertex form.

**(iv)** Take \(w,w'\in S_K\) of different parities. By (i) both are \(\le D\),
so \(D-w\) and \(D-w'\) are savings \(\ge0\) of different parities; the odd one
is \(\ge1\). ∎

### T4 (three or more attachments: the Y-savings identity) — proved

> Let \(P\) be a longest \(a\)–\(b\) path and \(K\) a component of \(H-V(P)\)
> with attachments including \(i<j<k\). Then there are a vertex \(u\in K\) and
> three internally disjoint paths from \(u\) to \(v_i,v_j,v_k\), of lengths
> \(\alpha,\beta,\gamma\ge1\), with interiors in \(K\); and, writing
> \(\sigma(p,q)\) for the savings of the corresponding bridge,
> \[
>   \sigma(i,k)=\sigma(i,j)+\sigma(j,k)+2\beta\ \ge\ 2\beta\ \ge\ 2 .
> \]
> In particular \(K\) admits a bridge of savings \(\ge2\).

*Proof.* **The spider.** Choose \(x,y,z\in K\) adjacent to \(v_i,v_j,v_k\)
respectively (not necessarily distinct) and let \(T\subseteq K\) be a minimal
connected subgraph containing \(x,y,z\); \(T\) is a tree whose leaves lie in
\(\{x,y,z\}\), so it has at most three leaves. If \(T\) has three leaves, let
\(u\) be its unique degree-3 vertex; the three \(T\)-paths from \(u\) to
\(x,y,z\) are internally disjoint, and appending the edges \(xv_i\), \(yv_j\),
\(zv_k\) gives the three legs. If \(T\) has at most two leaves it is a path;
take \(u\) to be whichever of \(x,y,z\) is not an endpoint of that path (if all
three coincide, \(u=x=y=z\)); the two path-directions from \(u\), extended by
the appropriate edges, together with the edge from \(u\) to its own attachment,
give three internally disjoint legs. In every case each leg has length \(\ge1\)
and its interior lies in \(K\).

**The identity.** Write \(\sigma(i,j)=(j-i)-(\alpha+\beta)\),
\(\sigma(j,k)=(k-j)-(\beta+\gamma)\), \(\sigma(i,k)=(k-i)-(\alpha+\gamma)\).
Then
\[
 \sigma(i,j)+\sigma(j,k)=(k-i)-(\alpha+2\beta+\gamma)=\sigma(i,k)-2\beta .
\]
**Nonnegativity.** For any two attachments \(p<q\) the walk
\(P[0,p]+(\text{leg to }v_p)+(\text{leg to }v_q)+P[q,M]\) is a simple
\(a\)–\(b\) path (the two legs meet only at \(u\), and their interiors avoid
\(V(P)\)), of length \(M-\sigma(p,q)\); maximality of \(P\) gives
\(\sigma(p,q)\ge0\). Hence \(\sigma(i,k)\ge2\beta\ge2\). ∎

T4 uses **only** maximality of \(P\): no power-freeness, no \(C_4\)-freeness,
no 2-connectivity. It is therefore also true on Calibration object #3, as it
must be.

### T5 (the positive-savings theorem) — proved

> Let \((H,a,b)\) be a power-free 2-connected profile pair and \(P\) a longest
> \(a\)–\(b\) path. Then **every** component \(K\) of \(H-V(P)\) admits a bridge
> of savings \(\ge1\) — savings \(\ge2\) if \(K\) has three or more attachments
> — unless statement 0.1 is false, with an explicit counterexample constructed
> from \(K\) by T2.
>
> In the window, the escape clause is closed outright whenever
> \(|K|\le22\), by `C034` (T2 form (b)).

*Proof.* \(K\) has at least two attachments, since \(H\) is 2-connected. Two
attachments: T3. Three or more: T4. ∎

**This removes the obstruction `A027` T5 named.** "A bridge with \(w=j-i\)
covers two positions and yields savings 0" — such a component does not exist.
Coverage forces savings again, as in the Hamiltonian case, and `A027` T2's
monotone-reroute machinery (interval-disjoint families, the left-to-right
savings DP, prefix certification) transports verbatim with bridges in place of
chords: its proof used only that the replaced arcs have pairwise disjoint
interiors and are met in order.

### T6 (the bridge span law and the gap law) — proved

> For every bridge \((i,j,w)\) of every component: \(w\le j-i\) (T3(i)/T4), and
> \((j-i)+w\notin\mathbb P\), because \(P[i,j]\) together with the bridge is a
> cycle of that length. Consequently:
>
> (i) two *consecutive* attachments of a component satisfy \(j-i\ge3\) (if
> \(j-i=2\) then \(w=2\) and the cycle has length 4);
> (ii) if \(j-i=4\) then \(w\le3\), so \(\sigma\ge1\) (\(w=4\) would give a
> \(C_8\)); if \(j-i=8\) then \(w\ne8\), so \(\sigma\ge1\) whenever \(C_{16}\)
> is also excluded.

This is `A026` T5's span law in its bridge form (chords are the case \(w=1\)),
and (ii) is a second, hypothesis-cheap source of savings independent of T3.

### T7 (coverage) — proved

> Every position \(p\in\{0,\dots,M\}\) is an endpoint of a chord or an
> attachment of a component of \(H-V(P)\); positions \(0\) and \(M\) are covered
> exactly once.

*Proof.* Verbatim `A027` T1's coverage step: an internal \(v_p\) has degree
\(\ge3\) and exactly two path edges, hence a third edge, which is either a chord
or an edge into \(W\); \(a=v_0\) has degree 2 with one path edge, hence exactly
one further edge; likewise \(b\). ∎

### T8 (what the descent still needs) — analysis, open

With T5–T7 the non-Hamiltonian stratum has the same *shape* as the Hamiltonian
one: a covering system of links, each contributing savings, with a monotone DP
certifying through-lengths. Two gaps remain before it is a decision procedure of
`A027` T1's kind, and they are recorded rather than papered over:

1. **Minimality is not yet available.** `A027` T1's descent deletes redundant
   chords and keeps every hypothesis. A component cannot be thinned edge by
   edge — deleting one of its bridges is not a subgraph operation on \(K\), and
   dropping \(K\) entirely destroys the degree profile at *all* of its
   attachments at once. What is needed is a minimal-cover notion whose atoms are
   components, together with a bound on their number. T5 gives the savings; it
   does not give the bound.
2. **The savings are per component, not per position.** T5 supplies one
   positive-savings bridge per component. The DP needs an *interval-disjoint
   family* of them, and different components' good bridges may nest or cross.

Neither gap is closed here.

### T9 (the strategic finding: the ladder has a ceiling, and the order-unbounded route is (INT)) — analysis

Three facts now sit together and point the same way.

- **The (F) window is not the problem's window.** `L046` gives "\(H\)
  2-connected **or** \(n_0\ge36\)". The (F) program therefore closes case (5b)
  only for \(n_0\le35\); case (5b) at order \(\ge36\) is untouched by any amount
  of laddering. A complete ladder does **not** prove `G015`.
- **The ladder's top mechanism must fail.** Above order 26 the poison prune
  stops firing and the rungs prove class-emptiness (`R003` F4); by T1 the
  ambient class is nonempty at arbitrarily large order, so class-emptiness
  cannot continue.
- **The remaining stratum is not a formality** (T1), and it is not obviously
  small: `C047`(c) already located the escapes on degree-2 corridors, which is
  the off-path analogue of exactly this stratum.

So the honest order-unbounded target is not a longer ladder but a **through-set
interpolation theorem**. Recorded as the sharpened missing tool:

> **(INT) — the no-gap conjecture.** For a vertex-taut \(\{C_4,C_8\}\)-free
> profile pair \((H,a,b)\), \(S(H,a,b)\supseteq[\,8,\max S\,]\).

Why 8, and why the profile: this is the strongest form consistent with every
object on record, and its refutation set is already on disk. **(INT) was then
kill-tested against both** (`E029`/`C050`, no new generation: \(S\) recomputed
by exact path enumeration from the stored graph6 strings; six anchors under two
interpreters).

| object | \(S\) | consistent with (INT)? |
|---|---|---|
| **24 recorded profile objects, orders 19–21** (`E029`, verified) | every hole in \(\{4,5,6\}\); none at 7 or above | **yes, 24/24** |
| order-21 profile member with \(6\notin S\) (`C049`, reproduced) | \([4,20]\setminus\{6\}\) | yes (hole \(<8\)) |
| order-20 part-14 member (`E029`, **new**) | \([3,19]\setminus\{4,5\}\) | yes — a second non-interval profile object, one order below `S027`'s |
| remaining 3 of the eight orders 19–20 (`A025` T3, not stored as graph6) | \(\supseteq[6,n-1]\) | yes |
| order-22, 8 objects (`C048`) | \([5,21]\setminus\{6\}\) | yes |
| order-22, 5 adjacent-terminal objects (`C048`) | \(\{1,5\}\cup[8,21]\) | yes, and **sharp** (\(7\notin S\)) |
| Petersen\(-e\) | \(\{4,5,7,8\}\) | yes (hole at 6) |
| order-14 calibration object | hole exactly at 6 | yes |
| `C047` corpus, `ndeg2 = 4` frontier rows | holes confined to \([2,7]\) | yes — and this is what **pins the constant** |
| `C047` corpus, 1,920 rows with `ndeg2` \(\ge5\) | holes at 8, 9, 10, 11, 14 | **no** — the profile hypothesis is load-bearing |

Two things the measurement added that were not anticipated.

- **The constant 8 is pinned from both sides.** Every hole value \(\le7\) is
  realised already at the corpus's minimum degree-2 count of **4**; the first
  hole at **8** needs 5. So (INT) with any constant \(\le7\) is *false* on the
  near-miss frontier, and 8 is the smallest constant the data permits.
- **The operative case has a five-vertex margin.** No corpus row opens a hole
  at **14** below `ndeg2 = 7`. Since 14 is the poison value that matters, the
  weakened form
  > **(INT-14)** a vertex-taut \(\{C_4,C_8\}\)-free profile pair with
  > \(\max S\ge14\) has \(14\in S\)
  is better supported than full (INT) and, by `L048`(iii), is all (F-S) needs.

The corpus rows are the point: (INT) is **false** without the exactly-two
profile, and the 9,061-row corpus of `C046`/`C047` is its standing refutation
set — the discipline `A026` established. It is also exactly what `C046`(b) and
`C047`(b) predicted any working lemma must consume.

**Why (INT) is the right target.** With (L-A) — \(\max S\ge14\), `A026` T7's
short-range half — (INT) gives \(14\in S\) directly, and \(14\in\mathbb P-2\) is
poison, so \(S\cap(\mathbb P-2)\ne\emptyset\): that is (F-S), **at every
order**, with no window, no ladder, and no \(C_{16}\) hypothesis. The pair
(INT) ∧ (L-A) is thus an order-unbounded architecture for case (5b) where the
ladder is a finite-window instrument. `A026` T6's validated chord-exchange
calculus ("the entire top of \(S\) down to 10, including 14, on all eight
profile objects") is evidence *for* (INT) and is its natural engine on the
Hamiltonian stratum; T5–T7 above are what the same engine needs on the
non-Hamiltonian one.

Not proved here. Recorded as the successor to `A026` T7's (L-A)/(L-B) split,
which it subsumes: (L-B) — "\(\max S\ge14\Rightarrow14\in S\) or \(6\in S\)" —
is the special case of (INT) that matters.

---

## Failure analysis

- **The recorded "best live alternative" is dead at class strength** (T1). This
  is a negative result about a route, obtained for the cost of two literature
  lookups; it was worth taking first, because the rest of this attempt exists
  precisely because that route is closed.
- **T5 does not finish the descent** (T8). The two gaps are stated. This attempt
  does **not** close the non-Hamiltonian stratum at any order, and no ledger row
  claims that it does.
- **T2's exclusion is conditional outside `C034`'s range** (form (a) vs (b)).
  Inside `G015`, where a counterexample is already assumed to exist, "0.1 is
  false" is not a contradiction; only `C034`'s range form, or an order
  comparison against \(n_0\) via `L040`, converts the dichotomy into an
  exclusion. Recorded explicitly so that no later session reads T3(iii) as an
  unconditional exclusion.
- **A route not taken.** Deleting a component and replacing it by a path of
  length \(w\in S_K\) yields \(H'\) with \(\mathrm{Spec}(H')\subseteq
  \mathrm{Spec}(H)\) and \(S(H')\subseteq S(H)\), so every hypothesis except the
  degree profile survives — but the replacement path's interior vertices have
  degree 2, so \(H'\) leaves the profile class. This is `C047`(c)'s subdivision
  phenomenon seen from the other side, and it is why a smoothing induction on
  the number of off-path vertices does not close.

## Salvageable results

1. **T1** and Calibration object #3 — the class-level Hamiltonian forcing is
   false; any future Hamiltonicity argument must consume power-freeness, the
   poison condition, minimality, or an order bound.
2. **T2** — the bipartite exclusion dichotomy, a general and order-unbounded
   tool: no power-free graph has a bipartite piece with \(\le2\) sub-cubic
   vertices, on pain of disproving 0.1.
3. **T3–T5** — the positive-savings theorem; `A027` T5's obstruction removed and
   its provisional first purchase discharged with the hypothesis matched.
4. **T6** — the bridge span law and the \(\ge3\) gap law.
5. **T9** — (INT), the no-gap conjecture, with its sharpness table and its
   on-disk refutation set; and the reason the ladder is not the route.

## Adversarial review

None delegated. This attempt promotes lemma-level rows only (`L053`–`L055`); no
statement-level candidate is offered, so the mandatory candidate-to-review
transition of `AGENTS.md` is not triggered. The self-checks actually run:

- T1's construction was checked hypothesis by hypothesis against the recorded
  class definition, and its two independent literature routes are recorded
  separately in `references/large-girth-non-hamiltonian-cubic-2026-07-26.md`.
- T3(iii)'s degree bookkeeping was carried through **all three** boundary cases
  (\(d_i+d_j\ge3\); \(d_i=d_j=1\) with \(u\ne u'\); \(u=u'\)), because `L035`
  T3's side condition "degrees summing to \(\ge3\)" fails in the second and
  third.
- T4's identity was verified on the degenerate instance
  \(\alpha=\beta=\gamma=1\) (a single-vertex component adjacent to
  \(v_i,v_j,v_k\)): the identity gives \(k-i\ge4\), while \(C_4\)-freeness alone
  gives only \(k-i\ne2\) and the span law \(k-i\ne6\) — consistent, with the
  identity strictly stronger.
- Every lemma was tested against the calibration objects: T4 must and does hold
  on Calibration object #3 (it consumes only maximality); T3 and T5 must and do
  fail there (they consume power-freeness, which \(F-e\) lacks); (INT) must and
  does fail on the corpus rows with \(\ge5\) degree-2 vertices (which lack the
  profile), and does not fail on any recorded profile object.
- (INT) was given a real kill test rather than being left as a formulation
  (`E029`/`C050`): 24 profile objects, \(S\) recomputed from graph6 rather than
  read from the `C043`/`C049` summaries, six anchors reproducing independently
  recorded quantities, two interpreters. It survived, and the measurement
  sharpened it twice (the pinned constant; the five-vertex margin at 14).

## Exit state

- Status: active
- Promoted records: ledger rows `L053` (T1 + calibration object #3), `L054`
  (T2), `L055` (T3–T7, the positive-savings package) offered; `G015` updated;
  (INT) recorded in `OBLIGATIONS.md` as the named successor target.
- Next action: attack **(INT)** on the Hamiltonian stratum with `A026` T6's
  chord-exchange calculus — the first falsifiable move is whether a
  chord-minimal cover of a Hamiltonian path with all spans \(\ge4\) can leave a
  gap above 8 in the reachable savings set. That is a hand question about span
  systems, not a search.
