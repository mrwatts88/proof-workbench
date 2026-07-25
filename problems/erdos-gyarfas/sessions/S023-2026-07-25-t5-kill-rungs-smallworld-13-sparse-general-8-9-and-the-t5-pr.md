# S023 — T5 kill rungs (smallworld 13, sparse general 8-9) and the T5 proof attempt

- Date: 2026-07-25
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1 (verbatim; no change contemplated).
- Work / claim status: `active` / `open`.
- Strongest established facts: `L041`/`L046` (case (5b) is the whole
  of `G015` below order 36, and its residual object is 2-connected
  there); `L048` + `C041`/`C042` (the interference calculus: all 553
  frontier blockers are two-through-path symmetric differences;
  completeness is empirically exactly vertex-tautness-shaped, necessity
  proved); `C043` + harvests (all eight profile objects in existence,
  orders 19–20, survive T5 on 4,661/4,661 cycles); `L047`/`C040`
  (every counterexample has \(\ge22\) vertices; window \([22,24]\));
  tight 1-atoms \(\ge22\), \(\mathcal G\)-members \(\ge21\).
- Open obligations in scope: `G015` (exclude case (5b)); `G013`(a).
- Inherited next action: (1) `smallworld 13` kill rung; (2) sparse
  general-graph probe at orders 8–9; (3) if T5 survives both, the T5
  proof attempt (clean-window reroute + minimal-choice exchange).
- Session goal: spend the two remaining cheap T5 kill rungs, then
  attempt the proof of T5.
- Falsifiable next move: `smallworld 13` — a single non-decomposable
  cycle in a vertex-taut member kills T5 as stated and names the
  missing hypothesis.

## Strategy audit

- Why the inherited route might work: T5 has survived every kill rung
  run so far (all eight profile objects; exhaustive in-class 10–12;
  exhaustive general 4–7 with zero side conditions), the two remaining
  cheap rungs are minutes each, and the named proof mechanism
  (reroute + exchange) has a concrete starting point with two named
  sub-obligations.
- Fastest way to falsify it: exactly the two rungs themselves — they
  are the falsification instrument (a non-decomposable cycle in any
  taut member ends T5 immediately).
- Mechanistically distinct alternative or reframing: (i) skip the
  rungs and go straight at the proof — rejected: the rungs are minutes,
  and a kill would save the whole proof effort and name the missing
  hypothesis; (ii) attack the forcing target (F) directly — rejected:
  (F) consumes T5 (`L048`(iii)); proving collision-forcing without
  knowing Spec = T1 wastes the calculus; (iii) Tier 3 ladder legs —
  excluded by the standing rule (run, never select). During the
  pre-run normalization of T5 a candidate proof architecture distinct
  from the recorded one emerged (prefix/suffix trimming of a path
  through a prescribed cycle edge, bypassing weaving entirely, with
  the block-chain characterization of tautness supplying the
  prescribed-edge path); the session will still run the rungs FIRST —
  if the architecture is wrong, the rungs are its cheapest refutation.
- Selected route and reason: the inherited route, tier 1 (`G015` case
  (5b) proof side), with the proof attempt upgraded to the
  trimming architecture. Highest expected information per hour in the
  dossier: either T5 dies cheaply or the program's central lemma gets
  a proof candidate.
- Pivot criterion: a non-decomposable cycle in a vertex-taut pair at
  either rung (kills T5 as stated → session pivots to naming the
  missing hypothesis and recalibrating the T5→(F) program); or the
  proof attempt stalls on a sub-obligation that resists both the
  trimming and the exchange mechanisms → record the obstruction and
  fall back to (F)-side evidence mining.

## Work performed

1. **Resume + strategy audit** (above): inherited route confirmed with
   the proof architecture upgraded to the trimming construction found
   during normalization; rungs ordered first as the cheapest
   refutation of that architecture.
2. **`E023` built** (driver `rungs.py` importing `E021/dissect.py`;
   all primitives imported, data writes redirected). Anchors re-passed
   before any extension: E021's 45-check suite, 45/45 under PyPy
   7.3.23 **and** CPython 3.14.2. New slice driver calibrated against
   `E021/tautgeneral.json` (exact match on all four aggregate keys)
   before first production use.
