# S012 — Bottom-rung audit fires: rung completeness, the lobe decomposition, and taut bottom rungs

- Date: 2026-07-24
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1
- Work / claim status: `active` / `open`
- Strongest established facts: `L022` (counterexamples \(\ge19\)
  vertices); `L023`–`L024` collision-wall theorem (reviewed `R001`);
  `L025` atom reduction with `C027` (atom class empty through order 15);
  imports `C024`–`C026`.
- Open obligations in scope: `G013` (atoms / spread-doubling), `G007`,
  `G002`/`G003`; `G004` peripheral.
- Inherited next action: prove that no power-free pinched gadget exists
  with \(s_{\min}\in\{1,2\}\) — "the \(s_{\min}=2\) case is sharply
  structured" — using ear/rerouting machinery and E010 profile samples;
  or exhibit such a gadget (disproof via `L025`).
- Session goal: execute the bottom-rung attack, or expose why it cannot
  work and replace it with the corrected form.
- Falsifiable next move: before proving anything, try to *construct*
  pinched gadgets at \(s_{\min}\le2\) from strong hypothetical
  ingredients — success kills the plan's premise instantly.

## Strategy audit

- Why the inherited route might work: the \(s_{\min}=2\) case looks
  rigidly structured (\(C_4\)-freeness forces a unique common neighbor
  of the terminals), suggesting a short forcing argument; rungs would
  build the spread-doubling mechanism incrementally.
- Fastest way to falsify it: test the premise that the rungs are
  lemma-sized. It failed at formulation time: a bridge with a disjoint
  counterexample copy on each side is a pinched gadget with
  \(S=\{1\}\), and an \(a\,w\,b\) path with counterexample lobes hung at
  \(a\) and \(w\) is one with \(S=\{2\}\) — so each unrestricted rung is
  **equivalent** to the full conjecture (`L026`), and "prove the bottom
  rung by hand" literally meant "prove the conjecture." Premise dead.
- Mechanistically distinct alternative or reframing: (a) the deferred
  order-16 census (finite information, no mechanism, heavy compute);
  (b) direct even-interval forcing under saturation constraints
  (dormant since S010); (c) the repair that emerged from the failure
  itself: the hiding mechanism is content invisible to every
  terminal-to-terminal path, so relativize the rungs to **taut**
  gadgets and handle the hidden parts structurally.
- Selected route and reason: (c) — it is not a new route but the
  corrected form of the inherited one, and it immediately produced
  theorems: the lobe decomposition (`L027`, hidden parts are always
  1-atom-like), the taut bottom rungs (`L028`, both rungs fall to
  \(C_4\)-only arguments), and the cubic reduction (`L029`). The
  census stays deferred (no mechanism); interval forcing stays dormant.
- Pivot criterion: none fired against the corrected route this session;
  for the next session, a taut pinched \(s_{\min}=3\) gadget found
  (disproof protocol), the rung closing with a generalizable mechanism
  (promote), or a stall (switch to 1-atom structure or the census).

## Work performed

- Opened attempt `A012`; proved T1 (rung completeness = `L026`), T2
  (lobe decomposition = `L027`, via the block–cut tree: essential
  vertices are exactly the chain blocks between the terminals, hanging
  branches meet the chain in one cut vertex), T3 (taut bottom rungs =
  `L028`: \(S=\{1\}\) trivially; \(s_{\min}=2\), \(S\subseteq\{2,3\}\)
  via unique common neighbor \(w\), the counting bounds "\(\le1\)
  \(w\)-edge per terminal side" and "\(\le1\) cross-neighbor per
  vertex," a tautness workhorse forcing every side vertex to touch
  \(\{w\}\cup Z\), degree forcing collapsing each side to \(\le1\)
  vertex, and a final forced 4-cycle \(a\,x\,z\,w\)), and T4 (cubic
  reduction = `L029`).
- Built experiment `E011` (fully independent implementation: graph6
  decoder, C4/cycle detectors, path + essential-vertex DFS, lobe
  components; 17 anchors including \(K_{3,3}-e\) tautness and both T1
  scaffolds with Petersen stand-ins) and ran it at orders 12–13
  (`C028`).
- Updated `CLAIMS.md` (`L026`–`L029`, `C028` + dependency notes),
  `OBLIGATIONS.md` (`G013` refined), `PROOF.md`, `DECISIONS.md`,
  `LOG.md`, `STATE.md`, `problem.json`.

