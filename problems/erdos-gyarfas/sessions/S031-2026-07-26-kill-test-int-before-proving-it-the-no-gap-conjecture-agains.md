# S031 — Kill-test (INT) before proving it: the no-gap conjecture against calibration object #3 and the distance stratum

- Date: 2026-07-26
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1 (unchanged)
- Work / claim status: `active` / `open` (unchanged at close)
- Strongest established facts: `L049`/`L050` (interference-completeness ⟺
  vertex-tautness, audited `R002`); `L048`(iii) (the residual object's
  power-freeness *is* through-path arithmetic, unconditional);
  `L052`/`C048` ((F) decided empty on the Hamiltonian stratum at
  \(H\)-orders 16–30, audited `R003`); `L047`/`C040` (every counterexample
  has \(\ge22\) vertices); `C049` (\(\mathcal G\) empty at 21; every tight
  1-atom \(\ge23\)); `L053`–`L055` (no class-level Hamiltonian forcing; the
  bipartite exclusion dichotomy; the positive-savings theorem).
- Open obligations in scope: `G015` (exclude case (5b)), `G013`(a).
- Inherited next action: attack **(INT)** — \(S\supseteq[8,\max S]\) for a
  vertex-taut \(\{C_4,C_8\}\)-free exactly-two-profile pair — on the
  Hamiltonian stratum with `A026` T6's chord-exchange calculus, the
  order-unbounded successor architecture recorded by `A028` T9.
- Session goal: run the recorded route's omitted kill test, then either
  execute the route or re-aim.
- Falsifiable next move: test (INT) and (INT-14) against **every**
  calibration object, not only the on-disk profile objects `C050` used.

## Strategy audit

- **Why the inherited route might work.** (INT) is order-unbounded, has a
  validated engine (`A026` T6 reproduces the top of \(S\) down to 10 —
  including 14 — on all eight profile objects), and a survived kill test
  (`C050`: 24 recorded profile objects, zero violations, the constant 8
  pinned from both sides, a five-degree-2-vertex margin at 14). With (L-A)
  it gives (F-S) at every order.
- **Fastest way to falsify it.** Not span systems: the dossier's own
  binding kill discipline (`A021`, restated in `A026` plan step 2) says a
  candidate lemma is tested against every calibration object before it is
  worked on. S030 created Calibration object #3 in `A028` T1 and used it
  only against Hamiltonicity arguments. It satisfies every hypothesis of
  (INT). Cost of the check: minutes.
- **Mechanistically distinct alternative.** Prove (L-A) instead (a lower
  bound on \(\max S\)); or abandon the interpolation genre and re-derive
  `L046`'s order dichotomy from the current class floors, which is pure
  arithmetic and moves the only window any (F)-side result can live in.
- **Selected route and reason.** Run the kill test first. It is strictly
  cheaper than the recorded route, it is mandatory under the dossier's own
  discipline, and its negative outcome is a proved delimitation rather than
  a wasted session. It fired.
- **Pivot criterion (pre-registered).** If (INT) survives the calibration
  objects, execute the recorded chord-exchange attack unchanged. If it
  fails, test the natural repair (relativizing the threshold to \(\min S\))
  immediately rather than reporting only a negative, and do not propose a
  replacement conjecture without a kill test of its own.

## Work performed

Proof-side, plus one small verification experiment. Attempt `A029`,
experiment `E030`.

1. **T1 — the kill test.** `L053`'s object is \(H=F-ab\) with \(F\) cubic,
   3-connected, of girth \(\ge17\). `L053` already records that \(H\) is a
   profile pair, 2-connected, and \(\{C_4,C_8,C_{16}\}\)-free; 2-connected
   with \(\delta\ge2\) gives vertex-taut. The one new step: an \(a\)–\(b\)
   path of length \(\ell\) plus the deleted edge is a cycle of \(F\) of
   length \(\ell+1\), so \(\min S\ge16\). **The audit then improved this
   substantially** (`R004` F4): the attempt's claim that no such object exists
   below order 70 was **false**, and the reviewer supplied the **truncated
   Petersen graph** minus a link edge — order **30**, \(S=[9,26]\) — with a
   two-copy chain at order **59** giving \(S=[18,52]\). Both were rebuilt and
   verified here (`E030/truncation.py`). So the refutation lands **inside** the
   case-(5b) window, not asymptotically, and imports nothing.
