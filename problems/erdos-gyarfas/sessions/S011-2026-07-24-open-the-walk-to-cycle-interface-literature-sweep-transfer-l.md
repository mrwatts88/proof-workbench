# S011 — Open the walk-to-cycle interface: literature sweep, transfer-lemma formulation, and failure-first calibration

- Date: 2026-07-24
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1
- Work / claim status: `active` / `open`
- Strongest established facts: `L022` (every counterexample has \(\ge19\)
  vertices; extremal window \([19,24]\)); `L024` collision-wall theorem
  (reviewed, `R001`): every finite connected multigraph base with
  \(\delta\ge3\) has identity-voltage tailless nb closed walks at every
  length \(\equiv0\bmod4\) (every even length if non-bipartite) past
  \(4\ell^*+4R_B+8\), for every finite voltage group; saturation package
  `L008`–`L013` with delimitations `L014`–`L016`; imports `C004`–`C009`,
  `C012`–`C014`, `C017`.
- Open obligations in scope: `G007` (global mechanism, now concentrated
  in walk-to-cycle), `G002`/`G003`; `G004` peripheral.
- Inherited next action: three-step walk-to-cycle opening — literature
  sweep on cycle-length intervals and mod-\(k\) results at minimum
  degree 3; formulate the transfer lemma candidate; failure-first gap
  measurement on hostile instances. Kill test: unbounded walk/cycle
  separation in 2-connected min-degree-3 graphs retires bounded
  transfer.
- Session goal: know exactly what the literature already forces at
  minimum degree 3; state the transfer target precisely; find its
  cheapest counterexamples.
- Falsifiable next move: construct explicit 2-connected min-degree-3
  families with large even-spectrum gaps (candidate: chains of
  two-terminal gadgets), which either kill naive transfer immediately or
  fail in an instructive way.

## Strategy audit

- Why the inherited route might work: `L024`'s trivial-group reading is
  the project's sharpest quantitative fact; the literature has genuine
  cycle-interval technology at minimum degree 3 (Bondy–Vince pairs,
  Sudakov–Verstraëte sparse intervals, Gao–Huo–Liu–Ma consecutive
  lengths); powers of two are multiplicatively dense, so any forced even
  interval \([a,2a]\) settles the statement for the graph carrying it.
- Fastest way to falsify it: fired during formulation, before any
  computation. Closed chains ("necklaces") of two-terminal gadgets are
  2-connected, min degree 3, and have even-spectrum multiplicative gaps
  of unbounded ratio (gadget-internal lengths, then nothing until the
  global lengths \(\approx\) chain length). Since nb closed walks exist
  at every even length past a small threshold in these graphs (`L024`,
  trivial group), the recorded kill test fires by construction: **no
  unconditional bounded walk-to-cycle transfer exists for 2-connected
  min-degree-3 graphs.** This is a scoping death, not a route death:
  the transfer must consume the power-freeness hypothesis itself
  (contradiction shape), and the necklace analysis names the exact
  enemy — through-length rigidity of two-terminal gadgets modulo an odd
  number (see A011).
- Mechanistically distinct alternative or reframing: (a) attack
  interval-forcing directly without the walk framing (deferred in S010);
  (b) the new gadget-rigidity reframing: if a power-free two-terminal
  gadget with internal min degree 3 can have all terminal-to-terminal
  path lengths in one residue class mod an odd \(m\ge3\), the conjecture
  is **false** (necklace assembly); if not, the impossibility proof is
  the core transfer mechanism. This turns the vague "walk-to-cycle
  interface" into one sharp two-sided question.
- Selected route and reason: keep the inherited three steps, amended by
  the scoping death: (1) sweep the literature first (mandatory frontier
  discipline — the interval and mod-\(k\) results determine what is
  already forced and whether large girth is already settled); (2) write
  the transfer target in conditional/contradiction form and record the
  necklace lemma; (3) failure-first computation now targets the
  decision-relevant object — small two-terminal gadgets and their
  through-length residue structure — rather than generic walk/cycle gap
  tables.
- Pivot criterion: a swept result already forcing even intervals or
  power cycles in the bounded-girth min-degree-3 regime (import and
  rebase); or the gadget search finds a power-free mod-odd-rigid gadget
  (switch the dossier to disproof mode immediately); or formulation
  shows the walk layer adds nothing over direct interval-forcing (drop
  the framing, keep the target).

## Work performed

- Literature sweep with primary sources
  (`references/source-audit-2026-07-24-S011.md`): Bondy–Vince 1998 read in
  the published PDF (`C024` import: Theorems 1–2 plus the Figure-1 ring
  remark with its exact quoted spectrum); Gao–Huo–Liu–Ma (`C025`) and
  Carr's diameter-2 note (`C026`) imported at abstract strength;
  Sudakov–Verstraëte and Bai–Grzesik–Li–Prorok inspected and deliberately
  not imported (hypotheses far above degree 3); West's problem page and a
  targeted novelty search checked (no ring/gadget/two-terminal treatment
  of EGC found); Carr's May 2026 preprint identified as the already-imported
  `C004`–`C006` content.
