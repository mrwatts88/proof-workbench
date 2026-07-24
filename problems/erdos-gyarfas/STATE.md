# Current state

- Last updated: 2026-07-24
- Problem: `P-002` — Erdős–Gyárfás Conjecture

## Exact target

Every finite simple undirected graph of minimum degree at least \(3\) contains a
cycle whose length is a power of two. See normalized `STATEMENT.md` version 0.1.

## Established

- `L001`–`L006`: block and edge-minimal reductions, longest-path chord
  restriction, hand proofs that every counterexample has \(\ge11\)
  vertices.
- `L008`–`L013` saturation package with `L014`–`L016` delimitations:
  bounded single-witness data cannot force.
- `L017`/`L018`/`L022` finite exclusions: every counterexample has at
  least **nineteen** vertices (order-18 census `C023`); the extremal
  \(\{C_4,C_8\}\)-free window is \([19,24]\). Census capped here.
- `L019`–`L021` lift machinery (projection certificate, tree gauge,
  abelian commutator obstruction), with exhaustive certificate verdicts
  `C020`/`C022` and truth census `C021`.
- **New (S010): `L023`–`L024`, the collision-wall theorem, reviewed
  (`R001`, delegated fresh-context logic audit, pass).** For every
  finite group \(\Gamma\), every connected multigraph base with
  \(\delta\ge3\), every voltage assignment: identity-voltage tailless
  non-backtracking closed walks exist at every length
  \(\equiv0\bmod4\) (every even length if non-bipartite) past
  \(4\ell^*+4R_B+8\), hence at every \(2^k\ge
  4\log_2\lvert\Gamma\rvert+C_B\). Proof: seed pair by pigeonhole,
  branch-and-steer through the strongly connected nb arc digraph
  (`L023`: strong connectivity, period \(\le2\), exact-length
  reachability — all internal), four-junction gluing, voltage
  telescoping in any group. Verified mechanically (`E009`, 9.6M
  assertions; reviewer's independent probe, 108 further cases).

## Program status

The voltage-lift falsification program is **closed as a theorem**:
abelian arm by `L021`/`C020`, non-abelian arm by `C022`, and now the
closing theorem `L024` gives per-base effective certificate death for
all \(\lvert\Gamma\rvert\ge\Gamma_0(B)\) (`G012` resolved). Caveats
recorded: closure is per-base (small fixed group on large-\(R_B\) bases
is untouched by the corollary), and bipartite bases force only
\(\equiv0\bmod4\) lengths — powers of two unaffected.

## Imported frontier

- `C004`–`C009`, `C012`–`C014`, `C017` unchanged (Carr minimality;
  \(P_{13}\)-free; Liu–Montgomery average degree; Biggs; Royle \(\ge16\)
  with the "17" overread flagged; Markström cubic \(\ge30\) and the
  order-24 census; Bensmail 1-connected spectrum confinement).

## Open obligations

- `G002`, `G003`, `G007`: the global mechanism. `G007` now holds the
  project's sharpest quantitative input (`L024`, trivial group):
  minimum degree \(3\) forces tailless nb closed **walks** at every
  mod-4 length past a constant threshold, balanceable in any finite
  quotient at log cost. The open gap is exactly **walk-to-cycle**.
- `G004`: only the original 1997 Erdős article body remains uninspected.

## Strategy portfolio

- Primary (new): the walk-to-cycle interface. Before attempting,
  sweep the cycle-lengths literature at minimum degree 3
  (Bondy–Vince pairs; Sudakov–Verstraëte and Gao–Huo–Liu–Ma-style
  even-interval and mod-\(k\) results; Liu–Montgomery methods) and
  import the strongest verified even-length interval facts; then
  formulate the transfer lemma against that frontier and search for
  its counterexamples first (large-girth cubic graphs calibrate how
  much length transfer must lose).
- Live alternative: the saturation constraints (`L008`–`L013`) as the
  extra hypothesis powering the transfer — a minimal counterexample is
  not an arbitrary min-degree-3 graph, and the interval mechanism only
  needs to work under those constraints.
- Support layer: census complete at its cap (order 18 empty; order 19
  needs a compiled filter and a route-driven reason).
- Pivot trigger: a literature result already giving consecutive even
  cycle lengths at minimum degree 3 (import and rebase); or a
  demonstrated unbounded walk/cycle length separation in 2-connected
  min-degree-3 graphs (kills bounded transfer; route must switch to
  walk abundance/counting).

## Best next action

Open the proof-side walk-to-cycle attempt: (1) deliberate literature
sweep on cycle-length intervals and mod-\(k\) cycle lengths at minimum
degree 3, importing the strongest primary-source results; (2) formulate
the walk-to-cycle transfer lemma candidate precisely (what cycle
lengths must follow from the forced balanced walk intervals of `L024`
plus 2-connectivity/saturation constraints); (3) failure-first: measure
the walk-vs-cycle length gap on large-girth cubic graphs and the
order-24 extremal graphs to find the transfer's true shape or its
counterexample. Success sharpens `G007` into a concrete forcing lemma;
the named kill test retires bounded transfer cheaply.

## Human-level state

The "collision wall" — last session's conjectured explanation for why
no algebraic construction of a counterexample can ever certify itself
safe — is now a proved theorem, checked by machine on millions of
instances and passed by an independent adversarial audit. It says:
in any robustly connected sparse graph, balanced round trips of every
suitable length are unavoidable once you pass a small threshold — no
matter what finite symmetry system labels the edges. That closes the
construction chapter rigorously and hands the proof side its sharpest
tool yet: the conjecture's difficulty is now cleanly concentrated in
one question — when must an unavoidable balanced round trip contain an
actual simple cycle of controlled length? The next session begins that
question: first by checking what the published literature already
knows about forced cycle lengths in minimum-degree-3 graphs, then by
testing the transfer idea against the graphs most likely to break it.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 2%
- Previous estimate: 2%
- Reason for no change: the session converted a heuristic into a
  reviewed theorem and closed `G012`, which is real, durable progress —
  but it is progress on the project's *own tool chapter*, not on the
  conjecture's hard core, which is now visibly the walk-to-cycle gap
  (`G002`/`G003`/`G007` all stand). Calibration rule: activity and
  elegance are not proximity.

## Resume reading

1. `STATEMENT.md`
2. `CLAIMS.md` (`L023`–`L024` new; dependency notes)
3. `OBLIGATIONS.md` (`G012` resolved; `G007` updated)
4. `attempts/A010-…md` (the collision-wall proof)
5. `reviews/R001-…md` (audit verdict and repair log)
6. `experiments/E009-…/README.md`
7. `sessions/S010-…md`
