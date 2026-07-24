# A017 — The parity channel is the bipartite channel: a congruence structure theorem for two-terminal gadgets

- Date opened: 2026-07-24
- Problem: `P-002`
- Status: active
- Portfolio role: primary (Thread B: the congruence/parity ring channel opened by `L034`)

## Intended mechanism

`L034` (audited external memo, `A016`) widened the ring disproof criterion from
the pinch to any \(L\)-fold sumset avoidance, and named three congruence
channels: all-odd \(S\), odd-prime \(\gcd(S)\), and \(S\subseteq2+4\mathbb Z\).
`A016` M4 recorded that these channels have **no reduction theory** — the
pendant/block machinery of `L031`/`L032` is pinch-specific because the pendant
shift \(S\mapsto1+S\) flips parity — and `A016` M3 recorded that the memo's
bipartite reformulation is only "the canonical instance, not an equivalence,"
because *all-odd \(S\) does not force bipartiteness*.

The mechanism proposed here is that both of those readings are too weak, and in
the same direction: **parity of the through-set is a global structural
invariant, not a numerical accident**. Concretely, the parity channel is
governed by two elementary facts that no previous session used together:

1. a bipartite two-terminal graph has parity-constant \(S\) *automatically*
   (parity of the terminals' colour classes), so no path enumeration is needed
   to certify the channel; and
2. conversely, parity-constancy of \(S\) forces bipartiteness as soon as every
   vertex is on some through-path (the standard failure — an odd cycle hidden
   in a lobe — is exactly what `L027` already routes to the 1-atom question).

If both hold, the parity channel *is* the bipartite channel: bipartite
generation becomes a complete instrument for it (not a heuristic restriction),
and the search cost collapses, because bipartite \(C_4\)-free graphs of minimum
degree \(\ge3\) are far rarer than general ones. That is the point of leverage:
the general \(\{C_4,\dots\}\)-free stream dies at order 15 (`C027`), while the
bipartite sub-stream is cheap into the low twenties — so this channel can be
pushed *past the wall that stops every other thread*.

Preferability over the live alternatives: the inherited proposal (i) was an
odd-\(S\) taut *scan mode* over the general order-\(\le15\) stream, which this
theorem makes redundant (it re-scans a class that is empty for a reason already
proved) and replaces with a search that reaches new orders; the inherited
proposal (ii), the `G014` source audits, is de-gated for this thread by the
criterion below, which needs no external import at all. The pencil endgame
(Thread A) is untouched and stays live: it lives at even bands, this at odd
ones.

## Entry assumptions

Statement 0.1 exactly as in `STATEMENT.md`; all graphs finite and simple.
"Power-free" = no cycle of length \(2^k\), \(k\ge2\). Definitions D-A1–D-A5
(`A011`), D-B1 (`A012`), D-P1–D-P3 (`A014`) at their recorded meanings.
Imported internal claims used at recorded strength: `L025` R1/R3/R4 (ring and
atom reductions), `L027` (lobe decomposition), `L034` (generalized ring
criterion), `L022`/`C027` (finite exclusions, used only to locate the search
frontier, never inside a proof). No external import is used anywhere in this
attempt.

## Targeted obligations

- `G013` sub-question (c): the congruence channels — their missing reduction
  theory, and the search instrument for them.
- `G014`: item (2) (the bipartite \(\ge32\) bound and the reported
  bipartite-EGC verification to 31) is **de-gated** for this thread by T3
  below; the audit remains open for the other threads that cite it.

## Plan and decisive tests

1. Cheapest falsification of the *theorem* half: exhaustive machine check of
   T1/T2 over all small two-terminal graphs (all connected graphs to order 8,
   every ordered terminal pair): any vertex-taut pair with parity-constant
   \(S\) in a non-bipartite graph refutes T2 outright.
2. Cheapest falsification of the *program* half: run the bipartite hunt at
   orders \(\le15\), where `C027` proves the class is empty. A hit there would
   contradict a proved row and means the pipeline is wrong, not the world.
3. Decisive test of the channel itself: the same hunt at orders 16–22. Any hit
   disproves statement 0.1 (T3); an empty run extends the finite frontier of
   the parity channel seven orders past the general wall.
4. Pivot condition: a hit at any order (→ disproof protocol, `PROOF.md`
   becomes a counterexample candidate and the mandatory review transition
   fires); or T2 failing verification (→ the channel keeps its old,
   enumeration-bound search and the memo's "instance, not equivalence" reading
   stands).

## Deductions

Throughout, \((H,a,b)\) is a two-terminal graph (D-A1: \(H\) finite, simple,
connected, \(a\ne b\)), \(S=S(H,a,b)\) its through-set, and *vertex-taut*
(D-B1) means every vertex of \(H\) lies on some simple \(a\)–\(b\) path. Call
\(S\) **parity-constant** if all its elements have the same parity.

### T0 (block chain of a vertex-taut two-terminal graph) — proved

Let \((H,a,b)\) be vertex-taut. Then

1. every cut vertex of \(H\) separates \(a\) from \(b\), and \(H-c\) has
   exactly two components for every cut vertex \(c\);
2. the block–cut tree is a path; writing the blocks in order
   \(B_1,\dots,B_m\) with \(a\in B_1\), \(b\in B_m\) and
   \(B_i\cap B_{i+1}=\{c_i\}\), and setting \(c_0=a\), \(c_m=b\), we have
   \(c_{i-1}\ne c_i\), every simple \(a\)–\(b\) path is a concatenation of
   independent simple \(c_{i-1}\)–\(c_i\) paths (one per block) and conversely,
   so
   \[S(H)=S(B_1)+\dots+S(B_m)\quad(\text{Minkowski sum, each } S(B_i)\ne\emptyset),\]
   and each \((B_i,c_{i-1},c_i)\) is vertex-taut;
3. every cycle of \(H\) lies in a single block.

*Proof.* (1) Let \(c\) be a cut vertex and \(K\) a component of \(H-c\)
containing neither \(a\) nor \(b\). A simple \(a\)–\(b\) path meeting \(K\)
would have to enter and leave \(K\) through \(c\), visiting \(c\) twice —
impossible. So no vertex of \(K\) is essential, contradicting tautness
(\(K\ne\emptyset\)). Hence every component of \(H-c\) contains \(a\) or \(b\);
as there are at least two components and \(a\ne b\), there are exactly two, one
containing each, so \(c\) separates them.

(2) In the block–cut tree, let \(P\) be the path from the block containing
\(a\) to the block containing \(b\). If a block \(B\) is not on \(P\), it hangs
off some cut vertex \(c\), i.e. \(B\setminus\{c\}\) lies in a component of
\(H-c\) containing neither \(a\) nor \(b\) — contradicting (1). So the tree is
the path \(P\). A simple \(a\)–\(b\) path must cross each cut vertex \(c_i\)
(by (1)), and between consecutive crossings it stays in one block, so it
decomposes as stated; conversely any choice of simple \(c_{i-1}\)–\(c_i\) paths
concatenates to a simple \(a\)–\(b\) path, since distinct blocks meet only in
cut vertices. \(c_{i-1}\ne c_i\) because a path in a tree does not repeat a
vertex. Tautness of each block: a vertex \(v\in B_i\) lies on a simple
\(a\)–\(b\) path of \(H\), whose \(B_i\)-segment is a \(c_{i-1}\)–\(c_i\) path
through \(v\). (3) Standard (a cycle is 2-connected, hence inside one block). ∎

*Remark.* T0 is `A014` T3.1/T3.2/T3.4 with the degree hypotheses deleted; their
recorded proofs never used the degrees. Nothing below needs the degree parts
(T3.3).

### T1 (parity fan lemma) — proved

Let \(H\) be 2-connected, \(a\ne b\in V(H)\), and let \(C\) be an odd cycle of
\(H\). Then \(H\) has simple \(a\)–\(b\) paths of both parities.

*Proof.* Let \(H'=H+z\) where \(z\) is a new vertex adjacent exactly to \(a\)
and \(b\). \(H'\) is 2-connected: \(H'-z=H\) is connected; \(H'-v\) for
\(v\in V(H)\) is connected because \(H-v\) is connected (\(H\) 2-connected) and
\(z\) retains at least one neighbour among \(\{a,b\}\setminus\{v\}\).

Apply the fan version of Menger's theorem in \(H'\) with \(k=2\), source
\(z\) and target set \(U=V(C)\) (\(|U|\ge3\ge k\), \(z\notin U\)): there are
two paths \(Q_1,Q_2\) from \(z\) to \(U\), meeting each other only in \(z\) and
each meeting \(U\) only in its endpoint. Since \(N_{H'}(z)=\{a,b\}\) and the
two paths leave \(z\) by distinct edges, we may take
\(Q_1=z\,a\cdots u\) and \(Q_2=z\,b\cdots v\) with \(u\ne v\) on \(C\).

Put \(P_a=Q_1-z\) (an \(a\)–\(u\) path in \(H\), possibly trivial when
\(a=u\)) and \(P_b=Q_2-z\) (a \(b\)–\(v\) path). They are vertex-disjoint, and
each meets \(V(C)\) only in its endpoint. The vertices \(u\ne v\) split \(C\)
into arcs \(A_1,A_2\) with \(\ell(A_1)+\ell(A_2)=|C|\) odd, so
\(\ell(A_1)\not\equiv\ell(A_2)\pmod 2\). Then
\(W_i=P_a\cdot A_i\cdot \overline{P_b}\) (\(i=1,2\)) are simple \(a\)–\(b\)
paths — the three pieces are pairwise disjoint except at the shared endpoints
\(u,v\) — of lengths \(\ell(P_a)+\ell(A_i)+\ell(P_b)\), which differ in parity.
∎

### T2 (parity structure theorem) — proved

Let \((H,a,b)\) be vertex-taut. Then the following are equivalent:

  (i) \(S\) is parity-constant;
  (ii) \(H\) is bipartite.

Moreover, under (ii), with \(\{X,Y\}\) the (unique) bipartition of the
connected graph \(H\): \(S\) is all-odd iff \(a,b\) lie in different classes,
and all-even iff they lie in the same class.

*Proof.* (ii)\(\Rightarrow\)(i) and the "moreover": in a bipartite graph every
\(a\)–\(b\) walk has length \(\equiv0\) or \(1\pmod2\) according as \(a,b\) lie
in the same class or not. (Tautness is not needed here.)

(i)\(\Rightarrow\)(ii): suppose \(H\) is not bipartite and fix an odd cycle
\(C\). By T0.3, \(C\) lies in one block \(B_j\), which is therefore not a
bridge, hence 2-connected. By T0.2 its attachment terminals satisfy
\(c_{j-1}\ne c_j\), so T1 applies to \((B_j,c_{j-1},c_j)\) and \(C\): \(S(B_j)\)
contains lengths of both parities. Choosing any \(s_i\in S(B_i)\ne\emptyset\)
for \(i\ne j\) and both parities in the \(j\)-th coordinate, the Minkowski
formula of T0.2 produces two elements of \(S\) of different parity —
contradicting (i). ∎

*Sharpness (both hypotheses used).* Tautness cannot be dropped: take a triangle
\(xyz\) and attach \(a\) and \(b\) to \(x\); the only \(a\)–\(b\) path is
\(a\,x\,b\), so \(S=\{2\}\) is parity-constant while \(H\) is not bipartite
(\(y,z\) are inessential — exactly the lobe of `L027`). Connectivity of the
argument is genuine: T1 fails for 1-separable graphs, which is why T0 is needed
first.

### T3 (bipartite assembly criterion) — proved

Let \(H\) be a finite simple connected **bipartite** graph, power-free, with at
most two vertices of degree \(<3\); if there are exactly two such vertices,
assume their degrees are \(\ge1\) and sum to \(\ge3\); if there is exactly one,
assume its degree is \(1\) or \(2\). Then statement 0.1 is **false**.

*Proof.* Three cases by the number \(t\) of sub-cubic vertices.

\(t=0\): \(H\) has \(\delta\ge3\) and is power-free — a counterexample outright.

\(t=1\): \(H\) is a 1-atom (D-A4); apply `L025` R4.

\(t=2\): let \(a,b\) be the two sub-cubic vertices, so
\(\{\deg a,\deg b\}\subseteq\{1,2\}\) with sum \(\ge3\), i.e. \(\{2,2\}\) or
\(\{1,2\}\). Then \((H,a,b)\) satisfies (D) (D-A2: non-terminals \(\ge3\);
terminal degrees \(\ge1\) summing to \(\ge3\)) and is power-free. Since \(H\)
is bipartite, \(S\) is parity-constant (T2, easy direction).

*Case A: \(S\) all odd.* Every 3-fold sum \(s_1+s_2+s_3\) with \(s_i\in S\) is
odd and \(\ge3\), hence not a power of two (powers of two here are \(\ge4\) by
D004). By `L034` — equivalently by `L025` R1, whose spectrum formula gives
\(\mathrm{Spec}(R_3)=\mathrm{Spec}(H)\cup\Sigma_3\) — the ring \(R_3(H,a,b)\)
is a counterexample.

*Case B: \(S\) all even.* Two sub-cases by the degree pair.

  *B1: \(\deg(a)=\deg(b)=2\).* Let \(H^+=H+a'\) with a new vertex \(a'\)
  adjacent exactly to \(a\), and consider \((H^+,a',b)\). Every simple
  \(a'\)–\(b\) path starts with the edge \(a'a\) and continues as a simple
  \(a\)–\(b\) path of \(H\), so \(S(H^+,a',b)=1+S\) is all odd; \(a'\) lies on
  no cycle, so \(\mathrm{Spec}(H^+)=\mathrm{Spec}(H)\) is power-free; and (D)
  holds: \(a\) is now a non-terminal of degree \(3\), all other non-terminals
  are unchanged with degree \(\ge3\), and the terminal degrees are
  \(\deg(a')=1\) and \(\deg(b)=2\), sum \(3\). Case A applied to
  \((H^+,a',b)\) gives the counterexample \(R_3(H^+,a',b)\).

  *B2: the degrees are \(\{1,2\}\); name them so that \(\deg(a)=1\),
  \(\deg(b)=2\).* Let \(x\) be the neighbour of \(a\). If \(x=b\) the edge
  \(ab\) is the only simple \(a\)–\(b\) path and \(S=\{1\}\) is odd, contrary
  to Case B; so \(x\ne b\), and \(x\) is a non-terminal with
  \(\deg_H(x)\ge3\). Every simple \(a\)–\(b\) path starts \(a\,x\), so
  \(S(H-a,x,b)=S-1\) is all odd; \(\mathrm{Spec}(H-a)=\mathrm{Spec}(H)\) is
  power-free (\(a\) lies on no cycle); and \((H-a,x,b)\) satisfies (D):
  \(\deg_{H-a}(x)=\deg_H(x)-1\ge2\), \(\deg(b)=2\), all other degrees
  unchanged \(\ge3\). Case A applied to \((H-a,x,b)\) gives the
  counterexample \(R_3(H-a,x,b)\). ∎

*Remark (what T3 buys).* T3 needs **no** path enumeration, **no** tautness
test, and **no** external import: a bipartite graph is a disproof as soon as it
is \(C_4\)-, \(C_8\)-, \(C_{16}\)-free (…) with at most two sub-cubic vertices.
In particular the memo's "Mersenne window" logic (`A016` M9), which was
conditional on the unverified bipartite \(\ge32\) bound, is unnecessary for the
bipartite hunt — the hunt does not need to know *which* through-lengths a
hypothetical hit would have.

### T4 (completeness of bipartite search for the parity channels) — proved

Suppose \((H,a,b)\) is a power-free (D)-gadget whose through-set is
parity-constant — in particular, any witness of `L034`'s channel (i) (all-odd
\(S\)) or channel (iii) (\(S\subseteq2+4\mathbb Z\), which is all-even). Then
either

  (a) \(H\) is vertex-taut, and then \(H\) is bipartite (T2) and is found by a
      bipartite search over its order; or
  (b) \(H\) is not vertex-taut, and then statement 0.1 is already false by
      `L027` — \(H\) contains a 1-atom (whence `L025` R4) or a power-free graph
      of minimum degree \(\ge3\) (a counterexample outright).

Hence a search over bipartite graphs with at most two sub-cubic vertices is
exhaustive for the parity channels, modulo exactly the same 1-atom
relativization every other rung of `G013` already carries. ∎

*Scope caveat.* T4 covers `L034` channels (i) and (iii) only. Channel (ii)
(\(\gcd(S)\) divisible by an odd prime) is **not** bipartite-forced: the theta
graph \(\Theta(3,3,3)\) is vertex-taut, non-bipartite, and has
\(S=\{3\}\) with \(\gcd=3\) (it fails (D) only through its degree-2 internal
vertices). So the mod-\(p\) channel keeps its own open reduction problem, and
no claim here bounds it.

### T5 (part-size bound for the search) — proved

Let \(H\) be bipartite with classes \(X,Y\) of sizes \(p,q\), \(C_4\)-free,
with at most two vertices of degree \(<3\), each of degree \(\ge2\). Then
\[3q-4\le\binom p2\qquad\text{and}\qquad 3p-4\le\binom q2 .\]

*Proof.* \(C_4\)-freeness says two vertices of \(Y\) have at most one common
neighbour, so the map sending \(y\in Y\) to the \(\binom{d(y)}2\) pairs of its
neighbours is injective into \(\binom X2\): \(\sum_{y\in Y}\binom{d(y)}2\le
\binom p2\). At most two vertices of \(Y\) have degree \(2\)
(\(\binom22=1\)) and the rest have degree \(\ge3\) (\(\binom32=3\)), so the
left side is \(\ge3(q-2)+2=3q-4\). Symmetrically for \(X\). ∎

This is used only to skip provably empty part-splits in `E015`; it makes the
skipping part of the exhaustiveness certificate rather than an unjustified
optimisation.

### T6 (corollaries recorded, not used below)

1. *Odd bands.* All-odd \(S\) forces \(d(a,b)=s_{\min}\) odd, all-even forces
   it even — so the parity ladder lives at odd bands and the mod-4 ladder at
   even bands \(\equiv2\bmod4\). (Already noted in `A016`; now with a reason.)
2. *Parity flip.* Under the pendant reduction `L031`, the core of an all-odd
   gadget is all-even, i.e. bipartite with **both** terminals in the same
   class. So the pendant/core bookkeeping of the pinched channel does transfer
   to the parity channel — it just alternates between the two bipartite
   sub-cases instead of preserving one. This is the reduction theory `A016` M4
   recorded as missing.
3. *Girth.* A power-free bipartite gadget has girth \(\ge6\) (no \(C_4\); odd
   girth impossible), so `C027`'s stream condition is satisfied and the
   bipartite hunt at orders \(\le15\) must be empty — a genuine cross-check of
   `C027` by an independent generator.

## Failure analysis

Not a failure. Two dossier-side corrections are needed, both in the direction
of *strengthening* the audited external memo rather than weakening it:

- `A016` M3 stated that the memo's bipartite reformulation is "the canonical
  instance, not an equivalence," because all-odd \(S\) does not force
  bipartiteness. The counterexample behind that reading is exactly a non-taut
  gadget (the pendant triangle above), i.e. the case `L027` already sends to
  the 1-atom question. On the taut side — the only side any rung of `G013`
  works with — T2 shows it *is* an equivalence. The recorded verdict is
  therefore too weak and is corrected here; the memo's instinct was right.
- `A016` M4 recorded that the parity channel "has no reduction theory yet
  (pendant shifts flip parity)". The flip is real but harmless: T6.2 makes it
  the statement that pendant reduction toggles between the two bipartite
  sub-cases. The channel has a reduction theory.

Neither correction touches a proved row.

## Salvageable results

T0–T6 stand independently of the search outcome. The pair (T3, T4) is the
usable asset: T3 makes any bipartite hit a disproof with no auxiliary
computation, T4 makes bipartite generation a complete instrument for the
channel. Together they convert an enumeration-bound scan of an
already-exhausted class into a search that runs several orders past the general
frontier (`E015`).

## Outcome

Both plan items executed in-session.

- The theorem's own kill condition (plan item 1) was run exhaustively
  before the ledger entry: every connected graph of order \(\le7\) and every
  connected \(C_4\)-free graph of orders 8–9, all ordered terminal pairs,
  through-sets by explicit path enumeration. T2 never failed (952 instances
  where its hypothesis held); T1 held in 27,196; T0's chain/Minkowski
  structure in 33,962; and all 10,788 parity-constant non-bipartite pairs
  were non-taut, which is the sharpness statement in quantitative form.
- The search (plan items 2–3) ran empty at every order \(\le21\)
  (`C034`): class sizes 0, 0, 2, 1, 6, 8, 75, 197, 2,715, 10,865 at orders
  12–21, every member containing a \(C_8\), minimum \(C_8\) count never
  below 13, so the \(C_{16}\) test is never decisive. Orders \(\le15\)
  returned empty as `C027` requires (plan item 2's consistency check). An
  order-22 run was launched and left unfinished on a loaded machine and is
  excluded from every record.
- Neither pivot condition fired.

Two readings of the negative result, both recorded as judgement rather than
theorem: the parity channel is *further* from a witness than the pinched one
(uniform \(\ge13\) blocking \(C_8\)s against 3–7 for the equality blocks),
and the natural proof-side target it suggests — "bipartite + \(\delta\ge3\)
+ \(C_4\)-free \(\Rightarrow C_8\)" — is false at large order, because the
bipartite double cover of a cubic graph of girth \(g\) is cubic, bipartite
and of girth \(\ge g\) (`C009` supplies the large-girth cubic graphs). So a
bipartite EGC theorem must be order-bounded or must consume the
\(C_{16}/C_{32}\) alternatives.

## Exit state

- Status: complete for its stated scope (channels (i) and (iii)); channel
  (ii) explicitly out of scope and now the open half of `G013`(c).
- Promoted records: `L035` (T0–T5, with T6.2 as the reduction theory);
  `C034` (`E015` results); corrective notes on `A016` M3/M4 and on `G014`
  item (2).
- Next action: finish the order-22 leg of `E015`; then open the
  odd-prime-gcd channel (Thread B3) — does condition (D) forbid
  \(\gcd(S)\) from having an odd prime factor? \(\Theta(3,3,3)\) shows the
  degree condition, not parity, must do the work there.
