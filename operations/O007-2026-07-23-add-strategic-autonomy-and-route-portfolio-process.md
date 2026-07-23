# O007 — Add strategic autonomy and route-portfolio process

- Date: 2026-07-23
- Classification: repository operation (not mathematical research)

## Scope

Strengthen the research process against strategy anchoring and mechanical
execution of an inherited next step, while preserving the existing proof
standard, provenance rules, adversarial review gates, status discipline, and
mandatory closure checkpoint.

Affected systems: the harness-neutral contract, workflow and toolkit guidance,
record semantics, future session/attempt/dossier scaffolds, harness notes,
repository overview, validator, and structural tests.

No mathematical problem dossier is in scope. In particular, neither `P-001` nor
`P-002` has any statement, state, claim, obligation, proof, decision, log,
attempt, experiment, review, session, status, or next action changed.

## Work performed

### Next action as a proposal

- Added `AGENTS.md` strategic-autonomy rules: `next_action` is the previous
  checkpoint's best proposal, not an instruction.
- A nontrivial exploration session now audits that proposal before committing:
  why it might work, the fastest falsification, a mechanistically distinct
  alternative or reframing, the selected route, and a pivot criterion.
- Agents are explicitly authorized to postpone, replace, or retire a route when
  mathematical evidence warrants it, without asking the human to approve a
  strategy change inside the authorized research scope.
- Intake, required review or reproduction, and mechanical closure are exempt
  from performative brainstorming.

### Generation, selection, and persistent recalibration

- Expanded `process/workflow.md` and `process/toolkit.md` to separate the
  generative phase from the critical phase and compare routes by information
  gain, leverage, falsifiability, and unsupported dependencies.
- Defined four useful route roles—primary, falsification, alternative, and
  reframing—without imposing a numeric idea quota.
- Added a compact route portfolio to future `STATE.md` scaffolds and added
  strategy-audit and recalibration fields to session records.
- Attempts now record their portfolio role and their kill or pivot criterion.
- Kept the single machine-readable `next_action`; a separate `STRATEGIES.md` or
  manifest schema was deliberately not added because it would duplicate the
  concise portfolio already appropriate for `STATE.md`.

### Fresh discovery without weakening review

- Added optional fresh-context discovery guidance. An explorer initially sees
  the exact statement, established claim strengths, obligations, and sources,
  but not the inherited next action or discovery narrative. External literature
  remains disabled unless the invoking prompt explicitly permits it, preserving
  benchmark and source-isolation decisions.
- Added Claude Code's read-only `.claude/agents/proof-explorer.md` role and
  harness instructions. Its memo is explicitly speculative, not a review or
  mathematical support.
- Corrected the Codex capability note: when collaboration subagents are exposed
  in a session, both mandatory review delegation and optional no-history
  discovery delegation are available; the clean-session exemption applies only
  when they are genuinely absent.
- The primary agent remains responsible for comparing, stress-testing, and
  recording any delegated ideas.

### Guardrails and documentation

- Updated `README.md`, `PROJECT_STATE.md`, and `process/records.md` with the new
  semantics and the risk that a strategy audit could itself become empty
  ceremony.
- Extended `proofctl.py validate` with required markers for the autonomy
  contract and future scaffolds.
- Added an integration test that creates a dossier, session, and attempt,
  verifies the strategy fields, and confirms validation detects a removed
  strategy-audit marker.
- Left all proof/disproof promotion gates and epistemic rules unchanged.

## Verification

- `python3 -m unittest discover -s tests` — passes 11 integration tests.
- `python3 scripts/proofctl.py validate` — passes for both existing dossiers.
- `git diff --check` — passes.
- Manual inspection confirmed that the strategy requirements agree across
  `AGENTS.md`, `process/workflow.md`, the record templates, harness guidance,
  and the repository handoff.
- Manual inspection confirmed that no file under either live problem dossier
  changed.

## Dossier impact

None. This is purely operational work. The files under
`problems/unique-common-neighbor/` and `problems/erdos-gyarfas/` are untouched,
as are both problem manifests and the generated problem index.

## Handoff

- Result: future agents must audit inherited strategies, preserve a compact route
  portfolio, and pivot on evidence while retaining the repository's existing
  rigor and review gates.
- Remaining operational follow-up: none required. Optional — after several
  research sessions, inspect whether route portfolios are substantive or merely
  templated, and adjust prompts rather than adding more fields if they become
  ceremonial.
- Files a later operator should read: `AGENTS.md`, `process/workflow.md`,
  `process/toolkit.md`, `templates/session.md`, `process/harness.md`, and
  `.claude/agents/proof-explorer.md`.
- Commit and push status: included in this operation's closure commit and push.
