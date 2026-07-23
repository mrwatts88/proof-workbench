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

Imported frontier facts, not a candidate:

- `C004`–`C006`: an order-then-size minimal counterexample is
  subgraph-minimal for minimum degree \(3\), its cubic vertices dominate, and
  at least \(4/7\) of its vertices are cubic;
- `C007`: a counterexample contains an induced \(P_{13}\);
- `C008`: sufficiently large average degree forces a power-of-two cycle.

## Argument

No complete argument has been promoted from an attempt. The proved preliminary
lemmas remain in `A001` and `CLAIMS.md`.

## Unresolved gaps

- `G002`: make the near-2-connected reduction force a power-of-two cycle.
- `G003`: obtain a global \(8,16,\ldots\)-cycle forcing mechanism.
- `G006`: make the induced-\(P_{13}\)/cubic-domination route decisive.

## Computational dependencies

`E001` and `E002` give exact finite evidence only and are not part of a proof
candidate. `L005` and `L006` have separate hand proofs.
