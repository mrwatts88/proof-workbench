# Integrated proof or disproof candidate

- Statement version: 0.1
- Candidate status: none

## Dependency outline

No candidate exists.

Established preliminary reductions, none sufficient for the main claim:

- `L001`: reduction to a 2-connected graph with at most one internal
  degree-\(2\) vertex;
- `L002`: edge-minimal counterexamples have independent high-degree vertices;
- `L003`: a counterexample has order at least \(9\);
- `L004`: longest-path endpoint chords avoid Mersenne indices;
- `L005`–`L006`: a counterexample has order at least \(11\).
- `L007`: the imported induced-\(P_{13}\) and cubic-minimality conclusions,
  even with no \(C_4,C_8\), do not force \(C_{16}\).
- `L008`: a counterexample may be made edge-maximal while power-cycle-free,
  forcing a \(2^k-1\)-edge path across every nonedge.
- `L009`: that saturation property excludes a connected bipartite cubic
  large-girth realization of the prior local bundle.
- `L010`: edges outside all odd cycles form a matching in a saturated
  counterexample.
- `L011`: the saturation witnesses persist inside a non-bipartite
  2-connected leaf block, except at its possible cut vertex.
- `L012`: a shortest odd cycle of length at least \(7\) in that block has an
  external ear.
- `L013`: every shortest odd cycle in the block has an external ear, including
  the triangle and \(5\)-cycle cases.
- `L014`: one-ear theta length equations alone do not force a power-of-two
  cycle.
- `L015`: a full one-excursion saturation witness admits infinite power-free
  realizations in every attachment configuration.
- `L016`: a full two-excursion witness pattern likewise admits infinite
  power-free realizations; bounded single-witness data cannot force.
- `L017`: every counterexample has at least fourteen vertices
  (computer-assisted via the exhaustive search `E004`; at orders \(11\)–\(13\)
  no minimum-degree-\(3\) graph avoids both \(C_4\) and \(C_8\)).
- `L018`: every counterexample has at least eighteen vertices
  (computer-assisted via the anchored census `E006`: at orders
  \(14\)–\(17\) no minimum-degree-\(3\) graph avoids both \(C_4\) and
  \(C_8\) at all). This passes the strongest inspectable published
  general bound (`C012`, sixteen).
- `L022`: every counterexample has at least nineteen vertices (the
  order-18 census extension `C023`: all \(834{,}711{,}846\) connected
  \(C_4\)-free minimum-degree-\(3\) graphs on \(18\) vertices contain a
  \(C_8\)); the smallest \(\{C_4,C_8\}\)-free minimum-degree-\(3\)
  graph has between \(19\) and \(24\) vertices.
- `L019`–`L021`: the voltage-lift machinery (projection certificate,
  tree gauge, abelian commutator obstruction) — unconditional tool
  lemmas from the falsification program, not reductions of `C001`; with
  `C020`–`C022` they close the lift-certificate route for all finite
  voltage groups on the tested bases.
- `L023`–`L024`: the arc-digraph structure package and the
  collision-wall theorem (reviewed, `R001`): every voltage assignment
  over any finite group on any connected minimum-degree-\(3\) base
  carries identity-voltage tailless nb closed walks at every length
  \(\equiv0\bmod4\) (every even length if non-bipartite) past
  \(4\log_2\lvert\Gamma\rvert+C_B\). This is the lift program's closing
  theorem: per-base effective certificate death for all
  \(\lvert\Gamma\rvert\ge\Gamma_0(B)\), complementing the finite
  verdicts. Its trivial-group reading — forced balanced walk intervals
  at minimum degree \(3\) — is the quantitative core handed to `G007`;
  the unresolved gap between these forced walks and actual cycles is
  exactly where the main claim stands.
- `L025`: the atom reduction (assembly lemma on the disproof side, not a
  reduction of `C001`): a power-free graph with exactly one sub-cubic
  vertex, or a power-free two-terminal gadget with terminal path lengths
  pinched below ratio 2, would yield counterexamples by doubling or by
  rings placed in a dyadic gap. Contrapositively the main claim requires
  **spread-doubling** (\(s_{\max}\ge2\,s_{\min}\) for power-free
  two-terminal gadgets) — the sharp conditional form of walk-to-cycle
  transfer, since `C024`'s ring shows the unconditional form is false.
  `C027`: no atom exists through order 15 (exhaustive, anchored).
- `L026`–`L029`: the corrected rung program. `L026` (rung completeness):
  pinched gadgets at \(s_{\min}\in\{1,2\}\) can hide two counterexample
  copies behind cut vertices, so each unrestricted bottom rung — and
  spread-doubling itself — is *equivalent* to the main claim, not a lemma
  short of it. `L027` (lobe decomposition): every gadget is taut (every
  vertex on a terminal-to-terminal path) or hangs a lobe at one cut
  vertex, and power-free lobes are 1-atoms or min-degree-3 power-free
  graphs. `L028` (taut bottom rungs): no taut gadget has \(S=\{1\}\), and
  no taut \(C_4\)-free gadget has \(s_{\min}=2\) with
  \(S\subseteq\{2,3\}\) — so every 2-atom with \(s_{\min}\le2\) routes
  through the 1-atom question and has order \(\ge17\). `L029` (cubic
  reduction): modulo the 1-atom question, every minimal counterexample is
  cubic — statement 0.1 is equivalent to "no cubic counterexample and no
  1-atom". The disproof interface is thereby concentrated on two objects:
  1-atoms, and taut 2-atoms with \(s_{\min}\ge3\) (`C028`: through order
  13 the taut pinched world starts at \(s_{\min}=6\), interval
  through-sets, always carrying a \(C_8\)).
