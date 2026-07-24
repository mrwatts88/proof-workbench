# S009 — Open the voltage-lift tool-building attempt: odd cyclic lifts, calibration spectra, and first kill-or-survive data

- Date: 2026-07-23
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1
- Work / claim status: `active` / `open`
- Strongest established facts: `L001`–`L018` (in particular `L008`–`L016`
  saturation package, `L018` order-\(\ge18\) bound); imports `C004`–`C018`
  (in particular `C017` Bensmail spectrum confinement needing cut vertices);
  the four verified order-24 extremal graphs from `E005`.
- Open obligations in scope: `G002`, `G003`, `G007` (global mechanism);
  `G004` (1997 body only, not workable today).
- Inherited next action: open the internal tool-building attempt on the
  falsification route — order-24 spectra as calibration, then voltage-graph
  lifts of small bases targeting a 2-connected minimum-degree-3 family whose
  cycle lengths avoid all powers of two, with kill conditions named before
  starting; proof-side alternative is a controlled-start
  consecutive-even-lengths lemma; capped support is the order-18 census.
- Session goal: actually open that attempt — formalize the lift mechanism
  precisely enough to prove a correspondence lemma, run the calibration,
  and get the first exhaustive kill-or-survive data on concrete bases.
- Falsifiable next move: exhaust all gauge-reduced voltage assignments over
  \(\mathbb{Z}_m\) (odd \(m\)) on the smallest 2-connected cubic bases and
  determine whether any lift dodges every power of two up to its order; a
  full sweep with zero survivors at every tested \((B,m)\) is the kill datum.

## Strategy audit

- Why the inherited route might work: over an odd-order cyclic voltage
  group, a power-of-two cycle in the lift cannot wrap (its wrap count would
  be an odd divisor of a power of two), so power cycles upstairs correspond
  exactly to power-length closed walks downstairs with zero net voltage —
  the entire infinite condition compresses into finitely many walk classes
  of the small base, each a hyperplane in the voltage space. Freeness
  becomes a finite, exhaustively checkable condition per \((B,m)\), and the
  verdict loop is instant against the validated `E004`/`E005` detectors.
- Fastest way to falsify it: a counting wall. Tailless non-backtracking
  closed walks of length \(L\) in a min-degree-3 base grow like \(2^L\)
  while the voltage group has only \(m\) classes; once \(2^L \gg m\),
  collisions force zero-voltage walks of length \(2L\) (pair a walk with
  the reverse of a distinct same-voltage walk). If those are generically
  realized as cycles, every cyclic lift dies at moderate powers. The sweep
  makes this quantitative immediately: if all assignments at all tested
  \(m\) die at length 16 or 32, the wall is real and the attempt pivots to
  proving it as an obstruction lemma (kill condition (a) of the plan).
- Mechanistically distinct alternative or reframing: proof-side
  controlled-start consecutive-even-lengths lemma at minimum degree 3
  (Bondy–Vince / Sudakov–Verstraëte style interval forcing) — deferred, not
  rejected: the lift attempt's failure data (which walk classes force) is
  direct input to what an interval lemma must exploit. Census-to-18 under
  PyPy stays capped support; it informs the extremal window, not the
  mechanism.
- Selected route and reason: the inherited voltage-lift attempt, unchanged.
  It was amended into place by the user's directive hours ago (S008), no
  new evidence has arrived since, it carries pre-named kill conditions,
  and both outcomes are informative — survivors are new record near-miss
  objects; a clean sweep converts directly into a provable obstruction
  target. Generate-and-verify with algebraic control is the only route on
  the board whose verdicts are cheap and exact today.
- Pivot criterion: kill condition (a) — a proved obstruction forcing a
  power-of-two balanced cycle in every admissible assignment — or (b) —
  loss of girth/spectrum control on the first concrete bases (all tested
  \((B,m)\) die and no structural lever emerges). Either sends the failure
  pattern to the proof-side interval lemma. A survivor at any order
  \(\ge 33\) that also dodges 32 (hence a counterexample if its order is
  \(\le 63\)) triggers immediate escalation: reproduction, then the
  mandatory counterexample review path.