## Results

- Proved claims: `L026` (rung completeness / spread-doubling ⟺ 0.1),
  `L027` (lobe decomposition), `L028` (taut bottom rungs closed,
  \(C_4\)-only; corollaries: every 2-atom with \(s_{\min}\le2\)
  contains a 1-atom or min-degree-3 power-free graph, and has order
  \(\ge17\)), `L029` (modulo 1-atoms, minimal counterexamples are
  cubic; 0.1 ⟺ no cubic counterexample ∧ no 1-atom; minimal 1-atoms
  have their sub-cubic vertex of degree 2).
- Provisional insights: the disproof interface now has exactly two
  live objects — 1-atoms and taut 2-atoms with \(s_{\min}\ge3\). The
  1-atom question is triply central (rungs, lobes, cubic reduction).
  \(K_{3,3}-e\) marks \(s_{\min}=3\) as the exact point where
  \(C_4\)-freeness stops sufficing and the power-spectrum fight begins.
- Computational evidence (`C028`): at orders 12–13, all 133
  rung-class gadgets are non-taut and all 265 lobe components have
  single essential attachments with internal degrees \(\ge3\) — both
  new lemmas hold on every instance in reach; stream and profile
  counts reproduce `E010` exactly from the independent implementation.
  Survey: every taut pinched gadget through order 13 has
  \(S=\{6,\dots,11\}\) (ratio \(11/6\)) and carries a \(C_8\); taut
  pinched \(s_{\min}\in\{3,4,5\}\) is empty there.
- Imported facts needing verification: none new this session
  (`C025`/`C026` remain abstract-strength).

## Failed routes and why

The inherited route as literally stated: its rungs are
conjecture-complete (`L026`), so executing it as written was
impossible, not merely hard. Preserved as the reason the rung ladder
must be taut-relativized; the S011 framing of \(s_{\min}\)-rungs as
independently provable steps is corrected in the records. Nothing else
was attempted and abandoned.

## Adversarial check

- The delicate proof is T3(ii); its forcing chain was re-derived twice
  (once via a cluster argument, once via the tautness workhorse) with
  every 4-cycle exhibited explicitly and each "\(\le1\)" bound checked
  against the exact edge inventory; the statement was then corrected to
  require \(s_{\min}=2\) explicitly after noticing \(S=\{3\}\) slips
  the common-neighbor hypothesis (it belongs to the next rung).
- T2's earlier draft used ad-hoc path surgery with a genuine gap (a
  2-linkage assumption); it was replaced by the block–cut-tree
  argument, where attachment uniqueness is tree combinatorics plus the
  standard fact that distinct blocks share at most one vertex.
- `E011` is a second, independent implementation of the entire
  detection stack; its exact agreement with `E010`'s recorded counts
  cross-validates both, and its per-instance checks could have refuted
  `L027`/`L028` on 16k+ real gadgets — they did not. The T1 scaffold
  anchors verify the constructions' combinatorics (through-sets,
  essential sets, spectrum confinement, degrees) with Petersen
  stand-ins, isolating exactly the properties the hand proofs use.
- All new numbers in records were copied from run outputs after the
  runs completed.

## Canonical records changed

- [ ] `STATEMENT.md` (unchanged; statement version stays 0.1)
- [x] `STATE.md`
- [x] `CLAIMS.md` (`L026`–`L029`, `C028` + dependency notes)
- [x] `OBLIGATIONS.md` (`G013` refined)
- [x] `PROOF.md` (outline: corrected rung program)
- [x] `DECISIONS.md` (rung program corrected; taut relativization)
- [x] `LOG.md`
- [x] `problem.json` and index
- [x] Session-scoped changes committed
- [x] Commit pushed to configured upstream

## Ending checkpoint

- Current frontier: finite exclusions unchanged (`L022`); disproof
  interface concentrated on 1-atoms (order \(\ge16\)) and taut
  2-atoms with \(s_{\min}\ge3\) (empty through order 13 even without
  \(C_8\)-freeness); spread-doubling now known equivalent to 0.1 in
  full, with its meaningful ladder being the taut one; conjecture
  reduced to cubic + 1-atoms.
- Remaining blockers: `G013` (both sub-questions), `G007`, `G002`,
  `G003`.
- Recalibration decision: pivoted at formulation time — the premise
  test killed the literal inherited plan and its repair became the
  session's theorems; this is the corrected continuation of the same
  program, not a new program.
