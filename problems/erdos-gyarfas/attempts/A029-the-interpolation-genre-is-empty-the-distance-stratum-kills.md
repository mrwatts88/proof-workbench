# A029 — the interpolation genre is empty: the distance stratum kills (INT) and (INT-14), the parity stratum kills every relativized form

- Date opened: 2026-07-26
- Problem: `P-002`
- Status: active
- Portfolio role: primary (Tier 1, `G015` case (5b), proof side; session
  `S031`). Executes the recorded next action's **kill test** rather than its
  proof attempt: `A028` T9 recorded (INT) as the order-unbounded successor
  architecture and `C050` as its survived kill test. That kill test was run
  against every recorded profile object *on disk*. It was never run against
  the calibration object `A028` T1 had constructed eight theorems earlier.

## Intended mechanism

The recorded next action is "attack (INT) on the Hamiltonian stratum with
`A026` T6's chord-exchange calculus". The dossier's own kill discipline
(`A021`, restated as binding in `A026` plan step 2) requires a candidate
lemma to be tested against **every** calibration object before it is worked
on. S030 created Calibration object #3 in `A028` T1 and stated its purpose
narrowly: "any proposed proof that the profile forces a Hamiltonian
through-path must fail on it". That is one use of a calibration object. The
other — the one `A021` established with Petersen\(-e\) — is that it is a
witness against *any* lemma whose hypotheses it satisfies.

Calibration object #3 satisfies every hypothesis of (INT).

This attempt therefore runs the kill test first, and then asks the wider
question: is the failure repairable, or is the whole **interpolation genre**
— lower-bound theorems of the form "the through-set of a class member has no
gaps above a threshold" — empty at class strength, in the way that the
congruence genre (`C037`) and the membership genre (`L045`/`C045`) are
already known to be empty?

## Entry assumptions

