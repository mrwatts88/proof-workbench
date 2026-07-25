# O013 — document when to use rented compute, and the measured constraints that decide it

- Date: 2026-07-25
- Classification: repository operation (not mathematical research)
- Status: complete.

## Scope

`O012` moved one job to Railway and, in doing so, measured several things no
record stated: what a service actually gives you, what splitting a search
actually costs, and what a rebuilt binary has to survive before its output may
be cited. Those measurements were sitting inside a single operation record about
a single run. This operation lifts them into a standing process document, so the
next agent knows rented compute is available, when it is worth reaching for, and
what discipline it carries.

Affected: `process/compute.md` (new), `process/README.md` (index), `AGENTS.md`
(one bullet under tool and file discipline). **Untouched:** every problem
dossier. No statement, claim, obligation, proof, review, status, or session
record is altered.

## Work performed

Wrote `process/compute.md`, covering:

- **The ordering rule.** The first question is never "can this be parallelised"
  but "is this computation worth doing at all". The standing example is `E028`:
  genuinely parallelisable (its DFS branches at position 0 over a single chord,
  giving \(\approx M\) independent root subtrees) and stopped anyway, because
  above order 26 the rungs no longer exercised the mechanism the proof needs.
  Scaling a doubtful computation buys the doubtful answer sooner and bills for
  it.
- **What a service actually is.** A Railway Pro service is capped at **24 vCPU /
  24 GB**; the pricing table's 1,000 vCPU is a per-service ceiling *including
  replica multiplication*, divided across the 42-replica maximum. Inside the
  container `os.cpu_count()` reports the host's 48 and is misleading — trust
  `railway metrics`. Concurrency therefore comes from more services, not bigger
  ones, and over-provisioning workers silently inflates every per-part timing
  one then reasons from.
- **Machine parity.** A cloud vCPU matched an M-series performance core on a
  fixed single-threaded leg (1,085.6 s against a recorded 1,069.6 s). Do not
  budget a slowdown factor without measuring one; `O012`'s original planning
  caveat did, and was wrong.
- **Splitting is not free.** Where each part redoes shared work before finding
  its own, total work is \(\text{mod}\times A+B\): cost rises linearly with the
  modulus, and with one wave the wall clock has a floor of
  \(\text{skew}\times A\) that no modulus beats. Fit \(A\) and \(B\) on a cheap
  order first; calibrate on an order already in the dossier so the sweep doubles
  as an exactness check; extrapolate ratios rather than absolutes, since \(A\)
  grows more slowly with order than total work does.
- **A rebuilt instrument is a new instrument** — the blocking gate, stated
  generically: full anchor suite compared field for field, at least one
  *nonzero* positive control, a set-equality cross-check against a recorded
  class, a partition check at the production modulus, byte-identity of copied
  sources, comparison performed locally against the dossier, and the new hash
  recorded as an architecture-tagged **second** pin beside the original rather
  than over it. Keep the local run as fallback until the gate passes.
- **Retrieval as part of the computation**: per-file hashes recorded by the
  producer, the parts forming the full residue system exactly once, each part
  self-describing as what it is filed under, the instrument's own coverage
  identities re-checked on this side of the wire, and the harvest run with the
  local anchored instrument.
- **The silent-truncation trap**, generalised from `E019/scan.py`'s
  `SAVE_LIMIT`: check whether the instrument *drops* output above a threshold
  before choosing a split, and check the "what was dropped" report before
  treating a result list as complete. This can justify a wide split on its own,
  independently of speed.
- **Cost guards** (`restartPolicyType: NEVER` for batch work, check metrics
  early, tear down after retrieval) and **where it gets recorded** (the run is
  an `O###`; the harvest is a session; an unfinished job is excluded from every
  ledger row).

Added the document to `process/README.md`'s reading order — and, while there,
added `concurrency.md`, which existed but had never been listed.

Added one bullet to `AGENTS.md` under tool and file discipline stating that
rented compute is available but is neither a default nor a reward for
parallelisability, and that a binary rebuilt on a different architecture is a
new instrument that must re-pass its anchor gate. The contract states the rule;
`process/compute.md` carries the detail, per the existing convention that
harness- and procedure-level detail lives under `process/`.

## Verification

`python3 scripts/proofctl.py validate` passes. No tests cover prose process
documents; the enforceable behaviour referenced (the anchor gate, the ledger
exclusion of unfinished background jobs) is unchanged and already carried by
existing contract text.

## Dossier impact

None. This records how to run computations, not the result of any.

## Handoff

- Result: `process/compute.md` exists and is indexed; `AGENTS.md` points at it.
- Remaining operational follow-up: none. Re-measure the figures if the platform
  or the instrument changes — they are dated in the document for that reason.
- Files a later operator should read: `process/compute.md` first; `O012` for the
  worked example and raw numbers; `E024/deploy/README.md` for the runnable
  recipe.
- Commit and push status: committed and pushed with this record.