2. **T2 — the repair, tested and killed.** The **triangle expansion** of a
   bipartite cubic 3-connected graph of girth \(\ge10\) (new import `X004`),
   minus an edge far from the triangle, is a *non-bipartite* vertex-taut
   \(\{C_4,C_8\}\)-free profile pair whose through-set has a parity hole at
   \(\min S+1\ge10\). Three-case connectivity proof; parity bookkeeping over
   \(k\in\{0,1,2\}\) triangle edges. **Verified end to end on an explicit
   graph** (`E030`): the cyclic Haar graph \(H(52;\{0,1,5\})\) — bipartite,
   cubic, order 104, girth 6, diameter 12, 3-connected by exhaustive cut
   enumeration — expanded at a vertex with \(\rho=6\); all of T2 (i)–(v)
   hold, with zero violations of the parity law over an exhaustive
   enumeration of short through-paths, and the claimed even holes 6, 8, 10
   all absent. That instance has girth 6, so it exercises the *mechanism*,
   not the class hypothesis — which is precisely what `X004` supplies.
3. **T3 — the genre.** Tabulated the three now-dead genres (congruence,
   membership, interpolation) and extracted the shared diagnosis. Derived the
   **conditional dyadic pinning**: any interpolation lemma plus `L042`'s
   forced memberships plus the poison condition gives
   \(2^j-2-c<\min S\le2^j\le\max S\le2^{j+1}-3\), i.e.
   \(\max S<2\min S+O(1)\) — `L031`/`L032`'s block-question constraint.
4. **T5 — the order dichotomy re-derived.** `A022` W1-T8's proof unchanged,
   its block-order input raised from 16 to 21 by `C039`/`C043`/S022/`C040`/
   `C049`.

## Results

**Refuted (proved negatives), offered to the ledger:**

- `L056` (T1, **proved**, audited `R004` — passed and strengthened):
  **(INT) and (INT-14) are false**, with explicit witnesses of orders **30**
  and **59** that import nothing, plus the asymptotic `L053` route.
- `L057` (T2, modulo `X004`; **audit FAIL twice, `R004` F3′ still open —
  NOT ESTABLISHED, recorded at `proposed`, not citable**): no relativized interpolation either. For every
  \(c\), \(S\supseteq[\min S+c,\max S]\) fails on a non-bipartite class
  member; the recorded pivot trigger ("a hole in \(S\) at a value \(\ge8\)")
  fires.
- `L058` (T5): **either \(H\) is 2-connected or \(n_0\ge42\)**, superseding
  `L046`'s constant 36.

**Provisional / conditional:**

- The dyadic pinning (T3(b)) — recorded as conditional structure, explicitly
  **not** progress, since its hypothesis is now known false at class
  strength. Its value is that it names the prize and a convergence with the
  block question that the portfolio had not recorded.

**Computational evidence:** `E030` part 1 — T2's five steps verified on an
explicit 106-vertex graph under both interpreters, deterministic, no external
data; a mechanism check, not a class witness (girth 6). `E030` part 2
(`truncation.py`) **is** a class witness: truncated Petersen minus a link
edge, verified cubic, 3-connected, \(\{C_4,C_8\}\)-free, 2-connected
exactly-two-profile with \(S=[9,26]\) by exhaustive path enumeration — this
is `L056`'s witness. Separately, the identity `L056` turns on — \(\min S=\mathrm{girth}-1\)
for \(F-ab\) — was reproduced on Petersen\(-e\) from a from-scratch
construction: \(S=\{4,5,7,8\}\), matching the dossier's recorded value, with
\(\min S=4=5-1\).

**Imported facts needing verification:** `X004` (bipartite cubic 3-connected
graphs of girth \(\ge10\), and of arbitrary girth), `reported-classical`,
used only inside a negative result. `L056`, the operative kill, uses no new
import.

## Failed routes and why

