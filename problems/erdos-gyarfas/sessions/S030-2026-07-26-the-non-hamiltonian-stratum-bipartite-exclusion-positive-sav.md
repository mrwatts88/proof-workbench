# S030 — the non-Hamiltonian stratum: bipartite exclusion, positive savings, and the bridge descent

- Date: 2026-07-26
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1, unchanged.
- Work / claim status: `active` / `open`, unchanged by this session.
- Strongest established facts in scope: `L049`/`L050` (interference-completeness
  ⟺ vertex-tautness), `L048`(iii) (the residual object's power-freeness is
  through-path arithmetic), `L052` (the chord-minimal descent), `C048` ((F)
  empty on the Hamiltonian stratum at orders 16–30), `C049` (the order-21 rung
  empty; 27/27 Hamiltonian), `C046`/`C047` (the census and its dissection).
- Open obligations in scope: `G015`.
- Inherited next action: `A027` T5 — extend the chord-minimal descent from
  chords to **bridges** on the non-Hamiltonian stratum.
- Session goal: that, plus the standing user steer for this session — bias to
  proof-side work; "more computation is getting ridiculous, we're just moving
  boundaries."
- Falsifiable next move: prove or refute that a zero-savings bridge can exist
  under the residual object's full hypotheses. If it can, the descent has no
  engine on this stratum.

## Strategy audit

**Inherited route (`A027` T5, bridges).** Why it might work: the descent's
coverage step survives verbatim off-path, and T5 had a provisional purchase
(zero-savings two-attachment components look bipartite). Fastest kill: exhibit a
zero-savings component consistent with all the hypotheses.

**The alternative the previous session named as best** — prove `C049`'s 27/27
Hamiltonicity pattern as a lemma, which would make `C048` a genuine closure of
case (5b) at orders 16–30. Fastest kill: find a non-Hamiltonian member of the
class. This is cheap to test and, if it dies, the inherited route stops being
optional. **Taken first, and it died** (T1).

**The reframing, and why this session went looking for one.** The user's steer
and the record agree: `R003` F4 had already recorded that above order 26 the
ladder proves class-emptiness rather than poison forcing. Reading `L046`
carefully, the (F) programme closes case (5b) only for \(n_0\le35\) — the
2-connectivity that the whole (F) frame assumes is only available below 36. So
even a *complete* (F) programme does not prove `G015`. That is a ceiling in the
architecture, not in the computation, and it had not been stated. The session
therefore also asked what an **order-unbounded** route would have to look like,
and found one already implicit in the data (T9).

**Selected route:** run the inherited bridge work to a verdict (it is the
proof-side move, and it is what a reframing would need anyway), take the cheap
kill test on the alternative first, and record the ceiling and its successor
target. **Tier served: Tier 1 (`G015`, case (5b)).**

**Pivot criterion, pre-registered:** if the savings theorem holds but the
descent still cannot be made minimal on this stratum, the route's deliverable is
a structure theorem rather than a decision procedure, and the session must say
so rather than present it as a closure. That is what happened (T8).

## Work performed

All of it is in `A028`; `E029` holds the one measurement.

1. **The alternative, killed (`A028` T1 → `L053`).** Two literature lookups —
   Haythorpe's non-Hamiltonian cubic graphs of arbitrarily large girth, and
   independently Kochol's large-girth snarks with the three-line internal proof
   that a Hamiltonian cubic graph is 3-edge-colourable — audited in
   `references/large-girth-non-hamiltonian-cubic-2026-07-26.md`. Deleting one
   edge from such a graph gives an exactly-two-profile, 2-connected,
   \(\{C_4,C_8,C_{16}\}\)-free pair with **no** Hamiltonian through-path.
2. **The bipartite transfer, with its hypothesis matched (`A028` T2 → `L054`).**
   The dichotomy, in three logical forms, with the difference between them
   recorded because it is easy to get wrong inside `G015`.
3. **The positive-savings theorem (`A028` T3–T7 → `L055`).** Two-attachment
   components via parity (vertex-tautness of the gadget from the Menger fan;
   `L035` T2; `L054`), three-or-more via the Y-identity
   \(\sigma(i,k)=\sigma(i,j)+\sigma(j,k)+2\beta\), which consumes maximality
   alone. Plus the bridge span law and the transported coverage step.
4. **The ceiling and its successor (`A028` T9).** (INT) formulated, and
   kill-tested in `E029` over data already on disk — no generation, no new
   class, no ladder rung.

## Results

### Proved

- **`L053`** — no class-level Hamiltonian forcing; calibration object #3.
- **`L054`** — the bipartite exclusion dichotomy.
- **`L055`** — the positive-savings theorem: **every** off-path component of a
  longest through-path admits a bridge with savings \(\ge1\) (\(\ge2\) with
  three or more attachments), unless 0.1 is false with an explicit witness. The
  obstruction `A027` T5 named — zero-savings bridges — **does not arise**, and
  `L052`(iii)'s reroute machinery transports from chords to bridges.

### Computational evidence

