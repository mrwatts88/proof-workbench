# Decision log

Append decisions that alter the statement, assumptions, conventions, proof
architecture, or disposition of a major approach.

| Date | Decision | Reason | Affected records |
|---|---|---|---|
| 2026-07-23 | Create statement version 0.1 for intake. | Initial dossier creation. | `STATEMENT.md`, `problem.json` |
| 2026-07-23 | Interpret the named conjecture as the finite simple undirected statement, with a simple cycle of length \(2^k\) for \(k\ge 2\). | This exposes the graph category and cycle convention without changing the standard substantive target; powers \(1\) and \(2\) cannot be simple-cycle lengths. | `STATEMENT.md`, `CLAIMS.md` |
| 2026-07-23 | Begin with an internal structural and exact-small-case attack; defer literature and current-status claims until sources are deliberately inspected. | This keeps imported facts separate from deductions and leaves provenance visibly unverified. | `STATEMENT.md`, `STATE.md`, `S001` |
| 2026-07-23 | After proving the order-\(9\) and order-\(10\) exclusions, stop using one-order-at-a-time enumeration as the main route. | The literature reports substantially stronger finite searches, while the order-\(11\) codegree budget already leaves twelve degree sequences; finite extension is evidence, not a scalable proof mechanism. | `A002`, `A003`, `E002`, `STATE.md` |
| 2026-07-23 | Import only precisely matched results from the inspected 2022–2026 primary papers, and keep the original 1997 source marked uninspected. | This distinguishes verified statement correspondence and usable external theorems from bibliographic or search-result reports. | `STATEMENT.md`, `CLAIMS.md`, `OBLIGATIONS.md`, `references/source-audit-2026-07-23.md` |
