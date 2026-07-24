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
  the walk-to-cycle interface is the **atom question** (`L025`, `G013`),
  taut-relativized by S012 (`L026`–`L029`) and closed \(C_4\)-only
  through \(s_{\min}=3\) by S013 (`L030`). **S014 collapsed the taut
  half onto blocks (`L031`/`L032`):** stripping a degree-1 terminal is a
  reversible through-path bijection onto a **core** at closed ratio
  \(s_{\max}\le2s_{\min}\), chains decompose at cut vertices, and
  bridge counting extracts — taut 2-atoms exist **iff** a power-free
  vertex-taut 2-connected core with \(s_{\max}\le2\,s_{\min}\) exists
  (the block question). The exact catalogue through order 14 (`E013`,
  `C030`/`C031`): six strict taut pinched gadgets (the five `C028`
  witnesses plus a new band-5 one at order 11), all pendant lifts of
  four 2-connected blocks; five blocks total including D14 (order 14,
  band 6); **every block at exact equality \(s_{\max}=2s_{\min}\)**, the
  band-4 block being Petersen minus an edge; no strict block through
  14; each block barred from power-freeness only by \(C_8\), and every
  \(C_8\) in the catalogue is a two-through-path symmetric difference.
  Sharpness: two Petersen\(-e\) blocks + a bridge form a strict taut
  core of order 20, so blocks (not cores) are the right level. Record
  repair: the "\(s_{\min}\in\{4,5\}\) empty through 14" summary now
  rests on `C030` (`C029` covered \(S\subseteq\{3,4,5\}\) only).
  Portfolio: the band-4 block rungs (primary — strict impossibility
  \(S\subseteq\{4..7\}\), equality \(C_8\)-forcing
  \(S\subseteq\{4..8\}\Rightarrow C_8\), via the disjoint-4-path
  interference mechanism), the order-15 closed catalogue as search leg,
  1-atom structure theory, order-16 census (deferred).
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

For `P-002`, attack the band-4 block rungs in the `L032` frame:
(i) prove no vertex-taut \(C_4\)-free 2-connected core (non-terminal
degrees \(\ge3\), terminal degrees \(\ge2\)) has
\(S\subseteq\{4,5,6,7\}\) (strict; empty through order 14 by `C031`);
(ii) prove every such core with \(S\subseteq\{4,\dots,8\}\) contains a
\(C_8\) (the first genuinely power-specific rung; Petersen\(-e\) is the
guide, and the candidate mechanism is two-path interference: an
internally disjoint pair of 4-paths closes into a \(C_8\) outright).
Search leg: extend the closed catalogue to order 15 under PyPy — a
strict block kills (i); a \(C_8\)-free equality block kills (ii) and
enters the disproof protocol (\(C_{16}\) check, pendant lift, ring);
it also tests D14's predicted unique order-15 strict witness.
Alternatives: 1-atom structure theory; the band-5 equality analogue;
order-16 census (deferred). No required action remains for `P-001`;
its reference comparison is optional and freely permitted.

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
