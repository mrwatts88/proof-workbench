# Where to run a computation

Rented compute is available to this repository and should be used when it buys
research time. It is not a default, and it is not a reward for a computation
being parallelisable. This document says when to reach for it, what it actually
costs, and what a cloud-produced number has to survive before it may be cited.

Everything numeric here was measured on 2026-07-25 during `O012` (moving the
`E024` order-21 rung to Railway). Re-measure rather than trusting these figures
if the platform or the instrument changes.

## The first question is not "can this be parallelised"

It is **"is this computation worth doing at all?"** Parallelising a job whose
value is in doubt just gets you the doubtful answer sooner and costs money on
the way.

The standing example is `E028`. Its ladder is genuinely parallelisable — the
search branches at position 0 over a single chord, giving roughly \(M\)
independent root subtrees — and it was nonetheless **stopped**, because an audit
showed that above order 26 the rungs had stopped exercising the mechanism the
proof needs. More rungs would have bought a floor and no understanding. The
right move was to stop, not to scale.

Ask, in order:

1. Would the result change the next research action? If no, do not run it
   anywhere.
2. Is the wall clock actually blocking? A job that finishes overnight on the
   laptop while you work on something else is not blocking.
3. Is the machine needed for something else? Freeing the laptop is a legitimate
   reason on its own.
4. Only then: does it split, and what does splitting cost?

## What it costs

- **$20 / vCPU-month ≈ $0.027 / vCPU-hour**, billed on usage.
- **A Railway Pro service is capped at 24 vCPU and 24 GB.** The "1,000 vCPU"
  figure in the pricing table is a per-service ceiling *including replica
  multiplication*, divided across the 42-replica maximum.
- **`os.cpu_count()` inside the container reports the host's 48 and is
  misleading.** Trust `railway metrics` (`cpu.limit`), not the process view.
  Running more workers than the quota only creates contention and silently
  inflates every per-part timing you then reason from.
- **Concurrency comes from more services, not bigger ones.** One service per
  block of ≤24 workers, each with its own volume.
- **A cloud vCPU is at parity with an M-series performance core** for tight C
  and PyPy work: a fixed single-threaded leg took 1,085.6 s in the cloud against
  1,069.6 s recorded on the laptop. Do not budget a slowdown factor without
  measuring one.

## Splitting is not free — measure it before choosing a width

The tempting model is "width is free: the same core-hours spread over more
cores, only the wall clock changes." **That is false whenever each part has to
redo shared work before it can find its own.**

`geng`'s `res/mod` splitting is the worked example: it assigns whole subtrees at
split level \(n-4\), so every part walks the entire tree *above* that level
first. Total work is

    total(mod) = mod × A + B

with `A` the duplicated prefix paid **once per part** and `B` the shared
remainder. Consequences:

- **cost rises linearly with the modulus**;
- with one wave (modulus = worker count) the wall clock is
  `skew × (A + B/mod)`, where `skew` is the largest part over the mean — so
  there is a **hard wall-clock floor of `skew × A`** that no modulus beats;
- the useful modulus sits at the knee, not at the maximum.

So: **fit `A` and `B` on a cheap order before committing the budget.** Two
moduli are enough. Calibrate on an order whose answer is already in the dossier,
so the sweep doubles as an exactness check of the split (each modulus must
reproduce the recorded class size). Extrapolate the *ratios* across orders, not
the absolutes — `A` grows more slowly with order than total work does, so an
extrapolation from a small order overstates it.

## A rebuilt instrument is a new instrument

The repository pins its binaries by sha256. **A rebuild on a different
architecture breaks that pin, and nothing the new build produces is citable
until it re-passes the gate the original passed.** This is blocking, not
advisory.

The gate, at minimum:

- the **full anchor suite**, compared field for field against the recorded file
  (exclude wall-clock and interpreter strings; require everything else equal);
- at least one **nonzero positive control** — a check that a silently broken
  build would fail, not merely an emptiness that a broken build also returns;
- a **set-equality cross-check** against a recorded class, which rules out the
  failure mode equal counts cannot: a part dropping one item and double-counting
  another;
- a **partition check at the production modulus** on the new build;
- **byte-identity of the copied sources** against the dossier.

Do the comparison **locally, against the dossier**, not inside the container.
Record the new hash as an **architecture-tagged second pin beside** the original
— never overwrite it. Keep the local run alive as a fallback until the gate
passes; only then stop it.