Statement 0.1 verbatim. Consumed at recorded strength: `L053` (`A028` T1 —
the calibration object, **proved**, including its profile, girth and
2-connectivity), `L050` (interference-completeness ⟺ vertex-tautness on
connected \(\delta\ge2\) graphs), `L035` T2 (parity-constancy ⟺
bipartiteness), `L042` (residual-object forced structure, including
\(S\cap\mathbb P\ne\emptyset\) and \(S\cap(\mathbb P-1)\ne\emptyset\) in the
non-triangle case), `L048`(iii) (the spectrum identity), `L046`
(2-connectivity below its threshold), `C046`/`C047` (census and dissection
corpora), `C050` ((INT)'s recorded kill test), `C049` (the order-21 rung).
External: `X001`–`X003` as recorded in
`references/large-girth-non-hamiltonian-cubic-2026-07-26.md`; **new** `X004`
in `references/bipartite-large-girth-cubic-2026-07-26.md`.

## Targeted obligations

- `G015`: exclude case (5b). This attempt removes a recorded route to it and
  re-orders what remains; it excludes nothing.
- `G013`(a): structure theory for the tight-1-atom question.

## Plan and decisive tests

1. **Run the omitted kill test.** Test (INT) and (INT-14) against
   Calibration object #3 before doing any span-system work. Cost: minutes.
   If they survive, proceed to the recorded next action unchanged.
2. **If they fail, test the natural repair immediately** — relativizing the
   threshold to \(\min S\), which is what the recorded pivot trigger already
   does implicitly — rather than reporting only the negative.
3. **Pivot trigger.** If both fail, the session's job changes from proving a
   lemma to characterising the genre and re-ordering the portfolio; say so
   and do not manufacture a replacement conjecture without a kill test of its
   own.

## Notation

A **profile pair** is \((H,a,b)\) with \(H\) finite simple, \(a\ne b\),
\(d_H(a)=d_H(b)=2\) and \(d_H(v)\ge3\) for every other vertex.
\(S=S(H,a,b)\) is the set of lengths of simple \(a\)–\(b\) paths,
\(\mathrm{Spec}(H)\) the set of cycle lengths, \(\mathbb P=\{4,8,16,\dots\}\).
The **poison set** is \(\mathbb P-2=\{2,6,14,30,62,\dots\}\).

The two recorded conjectures under test (`A028` T9, verbatim in content):

> **(INT)** — for a vertex-taut \(\{C_4,C_8\}\)-free profile pair,
> \(S\supseteq[8,\max S]\).
>
> **(INT-14)** — for a vertex-taut \(\{C_4,C_8\}\)-free profile pair with
> \(\max S\ge14\), \(14\in S\).

(INT-14) is the operative one: with `L048`(iii) it is all (F-S) needs, and
`A028` T9 recorded it as "better supported than full (INT)".

---

## Deductions

### T1 (the distance stratum: (INT) and (INT-14) are both false) — proved

> **(INT) and (INT-14) are false**, with explicit witnesses:
> a vertex-taut \(\{C_4,C_8\}\)-free profile pair of order **30**, which is
> also 2-connected, with \(S=[9,26]\) (so \(8\notin S\), \(\max S\ge8\));
> and a vertex-taut one of order **59** — **not** 2-connected, which (INT)
> does not require — with \(S=[18,52]\) (so \(14\notin S\),
> \(\max S\ge14\)). The same conclusion also follows asymptotically from the
> already-proved `L053`.

*Proof, asymptotic form (the route the attempt found first).* Take \(H=F-ab\) exactly as in `L053` (`A028` T1): \(F\) is a cubic,
3-connected, simple graph of girth \(\ge17\) and \(ab\in E(F)\). `L053`
already establishes for this \(H\): it is a profile pair
(\(d_H(a)=d_H(b)=2\), all other degrees 3); it is 2-connected; it has girth
\(\ge17\), so \(4,8,16\notin\mathrm{Spec}(H)\). Being 2-connected with
\(\delta\ge2\) it is **vertex-taut** — the fan form of Menger puts every
vertex on an \(a\)–\(b\) path, exactly the step `A028` T3(ii) uses; `L050`
gives the same conclusion.

The one fact `L053` did not record: **every \(a\)–\(b\) path of \(H\) has
length \(\ge16\).** If \(Q\) is an \(a\)–\(b\) path of \(H\) of length
\(\ell\), then \(Q+ab\) is a cycle of \(F\) of length \(\ell+1\), and girth
\(\ge17\) gives \(\ell\ge16\).

\(S\ne\emptyset\) (vertex-tautness, or 2-connectivity), so
\(\max S\ge\min S\ge16\). Hence \(8\in[8,\max S]\setminus S\), refuting
(INT); and \(\max S\ge14\) with \(14\notin S\), refuting (INT-14). ∎

**Repaired after `R004` F4 — the refutation is not asymptotic, and it lands
inside the window.** The draft of this attempt asserted that a profile pair
with \(\min S\ge9\) needs girth \(\ge10\) and hence order \(\ge70\) by the
\((3,10)\)-cage bound. That is **false**, and the audit produced the
counterexample. The cubic-minus-an-edge route is not the only route: applying
the triangle expansion of T2 at *every* vertex — i.e. **truncation** — costs
nothing in girth terms and buys distance.

> **The order-30 witness.** Let \(P^{\ast}\) be the truncated Petersen graph
> (replace each vertex of the Petersen graph by a triangle, each triangle
> vertex inheriting one of the three edges). \(P^{\ast}\) is cubic and
> 3-connected on **30** vertices, and its cycle spectrum below 13 is
> \(\{3,10,11,12\}\): a cycle other than a triangle uses \(\ell\ge5\) link
> edges and traverses \(\ell\) triangles at cost 1 or 2 each, so its length is
> in \([2\ell,3\ell]\subseteq[10,\infty)\). Hence \(P^{\ast}\) is
> \(\{C_4,C_8\}\)-free. Delete a **link** edge \(ab\): \(H=P^{\ast}-ab\) is a
> 2-connected — hence vertex-taut — exactly-two-profile pair of order 30 with
> \(S=[9,26]\).

So \(\min S=9\) and \(8\notin S\) while \(\max S=26\): **(INT) is false at
order 30**, inside the case-(5b) window \([22,40]\) of T5, and inside the
recorded window \([18,35]\) too. No import of any kind is used.

> **The order-59 witness for (INT-14).** Take two copies of \(H\) and identify
> \(b\) of the first with \(a\) of the second. The identified vertex has degree
> \(2+2=4\); the two surviving terminals have degree 2; no cycle is created at
> a cut vertex, so \(\{C_4,C_8\}\)-freeness persists; and every vertex lies on
> a terminal-to-terminal path because each copy is vertex-taut, so the chain is
> too (it is **not** 2-connected — the identified vertex is a cut vertex — but
> (INT) requires only vertex-tautness). Every terminal-to-terminal path splits at the cut vertex, so
> \(S=S(H)+S(H)=[18,52]\). Order \(30+30-1=59\).

Hence \(14\notin S\) with \(\max S=52\): **(INT-14) is false at order 59** —
below the 70 the draft claimed as a floor, though above the window.

**Why the recorded kill test missed it.** `C050`/`E029` recomputed \(S\) from
the stored graph6 strings of **24 recorded profile objects**, all of orders
19–22, plus the 9,061-row near-miss corpus (orders \(\le20\)). Every one of
those objects has \(\min S\le5\): the eight `A025` T3 objects have
\(S\supseteq[6,n-1]\); Petersen\(-e\) has \(\min S=4\); the order-21 `C049`
member has \(S=[4,20]\setminus\{6\}\); the order-22 objects have
\(\min S\in\{1,5\}\). **No object with \(\min S>8\) exists anywhere on disk.**
That is a fact about what has been *generated*, not about the class: the
searches are ladders over the \(\{C_4,C_8\}\)-free class by order, and they
stop at 21, while the smallest known distance witness has order 30. `C047`(a)
records that the corpus's distance dodges (shape A′) cap at \(\min S=7\)
"exactly, never \(\ge8\)"; those rows carry \(\ge4\) degree-2 vertices, so
they constrain the *near-miss* class and say nothing about the profile class
at all — reading that cap as a class property, rather than as a property of
the generated range, is what made (INT) look safe.

**Scope.** T1 is **not** asymptotic. It exhibits an explicit order-30 object
inside every window the programme uses, and an explicit order-59 object for
the operative form. It still moves no floor and changes no status: both
witnesses contain \(C_{16}\) (\(16\in\mathrm{Spec}(P^{\ast})\)) and are far
from power-free. It does not contradict `C050`'s 24/24 — none of those 24 is
this object — and it does not contradict `C047`(a). The `L053` route (a cubic
3-connected graph of girth \(\ge17\) minus an edge, giving \(\min S\ge16\))
remains valid and is the asymptotic version of the same mechanism; it is no
longer the primary witness.

**Consequence for the recorded architecture.** `A028` T9's implication
"(INT) ∧ (L-A) ⟹ (F-S) at every order" is unaffected as an implication; its
antecedent is false. (L-A) — \(\max S\ge14\) — is *true* on the object above,
so the failure is squarely (INT)'s. The successor architecture of S030 is
dead in the form recorded.

### T2 (the parity stratum: every relativized form fails too) — proved modulo `X004`

The obvious repair is to relativize the threshold to \(\min S\), which is
what the recorded **pivot trigger** already does implicitly ("a profile
object at any order with a **hole** in \(S\) at a value \(\ge8\)" — a value
below \(\min S\) is not a hole). Write

> **(INT-rel\(_c\))** — for a vertex-taut \(\{C_4,C_8\}\)-free profile pair,
> \(S\supseteq[\min S+c,\max S]\),

for a constant \(c\); the pivot-trigger form is the \(c\)-free assertion "no
hole at a value \(\ge8\)". T2 kills all of these at once.

> For every even \(g\ge10\) and every \(r\ge g/2\), given a bipartite cubic
> 3-connected graph of girth \(g\) and order \(>2^{\,r+1}-2\), there is a
> vertex-taut
> \(\{C_4,C_8\}\)-free profile pair \((H,a,b)\) which is **non-bipartite**,
> 2-connected, has \(\min S=g-1\) (odd, \(\ge9\)), and has \(h\notin S\) for
> **every even** \(h\in[g,2\rho+2)\) with \(\rho\ge r\). In particular
> \(\min S+1=g\) is a **hole at a value \(\ge10\)**; the hole contains at
> least \(r+1-g/2\) even values, unbounded as the order grows at fixed girth,
> so (INT-rel\(_c\)) fails for every constant \(c\) and the recorded pivot
> trigger fires.

*Construction.* Let \(\tilde F\) be a connected **bipartite** cubic
3-connected graph of even girth \(g\ge10\) and order \(N>2^{\,r+1}-2\) for
a radius \(r\ge g/2\) fixed in advance (`X004`, in its **decoupled** form:
girth held fixed while the order grows. The **order** is what (v) consumes —
see the ball bound there — and at \(g=10\), \(r=g/2\) it is automatic).
Pick a vertex \(v\) with
neighbours \(n_1,n_2,n_3\) and let \(F_1\) be the **triangle expansion** of
\(\tilde F\) at \(v\): delete \(v\), add a triangle \(T=v_1v_2v_3\), and join
\(v_i\) to \(n_i\). Let \(\pi:V(F_1)\to V(\tilde F)\) contract \(T\) back to
\(v\). Choose an edge \(ab\in E(\tilde F)\subseteq E(F_1)\), write
\(\rho:=d_{F_1}(\{a,b\},T)\), and set \(H=F_1-ab\). Steps (i)–(iv) hold for
**any** choice of \(v\) and \(ab\) with \(\rho\ge1\); the specific choice
that opens the hole is made in (v).

*(i) \(F_1\) is cubic and 3-connected.* Cubic is immediate. Suppose a set of
at most two vertices separates \(F_1\); enlarging it if necessary, write it as
\(\{x,y\}\) with \(x\ne y\) (a single cut vertex is covered by adding any
second vertex, which cannot restore connectivity). \(T\) induces a triangle,
so \(T\setminus\{x,y\}\) lies in a single component.

- \(\{x,y\}\cap T=\emptyset\): \(T\) lies wholly on one side, so contracting
  \(T\) carries the separation to a 2-separation of \(\tilde F\) —
  impossible.
- \(\{x,y\}\cap T=\{v_1\}\), say: \(v_2,v_3\) lie in one component \(C\), and
  some component \(D\) misses \(T\). If \(C\setminus T\ne\emptyset\), then any
  \(\tilde F\)-path from \(D\) to \(C\setminus T\) avoiding \(\{v,y\}\) lifts
  to an \(F_1\)-path avoiding \(T\cup\{y\}\supseteq\{v_1,y\}\), so
  \(\{v,y\}\) would separate \(\tilde F\) — impossible. And
  \(C\setminus T=\emptyset\) forces \(n_2,n_3\in\{v_1,y\}\), hence
  \(n_2=n_3=y\), i.e. a repeated edge at \(v\) in \(\tilde F\) — impossible
  in a simple graph.
- \(|\{x,y\}\cap T|=2\), say \(\{v_1,v_2\}\): then \(F_1-\{v_1,v_2\}\) is
  \(\tilde F-v\) with a pendant \(v_3\) attached at \(n_3\), and
  \(\tilde F-v\) is connected because \(\tilde F\) is 3-connected. Not a
  separation. ∎(i)

Hence \(H=F_1-ab\) is 2-connected, so it is **vertex-taut**.

*(ii) \(H\) is a \(\{C_4,C_8\}\)-free profile pair.* Degrees: \(a,b\) drop to
2, every other vertex keeps degree 3, and \(a,b\notin T\) since \(\rho\ge1\)
(so \(ab\), an edge of \(\tilde F\) not incident to \(v\), is an edge of
\(F_1\) — the inclusion \(E(\tilde F)\subseteq E(F_1)\) asserted in the draft
is of course false in general, and only this one edge is needed). Cycles of
\(F_1\): a cycle other than \(T\) meets \(T\) in \(k\in\{0,1,2\}\) edges and
projects under \(\pi\) to a closed walk of \(\tilde F\) of length \(\ell-k\),
which is a cycle whenever \(\ell-k\ge3\) — and \(\ell-k\le2\) forces
\(\ell\le4\) with the projection degenerate, which the triangle case already
covers. So \(\mathrm{Spec}(F_1)\subseteq\{3\}\cup[g,\infty)\) with
\(g\ge10\): no \(C_4\), no \(C_8\). ∎(ii)

*(iii) \(\min S\ge g-1\ge9\), and every \(a\)–\(b\) path avoiding \(T\) has
odd length.* If \(Q\) is an \(a\)–\(b\) path of \(H\), then \(Q+ab\) is a
cycle of \(F_1\), of length 3 or \(\ge g\); length 3 would put \(a,b\) on the
unique triangle \(T\), excluded. So \(|Q|\ge g-1\). If \(Q\) misses \(T\) then
\(\pi(Q)=Q\) is an \(a\)–\(b\) path of \(\tilde F\); \(\tilde F\) is
bipartite and \(ab\in E(\tilde F)\), so \(a,b\) lie in opposite classes and
\(|Q|\) is odd. ∎(iii)

*(iv) Even lengths cost \(2\rho\).* \(Q\) is a path and \(T\) a triangle, so
\(Q\cap T\) is a subpath of \(T\) using \(k\in\{0,1,2\}\) triangle edges, and
\(\pi(Q)\) is an \(a\)–\(b\) path of \(\tilde F\) of length \(|Q|-k\), hence
odd (note \(k=0\) covers both "\(Q\) misses \(T\)" and "\(Q\) passes through
exactly one \(T\)-vertex"). So \(|Q|\) is even **exactly when \(k=1\)**; such
a \(Q\) meets \(T\), and splitting it at its first and last \(T\)-contacts
gives \(|Q|=|{\rm seg}_a|+1+|{\rm seg}_b|\ge\rho+1+\rho=2\rho+1\), where the
middle 1 is the single triangle edge; being even, \(|Q|\ge2\rho+2\). ∎(iv)

*(v) The choice of \(ab\) and \(v\), and the hole.* Rebuilt after `R004`
F1/F2; the draft's numerics were wrong in two independent places and its
parameter choices were made in the wrong order.

Make the choices **in this order**:

1. choose \(ab\) **on a shortest cycle** of \(\tilde F\), so that the shortest
   cycle through \(ab\) has length exactly \(g\);
2. choose \(v\) with \(\rho=d(\{a,b\},v)\ge r\), for a radius \(r\ge g/2\)
   fixed in advance.

Step 2 is where the previous revision went wrong (`R004` F11): it derived
\(\rho\) from the **diameter**, which is a non sequitur once \(ab\) is
already fixed — what the construction consumes is the eccentricity of a
*pre-chosen* edge, and \(\mathrm{diam}=D\) gives only
\(\mathrm{ecc}(\{a,b\})\ge(D-1)/2\). The correct hypothesis is on the
**order**, and it is a one-line ball count. Girth \(g\) makes
\(B(\{a,b\},r-1)\) a tree: \(a\) and \(b\) contribute 2 vertices, each has
2 neighbours besides the other, and every subsequent vertex has 2 children, so
\[
  \lvert B(\{a,b\},r-1)\rvert\;\le\;2+4(2^{\,r-1}-1)\;=\;2^{\,r+1}-2 ,
  \qquad r\le g/2 .
\]
Hence **if \(N>2^{\,r+1}-2\) then some vertex lies at distance \(\ge r\)
from \(\{a,b\}\)**, which is step 2. No diameter, no eccentricity argument,
and no equality analysis of the Moore bound.

Two consequences worth recording. At \(r=g/2\) and \(g=10\) the requirement
is \(N>2^{6}-2=62\), which is **automatic**: a cubic graph of girth 10 has
order \(\ge70\). So the pivot-trigger form of T2 needs no order hypothesis at
all. And taking \(r\) large with \(g\) fixed gives \(\rho\ge r\)
from \(N>2^{\,r+1}-2\) alone, which is what supplies arbitrarily long holes
(`R004` F13 — previously asserted from "\(\mathrm{diam}\to\infty\)").

*\(\min S=g-1\), and it is odd.* The \(\ge\) is (iii). For the \(\le\): the
shortest cycle through \(ab\) gives an \(a\)–\(b\) path \(Q_0\) of
\(\tilde F-ab\) of length \(g-1\); every vertex of \(Q_0\) is within distance
\(\lfloor(g-1)/2\rfloor=g/2-1\) of \(\{a,b\}\), which is \(<\rho\), so
\(Q_0\) avoids \(v\) and survives verbatim in \(H\). As \(\tilde F\) is
bipartite, \(g\) is even, so \(\min S=g-1\) is odd, and \(\ge9\).

*The hole.* \(\min S+1=g\) is even, so by (iv) it lies in \(S\) only if
\(g\ge2\rho+2\), i.e. \(\rho\le g/2-1\) — excluded by choice 2. Hence
\(g\notin S\). It exceeds \(\min S\); it is \(\ge10\); and it is below
\(\max S\), because \(H\) is **vertex-taut** by (i), so every vertex of
\(T\) lies on some \(a\)–\(b\) path — that path meets \(T\), so by (iv)'s
count it has length \(\ge2\rho\ge g\) (`R004` F12: "\(v\) is not a cut
vertex" was the wrong justification; it does not produce a path *through*
\(v\), and tautness is already available). Since \(g\notin S\),
\(\max S>g\). So \(g\) is a **hole at a value \(\ge10\)**.

*Arbitrarily long holes.* By (iv) every even value in \([g,2\rho+2)\) is
absent, so the hole contains \(\rho+1-g/2\) even values. Fixing \(g=10\) and
taking \(N>2^{\,r+1}-2\) gives \(\rho\ge r\) for any prescribed \(r\), so
the hole is arbitrarily long. Therefore \(S\supseteq[\min S+c,\max S]\) fails
for every constant \(c\). ∎

**What the numbers actually need, recorded so the next reader does not have to
re-derive them.** The hole needs \(\rho\ge g/2\); the \(\min S=g-1\)
identification needs \(\rho\ge g/2\) as well; and \(\rho\ge r\) follows from
\(N>2^{\,r+1}-2\). So the requirement on the ambient graph is on its
**order**, not its diameter — and at \(g=10\) it is automatic. Three earlier
revisions got this wrong in three different ways (\(\mathrm{diam}\ge5\);
\(\mathrm{diam}\ge g\); \(\mathrm{diam}\ge g/2+1\)), which is why the
requirement is now derived rather than asserted. The Tutte 12-cage was
withdrawn as a witness on the way (`R004` F3) and stays withdrawn; with the
order form it is simply irrelevant.

**\(F_1\) is non-bipartite** (it contains \(T\)), so the repair "add
non-bipartiteness, which `L042` supplies anyway" does not save (INT-rel).

**The cheap half, recorded for completeness.** Dropping the
non-bipartiteness demand, \(\tilde F-ab\) itself is a vertex-taut
\(\{C_4,C_8\}\)-free profile pair whose through-set is **all-odd** (`L035`
T2), hence has holes at every even value above \(\min S\). That instance is
one line, and a defender answers it by importing `L042`'s
non-bipartiteness. The triangle expansion is what removes that answer.

### T3 (the genre is empty, and what an interpolation lemma would have bought) — analysis

**(a) Three dead genres.** The dossier now has three results of the same
shape, each saying a whole *style* of argument cannot exclude case (5b) from
the class-level hypotheses:

| genre | statement | killed by |
|---|---|---|
| congruence | no congruence-type theorem at any modulus excludes case (5b) from the forced hypotheses | `C037`/`A021` T1 (Petersen\(-e\); the \(2\lvert E(P)\cap E(Q)\rvert\) leak) |
| membership | membership arithmetic alone never excludes the chain case; no membership-collision pattern is universal | `L045`; `C045`/`A025` T1 |
| **interpolation** | **no lower bound of the form "\(S\) has no gap above a threshold" — absolute or relativized to \(\min S\) — holds at class strength** | **T1, T2 (this attempt)** |

The common structure is worth naming, because it predicts the next failure.
Each dead genre tries to derive a *global* arithmetic fact about \(S\) or
\(\mathrm{Spec}\) from hypotheses that are **local and hereditary**: degree
profile, forbidden short cycles, tautness, 2-connectivity. Every one of those
is satisfied by a large-girth cubic graph minus an edge, and on such an
object \(S\) is confined to an interval far above the small poison values.
The two hypotheses the case-(5b) residual object has that large-girth objects
do **not** are **power-freeness** (at powers *above* the girth) and
**minimum-order minimality**. Neither has ever been consumed by an (F)-side
lemma. That is the diagnosis, and it is `A021`'s diagnosis about
Petersen\(-e\) restated with a second, strictly stronger witness.

**(b) What an interpolation lemma would have bought.** Recorded because it is
why the genre looked attractive, and because it survives as a *conditional*
structure fact. Suppose, for the case-(5b) residual object \((H,a,b)\) with
\(ab\notin E\), that \(S\supseteq[\min S+c,\max S]\) for some constant \(c\).
`L042` gives \(S\cap\mathbb P\ne\emptyset\); fix \(2^j\in S\). The poison
condition gives \(2^j-2\notin S\) and \(2^{j+1}-2\notin S\). Then

- \(2^j-2<\min S+c\) (else \(2^j-2\in[\min S+c,\max S]\subseteq S\)), so
  \(\min S>2^j-2-c\);
- \(2^{j+1}-2>\max S\) (else it lies in that same interval, using
  \(2^{j+1}-2>2^j\ge\min S\) and \(2^{j+1}-2\ge\min S+c\) for
  \(2^j\ge c+2\)), so \(\max S\le2^{j+1}-3\).

Hence

\[
  2^j-2-c\;<\;\min S\;\le\;2^j\;\le\;\max S\;\le\;2^{j+1}-3 ,
\]

so the through-set is pinned into a single dyadic band anchored at \(2^j\)
(and \(2^j\) is then the **unique** power of two in \(S\): \(2^{j+1}>\max S\)
outright, and \(2^{j-1}<\min S\) as soon as \(2^{j-1}\ge c+2\)), and

\[
  \max S\;<\;2\min S+2c+2
  \qquad\text{(valid for integer }c\text{ with }2^j\ge c+2\text{)} .
\]

Up to the additive constant that is exactly the condition
\(s_{\max}\le2\,s_{\min}\) which `L031`/`L032` isolate as the **block
question's** defining constraint — the two live arms of `G013` would have
met. `L042`'s Mersenne membership tightens it further: \(2^k-1\in S\) with
\(2^j-2-c<2^k-1\le2^{j+1}-3\) forces \(k=j\) once \(c<2^{j-1}\), i.e.
\(2^j-1\in S\) and \(\min S\le2^j-1\).

Recorded as **conditional structure, not progress**: T1 and T2 show the
hypothesis is false at class strength, so this can only be used after an
interpolation lemma is proved *from power-freeness or minimality*, which is
the open problem. Its value is that it names the exact prize, and a
convergence the portfolio did not know it had.

**(c) The ceiling finding is unchanged; its constant is stale, and moving it
makes things worse, not better.** See T5, which performs the re-derivation.

### T5 (the order dichotomy re-derived from the current floors) — proved, in the `L046` frame

Added after `R004` was dispatched; the audit's scope is T1/T2/T3(b) as fixed
in its target identification, and nothing in T5 feeds them.

`L046`'s constant is explicitly lineage-dependent — the `CLAIMS.md`
dependency note records "32 from `C027`+`C036`; 36 once `C039`'s two-order
class extension is consumed" — and the block-order input has moved three
orders since. `A022` W1-T8's proof is unchanged; only its input changes.

**The input.** W1-T8(1) needs: a non-bridge block \(L\) of the chain is
connected, \(C_4\)-free, of minimum degree \(\ge2\), **power-free**, and has
at most two vertices of degree 2 (its terminals). Every such graph of order
\(\le20\) is excluded — `C039` for orders \(\le17\) (`C027`'s whole class),
`C043` at 18–19 and the S022 harvest at 20 (all three degree-2 buckets
empty). At order 21 the 0-bucket is excluded by `C040` (no
\(\{C_4,C_8\}\)-free \(\delta\ge3\) graph at 14–21) and the 2-bucket by
`C049` (the complete order-21 class has 19 profile members, none power-free;
its power-free members have degree-2 count \(\ge5\)). Only a 1-bucket member
of order exactly 21 is not excluded by direct generation, so the conservative
input is

> every non-bridge block has order \(\ge21\).

**The arithmetic.** \(|V(H)|=\sum_i|V(L_i)|-(m-1)\) with \(k\) non-bridges
and \(m-k\) bridges of order 2, and \(k\ge\lceil(m+1)/2\rceil\) (W1-T1(3)):

- \(m=2\): \(k=2\), \(|V(H)|\ge21+21-1=41\), so \(n_0\ge42\);
- \(m=3\): \(k\ge2\), \(|V(H)|\ge21+21+2-2=42\), so \(n_0\ge43\);
- \(m\ge4\): \(k\ge3\), \(|V(H)|\ge3\cdot21+2(m-3)-(m-1)=58+m\ge62\), so
  \(n_0\ge63\);
- linear form: \(n_0-1\ge21\lceil(m+1)/2\rceil+m+1\), hence
  \(m\le(n_0-12)/11\).

> **Order dichotomy, current.** Either \(H\) is 2-connected, or
> \(n_0\ge42\). Every chain has \(m\ge2\), so the chain case is empty below
> \(n_0=42\).

**What this does to the window, and why it is bad news.** The recorded
case-(5b) window was \(n_0\in[18,35]\), i.e. \(H\)-orders \([17,34]\); the
ladder `E028` is indexed by \(H\)'s order and ran 16–30. With the current
floors the window is \(n_0\in[23,41]\) — the bottom rises because every tight
1-atom has order \(\ge23\) (`C049`) — i.e. \(H\)-orders \([22,40]\). So the
ladder has covered 22–30 of a window that ends at **40**, not 34: **ten rungs
remain, not four.** At the measured wall-clock growth of 1.8–2.4 per rung
(`R003` F3) those ten rungs are not reachable. S030's ceiling finding is
therefore not softened by the re-derivation — it is sharpened. The (F)
programme is further from covering its own window than the records said, and
the correction runs in the direction that makes the finite-window route less
attractive, not more.

Conditionality is exactly `L046`'s: the (R) frame, and `C039`/`C043`/`C049`/
`C040` consumed at "tested" strength with their recorded generator lineage.
Offered as ledger row `L058`, superseding `L046`'s constant while leaving its
statement shape and its proof intact.

### T4 (the re-aim) — analysis

What T1/T2 remove: the successor architecture (INT) ∧ (L-A), and with it the
claim that Tier 1 has an order-unbounded route. What they do **not** remove:
(L-A) itself; the positive-savings theorem `L055`; the chord-exchange
calculus `A026` T6, which remains a true statement about the objects it was
measured on and simply cannot be promoted to a class-level theorem; and the
entire finite-window programme.

The honest portfolio position after this attempt is that **every live Tier-1
route is window-bounded, and the width of that window is currently
mis-recorded.** Ordered moves, cheapest first:

1. ~~Re-derive `L046`'s threshold~~ — **done in T5**: the window is
   \(n_0\in[23,41]\), the ladder is ten rungs short of it rather than four,
   and the correction makes the finite-window route *less* attractive.
2. **Close the non-Hamiltonian stratum's two gaps** (`A028` T8:
   component-atomic minimality; savings per position rather than per
   component). This is the only remaining route that makes the window's
   *interior* fully decided rather than half-decided, and `L055` already
   supplies its engine.
3. **Consume power-freeness for the first time on the (F) side.** Every dead
   genre died because its hypotheses are inherited by \(F-ab\) for
   large-girth cubic \(F\). The first (F)-side lemma that is *false* on that
   object — i.e. one that uses \(4,8,16,32,\dots\notin\mathrm{Spec}(H)\) at a
   power **above** the girth, or uses minimum-order minimality — is the first
   that can be order-unbounded. Named target; no proof step exists yet.
4. **Open search question** (not a proof route): the smallest order at which
   the distance stratum is nonempty. `C046` shows it is empty at \(\le20\);
   the cubic-minus-an-edge route needs order \(\ge70\). A witness inside
   \([21,35]\) would refute (INT) *in the window* and would also be a new
   class member at an order where the ladder has been running.

**Kill discipline going forward**, strengthened by this attempt:
**Calibration object #3 is now the primary calibration object for the (F)
side**, ahead of Petersen\(-e\), because it satisfies every class-level
hypothesis simultaneously at arbitrarily large order. Any proposed (F)-side
lemma must be checked against it *before* it is worked on, and the check is
mechanical: if the lemma's hypotheses are girth-monotone and its conclusion
mentions a specific value below the girth, it is false.

---

## Failure analysis

- **The recorded next action was not attempted.** Its target is false, so the
  chord-exchange work it prescribed would have been spent proving something
  untrue. The hand question it named — "can a chord-minimal cover with all
  spans \(\ge4\) leave a gap above 8 in the reachable savings set?" — is not
  answered here and is moot as stated: at class strength the answer is yes,
  and T1 exhibits the reason without any span analysis.
- **T2 rests on one new import** (`X004`). It is an existence use inside a
  **negative** result, so an error in it could only remove a warning, never
  create a false proved row — the discipline `X001`'s audit already records.
  T1, the operative kill, rests on no new import at all: it is a two-line
  corollary of the already-proved `L053`.
- **T2's numerics were wrong twice and the parameter choices were made in the
  wrong order; both are repaired, and the audit caught them.** `R004` F1/F2:
  the draft chose \(ab\) to *maximise* \(\rho\), which is orthogonal to (and in
  large graphs in tension with) \(ab\) lying on a girth cycle, so
  \(\min S=g-1\) was assumed rather than derived; and it inferred
  \(\rho\ge5\) from diameter \(\ge5\) (false in a bipartite graph, where
  \(\rho\le\mathrm{diam}-1\)) and \(2\rho\ge g+1\) from \(\rho\ge(g-1)/2\)
  (false). T2(v) is rebuilt: choices ordered, \(\rho\le\mathrm{diam}-1\)
  proved, the even bound sharpened to \(2\rho+2\) (`R004` F5 — and this
  sharper bound is what `E030` observed all along), and the requirement
  restated correctly as \(\mathrm{diam}(\tilde F)\ge g/2+1\).
- **The named witness in `X004` was wrong and is withdrawn** (`R004` F3). The
  Tutte 12-cage has girth 12 and diameter 6, so \(\rho\le5<6\); every
  \((3,g)\)-cage has diameter \(\approx g/2\), so the whole cage family sits
  in the failing regime. `X004` is restated in **decoupled** form — girth
  fixed at \(\ge10\), order and diameter unbounded — which is what T2 needs
  and what the coupled "larger girth ⟹ larger diameter" form does not give.
- **T1's order-70 claim was false and is deleted** (`R004` F4). "A profile
  pair with \(\min S\ge9\) needs girth \(\ge10\), hence order \(\ge70\)" is
  refuted by truncated Petersen minus a link edge: order **30**,
  \(S=[9,26]\). The audit produced it; it is verified in `E030`. The effect is
  that T1 is **stronger** than the draft claimed — (INT) is false *inside* the
  window, not merely asymptotically — and T4's move 4, which asked for exactly
  such an object, is answered rather than open.
- **What this attempt does not settle.** It does not determine the smallest
  order at which the distance stratum is nonempty (T4 move 4), and it does
  not exhibit any object inside the window. Both refuting objects are far
  from power-free — they are calibration objects, not counterexample
  candidates. **No floor moves and no status changes**; nothing here bears on
  statement 0.1.

## Salvageable results

1. **T1** — (INT) and (INT-14) are false, with **explicit in-window
   witnesses**: order 30 for (INT) (\(S=[9,26]\)) and order 59 for (INT-14)
   (\(S=[18,52]\)), neither using any import; plus the asymptotic `L053`
   route. Offered as ledger row `L056`, with the diagnosis of why `C050`
   survived (nothing with \(\min S>8\) has ever been *generated*, because the
   ladders stop at order 21 and the smallest known witness has order 30).
2. **T2** — no relativized interpolation either, and the recorded pivot
   trigger fires; offered as `L057` (modulo `X004` in its decoupled form),
   **repaired after `R004` and not yet re-audited** — see the obligation in
   the review section. Every step is verified on an explicit 106-vertex graph
   (`E030`), whose observed hole matches the repaired bound \(2\rho+2\)
   exactly. The triangle-expansion construction is reusable in two ways: at
   one vertex it produces **non-bipartite** class members with long parity
   holes, and at *every* vertex (truncation) it produces the order-30 witness
   of T1.
3. **T3(a)** — the three-dead-genres table and the shared diagnosis: local
   hereditary hypotheses are all inherited by large-girth cubic graphs minus
   an edge, and power-freeness and minimality have never been consumed.
4. **T3(b)** — the dyadic pinning, conditional: any interpolation lemma
   yields \(\max S<2\min S+O(1)\), i.e. `L031`/`L032`'s block-question
   constraint. A recorded convergence between the two live arms of `G013`.
5. **T5** — the order dichotomy re-derived from the current floors: either
   \(H\) is 2-connected or \(n_0\ge42\), so the case-(5b) window is
   \(n_0\in[23,41]\) (\(H\)-orders \([22,40]\)) and the `E028` ladder is
   **ten** rungs short of it, not four. Offered as `L058`, superseding
   `L046`'s constant. The correction runs against the finite-window route.

## Adversarial review

**`R004`, delegated to a fresh-context `proof-reviewer` (independence mode
`delegated-subagent`): FAIL at lemma level** — 2 critical, 2 major, 4 minor,
2 notes. The audit was initiated voluntarily (no statement-level candidate is
offered, so the mandatory transition of `AGENTS.md` is not triggered) because
the finding reverses a recorded portfolio direction. It was worth it: the
reviewer broke T2 and improved T1.

Verdict by deduction, and what was done:

- **T1 — the refutation PASSES**; the reviewer verified every hypothesis match
  and confirmed `L053` is used inside its recorded scope. But its *diagnostic*
  clause ("none can exist below order 70 by the cage bound") is **false**, and
  the reviewer refuted it with an explicit order-30 object built during the
  audit (**F4**, major). **Resolved:** the clause is deleted; the object is now
  T1's primary witness, independently rebuilt and verified here
  (`E030/truncation.py`: order 30, cubic, 3-connected, cycle spectrum below 13
  \(=\{3,10,11,12\}\), \(S=[9,26]\)); the order-59 chain for (INT-14) is
  proved by the cut-vertex sum \(S=S_1+S_2\); and T1's scope note, which said
  the result exhibits nothing in the window, is corrected — it exhibits an
  object *inside* it. T4's move 4 is answered, not open.
- **T2 — FAILS.** **F1** (critical): the hole was not proved to open — \(ab\)
  was chosen to maximise \(\rho\), which does not secure \(\min S=g-1\).
  **F2** (critical): two false numeric steps — "diameter \(\ge5\Rightarrow
  \rho\ge5\)" (bipartite parity gives \(\rho\le\mathrm{diam}-1\)) and
  "\(2\rho\ge g+1\)" from \(\rho\ge(g-1)/2\). **F3** (major): the named `X004`
  witness, the Tutte 12-cage, provably fails the requirement, and every
  \((3,g)\)-cage does; the coupled form of the import does not give
  arbitrarily long holes. **F5** (minor): the boxed claim and the proof used
  different bounds. **Resolved:** T2(v) is rebuilt with the choices ordered,
  \(\rho\le\mathrm{diam}-1\) proved, the even bound sharpened to \(2\rho+2\),
  the requirement restated as \(\mathrm{diam}\ge g/2+1\); `X004` is restated in
  decoupled form and the cage withdrawn. **The repair is not re-audited**, and
  `L057` is offered at that reduced confidence; see the exit state.
- **T3(b) — PASSES** up to side conditions, correctly labelled conditional.
  **F6** (minor) **resolved**: \(2^j\ge c+2\) is now carried into the display,
  the uniqueness clause carries \(c\le2^{j-1}-2\), and \(c\) is integer.
- **F7** (minor, mis-citation) **resolved**: the shape-A′ cap is `C047`(a),
  not `C046`(b), and the inference is weakened accordingly — those rows carry
  \(\ge4\) degree-2 vertices and constrain nothing about the profile class.
- **F8** (minor) **resolved**: the (i) case split now covers a single cut
  vertex, the false inclusion \(E(\tilde F)\subseteq E(F_1)\) is replaced by
  the one edge actually needed, and the \(\ell-k\ge3\) side condition in (ii)
  is stated.
- **F9** (note) **accepted**: T3(b)'s "convergence" with `L031`/`L032` compares
  different objects and stays filed as analysis; no object-level
  identification is made anywhere.
- **F10** (note): T1 survived every attack the reviewer attempted, and nothing
  in the ledger is contradicted by T1 or T2.

Self-checks run before delegation (all still stand):

- **T1's mechanism was verified on a recorded object at girth 5.** The
  identity it turns on is \(\min S=\mathrm{girth}(F)-1\) for \(H=F-ab\).
  Petersen\(-e\) is exactly that object with \(\mathrm{girth}=5\), and an
  independent recomputation returns \(S=\{4,5,7,8\}\) — reproducing the
  dossier's recorded value — with \(\min S=4=5-1\). It satisfies (INT) only
  because \(\max S=8\).
- The claim "no recorded profile object has \(\min S>8\)" was checked against
  `A028` T9's own table row by row.
- T2's connectivity step was proved in all cases rather than asserted.
- T2 was checked to produce **nothing** at the orders of the eight profile
  objects, as it must, since they satisfy (INT).
- T3(b) was checked for vacuity against those same objects: it must fail on
  them, and does, exactly because \(14\in S\).
- **`E030`** verifies T2 (i)–(v) on an explicit 106-vertex graph. Its observed
  smallest even through-length, 14, equals the repaired bound \(2\rho+2=14\)
  exactly — so the experiment had been recording the sharp bound that `R004`
  F5 asked the proof to state, which is why the repair changes no number in
  the experiment.

## Exit state

- Status: active
- Promoted records: ledger rows `L056` (T1, **strengthened** by the audit to
  explicit order-30 and order-59 witnesses), `L057` (T2, repaired after a
  FAIL and **not re-audited** — offered at reduced confidence, with a standing
  obligation to re-audit before any use) and `L058` (T5) offered; experiment
  `E030` (T2's mechanism check plus the order-30 witness); reference `X004`
  restated in decoupled form; review `R004` recorded with all ten findings
  resolved or accepted; `OBLIGATIONS.md` `G015` updated; (INT) retired as a
  target and recorded as **refuted**, not merely unproved.
- Standing obligation from `R004`: T2/`L057`'s repair has not been through a
  fresh audit. The genre conclusion does **not** depend on it — T1 alone kills
  the absolute form, and the bipartite one-liner kills the relativized form
  against a bipartite defender — but the *non-bipartite* relativized kill,
  which is the half that matters given `L042`, rests on the unaudited repair.
- Next action: close the non-Hamiltonian stratum's two `A028` T8 gaps
  (component-atomic minimality; savings per position rather than per
  component), which is the only route that makes the window's interior fully
  decided — with the standing instruction that any lemma drafted for it be
  checked against Calibration object #3 *first*.
