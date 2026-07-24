# Project state

Last reviewed: 2026-07-23

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
  The S007 frontier sweep imported the true primary-source bounds (exposing
  the circulating "17 vertices" as an overread), confirmed by recorded sweep
  that the edge-maximal saturation reduction is absent from the literature,
  verified the extremal 24-vertex graphs, and proved the computer-assisted
  bound `L018`: every counterexample has at least eighteen vertices — past
  the strongest published general bound (sixteen, 2002). The portfolio now
  has three named routes: saturation strengthening (proof side),
  interval/spectrum-density mechanisms (proof side), and a Bensmail-style
  spectrum-gap program in 2-connected blocks (disproof side); the exact
  census layer is explicitly capped.
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

For `P-002`, analyze all four verified order-24 extremal graphs as test
material for the two deep routes: full even-cycle spectra and witness
structure, checked against the consecutive-even-lengths and
cycle-pair-forcing mechanisms, ending in the first concrete lemma target
for either the saturation-strengthening or the spectrum-gap route. The
deferred alternative is extending the exact census to order 18 with a
compiled filter. No required action remains for `P-001`; its reference
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