Match the interpreter version to the local one where you can. It costs nothing
and makes the anchor comparison exact rather than approximate.

### …but the gate attaches to the hash, not to the build event

**You only pay for the gate once.** A binary whose sha256 equals a recorded
gated pin *is* the instrument that passed those checks; re-running them
establishes nothing new. So a later cloud run must not repeat the gate — it must
**prove it is holding the same instrument**, which is cheaper and stronger:

1. **Keep the gated binaries in the repository**, with their hashes
   (`E019/prebuilt/linux-amd64/` is the worked example), and **install them**
   rather than recompiling. Copying them in is legitimate *because the pins
   identify a gated build*; it is not a way to skip the gate for a binary that
   never passed one.
2. **Assert the hashes inside the build**, and make the build fail if they do
   not match. Never weaken that assertion to get a build through — a mismatch
   means you are holding a different instrument.
3. **Pin the base image by digest, not by tag**, so the runtime does not drift
   underneath you either.

### Do not assume a rebuild reproduces the binary — it usually will not

This was tested, and the assumption failed. `O014` rebuilt the `E019`
instrument from identical sources, on a **digest-pinned** base image, and got a
**different `genc48`**. The cause: nauty's `./configure` appends
`-march=native` to the flags used for `gtoolsW.o`, `nautyW1.o`,
`nautilW1.o`, `naugraphW1.o`, `schreierW.o` — precisely the objects the
generator links. `-march=native` tunes code generation to the CPU of whichever
machine runs the build, and a cloud builder is not a fixed machine.

The consequence is the whole point of this section: **the gate cannot be
re-established by rebuilding.** The gate attaches to a hash; the rebuild does
not reproduce the hash; so the rebuilt binary is a *new instrument* requiring a
*new* gate. Preserving the gated binary is therefore necessary, not a
convenience.

Two further warnings from the same finding:

- **Identical hashes across several cloud builds are not evidence of
  reproducibility.** Layer caching makes repeat builds return the same layer
  without recompiling. Four builds agreed during `O012`; the first genuinely
  independent recompile disagreed.
- `-march=native` also makes the binary **tuned to the builder's CPU**, which
  is a portability hazard in a container. If a future gate is run deliberately,
  set `CFLAGS`/`MORECFLAGS` explicitly without it: the build becomes
  reproducible *and* portable, and thereafter a rebuild self-certifies against
  the pin. That is a new binary and needs its own gate, so it is a deliberate
  choice, not a change to slip in beside other work.

## Retrieval and verification

Getting numbers back is part of the computation, not an afterthought:

- verify **every file against the hash the container recorded** for it, so a
  truncated download cannot pass;
- check the parts form the **full residue system exactly once** — no gap, no
  part delivered twice by two containers;
- check each part **self-describes** as the order and part it is filed under;
- re-check the instrument's own **coverage identities** on this side of the
  wire;
- run the **harvest with the local, already-anchored instrument**, so the
  numbers that reach a ledger come from the build the repository has always
  trusted.

## The silent-truncation trap

Before splitting, check whether the instrument **drops output above a
threshold**. `E019/scan.py` writes a part's class file only when that part emits
at most `SAVE_LIMIT = 200,000` graphs — and the graph6 strings of the objects
the research actually wants live *only* in those files. An oversized part
discards them without erroring.

This is not hypothetical: at order 20 it left only 3 of 7 profile members
recoverable, and in the order-21 laptop run a single oversized part took 8 of
the 11 members found with it. **Choose the split so every part stays well under
any such limit, and check the run's "what was dropped" report before treating a
result list as complete.** A wide split can be justified by this alone, quite
apart from speed.

## Cost guards

- Set the restart policy to `NEVER` for a batch job; a bounded job is safe, a
  restart loop is not. Declare it in `railway.json` so it applies to every
  service built from that context.
- Check metrics a few minutes in, before walking away.
- Tear the services down once the results are retrieved and verified.

## Recording it

A cloud run is **operational work**: it changes *where* a computation runs, not
what it computes. It gets an `O###` record covering the image, the gate result,
the pins, the measured cost model, and the retrieval procedure. Commit the
deployment assets into the experiment's own directory so the run is
reproducible without the session's scratch space.

The **harvest is mathematical** and belongs to a session record with the usual
ledger reconciliation. Do not let an operation record carry a claim, and do not
let a research session become the diary for the infrastructure.

Until a background run is harvested, it is excluded from every ledger row. An
unfinished job's results may not be claimed.