3. **Kill rung 1 run and survived** (`E023 smallworld13`, exhaustive
   in-class at order 13, class count = `A021`'s 10,966): all 10,853
   vertex-taut members pass on all 1,614,300 cycles; all 113 non-taut
   members fail — the `C042` biconditional is exact at order 13.
4. **Kill rung 2 run and survived** (`E023 tautslice`, general
   connected graphs, no degree/freeness conditions): order-8
   cyclomatic-\(\le5\) slice (25,907 taut pairs; 399,120 cycles),
   order-9 \(\le5\) and \(=6\) layers (130,842 + 224,320 taut pairs;
   2,131,695 + 7,115,669 cycles), order-10 \(\le4\) (120,252;
   1,193,874), order-11 \(\le3\) (39,360; 217,272) — **zero
   non-decomposable cycles anywhere**. The dense completion of order
   8 landed in-session (8,300 graphs, 192,188 taut pairs, 36,398,537
   cycles, zero failures, 1,590.9 s): with the 23 cycle-free trees,
   T5's conclusion is now verified **exhaustively on every graph of
   order \(\le8\), every vertex-taut pair, every cycle** (order-8
   totals: 218,095 taut pairs, 36,797,657 cycles).
5. **T5 proved** (`A024`): the trimming construction. T1 the taut
   block chain (tautness ⟺ the block–cut tree is a path with the
   terminals non-cut in the end blocks; splice lemma); T2 the fan
   corollary (Menger \(k=2\) imported with precise statement,
   `references/textbook-classics-2026-07-25.md`); T3 subdivision;
   T4 **Lemma A** (in a taut pair every cycle edge lies on a through
   path); T5 **the theorem** — for any cycle \(C\) and any edge
   \(pq\in C\), any through path \(R\ni pq\), trimmed at its first and
   last \(V(C)\)-hits and completed through the two arcs of \(C\),
   yields two distinct simple \(a\)–\(b\) paths with symmetric
   difference exactly \(C\), in trunk-identical arc form. The recorded
   weaving obstruction never arises: the trimmed middle is discarded.
   T6 corollaries: (a) every 2-connected graph is
   interference-complete for every vertex pair (subsumes the pinched
   100% census and `C041`'s 553/553); (b) for connected graphs with
   \(\delta\ge2\): interference-complete ⟺ vertex-taut (the `C042`
   biconditional is a theorem on its class); (c) the case-(5b)
   spectrum identity \(\mathrm{Spec}(B)=T_1\cup(S+2)\) is
   **unconditional** (`L048`(iii) upgraded); (d) scope honesty: T5
   produces no power-of-two cycle; (F) remains the open content.
6. **The proof mechanically verified per instance** (`E023
   constructive`): every step of the construction (Lemma-A witness,
   trimming invariants, simplicity, \(\triangle=C\), census
   membership) asserted for every cycle and **every cycle edge** of
   every vertex-taut pair over: all connected graphs of orders 4–7
   (3,727,132 edge instances), the order-8 and order-9 sparse slices
   (2,008,186 + 11,577,122), and the ten named objects — Petersen
   \(-e\), the order-14 exemplar, and **all eight profile objects**
   (4,661 cycles, the recorded S022 totals reproduced object by
   object; 66,038 edge instances). Zero failures.
7. **Adversarial review delegated and passed** (`R002`, created
   manually per the `R001` precedent since `proofctl.py review` gates
   on main-statement candidates): fresh-context `proof-reviewer`
   subagent (model: fable), independence mode `delegated-subagent`;
   prompt restricted to slug, record path, review type, and the
   standard starting instruction. **Verdict: PASS at lemma level — 0
   critical, 0 major, 2 minor (F1: the splice cited circularly in the
   T1 converse remark — substantively harmless, rescoped as a
   standalone chain-splice lemma; F2: the then-unlanded dense order-8
   run cited in T7 — repaired to its landed figures), 6 notes (F3–F8:
   scope clause, symmetric case, terminal corner of the fan, explicit
   \(a\ne b\), trunk-split definition, two block facts itemized).**
   All eight repaired in place in `A024` and the references note,
   each marked with its finding ID. The reviewer also re-ran every
   recorded `E023` command with writes redirected outside the
   repository (all aggregates reproduced) and re-verified
   T5/Lemma A/the biconditional with a fully independent
   implementation — own g6 parser, own path/cycle enumeration, no
   shared code — on all labelled graphs through order 6 (3.2M cycle
   instances) and the ten named objects: zero failures. One recorded
   independence exception: the candidate lives in `A024`, so that one
   attempt file was read as directed by the record's target
   identification; no other attempts, sessions, or reviews before the
   verdict.
8. **Ledger promotion** (post-verdict): `L049` (T5 + trunk-identical
   arc form + prescribed-edge freedom + Lemma A; \(a\ne b\) explicit
   per F6), `L050` (the \(\delta\ge2\) biconditional), `C044` (the
   E023 kill-rung + constructive data) added; `C042` updated (rungs
   spent; superseded by the theorems), `L048` updated ((iii)
   unconditional, trunk-split defined per F7); `G015`/`G013`(a)
   rewritten around the (F) program; `PROOF.md` dependency outline +
   gaps updated; `DECISIONS.md` row; `LOG.md` entry;
   `STATE.md` rewritten; `problem.json`/index; `PROJECT_STATE.md`.
9. **Tier 3 background leg launched at close** (`E024`): the
   order-21 \(\mathcal G\)-profile rung through `E022/ladder.py`'s
   `load_scan` (E019 instrument, DATA redirected to `E024/data`;
   neither E019 nor E022 written). Anchors gate re-passed through the
   same import path (146 checks, 3.6 s) before production; 16 parts
   `--verify-all` on 8 workers, \(\approx\)21 h projected. **Running
   at close; excluded from every ledger; not citable until a later
   session harvests it** (named follow-up).

## Results

- **Proved and promoted (audited `R002`: PASS, 0 critical / 0
  major):** `L049` — T5, vertex-taut ⟹ interference-complete, with
  trunk-identical arc form, prescribed-edge freedom, and Lemma A;
  `L050` — on connected \(\delta\ge2\) graphs, interference-complete
  ⟺ vertex-taut (plus: every 2-connected graph is
  interference-complete for every pair); the `L048`(iii) upgrade —
  the case-(5b) spectrum identity \(\mathrm{Spec}(B)=T_1\cup(S+2)\)
  is unconditional, every element a trunk-split pair value.
- **Computational evidence (exact, exhaustive in stated scopes,
  `E023`):** both pre-registered kill rungs survived; biconditional
  exact at order 13; constructive verification all-pass everywhere
  including the eight profile objects.
- **Imported:** Menger \(k=2\)/Whitney and the block-structure facts
  B1–B3, precise statements and sources in
  `references/textbook-classics-2026-07-25.md`.
- **Provisional:** nothing in this session touches (F); T5 makes (F)
  literally equivalent to "no power-free vertex-taut (5b)-profile
  object in the window", now expressible entirely as through-path
  arithmetic.

## Failed routes and why

None died. The `A023` reroute/exchange plan was superseded, not
refuted: its two named sub-obligations were resolved (essentiality
proved as Lemma A; weaving control shown unnecessary by trimming). If
`R002` fails the proof, the reroute/exchange plan is the recorded
fallback.

## Adversarial check

- The rungs were run **before** the proof was written up, per the
  pre-registered order; any error in the architecture had 12.7M new
  cycle instances to fail on and did not.
- The proof was then re-executed mechanically step by step on every
  instance in scope (`constructive`), including the census-membership
  cross-check tying the construction to the recorded predicate
  semantics, and on the case-(5b)-adjacent objects the theorem exists
  to serve.
- The intricate deductions (T1's tree argument, T6(b)'s case split)
  were re-derived once more against the write-up before delegation;
  the review (`R002`) is the independent pass, delegated to a fresh
  context with a minimal prompt.
- Numbers quoted in `A024`/`E023` were corrected to the actual run
  outputs where the first draft had projected them; the dense order-8
  leg was marked non-citable until it landed and its recorded figures
  are the actual outputs (the pre-run projections were discarded).

## Canonical records changed

- [x] `STATEMENT.md` — unchanged (no statement change; checkbox
  recorded as reviewed-not-needed)
- [x] `STATE.md`
- [x] `CLAIMS.md`
- [x] `OBLIGATIONS.md`
- [x] `PROOF.md`
- [x] `DECISIONS.md`
- [x] `LOG.md`
- [x] `problem.json` and index
- [x] Session-scoped changes committed
- [x] Commit pushed to configured upstream

## Ending checkpoint

- Current frontier: T5 is a theorem (`L049`, audited `R002`); the
  case-(5b) residual object's power-freeness is unconditionally
  through-path arithmetic (`L048`(iii)); **(F) ⟺ case (5b) empty
  below 36** — the whole proof side of `G015` there. Floors: every
  counterexample \(\ge22\) (window \([22,24]\)); tight 1-atoms
  \(\ge22\); \(\mathcal G\)-members \(\ge21\) (order 21 in flight,
  `E024`).
- Remaining blockers: (F) has no proof step — no mechanism is even
  named yet; Tier 0's global forcing question untouched; the
  order-21 rung unharvested.
- Recalibration decision: **continued and advanced** — the inherited
  route was followed exactly (rungs first), and its proof phase
  landed by a better mechanism than the recorded plan (trimming
  instead of reroute/exchange); the recorded plan is retired as
  superseded, not falsified.
- Best live alternative or reframing: if the (F) realization tables
  show no membership pattern, redirect (F) to window/order
  arithmetic (the object's order \(\in[18,35]\) bounds \(S\) and the
  trunk lengths — a finite-geometry angle); the `C038` block-rung
  and the long-link descent stay live behind it.
- Pivot trigger: a power-free vertex-taut (5b)-profile pair anywhere
  in the window (defeats (F) as stated, disproof-adjacent); an
  \(S\)-satisfying order-21 profile hit (immediate disproof); a
  non-decomposable cycle in a taut pair is now a **soundness alarm**
  on `L049`/`R002`, not a pivot.
- Best next action: the (F) opening probe — the power-collision
  realization tables of the ten named objects (as recorded in
  `problem.json`/`STATE.md`); harvest `E024` first if landed.
- Files a new session should read: `STATE.md` (resume list), `A024`,
  `R002`, `A023` (T6: the (F) target and calibration), `E023`/`E024`
  READMEs, `CLAIMS.md` rows `L049`/`L050`/`C044`/`L048`/`C042`.

## Plain-language recap

The project is trying to settle a 1990s conjecture: every network in
which each node has at least three connections must contain a closed
loop whose length is exactly a power of two (4, 8, 16, ...). The
programme's centerpiece target is a reduction theorem — "if the
conjecture holds for perfectly 3-regular networks, it holds for all
of them" — and after three weeks of work that reduction hinges on
ruling out one last dangerous configuration: a network with a single
weak spot (one node of degree two) and no power-of-two loop.

Earlier sessions discovered a striking empirical law about the graphs
closest to that dangerous shape: every loop that "blocks" them (the
8-loop or 16-loop that disqualifies them) is an interference pattern
— the overlay of two routes running between the two ends of the weak
spot. This session turned that law into a proven theorem. First, the
two remaining cheap attempts to break it were run: every candidate
graph of the right shape with 13 nodes, and every graph whatsoever
with up to 8 nodes — tens of millions of loops, not one exception.
Then a short proof was found, and it is simpler than anyone planned:
to realize any loop as an interference pattern, route a path through
one chosen edge of the loop, throw away the path's middle (keeping
only the piece before it first touches the loop and the piece after
it last leaves), and close the two kept ends around the loop's two
sides. Everything difficult about the old plan lived in the
discarded middle. A separate, isolated referee — deliberately given
none of the discovery reasoning — attacked the proof, rebuilt every
computation from scratch in its own code, found only cosmetic
issues, and passed it; the fixes are in.

Why it matters: the dangerous configuration is forced to have the
"every node carries end-to-end traffic" property the theorem needs,
so its defining no-power-loop property is now, provably, pure
arithmetic of its own internal route lengths. Two earlier impossibility
theorems showed remainder arithmetic and membership arithmetic can
never finish the job; route-length arithmetic is exactly the kind of
argument they left alive, and it is now unconditionally available.
What remains of this branch is a single question, the forcing
question: do the route lengths this configuration is *forced* to
have always collide into a power-of-two loop when the network has
fewer than 36 nodes? A yes settles the dangerous case below 36 and
proves the reduction there. Overnight, the search machine is also
grinding through all candidate shapes with 21 nodes — each find
would be both a test object and, if it passes one extra arithmetic
condition, an outright counterexample to the conjecture.

## Proposed next step

Build the collision tables: for the ten concrete graphs closest to
the dangerous configuration (the eight found by the searches plus
the two standing calibration graphs), list every way their
power-length loops arise as an overlay of two routes — which pairs
of route lengths, sharing how much. The question the tables answer:
do the *forced* route lengths (the memberships every dangerous
configuration must have) show up as the collision partners in a
regular, provable pattern? If yes, that pattern is the candidate
mechanism for the forcing question and the next proof attempt
starts there; if no, the forcing question gets attacked through
size bounds instead. Cheap, decisive either way, and calibrated:
any claimed mechanism must fail on the two calibration graphs
(which satisfy all the forced arithmetic but are not
counterexamples) unless it genuinely uses the no-power-loop
property. Also: harvest the overnight 21-node search first if it
has landed. Deferred alternative: going straight at the size-bound
version of the forcing question without the tables — rejected
because the tables are hours of work and would shape (or kill) that
attack too.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 8%
- Previous estimate, if any: 7% (S022)
- Reason for change: the program's gate lemma stopped being a
  conjecture — proved, audited, and mechanically verified on every
  instance in reach, with the two pre-registered falsification runs
  surviving first. The case-(5b) object's power-freeness is now
  unconditionally through-path arithmetic — the one genre of
  argument the two recorded impossibility theorems left alive — and
  the proof's machinery (block chain, trunk-split normal form)
  carries into the (F) attack.
- Basis: most promising route — the (F) program on the \([18,35]\)
  window, now the entire proof side of case (5b) below 36, with ten
  concrete realization data points and a named first probe.
  Strongest obstacle — (F) is *equivalent* to the emptiness being
  sought: T5 supplies the language, not the forcing, and nothing yet
  makes power-freeness itself fight; Tier 0 is untouched, and the
  deliverable is still the cubic reduction, not statement 0.1. One
  point up for converting the route's foundation from conjecture to
  audited theorem with zero negative surprises en route.
