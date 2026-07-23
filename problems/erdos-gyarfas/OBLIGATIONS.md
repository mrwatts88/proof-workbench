# Proof obligations

An obligation is resolved only when the resolution column links to an exact proof,
counterexample, decision, or certificate.

| ID | Obligation | Status | Blocks | Resolution |
|---|---|---|---|---|
| G001 | Normalize the statement, definitions, quantifiers, negation, and boundary conventions. | resolved | All research | `STATEMENT.md` version 0.1; `DECISIONS.md` |
| G002 | Use or strengthen `L001` to prove the power-cycle conclusion for a 2-connected graph with at most one degree-\(2\) vertex and every other degree at least \(3\). | open | `C001` | — |
| G003 | Find a global mechanism that upgrades the absence of a \(4\)-cycle, plus the minimal-counterexample restrictions, into a forced cycle of length \(8,16,\ldots\). | open | `C001` | `L005`–`L006` close only two finite orders |
| G004 | Complete source correspondence by inspecting the original 1997 article body and, where needed, the original Markström computation rather than later reports. | in_progress | Full provenance and prior-bound verification; not the formal truth of version 0.1 | Partial audit in `references/source-audit-2026-07-23.md` |
| G005 | Extend exact \(C_4\)-free enumeration from order \(9\) through order \(10\), with auditable degree sequences and survivor structure. | resolved | Selection of the next structural lemma; not a universal proof by itself | `E002`, `A002/L005`, `A003/L006` |
| G006 | On the induced \(P_{13}\) forced by `C007`, classify how the cubic dominating set from `C005` can attach, and prove that a surviving attachment pattern yields a \(4\)-, \(8\)-, or \(16\)-cycle—or exhibit a pattern that refutes this route. | resolved | A scalable route to `C001` | `A004/L007` gives a complete cubic large-girth graph satisfying the structural bundle while avoiding all three lengths |
| G007 | Find a genuinely global restriction on a minimal counterexample that is not shared by arbitrary connected cubic graphs of girth at least \(17\), and use it noncircularly to force some power-of-two cycle. | in_progress | A replacement scalable route to `C001` | `L008`–`L014` supply, stress-test, and delimit the saturation restriction, but the cycle-forcing step remains open |
| G008 | In the saturated block from `L011`, convert the Mersenne-path witnesses and odd-cycle ears into adjustable even cycle lengths, or exhibit an exact overlap/length obstruction that retires this route. | in_progress | Completion of the saturation route toward `C001` | `L012`–`L013` supply ears in all shortest-odd-cycle cases; `L014` proves that one-ear theta lengths alone are insufficient, so the full witness intersection pattern remains |
