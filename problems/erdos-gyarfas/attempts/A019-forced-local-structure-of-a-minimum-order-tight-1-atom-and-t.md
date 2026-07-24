# A019 — Forced local structure of a minimum-order tight 1-atom and transfer of the two-terminal collapse machinery

- Date opened: 2026-07-24
- Problem: `P-002`
- Status: active
- Portfolio role: primary (Tier 1, `G015` route R1; session S019)

## Intended mechanism

Let \(B\) be a tight 1-atom (`A018` T2: finite, simple, connected,
power-free, unique sub-cubic vertex \(u\) with \(\deg u=2\)) of minimum
order, \(N(u)=\{a,b\}\). Two levers the *unrestricted* 1-atom never
offered:

1. **Order-minimality has a target in its own class.** Deleting \(u\)
   leaves a graph whose degree profile is controlled entirely by
   \((\deg a,\deg b)\) and the cutvertex status of \(u\). Several cases
   should hand back a *smaller tight 1-atom*, which minimality forbids —
   the move `A012` Remark T4.1 tried to make against the degree-1 object
   and could not (its failure case was a cubic pendant-reduct; the
   degree-2 object has no pendant to shed).
2. **The (3,3) case is a closed two-terminal object.** If both
   neighbours are cubic, \(B-u\) is a two-terminal gadget with terminals
   \(a,b\) of inner degree 2 — the dossier's native object — and \(B\)
   is its closure by a 2-path. Power-freeness of \(B\) should then split
   as: \(B-u\) power-free **and** its \(a\)–\(b\) path spectrum \(S\)
   avoids \(\{2^k-2:k\ge2\}=\{2,6,14,30,\dots\}\) (a cycle through
   \(u\) is a path plus 2). That is the ring criterion's shape (`L034`)
   with \(L=1\) and offset 2, and it is where the `L030` middle-layer
   collapse and `L033` pencil dichotomy get their chance to transfer.

A reframing to test *first*, because it changes what "success" needs:
for `G015` the needed lemma is only the **conditional** "if no cubic
counterexample exists, then no tight 1-atom exists" — equivalently,
**a tight 1-atom yields a cubic counterexample**. The unconditional form
is stronger than the reduction requires, and the extra hypothesis is
available exactly where minimality arguments have previously died
(reducts that are counterexamples but not tight 1-atoms).

## Entry assumptions

Statement 0.1 verbatim. D-A1–D-A5 (`A011`), tightness per `A018` T2.
Consumed at recorded strength: `L025` R4 (degree-2 assembly:
edge-doubling a tight 1-atom yields a counterexample), `L029` restated,
`L030`, `L033`, `L034`; base data `C027` (no tight 1-atom of order
\(\le15\)), `C034` (no bipartite tight 1-atom of order \(\le22\)).
Imported, unverified: `C004`–`C006` (Carr) — **not** consumed by R1
deductions unless explicitly flagged as conditional on them (sibling
session S020 is verifying `C006` concurrently; its in-progress state is
not citable here).

## Targeted obligations

- `G015`: the cubic reduction, route R1.
- `G013`(a): the tight 1-atom question.

## Plan and decisive tests

1. **Case analysis at \(u\)** by \((\deg a,\deg b)\) and whether \(u\)
   is a cutvertex, under \(C_4\)-freeness (\(N(a)\cap N(b)=\{u\}\)).
   Decisive test: which cases does minimality kill outright by
   producing a smaller tight 1-atom? Expected survivors: (3,3)
   non-cut; both-\(\ge4\); cut cases with a degree-\(\ge4\) side.
2. **The (3,3) correspondence.** Prove the closure equivalence exactly
   (cycles through \(u\) vs. \(a\)–\(b\) paths; cycles avoiding \(u\)
   vs. power-freeness of \(B-u\)), including the degenerate
   \(ab\in E\) case. Check consistency against the closed-pair scans
   (`E012`/`E013`) and `C027`'s range.
3. **Transfer test.** Do `L030`/`L033` need the *second* terminal, or
   only a shortest-path band? State precisely what each argument
   anchors on; the answer decides whether R1 has a proof engine or
   only a search specification.
4. **Conditional-form test.** In every case that ends at "\(B\)
   contains a counterexample", check whether the extra hypothesis
   "that counterexample is not cubic" (available under the conditional
   reframing via `A012` T4 branch structure) closes it.
5. Kill condition / pivot: if every surviving case resists both
   minimality and the transfer machinery, record the surviving-profile
   specification as the R1 search target and fall back per the S019
   strategy audit. A found tight 1-atom at any point triggers the
   disproof protocol immediately.

## Deductions

Deductions carry **W1-T** numbers (worker W1 of `S019`); claim IDs are
assigned by the orchestrator, not here. Every deduction is labelled
**proved**, **provisional** or **failed**. Nothing below consumes
`C004`–`C006`; the one place where they would have been usable is
flagged in W1-T16.

### Notation and standing conventions

Throughout, "power-free" means: no cycle of length \(2^k\), \(k\ge2\);
a **counterexample** is a finite simple graph with \(\delta\ge3\) and
power-free cycle spectrum; a **tight 1-atom** (`A018` T2) is a finite
simple connected power-free graph with exactly one vertex of degree
\(<3\), that vertex having degree exactly \(2\). Write

- \(\mathcal T\) for the class of tight 1-atoms, \(\mathcal C\) for the
  class of counterexamples;
- \(\mathbb P=\{2^k:k\ge2\}=\{4,8,16,32,\dots\}\), and
  \(\mathbb P-j=\{2^k-j:k\ge2\}\); so \(\mathbb P-1=\{3,7,15,31,\dots\}\)
  (**Mersenne lengths**) and \(\mathbb P-2=\{2,6,14,30,\dots\}\);
- for a tight 1-atom \(B\): \(u\) its degree-2 vertex,
  \(N_B(u)=\{a,b\}\), \(H=B-u\), and
  \(S=S(H,a,b)\) the set of lengths (in edges) of simple \(a\)–\(b\)
  paths of \(H\) (so \(S=\emptyset\) when \(a,b\) lie in different
  components of \(H\));
- \(P_H(x,y)\) the set of lengths of simple \(x\)–\(y\) paths of \(H\);
- \(\mathrm{Spec}(G)\) the set of cycle lengths of \(G\);
- when \(\mathcal T\ne\emptyset\),
  \(n_0=\min\{|V(B)|:B\in\mathcal T\}\).

**Standing hypothesis (R) — the residual hypothesis.**
\(\mathcal T\ne\emptyset\) *and no counterexample has order \(<n_0\)*.

(R) is the exact negation of the hypothesis of W1-T4 below. The
architecture of this attempt is: W1-T4 shows that failure of (R)
delivers the `G015` deliverable outright; W1-T6 shows that (R) forces a
single local configuration; W1-T9–W1-T15 develop that configuration.

---

### W1-T1 (closure calculus) — proved

**Claim.** Let \(H\) be a finite simple graph and \(a\ne b\in V(H)\).

1. *(2-closure.)* Let \(B_2=H+u\), where \(u\notin V(H)\) is new with
   \(N(u)=\{a,b\}\). Then \(B_2\) is simple, \(|V(B_2)|=|V(H)|+1\),
   \(\deg_{B_2}(u)=2\), \(\deg_{B_2}(a)=\deg_H(a)+1\),
   \(\deg_{B_2}(b)=\deg_H(b)+1\), all other degrees unchanged, and
   \[\mathrm{Spec}(B_2)=\mathrm{Spec}(H)\cup(S+2),\qquad S=S(H,a,b).\]
2. *(1-closure.)* If \(ab\notin E(H)\), let \(B_1=H+ab\). Then \(B_1\) is
   simple, \(|V(B_1)|=|V(H)|\), \(\deg_{B_1}(a)=\deg_H(a)+1\),
   \(\deg_{B_1}(b)=\deg_H(b)+1\), all other degrees unchanged, and
   \[\mathrm{Spec}(B_1)=\mathrm{Spec}(H)\cup(S+1).\]
   More generally, for any \(z\in V(H)\) with \(z\ne a\), \(az\notin
   E(H)\): \(\mathrm{Spec}(H+az)=\mathrm{Spec}(H)\cup(P_H(a,z)+1)\).
