# A021 — the mod-4 congruence hunt against the case-5b residual object: chain-calculus limits and the kill test

- Date opened: 2026-07-24
- Problem: `P-002`
- Status: closed (kill condition fired; route retired)
- Portfolio role: proof-side companion of the S020 primary (the order-16
  \(\mathcal G\)-profile scan, `E018`); this is `A019` exit item 2 run to
  its pre-registered kill condition.

## Intended mechanism

`A019` W1-T13 proved the residual object non-bipartite by a *congruence*
argument: bipartiteness confines every \(P_H(a,z)\) to one parity class,
while Mersenne saturation (W1-T12) forces \(P_H(a,z)\) to hit
\(\mathbb P-1\subseteq2\mathbb Z+1\) for every non-neighbour \(z\). The
hunt: find the mod-4 analogue. The relevant residues are perfectly
separated — for \(k\ge2\),
\[\mathbb P\equiv0,\qquad \mathbb P-1\equiv3,\qquad \mathbb P-2\equiv2
\pmod4,\]
and `L042` forces \(S\) to meet the first two and avoid the third
(as a set, not as a residue class). A mod-4 structure theorem for
through-sets of vertex-taut \(C_4\)-free cores — some hypothesis playing
the role bipartiteness plays at mod 2 — could then contradict the forced
memberships and exclude case (5b), closing `G015` (`L041`).

Pre-registered kill condition (`A019` exit item 2, carried into
`problem.json`): *exhibit a vertex-taut \(C_4\)-free (D)-core whose
through-set realizes all three memberships with no mod-4 structure* —
then the congruence route is dead and case (5b) reduces to the search
leg alone.

## Entry assumptions

