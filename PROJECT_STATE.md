# Project state

Last reviewed: 2026-07-24

## Mission

Find genuinely open conjectures and settle them — by proof, disproof, or
precisely delimited new partial results. Lean on all existing verified
knowledge to stand at the published frontier immediately; the work that counts
is what passes the frontier and produces information the mathematical
community does not already have. Re-deriving known results for internal
provenance is explicitly not a goal. The repository makes uncertainty visible
and every status promotion auditable.

## Current phase

The first problem, worked before the mission was clarified, has an internally
proved result that passed its adversarial review gates. The active research
dossier targets the Erdős–Gyárfás conjecture, which is open in the literature.

## Active problems

- `P-001` — Unique Common Neighbor: proved internally for statement version
  0.2. It was historically run under a since-retired internal-only rule, so no
  reference comparison has yet been made; that comparison is now freely
  permitted and simply optional.
- `P-002` — Erdős–Gyárfás Conjecture: active and open at statement version 0.1.
  The finite frontier stands at `L022` (every counterexample has at least
  **nineteen** vertices; extremal \(\{C_4,C_8\}\)-free window \([19,24]\);
  census capped at order 18). The voltage-lift falsification program is
  closed as a theorem (`L023`/`L024` collision-wall, reviewed `R001`);
  the walk-to-cycle interface is the **atom question** (`L025`, `G013`).
  S012 rebased the rung ladder on **taut** gadgets (`L026`–`L029`:
  unrestricted rungs are conjecture-complete; lobes confine hiding;
  taut \(s_{\min}\le2\) closed; cubic reduction modulo 1-atoms). S013
  closed the next rung as a theorem (`L030`): no vertex-taut
  \(C_4\)-free (D)-gadget has \(S\subseteq\{3,4,5\}\) — the middle
  layer collapses under the path-length ceiling and the surviving
  three-matchings skeleton always carries a \(C_4\) or a length-7 path.
  \(C_4\)-freeness alone carries this rung too, refuting S012's
  prediction; taut 2-atoms now have \(s_{\min}\ge4\), \(s_{\max}\ge6\),
  and every 2-atom with \(s_{\min}\le3\) routes through the 1-atom
  question. Falsification search (`E012`/`C029`): zero targets at
  orders 6–14 over **all** terminal pairs (first coverage of
  degree-\(\ge3\) terminals); the endgame dichotomy exact on all 218
  small structures. Boundary map: \(C_4\)-only provably fails at
  \(s_{\min}=6\) (`C028`'s five witnesses, each with a \(C_8\)), so the
  power fight lives in \(s_{\min}\in\{4,5,6\}\). Portfolio: the taut
  \(s_{\min}=4\) rung via the collapse mechanism (primary; depth-2
  middles are the new case), \(C_8\)-forcing at the \(s_{\min}=6\)
  witnesses (alternative), 1-atom structure theory, order-16 census
  (deferred).
- See the generated [problem index](problems/INDEX.md).

## Repository-wide decisions

- Each problem is a self-contained dossier under `problems/<slug>/`.
- Workflow maturity and mathematical outcome are tracked separately.
- Atomic claims and unresolved obligations are first-class records.
- A proof is not complete until adversarial reviews and promotion gates pass.
- Agents initiate and delegate those reviews automatically when a candidate
  appears; humans do not schedule the review lifecycle. Delegation to a fresh
  reviewer is mandatory wherever the harness supports it, and how independence was
  obtained is recorded on the review.
- The operating contract is harness-neutral and works in either Codex or Claude
  Code; harness-specific files configure a harness but never hold process rules.
- Every internally proved result has a standalone LaTeX source, and the generated
  README dashboard displays both current status and prior-proof provenance.
- A proved result also has a committed PDF compiled by Tectonic, with the source,
  PDF, and compiler version recorded in its dossier.
- Repository process and tooling work is recorded separately under `operations/`;
  it does not count as progress on a mathematical dossier.
- Session continuity comes from concise handoffs plus detailed append-oriented
  records, not retained chat history.
- A recorded next action is the previous session's best proposal, not a command.
  Each nontrivial exploration session audits it against a fast falsification move
  and a mechanistically distinct alternative or reframing before committing.
- External knowledge is leaned on, never avoided: published theorems, bounds,
  computations, and examples are imported at their verified strength so work
  starts at the frontier. There is no internal-first or no-consultation rule;
  the retired benchmark-era rule on `P-001` must not be reintroduced. Novelty
  relative to the literature is checked deliberately, because producing new
  information is the point.
- `STATE.md` and session records preserve a compact strategy portfolio: primary
  route, live alternative, and pivot trigger. Fresh discovery agents may reduce
  anchoring where the harness supports them, but their suggestions remain
  speculative until checked by the primary agent.
- Missing tools are internal research targets: when the obstacle is "no known
  technique applies," strategy audits weigh a tool-building attempt with a
  falsifiable first move and kill condition; capability-based deference is not
  a valid route-selection reason, and estimates stay calibrated regardless.
- Closing a substantive session includes a mandatory canonical-record checkpoint;
  the human shorthand `close session` invokes the whole checkpoint.
- Each closure preserves a plain-language recap, a subjective percentage estimate
  of the chance of eventually settling the exact current statement, and a
  plain-language statement of the proposed next step.
- Computational work must be reproducible and its logical scope must be stated.

## Next action

For `P-002`, attack the taut \(s_{\min}=4\) rung (`L030`'s successor):
prove that no vertex-taut \(C_4\)-free (D)-gadget with
\(S\subseteq\{4,5,6,7\}\) exists — extending the `L030` middle-layer
collapse to depth-2 middles, the genuinely new configuration — or find
a \(C_4\)-free taut pinched \(s_{\min}\in\{4,5\}\) gadget at orders
14–16 (`C029`: empty through 14 over all terminal pairs; \(C_4\)-only
closure provably fails at \(s_{\min}=6\)). A found gadget branches on
power-freeness: power-free disproves statement 0.1 via `L025`;
otherwise it marks where the \(C_8\) fight begins. Alternatives:
\(C_8\)-forcing at the \(s_{\min}=6\) witnesses; 1-atom structure
theory; order-16 census (deferred). No required action remains for
`P-001`; its reference comparison is optional and freely permitted.

## Known process risks

- A structurally valid dossier can still contain invalid mathematics.
- Independent review is a reasoning discipline, not something filenames can
  guarantee.
- Handoffs become misleading if agents omit the end-of-session checkpoint.
- Strategy audits can become empty ceremony if agents list cosmetic variants
  instead of comparing distinct mechanisms and acting on negative evidence.
- Imported results are only as good as their statement correspondence: a
  miscopied hypothesis or an overread bound silently corrupts everything built
  on it. Precise statements, matched hypotheses, and sources are mandatory.
- Effort can silently drift into re-deriving known results; route selection
  must ask what the work adds beyond the published frontier.
