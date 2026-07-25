# O012 — migrate the E024 order-21 rung to Railway: linux/amd64 generator rebuild, anchor re-gate, and wide res/mod splitting

- Date: 2026-07-25
- Classification: repository operation (not mathematical research)
- Status: **PLANNED — nothing executed.** No Railway project, service,
  volume, or deployment was created; no job was launched; no local job was
  stopped. This record is the specification for a later operator.

## Scope

Move the compute of `E024` (the order-21 \(\mathcal G\)-profile ladder rung,
launched at the `S023` close and still running on the laptop) from 8 local
cores to Railway, so that it finishes in about an hour instead of about
fifteen, and frees the laptop.

Affected systems: the `E019` generator binary (`genc48` = nauty `geng` plus
the recorded PREPRUNE \(C_8\) plugin), `E024`'s driver `rung21.py`, and a new
container image. **Untouched:** every problem dossier. This changes *where*
`E024` runs, not *what* it computes. No statement, claim, obligation, proof,
review, status, or session record is altered by this operation.

## Why this job and not the others

- `E024` is already split into **16 independent `geng` res/mod parts**, and
  `geng`'s splitting takes an arbitrary modulus. It parallelises perfectly
  and needs no new code to go wider.
- The laptop has 12 cores and is running 8 parts; the remaining 13 parts are
  the entire wall-clock cost.
- `E028`'s ladder is **deliberately excluded**: each rung is a single
  Python/PyPy process, so more cores buy nothing per rung, and cloud cores
  are not faster than this laptop's performance cores. Parallelising that
  search (splitting on the first chord choice) is new work and is not part of
  this operation.

## Sizing and cost (Railway pricing as of 2026-07-25)

Billing is usage-based: **$20 / vCPU-month ≈ $0.027 / vCPU-hour**, $10 /
GB-month for RAM, plus the plan subscription. The consequence that drives the
design: **width is nearly free.** Spreading a fixed number of core-hours over
150 cores costs the same as over 8 — only the wall clock changes.

| Plan | vCPU ceiling per service | Realistic wall clock for the E024 remainder |
|---|---|---|
| Free / Trial | 1–2 | unusable |
| Hobby ($5/mo) | 48 (6 replicas) | ~3–6 h |
| **Pro ($20/mo)** — selected | **1,000 (42 replicas)** | **well under 1 h** |

Work remaining: the S023 estimate was ~21 h on 8 workers ≈ **~170 core-hours
total**; 3 of 16 parts had finished after 5 h 35 m, so **~135 core-hours
remain**. At $0.027/vCPU-hour that is **≈ $4–6 of CPU**, plus a few dollars
of RAM (the generator is memory-light; budget 0.5–1 GB per part), so
**≈ $10 all-in** on top of the $20 subscription.

Caveat to carry into the estimate: an Apple M-series performance core is
typically **faster** than a cloud vCPU on tight C code like `geng`, so budget
1.3–2× more vCPU-hours than the laptop figures suggest — call it 200–270
vCPU-hours, ≈ $6–8 of CPU. The conclusion is unchanged.

## Plan (for the operator who executes this)

1. **Image.** Build a `linux/amd64` container that compiles nauty **from
   source** inside the image together with the `E019` PREPRUNE plugin. Pin
   and record the nauty version and the plugin source hash in the image
   labels and in this record. Do not ship a prebuilt binary.
2. **Anchor re-gate — mandatory, blocking.** The repository pins `genc48` by
   sha256 (`E022/data/provenance.json`); a different-architecture rebuild
   breaks that pin, so the cloud binary is a *new instrument* until it passes
   the same gate the arm64 one did:
   - the full **146-check anchor suite**, output compared against the
     recorded `E019` anchor file;
   - the **cubic order-24 positive control** (must reproduce Markström's
     census — a nonzero control, so a silently broken build cannot pass);
   - at least one **set-equality cross-check** against a recorded class at a
     small order.
   Record the new binary's sha256 as an **architecture-tagged second pin**
   beside the arm64 one. Do not overwrite the existing pin. **No output from
   the cloud run is citable until this gate passes**, per the standing rule
   that anchors re-pass before any extension.
3. **Re-split rather than resume.** Do not try to resume the laptop's
   partial parts. Start a fresh run with a larger modulus (64 or 128 parts,
   so the longest part does not dominate). Partition-independence is already
   anchored — `C043` records a dual-split 16-vs-24 check with equal totals
   and `labelg` set-equal class files — but the new modulus must be recorded,
   and the stream total must be asserted equal to the 16-part total if both
   ever complete.
4. **Run.** One service, all parts concurrent within the plan's vCPU
   ceiling. Each part writes its class file and scan JSON exactly as
   `rung21.py` does locally.
5. **Retrieve and verify.** Output is small (class files plus JSON). Pull it
   down, verify per-part line counts against the reported tallies, and re-run
   the profile extraction **locally** so the harvested numbers come from the
   already-anchored local instrument.
6. **Cost guard.** Set the replica/vCPU ceiling explicitly before launching
   and check `railway metrics` after the first few minutes; the job is
   bounded, but a misconfigured restart loop is not.
7. **Keep the laptop run as fallback** until step 2 passes. Only then stop
   it. It is excluded from every ledger row either way.

## What the harvest must record (mathematical, handled in the dossier)

Not part of this operation, but the reason it is worth doing — for every
order-21 profile member found: \(\max S\) against \(n-1\) (**the
Hamiltonian / non-Hamiltonian split**, which is now the decisive
measurement), \(S\cap\{2,6,14,30\}\), and \(C_{16}\) presence.

## Work performed

Specification only. Account state was read (`railway whoami`, workspace
listing, pricing documentation) to size the job; nothing was created or
changed. The user's account is a personal workspace with one project; the
**Pro plan is the selected tier** and must be active before step 4.

## Verification

None yet — nothing was executed. The verification burden is entirely step 2,
and it is blocking by design.

## Dossier impact

**None from this operation.** The mathematical re-prioritisation that makes
this job worth doing (promoting the `E024` harvest, stopping the `E028`
ladder after order 30) is recorded separately in the `P-002` dossier —
`DECISIONS.md`, `STATE.md`, `problem.json`, `LOG.md` — as required by the
mixed-work split rule.

## Handoff

- Result: plan only; **no infrastructure exists yet**.
- Remaining operational follow-up: all seven steps above, in order, with
  step 2 blocking steps 4–7.
- Files a later operator should read: this record; `E019/README.md` (the
  generator build and its 146-anchor suite); `E022/data/provenance.json`
  (the existing sha256 pin); `E024/rung21.py` and its `data/rung21_status.json`
  (what has already finished locally); `C043` for the partition-independence
  precedent.
- Commit and push status: committed and pushed with the S027 follow-up.
