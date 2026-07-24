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
  **nineteen** vertices; order-18 census empty across 834,711,846 graphs;
  extremal \(\{C_4,C_8\}\)-free window \([19,24]\); census capped). S010
  proved the **collision-wall theorem** (`L024`, with the arc-digraph
  structure package `L023`): for every finite voltage group, every
  connected minimum-degree-3 base, and every assignment,
  identity-voltage tailless non-backtracking closed walks exist at every
  length \(\equiv0\bmod4\) (every even length if non-bipartite) past
  \(4\log_2\lvert\Gamma\rvert+C_B\). It passed a delegated fresh-context
  logic audit (`R001`, pass; minor findings repaired) with two
  independent machine verifications, resolving `G012` and closing the
  voltage-lift falsification program as a theorem rather than an
  observation. Portfolio: proof-side walk-to-cycle interface (primary —
  the theorem's trivial-group reading forces balanced walk intervals,
  and the conjecture's hard core is now converting forced walks into
  cycles), saturation-constrained transfer (alternative), census capped
  and complete.
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

For `P-002`, open the proof-side walk-to-cycle attempt: (1) a
deliberate literature sweep on cycle-length intervals and mod-\(k\)
cycle lengths at minimum degree 3, importing the strongest
primary-source results; (2) formulate the walk-to-cycle transfer lemma
candidate — what cycle lengths must follow from the forced balanced
walk intervals of `L024` plus 2-connectivity/saturation constraints;
(3) failure-first: measure the walk-vs-cycle length gap on large-girth
cubic graphs and the order-24 extremal graphs. Kill test: an unbounded
walk/cycle separation in 2-connected minimum-degree-3 graphs retires
bounded transfer. No required action remains for `P-001`; its reference
comparison is optional and freely permitted.

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