- **`C050`** (`E029`, six anchors under two interpreters, nothing generated):
  (INT) holds on all 24 recorded profile objects with \(S\) recomputed from
  graph6 — every hole in \(\{4,5,6\}\), none at 7 or above. Over `E027`'s
  9,061-row corpus the minimum degree-2 count admitting a hole is 4 for every
  value \(\le7\) and **5** at 8, so the conjecture's constant is the smallest
  the data permits; a hole at **14** needs degree-2 count \(\ge7\), five above
  the profile. New en route: a second non-interval profile object, at order 20
  (\(S=[3,19]\setminus\{4,5\}\)) — one order below where `S027` first saw one.

### Provisional / not proved

- **(INT)** and its operative weakening **(INT-14)** are conjectures with a
  survived kill test, recorded as such. They are not citable as support.
- The expectation that the *Hamiltonian* sub-class is also nonempty at large
  order (it needs Hamiltonian cubic graphs of girth \(\ge17\)) is flagged, not
  imported.

### What is explicitly **not** established

The non-Hamiltonian stratum is cleared at **no order**. `L055` removes an
obstruction; it does not finish the descent. `A028` T8 records the two gaps:
components are not thinnable edge by edge, so there is no component-atomic
minimal-cover notion with a bound on the number of components; and the savings
are per component rather than per position, while the DP needs an
interval-disjoint family.

## Failed routes and why

- **Promoting 27/27 to a lemma** — dead at class strength (`L053`). Any
  surviving form must consume power-freeness, the poison condition, minimality,
  or an order bound.
- **Smoothing induction on the number of off-path vertices.** Replacing a
  component by a path of length \(w\in S_K\) preserves \(\mathrm{Spec}\subseteq\)
  and \(S\subseteq\), i.e. every hypothesis except the degree profile — but the
  replacement path's interior has degree 2, so the object leaves the class.
  This is `C047`(c)'s subdivision phenomenon seen from the other side, and it is
  why the induction does not close. Recorded in `A028`'s failure analysis.

## Adversarial check

- The session's own premise was tested before being built on: the cheap kill of
  the recorded best alternative ran **first**.
- `L054`'s three logical forms were separated precisely because the dichotomy
  form is *not* a contradiction inside `G015`; a note to that effect is in
  `CLAIMS.md`'s dependency section so a later session cannot read the transfer
  as unconditional.
- `L055`'s two-attachment half was carried through **all three** boundary cases
  of `L035` T3's degree side condition, which fails in two of them.
- Every new lemma was checked against the calibration objects: the Y-identity
  must and does hold on calibration object #3 (maximality only); the parity half
  must and does fail there (it consumes power-freeness, which that object
  lacks); (INT) must and does fail on the corpus rows with \(\ge5\) degree-2
  vertices, and fails on no recorded profile object.
- `E029` recomputes \(S\) from graph6 rather than reading the `C043`/`C049`
  summaries, and its Petersen\(-e\) anchor is built from an explicit edge list
  inside the instrument, independent of the data layer. Both interpreters give
  identical output.
- The new claim rows were written with their scope limits in the row itself:
  `L053` is asymptotic and moves no floor; `L055` clears no order.

## Canonical records changed

- [ ] `STATEMENT.md`
- [x] `STATE.md`
- [x] `CLAIMS.md`
- [x] `OBLIGATIONS.md`
- [ ] `PROOF.md`
- [x] `DECISIONS.md`
- [x] `LOG.md`
- [x] `problem.json` and index
- [x] Session-scoped changes committed
- [x] Commit pushed to configured upstream

## Ending checkpoint

- Current frontier: (F) empty on the Hamiltonian stratum at orders 16–30; the
  \(\mathcal G\)-profile class empty at 18–21 (counterexamples \(\ge22\),
  \(\mathcal G\)-members \(\ge22\), tight 1-atoms \(\ge23\)); the
  non-Hamiltonian stratum has an engine (`L055`) but is cleared at no order;
  the (F) programme is now known to have a ceiling at order 36.
- Remaining blockers: `G015`(b) — and, above it, the architecture: case (5b) at
  \(n_0\ge36\) needs an order-unbounded argument, for which (INT) ∧ (L-A) is the
  recorded candidate.
- Recalibration decision: **pivoted**. The ladder is demoted from the proof-side
  route to a source of floors; (INT) ∧ (L-A) replaces it as the named
  architecture. The bridge descent stays live as the non-Hamiltonian half.
- Best live alternative or reframing: prove **(L-A)** instead — \(\max S\ge14\)
  for an in-window profile pair — which is the other half of the same
  architecture and is a *lower* bound on longest through-paths, a genuinely
  different genre from (INT)'s interpolation.
- Pivot trigger: a profile object, at any order, with a hole in \(S\) at a value
  \(\ge8\). That refutes (INT) outright and sends the architecture back to the
  window. (The previous saturation-form trigger is already retired; this is its
  successor and it is sharper.) Standing: a power-free vertex-taut
  (5b)-profile pair anywhere in the window is disproof-adjacent, and a
  non-decomposable cycle in a vertex-taut pair remains a soundness alarm
  against `L049`.