- `L030`: the taut \(s_{\min}=3\) rung. No vertex-taut \(C_4\)-free
  (D)-gadget has \(S\subseteq\{3,4,5\}\): tautness confines every middle
  vertex to distance one from a terminal neighborhood, forbidden
  length-6/7 paths collapse the middle layer entirely, and the surviving
  three-matchings structure on \(N(a)\cup N(b)\) dies in a dichotomy
  (\(C_4\) block or length-7 path). \(C_4\)-freeness alone suffices —
  the power spectrum is not yet needed at \(s_{\min}=3\). Corollaries:
  every taut 2-atom has \(s_{\min}\ge4\) and \(s_{\max}\ge6\); every
  2-atom with \(s_{\min}\le3\) routes through the 1-atom question
  (order \(\ge19\) at \(s_{\min}=3\)). By `C028`'s witnesses the
  \(C_4\)-only regime provably ends by \(s_{\min}=6\); the
  \(s_{\min}\in\{4,5\}\) rungs are the open boundary (`C029`: empty
  through order 14 over all terminal pairs).

Imported frontier facts, not a candidate:

- `C004`–`C006`: an order-then-size minimal counterexample is
  subgraph-minimal for minimum degree \(3\), its cubic vertices dominate, and
  at least \(4/7\) of its vertices are cubic;
- `C007`: a counterexample contains an induced \(P_{13}\);
- `C008`: sufficiently large average degree forces a power-of-two cycle.
- `C009`: finite Hamiltonian cubic graphs exist with arbitrarily large girth;
  this supplies the separation example in `L007`.
- `C012`–`C013`: the primary-source computational bounds — no
  counterexample below sixteen vertices (Royle; now superseded internally
  by `L018`), no cubic counterexample below thirty.
- `C014`–`C015`: the four extremal cubic \(\{C_4,C_8\}\)-free graphs at
  order \(24\); the planar one is internally verified with full Mersenne
  witness coverage across its nonedges.
- `C017`: Bensmail's 1-connected spectrum-confinement constructions
  (no \(q\)-power cycles for \(q\ge3\); only-\(C_4\) or only-\(C_8\)
  2-power families), delimiting what bounded cycle spectra can do without
  2-connectivity.
- `C024`: Bondy–Vince — at most two sub-cubic vertices forces two cycles
  with lengths differing by one or two; non-bipartite 3-connected forces
  a difference of exactly one; and their ring of \(K_{3,3}-e\) copies
  shows 2-connected minimum-degree-3 spectra can have unbounded-ratio
  gaps.
- `C025`–`C026`: Gao–Huo–Liu–Ma mod-\(k\)/consecutive-lengths package
  (nothing beyond `C024` at degree 3) and Carr's diameter-2 confirmation
  (a counterexample has diameter \(\ge3\)); both abstract-strength.

## Argument

No complete argument has been promoted from an attempt. The proved preliminary
lemmas remain in `A001` and `CLAIMS.md`.

## Unresolved gaps

- `G002`: make the near-2-connected reduction force a power-of-two cycle.
- `G003`: obtain a global \(8,16,\ldots\)-cycle forcing mechanism.
- `G007`: find a global minimal-counterexample restriction not shared by
  arbitrary connected cubic graphs of large girth and make it decisive; by
  `L015`–`L016` the decisive use of saturation must couple unboundedly many
  witnesses or generate an interval of even cycle lengths. (`G011` is
  resolved: the saturation reduction appears nowhere in the swept
  literature, so it is the project's frontier-passing asset.)
- `G013`: settle the atom question — find an atom (disproof by `L025`
  assembly) or prove the spread-doubling lemma (closing the ring channel
  and giving the first conditional walk-to-cycle forcing result). After
  `L026`–`L030` its live sub-questions are the 1-atom question (which
  also gates the cubic reduction) and taut 2-atoms, now with
  \(s_{\min}\ge4\) and \(s_{\max}\ge6\); the next rung is taut
  \(s_{\min}=4\), and \(C_4\)-only methods provably stop by
  \(s_{\min}=6\).

## Computational dependencies

`E001` and `E002` give exact finite evidence only and are not part of a proof
candidate. `L005` and `L006` have separate hand proofs.

`E003` rules out one 18-vertex attachment family but is not part of `L007`,
which instead uses the imported large-girth existence theorem `C009`.

`E004` is an exception to the evidence-only pattern: `L017` is proved
computer-assisted, with the collapse and coverage arguments in `A006` and the
exhaustive, anchor-validated search `E004` as its computational leg. `L005`
and `L006` retain independent hand proofs; `L017` does not have one.

`E006` plays the same role for `L018`, with one further dependency:
its generation layer is nauty's geng (an imported tool), anchored against
published OEIS counts and against `E004` at overlapping orders, with
per-graph independent re-verification of the degree and \(C_4\)
conditions. `E005` verifies the imported Markström graph and reproduces
the order-\(24\) cubic census; it supports `C014`, `C015`, and `C018`
only, not any lemma.
