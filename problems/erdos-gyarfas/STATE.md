# Current state

- Last updated: 2026-07-23
- Problem: `P-002` — Erdős–Gyárfás Conjecture

## Exact target

Every finite simple undirected graph of minimum degree at least \(3\) contains a
cycle whose length is a power of two. See normalized `STATEMENT.md` version 0.1.

## Established

- `L001`–`L006`: block and edge-minimal reductions, a longest-path chord
  restriction, and hand proofs that every counterexample has at least eleven
  vertices.
- `L008`–`L013`: the saturation reduction — Mersenne witnesses across every
  nonedge — with its parity separation, odd-cycle matching structure,
  leaf-block persistence, and external ears; `L014`–`L016` delimit it:
  bounded single-witness data cannot force.
- `L017` (computer-assisted, internal generation): every counterexample has
  at least fourteen vertices.
- `L018` (computer-assisted, anchored geng generation): every counterexample
  has at least **eighteen** vertices — past the strongest inspectable
  published general bound (sixteen, Royle 2002, `C012`). At orders
  \(14\)–\(17\) no minimum-degree-3 graph avoids both \(C_4\) and \(C_8\)
  at all (`E006`/`C016`), so the smallest such graph has \(18\)–\(24\)
  vertices.

## Imported frontier

- `C004`–`C006` (Carr 2026), `C007` (P13-free, 2025), `C008`
  (Liu–Montgomery), `C009` (Biggs): unchanged.
- `C012` (Royle 2002): general bound \(\ge16\); the circulating "\(\ge17\)"
  is an unsupported overread — do not cite it.
- `C013` (Markström 2004): cubic counterexamples have \(\ge30\) vertices.
- `C014` (Markström 2004, Table 3): cubic \(\{C_4,C_8\}\)-free counts
  \(4/23/251\) at orders \(24/26/28\); smallest at \(24\); one planar.
- `C017` (Bensmail 2017): 1-connected spectrum-confinement families — no
  \(q\)-power cycles for every \(q\ge3\); only-\(C_4\) or only-\(C_8\)
  2-power families. The trick needs cut vertices, which `L011` removes.

## Verified test material

- The Markström graph (HoG 51419) is held and fully verified (`C015`,
  `E005`): cubic, planar, spectrum \(\{3,5,6,7\}\cup\{9..24\}\), and every
  one of its 240 nonedges carries a Mersenne witness — adding any edge
  creates a power-of-two cycle. It misses `L008` sainthood only by
  containing \(C_{16}\).
- All four extremal order-24 cubic graphs are held, reproduced from
  scratch (`C018`, `E005`: 4 of 9,467,449 \(C_4\)-free cubic graphs;
  orders \(14\)–\(22\) empty; exactly one planar, isomorphic to HoG
  51419). Every one of the four is fully Mersenne-witness-covered — the
  whole extremal class sits "one \(C_{16}\) away" from `L008` saturation.

## Open obligations

- `G002`, `G003`, `G007`: the global mechanism, untouched by anything
  finite. By `L015`–`L016`, decisive saturation use needs unbounded witness
  coupling or an even-length interval.
- `G004`: only the original 1997 Erdős article body remains uninspected
  (access attempts recorded).
- `G011` is resolved: the saturation reduction appears nowhere in the swept
  literature — it is this project's unclaimed asset (caveat: re-sweep before
  any external novelty claim).

## Strategy portfolio

- Primary (proof side): strengthen the saturation line — the confirmed-novel
  asset — using the verified extremal graphs as the concrete boundary
  objects; its decisive form must couple unboundedly many witnesses or
  produce an interval of even lengths (`G007`).
- Live alternative (disproof side, new): the spectrum-gap program — Bensmail
  confinement shows how bounded spectra dodge sparse power sets and why
  1-connectivity is essential; the counterexample question is whether a
  2-connected minimum-degree-3 spectrum can gap every power of two against
  forced-density results (Bondy–Vince pairs; Sudakov–Verstraëte consecutive
  even lengths). Erdős and Gyárfás themselves expected the answer to be
  negative.
- Support layer (capped): the exact census. Do not extend past order ~18
  without a faster filter (the user has offered PyPy, installed and
  suitable for the pure-Python bitmask detectors; a compiled filter is the
  fallback) and a route-driven reason; the window \([18,24]\) for the
  first \(\{C_4,C_8\}\)-free graphs is already a concrete target.
- Pivot trigger: a \(\{C_4,C_8\}\)-free graph at orders 18–23 (new
  structure, counterexample screen), or a decisive lean in the
  gap-versus-density tension from the order-24 spectra analysis.

## Best next action

Open the internal tool-building attempt on the falsification route:
compute the four order-24 graphs' full even-cycle spectra as calibration,
then attempt voltage-graph lifts of small base graphs targeting a
2-connected minimum-degree-3 family whose cycle lengths avoid all powers
of two up to the order — naming kill conditions before starting (a proved
obstruction forcing a power-of-two balanced cycle in every admissible
assignment, or loss of girth/spectrum control on the first concrete
bases). Proof-side alternative: attempt a controlled-start
consecutive-even-lengths lemma at minimum degree 3 on girth-extremal
graphs. Capped support: extend the census to order 18 under PyPy. Per the
contract's tool-building rule (O009), missing techniques are attempted
internally, not awaited.

## Human-level state

The session imported the literature's real numbers from primary sources
(catching that the widely repeated "seventeen vertices" bound was never
actually computed), verified the famous 24-vertex near-miss graph down to
the bone, confirmed by a recorded literature sweep that this project's
saturation idea is genuinely absent from published work, and then used a
modern generator to pass the 24-year-old computational frontier: every
counterexample now provably needs at least eighteen vertices, and below
eighteen there isn't even a graph avoiding the two smallest forbidden
cycle lengths. Strategically, the user's challenge ("is exhaustive
checking really the path?") was answered by capping the search layer and
naming a falsification program built from Bensmail's constructions: the
whole question is whether a robustly connected sparse graph can steer its
cycle lengths around every power of two — the known constructions that do
this all cheat with cut vertices.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 2%
- Previous estimate: 1%
- Reason for change: better route inventory, not better evidence — the
  saturation asset is confirmed unclaimed, and the falsification-side
  spectrum-gap program is concrete and mechanistically distinct; both still
  need tools beyond the current field.

## Resume reading

1. `STATEMENT.md`
2. `CLAIMS.md`
3. `OBLIGATIONS.md`
4. `attempts/A007-the-general-finite-frontier-past-order-sixteen.md`
5. `references/source-audit-2026-07-23-S007.md`
6. `experiments/E005-…/README.md` and `experiments/E006-…/README.md`
7. `sessions/S007-…md`
