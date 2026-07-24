# Current state

- Last updated: 2026-07-23
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
- `L017` (computer-assisted, internal generation): counterexamples have
  \(\ge14\) vertices. `L018` (computer-assisted, anchored geng):
  \(\ge18\). **`L022` (new, S009 census extension): \(\ge19\)** — the
  order-18 class of \(834{,}711{,}846\) connected \(C_4\)-free
  minimum-degree-3 graphs is entirely \(C_8\)-positive (`C023`); the
  smallest \(\{C_4,C_8\}\)-free minimum-degree-3 graph has
  \(19\)–\(24\) vertices.
- **New (S009), lift machinery:** `L019` (cycles in a voltage lift
  project to tailless non-backtracking closed walks of the same length
  with zero net voltage — the power-freeness certificate), `L020`
  (spanning-tree gauge; assignments live in \((\mathbb{Z}_m)^\mu\); net
  voltage is the cycle-space pairing), `L021` (commutator words are
  tailless non-backtracking closed walks of length
  \(2(|W_1|+|W_2|)\) with zero net voltage over **every** abelian group;
  realized at length 8 on the dumbbell, 16 on theta3/\(K_4\)).

## Imported frontier

- `C004`–`C009`, `C012`–`C014`, `C017` unchanged (Carr minimality;
  \(P_{13}\)-free; Liu–Montgomery; Biggs; Royle \(\ge16\) with the "17"
  overread flagged; Markström cubic \(\ge30\) and the order-24 census;
  Bensmail 1-connected spectrum confinement).

## Verified test material

- The four order-24 extremal cubic graphs (`C018`, `E005`), plus new
  calibration `C019`: they contain \(315/330/207/228\) sixteen-cycles,
  every edge on at least \(70\), no edge on all — the extremal
  \(C_{16}\) obstruction is massively redundant; no local surgery can
  reach a counterexample from the census boundary.

## S009 verdict on the voltage-certificate program (A008 and A009, both closed)

- Cyclic/abelian arm (`A008`, `C020`): for the complete list of
  cycle-rank-2 minimum-degree-3 bases (bouquet, theta3, dumbbell) plus
  \(K_4\), \(K_{3,3}\), prism, and **every** modulus \(m\ge2\), no
  cyclic voltage assignment can be walk-certified power-free —
  exhaustive sieve below each base's zero-vector threshold, integer
  zero vector (`L021`, commutator words) above it.
- Truth level (`C021`): at every lift order in \([12,30]\), all cyclic
  assignments, every simple lift actually contains \(C_4\), \(C_8\), or
  \(C_{16}\) — no counterexample in the cyclic-lift universe of these
  bases through order 30.
- Non-abelian arm (`A009`, `C022`): the solvable cascade (double
  commutators, power-twisted commutators; Feit–Thompson rules out all
  odd-order groups) was confirmed by pre-registered predictions — and
  then the decisive test failed too: the perfect group \(A_5\), immune
  to every structural channel, is certificate-dead by length 16 on all
  cycle-rank-2 bases, all 3600 assignments each, zero survivors.
- Diagnosis: the binding constraint was never group structure but group
  **size** — the collision wall. Walk counts grow like \(2^L\) against
  \(\lvert\Gamma\rvert\) voltage values, so certificates die at
  \(\approx2\log_2\lvert\Gamma\rvert\) while power-freeness needs
  survival to \(\approx n_B\lvert\Gamma\rvert\). No group crosses that
  exponential gap. The certificate program is retired for all finite
  groups; its closing theorem (the collision-wall lemma) is the refined
  `G012`.

## Open obligations

- `G002`, `G003`, `G007`: the global mechanism, untouched by anything
  finite. Decisive saturation use needs unbounded witness coupling or an
  even-length interval (`L015`/`L016`); the `L021` length formula and
  the collision wall are new concrete input for what an interval lemma
  should force.
- `G012` (refined): prove the collision-wall lemma — identity-voltage
  tailless nb closed walks at every power length
  \(\ge C\log_2\lvert\Gamma\rvert+C_B\), for every group and every
  min-degree-3 base; composition construction explicit, only
  first/last-arc diversity bookkeeping open; coset confinement already
  ruled out (undirectedness forces period \(\le2\)).
- `G004`: only the original 1997 Erdős article body remains uninspected.