- Opened attempt `A011` and proved the atom reduction (R1 ring-spectrum
  lemma, R2 dyadic placement, R3 2-atom ⇒ disproof, R4 1-atom ⇒ disproof,
  R5 contrapositive necessary conditions), promoted as `L025`.
- Built experiment `E010` (12 anchors, including exact reproduction of the
  published Bondy–Vince ring spectrum \(\{4,6,9,11,13,15\}\) by the
  internal ring builder — the same builder that would assemble a
  counterexample if an atom were found) and ran the exhaustive atom search
  at orders 6–15 plus the ratio-profile calibration at orders 12–13
  (`C027`).

## Results

- Proved claims: `L025` (atom reduction, hand proofs in `A011`).
- Refuted route: the *unconditional* walk-to-cycle bounded transfer died
  at formulation — the inherited kill test fires by construction
  (Bondy–Vince ring + `L024` walk intervals), no computation needed.
- Provisional insights: the conjecture is equivalent to a *pinching
  impossibility* on the disproof-relevant boundary — power-freeness must
  force terminal-path-length spread of ratio \(\ge2\) (spread-doubling)
  and forbid single-sub-cubic-vertex power-free graphs; the constant 2 is
  exactly the multiplicative gap of the powers of two. The distance
  between the 1998 Bondy–Vince figure and a disproof of 0.1 is precisely
  the power-freeness of one gadget.
- Computational evidence (`C027`): the atom class is **empty through
  order 15** (no power-free connected graph with at most two sub-cubic
  vertices exists at all); assembly counterexamples therefore need
  gadgets of order \(\ge16\) (1-atom doublings: order \(\ge32\)).
  Profile: pinched through-spread (ratio \(<2\), even a single
  through-length) occurs 22 times at order 12 and 116 at order 13 once
  power-freeness is dropped — and every occurrence contains a \(C_8\).
  Geometry permits the pinch; power-freeness is what blocks it.
- Imported facts needing verification: `C025`, `C026` are
  abstract-strength; full-text audits required before any proof step
  leans on them. `C026` is a preprint.

## Failed routes and why

The unconditional transfer lemma (walks at length \(L\) force cycles near
\(L\), for all 2-connected min-degree-3 graphs): false, witnessed by the
ring construction — spectra with unbounded-ratio gaps coexist with full
walk intervals. Preserved as the reason the interface must consume
power-freeness. Nothing else was attempted and abandoned.

## Adversarial check

- R1's cycle inventory (the only delicate proof) was double-checked via
  the closed-trail-in-\(C_L\) argument and then verified externally: the
  ring builder + spectrum detector reproduce Bondy–Vince's published
  Figure-1 spectrum exactly (E010 anchor A4); any error in the inventory
  (partial wraps, missed cycle types) would have shown up as a spectrum
  mismatch.
- R2's arithmetic was derived with an explicit effective bound on
  \(2^k\), not asymptotics.
- E010 re-verifies everything downstream of geng (degrees and \(C_4\)
  from the decoded adjacency; \(C_8\)/\(C_{16}\) by the `E004` anchored
  detector) and cross-checks DFS path minima against BFS distances;
  anchors include OEIS cubic counts and the internally verified `C016`
  class size 6059. Anchors were re-passed under PyPy 7.3.23 before the
  order-15 run (interpreter recorded per data file).
- Data provenance: every number in `E010`'s README and `C027` was copied
  from run outputs / JSON files after the runs completed (an extrapolated
  placeholder briefly written before the order-15 run finished was
  removed and replaced with the true counts, which differed).
- Coverage of the search class was argued, not assumed: atoms with both
  terminals of degree \(\ge3\) are excluded through order 18 by
  `L022`/`C023`; everything else has \(\le2\) sub-cubic vertices and is
  in the enumerated class.

## Canonical records changed

- [ ] `STATEMENT.md` (unchanged; statement version stays 0.1)
- [x] `STATE.md`
- [x] `CLAIMS.md` (`C024`–`C027`, `L025` + dependency notes)
- [x] `OBLIGATIONS.md` (`G013` opened; `G007` rescoped)
- [x] `PROOF.md` (outline: `L025`, `C024`–`C026`, `G013`)
- [x] `DECISIONS.md` (transfer retired; atom interface adopted)
- [x] `LOG.md`
- [x] `problem.json` and index
- [x] Session-scoped changes committed
- [x] Commit pushed to configured upstream

## Ending checkpoint

- Current frontier: finite exclusions unchanged (`L022`, counterexamples
  \(\ge19\)); the disproof side has a new finite interface — atoms — empty
  through order 15 (`C027`); the proof side has a new sharp necessary
  condition — spread-doubling (`L025`/`G013`) — replacing the retired
  unconditional transfer.