**In-session continuation audit (added when A008 closed mid-session).**
After kill condition (a) fired, the user directed immediate continuation
rather than deferral to a new session. Before running the recorded
successor (odd-order non-abelian groups 21 and 27), the route was
re-audited: Feit–Thompson makes every odd-order group solvable, and the
solvable cascade (double commutators; power-twisted commutators via
exponent laws) predicts certificate death at \(\le32\) — so the
recorded targets could only serve as theory probes, and the decisive
experiment was the smallest cascade-immune group, the perfect \(A_5\).
The probes were kept (cheap, predictions pre-registered) and \(A_5\)
was added as the live test. Pivot condition: \(A_5\) surviving (→
counterexample path) or dying (→ identify the non-structural
obstruction). It died; the obstruction is the collision wall; the
program is retired for all groups. This audit and its outcome are
recorded in `A009`.

## Work performed

- Opened attempt `A008` (cyclic voltage lifts against the power spectrum)
  and proved in it the projection lemma `L019` (cycles upstairs project to
  tailless non-backtracking closed walks downstairs of the same length
  with zero net voltage; simplicity encoded by walk lengths 1–2), the
  gauge lemma `L020` (spanning-tree gauge fixing; assignment space
  \((\mathbb{Z}_m)^\mu\); net voltage = cycle-space pairing \(\nu\cdot
  x\)), and — after the computation exposed the mechanism — the
  commutator obstruction `L021` (four arc conditions under which
  \(W_1W_2\overline{W_1}\overline{W_2}\) is a tailless non-backtracking
  closed walk of length \(2(|W_1|+|W_2|)\) with zero net voltage over
  every abelian group), with concrete realizations at length 8
  (dumbbell), 16 (theta3, \(K_4\)), all cross-checked against DP
  witnesses.
- Built experiment `E007` (`lifts.py`): base multigraphs with arcs and
  tree gauge; exact DP for the walk-class sets \(V_L(B)\); hyperplane
  sieve over all assignments; explicit lift construction with `E004`
  detector verification, 2-connectivity, girth; truth census; calibration
  counter. Eight validation anchors (A1–A8), passing identically under
  CPython 3.14.2 and PyPy 7.3.23.
- Calibration (`C019`): the four verified order-24 extremal graphs carry
  \(315/330/207/228\) sixteen-cycles; every edge lies on \(\ge70\); no
  edge lies on all — the extremal \(C_{16}\) obstruction is massively
  redundant, so surgery at order 24 is hopeless and scale must come from
  construction, as the route assumed.
- Sieve (`C020`): theta3 and dumbbell exhausted for all odd \(m\le127\)
  (orders to 254, walk classes to length 128), \(K_4\) for odd
  \(m\le15\); zero survivors everywhere. The outputs revealed integer
  zero vectors at power lengths (dumbbell 8; theta3, \(K_4\), prism 16;
  \(K_{3,3}\) 32; bouquet 4), witnesses extracted and decoded; small
  even-\(m\) windows closed by explicit sieve, making the verdict cover
  every \(m\ge2\) for all six bases — the complete cycle-rank-2 base
  list plus \(K_4\), \(K_{3,3}\), prism.
- Truth census (`C021`): for every lift order in \([12,30]\), all
  assignments, both parities, every simple lift contains a \(C_4\),
  \(C_8\), or \(C_{16}\) by direct detector test — no counterexample
  exists in the cyclic-lift universe of these bases through order 30.
- Closed `A008` by its own pre-named kill condition (a), with the
  obstruction *proved* (`L021`), not merely observed; opened `G012` (the
  successor question: effective general abelian obstruction, or the
  non-abelian sieve where the commutator kill vanishes at its root).
- **Continued in-session at the user's direction (attempt `A009`,
  experiment `E008`):** re-audited the successor route before running
  it — Feit–Thompson makes all odd-order groups solvable, and the
  solvable cascade (double commutators; power-twisted commutators)
  predicts their certificate death, so the recorded odd-order targets
  became pre-registered theory probes and the perfect group \(A_5\)
  became the decisive test. Built the per-assignment group-table
  certificate engine (`nasieve.py`), anchored bidirectionally against
  the `E007` hyperplane engine (hit-for-hit agreement at every
  assignment and power length over cyclic groups at \(m\in\{5,7,9\}\)),
  with full group-axiom verification including \(O(n^3)\)
  associativity, \(A_5\) perfectness, and Heisenberg exponent checks.