- **The inherited next action was not executed and is now moot.** Its
  target is false. The hand question it posed ("can a chord-minimal cover
  with all spans \(\ge4\) leave a gap above 8 in the reachable savings
  set?") has answer *yes* at class strength, exhibited without any span
  analysis.
- **The session's "no such object below order 70" claim was false** and is
  deleted (`R004` F4). It was a guess dressed as a bound: the cubic-minus-an-
  edge route does need girth \(\ge10\), but it is not the only route, and
  truncation reaches \(\min S=9\) at order 30. The effect is that the
  session's headline is **stronger** than it claimed, and that its own T4 move
  4 ("find such an object in-window") was answered by the auditor rather than
  left open.
- **T2 is the session's real failure.** Its numerics were wrong in three
  successive revisions (`R004` F2, then F11) and its parameter choices were
  made in the wrong order (F1); the named import witness was wrong (F3); and
  after all repairs the import still asserts 3-connectivity **with no source**
  (F3′, open). `L057` is recorded at `proposed` and is **not citable**. The
  first decisive failure is identifiable and worth stating: the construction
  was written before the quantity it depends on was identified, so each
  revision fixed a symptom (diameter \(\ge5\), then \(\ge g\), then
  \(\ge g/2+1\)) rather than the cause — that what places the far vertex is
  the **order**, via a girth ball count, and never the diameter.
- **The session's first guess about `L046` was wrong and is corrected in
  place.** `A029` T3(c) initially recorded that `L046`'s threshold was stale
  by four orders and that re-deriving it would *widen* the programme's
  reach. Checking `A022` W1-T8 showed 36 already consumes `C039`; the real
  movement comes from the bucket floors, and it raises the window's **bottom**
  as well as its top. Net effect: the `E028` ladder is ten rungs short of the
  window, not four. The correction runs against the finite-window route.

## Adversarial check

- Delegated fresh-context audit **`R004`** (`proof-reviewer`, independence
  mode `delegated-subagent`), scoped to T1, T2 and T3(b), given only
  `STATEMENT.md`, the review record and `A029` — no session narrative, no
  discovery reasoning. **Verdict: FAIL at lemma level** (2 critical, 2 major,
  4 minor, 2 notes). T1 passed and was strengthened by F4's order-30 object;
  T2 failed on F1/F2 (the hole was not proved to open; two false numeric
  steps) and F3 (the named `X004` witness provably fails, as does every cage);
  T3(b) passed up to side conditions. The reviewer then **re-audited the
  repairs** and raised two more majors: F11 (the diameter route is a non
  sequitur once \(ab\) is fixed — resolved, the requirement is now on the
  **order** via a tree ball bound, which is automatic at \(g=10\)) and
  **F3′, still open** — `X004`'s 3-connectivity clause has no source, so
  `L057` is **not established** and may not be cited. All findings are
  recorded in `reviews/R004-…md` with their resolution status. Net: `L056`
  proved and audited (and strengthened by the audit); `L058` proved in the
  `L046` frame; `L057` blocked.
- Before delegation: every hypothesis of (INT) matched field by field against
  `L053`'s recorded conclusion; T2's connectivity proved in all three cases
  including the degenerate branch that needs simplicity; T2 checked to
  produce **nothing** at the orders of the eight profile objects (as it must,
  since they satisfy (INT)); T3(b) checked for vacuity against those same
  objects (it must fail on them, and does, exactly because \(14\in S\)).
- The diagnosis of why `C050` survived was checked against `A028` T9's own
  table row by row rather than recomputed: no recorded profile object has
  \(\min S>8\), and none can exist below order 70 by the \((3,10)\)-cage
  bound.

## Canonical records changed

- [ ] `STATEMENT.md` (unchanged)
- [x] `STATE.md`
- [x] `CLAIMS.md`
- [x] `OBLIGATIONS.md`
- [ ] `PROOF.md` (unchanged — nothing integrated; no proved row bears on 0.1)
- [x] `DECISIONS.md`
- [x] `LOG.md`
- [x] `problem.json` and index
- [x] Session-scoped changes committed
- [x] Commit pushed to configured upstream

## Ending checkpoint

- **Current frontier.** Unchanged in floors: every counterexample has
  \(\ge22\) vertices (window \([22,24]\)); every \(\mathcal G\)-member
  \(\ge22\); every tight 1-atom \(\ge23\). Changed in architecture: the
  case-(5b) 2-connected window is \(n_0\in[23,41]\) (\(H\)-orders
  \([22,40]\)), and (F) is decided on the Hamiltonian stratum only at
  \(H\)-orders 16–30.
- **Remaining blockers.** (a) The non-Hamiltonian stratum is cleared at no
  order (`A028` T8's two gaps). (b) Ten ladder rungs separate the completed
  computation from the window's top, at 1.8–2.4× wall clock per rung. (c) No
  (F)-side lemma has ever consumed power-freeness above the girth or
  minimum-order minimality — which is exactly why all three genres died.
- **Recalibration decision: pivoted.** (INT) ∧ (L-A) is retired as the Tier-1
  architecture; it is recorded as **refuted**, not unproved. Tier 1's primary
  work returns to the non-Hamiltonian stratum (`A028` T8), with the honest
  acknowledgement that the whole (F) programme is finite-window.
- **Best live alternative or reframing.** Build the first (F)-side lemma that
  is *false* on Calibration object #3 — i.e. that consumes
  \(\mathbb P\cap\mathrm{Spec}(H)=\emptyset\) at a power **above** the girth,
  or consumes minimality. That is the only shape of statement that can be
  order-unbounded, and no proof step exists for it yet.
- **Pivot trigger.** (i) A power-free vertex-taut profile pair anywhere in
  \([22,40]\) — disproof-adjacent, report immediately. ~~(ii) a
  \(\{C_4,C_8\}\)-free profile pair of order \(\le35\) with
  \(\min S\ge9\)~~ — **answered by the audit**: truncated Petersen minus a
  link edge, order 30. The residual question, worth recording but not a
  trigger, is the smallest such order (\(>20\) by `C046`, \(\le30\)).
  (iii) Any lemma drafted for the non-Hamiltonian stratum that holds on
  Calibration object #3 — that is a soundness alarm on the draft, since the
  object satisfies every class-level hypothesis. (iv) A non-decomposable
  cycle in a vertex-taut pair remains a soundness alarm against `L049`, not a
  route pivot.
- **Open obligation carried out of this session.** `R004` F3′: `X004`'s
  3-connectivity clause is unsourced, so `L057` is blocked. Discharge it by
  sourcing bipartite cubic 3-connected graphs of fixed girth \(\ge10\) and
  unbounded order, or by replacing 3-connectivity with anything that delivers
  vertex-tautness — the only use T2 makes of it. Cheap, and it converts a
  blocked row into a proved one.
- **Best next action.** Close `A028` T8's two gaps for the non-Hamiltonian
  stratum: a component-atomic minimal-cover notion with a bound on the number
  of components, and an interval-disjoint family of positive-savings bridges
  (T5's savings are per component, the DP needs them per position). Kill
  condition: a power-free 2-connected profile pair with a longest through-path
  whose off-path components cannot be thinned to a bounded family.
- **Files a new session should read.** `STATEMENT.md`; then `A029` (this
  arc's attempt: T1/T2 the refutations, T3 the dead-genre diagnosis and the
  conditional dyadic pinning, T5 the re-derived dichotomy) and `R004`; then
  `A028` (T3–T7 the positive-savings package, T8 the two gaps) and `A027`
  T5; then `A022` W1-T8 (the order dichotomy whose constant T5 supersedes);
  then `CLAIMS.md` rows `L056`–`L058` with the dependency notes at the foot.

## Plain-language recap

The last session proposed a new central conjecture and called it the
programme's best hope: in these graphs, the set of achievable
route-lengths between the two special points has no holes above eight. If
true, the length fourteen would always be achievable, and fourteen is one of
the lengths that kills a candidate — settling the problematic case at every
size, with no search. It was tested against every such graph stored on disk
and passed twenty-four out of twenty-four.

This session tested it against one more object, and it is false.

The object is not new. The same previous session had *built* it, for a
different purpose: a large cubic graph with no short cycles at all, minus one
edge. It has exactly the right shape, obeys every structural rule, and is
two-connected — so it satisfies every hypothesis of the conjecture. But
because it has no short cycles, the two special points are far apart, and
**every** route between them is long. There is no route of length eight, and
none of length fourteen either. The conjecture, and the weaker version that
only asks about fourteen, are both simply false.

The stored evidence could not have caught this: every graph on disk has its
two special points close together. The survival of the test measured the size
of the collection, not the truth of the conjecture.

An independent referee, given only the claim and the proof, then made the
result considerably worse for the conjecture. This session had guessed that
any such graph must have around seventy vertices — comfortably outside the
range that matters. That guess was wrong, and the referee produced the graph:
take the Petersen graph, blow every vertex up into a small triangle, and
delete one connecting edge. Thirty vertices, every structural rule obeyed, and
the shortest route between its two special points has length nine — so length
eight is unreachable. **The conjecture fails inside the very size range the
search ladder is climbing**, not off at infinity. Joining two copies end to
end gives fifty-nine vertices with no route shorter than eighteen, which kills
the version that only asks about fourteen. Both were rebuilt and checked here.
The referee also broke the second half of the session's argument — the part
ruling out the weaker "no gaps above the shortest route" version — finding two
wrong numerical steps and a named example that provably does not do what it
was cited for. Those are repaired, but the repair has not itself been
refereed, so that half is recorded as provisional. The main conclusion does
not depend on it.

The obvious repair — ask only that there be no holes *above the shortest
route* rather than above eight — was tested too, and also fails. Taking a
two-colourable graph with no short cycles and replacing one vertex by a
triangle produces a graph of the right shape in which routes of one parity
are cheap and routes of the other parity are enormously expensive, so the
achievable lengths have a long gap immediately above the shortest one.

That makes three whole styles of argument now proved unable to settle this
case: remainder arithmetic, membership arithmetic, and now length
interpolation. They all fail for the same reason, and the reason is
diagnostic: each uses only *local* properties — how many edges at each
vertex, which short cycles are banned, that every vertex carries traffic —
and every one of those properties is shared by large graphs with no short
cycles, where the arithmetic the argument wants simply does not happen. The
two properties the dangerous object has that those decoys do not are that it
avoids powers of two *above* its own shortest cycle, and that it is the
smallest of its kind. Neither has ever been used.

A fourth finding is bookkeeping, and it also runs against us. The search
ladder's reach is bounded by a structural fact whose numerical threshold was
last computed three rounds of search results ago. Recomputing it moves the
range that needs covering from "sizes eighteen to thirty-five" to "sizes
twenty-three to forty-one". The ladder has reached thirty. So it is ten sizes
short of its own target, not four — and each further size costs roughly twice
the last.

## Proposed next step

Go back to the one part of the problematic case that no computation has ever
touched: the graphs where the longest route between the two special points
misses some vertices. Last session proved the key enabling fact there — every
detour hanging off the main route pays for itself — but two pieces are still
missing before that becomes a decision procedure: a way to reduce to a
bounded number of detours, and a way to use several detours at once rather
than one at a time. Closing both would make the problematic case fully
decided inside its size range instead of half-decided, which is the most any
finite-range route can deliver.

The move is small and falsifiable: it either produces the two missing pieces
or it produces a concrete detour system that cannot be reduced, which is
itself a named obstruction. Every lemma drafted along the way must first be
checked against the object that killed this session's conjecture — if the
lemma is still true there, it is too weak to be useful, and that check costs
nothing.

The alternative considered and deferred: hunt directly for a graph of the
right shape, at a size the searches can reach, whose two special points are
far apart. That would move this session's refutation from "true at large
size" to "true inside the range we care about", which would be more damaging
still — but it is a search, and the proof-side gap is the thing actually
blocking the programme.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: **7%**
- Previous estimate: 9% (S030); 9% (S029); 10% (S027)
- Reason for change: down two points, and the reasons are all negative
  information about routes rather than about the problem — sharpened by the
  audit, which showed the refutation is not confined to large order but lands
  at order 30, inside the window the ladder is climbing. S030 raised the
  architecture's standing on the strength of an order-unbounded successor;
  that successor is now **refuted**, not merely unproved, so the reason for
  the previous estimate's stability is withdrawn. Worse, the refutation is
  generic — it kills the whole interpolation genre, which is the third genre
  to die to the same diagnosis, and it makes the pattern legible: every
  proof-side idea this programme has generated is expressible in local,
  hereditary hypotheses, and every such idea is defeated by large-girth cubic
  graphs minus an edge. The one honest piece of good news, the re-derived
  order dichotomy, also runs the wrong way: it widens the window the ladder
  must cover from four remaining rungs to ten. Against that, nothing proved
  was lost — the floors, `L049`, `L052` and `L055` are untouched — and the
  session cost two theorems' worth of effort rather than a wasted route.
- Basis: most promising route is the non-Hamiltonian stratum's two gaps
  (`A028` T8), which has a proved engine (`L055`) and a bounded objective;
  strongest obstacle is now stated sharply — **no (F)-side lemma has ever
  consumed power-freeness above the girth or minimum-order minimality**, and
  the three dead genres show that nothing weaker can work; the evidence that
  informed the judgment is `L056` (a proved refutation of the recorded
  architecture from a recorded object), `L057` (the same for its repair), and
  `L058` (the window is wider at the top and higher at the bottom than
  recorded). Tier 0 still has no cheap move.

This is a subjective research outlook, not mathematical evidence or a
claim-status promotion.