3. *(0-closure.)* If \(ab\notin E(H)\) **and** \(N_H(a)\cap
   N_H(b)=\emptyset\), let \(B_0=H/(a{=}b)\) be the graph obtained by
   identifying \(a\) and \(b\). Then \(B_0\) is simple,
   \(|V(B_0)|=|V(H)|-1\), the merged vertex has degree
   \(\deg_H(a)+\deg_H(b)\), all other degrees are unchanged, and
   \[\mathrm{Spec}(B_0)=\Sigma'\cup S\ \subseteq\ \mathrm{Spec}(H)\cup S,\]
   where \(\Sigma'\subseteq\mathrm{Spec}(H)\) is the set of lengths of
   cycles of \(H\) containing **at most one** of \(a,b\).

*Proof.* (1) Simplicity and the degree list are immediate. A cycle of
\(B_2\) avoiding \(u\) is a cycle of \(H\) and conversely. A cycle
through \(u\) uses both edges at \(u\), hence has the form \(u\,a\,P\,b\,u\)
with \(P\) a simple \(a\)–\(b\) path of \(H\); its length is
\(\ell(P)+2\ge3\). Conversely every simple \(a\)–\(b\) path of \(H\)
closes through \(u\) into a cycle of \(B_2\). Hence
\(\mathrm{Spec}(B_2)=\mathrm{Spec}(H)\cup(S+2)\).

(2) A cycle of \(B_1\) not using the edge \(ab\) is a cycle of \(H\). A
cycle using \(ab\) is \(ab\) together with a simple \(a\)–\(b\) path of
\(B_1-ab=H\), of length \(\ell+1\); since \(ab\notin E(H)\) we have
\(1\notin S\), so \(\ell\ge2\) and \(\ell+1\ge3\) as required. The
statement for a general nonadjacent pair \((a,z)\) is the same argument.

(3) Simplicity: a repeated edge at the merged vertex \(x\) would come
from a common neighbour of \(a\) and \(b\); a loop would come from the
edge \(ab\). Both are excluded. Note \(1,2\notin S\) under these
hypotheses. A cycle of \(B_0\) avoiding \(x\) is a cycle of \(H\)
avoiding both \(a\) and \(b\). Let \(C=x,w_1,\dots,w_m,x\) be a cycle of
\(B_0\) through \(x\) (it visits \(x\) once), of length \(m+1\). The two
edges of \(C\) at \(x\) lift to edges \(\alpha w_1\) and \(w_m\beta\) of
\(H\) with \(\alpha,\beta\in\{a,b\}\), and \(w_1,\dots,w_m\notin
\{a,b\}\). If \(\alpha=\beta\) then \(\alpha,w_1,\dots,w_m,\alpha\) is a
cycle of \(H\) of length \(m+1=\ell(C)\) meeting \(\{a,b\}\) exactly
once. If \(\alpha\ne\beta\) then \(\alpha,w_1,\dots,w_m,\beta\) is a
simple \(a\)–\(b\) path of \(H\) of length \(m+1=\ell(C)\), so
\(\ell(C)\in S\); and \(\ell(C)\ge3\) because \(1,2\notin S\). Both
directions are reversible, giving \(\mathrm{Spec}(B_0)=\Sigma'\cup S\).
∎

**Warning (recorded because it is the one asymmetry of the calculus).**
In (3) the identity is **not** \(\mathrm{Spec}(H)\cup S\): a cycle of
\(H\) through *both* \(a\) and \(b\) becomes a closed walk meeting \(x\)
twice and contributes nothing. Only the stated inclusion is available in
that direction, and only the inclusion is used below. This was caught by
`E016` check A1 (the first formulation of (3) as an equality failed at
order 6).

**Corollary W1-T2 (power-free closure criterion) — proved.** With the
notation of W1-T1 and \(\mathrm{Spec}(H)\) power-free:

- \(B_2\) is power-free \(\iff S\cap(\mathbb P-2)=\emptyset\);
- if \(ab\notin E(H)\) and \(S\cap(\mathbb P-1)=\emptyset\), then \(B_1\)
  is power-free; likewise \(H+az\) is power-free whenever
  \(P_H(a,z)\cap(\mathbb P-1)=\emptyset\);
- if \(ab\notin E(H)\), \(N_H(a)\cap N_H(b)=\emptyset\) and
  \(S\cap\mathbb P=\emptyset\), then \(B_0\) is power-free.

*Proof.* Immediate from W1-T1, using \(\mathrm{Spec}(H)\) power-free and
\(\Sigma'\subseteq\mathrm{Spec}(H)\). ∎

---

### W1-T3 (the (3,3) closed-gadget correspondence) — proved

Define
\[\mathcal A=\Bigl\{(B,u)\ :\ B\in\mathcal T,\ u\ \text{its degree-2
vertex},\ N_B(u)=\{a,b\},\ \deg_B(a)=\deg_B(b)=3,\ B-u\ \text{connected}
\Bigr\},\]
\[\mathcal G=\Bigl\{(H,a,b)\ :\ H\ \text{finite simple connected},\
\deg_H(a)=\deg_H(b)=2,\ \deg_H(v)\ge3\ (v\ne a,b),\
\mathrm{Spec}(H)\ \text{power-free},\ S(H,a,b)\cap(\mathbb P-2)=\emptyset
\Bigr\}.\]

**Claim.** \((B,u)\mapsto(B-u,a,b)\) is a bijection \(\mathcal A\to
\mathcal G\) with inverse \((H,a,b)\mapsto(H+u,u)\), and
\(|V(B)|=|V(H)|+1\). Moreover every \((H,a,b)\in\mathcal G\):

1. satisfies condition (D) of `D-A2` (non-terminal degrees \(\ge3\);
   terminal degrees \(2,2\), sum \(4\ge3\)), i.e. is a two-terminal
   **(D)-gadget**, and is in addition a **core** in the sense of both
   terminal degrees being \(\ge2\);
2. is \(C_4\)-free, and \(2\notin S\) — equivalently \(a,b\) have no
   common neighbour in \(H\) and \(d_H(a,b)\ne2\);
3. has \(1\in S\iff ab\in E(H)\iff B\) contains the triangle \(uab\);
4. has order \(\ge16\), so every member of \(\mathcal A\) has order
   \(\ge17\).

*Proof.* Let \((B,u)\in\mathcal A\) and \(H=B-u\). \(H\) is connected by
assumption, power-free as a subgraph of \(B\), \(\deg_H(a)=\deg_H(b)=2\),
and \(\deg_H(v)=\deg_B(v)\ge3\) for \(v\ne a,b\) (such \(v\) is not
adjacent to \(u\)). By W1-T1(1), \(\mathrm{Spec}(B)=\mathrm{Spec}(H)\cup
(S+2)\); power-freeness of \(B\) therefore gives both
\(\mathrm{Spec}(H)\) power-free and \((S+2)\cap\mathbb P=\emptyset\),
i.e. \(S\cap(\mathbb P-2)=\emptyset\). So \((H,a,b)\in\mathcal G\).

Conversely let \((H,a,b)\in\mathcal G\) and \(B=H+u\). \(B\) is simple
and connected; by W1-T1(1) and W1-T2 it is power-free; its degrees are
\(\deg(u)=2\), \(\deg(a)=\deg(b)=3\), all others \(\ge3\). So \(u\) is
the unique vertex of degree \(<3\) and \(B\in\mathcal T\) with
\(B-u=H\) connected and both \(u\)-neighbours cubic:
\((B,u)\in\mathcal A\). The two maps are mutually inverse by
construction.

(1) is the degree list. (2): \(2\in\mathbb P-2\), so \(2\notin S\), which
says exactly that \(a,b\) have no common neighbour; \(C_4\)-freeness of
\(H\) follows from \(4\in\mathbb P\) and \(\mathrm{Spec}(H)\)
power-free. (3) is immediate. (4): \(H\) is connected, \(C_4\)-free, of
minimum degree \(2\), with exactly two sub-cubic vertices, hence lies in
the search class of `C027`; its edge count satisfies
\(2|E|\ge4+3(|V(H)|-2)\), i.e. \(|E|\ge\lceil(3n-2)/2\rceil\), so the
class's edge bound is met. `C027` states that no member of that class of
order \(\le15\) is power-free; \(H\) is power-free, so \(|V(H)|\ge16\).
∎

**Reading.** This is the *exact* form of the mechanism sketched in the
intended-mechanism section: \(B\) is the closure of a two-terminal
gadget by a 2-path, and power-freeness of \(B\) splits into
"\(H\) power-free" **plus** "the through-set avoids \(\mathbb P-2\)".
It is `L034`'s ring shape at \(L=1\) with offset \(2\). Note what the
criterion is *not*: it is not a pinch. \(\mathbb P-2\) is an
exponentially thin set of forbidden lengths, and it imposes **no upper
bound whatever on \(s_{\max}\)**. That single fact governs the transfer
test (W1-T15).

---

### W1-T4 (the reduction engine) — proved

**Claim.** Suppose some counterexample has order \(<n_0\) (in
particular \(\mathcal T\ne\emptyset\) and \(\mathcal C\ne\emptyset\)).
Then a **cubic** counterexample exists.

*Proof.* Let \(G^*\) minimize \(|V|\), then \(|E|\), over \(\mathcal C\),
and put \(m_0=|V(G^*)|\); by hypothesis \(m_0<n_0\). Suppose \(G^*\) is
not cubic and pick \(x\) with \(\deg_{G^*}(x)\ge4\).

*Branch 1: some neighbour \(y\) of \(x\) has \(\deg_{G^*}(y)=3\).*
\(G^*-xy\) is power-free (its spectrum only shrinks), and its degrees
are \(\deg(y)=2\), \(\deg(x)\ge3\), all others unchanged and \(\ge3\).
If \(G^*-xy\) is connected it is a tight 1-atom of order \(m_0<n_0\),
contradicting the minimality of \(n_0\). If not, \(xy\) was a bridge;
let \(K\) be the component of \(y\). \(K\) is connected, power-free,
\(\deg_K(y)=2\), and \(\deg_K(v)=\deg_{G^*}(v)\ge3\) for every other
\(v\in V(K)\) (all \(G^*\)-edges at such \(v\) survive and stay in
\(K\)). So \(K\) is a tight 1-atom of order \(\le m_0<n_0\) — again a
contradiction.

*Branch 2: every neighbour of \(x\) has degree \(\ge4\).* Pick any
\(y\in N(x)\). \(G^*-xy\) has \(\delta\ge3\) and is power-free. If
connected, it is a counterexample of order \(m_0\) with fewer edges,
contradicting size-minimality. If disconnected, each component has
\(\delta\ge3\) and is power-free, i.e. is a counterexample of order
\(<m_0\), contradicting order-minimality.

Both branches are impossible, so \(G^*\) is cubic. ∎

**Remark.** This is `A012` T4 run against \(n_0\) rather than against the
hypothesis "no tight 1-atom exists". The strictness \(m_0<n_0\) is
load-bearing: with \(m_0\le n_0\) Branch 1 produces a tight 1-atom of
order \(\le n_0\), which is not a contradiction. Every construction
below is therefore aimed at a counterexample of order **strictly**
below \(n_0\).

---

### W1-T5 (peeling a small 1-atom) — proved

**Claim.** Assume \(\mathcal T\ne\emptyset\) and let \(L\) be a 1-atom
(`D-A4`: exceptional degree \(1\) **or** \(2\)) with \(|V(L)|<n_0\).
Then some counterexample has order \(<n_0\), hence (W1-T4) a cubic
counterexample exists.

*Proof.* Let \(c\) be the exceptional vertex of \(L\). Since all other
vertices have degree \(\ge3\), \(|V(L)|\ge4\). If \(\deg_L(c)=2\) then
\(L\) is a tight 1-atom of order \(<n_0\), contradicting minimality; so
\(\deg_L(c)=1\). Then \(L-c\) is connected (deleting a leaf), power-free
(subgraph), has order \(|V(L)|-1<n_0\), and its degrees agree with those
of \(L\) except at \(c\)'s unique neighbour \(c'\), where the degree
drops from \(\ge3\) to \(\ge2\). If \(\deg_{L-c}(c')\ge3\) then
\(\delta(L-c)\ge3\), so \(L-c\) is a counterexample of order \(<n_0\).
If \(\deg_{L-c}(c')=2\) then \(L-c\) is a tight 1-atom of order
\(<n_0\), contradicting minimality — so this case does not occur. ∎

**Reading (the repair of the withdrawn `A012` Remark T4.1).** T4.1 tried
the same peel and had to close the branch "\(L-c\) is a counterexample"
by *contradiction*, which is unavailable. Under the conditional
reframing that branch is not an obstacle but the **goal**: a
counterexample of order \(<n_0\) is exactly the input W1-T4 wants. This
is the precise sense in which the conditional target is strictly easier
than the unconditional one, and it is the reason R1 must be run in
conditional form.

---

### W1-T6 (the case analysis at \(u\)) — proved

**Claim.** Let \(B\in\mathcal T\) with \(|V(B)|=n_0\), \(u,a,b,H\) as
above. Then \(H\) has at most two connected components, and exactly one
of the following five cases occurs.

| | case | conclusion |
|---|---|---|
| (1) | \(u\) is a cutvertex and \(\min(\deg_Ba,\deg_Bb)=3\) | **impossible** |
| (2) | \(u\) is a cutvertex and \(\deg_Ba,\deg_Bb\ge4\) | a counterexample of order \(\le n_0-2\) exists; \(n_0\ge39\) |
| (3) | \(u\) is not a cutvertex and \(\{\deg_Ba,\deg_Bb\}=\{3,d\}\), \(d\ge4\) | **impossible** |
| (4) | \(u\) is not a cutvertex and \(\deg_Ba,\deg_Bb\ge4\) | \(H\) is a counterexample of order \(n_0-1\); \(n_0\ge20\) |
| (5) | \(u\) is not a cutvertex and \(\deg_Ba=\deg_Bb=3\) | \((H,a,b)\in\mathcal G\); \(n_0\ge17\) |
| (5a) | case (5) and \((H,a,b)\) is **not** vertex-taut | a counterexample of order \(<n_0\) exists |
| (5b) | case (5) and \((H,a,b)\) **is** vertex-taut | *survives* |

*Proof.* **At most two components.** Let \(v\in V(H)\). A shortest
\(v\)–\(u\) path of \(B\) ends with the edge \(au\) or \(bu\), so its
initial segment is a \(v\)–\(a\) or \(v\)–\(b\) path inside \(H\). Hence
every vertex of \(H\) lies in the component of \(a\) or that of \(b\). If
those coincide \(H\) is connected and \(u\) is not a cutvertex;
otherwise \(H\) has exactly two components \(H_a\ni a\), \(H_b\ni b\) and
\(u\) is a cutvertex. In the latter case there is no edge between
\(V(H_a)\) and \(V(H_b)\), and \(|V(H_a)|,|V(H_b)|\le n_0-2\).

**(1).** Say \(\deg_B(a)=3\). \(H_a\) is connected, power-free (subgraph
of \(B\)), \(\deg_{H_a}(a)=\deg_B(a)-1=2\), and every other
\(v\in V(H_a)\) has \(\deg_{H_a}(v)=\deg_B(v)\ge3\). So \(H_a\) is a
tight 1-atom of order \(\le n_0-2<n_0\): contradiction.

**(2).** As above with \(\deg_{H_a}(a)=\deg_B(a)-1\ge3\): \(H_a\) is
connected, power-free with \(\delta\ge3\), i.e. a counterexample of order
\(\le n_0-2\); so is \(H_b\). By `L022` each has order \(\ge19\), whence
\(n_0=|V(H_a)|+|V(H_b)|+1\ge39\).

**(3).** Say \(\deg_B(a)=3\), \(\deg_B(b)\ge4\). \(H\) is connected,
power-free, \(\deg_H(a)=2\), \(\deg_H(b)\ge3\) and all other degrees
\(\ge3\): a tight 1-atom of order \(n_0-1<n_0\): contradiction.

**(4).** \(H\) is connected, power-free with \(\delta\ge3\): a
counterexample of order \(n_0-1\), so \(n_0-1\ge19\) by `L022`.

**(5).** W1-T3 gives \((H,a,b)\in\mathcal G\) and \(|V(H)|\ge16\).

**(5a).** \((H,a,b)\) is a connected (D)-gadget (W1-T3(1)), so by `L027`
it is vertex-taut or contains a lobe \(L\) at some vertex \(c\), with
\(|V(L)|\ge2\), \(V(L)\cap\mathrm{Ess}=\{c\}\), \(\deg_L(v)\ge3\) for all
\(v\in V(L)\setminus\{c\}\) and \(\deg_L(c)\ge1\). \(L\) is connected and
power-free (subgraph of \(H\)). Since \(a,b\in\mathrm{Ess}\) and
\(V(L)\cap\mathrm{Ess}=\{c\}\), at most one of \(a,b\) lies in \(V(L)\),
so \(|V(L)|\le|V(H)|-1=n_0-2<n_0\).
If \(\deg_L(c)\ge3\) then \(\delta(L)\ge3\) and \(L\) is a
counterexample of order \(<n_0\). If \(\deg_L(c)\in\{1,2\}\) then \(L\)
is a 1-atom of order \(<n_0\) and W1-T5 supplies a counterexample of
order \(<n_0\). ∎

**Corollary W1-T7 (the conditional cubic reduction, modulo one case) —
proved.** Assume (R). Then every minimum-order tight 1-atom falls in case
(5b). Equivalently: *if the configuration of case (5b) can be excluded,
then "a tight 1-atom exists \(\Rightarrow\) a cubic counterexample
exists", and hence — with `L029`/`L036` — statement 0.1 holds **iff** no
cubic counterexample exists, which is precisely the `G015`
deliverable.*

*Proof.* Under (R) no counterexample of order \(<n_0\) exists, so cases
(2), (4) and (5a) are impossible; cases (1) and (3) are impossible
outright by W1-T6. Only (5b) remains. For the second sentence: suppose
case (5b) is excluded and a tight 1-atom exists. Then (R) must fail (else
W1-T6 forces (5b)), so a counterexample of order \(<n_0\) exists and
W1-T4 gives a cubic counterexample. Then by `L029` (cubic reduction
modulo tight 1-atoms, in the corrected `A018` T2 form), "no cubic
counterexample" implies "no tight 1-atom", so statement 0.1 is equivalent
to the nonexistence of a cubic counterexample. ∎

**Corollary W1-T8 (order bound) — proved.** Every tight 1-atom has order
\(\ge17\). (Unconditional; supersedes the \(\ge16\) reading of `C027` for
this object.)

*Proof.* Apply W1-T6 to a minimum-order \(B\). Cases (1),(3) are
impossible; cases (2),(4),(5) give \(n_0\ge39\), \(n_0\ge20\),
\(n_0\ge17\) respectively. So \(n_0\ge17\), and by minimality every
tight 1-atom has order \(\ge17\). ∎

*Computational input:* `C027` (orders \(\le15\), at its recorded
strength, with its geng caveats) and `L022`. The new content is the
minimality step that kills cases (1) and (3).

---

### The residual object

For the rest of this attempt assume **(R)**, so that by W1-T7 we are in
case (5b): \(B\) is a minimum-order tight 1-atom, \(H=B-u\) is
connected, \(\deg_B(a)=\deg_B(b)=3\), \((H,a,b)\in\mathcal G\) is
vertex-taut, and \(n_0\ge17\). Call \((B,u,a,b,H)\) the **residual
object**.

Note the reformulation of tautness that will be used repeatedly:
\((H,a,b)\) is vertex-taut **iff every vertex of \(B\) lies on a cycle of
\(B\) through \(u\)** (a simple \(a\)–\(b\) path of \(H\) plus \(u\) is
such a cycle, and conversely).

### W1-T9 (the residual object is 2-connected) — proved

**Claim.** In the residual object, \(B\) is 2-connected.

*Proof.* \(B\) is connected with \(n_0\ge17\ge3\) vertices. Suppose
\(c\in V(B)\) is a cutvertex. Since \(u\) is not a cutvertex (case (5)),
\(c\ne u\); so \(c\in V(H)\). Let \(K\) be the component of \(B-c\)
containing \(u\) and pick \(v\) in another component; then \(v\ne u,c\),
so \(v\in V(H)\). By tautness \(v\) lies on a simple \(a\)–\(b\) path of
\(H\), which together with \(ua,ub\) is a cycle \(C\) of \(B\) through
both \(u\) and \(v\). If \(c\notin V(C)\) then \(C\) is intact in
\(B-c\), so \(u\) and \(v\) lie in one component — contradiction. If
\(c\in V(C)\) then \(C-c\) is a path containing both \(u\) and \(v\)
(as \(u,v\ne c\)), again a contradiction. ∎

### W1-T9.1 (edge criticality: the degree-\(\ge4\) vertices are independent) — proved

Refine the choice of \(B\): among tight 1-atoms of order \(n_0\), take one
of minimum **size**. Every statement above still applies (a
minimum-order-then-size tight 1-atom is in particular minimum-order), so
under (R) this \(B\) is still residual and 2-connected.

**Claim.** Every edge of \(B\) has an endpoint of degree \(\le3\);
equivalently, the vertices of degree \(\ge4\) in \(B\) form an
independent set. In particular the same holds in \(H=B-u\) for every
edge not incident to \(a\) or \(b\).

*Proof.* Suppose \(wy\in E(B)\) with \(\deg_B(w),\deg_B(y)\ge4\). Since
\(B\) is 2-connected (W1-T9) it is bridgeless, so \(B-wy\) is connected;
it is power-free as a subgraph of \(B\); and its degrees are \(\ge3\) at
\(w\) and \(y\) and unchanged elsewhere, so \(u\) is still the unique
vertex of degree \(<3\) and still has degree 2. Hence \(B-wy\) is a tight
1-atom of order \(n_0\) with smaller size — contradicting the refined
minimality. ∎

**Reading.** This is `L002`'s conclusion ("in an edge-minimal
counterexample the degree-\(\ge4\) vertices are independent") transported
to the tight 1-atom, and it is available only because W1-T9 supplied
2-connectivity: without bridgelessness, deleting \(wy\) could disconnect
\(B\) and the reduct need not be a 1-atom. It is free structure — no
computation, no import — and it is the natural partner of `C006` for
anyone who later chooses to consume that unverified density bound.

### W1-T10 (forced arithmetic of the through-set) — proved

**Claim.** Let \((B,u,a,b,H)\) be residual and \(S=S(H,a,b)\). Then

1. \(S\cap(\mathbb P-2)=\emptyset\) — i.e. \(2,6,14,30,\dots\notin S\);
2. if \(ab\notin E(H)\) then \(S\cap\mathbb P\ne\emptyset\) and
   \(S\cap(\mathbb P-1)\ne\emptyset\): \(S\) contains a power of two
   **and** a Mersenne number \(2^k-1\);
3. \(d_H(a,b)=\min S\notin\{2,6,14,30,\dots\}\), and if \(d_H(a,b)\ge3\)
   then \(\max S\ge7\).

*Proof.* (1) is W1-T3. (2): if \(S\cap\mathbb P=\emptyset\), then by
W1-T3(2) \(a,b\) have no common neighbour and by hypothesis \(ab\notin
E(H)\), so W1-T1(3)/W1-T2 apply: \(B_0=H/(a{=}b)\) is simple, connected,
power-free, of order \(n_0-2\), and its degrees are \(\deg_H(a)+
\deg_H(b)=4\) at the merged vertex and \(\ge3\) elsewhere. So \(B_0\) is
a counterexample of order \(<n_0\), contradicting (R). If
\(S\cap(\mathbb P-1)=\emptyset\), then \(B_1=H+ab\) is simple, connected,
power-free (W1-T2), of order \(n_0-1\), with \(\deg(a)=\deg(b)=3\) and
all other degrees \(\ge3\): again a counterexample of order \(<n_0\),
contradicting (R).
(3) \(\min S=d_H(a,b)\) because a shortest \(a\)–\(b\) path is simple.
If \(d_H(a,b)\ge3\) then \((H,a,b)\) is a vertex-taut \(C_4\)-free
(D)-gadget with \(d(a,b)\ge3\), so `L030` forces a simple \(a\)–\(b\)
path of length \(\ge6\); since \(6\notin S\) by (1), \(\max S\ge7\). ∎

### W1-T11 (the degenerate case \(ab\in E\)) — proved

**Claim.** Let \((B,u,a,b,H)\) be residual with \(ab\in E(H)\) (so
\(uab\) is a triangle of \(B\)). Write \(N_H(a)=\{b,p\}\),
\(N_H(b)=\{a,r\}\). Then \(p\ne r\), \(pr\notin E(H)\),
\(p,r\notin\{a,b\}\), \(\deg_{H-a-b}(p),\deg_{H-a-b}(r)\ge2\), and the
set \(\Lambda\) of lengths of simple \(p\)–\(r\) paths of \(H-a-b\)
satisfies
\[\Lambda\cap(\mathbb P-4)=\emptyset,\qquad
  \Lambda\cap(\mathbb P-3)=\emptyset,\qquad
  \Lambda\cap(\mathbb P-1)\ne\emptyset.\]

*Proof.* \(p=r\) would make \(a\,p\,b\,u\) a 4-cycle; \(pr\in E\) would
make \(a\,p\,r\,b\) a 4-cycle (all four vertices distinct). \(p\ne b\)
and \(r\ne a\) by construction, and \(p\not\sim b\), \(r\not\sim a\) (the
neighbourhoods are listed), so \(p,r\) keep degree \(\ge3-1=2\) in
\(H-a-b\).
Every simple \(a\)–\(b\) path of \(H\) is the edge \(ab\) or has the form
\(a\,p\cdots r\,b\), so \(S=\{1\}\cup(\Lambda+2)\). Every cycle of \(H\)
through \(a\) uses both edges \(ab,ap\) and hence also \(b\)'s second
edge \(br\), giving cycle lengths \(\Lambda+3\); likewise for \(b\); so
\(\mathrm{Spec}(H)=\mathrm{Spec}(H-a-b)\cup(\Lambda+3)\).
Power-freeness of \(B\) gives \((S+2)\cap\mathbb P=\emptyset\), i.e.
\((\Lambda+4)\cap\mathbb P=\emptyset\), i.e.
\(\Lambda\cap(\mathbb P-4)=\emptyset\), and power-freeness of \(H\) gives
\(\Lambda\cap(\mathbb P-3)=\emptyset\).
For the last clause, let \(G=(H-a-b)+pr\) — the *suppression* of the
degree-2 path \(p\,a\,b\,r\). \(G\) is simple (as \(pr\notin E\)),
connected, of order \(n_0-3\); \(\deg_G(p)=\deg_H(p)\ge3\),
\(\deg_G(r)=\deg_H(r)\ge3\), and all other degrees are unchanged and
\(\ge3\); so \(\delta(G)\ge3\). Its cycles are the cycles of
\(H-a-b\) together with, for each simple \(p\)–\(r\) path of \(H-a-b\) of
length \(\ell\), a cycle of length \(\ell+1\); hence
\(\mathrm{Spec}(G)=\mathrm{Spec}(H-a-b)\cup(\Lambda+1)\subseteq
\mathrm{Spec}(H)\cup(\Lambda+1)\). If \(\Lambda\cap(\mathbb
P-1)=\emptyset\) then \(G\) is power-free, hence a counterexample of
order \(<n_0\), contradicting (R). ∎

**Remark W1-T11.1 — proved.** In this sub-case \((H-a-b,p,r)\) is itself
a vertex-taut \(C_4\)-free (D)-core: tautness of \((H,a,b)\) says every
vertex other than \(a,b\) lies on a path \(a\,p\cdots r\,b\), i.e. on a
simple \(p\)–\(r\) path of \(H-a-b\); the degrees are \(\ge2\) at
\(p,r\) and \(\ge3\) elsewhere. Consequently `L028`(ii) and `L030` apply
to it: since \(\Lambda\) avoids \(4\) and \(5\) (W1-T11), it is not
contained in \(\{2,3\}\) and not contained in \(\{3,4,5\}\), so in every
case \(\max\Lambda\ge6\). This is the *only* place in the residual
analysis where the taut ladder acts on a fresh object, and it still
yields only the boundary fact — see W1-T15(a).

### W1-T12 (Mersenne saturation at the terminals) — proved

**Claim.** Let \((B,u,a,b,H)\) be residual. Then for **every**
\(z\in V(H)\) with \(z\ne a\) and \(az\notin E(H)\), the graph \(H\)
contains a simple \(a\)–\(z\) path of length \(2^k-1\) for some
\(k\ge2\); i.e. \(P_H(a,z)\cap(\mathbb P-1)\ne\emptyset\). The same holds
at \(b\). The number of such \(z\) at \(a\) is \(|V(H)|-3=n_0-4\ge13\).

*Proof.* Fix such a \(z\) and put \(G=H+az\); \(G\) is simple,
connected, of order \(n_0-1<n_0\), and by W1-T1(2)
\(\mathrm{Spec}(G)=\mathrm{Spec}(H)\cup(P_H(a,z)+1)\), where
\(\mathrm{Spec}(H)\) is power-free.

*Case \(z=b\).* Then \(\deg_G(a)=\deg_G(b)=3\) and all other degrees are
\(\ge3\), so \(\delta(G)\ge3\). If \(G\) were power-free it would be a
counterexample of order \(<n_0\), contradicting (R). Hence
\((P_H(a,b)+1)\cap\mathbb P\ne\emptyset\).

*Case \(z\ne b\).* Then \(z\ne a,b\), so \(\deg_H(z)\ge3\) and
\(\deg_G(z)\ge4\); also \(\deg_G(a)=3\). Thus \(b\) is the unique vertex
of \(G\) of degree \(<3\), and it has degree \(2\). If \(G\) were
power-free it would be a tight 1-atom of order \(n_0-1<n_0\),
contradicting the minimality of \(n_0\). Hence
\((P_H(a,z)+1)\cap\mathbb P\ne\emptyset\).

In both cases \(P_H(a,z)\cap(\mathbb P-1)\ne\emptyset\). The count is
\(|V(H)|-1-\deg_H(a)=|V(H)|-3\), and \(|V(H)|=n_0-1\ge16\). ∎

**Reading.** This is a *saturation* condition of exactly the type
`L008`/`L011` produce for edge-maximal counterexamples, but obtained here
from order-minimality of the tight 1-atom rather than from
edge-maximality, and localized at a degree-2 vertex. At order \(17\)–\(18\)
the only available Mersenne lengths are \(3,7,15\), and every one of the
\(\ge13\) non-neighbours of \(a\) must be reachable from \(a\) by a
simple path of exactly one of those three lengths.

**Calibration — the lever is weak in isolation (`E016` A6).** With
power-freeness dropped, saturation at *both* degree-2 vertices holds for
\(1/1\), \(2/2\), \(22/22\), \(123/125\), \(1{,}133/1{,}139\) and
\(10{,}966/10{,}966\) members of the connected \(C_4\)-free
two-degree-2-vertex class at orders \(8,9,10,11,12,13\). So the
saturation condition alone carries essentially no information about this
class: \(P_H(a,z)\) is typically a long interval and hits
\(\{3,7,15,\dots\}\) automatically. W1-T12 can only contribute in
combination with a hypothesis that *confines* \(P_H(a,z)\) — the same
confinement deficit identified in W1-T15. Its one free consequence that
does not need confinement is the parity consequence W1-T13, because
parity is a congruence obstruction rather than a confinement one.

### W1-T13 (the residual object is non-bipartite) — proved

**Claim.** In the residual object, \(H\) and \(B\) are non-bipartite.

*Proof.* Suppose \(H\) is bipartite with parts \(V_0\ni a\) and \(V_1\).
Then every simple \(a\)–\(z\) path has length \(\equiv0\pmod2\) if
\(z\in V_0\) and \(\equiv1\pmod2\) if \(z\in V_1\). Pick \(p\in N_H(a)\)
(\(\subseteq V_1\)); since \(p\ne a,b\) or \(p=b\), in either case
\(\deg_H(p)\ge2\), so \(p\) has a neighbour \(z\ne a\), and \(z\in V_0\).
Then \(az\notin E(H)\) (both in \(V_0\)) and \(z\ne a\), while
\(P_H(a,z)\) consists of even numbers only, so it misses
\(\mathbb P-1\subseteq2\mathbb Z+1\) — contradicting W1-T12. Hence \(H\)
is non-bipartite, and so is \(B\supseteq H\). ∎

**Reading.** `C034` excludes bipartite tight 1-atoms computationally
through order \(22\). W1-T13 gives, at every order, a *hand proof* of
non-bipartiteness for the residual object — conditional on (R), but with
no order restriction and no computational input.

### W1-T14 (block-chain constraints) — proved

**Claim.** Let \((B,u,a,b,H)\) be residual and suppose \(c\) is a cut
vertex of \(H\); by `L032`/`L035` T0 (\(H\) is vertex-taut with
non-terminal degrees \(\ge3\)) \(c\) separates \(a\) from \(b\), and we
may write \(H=H_1\cup H_2\) with \(V(H_1)\cap V(H_2)=\{c\}\),
\(a\in V(H_1)\), \(b\in V(H_2)\), \(E(H_1)\cup E(H_2)=E(H)\). Put
\(S_1=S(H_1,a,c)\). Then

1. if \(\deg_{H_1}(c)\ge2\): \(S_1\cap(\mathbb P-2)\ne\emptyset\);
2. if \(\deg_{H_1}(c)=1\), with \(c'\) the unique \(H_1\)-neighbour of
   \(c\) and \(c'\ne a\): \(S_1\cap(\mathbb P-1)\ne\emptyset\).

The mirror statements hold for \(H_2\) with terminals \(c,b\).

*Proof.* First, **neither terminal is a cut vertex of \(H\)**: if \(a\)
were one, then since \(\deg_H(a)=2\), \(H-a\) has exactly two
components, and a vertex \(v\) in the one not containing \(b\) lies on no
simple \(a\)–\(b\) path (such a path would have to leave that component,
which is possible only through \(a\), already used) — contradicting
tautness. Symmetrically for \(b\). Hence \(c\notin\{a,b\}\), so
\(a\in V(H_1)\setminus\{c\}\) and \(b\in V(H_2)\setminus\{c\}\), and
every \(H\)-edge at a vertex of \(V(H_1)\setminus\{c\}\) lies in
\(H_1\). Second, \(|V(H_1)|\le n_0-2\), because
\(|V(H_1)|+|V(H_2)|=|V(H)|+1=n_0\) and \(|V(H_2)|\ge2\).

(1) Let \(G=H_1+u_1\) with \(u_1\) new and \(N(u_1)=\{a,c\}\); \(G\) is
simple and connected of order \(|V(H_1)|+1\le n_0-1<n_0\). Degrees:
\(\deg_G(u_1)=2\); \(\deg_G(a)=\deg_{H_1}(a)+1=\deg_H(a)+1=3\);
\(\deg_G(c)=\deg_{H_1}(c)+1\ge3\); and for \(v\in V(H_1)\setminus
\{a,c\}\), \(\deg_G(v)=\deg_{H_1}(v)=\deg_H(v)\ge3\) (such \(v\) is
neither terminal). So \(u_1\) is the unique sub-cubic vertex of \(G\), of
degree 2. \(\mathrm{Spec}(H_1)\subseteq\mathrm{Spec}(H)\) is power-free,
so by W1-T1(1)/W1-T2, \(G\) is power-free iff
\(S_1\cap(\mathbb P-2)=\emptyset\). Power-freeness would make \(G\) a
tight 1-atom of order \(<n_0\), contradicting minimality; hence
\(S_1\cap(\mathbb P-2)\ne\emptyset\).

(2) Now \(cc'\) is a bridge of \(H\). Let \(G=(H_1-c)+u_1\) with
\(N(u_1)=\{a,c'\}\); this needs \(a\ne c'\), which is the stated side
condition. \(H_1-c\) is connected, of order \(|V(H_1)|-1\), so
\(|V(G)|=|V(H_1)|\le n_0-2<n_0\). Degrees: \(\deg_G(u_1)=2\),
\(\deg_G(a)=3\), \(\deg_G(c')=\deg_{H_1}(c')-1+1=\deg_H(c')\ge3\), and
all others \(\ge3\) as in (1). So \(G\) is tight-1-atom-shaped.
Every simple \(a\)–\(c\) path of \(H_1\) ends with the edge \(c'c\), so
\(S(H_1-c,a,c')=S_1-1\), and \(\mathrm{Spec}(H_1-c)\subseteq
\mathrm{Spec}(H)\) is power-free. By W1-T1(1), \(G\) is power-free iff
\((S_1-1)\cap(\mathbb P-2)=\emptyset\), i.e. iff
\(S_1\cap(\mathbb P-1)=\emptyset\). Minimality forbids power-freeness,
so \(S_1\cap(\mathbb P-1)\ne\emptyset\). ∎

**Reading.** Each block of the residual object's chain must itself carry
a forbidden length in its own local through-set. Since \(S=S_1+S_2\)
(Minkowski, `L032`) and \(S\) avoids \(\mathbb P-2\) globally, the
forbidden lengths must **cancel** across the chain. That is a genuine
tension, and the natural next lever after the endgame described in the
exit state.

---

### W1-T15 (transfer test: what `L030` and `L033` anchor on) — proved analysis

**(a) `L030` (`A013` T8, the middle-layer collapse) does not transfer.**

Anchor inventory (`A013` Remark T8.1, re-derived here): the proof
consumes (i) \(C_4\)-freeness; (ii) non-terminal degrees \(\ge3\);
(iii) terminal degrees \(\ge1\); (iv) vertex-tautness; and (v)
\(S\subseteq\{3,4,5\}\), *read as* "\(d(a,b)\ge3\) **and no simple
\(a\)–\(b\) path has length \(\ge6\)**". Hypothesis (v) is the engine:
every contradiction in T2–T8 is exhibited either as a 4-cycle or as a
simple \(a\)–\(b\) path of length 6 or 7.

The residual object supplies (i)–(iv) — by W1-T3 it is a vertex-taut
\(C_4\)-free (D)-gadget — and **fails (v) completely**: power-freeness of
\(B\) forbids only \(S\cap(\mathbb P-2)=\emptyset\), an exponentially
thin set, and imposes *no* upper bound on \(s_{\max}\). Consequences,
step by step:

- `A013` **T2** (middle coverage) is the step that dies first and
  fatally. It uses \(\ell\le5\) to place every middle vertex at distance
  1 from \(N(a)\) or \(N(b)\). Tautness of the residual object puts each
  vertex on *some* \(a\)–\(b\) path, of unbounded length; there is no
  layer structure, no \(M_2/M_3\) decomposition, and hence no T3–T8.
  The cascade never starts.
- The *exhibits* transfer only in part. A simple \(a\)–\(b\) path of
  length \(6\) **is** a contradiction in the residual object
  (\(6=2^3-2\), so it closes through \(u\) into a \(C_8\) of \(B\)); so
  are lengths \(2,14,30,\dots\). A path of length \(7\) is **not**
  (\(7+2=9\)). The length-7 exhibits occur at four places: T4 Step 2
  (second bullet, \(v\in P\)); T7 Case 1 (first bullet, "another
  middle"); T7 Case 2 (first bullet, "another middle"); T8 Case B (the
  endgame path \(a\,x_1\,z_s\,z_t\,x_j\,x_{j'}\,z_f\,b\)). Even granting
  a hypothetical replacement for T2, the cascade would break at those
  four points.

**Verdict: R1 gains no proof engine from `L030`.** What it gains is one
boundary fact, already recorded as W1-T10(3): if \(d_H(a,b)\ge3\) then
`L030` forces \(s_{\max}\ge6\), hence \(\ge7\).

**(b) `L033` (`A015` T0–T3, the band-4 pencil dichotomy) transfers, but
only at band 4.**

Anchor inventory: T0/T1/T1′ use **nothing** but \(d(x,y)=4\) — no
terminal degrees, no tautness, no bound on \(s_{\max}\), not even
\(C_4\)-freeness. T2/T3 add \(C_4\)-freeness and nothing else. So these
lemmas anchor on the **shortest-path band**, not on a two-terminal
gadget structure and not on interval confinement. They therefore apply
verbatim to \((H,a,b)\) whenever \(d_H(a,b)=4\):

> **W1-T15.1 — proved.** If the residual object has \(d_H(a,b)=4\), then
> \(H\) has no two internally disjoint 4-paths (their union would be a
> \(C_8\) of \(H\), forbidden), so by `L033` T1 all 4-paths of \(H\)
> form a pencil; by `L033` T2 the pencil vertex \(c\) is unique and
> adjacent to a terminal, the fan is rigid (middles biject with strands,
> one exit per middle, no cross chords, every strand pair spanning a
> hexagon), and by `L033` T3 every \(N(a)\)-vertex other than the
> pencil-side one is at distance \(\ge4\) from \(b\). Since
> \(\deg_H(a)=\deg_H(b)=2\), the pencil vertex lies in the four-element
> set \(N_H(a)\cup N_H(b)\) and the fan has at most two strands.

*Proof.* The first sentence is `L033` T1′ plus power-freeness of \(H\).
The rest is `L033` T2/T3 applied to \((H,a,b)\); the last sentence
follows because a fan at \(c\in N(x)\) has its strands' layer-1 vertex
equal to \(c\), and by `L033` T2(3) each middle has \(A(m)=\{c\}\), so
the number of strands is at most \(|N(y)|=2\) via the distinct exits. ∎

More generally, two internally disjoint shortest \(a\)–\(b\) paths give a
cycle of length \(2d\), which \(H\) forbids exactly when
\(d\in\{4,8,16,\dots\}\) (\(d=2\) is already excluded). But `L033` T1's
conversion of "pairwise intersecting" into "pencilled" is
band-4-specific — its proof uses that the internal layers are exactly
\(1,2,3\) and that coincidences are confined to a layer — so no analogue
is available at \(d=8\).

**Verdict: a genuine but narrow transfer.** The residual object's
admissible bands are \(d\in\{1,3,4,5,7,8,9,\dots\}\) (all
\(d\notin\mathbb P-2\)); `L033` bites at exactly one of them.

**(c) One-line summary of the anchor analysis.** `L030` anchors on
*interval confinement of the through-set* (a pinch) and on two terminals
with all traffic short; `L033` anchors on the *shortest-path band* and on
\(C_8\)-freeness, and needs neither terminal degrees nor tautness nor a
pinch. The residual object supplies a band but no pinch. So the
machinery that transfers to R1 is the band machinery, not the collapse
machinery — R1 is not a rung of the taut ladder and cannot be run as
one.

---

### W1-T16 (what `C004`–`C006` would and would not add) — recorded

No deduction above uses `C004`–`C006` (unverified Carr imports); every
proof is self-contained modulo `L022`, `C027`, `L027`, `L029`–`L033`,
`L036` at their recorded strengths. The one place they would apply is
W1-T4: `C005` (every vertex of an order-then-size minimal counterexample
has a neighbour of degree exactly 3) would let Branch 2 be skipped
entirely, and `C006` (density \(\ge4/7\)) would do the same. This is a
*simplification*, not a strengthening — W1-T4 is proved without them —
so R1 has no dependence on the sibling audit's outcome. Recorded so that
no later reader imports them into this attempt by reflex.

---

### Computational verification (`E016`)

`E016` (`verify.py`, CPython 3.14.2, nauty 2.9.3 `geng`) is exact,
exhaustive and deterministic. Checks:

- **A5** fixed anchors: \(K_4\), \(K_{3,3}-e\) (spectrum \(\{4,6\}\),
  \(S=\{3,5\}\)), Petersen (spectrum \(\{5,6,8,9\}\)), Petersen\(-e\)
  (\(S=\{4,5,7,8\}\)), and the 2-closure of Petersen\(-e\) (spectrum
  \(\{5,6,7,8,9,10\}\), not power-free, as W1-T3 predicts from
  \(6\in S+2\)).
- **A1** the closure calculus W1-T1 on every connected graph of orders
  4–8 and every vertex pair: the \(j=2\) and \(j=1\) identities and the
  \(j=0\) exact form \(\Sigma'\cup S\) plus the inclusion into
  \(\mathrm{Spec}(H)\cup S\). *This check falsified the first draft of
  W1-T1(3)* (stated as an equality with \(\mathrm{Spec}(H)\cup S\)) at
  order 6, which is why the warning after W1-T1 exists.
- **A2** the W1-T6 case dichotomy: all 67,432 tight-1-atom-shaped graphs
  (power-freeness dropped) of orders 5–9 are classified into exactly one
  of the five cases — 0 / 1 / 14,257 / 51,578 / 1,596 in cases
  (1)/(2)/(3)/(4)/(5) — and the predicted reduct has the predicted degree
  profile and order bound in every instance; \(B-u\) never had more than
  two components.
- **A3** the W1-T12 construction on the 1,596 (3,3)/non-cut reducts and
  all 7,841 lifts \(H+az\): each is tight-1-atom-shaped of order
  \(|B|-1\) (or, in the boundary case \(z=b\), of minimum degree \(\ge3\)
  — the case split of W1-T12's proof), with spectrum
  \(\mathrm{Spec}(H)\cup(P_H(a,z)+1)\).
- **A4** `C027` stream anchor at orders 6–11: the geng stream counts
  \(4,5,36,84,918,4058\) reproduce exactly from an independent
  implementation, and no member of the \(\le2\)-sub-cubic class at those
  orders is power-free.
- **A6** kill test for the W1-T12 lever: in the connected \(C_4\)-free
  class with exactly two degree-2 vertices and all others \(\ge3\),
  Mersenne saturation at both of them holds for \(1/1\), \(2/2\),
  \(22/22\), \(123/125\), \(1{,}133/1{,}139\), \(10{,}966/10{,}966\)
  members at orders \(8\)–\(13\) (power-freeness dropped; no member of
  that class is power-free at those orders, an independent
  re-derivation of `C027`'s verdict on this one profile). **The kill
  test fires**: see the Failure analysis.

See `E016/README.md` for the outputs and the recorded tool versions.

## Failure analysis

Not abandoned; one target was reached and one was not, and the boundary
between them is sharp.

**Reached.** The conditional form of R1 — "a tight 1-atom yields a cubic
counterexample", which is all `G015` needs — is reduced by W1-T6/W1-T7
from an open question about an unbounded class to a *single* local
configuration, case (5b). Four of the five cases at \(u\) close, two of
them (cases (1) and (3)) outright by minimality, which is exactly the
lever `A012` Remark T4.1 could not find at the degree-1 object.

**Not reached.** Case (5b) itself. The concrete obstruction, stated
precisely:

> The closure criterion of W1-T3 forbids the through-set \(S\) only from
> meeting \(\{2,6,14,30,\dots\}\). Every reduction lemma the dossier owns
> for two-terminal objects (`L028`, `L030`, `L032`'s excess arithmetic,
> `A014`'s rungs, `A015`'s endgame) consumes an **upper bound on
> \(s_{\max}\)** — a pinch, an excess, or a band with \(s_{\max}\le2d\).
> The residual object has none, and cannot be given one: `L034` already
> records that the pinch is only one of several ring channels, and the
> \(L=1\) closure channel is the one with no window at all.

So the failure is not a broken step; it is a *category* mismatch. R1's
object is a congruence-type channel (avoid a thin set of lengths), while
the dossier's proof machinery is confinement-type (bound a window). The
tools built here in response — the closure calculus (W1-T1), the
peeling lemma (W1-T5), the saturation lemma (W1-T12) — are the beginnings
of congruence-type machinery, and W1-T12 is the first of them that
constrains an unbounded object.

**Kill condition status.** The kill condition recorded in the plan
("if every surviving case resists both minimality and the transfer
machinery, record the surviving-profile specification as the R1 search
target") **fired for the transfer machinery** (W1-T15) but **not for
minimality**: minimality killed cases (1) and (3) outright and reduced
(2), (4), (5a) to the conditional goal. Minimality is therefore retained
as the primary lever, and the surviving-profile specification is recorded
below as a search target in parallel rather than as a replacement.

**A second kill condition, opened and fired inside this attempt.** The
saturation lemma W1-T12 was the strongest hand lever produced here, so it
was given its own pre-registered kill test before being proposed as the
next action: *if Mersenne saturation is generically satisfied in the
ambient class with power-freeness dropped, the lever is weak.* `E016`
check A6 ran that test and it fired decisively — saturation at both
terminals holds for 100% of the class at order 13 and \(\ge99.5\%\) at
orders 11–12. W1-T12 therefore stays as recorded structure but is
**demoted** from primary proof lever; the exit state below reflects the
demotion rather than the pre-test plan. Its parity corollary W1-T13 is
unaffected and is the part worth carrying forward.

## Salvageable results

Everything in W1-T1–W1-T16 stands, including the sub-numbered W1-T9.1
(edge criticality), W1-T11.1 (the suppressed core in the triangle case)
and W1-T15.1 (the band-4 pencil transfer). In order of expected reuse:

1. **W1-T6/W1-T7 (the case analysis and the conditional reduction).** The
   `G015` deliverable now has a single named obstruction. Any future
   session that closes case (5b) closes the cubic reduction.
2. **W1-T4/W1-T5 (the engine and the peel).** These make "a
   counterexample of order \(<n_0\)" an *acceptable outcome* rather than a
   dead end, which is the structural repair of the withdrawn `A012`
   Remark T4.1. They apply to any future 1-atom-flavoured reduction.
3. **W1-T1 (the closure calculus).** A reusable exact tool: the three
   closures \(j=0,1,2\) with their spectra, degree lists and orders, and
   the recorded asymmetry at \(j=0\). It is the \(L=1\) instance of
   `L034`'s ring criterion made explicit.
4. **W1-T13 (non-bipartiteness of the residual object).** A hand proof,
   at every order, of what `C034` established computationally through
   order 22 for the bipartite channel — obtained as the *parity*
   corollary of W1-T12. It is the one part of the saturation lemma that
   survived its own kill test, and it is the model for the congruence
   route proposed in the exit state.
5. **W1-T9 (2-connectivity) and W1-T9.1 (degree-\(\ge4\) independence).**
   Free structure on the residual object; W1-T9.1 is `L002`'s
   independence conclusion transported to the tight 1-atom and needs
   W1-T9 to be legal.
6. **W1-T8 (\(n_0\ge17\)), W1-T10/W1-T11/W1-T14 (arithmetic and chain
   constraints), W1-T12 (saturation, demoted).** The residual-object
   profile, ready to be used either as a hand-proof target or as a search
   filter.
7. **W1-T15 (the transfer verdict) and the A6 calibration.** Two negative
   results worth keeping: the taut-ladder machinery is confinement-type
   and does not reach the \(L=1\) closure channel; and Mersenne
   saturation is generically satisfied in the ambient class, so it cannot
   carry a proof alone. Do not spend another session on either.

**Warnings.**

- Do not read W1-T6 as progress on the *unconditional* question "no tight
  1-atom exists". Cases (2), (4) and (5a) end at "a counterexample of
  order \(<n_0\) exists", which is a success only for the conditional
  target. The unconditional question is not touched, and cannot be
  touched by this method: its reducts are counterexamples, not tight
  1-atoms.
- W1-T8's \(\ge17\) inherits `C027`'s geng caveats and `L022`'s
  computational lineage verbatim.
- The (5b) residual profile is a *conditional* specification (it assumes
  (R)). A search that finds an object matching it has found a tight
  1-atom and hence disproves statement 0.1; a search that finds the
  profile empty at some order proves nothing beyond that order.

## Exit state

- Status: active (case (5b) open)
- Promoted records: W1-T1–W1-T16 offered for the ledger (the orchestrator
  assigns IDs); experiment `E016`.
- Next action (recommended for R1), in falsifiable form, after the A6
  kill test:

  1. **Primary (search, decisive at one order).** The first live order for
     case (5b) is **16**, and the object is exactly the class
     \(\mathcal G\) of W1-T3 at order 16: connected, \(C_4\)-free,
     exactly two degree-2 vertices, all others \(\ge3\), power-free, with
     \(S\cap\{2,6,14\}=\emptyset\). `C027` stops at 15 and `C035` is
     pair-level only, so the stream-level question at 16 is open. Run a
     dedicated \(C_8\)/\(C_{16}\) filter over that profile — much cheaper
     than `E013`'s closed-pair scan, which enumerated paths on every
     admissible pair, because power-freeness can be decided before any
     path work and by W1-T3 the profile is a single degree pattern.
     Outcome if empty: W1-T8 improves to \(n_0\ge18\). Outcome if
     non-empty and the \(S\)-condition holds: a tight 1-atom, hence
     **statement 0.1 is false** (`L025` R4). Additional cheap prefilters
     available from this attempt: 2-connectivity of the closure (W1-T9),
     non-bipartiteness (W1-T13), independence of the degree-\(\ge4\)
     vertices (W1-T9.1), and \(S\) meeting both \(\mathbb P\) and
     \(\mathbb P-1\) (W1-T10).
  2. **Primary (proof).** Look for a **congruence-type** obstruction, not
     a confinement-type one. W1-T13 is the model: it came free from the
     fact that \(\mathbb P-1\) is entirely odd. The concrete next
     falsifiable move is the mod-4 analogue: \(\mathbb P-1\equiv3\)
     and \(\mathbb P\equiv0\pmod4\) for \(k\ge2\), while
     \(\mathbb P-2\equiv2\pmod 4\); ask whether the residual object's
     forced memberships (W1-T10: \(S\) meets \(\mathbb P\) and
     \(\mathbb P-1\), avoids \(\mathbb P-2\)) plus the saturation
     residues of W1-T12 can be made to contradict a mod-4 structure
     theorem for through-sets, in the way `L035` T2 turns parity-constancy
     into bipartiteness. Kill condition: exhibit a vertex-taut
     \(C_4\)-free (D)-core whose through-set realizes all three
     memberships with no mod-4 structure (then the congruence route is
     dead too and R1 reduces to the search leg alone).
  3. **Secondary (proof).** W1-T14's chain cancellation: \(S=S_1+S_2\)
     with each \(S_i\) forced to meet a forbidden set while the sum
     avoids one. Quantify the cancellation and see whether it bounds the
     number of blocks or forces 2-connectivity of \(H\).
  4. **Deferred and why.** (i) Running R1 as a rung of the taut ladder —
     retired by W1-T15. (ii) Mersenne saturation as a standalone lever —
     demoted by the A6 kill test. (iii) Strengthening `C006` to density 1
     (route R2 of `G015`) — outside this leg and dependent on an
     unverified import. (iv) The unconditional form "no tight 1-atom
     exists" — unreachable by minimality (see the warning above); it
     should be retired as an R1 target in favour of the conditional form,
     which is what `G015` actually needs.
