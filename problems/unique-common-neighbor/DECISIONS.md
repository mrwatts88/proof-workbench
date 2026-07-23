# Decision log

Append decisions that alter the statement, assumptions, conventions, proof
architecture, or disposition of a major approach.

| Date | Decision | Reason | Affected records |
|---|---|---|---|
| 2026-07-23 | Create statement version 0.1 for intake. | Initial dossier creation. | `STATEMENT.md`, `problem.json` |
| 2026-07-23 | Normalize the supplied wording as version 0.2 and take the finite vertex set to be nonempty. | Allowing the empty graph would make the hypothesis vacuous while falsifying the existential conclusion. The domain convention must be explicit rather than silently assumed. | `STATEMENT.md`, `problem.json`, `CLAIMS.md`, `OBLIGATIONS.md`, `PROOF.md` |
| 2026-07-23 | Treat the reported external solution only as provenance; prohibit solution searches, citations, and intentional reproduction during the internal investigation. | The benchmark is intended to test independent proof development and review. | `STATEMENT.md`, `STATE.md`, `OBLIGATIONS.md`, `S001` |
| 2026-07-23 | Defer reference-solution comparison to a separately recorded phase after an internal candidate has undergone review. | Early comparison would contaminate the independent investigation. | `STATE.md`, `OBLIGATIONS.md`, `S001` |
| 2026-07-23 | Treat the deferred reference comparison as optional provenance work, not a condition for completing the exact internal mathematical claim. | The statement is settled by a self-contained proof and required independent reviews; no reference was consulted. | `OBLIGATIONS.md` G004, `R001`, `R002` |
| 2026-07-23 | Integrate the `L001`–`L005` route as the first proof candidate: local parity, equality across nonedges, complement connectivity, regularity, then a self-contained matrix-trace contradiction. | `A001` produced a complete dependency chain without external sources or computation. | `CLAIMS.md`, `OBLIGATIONS.md`, `PROOF.md`, `STATE.md`, `S002` |
| 2026-07-23 | Publish the reviewed internal proof as a standalone LaTeX source and label its prior-proof provenance as `reported`, not verified. | The reported external solution was never inspected; the LaTeX source makes the independently reviewed argument easy to read without upgrading that provenance. | `papers/unique-common-neighbor.tex`, `problem.json`, `S004` |
| 2026-07-23 | Use Tectonic as the required PDF compiler and make a successful PDF build a proof-promotion artifact. | Tectonic 0.16.9 is already installed and compiled the current source successfully; its one-command workflow suits agent automation. | `papers/build/unique-common-neighbor.pdf`, `problem.json`, `S005` |
