# Current state

- Last updated: 2026-07-24 (S011)
- Problem: `P-002` — Erdős–Gyárfás Conjecture

## Exact target

Every finite simple undirected graph of minimum degree at least \(3\) contains a
cycle whose length is a power of two. See normalized `STATEMENT.md` version 0.1.

## Established

- `L001`–`L006`: block and edge-minimal reductions, longest-path chord
  restriction, hand proofs that every counterexample has \(\ge11\)
  vertices.
- `L008`–`L013` saturation package with `L014`–`L016` delimitations.
- `L017`/`L018`/`L022` finite exclusions: every counterexample has at
  least **nineteen** vertices; extremal \(\{C_4,C_8\}\)-free window
  \([19,24]\); census capped at order 18.
- `L019`–`L021` lift machinery; `L023`–`L024` the collision-wall theorem
  (reviewed, `R001`): balanced nb closed walks at every admissible
  length past a per-base threshold, in any finite voltage group — the
  lift/falsification program is closed as a theorem.
- **New (S011): `L025`, the atom reduction.** A power-free graph with
  exactly one sub-cubic vertex (1-atom), or a power-free two-terminal
  gadget with non-terminal degrees \(\ge3\) and all terminal-to-terminal
  path lengths within multiplicative ratio \(<2\) (2-atom), yields
  counterexamples by doubling/triangle or ring-in-dyadic-gap assembly
  (ring spectrum computed exactly; builder verified against the
  published Bondy–Vince figure spectrum). Contrapositively, statement
  0.1 forces **spread-doubling**: power-freeness must push
  \(s_{\max}\ge2\,s_{\min}\) in every such gadget.

## Imported frontier

- `C004`–`C009`, `C012`–`C014`, `C017` unchanged.
- **New (S011):** `C024` Bondy–Vince read in the published PDF (two
  cycles differing by 1 or 2 at \(\le2\) sub-cubic vertices; difference
  exactly 1 at 3-connected non-bipartite; the Figure-1 **ring** with
  spectrum \(\{4,6,9,11,13,15\}\) — 2-connected min-degree-3 spectra can
  gap at unbounded ratio); `C025` Gao–Huo–Liu–Ma and `C026` Carr
  diameter-2 (abstract strength). The min-degree-3 frontier in the
  literature is exactly Bondy–Vince strength; interval technology needs
  higher degree.

## Program status

The walk-to-cycle interface was scoped on arrival: the inherited kill
test fires **by construction** (`C024`'s ring carries the `L024` walk
intervals with unbounded-ratio spectrum gaps), so no unconditional
transfer exists — the conversion must consume power-freeness. Its sharp
form is the two-sided atom question `G013`: find an atom (disproof) or
prove spread-doubling (closes the entire ring/assembly channel).
`C027` (E010, anchored, exhaustive): **no atom — indeed no power-free
graph with \(\le2\) sub-cubic vertices — exists through order 15**;
profile data shows the pinch (ratio \(<2\), even a single through-length)
is geometrically common without power-freeness and every occurrence
contains a \(C_8\). Assembly counterexamples need gadgets \(\ge16\)
(doubling: order \(\ge32\)).

## Open obligations

- `G013` (new core): the atom / spread-doubling question.
- `G002`, `G003`, `G007`: the global mechanism; `G007` now routes
  through `G013`'s conditional transfer.
- `G004`: only the original 1997 Erdős article body remains uninspected.

## Strategy portfolio

- Primary: spread-doubling's bottom rungs — prove no power-free pinched
  gadget exists with \(s_{\min}\in\{1,2\}\) (the distance-2 case is
  tightly structured: \(C_4\)-freeness gives the terminals a unique
  common neighbor), with the ear/rerouting machinery `L012`–`L013` and
  the E010 profile samples as guides. Falsifiable both ways: a proof is
  the lemma's first rung; an explicit gadget is a disproof.
- Live alternative: extend the atom census to order 16 (multi-part PyPy,
  `E006`/S009 pattern, \(\sim\!15\times\) order 15); or attack
  even-interval forcing under saturation constraints directly.
- Pivot trigger: an atom found (switch to disproof mode: assemble the
  ring, verify, open a fresh reproduction audit); or bottom-rung proofs
  revealing a general mechanism (promote); or a deeper sweep surfacing
  prior ring/gadget treatments (rebase novelty).

## Human-level state

The project asked when unavoidable balanced round trips force actual
cycles. This session's answer: never unconditionally — a 1998
construction of Bondy and Vince already carries all the round trips with
huge gaps in its cycle lengths — but the question sharpens into one
finite object. If a small two-terminal gadget can be simultaneously free
of power-of-two cycles and "pinched" (all connection paths within a
factor-2 band), the conjecture is false by an explicit ring assembly we
proved correct and verified against the 1998 paper's own numbers. If no
such gadget exists at any size, that impossibility — power-freeness
forcing path spread to double — is the mechanism a proof needs. The
exhaustive search says: through 15 vertices, nothing power-free exists in
the gadget class at all, while pinching alone is easy — the two
properties genuinely fight, and the conjecture says power-freeness always
wins. The fight's general outcome is now the project's central question.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 2%
- Previous estimate: 2% (S010)
- Reason for no change: structural clarity (a finite disproof interface;
  a sharp necessary condition) is real progress but not proximity — the
  atom search is empty where it is cheap, and spread-doubling in general
  has the same global-forcing character as the conjecture itself.

## Resume reading

1. `STATEMENT.md`
2. `A011` (the atom reduction and its proofs)
3. `E010/README.md` (search + profile results)
4. `CLAIMS.md` rows `C024`–`C027`, `L025`; `OBLIGATIONS.md` `G013`
5. `references/source-audit-2026-07-24-S011.md`
6. `sessions/S011-…md`
