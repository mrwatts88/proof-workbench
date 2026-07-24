# Current state

- Last updated: 2026-07-24 (S013)
- Problem: `P-002` — Erdős–Gyárfás Conjecture

## Exact target

Every finite simple undirected graph of minimum degree at least \(3\) contains a
cycle whose length is a power of two. See normalized `STATEMENT.md` version 0.1.

## Established

- `L001`–`L006`: block and edge-minimal reductions; hand proofs that every
  counterexample has \(\ge11\) vertices.
- `L008`–`L013` saturation package with `L014`–`L016` delimitations.
- `L017`/`L018`/`L022` finite exclusions: every counterexample has at
  least **nineteen** vertices; extremal \(\{C_4,C_8\}\)-free window
  \([19,24]\); census capped at order 18.
- `L019`–`L021` lift machinery; `L023`–`L024` the collision-wall theorem
  (reviewed, `R001`): the lift/falsification program is closed as a
  theorem.
- `L025` atom reduction; `L026` rung completeness (unrestricted rungs and
  full spread-doubling are each *equivalent* to 0.1); `L027` lobe
  decomposition; `L028` taut bottom rungs (\(s_{\min}\le2\), \(C_4\)-only);
  `L029` cubic reduction modulo 1-atoms.
- **New (S013): `L030`, the taut \(s_{\min}=3\) rung.** No vertex-taut
  \(C_4\)-free (D)-gadget has \(S\subseteq\{3,4,5\}\) — equivalently,
  taut + \(C_4\)-free + \(d(a,b)\ge3\) forces an \(a\)–\(b\) path of
  length \(\ge6\). \(C_4\)-freeness alone carries the whole rung (the
  S012 expectation that the power spectrum must enter at \(s_{\min}=3\)
  was wrong). Proof: middle-layer collapse (tautness pins middles to
  distance one from \(N(a)\cup N(b)\); forbidden length-6/7 paths empty
  the middle) plus a three-matchings endgame dichotomy (\(C_4\) block or
  length-7 path). Corollaries: every taut 2-atom has \(s_{\min}\ge4\)
  and \(s_{\max}\ge6\); every 2-atom with \(s_{\min}\le3\) routes
  through the 1-atom question and has order \(\ge19\) at \(s_{\min}=3\).

## Imported frontier

- `C004`–`C009`, `C012`–`C014`, `C017`, `C024`–`C026` unchanged
  (Bondy–Vince read in the published PDF; `C025`/`C026`
  abstract-strength). The min-degree-3 literature frontier remains
  exactly Bondy–Vince strength.

## Program status

The disproof interface (`G013`) has two live objects. (a) The **1-atom
question**: a power-free graph with exactly one sub-cubic vertex (degree
2 in the minimal case, `L029`) — the sole content of the unrestricted
bottom rungs, the lobe half of every non-taut 2-atom, and the sole
obstruction to the cubic reduction. (b) **Taut 2-atoms, now with
\(s_{\min}\ge4\) and \(s_{\max}\ge6\)** (`L030` C1). Boundary map: the
\(C_4\)-only regime of the taut ladder closes \(s_{\min}\le3\) (`L028`,
`L030`) and provably fails at \(s_{\min}=6\) (`C028`'s five taut pinched
witnesses, \(S=\{6,\dots,11\}\), each with a \(C_8\)); the
\(s_{\min}\in\{4,5\}\) rungs are the open boundary, empty through order
14 over **all** terminal pairs (`C029`, the first search covering
degree-\(\ge3\) terminals). `C027`: no atom of any kind through order 15.

## Open obligations

- `G013` (core, refined S013): 1-atoms; taut 2-atoms with
  \(s_{\min}\ge4\).
- `G002`, `G003`, `G007`: the global mechanism; `G007` routes through
  `G013`'s conditional transfer.
- `G004`: only the original 1997 Erdős article body remains uninspected.

## Strategy portfolio

- Primary: the **taut \(s_{\min}=4\) rung** — prove no taut
  \(C_4\)-free (D)-gadget has \(S\subseteq\{4,5,6,7\}\), or find a
  \(C_4\)-free taut pinched \(s_{\min}\in\{4,5\}\) gadget at orders
  14–16. The `L030` cascade is the candidate mechanism; the new case is
  depth-2 middles (vertices at distance 2 from both terminal
  neighborhoods), where the position analysis genuinely branches. Either
  outcome locates the exact \(C_4\)/power boundary of the ladder.
- Live alternative: direct \(C_8\)-forcing at \(s_{\min}=6\) — prove
  every taut \(C_4\)-free pinched \(s_{\min}=6\) gadget contains a
  \(C_8\), guided by the five concrete witnesses; this is the real
  power-spectrum fight and feeds `G007` directly.
- Second alternative: minimal 1-atom structure theory (sub-cubic vertex
  has degree 2; next: 2-connectivity, cycle structure through the
  exceptional vertex).
- Deferred: order-16 atom census (multi-part PyPy, `E006`/S009 pattern).
- Pivot triggers: a taut pinched \(s_{\min}\in\{4,5\}\) gadget found
  (**check power-freeness**: if power-free it is a 2-atom — disproof
  protocol; if not, the rung survives only power-relativized and the
  analysis switches to what its power cycles look like); the \(s_{\min}=4\)
  cascade stalling at depth-2 middles after honest effort (switch to the
  \(s_{\min}=6\) \(C_8\)-forcing alternative or 1-atom theory).

## Human-level state

The project's disproof interface asks for a small two-terminal graph
that avoids power-of-two cycles while keeping all its connection paths
in a narrow band. Last session showed the two narrowest cases are
impossible for "taut" gadgets (every vertex serving some connection
path), using only the absence of 4-cycles, and predicted the next case —
paths of lengths 3-to-5 — would need the power-of-two structure itself.
This session proved that prediction wrong in the best way: the 3-to-5
case is also impossible, again from 4-cycle absence alone. The proof
watches the gadget's middle collapse under the path-length ceiling until
only a rigid skeleton of three perfect matchings remains, and that
skeleton always contains either a 4-cycle or a too-long path. A
machine search over every terminal choice of every candidate graph up
to 14 vertices — five and a half million graphs, 1.36 million terminal
pairs — found nothing, matching the theorem. The known enemy shapes at
band 6-to-11 show the free ride ends by band-start 6: somewhere in
band-start 4 or 5 the 4-cycle argument must run out, and the fight
against the 8-cycle begins.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 2%
- Previous estimate: 2% (S012)
- Reason for no change: the session closed its target rung cleanly and
  one rung earlier than expected in the ladder's own terms, but the
  mechanism used (\(C_4\)-only collapse) provably cannot reach the
  \(s_{\min}=6\) wall, so the genuinely hard object — forcing a power
  cycle from power-freeness — has still never been engaged. Progress is
  real but is boundary-mapping, not penetration.

## Resume reading

1. `STATEMENT.md`
2. `A013` (the rung theorem `L030`: middle-layer collapse, three-matchings
   endgame)
3. `A012` (tautness, lobes, rung completeness), `A011` (atoms, rings)
4. `CLAIMS.md` rows `L025`–`L030`, `C027`–`C029`; `OBLIGATIONS.md`
   `G013`
5. `E012/README.md`; `sessions/S013-…md`