- Remaining blockers: `G002`, `G003`, `G007` (now concentrated in
  `G013`'s two-sided question); `G004` peripheral.
- Recalibration decision: pivoted at formulation time — the inherited
  three-step plan was kept but its transfer target was replaced by the
  conditional (power-freeness-consuming) form after the kill test fired
  by construction; the failure-first computation was redirected from
  generic gap tables to the decision-relevant atom search.
- Best live alternative or reframing: extend the atom census to order 16
  (multi-part PyPy, `E006`/S009 pattern); or attack the even-interval
  forcing directly under saturation constraints (`L008`–`L013`) without
  the gadget framing.
- Pivot trigger: an atom found at any order (switch the dossier to
  disproof mode; assemble and verify the ring; open a fresh reproduction
  audit per the counterexample protocol); or a proof of spread-doubling's
  bottom rungs revealing the general mechanism (promote it to the main
  attack); or a published treatment of ring/gadget assemblies surfacing
  in a deeper sweep (rebase novelty claims).
- Best next action: attack spread-doubling at its bottom rungs — prove
  that no power-free pinched gadget exists with \(s_{\min}\in\{1,2\}\)
  (the \(s_{\min}=2\) case is sharply structured: \(C_4\)-freeness forces
  a unique common neighbor of the terminals), using the ear/rerouting
  machinery (`L012`–`L013`) and the `E010` profile samples as guides —
  or find one, which would disprove statement 0.1.
- Files a new session should read: `STATE.md`, `A011`, `E010/README.md`,
  `CLAIMS.md` rows `C024`–`C027`/`L025`, `OBLIGATIONS.md` `G013`,
  `references/source-audit-2026-07-24-S011.md`, this session.

## Plain-language recap

Last session's plan was to bridge the project's big walk theorem to actual
cycles. The first discovery this session is that the naive bridge is
provably impossible — and the witness has been sitting in the literature
since 1998. Bondy and Vince, in the founding paper on cycle lengths in
degree-3 graphs, drew a "ring" of six-vertex gadgets whose cycle lengths
have enormous gaps, while our walk theorem says balanced round trips exist
at every scale in those same graphs. So round trips alone can never force
cycles; any bridge must use the special structure of a hypothetical
counterexample.

The second discovery is what that bridge must look like. Their ring
construction, examined closely, turns the conjecture into a question about
one finite object: a "gadget" — a small graph with two attachment points —
that (i) contains no cycle of power-of-two length inside itself, and (ii)
has all attachment-to-attachment path lengths confined to a narrow band
(the longest less than twice the shortest). If such a gadget exists, the
conjecture is false: stringing enough copies in a ring places every cycle
length in a gap between consecutive powers of two, and we proved this
assembly argument rigorously, verifying its machinery against the exact
spectrum Bondy and Vince published. If the conjecture is true, then
power-freeness must always force path lengths to spread by at least a
factor of two — a crisp phenomenon we named spread-doubling, whose factor
2 is exactly the spacing of the powers of two.

Third, we searched exhaustively for such a gadget through 15 vertices:
none exists — in fact nothing power-free exists at all in the relevant
class, across tens of millions of candidates. A control experiment shows
the narrow-band property itself is easy to achieve once you allow
power cycles — the graphs that achieve it always contain an 8-cycle. So
the tension is real: narrow path bands and power-freeness fight each
other, and the conjecture says power-freeness always wins. What remains
is to prove that fight's outcome in general — or find a larger gadget
that wins it for the other side.

## Proposed next step

Attack the simplest cases of the spread-doubling phenomenon by hand: show
that a power-free gadget whose two attachment points are adjacent or at
distance two can never have all its connecting paths in a narrow band
(equivalently, rule out the two most structured gadget shapes — the
distance-two case is tightly constrained because forbidding 4-cycles
leaves the attachment points exactly one common neighbor). Success would
give the first rung of the general lemma and likely reveal the rerouting
mechanism; failure in the form of an explicit gadget would disprove the
conjecture outright. Deferred alternative: extend the gadget search to 16
vertices with the existing multi-part pipeline (a compute-heavy but
routine census extension).

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 2%
- Previous estimate, if any: 2% (S010)
- Reason for change: none. The session replaced a vague interface
  (walk-to-cycle) with a sharp two-sided question (atoms /
  spread-doubling) and gave the disproof side its first finite,
  searchable objective since the lift program closed — real structural
  clarity, but no evidence the two-sided question is easier than the
  conjecture itself: the atom search is empty where it is cheap, and
  spread-doubling in general has the same global-forcing character as
  the main claim. Calibration rule: clarity is not proximity.
- Basis: most promising routes — spread-doubling's structured bottom
  rungs (analytic) and the order-16 atom frontier (computational);
  strongest obstacle — nothing yet forces cycle-length spread from
  power-freeness at any generality; evidence — `C024`'s ring, `L025`,
  `C027`'s emptiness-plus-profile data showing the pinch is geometric
  and the block is power-freeness.

This is a subjective research outlook, not mathematical evidence or a claim-status
promotion.
