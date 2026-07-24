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
  taut-relativized (`L026`–`L029`), closed \(C_4\)-only through
  \(s_{\min}=3\) (`L030`), and collapsed onto **blocks** by S014
  (`L031`/`L032`: taut 2-atoms exist iff a power-free vertex-taut
  2-connected core with \(s_{\max}\le2\,s_{\min}\) exists). **S015
  proved the band-4 pencil dichotomy (`L033`)** — in any graph with
  \(d(x,y)=4\), either two internally disjoint 4-paths exist
  (equivalently a \(C_8\) **through both terminals**) or all 4-paths
  share one internal vertex; no \(C_4\)-freeness needed, and under
  \(C_4\)-freeness the pencil is terminal-adjacent with a rigid fan —
  so band 4 of the block question is exactly the **pencil endgame**:
  no vertex-taut 2-connected \(C_4\)-free core with \(d(x,y)=4\),
  \(s_{\max}\le8\) can be pencil-type. Catalogue through order 15
  (`C032`): block world stable at five equality blocks (P10 =
  Petersen\(-e\) the only band-4 core, disjoint-type), no strict block,
  the strict-15 scan = exactly D14's predicted pendant lift, closed
  bands 4–7 only. Hypothesis necessity (`C033`): with \(C_4\)s allowed,
  strict blocks exist from order 6 and \(C_8\)-free band-4 equality
  cores from order 9 — \(C_4\)-freeness is essential to both rungs.
  Three hand constructions against the endgame died to the cascade
  obstruction (`A015`). **Mid-session a user-supplied external memo was
  audited (`A016`) and its core confirmed as `L034`:** the ring
  criterion is any-\(L\)-sumset avoidance, not just the pinch — parity
  (all-odd \(S\); bipartite instance), odd-prime gcd, and mod-4
  channels join the pinched one (fatal invisible shapes:
  \(S=\{3,7\}\), \(\{2,6\}\)); all channels are empty through order 15
  because `C027` is profile-agnostic; the "pinch = the criterion"
  glosses are retracted (no proved row false); the program ceiling is
  explicit (assembly closure + 1-atoms = cubic reduction, not 0.1);
  `G014` opened for the memo's unverified literature/census leads.
  **S016 proved `L035`, the parity structure theorem**: for a
  vertex-taut two-terminal graph, parity-constancy of the through-set
  is *equivalent* to bipartiteness, so (a) any connected bipartite
  power-free graph with \(\le2\) sub-cubic vertices disproves 0.1 with
  no path enumeration and no external import, and (b) bipartite
  generation is exhaustive for `L034` channels (i) and (iii) modulo
  1-atoms. `E015`/`C034` then searched that class exhaustively: **no
  power-free member at any order \(\le21\)** (22 with a pendant) —
  six orders past the general wall — every member blocked by a
  \(C_8\), never fewer than 13 of them; by-products at the same
  orders: no bipartite 1-atom and no bipartite counterexample
  (verifying internally the range `G014` item 2 was to supply, which
  is now de-gated). Not covered: `L034` channel (ii), the
  odd-prime-gcd channel (\(\Theta(3,3,3)\) is vertex-taut and
  non-bipartite with \(S=\{3\}\)) — now the only congruence channel
  with no structure theory.
  Portfolio (all threads carried, per standing user instruction): the
  pencil endgame + band-2 rung (pinched channel); the bipartite hunt
  at order 22+ and the new gcd-channel theory question; the cubic
  census at order 30; census mining; bipartite EGC and Carr 4/7 → 1
  (proof side); 3-connectivity leverage; 1-atom theory; order-16
  pinched catalogue (a separate agent's in-flight scan from S015,
  untouched by S016).
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

For `P-002`, finish the **order-22 leg of the `E015` bipartite hunt**
(launched in S016, left unfinished on a loaded machine, so order 22 is
excluded from `C034`): any power-free member is an immediate disproof
by `L035` T3, an empty run extends the parity/mod-4 exclusion by one
order. Then open **Thread B3**, the one congruence channel `L035` does
not reach: does condition (D) forbid \(\gcd(S)\) from having an odd
prime factor? \(\Theta(3,3,3)\) shows the degree condition, not
parity, must do the work, and the `L035` fan argument suggests a
mod-\(p\) analogue to try. The **pencil endgame** stays co-primary on
the pinched channel, and every other thread in `STATE.md`'s portfolio
stays live per the standing instruction. No required action remains
for `P-001`; its reference comparison is optional and freely
permitted.

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
