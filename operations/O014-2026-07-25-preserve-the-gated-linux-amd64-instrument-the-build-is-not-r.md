# O014 — preserve the gated linux/amd64 instrument; the build is not reproducible

- Date: 2026-07-25
- Classification: repository operation (not mathematical research)
- Status: complete and verified.

## Scope

`O012` gated a linux/amd64 build of the `E019` instrument at real cost — the
146-check anchor suite, the cubic order-24 positive control, the stream
cross-check at orders 12–17, a production-modulus partition check, all compared
locally against the dossier. That binary existed **only inside a container
image**. Railway retains images for 120 hours on Pro; after that a future run
would rebuild, and the working assumption was that a rebuild reproducing the
recorded hash would carry the gate with it.

**That assumption is false, and this operation establishes it.** Affected:
`E019/prebuilt/linux-amd64/` (new), `E024/deploy/Dockerfile` (rewritten),
`E024/deploy/Dockerfile.rebuild-from-source` (the previous compile version, kept
runnable), `E024/deploy/README.md`, `process/compute.md`. **Untouched:** every
problem dossier, and the running `E024` production job.

## The finding

A rebuild from identical sources, on a base image pinned by **digest** rather
than tag, produced a **different `genc48`** and failed the hash assertion.

Cause, confirmed from the build log: nauty's `./configure` sets
`MORECFLAGS = -mpopcnt -march=native` and uses it to compile `gtoolsW.o`,
`nautyW1.o`, `nautilW1.o`, `naugraphW1.o`, `schreierW.o` — precisely the
objects the `genc48` link line consumes. `-march=native` tunes code generation
to the CPU of whichever machine runs the build, and a cloud builder is not a
fixed machine.

Consequences:

1. **The gate cannot be re-established by rebuilding.** The gate attaches to a
   hash; a rebuild does not reproduce the hash; so a rebuilt binary is a *new
   instrument* requiring a *new* gate. Preserving the binary is necessary, not
   a convenience.
2. **Identical hashes across cloud builds are not evidence of
   reproducibility.** Layer caching returns the same layer without
   recompiling. Four `O012` builds agreed; the first genuinely independent
   recompile disagreed. The earlier reading of those four as evidence was
   wrong, and `process/compute.md` has been corrected — it previously said such
   builds are "reproducible in practice".
3. `-march=native` additionally makes the binary tuned to the builder's CPU,
   which is a portability hazard in a container. Recorded as the fix for any
   future gate: set `CFLAGS`/`MORECFLAGS` without it, and the build becomes
   reproducible *and* portable, after which a rebuild self-certifies. That is a
   different binary and needs its own gate, so it is a deliberate future
   choice, not something to slip in beside other work.

## Work performed

- Extracted the three gated binaries from the running gate service over
  `railway ssh` (streamed as base64; note the CLI parses `-p` out of a command
  string and drops shell quoting, so single commands without grouping are the
  workable form), decoded locally, and **verified each against its recorded pin
  before committing**: `genc48` `e8e839f6…4bb0` (175,224 B), `geng`
  `886e88a2…aa299` (174,744 B). `labelg` had no prior pin; its hash
  `c28c5273…1d7dd` (524,176 B) is now recorded, since the anchor suite uses it
  for canonical forms.
- Committed them to `E019/prebuilt/linux-amd64/` with a `MANIFEST.md` giving
  hashes, provenance, the non-reproducibility finding, and the restore
  procedure. `E019/.gitignore` excludes `build/` because `build.sh` re-creates
  the *arm64* binaries; `prebuilt/` is different in kind — a gated artifact
  kept because the gate is expensive and cannot be re-derived.
- Rewrote `E024/deploy/Dockerfile` to **install and verify** the gated binaries
  rather than compile them: five hash assertions (three binaries plus `scan.py`
  and `prune_c8.c`), then four execution checks — `genc48` returning 17 and 12
  on the two recorded order-8 invocations, stock `geng` returning 28, and
  `genc48 | labelg` returning 17 canonical forms, which exercises all three
  binaries end to end. Base image pinned by digest
  `sha256:0af1bf10…8112`. The image no longer needs `build-essential` or the
  nauty tarball.
- Kept the compile path as `Dockerfile.rebuild-from-source`, headed by a
  statement that it produces a new instrument needing a new gate.

## Verification

- The hash assertion was **tested by deploying it**, not assumed. First
  deployment: build **FAILED** at the assertion with
  `sha256sum: WARNING: 1 computed checksum did NOT match` — which is how the
  non-reproducibility was discovered. An untested `RUN` check is exactly the
  kind of thing that silently does not fire; this one fires.
- Second deployment, with the rewritten Dockerfile: build **SUCCESS**, printing
  `GATED INSTRUMENT CONFIRMED — hashes match and the binaries execute here`.
- **The running production job was checked, not assumed safe.** All six
  services were queried live over `railway ssh`, and every one reports
  `genc48 = e8e839f6…4bb0` — the gated hash. The job is running the gated
  instrument and was not disturbed. The mismatching build was a separate,
  deliberate deployment to the idle gate service.
- `python3 scripts/proofctl.py validate` passes; `tests/test_proofctl.py` 12/12.

## Dossier impact

**None.** No statement, claim, obligation, proof, review, status, or session
record changed. `C048` and the `E024` handoff are unaffected: the instrument
that produced every cited number is unchanged, and this operation preserves it
rather than altering it.

## Handoff

- Result: the gated instrument is in the repository and the image installs it
  under verification. A future cloud run does **not** re-gate.
- Remaining operational follow-up: if a new instrument is ever wanted, remove
  `-march=native` first so the new build is reproducible, then gate it and
  record a new architecture-tagged pin beside the existing ones.
- Files a later operator should read: `E019/prebuilt/linux-amd64/MANIFEST.md`,
  `E024/deploy/README.md`, `process/compute.md`, then `O012` for the gate
  itself.
- Commit and push status: committed and pushed with this record.
