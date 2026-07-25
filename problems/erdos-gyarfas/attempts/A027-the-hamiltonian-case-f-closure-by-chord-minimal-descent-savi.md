# A027 — the Hamiltonian-case (F) closure by chord-minimal descent: savings reachability and the exhaustive dodger search

- Date opened: 2026-07-25
- Problem: `P-002`
- Status: active
- Portfolio role: primary (Tier 1, `G015` case (5b), proof side; session
  `S027` — the (L-B) chord-savings move of `A026` T7, redirected from a
  lemma-first to a **reduction-first** attack)

## Intended mechanism

`A026` T7 split the interpolation target into (L-A) (short-range
exclusion) and (L-B) (long-range poison forcing) and named the missing
tool for (L-B): *the span/savings combinatorics of the chord system of a
longest path under \(C_4/C_8\)-exclusion*. The recorded plan was to prove
a savings-reachability lemma by hand.

This attempt keeps the object and inverts the order of work. Rather than
guessing a lemma about chord systems and testing it against the corpus, it
**proves two reductions** that turn the chord-system question into a
finite, decidable question at each order, and then decides it.

Two further changes of aim, both strictly in our favour:

1. **Prove the disjunction (F), not a disjunct.** `A025` T4 recorded
   (F) = (F-S) ∨ (F-T) and the plan was to prove one of them. Only (F)
   closes case (5b), and assuming *both* conclusions fail gives strictly
   more hypotheses: the residual object is then
   \(\{C_4,C_8,C_{16},C_{32}\}\)-free **and** has
   \(S\cap\{2,6,14,30\}=\emptyset\). Nothing in the program requires the
   disjuncts to be separated.
2. **Use the whole poison set \(\{2,6,14,30\}\).** \(30+2=32\) is a power,
   so \(30\in S\) blocks the closure exactly as 6 and 14 do
   (`L048`(iii)). At long path lengths 30 is the *cheap* target: a
   Hamiltonian path of length 34 needs savings 4 to reach it, not 20.

Target of this attempt, on the stratum where all eight known profile
objects live:

> **(H-F) (the Hamiltonian-case forcing statement).** Let \(H\) be a
> simple graph of order \(n\) with \(18\le n\le35\), let \(a,b\in V(H)\)
> have \(d(a)=d(b)=2\) and every other vertex degree \(\ge3\), let \(H\)
> be \(\{C_4,C_8\}\)-free, and suppose \(H\) has a Hamiltonian \(a\)–\(b\)
> path. Then \(S(H,a,b)\cap\{2,6,14,30\}\ne\emptyset\) or
> \(\mathrm{Spec}(H)\cap\{16,32\}\ne\emptyset\).

(H-F) is exactly (F) on the Hamiltonian stratum. Its negation is a
case-(5b) residual object whose 2-path closure is a tight 1-atom — the
standing **disproof-adjacent** pivot trigger — so the search decides, at
each order, either a proof step or a find.