## Strategy portfolio

- Primary: prove the collision-wall lemma (`G012`). It is the closing
  theorem of the lift program, it is small and falsifiable (either the
  bookkeeping closes or a value-confinement counterexample family
  appears — which would itself be a new construction lever), and its
  content is proof-side raw material: minimum degree 3 forces
  identity-voltage closed walks at *every* even length past a
  logarithmic threshold, leaving walk-to-cycle injectivity as the
  conjecture's hard core seen quantitatively.
- Live alternative (proof side): the controlled-start
  consecutive-even-lengths lemma at minimum degree 3, now fed by both
  the `L021` length formula and the wall heuristic.
- Support layer (capped, and now complete to its cap): the order-18
  census finished empty (`C023`/`L022`); order 19 is \(\sim2\times
  10^{10}\) graphs — past this pipeline without a compiled filter, and
  the cap stands.
- Pivot trigger: a proved collision-wall lemma (fold it into the note
  and move to the proof side), or a confinement counterexample family
  (reopen construction with that lever).

## Best next action

Attempt the collision-wall lemma: for every finite voltage group
\(\Gamma\) and every connected min-degree-3 base, every assignment
admits an identity-voltage tailless non-backtracking closed walk of
length \(2^k\) for every \(2^k\ge C\log_2\lvert\Gamma\rvert+C_B\). The
route: pigeonhole same-voltage non-backtracking walk pairs and compose
\(W\cdot\overline{W'}\); what is open is only the first/last-arc
diversity needed for the tailless junctions (`A009` records the
construction, the matching data, and why coset confinement cannot
dodge). Success closes `G012`, adds the strongest lemma of the
publishable note, and hands `G007` its quantitative core; failure in
the form of a confinement family would reopen construction with a new
lever. Deferred alternative: the proof-side interval lemma directly.
The census support layer is complete at its cap (order 18 empty,
`L022`).

## Human-level state

The project spent the session trying to *build* a counterexample
instead of searching for one, using "lifted" graphs — big graphs
assembled from a small template plus group arithmetic, chosen because
forbidden cycle lengths upstairs correspond to checkable walk
conditions downstairs. The attempt was structured to fail informatively,
and it did, twice, at increasing depth: commutative arithmetic is blind
to commutator round-trips, which land exactly on forbidden lengths —
proved, for every modulus; and when the construction was rebuilt over
non-commutative symmetry groups, including the smallest "perfect" group
immune to every structural excuse, everything still died at length 16.
The reason turned out to be counting, not algebra: a group with
\(N\) elements can only distinguish \(N\) walk-values, while the number
of walks explodes exponentially with length, so certificates of safety
die at a length like \(2\log N\) — hopelessly short of the graph's own
size, for every possible group. That closes the entire
algebraic-certificate road to a counterexample and leaves a clean,
unproved lemma ("the collision wall") whose proof would both finish
this chapter rigorously and supply the proof side of the conjecture
with its sharpest quantitative fact so far. The 24-vertex near-miss
graphs were also fingerprinted (hundreds of 16-cycles through every
edge), confirming no small repair of known graphs can work. Overnight,
the exhaustive check of all 18-vertex candidates finished empty —
834,711,846 graphs, every one containing a forbidden cycle — so any
counterexample now provably needs at least 19 vertices, and the first
graph avoiding the two smallest forbidden lengths lives somewhere
between 19 and 24 vertices.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 2%
- Previous estimate: 2%
- Reason for no change: the session produced real information — three
  permanent lemmas, a complete kill of the abelian tool arm, and a
  sharpened successor — but killing one's own tool is progress in
  knowledge, not proximity; the deep obstacles (`G002`/`G003`/`G007`)
  stand, and inflating on activity is what the calibration rule forbids.

## Resume reading

1. `STATEMENT.md`
2. `CLAIMS.md` (`L019`–`L022`, `C019`–`C023` new)
3. `OBLIGATIONS.md` (`G012` refined)
4. `attempts/A008-…md` and `attempts/A009-…md`
5. `experiments/E007-…/README.md` and `experiments/E008-…/README.md`
6. `attempts/A007-…md` addendum and `experiments/E006-…/README.md`
   (order-18 extension, `L022`)
7. `sessions/S009-…md`