- Ran the probes and the decisive test (`C022`): orders 21, 27
  (both groups), and \(A_5\) — every assignment on every tested base
  certificate-dead by length **16**, zero survivors (all 3600 per base
  over \(A_5\), certificate lengths through 64). Predictions confirmed
  at or before their bounds; \(A_5\)'s death matches the collision-wall
  prediction \(2^k\approx2\log_2\lvert\Gamma\rvert\). Closed `A009` by
  its kill trigger 5, identified the obstruction as group-size
  counting (not structure), refined `G012` into the collision-wall
  lemma, and shifted the recorded portfolio accordingly.
- Capped support: ran the `E006` order-18 census extension under PyPy
  (anchors re-passed under PyPy first; 48 geng parts, 8 workers,
  ~2h50m wall). Result: the connected \(C_4\)-free minimum-degree-3
  class at order 18 has \(834{,}711{,}846\) members and every one
  contains a \(C_8\) — zero \(\{C_4,C_8\}\)-free graphs, zero
  counterexamples (`C023`). With `A007`'s connectivity and collapse
  lemmas this proves `L022`: every counterexample has at least
  **nineteen** vertices; the extremal window for \(\{C_4,C_8\}\)-free
  minimum-degree-3 graphs narrows to \([19,24]\). Recorded in the
  `A007` addendum and the extended `E006` README. Order 19
  (\(\sim2\times10^{10}\) graphs) is past the pipeline without a
  compiled filter; the census cap stands.

## Results

- Proved claims: `L019`, `L020`, `L021` (hand proofs in `A008`;
  DP-cross-checked realizations; `L019`/`L020` group-agnostic per the
  `A009` re-walk); `L022` (counterexamples have \(\ge19\) vertices;
  computer-assisted, `A007` addendum).
- Computational evidence (exact, exhaustive in stated scope): `C019`
  (calibration), `C020` (cyclic certificate verdict, every \(m\ge2\),
  six bases), `C021` (truth census, orders 12–30), `C022` (non-abelian
  certificate verdict: orders 21, 27, 27, and \(A_5\), all
  assignments, all tested bases, dead by 16, zero survivors), `C023`
  (order-18 census: \(834{,}711{,}846\) graphs, all \(C_8\)-positive).
- Provisional insights (labeled as such in `A009`/`E008`): the
  collision wall — certificates die at
  \(2^k\approx2\log_2\lvert\Gamma\rvert\) for *every* finite group by
  same-voltage walk-pair composition, with only arc-diversity
  bookkeeping between the construction and a theorem; coset
  confinement cannot dodge it (undirectedness forces period \(\le2\));
  its proof-side reading hands `G007` forced identity-voltage closed
  walks at every even length past a log threshold.
- No change to the status of `C001`; no proof or disproof candidate
  exists.

## Failed routes and why

Two arms of the same program, killed at increasing depth:

1. The cyclic/abelian certificate program (primary route) failed by its
   own kill condition (a): the integer zero vector (a commutator word)
   sits in \(V_{2^k}(B)\) at small \(k\) for every tested base, so no
   abelian assignment of any modulus can ever be walk-certified free of
   that power length. Found within minutes of the first full sieve run,
   then proved structural (`L021`) rather than accidental.
2. The non-abelian successor failed by `A009`'s kill trigger 5: the
   solvable groups died on schedule (cascade predictions confirmed),
   and the perfect group \(A_5\) — immune to every structural channel —
   died at the same length 16, exposing the binding constraint as group
   size, not group structure. The wrong assumption, visible only in
   hindsight: that algebraic structure was what limited the tool; the
   collision wall (walk counts \(2^L\) versus \(\lvert\Gamma\rvert\)
   values) kills every group at logarithmic lengths while the lift
   needs linear survival.

Salvage: the verified two-engine machinery; the cascade word-analysis
as a predictive tool; the collision-wall lemma as the closing-theorem
target (`G012`); and the wall's forcing heuristic as proof-side input.

## Adversarial check