Why this beats the recorded alternatives: it is the mechanism `A026`
already validated (chord surgery on a Hamiltonian path); it consumes the
profile hypothesis exactly where the near-miss corpus proves it must be
consumed (every internal position of the path must carry a chord —
precisely what the corpus's degree-2 corridors evade); it is falsifiable
at every order rather than only at the end; and its negative outcome is a
find, not a wasted session.

## Entry assumptions

Statement 0.1 verbatim. Consumed at recorded strength: `L049`/`L050`
(interference-completeness ⟺ vertex-tautness), `L048`(iii) (the spectrum
identity \(\mathrm{Spec}(B)=T_1\cup(S+2)\) — this is what makes
\(\{2,6,14,30\}\) the poison set and \(\{4,8,16,32\}\) the forbidden
spectrum), `L042` (residual-object structure), `L046` (2-connected below
36), `C046` (census), `C047`/`A026` (taxonomy, span law, exchange
calculus). `C040`/`C043` (the ladder's emptiness figures) are used **only
as cross-checks**, never as premises.

## Targeted obligations

- `G015`: exclude case (5b). (H-F) on \([18,35]\) closes it below 36 for
  every residual object carrying a Hamiltonian through-path.
- `G013`(a): structure theory for the tight-1-atom question.

## Plan and decisive tests

1. **Instrument (`E028`).** Anchors under both interpreters; the
   enumerator validated against an independently written brute-force
   enumeration (different traversal, different cycle detector, different
   savings routine, no symmetry breaking, no minimality propagation) on
   every case where either is feasible, including **nonempty** positive
   controls.
2. **Cross-check against the recorded ladder** (binding): with the poison
   prune switched off, the enumeration must return exactly 0 covers at
   orders \(\le18\), and at 19–20 only objects whose invariants match the
   recorded profile members. This ties an independent generation
   principle to `C039`/`C043`.
3. **Kill discipline (`A021`/`A026`, binding).** Petersen\(-e\) has **no**
   Hamiltonian \(a\)–\(b\) path (\(\max S=8=n-2\)), so it is outside the
   stratum; the order-14 exemplar is Hamiltonian and exactly-two but
   carries \(C_8\)s, so the class hypothesis excludes it. Both calibration
   objects are excluded by a *named* hypothesis, not by the order window
   alone. The 36 Hamiltonian corpus dodgers have \(\ge7\) degree-2
   vertices, so their chord systems do not cover: the profile hypothesis
   is consumed exactly where `C047` says it must be.
4. **Cheapest falsification of the approach:** the survivor count explodes
   before the window is decided, so that no order beyond the recorded
   ladder is settled.
5. **Pivot triggers.** A survivor that passes the exact stage is a
   case-(5b) residual object — report immediately, disproof-adjacent. An
   exploding survivor count turns the attempt to T5's bridge recursion or
   to a stronger route calculus.

## Deductions

Throughout: \(H\) is a graph of order \(n\), \(P=v_0v_1\cdots v_M\) is a
Hamiltonian \(a\)–\(b\) path (\(a=v_0\), \(b=v_M\), \(M=n-1\)), and a
**chord** is an edge \(v_iv_j\) of \(H\) with \(|i-j|\ge2\), identified
with the interval \([i,j]\); its **span** is \(j-i\). \(\mathcal C\) is
the chord set and \(\deg_{\mathcal C}(p)\) the number of chords with an
endpoint at position \(p\).

### T1 (chord-minimal descent) — proved

> Let \(H\) be a counterexample to (H-F) at order \(n\) (it satisfies the
> hypotheses, \(S\cap\{2,6,14,30\}=\emptyset\) and
> \(\mathrm{Spec}(H)\cap\{16,32\}=\emptyset\)), with Hamiltonian
> \(a\)–\(b\) path \(P\) and chord set \(\mathcal C\). Then \(\mathcal C\)
> covers \(\{0,\dots,M\}\) — every position is an endpoint of a chord —
> and for **every** inclusion-minimal subcover
> \(\mathcal C'\subseteq\mathcal C\) the graph \(H'=P+\mathcal C'\) is
> again a counterexample to (H-F) at the same order, with the extra
> property that every chord of \(\mathcal C'\) has an endpoint \(p\) with
> \(\deg_{\mathcal C'}(p)=1\).

*Proof.* **Coverage.** \(v_i\) with \(0<i<M\) has \(d_H(v_i)\ge3\) and
exactly two path edges, hence at least one incident chord; \(v_0\) has
degree 2 with one path edge, hence exactly one incident chord, and
likewise \(v_M\). Now fix an inclusion-minimal cover
\(\mathcal C'\subseteq\mathcal C\) and put \(H'=P+\mathcal C'\).

**Degrees.** Internal positions keep both path edges and at least one
chord, so \(d_{H'}(v_i)\ge3\). The unique chord at \(v_0\) lies in every
subcover (nothing else covers position 0), so \(d_{H'}(v_0)=2\); likewise
\(d_{H'}(v_M)=2\). Hence \(H'\) has exactly the two degree-2 vertices
\(a,b\), and \(P\) is a Hamiltonian \(a\)–\(b\) path of \(H'\).

**Forbidden cycles.** \(H'\subseteq H\) is a spanning subgraph and
"contains no \(C_\ell\)" is hereditary, so \(H'\) is
\(\{C_4,C_8,C_{16},C_{32}\}\)-free.

**Through-set.** Every \(a\)–\(b\) path of \(H'\) is one of \(H\), so
\(S(H',a,b)\subseteq S(H,a,b)\) and the poison set is still missed.

**Minimality form.** If a chord \(e=(i,j)\in\mathcal C'\) had
\(\deg_{\mathcal C'}(i)\ge2\) and \(\deg_{\mathcal C'}(j)\ge2\), then
\(\mathcal C'\setminus\{e\}\) would still cover, contradicting
minimality. ∎

T1 bounds the object: a minimal cover of \(M+1\) positions has at most
\(M+1\) chords and at least \(\lceil (M+1)/2\rceil\), so the
counterexample search at order \(n\) runs over a finite, explicitly
bounded family — bounded in the *number of chords*, not in the number of
graphs.

### T2 (the monotone reroute prune) — proved

> Let \(\mathcal D=\{(i_1,j_1),\dots,(i_t,j_t)\}\subseteq\mathcal C\) with
> \(i_1<j_1\le i_2<j_2\le\cdots\le i_t<j_t\). Then \(H\) has an \(a\)–\(b\)
> path of length \(M-\sum_{k=1}^{t}(j_k-i_k-1)\). Consequently, writing
> \(\Sigma(\mathcal C)\) for the set of all such sums,
> \(\{\,M-s : s\in\Sigma(\mathcal C)\,\}\subseteq S(H,a,b)\).

*Proof.* Traverse \(P\) from \(v_0\), replacing each arc \(P[i_k,j_k]\) by
the chord \(v_{i_k}v_{j_k}\). The intervals \([i_k,j_k]\) have pairwise
disjoint interiors and are met in order, so no vertex repeats: the result
is an \(a\)–\(b\) path. It omits \(j_k-i_k\) edges and adds one per
replaced arc. ∎

\(\Sigma\) is computed by the left-to-right dynamic program
\(R_0=\{0\}\), \(R_p=R_{p-1}\cup\bigcup_{(i,p)\in\mathcal C}(R_i+(p-i-1))\),
with \(R_p\subseteq R_M=\Sigma\); so the test "does \(\Sigma\) meet
\(\{M-2,M-6,M-14,M-30\}\)?" is monotone in the chord set and fires on
**prefixes**. That is what makes the search tractable, and T2 being a
one-sided (necessary) condition on a hypothetical dodger is what makes
pruning by it sound.

The span law of `A026` T5 is the \(t=1\) shadow of T2 under
\(\{C_4,C_8\}\)-freeness (a chord of span 3 or 7 closes a \(C_4\)/\(C_8\)
with its arc) and is not assumed separately here: the search tests the
whole graph for forbidden cycles, so all pairwise and higher-order
exclusions are enforced exactly rather than through a hand-derived table.
(One hand-derived entry of that table was found to be **wrong** during
this session and is corrected below, T6.)

### T3 (what the search decides) — proved (reduction); computed per order

Combining T1 and T2: at each \(M\), enumerate the inclusion-minimal covers
\(\mathcal C'\) of \(\{0,\dots,M\}\) with (i) \(P+\mathcal C'\)
\(\{C_4,C_8\}\)-free, (ii) \(\deg_{\mathcal C'}(0)=\deg_{\mathcal C'}(M)=1\),
(iii) \(\Sigma(\mathcal C')\cap\{M-2,M-6,M-14,M-30\}=\emptyset\). Every
counterexample to (H-F) at order \(n=M+1\) yields such a \(\mathcal C'\).
Hence

- **the enumeration is empty ⟹ (H-F) holds at that order**;
- **a survivor is only a candidate**, settled by exact computation of
  \(S\) (full path enumeration) and of \(\mathrm{Spec}\cap\{16,32\}\).

Survivors are expected and harmless: T2 sees only *monotone* reroutes, so
a graph whose length-14 path zigzags survives the prune and dies at the
exact stage. What matters for the proof is that the enumeration is
exhaustive and the exact stage decisive.

**Verdict (`E028`).** Run B (the (F) hypothesis, \(\{C_4,C_8,C_{16}\}\)) is
**empty at every order 16–29**, the last completed rung at the S027 close.
Run A (\(\{C_4,C_8\}\) only) is empty at 16–20 and at orders 21 and 22
returns 10 and 43 chord-minimal survivors — new objects, the first exhibited
at those orders (3 and 16 up to isomorphism) — every one killed twice by the
exact stage (\(14\in S\) on all 53, \(6\in S\) on 40, a \(C_{16}\) on all 53).

**What the top of run B actually proves** (`R003` F4 — important, and a
correction to the reading above). The poison prune's branch kills fall away
with \(M\): 61, 33, 45, 17, 2, 1, **0, 0, 0** at \(M=20\ldots28\). From
\(M=26\) on the search tree *with* the poison test is identical to the tree
without it, so what is proved at orders 27–29 is the **stronger**,
poison-free statement:

> no \(\{C_4,C_8,C_{16}\}\)-free graph of that order has exactly two
> degree-2 vertices, all other degrees \(\ge3\), and a Hamiltonian
> \(a\)–\(b\) path — whatever its through-set.

That implies (F) there a fortiori, but it exercises **none** of (F)'s
forcing mechanism: no inference about *why* the poisons appear is supported
above order 26. The ladder above that point is a class-emptiness ladder,
and should be read as one.

### T4 (the reach of the first-order calculus) — proved (the bound); expectation (the trend)

Let \(\mu_M=\min\{M-s:s\in\Sigma\}=M-\max\Sigma\) be the shortest
**monotone** route length. **Proved:** the T2 prune can never certify a
poison length below \(\mu_M\). **Expectation, not proved:** the binding
target is \(M-14\) — at \(M=17\) it needs savings 3, at \(M=29\) savings
15 — so the survivor count should grow with \(M\) until \(M\ge31\), where
\(30\in S\) becomes reachable with savings \(\le4\) again (and
\(M\in\{6,14,30\}\) is poisoned outright). Run A's counts (0, 0, 0, 0, 0,
10, 43 at orders 16–22) match. **Amendment (`R003` F4):** this expectation
is about run A only. In run B the \(C_{16}\) hypothesis empties the class
outright before the weakening can show, and the poison prune stops firing
entirely from \(M=26\) — so run B's zero survivors at the top of the ladder
say nothing about the calculus's reach. The *proof* content
of an empty enumeration is unaffected — emptiness stays decisive — but the
exact stage carries more of the load as \(M\) grows. This is the honest
statement of the calculus's reach, and it is why the exact stage is part
of the instrument rather than an afterthought.

### T5 (the non-Hamiltonian gap) — analysis; open

(H-F) assumes a Hamiltonian \(a\)–\(b\) path. All eight *independently
generated* profile objects (`C043`) have \(\max S=n-1\), but it is **not
proved** that the profile forces it — and the order-21/22 objects found
here are **no evidence at all** on that point (`R003` F8): they are
*constructed on* a Hamiltonian path, so their having one is a tautology,
not a datum. For a longest
\(a\)–\(b\) path \(P\) of length \(M<n-1\) the right generalisation of
T1/T2 replaces chords by **bridges** \((i,j,w)\): \(v_i\)–\(v_j\) paths of
length \(w\ge1\) internally disjoint from \(P\). Then

- maximality of \(P\) forces \(w\le j-i\);
- the cycle \(P[i,j]\,+\)bridge has length \((j-i)+w\), so
  \((j-i)+w\notin\{4,8,16,32\}\);
- T2 generalises verbatim to interval-disjoint bridge families with
  pairwise disjoint interiors, savings \(\sum((j_k-i_k)-w_k)\);
- T1's coverage step survives (every internal position still has a third
  edge, leading either to a chord or into a bridge),

**but** a bridge with \(w=j-i\) covers two positions and yields savings 0,
so covering no longer forces savings. That is precisely the corpus
mechanism (`C047`(c): dodges ride on degree-2 corridors; 99.1% of dodge
rows smooth to class-violating graphs) transposed to the off-path side —
with one constraint the corpus rows do not satisfy: on a profile pair
every *interior* vertex of every bridge also has degree \(\ge3\), so it
sprouts further bridges. Making that recursion carry the argument is the
named residue of this attempt.

**A first purchase on the zero-savings case (this session, provisional).**
Let \(K\) be a component of \(H[V\setminus V(P)]\) attaching to \(P\) at
exactly two positions \(v_i,v_j\) (\(i<j\)), and suppose the bridge through
\(K\) yields no savings, i.e. the shortest \(v_i\)–\(v_j\) path through
\(K\) already has length \(j-i\). Maximality of \(P\) bounds the *longest*
such path by \(j-i\) as well (otherwise substitute the arc and lengthen
\(P\)). So **every** \(v_i\)–\(v_j\) path through \(K\) has length exactly
\(j-i\): the two-terminal gadget \(G_K=H[K\cup\{v_i,v_j\}]\) has a
**singleton through-set**. It is vertex-taut by construction (2-connectivity
of \(H\) puts every vertex of \(K\) on such a path), so `L049` applies and
every cycle of \(G_K\) is the symmetric difference of two through-paths, of
length \(2(j-i)-2s\) — **every cycle of \(G_K\) is even, i.e. \(G_K\) is
bipartite** — while every interior vertex of \(K\) has degree \(\ge3\).
That is exactly the shape the bipartite hunt has been emptying
(`L035`/`C034`: no power-free member of the connected bipartite,
\(\le2\)-sub-cubic class at any order \(\le24\)). The route this suggests
for T5 is therefore *not* new combinatorics but a transfer: bound the
zero-savings bridges by the bipartite theory already in the dossier, and
handle \(\ge3\)-attachment components separately. Provisional — the
transfer needs the power-freeness hypothesis matched, which is not done
here.

### T6 (correction to the hand-derived chord-pair table) — proved

While deriving the pairwise exclusion table by hand it was asserted that
two **interior-disjoint** chords \((i,j)\), \((k,l)\) with \(j\le k\)
close a cycle of length \((l-i)+(k-j)+2\) with the path. That is **false**:
the putative return arc \(P[i,l]\) revisits both chord intervals, so
\(P\cup\{e,f\}\) contains no cycle other than \(C_e\) and \(C_f\) when
\(e,f\) are interior-disjoint. Two chords interact only when they share an
endpoint, nest, or cross; the correct cycle lengths are
\((k-j)+2\) (shared left endpoint \(i\), \(j<k\)),
\((k-i)+2\) (shared right endpoint / consecutive),
\((k-i)+(j-l)+2\) (nested \(i<k<l<j\)),
\((k-i)+(l-j)+2\) (crossing \(i<k<j<l\)).
The error was caught by the instrument's anchor suite before any use;
nothing downstream depended on it. Recorded because it is exactly the kind
of hand-table slip that the "test the whole graph, not the table" design
of `E028` is meant to make impossible.

## Failure analysis

No step failed. Two things were wrong in the *evidence and the framing*, and
both were caught by the delegated audit `R003` rather than by this attempt:

1. **The reachability claim was an extrapolation the data does not support**
   (`R003` F3(b)). "\(C_{16}\)-freeness brings the whole window
   \([18,35]\) into range" was read off the *node* growth
   (\(\approx\times1.9\)); the *wall-clock* growth is 1.8–2.4 per rung and
   rising, which puts orders 30–35 at days of single-core computation. The
   claim is withdrawn: the ladder is an open-ended computation with a stated
   last completed rung (order 29 at the S027 close).
2. **The top of the ladder no longer tests (F)** (`R003` F4). The poison
   prune stops firing at \(M=26\), so orders 27–29 prove class-emptiness,
   not poison forcing. Stronger as a statement, weaker as evidence about the
   mechanism — recorded in T3.

The standing risk is T4's, for run A: the first-order prune weakens as
\(M\) grows, and run A's reach is bounded by its survivor count and by its
enumeration growth (\(\approx\times3.5\) per order).

## Salvageable results

1. T1 and T2 — the two reductions. They are independent of the outcome and
   are what convert "a lemma nobody knows how to prove" into "a finite
   decision problem per order".
2. T5 — the bridge generalisation, with the exact point where the covering
   argument breaks: the named next tool.
3. T6 — the corrected chord-pair table.
4. The instrument `E028`: an independent generator of \(\mathcal G\)-profile
   members with a Hamiltonian through-path, orders of magnitude cheaper
   than the geng ladder on that stratum, and an independent cross-check of
   `C039`/`C043` at orders \(\le20\).

## Adversarial review

`R003`, delegated to a fresh-context `proof-reviewer` (independence mode
`delegated-subagent`): **PASS at lemma-and-instrument level**, 0 critical /
4 major / 4 minor / 3 notes. T1, T2 and T6 verified correct as stated; the
enumerator verified exhaustive over chord-minimal covers; every prune
verified one-sided; the symmetry break verified lossless; run A
\(M=15..21\) and run B \(M=15..23\) node counts reproduced **to the last
digit** by the reviewer re-running the shipped instrument outside the
repository, and the run-B configuration independently returned empty at
orders 19–25 from an enumerator the reviewer wrote from scratch.

All four major findings are answered:

- **F1/F2 (the load-bearing pair).** None of the three loss-capable prunes —
  the poison DP, the reversal symmetry break, and \(C_{16}\) detection — was
  exercised on a positive or nonempty instance by any recorded check: the
  \(\{C_4,C_8\}\)-free chord-minimal class is empty below order 19, so every
  `a3` comparison was \(\emptyset=\emptyset\), and the \(C_{16}\) branch
  (depth 15) was only ever called on graphs of order \(\le12\), where it can
  only return `False`. A bug there would have produced exactly the observed
  all-zero table. **Repaired**: new anchor families a6 (539 positive and 63
  negative \(C_{16}\) instances across \(M=15..34\), three detectors) and a7
  (reversal closure and poison-prune selection verified on the nonempty
  order-19/20 cover sets, plus the full production configuration against the
  independent reference on nonempty sets). Suite now 80,131 checks under both
  interpreters, identical histograms.
- **F3.** Placeholders filled; the window-reachability extrapolation
  withdrawn (see Failure analysis).
- **F4.** Recorded in T3 and amended in T4.

Minor findings F5–F8 and notes F9–F11 are answered in `E028/README.md`
(provenance and revision drift; the reproduction block and anchor count; the
cross-check restated at isomorphism level — where it is *stronger* than
claimed, recovering exactly the recorded objects; and the removal of the
"eighteen objects" over-count and its selection bias).

## Exit state

- Status: active
- Promoted records: experiment `E028`; ledger rows `L052` (reduction) and
  `C048` (computational verdict) offered; review `R003` passed with all
  major findings repaired in place; `G015` updated.
- Next action: finish the run-B ladder above order 29 (open-ended; it is a
  class-emptiness ladder above order 26), then `T5` — extend the descent
  from chords to bridges for the non-Hamiltonian stratum.