- Best live alternative or reframing: minimal 1-atom structure theory;
  order-16 census deferred.
- Pivot trigger: taut \(s_{\min}=3\) gadget found → disproof protocol;
  rung closed with generalizable mechanism → promote to the ladder;
  stall → 1-atom structure or census.
- Best next action: attack the taut \(s_{\min}=3\) rung — prove no
  taut \(C_4\)-free power-free (D)-gadget with \(S\subseteq\{3,4,5\}\)
  exists, or exhibit one (disproof via `L025` R3).
- Files a new session should read: `STATE.md`, `A012`, `A011`,
  `E011/README.md`, `CLAIMS.md` rows `L025`–`L029`/`C028`,
  `OBLIGATIONS.md` `G013`, this session.

## Plain-language recap

The plan handed to this session was to prove the two narrowest cases of
the project's central "spread-doubling" principle: that a small
two-terminal graph free of power-of-two cycles can never keep all its
terminal-to-terminal paths in a narrow band. Before executing, the
session stress-tested the plan's premise — and it collapsed. In those
narrowest cases, a would-be gadget can smuggle an entire hypothetical
counterexample inside parts of itself that no terminal-to-terminal path
ever visits, hidden behind single-vertex bottlenecks. So proving those
cases impossible is *exactly as hard as the whole conjecture* — they
were never small steps at all. This turns out to be a theorem, not a
suspicion, and it sharpens the earlier picture: spread-doubling is not
just a consequence of the conjecture but fully equivalent to it.

The repair came from naming the smuggling mechanism. If we demand the
gadget be "taut" — every vertex must actually serve some
terminal-to-terminal path — then the hiding places are provably
confined to "lobes" hanging off single vertices, and each lobe is
itself a near-counterexample object (a "1-atom": one vertex of degree
below three, everything else at least three, no power-of-two cycles).
Under tautness, both narrow cases really are impossible, by short
arguments that only use the absence of 4-cycles. As a byproduct, the
same style of argument shows: unless a 1-atom exists somewhere, the
whole conjecture reduces to 3-regular graphs — so the 1-atom object is
now the load-bearing unknown on the disproof side.

Machine verification backed every step: an independently written
checker confirmed the new lemmas on every one of tens of thousands of
real graphs at 12–13 vertices, reproduced the previous session's
counts exactly, and surveyed the actual "honest" pinched gadgets: the
smallest ones keep their paths in the band 6–11 and always contain an
8-cycle. The next fight — terminals at distance three, where a classic
1998 example shows the shape first becomes realizable — is genuinely
open and is where the power-of-two structure itself must start doing
the work.

## Proposed next step

Attack the distance-three case of the taut gadget question: prove that
no taut, 4-cycle-free, power-free two-terminal gadget can keep all its
connection paths at lengths 3, 4, or 5 — or find one, which would
disprove the conjecture outright by the proved ring assembly. This is
the first rung where the power-of-two structure (not just 4-cycle
absence) must carry the argument: the classic \(K_{3,3}\)-minus-an-edge
example realizes exactly this shape and is blocked only by its
4-cycles, and the new survey shows the target is empty through 13
vertices. Success gives the first genuinely power-spectrum-driven rung
of the ladder and likely the general mechanism; an explicit gadget
instead would settle the conjecture negatively. Deferred alternatives:
structure theory for the 1-atom object (now the disproof side's
load-bearing unknown), and the 16-vertex census extension.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 2%
- Previous estimate, if any: 2% (S011)
- Reason for change: none. The session's negative half (the rungs were
  conjecture-complete) removes an illusory shortcut; the positive half
  (taut rungs closed, lobe decomposition, cubic reduction) is real but
  organizes the boundary rather than penetrating it. The two live
  objects — the taut \(s_{\min}=3\) rung and the 1-atom question —
  both retain the global-forcing character that has held the estimate
  at 2%.
- Basis: most promising routes — the taut \(s_{\min}=3\) rung (first
  genuinely power-spectrum-driven target, hand-scale structure) and
  1-atom structure theory; strongest obstacle — nothing yet forces
  cycle-length spread from power-freeness at any generality, and the
  equivalence results show the shortcuts were illusions; evidence —
  `L026`–`L029`, `C028`'s exact survey, the \(K_{3,3}-e\) boundary
  case.

This is a subjective research outlook, not mathematical evidence or a claim-status
promotion.
