# S002 — Exact C4-free frontier and survivor analysis

- Date: 2026-07-23
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1
- Work / claim status: `active` / `open`
- Strongest established facts: `L001`–`L004`, especially edge-minimal
  high-degree independence and the order-\(9\) lower boundary
- Open obligations in scope: `G003`, global forcing; `G005`, exact
  \(C_4\)-free enumeration from order \(9\)
- Session goal: extend the exact finite frontier, convert survivor patterns
  into proofs where possible, and then compare the route against primary
  literature
- Falsifiable next move: enumerate every degree sequence and graph satisfying
  the proved edge-minimal conditions at orders \(9\) and \(10\)

## Work performed

- Opened `A002` and used the codegree budget, handshake parity, and `L002` to
  prove `L005`: order \(9\) is impossible.
- Built `E002`, a deterministic exact backtracker that:
  - derives feasible degree sequences from exact inequalities;
  - fixes a nonincreasing degree placement, which covers every isomorphism
    type after relabeling;
  - forbids high-to-high edges by `L002`;
  - rejects an edge exactly when it closes a \(4\)-cycle;
  - checks connected completions for an \(8\)-cycle.
- At order \(10\), `E002` left only cubic graphs and the sequence
  \((4^2,3^8)\); every completion in both classes had an \(8\)-cycle.
- Opened `A003` and replaced that computational observation with a complete
  structural proof `L006`. The cubic case reduces to 2-regular remainders and
  a \(1,2,4\) theta/two-triangle dumbbell classification. The
  \((4^2,3^8)\) case reduces to an induced \(8\)-cycle.
- Searched and inspected primary research papers from 2021–2026, recorded in
  `references/source-audit-2026-07-23.md`.
- Imported the precisely matched minimal-counterexample, induced-\(P_{13}\),
  and high-average-degree results as `C004`–`C008`.

## Results

- Proved `L005` and `L006`: every counterexample has at least eleven vertices.
- Resolved `G005` with `E002` plus independent hand proofs.
- `E002` examined \(47{,}022\) search nodes at order \(9\) and found no
  \(C_4\)-free completion. At order \(10\), it found \(937{,}440\) cubic and
  \(10{,}080\) \((4^2,3^8)\) completions for the fixed degree placements; all
  contained \(C_8\).
- The May 2026 Carr preprint explicitly reports that the general conjecture
  remains open and proves cubic domination and a \(4/7\) cubic-vertex density
  in a minimal counterexample.
- The 2025 Hegde–Sandeep–Shashank computer-assisted theorem implies that every
  counterexample contains an induced \(P_{13}\).
- The 2023 Liu–Montgomery theorem supplies a power-of-two cycle above some
  absolute average-degree threshold, but does not reach minimum degree \(3\).
- Later primary papers corroborate the dossier statement; the original 1997
  article body remains uninspected.
- No proof or disproof candidate for `C001` exists.

## Failed routes and why

- Continuing the finite degree-budget approach to order \(11\) already leaves
  twelve degree sequences before graph generation. This is possible
  computationally but offers no scalable universal argument.
- The literature reports stronger finite searches, including a cubic
  counterexample lower bound of at least \(30\). Thus the internally proved
  order-\(11\) bound is a correctness result, not a new frontier.
- `L002` was independently derived in `S001`, but the literature audit showed
  that Markström had already observed its high-degree-independence conclusion.
- The original publisher page denied access to the 1997 article body, so exact
  original-source inspection remains incomplete.

## Adversarial check

- Re-derived the order-\(9\) and order-\(10\) degree sequences by hand from
  both the codegree budget and degree-sum parity.
- Checked that the high-to-low incidence inequality counts each pair of high
  vertices once per common low neighbor and uses no regularity assumption.
- Audited every \(C_8\) construction in `A003` edge by edge, including both
  2-regular cubic remainders, both suppressed multigraph types, and the shared
  neighbor subcase for \((4^2,3^8)\).
- Verified that suppressing the degree-\(2\) vertices in the cubic remainder
  yields only a theta or dumbbell multigraph, and enumerated all six
  length-\(4\) paths needed in the \(1,2,4\) theta.
- Added positive and negative \(C_4\)-creation tests, \(C_8\) boundary tests,
  and feasible-sequence-count assertions to `E002`.
- Kept the computational result at `tested`; `L005` and `L006` instead link to
  independent written proofs.
- Distinguished papers actually inspected from search snippets, and recorded
  externally reported computations as unverified rather than imported proofs.
- This is still a same-session self-audit, not an independent review of a main
  proof candidate.

## Canonical records changed

- [x] `STATEMENT.md`
- [x] `STATE.md`
- [x] `CLAIMS.md`
- [x] `OBLIGATIONS.md`
- [x] `PROOF.md`
- [x] `DECISIONS.md`
- [x] `LOG.md`
- [x] `problem.json` and index
- [x] Session-scoped changes committed
- [x] Commit pushed to configured upstream

## Ending checkpoint

- Current frontier: an internal proof excludes counterexamples through order
  \(10\); imported results force an induced \(P_{13}\), a dominating set of
  cubic vertices, and cubic density at least \(4/7\) in a minimal
  counterexample.
- Remaining blockers: `G002` and `G003`, the global cycle-forcing step;
  `G004`, original-source completion; `G006`, induced-path attachment analysis.
- Best next action: fix an induced \(P_{13}\), encode attachments from the
  cubic dominating set, and test whether every pattern avoiding \(C_4\) and
  \(C_8\) forces \(C_{16}\).
- Files a new session should read: `STATE.md`, `CLAIMS.md`, `OBLIGATIONS.md`,
  `A002`, `A003`, `E002/README.md`,
  `references/source-audit-2026-07-23.md`, and this session.

## Plain-language recap

We pushed the internal small-case proof two vertices farther: a counterexample
cannot have nine or ten vertices. The program independently checked every
necessary degree pattern, and the surviving order-ten graphs led to a complete
hand classification rather than a computer-dependent claim. The literature
check then put this in perspective: stronger finite computations were already
known, and the conjecture was still open in May 2026. More usefully, known
theorems say that any hypothetical smallest counterexample is mostly made of
degree-three vertices and contains a long path with no shortcuts. The next
session will combine those facts instead of checking one graph order at a time.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 2%
- Previous estimate, if any: 3%
- Reason for change: the literature audit shows that the correct internal
  finite progress lies below substantially stronger known computation and that
  many sophisticated special cases still stop short of the general conjecture
- Basis: the induced-\(P_{13}\)/cubic-domination route is concrete and
  falsifiable, but no scalable cycle-length mechanism has yet emerged and the
  known high-average-degree machinery does not operate at minimum degree \(3\).

This is a subjective research outlook, not mathematical evidence or a claim-status
promotion.
