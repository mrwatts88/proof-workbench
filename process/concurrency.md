# Parallel sessions on one dossier

Two agents may work the same problem at the same time. This document says when
that is allowed, how the work is partitioned, and how the shared records are
written without one session silently overwriting the other.

The rules here are operational detail for the `AGENTS.md` section *Parallel
sessions*; that section is the contract, this file is how to satisfy it.

## Why a protocol is needed

The dossier is deliberately split into two kinds of files:

- **Owned records** — `attempts/A###`, `experiments/E###`, `sessions/S###`,
  `reviews/R###`. Each belongs to exactly one session and is never touched by
  another.
- **Shared ledgers** — `STATEMENT.md`, `problem.json`, `STATE.md`, `CLAIMS.md`,
  `OBLIGATIONS.md`, `PROOF.md`, `DECISIONS.md`, `LOG.md`, plus the repository's
  `PROJECT_STATE.md` and the generated `problems/INDEX.md` and `README.md`.

Owned records parallelize perfectly. Shared ledgers do not: two sessions in the
same working tree have no version-control boundary between them, so the second
writer overwrites the first. Two sessions in *separate* trees have a boundary,
but both will still have rewritten overlapping regions and one of them must
merge.

Everything below follows from that one asymmetry.

## When parallel work is allowed

Both conditions must hold.

1. **Disjoint owned records.** The two sessions' work lands in different
   `A###`/`E###`/`S###` files, allocated in advance (below).
2. **No unrecorded dependency.** Neither session's argument may consume a result
   the other has not yet committed. A sibling's in-progress reasoning is not
   citable; if session B needs session A's lemma, B waits for A's commit or
   proves it independently.

Do **not** run parallel sessions when:

- both would restate or promote the same claim row (they will collide in the
  one place merging cannot be mechanical);
- one session's route is a premise of the other's;
- the work is a required adversarial review — see *Independence* below;
- the second session exists only to add throughput to a single proof attempt.
  Proof work is bottlenecked on insight, not on hands; two agents reading the
  same records reach the same impasse twice.

The productive pairings are *mechanistically distinct routes to the same
target*, or *one proof route plus one tooling/verification task*.

## Record ID allocation

`proofctl.py add` assigns the next free number by scanning the tree it can see.
Two sessions therefore receive the **same** ID, and the collision only surfaces
at merge time.

The session that launches the parallel work allocates IDs in advance and passes
them to each agent explicitly:

```sh
python3 scripts/proofctl.py add <slug> attempt "<title>" --id A019
python3 scripts/proofctl.py add <slug> experiment "<title>" --id E016
python3 scripts/proofctl.py add <slug> session "<focus>" --id S019
```

`--id` refuses a number that is already used in that tree and refuses a
malformed one. It does not and cannot detect an allocation made in a sibling
tree, so the launching session is responsible for handing out disjoint blocks —
conventionally consecutive numbers, one block per agent, recorded in the
launching session's record.

## Isolation

Prefer a **separate git worktree per agent**:

```sh
git worktree add ../rh-agent-b -b <branch>
```

Each agent then has its own checkout, its own index, and a real merge boundary.
Without it, parallelism relies on the agents never touching a file at the same
moment, which is not a property anything enforces.

A single shared tree is permissible only when the sessions are strictly
sequenced on the ledgers (below) and each announces itself in its session
record. That is what `S016`/`S017` did on 2026-07-24; it worked, but only
because the second session noticed the first mid-edit and deferred.

## Ledger discipline

**During the session:** each agent writes only its own owned records. No ledger
edits, no `set-status`, no `index`.

**At close:** ledger writes are serialized. One session at a time performs the
full canonical checkpoint — `CLAIMS.md`, `OBLIGATIONS.md`, `PROOF.md`,
`DECISIONS.md`, `LOG.md`, `STATE.md`, `problem.json`, index, validate, commit,
push — and only then does the other begin its own.

The second finisher must **re-read every ledger it is about to change** before
writing. The state it saw at session start is stale by construction: the first
finisher may have added claim rows, changed the next action, or rewritten
`STATE.md` wholesale.

### The punch list

If an agent must close while the ledgers are held by its sibling, it records its
pending ledger edits verbatim in its own session record under a heading
`## Deferred ledger edits (punch list)`, commits its owned records, and reports
the dossier as **not yet reconciled**. The next session applies the punch list
before doing anything else.

This is a real closure path, not an escape hatch: the session is closed only
when the punch list has been applied by someone.

### Conflicts

On a merge conflict in a ledger, re-read the incoming version and re-apply your
rows on top of it. Never resolve by taking your whole file, and never force-push
over a sibling's commit. A conflict in `CLAIMS.md` or `PROOF.md` is a signal
that the two sessions were not as disjoint as claimed — record that in both
session records.

## Cross-session declarations

Each parallel session records, in its **Starting checkpoint**:

- that a sibling session is active, with its ID and one-line scope;
- which record IDs it was allocated;
- an explicit statement that it did not consume the sibling's uncommitted
  results;
- whether it holds or defers the ledgers.

Each records, in its **Ending checkpoint**, whether it performed the canonical
checkpoint or left a punch list.

## Independence is unaffected

A sibling session is **not** a fresh reviewer. Parallel execution does not
satisfy the mandatory adversarial-review delegation of `AGENTS.md`, and two
agents that agree do not corroborate each other: they may share the framing,
the records, and the same blind spot. Review independence is governed solely by
`process/harness.md`, and a review must still come from an agent with no
discovery context.

The same applies to discovery: a sibling's route memo is speculative input, at
exactly the strength a `proof-explorer` memo would carry.

## Machine resources

Parallel agents share one machine, and long searches are the usual reason to
run them at all.

- Check load before launching a heavy job; a saturated machine turns two
  parallel searches into two slow searches plus contention.
- Record the interpreter, the command, and — when it materially affects the
  timings a later session will plan from — the contention. Timings recorded
  under an unrelated 700%-CPU neighbour are not comparable to clean ones.
- A background job must be documented in the session record with the exact
  re-run command, and **its results may not be claimed until it finishes**. An
  unfinished leg is excluded from every ledger row; the harvest is a named
  follow-up. See `C032` (order 16) and `C034` (order 22) for the precedent.

## Checklist

Launching session:

- [ ] confirm the two routes are mechanistically distinct and dependency-free
- [ ] allocate disjoint record IDs and write them into the launch record
- [ ] create a worktree per agent, or declare the shared-tree sequencing
- [ ] state which agent holds the ledgers first

Each parallel session:

- [ ] declare the sibling, the allocated IDs, and the ledger hold in the
      Starting checkpoint
- [ ] write only owned records during the work
- [ ] at close, either perform the full checkpoint or leave a punch list
- [ ] re-read the ledgers before writing if finishing second
- [ ] commit only session-scoped files; never stage a sibling's records
