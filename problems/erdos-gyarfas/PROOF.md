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

Imported frontier facts, not a candidate:

- `C004`–`C006`: an order-then-size minimal counterexample is
  subgraph-minimal for minimum degree \(3\), its cubic vertices dominate, and
  at least \(4/7\) of its vertices are cubic;
- `C007`: a counterexample contains an induced \(P_{13}\);
- `C008`: sufficiently large average degree forces a power-of-two cycle.
- `C009`: finite Hamiltonian cubic graphs exist with arbitrarily large girth;
  this supplies the separation example in `L007`.

## Argument

No complete argument has been promoted from an attempt. The proved preliminary
lemmas remain in `A001` and `CLAIMS.md`.

## Unresolved gaps

- `G002`: make the near-2-connected reduction force a power-of-two cycle.
- `G003`: obtain a global \(8,16,\ldots\)-cycle forcing mechanism.
- `G007`: find a global minimal-counterexample restriction not shared by
  arbitrary connected cubic graphs of large girth and make it decisive; by
  `L015`–`L016` the decisive use of saturation must couple unboundedly many
  witnesses or generate an interval of even cycle lengths.
- `G010`: extend the exhaustive \(\{C_4,C_8\}\)-free search through orders
  \(14\)–\(15\), where the small-order collapse still applies; record and
  classify any survivors.

## Computational dependencies

`E001` and `E002` give exact finite evidence only and are not part of a proof
candidate. `L005` and `L006` have separate hand proofs.

`E003` rules out one 18-vertex attachment family but is not part of `L007`,
which instead uses the imported large-girth existence theorem `C009`.

`E004` is an exception to the evidence-only pattern: `L017` is proved
computer-assisted, with the collapse and coverage arguments in `A006` and the
exhaustive, anchor-validated search `E004` as its computational leg. `L005`
and `L006` retain independent hand proofs; `L017` does not have one.
