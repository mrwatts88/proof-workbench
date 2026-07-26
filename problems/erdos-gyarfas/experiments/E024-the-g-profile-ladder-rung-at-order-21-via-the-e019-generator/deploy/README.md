# E024 deployment assets — the order-21 rung on Railway (`O012`)

Everything needed to rebuild and re-run the cloud leg of `E024`. The operation
record with the measurements, the anchor-gate verdict and the reasoning is
`operations/O012-2026-07-25-migrate-the-e024-order-21-rung-to-railway-linux-amd64-genera.md`.

The instrument is **not** here. `cloud.py` (one level up, beside `rung21.py`)
is a driver: it reaches every mathematical operation through `E022/ladder.py`'s
`load_scan`, which imports `E019/scan.py` and redirects its `DATA` constant.
Nothing in this directory computes a graph property.

## The image installs the gated instrument; it does not compile it

**`Dockerfile` copies in the committed, already-gated binaries from
`E019/prebuilt/linux-amd64/` and verifies their hashes.** It does not build
nauty. That is deliberate.

nauty's `./configure` appends `-march=native` to the flags used for
`gtoolsW.o`, `nautyW1.o`, `nautilW1.o`, `naugraphW1.o`, `schreierW.o` — exactly
the objects `genc48` links — so the binary is tuned to whichever machine ran
the build. `O014` tested this: a rebuild from identical sources on a
**digest-pinned** base produced a **different `genc48`**.

The consequence: **the anchor gate cannot be re-established by rebuilding.**
The gate attaches to a hash, a rebuild does not reproduce the hash, so a
rebuilt binary is a new instrument needing a new gate. Hence the binaries are
committed and installed.

`Dockerfile.rebuild-from-source` is the compile-from-source version, kept
runnable for when a **new** instrument is genuinely wanted. Anything it
produces must go through the full gate before it is cited.

## Assembling the build context

The image is built from a staging tree, not from the repository root, so that
the upload stays small. Create `<ctx>/` containing:

```
<ctx>/Dockerfile                 <- from here
<ctx>/railway.json               <- from here
<ctx>/rh/experiments/E005-markstrom-.../data/survivors_n24.g6
<ctx>/rh/experiments/E019-dedicated-.../{scan.py, prune_c8.c, data/,
                                         prebuilt/linux-amd64/}
<ctx>/rh/experiments/E022-the-g-profile-.../ladder.py
<ctx>/rh/experiments/E024-the-g-profile-.../cloud.py
```

The long experiment directory names must be preserved exactly: `ladder.py` and
`cloud.py` locate their siblings by those names relative to their own path.
Do **not** copy `E019/build/` — that holds the arm64 binaries, which will not
run there.

Only for `Dockerfile.rebuild-from-source` you additionally need
`<ctx>/nauty2_9_3.tar.gz`, the tarball the repository already pins,

    sha256 9fc4edae04f88a0f5883985be3b39cf7f898fd6cc96e96b9ee25452743cc1b5b
    https://pallini.di.uniroma1.it/nauty2_9_3.tar.gz   (5,496,724 bytes)

also available from the Homebrew download cache. It is shipped in the context
rather than fetched during the build so the build does not depend on a
third-party host; the Dockerfile verifies the hash either way. It is not
committed, for the same reason `E019/.gitignore` excludes `build/`.

## Running

```sh
railway init --name rh-e024
railway link --project <id> --environment production --service <name>
railway volume add --mount-path /data
```

Then set per-service variables and deploy with `railway up --service <name> --detach`.

| variable | meaning |
|---|---|
| `E024_MODE` | `gate` \| `calib` \| `run` |
| `E024_ORDER` | order to scan (21) |
| `E024_MOD` | res/mod modulus (144 in production) |
| `E024_PARTS` | `"a-b"` \| `"k/S"` stride \| `"0,3,9"` \| empty = all |
| `E024_WORKERS` | concurrent parts **— never above 24**, see below |
| `E024_HOLD` | keep the container alive after finishing, so the volume stays reachable |

**A Railway Pro service is capped at 24 vCPU**, not the 1,000 in the pricing
table (that ceiling is divided across the 42-replica maximum).
`os.cpu_count()` inside the container reports the host's 48 and is misleading.
Concurrency comes from running more services, not from raising `E024_WORKERS`.

## Order of operations

1. **`gate` — blocking, but only for a NEW instrument.** If the build asserted
   the committed hashes and printed `GATED INSTRUMENT CONFIRMED`, you are
   holding the binary that already passed, and **no re-gate is needed**. Run
   the gate when the binary is new: download `/e024` from the volume and run
   `gatecheck.py <dir>`; nothing a new build produces is citable until it
   prints `GATE PASSED`.
2. **`calib` — optional but advisable for a new order.** Sweeps moduli and fits
   `total_cpu(mod) = mod × A + B`. Splitting is *not* free: `geng` assigns
   whole subtrees at split level `n-4`, so every part duplicates the walk above
   that level. Feed the result to `project.py` to choose the modulus.
3. **`run` — production.** One service per stride class.
4. **Retrieve.** `collect.sh <n_services> <staging>` then
   `merge_verify.py <staging> <order> <mod> <dest>`, which fails loudly on a
   missing part, a hash mismatch, a duplicated part, or a violated coverage
   identity. `crosscheck_n19.py` compares a calibration run's order-19 class
   against the recorded one as a *set*, which is stronger than the gate's
   count-level partition check.
5. **Harvest locally**, with the already-anchored arm64 instrument. That step
   is mathematical work and belongs to a session record, not to `O012`.

## The class-file trap

`scan.py` writes a part's class file only when that part emits at most
`SAVE_LIMIT = 200,000` graphs, and **the graph6 strings of degree-profile
members exist only in the class files** — the scan JSON keeps counts plus full
records for the \(C_{16}\)-free `survivors`, and every profile object found so
far is \(C_{16}\)-blocked. At order 20 this cost 4 of 7 members; in the local
order-21 run, part 0/16 emitted 210,802 graphs and took 8 of the 11
then-known profile members with it. Choose the modulus so that every part
stays well under the limit, and check `parts_without_class_file` in the run
manifest before treating a profile list as complete.