- Best next action: attack **(INT)** on the Hamiltonian stratum with `A026`
  T6's chord-exchange calculus — specifically, whether a chord-minimal cover of
  a Hamiltonian path with all spans \(\ge4\) can leave a gap above 8 in the
  reachable savings set. That is a hand question about span systems.
- Files a new session should read: `A028` (all of T1–T9), `E029/README.md`,
  then `A027` T5 and `A026` T6 for the engine, and `C050`/`L053`–`L055`.

## Plain-language recap

The previous session had ended with two candidate moves: attack the case no
computation has touched, or try to prove a striking pattern (twenty-seven out
of twenty-seven of the relevant graphs contain a route through every point).
This session did the cheap one first — and the pattern turned out **not** to be
a law. There are graphs of exactly the right shape, obeying every one of the
structural rules, with no such route. They are large, so the pattern is real at
the sizes we can search and false in general; what dies is the shortcut, not the
observation. So the untouched case genuinely has to be handled.

Then it was handled, in part. The sticking point was that a "detour" — a piece
of the graph hanging off the main route — could in principle be a pure
liability: it covers ground while shortening nothing, which is what made the
existing argument stall. Two independent arguments now show that cannot happen.
If the detour touches the main route in three or more places, a short
calculation with three legs of a Y shows one of its shortcuts must save at least
two steps — this uses nothing but the fact that the route was chosen as long as
possible. If it touches in exactly two places, then either it saves something,
or it is two-colourable in a very rigid way — and a two-colourable piece of this
kind would hand us an outright counterexample to the conjecture. So every detour
pays. The obstruction is gone; the machinery still needs one more piece before
it becomes a decision procedure, and that piece is named.

The third and probably most important thing is a piece of honest accounting.
The search ladder everyone has been climbing can only ever settle sizes below
thirty-six — not because the computer is slow, but because the structural fact
that sets up the whole question is only available below thirty-six. Above that,
the ladder says nothing, however far it goes. And a by-product of the first
result shows the ladder's recent rungs have been proving something that must
stop being true at some size. So the programme needed a route whose strength
does not depend on size at all.

There is one, and it was hiding in the data. Every one of these graphs, so far,
has the property that its set of achievable route-lengths has no holes above
eight — the lengths run in an unbroken block from eight up to the maximum. If
that is a theorem, then the length fourteen is always achievable, and fourteen
is exactly one of the lengths that kills a candidate. That would settle the case
at every size, with no search at all. The conjecture was tested against
everything on disk: it holds on all twenty-four graphs of the right shape whose
descriptions we store, their holes stopping at six; the threshold eight is
exactly the smallest number the data allows; and the nearest near-miss to the
crucial value fourteen needs five more low-degree vertices than the shape
permits. It is a conjecture, not a theorem — and there are nearly two thousand
graphs on disk that break it the moment you relax the shape, which is precisely
what any proof will have to use.

## Proposed next step

Try to prove the no-holes property, starting with the easier half: the graphs
that do have a route through every point. Concretely, take such a route and the
set of shortcut edges that must cover every position along it, and ask whether
the achievable savings can skip a value once every shortcut spans at least four
steps. If they cannot, the no-holes property follows on that half and the
crucial length fourteen is forced at every size — which would close the
remaining case outright rather than one size at a time. If they can, the example
that shows it is a new test object and the property has to be weakened to the
version that only asks about fourteen.

The alternative considered and deferred is the other half of the same plan:
prove that these graphs always have a route of length at least fourteen. It is a
different kind of statement — a lower bound rather than an interpolation — and
it is deferred because the no-holes half is the one with a validated engine
behind it and a sharply calibrated conjecture in front of it.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: **9%**
- Previous estimate: 9% (S029); 10% (S027)
- Reason for change: unchanged, but for two offsetting reasons rather than
  because nothing happened. Down: this session established that the route the
  last eight sessions have been extending has a **ceiling at order 36** and
  cannot prove the programme's own deliverable however far it is pushed, and it
  killed the shortcut that would have made the completed ladder mean more than
  it does. That is real negative information about the architecture, and it
  would have cost a percentage point on its own. Up: the same session removed
  the named obstruction on the untouched half with two clean order-unbounded
  lemmas, and it identified a successor architecture — (INT) ∧ (L-A) — that is
  order-unbounded, is already sharply calibrated against every object on
  record, and would close case (5b) at every order rather than in a window. A
  route with no ceiling, even a conjectural one, is worth about what the
  ceiling cost.
- Basis: most promising route is (INT) via the chord-exchange calculus;
  strongest obstacle is unchanged — nothing yet forces through-path lengths from
  below, which is both (L-A) and the reason (INT) is hard; the evidence that
  informed the judgment is `L053` (a proved delimitation), `L055` (a proved
  reduction), and `C050` (a survived kill test with measured margins), against
  the fact that no order of the non-Hamiltonian stratum is cleared and that even
  full success on case (5b) proves the **cubic reduction**, not statement 0.1.
