# A018 — 1-atom completeness and the repair of the cubic reduction

- Date opened: 2026-07-24
- Problem: `P-002`
- Status: active
- Portfolio role: audit (of the dossier's own architecture) + repair

## Intended mechanism

The user asked why sixteen sessions of strategy audits have deferred the
1-atom question (`G013`(a)) while repeatedly recording it as "the only
sub-question with direct proof-side yield". The obvious readings are
psychological — it has no cheap decisive search, so it loses every audit
that ranks routes by falsifiability per hour. This attempt tests a
mathematical reading instead: **that the 1-atom question is not a
sub-question at all**, but a restatement of statement 0.1.

The test is one construction. `L026` (rung completeness) already showed
that a two-terminal rung can be conjecture-complete because a
counterexample can be *hidden* inside it — two disjoint copies behind a
bridge. The same move has never been tried on the one-terminal object.
It is much cheaper there: a pendant vertex is invisible to the cycle
spectrum.

## Entry assumptions

Statement 0.1 exactly as in `STATEMENT.md`. Definitions D-A1–D-A5
(`A011`), in particular D-A4 verbatim: *a 1-atom is a finite simple
connected power-free graph with exactly one vertex of degree less than 3,
that vertex having degree 1 or 2 and all others degree \(\ge3\)*.
`L025` R4 and `L029`/`A012` T4 are consumed at their recorded strength
and then audited.

## Targeted obligations

- `G013`(a): the 1-atom question — its status as a sub-question.
- `G007`: what the assembly programme can deliver on the proof side.

## Plan and decisive tests

1. Decisive test (one line): is a counterexample plus a pendant vertex a
   1-atom under D-A4? If yes, the two questions are equivalent and every
   "modulo 1-atoms" statement in the dossier must be re-read.
2. If yes, locate the exact place where the recorded reduction survives —
   which degree of exceptional vertex `A012` T4's proof actually produces —
   and restate the reduction there.
3. Kill condition for the repair: if T4's proof can produce a degree-1
   exceptional vertex, no non-vacuous restatement exists and the cubic
   reduction must be abandoned as an internal route.

## Deductions

### T1 (1-atom completeness) — proved

**Claim.** A 1-atom (D-A4) exists **iff** a counterexample to statement 0.1
exists. Consequently "no 1-atom exists" is *equivalent* to statement 0.1,
and the unrestricted 1-atom question is conjecture-complete.

*Proof.* (⇐) `L025` R4: a 1-atom yields a counterexample by edge-doubling
(exceptional degree 2) or triangle assembly (exceptional degree 1).

(⇒) Let \(G\) be a counterexample. Some connected component of \(G\) is
again a counterexample (minimum degree and power-freeness are inherited),
so assume \(G\) connected. Let \(v\in V(G)\) and let \(B=G+p\) where \(p\)
is a new vertex adjacent exactly to \(v\). Then \(B\) is finite, simple and
connected; \(p\) lies on no cycle, so
\(\mathrm{Spec}(B)=\mathrm{Spec}(G)\) is power-free; \(\deg_B(p)=1\),
\(\deg_B(v)=\deg_G(v)+1\ge4\), and every other degree is unchanged and
\(\ge3\). So \(B\) has exactly one vertex of degree \(<3\), of degree 1:
a 1-atom. ∎

*Remark.* This is the one-terminal analogue of `L026`'s hiding
constructions, and cheaper: a pendant is spectrum-invisible, so no
scaffold is needed.

### T2 (what `A012` T4 actually proves) — proved, restatement

Call a 1-atom **tight** if its exceptional vertex has degree exactly 2.

**Claim.** If no *tight* 1-atom exists, then every counterexample of
minimum order (then minimum size) is cubic. Hence statement 0.1 holds
**iff** no cubic counterexample and no tight 1-atom exist.

*Proof.* Verbatim `A012` T4. Its only use of the hypothesis is: from a
minimum counterexample \(G\) with \(\deg(x)\ge4\) and a neighbour \(y\) of
degree 3, the graph \(G-xy\) (or the component of \(y\) in it, when \(xy\)
is a bridge) is connected, power-free, and has exactly one sub-cubic
vertex, namely \(y\), **of degree 2** — a tight 1-atom. The second branch
of T4 (all neighbours of \(x\) of degree \(\ge4\)) uses no 1-atom at all.
∎

So T4's hypothesis can be weakened to tightness, and must be: by T1 the
hypothesis as recorded is equivalent to statement 0.1 itself, i.e. `L029`
as stated is a true but **vacuous** implication, and its recorded reading
("modulo the 1-atom question, 0.1 reduces to cubic graphs") is empty,
because the modulus is the whole conjecture.

### T3 (tightness is a proper restriction) — proved, with an open gap named

**Claim.** "No tight 1-atom exists" is implied by statement 0.1 but is not
known to imply it; in particular T2's reduction is not vacuous.

*Proof of the implication.* A tight 1-atom yields a counterexample
(`L025` R4, degree-2 case), so 0.1 forbids tight 1-atoms.

*Why the converse is not available.* The construction of T1 produces an
exceptional vertex of degree **1**, never 2, and no route in the dossier
converts a counterexample into a tight 1-atom when the counterexample is
cubic: deleting an edge of a cubic graph leaves two sub-cubic vertices, and
subdividing shifts the lengths of every cycle through that edge, so
power-freeness is not preserved. Hence for all we know the tight 1-atom
question is strictly weaker than 0.1 — which is exactly what makes T2 a
usable reduction. ∎

**Gap found in `A012` Remark T4.1.** That remark claims that in a
minimum-order 1-atom the exceptional vertex has degree 2. Its argument
deletes a degree-1 exceptional vertex \(u\) and splits on \(B-u\): either
\(B-u\) is a smaller 1-atom, or \(B-u\) has minimum degree \(\ge3\) and is
power-free, i.e. is a counterexample — and it then asserts a contradiction
"by deleting one further edge as in T4, or directly as a counterexample".
Neither branch closes when \(B-u\) is **cubic**: T4's edge deletion needs a
vertex of degree \(\ge4\), and "directly as a counterexample" only
contradicts 0.1, which is not an available hypothesis inside a claim about
minimum-order 1-atoms. So Remark T4.1 is **unproved as stated**; it would
follow if a non-cubic counterexample existed, which is what the whole
programme is trying to decide. Recorded as a defect, not repaired here.

### T4 (consequences for the programme's ceiling) — recorded

`A016` M6 stated the ceiling as: closing every assembly channel *plus* the
1-atom question yields the cubic reduction, not 0.1, and that "of the two,
only the 1-atom question has direct proof-side yield". Under T1 that
reading is circular: one of the two halves *is* 0.1, so the conjunction is
0.1 and the "ceiling" is a tautology rather than a ceiling. The corrected,
non-circular statement is:

> Closing every assembly channel and proving that **no tight 1-atom
> exists** yields exactly the cubic reduction — statement 0.1 restricted
> to cubic graphs — and nothing more.

The programme's honest proof-side deliverable is therefore the **cubic
reduction**, and its price is the *tight* 1-atom question, not the 1-atom
question.

## Failure analysis

Not a failed route; a defect found in the dossier's own architecture, in
the direction that removes an illusory target. Root cause: D-A4 was written
to make `L025` R4's two assembly constructions (doubling at degree 2,
triangle at degree 1) both expressible, and no later session asked whether
the degree-1 case trivialises the resulting question. Every subsequent
record inherited "1-atom" as a single object. The same oversight explains
why sixteen strategy audits deferred it: there was no lever because there
was no sub-question — a fact that was mathematical, not psychological, all
along.

## Salvageable results

T1 and T2 stand. The tight 1-atom question is a genuine, strictly-weaker
sub-question and is the correct target; it inherits every search already
run (`C027`: no tight 1-atom of order \(\le15\), since the `E010` stream
covers the one-sub-cubic-vertex profile; `C034`: no bipartite tight 1-atom
of order \(\le21\)). `A012` T4's proof is untouched and now carries a
non-vacuous hypothesis. Remark T4.1 is demoted to an open question.

## Exit state

- Status: complete for its stated scope
- Promoted records: `L036` (T1–T3); `L029` restated with tightness;
  corrective notes on `A016` M6 and `A012` Remark T4.1; `G013`(a)
  rewritten; `G015` opened (the cubic reduction as a named deliverable
  with two independent routes).
- Next action: attack the cubic reduction — route R1, no tight 1-atom
  exists; or route R2, strengthen the imported \(4/7\) cubic-density bound
  on minimal counterexamples (`C006`) to 1. Neither route passes through
  the conjecture-complete object.
