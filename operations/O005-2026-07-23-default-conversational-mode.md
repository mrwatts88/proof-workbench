# O005 — Default conversational mode

- Date: 2026-07-23
- Classification: repository operation (not mathematical research)

## Scope

Make conversational interaction the default outside an explicit request to act,
even when the topic is the repository or its process. No problem dossier is
affected.

- Added the `Conversational default` section to `AGENTS.md`.
- Added the same boundary to workflow classification guidance.
- Defined clear authorization verbs (inspect, change, build, record, test,
  commit, deploy) and the rule to answer first when a request is ambiguous.

- Inspected the agent contract to confirm this rule appears before workflow
  classification and therefore applies before any repository action.
- Repository validation and integration tests are run at closure.

## Dossier impact

None. No mathematical statement, claim, obligation, proof, review, status, or
research session changed.

## Handoff

- Result: casual discussion no longer authorizes repository activity by default.
- Remaining operational follow-up: none.
- Files a later operator should read: `AGENTS.md` and `process/workflow.md`.
- Commit and push status: included in this operation's closure commit and push.