- The DP was validated against an independent brute-force enumerator on
  four bases at all lengths \(\le8\) (anchor A2) and against seven other
  anchors including two known graphs (Petersen as a dumbbell lift,
  \(K_{3,3}\) as a theta lift); all anchors pass under two independent
  interpreters (CPython, PyPy).
- The certificate/truth distinction is kept explicit everywhere: `C020`
  claims only that the certificate fails (sieve incompleteness noted in
  `E007`'s logical-scope section), while `C021` is detector ground truth
  but finite; neither is cited as evidence about `C001` beyond its
  scope.
- The L019 soundness direction is asserted at runtime on every verified
  survivor (none arose; the assertion also guards future reuse).
- Zero-vector witnesses were decoded by hand (the dumbbell witness is
  literally the L021 word \([\,b\,l_1\,\bar b,\ l_0\,]\)); the L021
  corollary words for \(K_4\) and theta3 were checked arc-by-arc against
  the four junction conditions in `A008`.
- Consistency with prior records was verified in the outputs: all
  sieve/truth rows at orders \(\le17\) empty (as `L017`/`L018` force);
  the 48 order-28 \(K_4\)-lifts avoiding \(C_4,C_8\) all contain
  \(C_{16}\) (as `C013` forces); every simple circulant \(\le30\)
  contains \(C_4\) (the commutator made concrete).
- The E008 engine was anchored *bidirectionally* against the
  independently validated E007 engine on cyclic groups: per-assignment
  DP hits equal the hyperplane predicate at every assignment and every
  power length (\(m\in\{5,7,9\}\), two bases) — two structurally
  different algorithms agreeing exactly. Group tables passed full
  axiom checks (including complete associativity) plus structure
  assertions (metabelian commutator subgroup of order 7; Heisenberg
  exponent 3; \(A_5\) perfect with orders \(\{1,2,3,5\}\)); the
  identical \(K_4\) first-hit tables for the two distinct order-27
  groups were noticed and checked against those structure assertions
  rather than assumed benign.
- The solvable-cascade predictions were registered in `A009` *before*
  the probe runs, so their confirmation is a genuine test of the word
  analysis, not a postdiction; the collision-wall mechanism is kept at
  provisional strength everywhere (`C022` cites it as recorded, not
  proved).
- Scope honesty: lift families overlap named graph families (cyclic Haar
  graphs, I-graphs/generalized Petersen); no novelty claim is made for
  any object or lemma here, and the A008 prior-art caveat stands.

## Canonical records changed

- [ ] `STATEMENT.md` (unchanged; statement version stays 0.1)
- [x] `STATE.md`
- [x] `CLAIMS.md` (`L019`–`L022`, `C019`–`C023`)
- [x] `OBLIGATIONS.md` (`G012` opened, then refined)
- [x] `PROOF.md` (dependency outline: `L022`, lift-lemma note; no candidate)
- [x] `DECISIONS.md` (two rows: abelian arm closed; program retired for all groups)
- [x] `LOG.md`
- [x] `problem.json` and index
- [x] Session-scoped changes committed
- [x] Commit pushed to configured upstream

## Ending checkpoint

- Current frontier: `L022` — counterexamples have \(\ge19\) vertices
  (order-18 census empty across \(834{,}711{,}846\) graphs); extremal
  window \([19,24]\). On the tool side, the entire voltage-certificate
  program is closed: the abelian arm by proof (`L021`, `C020`) plus
  truth census (`C021`), the non-abelian arm by exhaustive verdict
  (`C022`) with the obstruction identified as the group-size collision
  wall.
- Remaining blockers: `G002`, `G003`, `G007` (global mechanism); `G012`
  (collision-wall lemma, the program's closing theorem); `G004` (1997
  body only).
- Recalibration decision: pivoted twice on evidence within one session
  — cyclic arm retired by its pre-named kill condition; recorded
  odd-order successor re-audited (Feit–Thompson) into pre-registered
  probes plus the decisive \(A_5\) test; \(A_5\) died; the whole
  certificate program retired for all finite groups. New primary:
  prove the collision-wall lemma.
- Best live alternative or reframing: proof-side controlled-start
  consecutive-even-lengths lemma at minimum degree 3, now fed by the
  `L021` length formula and the wall heuristic.
- Pivot trigger: collision-wall lemma proved (fold into the note, move
  to the proof side); a value-confinement counterexample family
  (reopens construction with a new lever); or order-18 census
  survivors (new extremal objects take priority as test material).
- Best next action: attempt the collision-wall lemma (`G012`); the
  census support layer is complete at its cap.
- Files a new session should read: `STATE.md`, `A008`, `A009`,
  `E007/README.md`, `E008/README.md`, `CLAIMS.md` rows `L019`–`L021`
  and `C019`–`C022`, `OBLIGATIONS.md` `G012`, this session.

## Plain-language recap

For the first time the project tried to *build* a counterexample
instead of searching for one. The method — "lifting" a small template
graph through group arithmetic — was chosen because forbidden cycle
lengths in the big graph correspond to machine-checkable walk
conditions on the template. The session proved the lemmas that make
this rigorous, built two independent engines, and ran them
exhaustively. The method failed twice, each failure more informative
than the last. First: any lift built from *commutative* arithmetic is
blind to commutator round-trips, which land exactly on the forbidden
lengths 8, 16, 32 — proved for every template and every modulus, and
confirmed by explicitly building every such lift with 12–30 vertices
(each really contains a forbidden cycle). Second: rebuilding the
machine over *non-commutative* symmetry groups — ending with the
smallest "perfect" group, which is immune to every structural excuse
the first failure identified — changed nothing: every assignment still
died by length 16. The real reason emerged only then: it was never
about algebraic structure. A group with \(N\) elements can only tell
apart \(N\) walk-values while walks multiply exponentially with
length, so safety certificates die at lengths like \(2\log N\) — while
the graph would need them to survive to lengths comparable to its own
size. No group can cross that gap. This closes the entire
algebraic-certificate road to a counterexample. What survives: a
sharply posed unproved lemma (the "collision wall") whose proof would
finish this chapter rigorously — and whose content, read the other
way, is the strongest quantitative fact yet pointing *toward* the
conjecture: robustly connected sparse graphs cannot avoid
identity-balanced round trips at any even scale. Separately, the four
known 24-vertex near-miss graphs were fingerprinted: each contains
hundreds of 16-cycles threaded through every edge, so no small repair
of known graphs can ever work. And overnight, the exhaustive check of
all 18-vertex candidates finished empty — 834,711,846 graphs, every
one containing a forbidden cycle — so any counterexample now provably
needs at least 19 vertices, and the first graph dodging even the two
smallest forbidden lengths lives somewhere between 19 and 24 vertices.

## Proposed next step

Try to prove the collision-wall lemma: in any template of minimum
degree 3 with voltages in any group of size \(N\), balanced round
trips of every power-of-two length beyond roughly \(2\log N\) are
unavoidable. The construction is already explicit (pair up two walks
carrying the same group value and traverse one forward, the other
backward); what remains is the bookkeeping ensuring the two walks can
be joined without immediate turn-backs. Proving it would close the
lift chapter as a theorem rather than an observation, strengthen the
planned publication, and hand the proof side its sharpest quantitative
ingredient. If instead a structured family dodges the pairing argument,
that family would itself be a new construction lever — either outcome
moves the project. Deferred alternative: attack the "forced consecutive
even cycle lengths" lemma directly. The census layer is complete at its
cap (order 18 empty; order 19 would need a compiled filter and a
route-driven reason).

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 2%
- Previous estimate, if any: 2% (S008)
- Reason for change: none — the session added three proved lemmas, four
  exhaustive computational verdicts, and a complete two-arm closure of
  the construction program, but closing one's own tool is information
  gain, not proximity gain; the global-mechanism obstacles are
  untouched, and the falsification side now has *no* live construction
  tool, which cuts against disproof hopes roughly as much as the wall
  heuristic aids proof-side intuition.
- Basis: most promising route is the collision-wall lemma (small,
  concrete, falsifiable, double value: closes `G012`, feeds `G007`);
  strongest obstacle remains that nothing here or in the literature
  controls full cycle spectra of 2-connected minimum-degree-3 graphs
  at unbounded order — the wall forces balanced *walks*, and the gap
  from walks to *cycles* is exactly the conjecture's hard core.

This is a subjective research outlook, not mathematical evidence or a claim-status
promotion.