Statement 0.1 verbatim; D-A1–D-A5; tightness per `A018` T2; the S019
state at recorded strength: `L039` (the class \(\mathcal G\)), `L041`
(case analysis; only (5b) survives under (R)), `L042` (the residual
object's forced structure, (R)-conditional). The probe below drops
power-freeness deliberately (as `E016` A6 did): it measures what
tautness + \(C_4\)-freeness + the degree profile force *without* the
power spectrum's help.

## Targeted obligations

- `G015`: exclude case (5b) — the congruence-type obstruction leg.
- `G013`(a): structure theory for the tight-1-atom question.

## Plan and decisive tests

1. Hand analysis first: what does the cycle-space calculus actually
   control about path lengths mod 4? (If the answer is "nothing beyond
   parity," the theorem being hunted has no mechanism to run on.)
2. The kill test, computational: enumerate the exact terminal profile of
   case (5b) — connected, \(C_4\)-free, exactly two degree-2 vertices,
   all others \(\ge3\) — at orders \(\le13\) (power-freeness dropped),
   restrict to vertex-taut members, and tabulate the joint distribution
   of the forced-membership triple against \(S\bmod4\). Kill fires if
   the triple is realized with unconfined residues.
3. Pivot triggers: kill fires → retire the route, record why, and hand
   the proof side of case (5b) to the chain-cancellation tension
   (`L042`/W1-T14) and the search ladder. A genuine residue invariant
   appears → chase the structure theorem.

## Deductions

### T1 (the chain-calculus identity and its mod-2 exactness) — proved

**Claim.** Let \(H\) be a graph, \(x\ne y\in V(H)\), and \(P,Q\) two
simple \(x\)–\(y\) paths. Then \(E(P)\,\triangle\,E(Q)\) is an even
subgraph, hence an edge-disjoint union of cycles \(C_1,\dots,C_t\), and
\[\ell(P)+\ell(Q)\;=\;2\,|E(P)\cap E(Q)|\;+\;\sum_{i=1}^t\ell(C_i).\]
Consequently, if every cycle length of \(H\) lies in a fixed residue
class \(r\bmod m\):

1. for \(m=2\) (i.e. \(H\) bipartite when \(r=0\)): \(\ell(P)\equiv
   \ell(Q)\pmod 2\) — parity of \(x\)–\(y\) paths is an invariant;
2. for \(m=4\): the identity constrains \(\ell(P)+\ell(Q)\) only up to
   the term \(2|E(P)\cap E(Q)|\), which takes both residues \(0,2\bmod4\)
   as the shared edge set varies; **no confinement of \(\ell(P)\bmod4\)
   follows**.

*Proof.* In the multigraph \(P+Q\) every vertex has even degree (each of
\(x,y\) has one edge from each path; every internal vertex has 0 or 2
from each), so after cancelling doubled edges, \(E(P)\triangle E(Q)\)
has all degrees even and decomposes into edge-disjoint cycles. Counting
edges, \(\ell(P)+\ell(Q)=|E(P)\triangle E(Q)|+2|E(P)\cap E(Q)|
=\sum_i\ell(C_i)+2|E(P)\cap E(Q)|\). (1) is immediate mod 2 (the shared
term vanishes). For (2), the shared term survives mod 4 and is not
controlled by any cycle hypothesis; T3's data realizes both behaviours
inside the target class. ∎

**Reading.** Parity is *exactly* the information the cycle space carries
about path lengths; the leak term \(2|E(P)\cap E(Q)|\) destroys every
congruence finer than mod 2. This is why `L035` T2 (parity-constant
\(\iff\) bipartite) exists and why it has no mod-\(2^t\) (\(t\ge2\))
analogue built on cycle structure: any such theorem would need a
mechanism *outside* the chain calculus (path systems with controlled
intersections, orientations/flows, …). Recorded as the mechanism-side
half of the kill; it is an analysis of where the machinery can run, in
the spirit of `A019` W1-T15, not a formal impossibility proof.

### T2 (an illustrative boundary case) — proved

All three cycle lengths of a theta graph \(\Theta(p,q,r)\)
(\(p\le q\le r\), internally disjoint branches) are \(\equiv0\bmod4\)
iff \(p\equiv q\equiv r\equiv0\) or \(p\equiv q\equiv r\equiv2\bmod4\);
e.g. \(\Theta(2,6,6)\) (cycles \(8,8,12\)), whose through-set
\(S=\{2,6\}\) is exactly `L034`'s fatal invisible shape. Even in this
maximally rigid all-cycles-\(0\bmod4\) situation the through-set sits in
one residue class *only because the branches are disjoint* (the T1
shared term is 0); the moment paths share edges the confinement is
gone. (Hand check; consistent with the `E018`/`mod4.py` data below.)

### T3 (the kill test) — computational, `E018`/`mod4.py`

Probe over the exact case-(5b) terminal profile (connected,
\(C_4\)-free, exactly two degree-2 vertices \(a,b\), all others
\(\ge3\); geng stream as in `E018`, power-freeness dropped), orders
10–13, PyPy 7.3.23. Per member: \(S=S(H,a,b)\) by exact simple-path
enumeration with an essential-vertex mask (vertex-taut \(\iff\) every
vertex on some \(a\)–\(b\) path); the membership triple
(\(S\cap\mathbb P\ne\emptyset\), \(S\cap(\mathbb P-1)\ne\emptyset\),
\(S\cap(\mathbb P-2)=\emptyset\)); \(S\bmod4\); bipartiteness;
cut-vertex count. Results (`data/mod4_n{10..13}.json`):

| order | class | vertex-taut | taut + full triple | residue sets seen among triples |
|---|---|---|---|---|
| 10 | 22 | 22 | **2** | \(\{0,1,3\}\) (both) |
| 11 | 125 | 124 | 0 | — |
| 12 | 1,139 | 1,120 | **3** | \(\{0,1,2,3\}\) (all three) |
| 13 | 10,966 | 10,853 | **55** | \(\{0,1,2,3\}\) (all 55) |

Every triple witness is non-bipartite (forced, `L035` T2) and
2-connected (0 cut vertices); 47/55 at order 13 have \(ab\in E\); no
member of the taut class at any of these orders has \(S\subseteq
\mathbb P-2\) (no invisible shape); tautness is generic in the profile
class (\(\ge98.9\%\) at every order).

**The order-10 witnesses are decisive.** One of the two is **Petersen
minus an edge** (verified by `labelg` canonical-form equality;
spectrum \(\{5,6,8,9\}\), \(S=\{4,5,7,8\}\) as recorded in `C031`).
So the very first order at which the profile class realizes the triple
realizes it on the dossier's most-studied gadget: \(S\) meets
\(\mathbb P\) at \(\{4,8\}\), meets \(\mathbb P-1\) at \(\{7\}\), avoids
\(\mathbb P-2\), with \(\min S=d(a,b)=4\notin\mathbb P-2\) and
\(\max S=8\ge7\) — every forced through-set condition of `L042` — while
also being vertex-taut, non-bipartite, 2-connected, Mersenne-saturated
(`E016` A6 covers order 10), and degree-\(\ge4\)-independent
(vacuously). The residue patterns \(\{0,1,3\}\) (residue 2 absent,
order 10) and \(\{0,1,2,3\}\) (residue 2 present, orders 12–13) **both**
occur: presence of residue-2 elements is not controlled in either
direction. No invariant separates the triple witnesses from the rest of
the taut class at the residue level.

**Verdict: the pre-registered kill condition fired.**

### T4 (scope of the kill — stronger than mod 4) — proved reading

The kill condition asked for one exhibit; T3 supplies sixty, and the
exhibit's meaning is modulus-independent: the hypothesis set
\(\{\)vertex-taut, \(C_4\)-free, (5b) degree profile,
\(S\cap\mathbb P\ne\emptyset\), \(S\cap(\mathbb P-1)\ne\emptyset\),
\(S\cap(\mathbb P-2)=\emptyset\), non-bipartite, 2-connected,
Mersenne-saturated\(\}\) is **simultaneously realizable** (Petersen
\(-e\)). Therefore *no theorem — congruence-type or otherwise — can
derive a contradiction from that hypothesis set alone*, for any
modulus: something not on the list must fight. On Petersen\(-e\) the
only `L042` constraint that fails is the band-4 pencil condition
(W1-T15.1, "no two internally disjoint 4-paths"), which is exactly
where **power-freeness** enters at band 4 — Petersen\(-e\) is
disjoint-type (`C032`/`C035`) and its \(C_8\)s are two-through-path
symmetric differences. The discriminating layer for case (5b) is the
\(C_8\) interference/confinement structure, never residue arithmetic.
This sharpens `A019`'s category diagnosis: the congruence *channel* is
where the residual object lives, but a congruence *argument* cannot
close it.

## Failure analysis

The route was killed by its own pre-registered test, at the first order
the test could possibly fire (the profile class first realizes the
triple at order 10), on a graph the dossier already knew intimately.
First obstruction, precisely: T1's leak term \(2|E(P)\cap E(Q)|\) — the
cycle space controls path arithmetic mod 2 and no finer, so mod-4
confinement has no mechanism; T3 then shows the hoped-for conclusion is
false anyway (the forced memberships are realizable with no residue
structure). Two independent nails.

What the parity success actually used, in hindsight: \(\mathbb P-1\) is
*entirely* odd — a residue-class statement — whereas \(\mathbb P-2\) is
a *thin subset* of its residue class \(2+4\mathbb Z\). Avoiding a thin
set is arithmetically cheap (T3's order-12/13 witnesses contain
\(10\in2+4\mathbb Z\) while avoiding \(\{2,6\}\)); no congruence can see
thinness.

## Salvageable results

1. **T1** — a reusable exact identity and the precise statement of why
   parity is the ceiling of chain-calculus congruence arguments. Any
   future congruence attempt must name its non-chain mechanism first.
2. **T3's data** — the taut profile class through order 13 with
   through-sets, memberships, and residues (`E018/data/mod4_n*.json`);
   also: tautness is generic (\(\ge98.9\%\)) in the (5b) profile class,
   and no invisible-\(S\) (\(S\subseteq\mathbb P-2\)) taut member exists
   through order 13.
3. **T4's reading** — the live proof-side levers against case (5b) are
   now exactly: (i) the chain-cancellation tension (`L042`/W1-T14 —
   Minkowski additivity across cut vertices, a mechanism T1 does *not*
   kill because it is about set sums, not residues), and (ii) anything
   that makes power-freeness itself fight (the band-4 pencil `L033` is
   the model). The search ladder (`E018` at 16, then 17, then the Tier 4
   generator) is the decisive instrument in the meantime.
4. Petersen\(-e\) as the standing **calibration object** for case (5b):
   any proposed exclusion argument for the residual object must fail on
   Petersen\(-e\) unless it invokes power-freeness or a minimality
   lever — a one-graph sanity test for future sessions.

## Exit state

- Status: closed — kill condition fired (T3), mechanism absent (T1);
  route retired at any modulus (T4).
- Promoted records: offered to the ledger — the kill observation
  (computational row citing `E018`/`mod4.py`) and the retirement of the
  congruence-obstruction leg from `G015`'s live moves; T1 stays in this
  attempt (a support lemma, not a standalone ledger claim).
- Next action: none for this route. The proof side of case (5b) falls
  to the chain-cancellation tension; the search side to `E018` and its
  successors. Recorded in S020's checkpoint.
