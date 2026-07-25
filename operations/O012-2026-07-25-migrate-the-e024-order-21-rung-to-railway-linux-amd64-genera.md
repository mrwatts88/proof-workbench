# O012 — migrate the E024 order-21 rung to Railway: linux/amd64 generator rebuild, anchor re-gate, and wide res/mod splitting

- Date: 2026-07-25
- Classification: repository operation (not mathematical research)
- Status: **EXECUTED.** The image is built and gated, the anchor re-gate
  **PASSED** and was independently re-verified locally, and the order-21
  production run is live on six Railway services. Retrieval, merge and the
  mathematical harvest remain; the harvest is research work and belongs to a
  later `S###` session, not to this record.

## Scope

Move the compute of `E024` (the order-21 \(\mathcal G\)-profile ladder rung,
launched at the `S023` close) off the laptop and onto Railway.

Affected systems: the `E019` generator binary (`genc48` = nauty `geng` plus the
recorded PREPRUNE \(C_8\) plugin), a new container image, and a new cloud
driver `E024/cloud.py`. **Untouched:** every problem dossier. This changed
*where* `E024` runs, not *what* it computes. No statement, claim, obligation,
proof, review, status or session record is altered by this operation.

## What was built

A `linux/amd64` image (`Dockerfile`, build context staged outside the
repository) on `pypy:3.11-bookworm`, which supplies **PyPy 7.3.23 / Python
3.11.15 — the same interpreter version as the laptop**, so even the
`interpreter` field of the anchor output matches.

nauty 2.9.3 is compiled **from source inside the image** from the tarball the
repository already pins (`sha256 9fc4edae…1b5b`, verified in the build), using
`E019/build.sh`'s compile line verbatim: same objects, same
`-DMAXN=WORDSIZE -DWORDSIZE=32`, same `-DPREPRUNE=prune_c8 -DSUMMARY=summary_c8`.
`scan.py`, `prune_c8.c`, `ladder.py` and `E005/data/survivors_n24.g6` are
copied in byte-for-byte; the instrument is E019's, unchanged.

The tarball ships **in the build context** rather than being fetched at build
time, so the build does not depend on a third-party host being reachable from
Railway's build network. The bytes and the sha256 are identical either way
(the upstream URL was confirmed to serve exactly those 5,496,724 bytes).

`E024/cloud.py` is a driver only, in the same relationship to the instrument as
`rung21.py`: it reaches every mathematical operation through `E022/ladder.py`'s
`load_scan`, and computes no graph property itself. It adds three things:
a `gate` mode, a `calib` mode, and a post-run filter that selects the
degree-profile members out of the class files (see "the class-file trap").

## The anchor re-gate — PASSED

A different-architecture rebuild breaks the repository's sha256 pin, so the
cloud binary was treated as a **new instrument** until it reproduced what the
arm64 build recorded. Run in the container, then **downloaded and compared
locally** against the dossier by `gatecheck.py` (wall-clock and interpreter
fields excluded; every other field required to match exactly):

| check | result |
|---|---|
| 146-check anchor suite | **identical** to `E019/data/anchors_pypy.json` *and* `E024/data/anchors_pypy.json` |
| cubic order-24 positive control | 4 graphs, set-equal to `E005`, = Markström Table 3 |
| stream cross-check, orders 12–17 | **identical** to `E019/data/crosscheck_mindeg3.json`; order 17 streams 34,758,006 graphs |
| partition check at the production modulus | order 16, mod 512: unsplit 7,615 = split total 7,615, exact |
| `scan.py`, `prune_c8.c` sha256 | byte-identical to the dossier |

**Architecture-tagged second pin**, recorded beside — not replacing — the
arm64 pin in `E022/data/provenance.json`:

| | arm64 (recorded, unchanged) | linux/amd64 (new) |
|---|---|---|
| `genc48` | `f0d9ca22a164838d9b2b6287e8d6f8abe6cc901a6cc369fb82de7f2f87ef341e` | `e8e839f6d5ef90dafafe4e87d3d9fee502b0bbce7000902cc65dbcba57cf4bb0` |
| `geng` (reference) | `440758302235ea0e6494d1cc8e1175f122bb9177be5d951ffe423200eaf11151` | `886e88a231350c7a2f55c54be081e38ce5868d8a6ad339ed8b8d4e25024aa299` |

Machine parity, measured on the gate's own timings: the order-17 cross-check
took **1,085.6 s** in the cloud against **1,069.6 s** recorded on the laptop
(1.5% slower). The planning caveat in the original version of this record —
"budget 1.3–2× more vCPU-hours than the laptop figures suggest" — is
**withdrawn**; for this workload a cloud vCPU is at parity with an M-series
performance core.

## Three findings that corrected the plan

### 1. A Pro service is capped at 24 vCPU, not 1,000

The pricing table's "1,000 vCPU" is a *per-service* ceiling **including replica
multiplication**, and Railway divides it by the 42-replica maximum: each
container gets **24 vCPU / 24 GB**, confirmed on two services
(`cpu.limit = 24.0`, observed average 22.98 under load). `os.cpu_count()`
inside the container unhelpfully reports the host's 48.

Consequence: **concurrency comes from more services, not bigger ones**, and a
worker count above 24 per service only creates contention. The original plan's
"one service, all parts concurrent within the plan's vCPU ceiling" is not
achievable as written.

### 2. "Width is nearly free" is false for this generator

This was the load-bearing assumption of the original record ("Spreading a fixed
number of core-hours over 150 cores costs the same as over 8 — only the wall
clock changes"). It is wrong, and the reason is in `geng.c`:

```
if (maxn >= 14 && mod > 1) splitlevel = maxn - 4;
```

`geng` assigns whole subtrees at that split level, so **every part must walk
the entire tree above the split level** before it can tell which subtrees are
its own. Total work is therefore

    total_cpu(mod) = mod × A + B

with `A` the duplicated upper-tree walk paid *once per part* and `B` the shared
work below. Measured by the `calib` mode at order 19 (whose class size, 74,589,
is on record, so each sweep is also an exactness check):

- modulus 16 (recorded, laptop): 11,226.8 core-s
- modulus 64 (measured, cloud): ≈18,000 core-s
- fit: **A ≈ 141 core-s per part, B ≈ 8,969 core-s**

Splitting 144 ways nearly **triples** total CPU. Worse, the largest part runs
**2.86×** the mean (measured over the 64-way sweep), so with one wave the wall
clock is `skew × (A + B/mod)`, which has a **hard floor of `skew × A`** — about
**4.9 h at order 21, unreachable by any modulus**. The original record's
"finishes in about an hour instead of about fifteen" was not achievable.

Projection at order 21 (scaling A and B by the recorded rung growth):

| mod = workers | services | total core-h | wall (h) | cost |
|---|---|---|---|---|
| 24 | 1 | 150 | 17.8 | $4.10 |
| 96 | 4 | 273 | 8.1 | $7.48 |
| **144** | **6** | **355** | **7.0** | **$9.72** |
| 192 | 8 | 437 | 6.5 | $11.97 |
| 240 | 10 | 519 | 6.2 | $14.22 |
| *laptop, mod 16, 8 workers* | — | *136* | *24.3* | — |

Modulus **144 on 6 services** was selected as the knee: past it, cost rises
roughly linearly for minutes of wall clock.

### 3. The class-file trap — the real payoff of the re-split

`scan.py` writes a part's class file only when that part emits at most
`SAVE_LIMIT = 200,000` graphs. This is not a cosmetic limit: **the graph6
strings of degree-profile members exist only in the class files.** The scan
JSON keeps counts, plus full records for `survivors` (the \(C_{16}\)-free ones)
— and every profile object found to date is \(C_{16}\)-blocked, so the members
the decisive measurement needs are exactly the ones that live only in the class
file.

Confirmed twice:

- **Order 20, on record:** of 7 profile members, only **3** are recoverable —
  5 of 16 parts exceeded the limit. (Verified by a known-answer test of the
  extractor against `E022`'s recorded data.)
- **Order 21, the local run, live:** part 0/16 emitted **210,802** graphs, over
  the limit, and it contained **8 of the 11 profile members found so far**.
  Their graph6 strings were never written.

At modulus 144 the expected class (~1M graphs, extrapolated from the six
completed local parts) gives ~7k graphs per part, far under the limit, so every
profile member is captured. **The migration is justified on correctness
grounds even where it disappointed on speed.**

## Production configuration (live)

Six services `part-0` … `part-5`, project `rh-e024`
(`d949a7fa-ba8b-48b0-9e10-c8668e508e5c`), each with its own volume mounted at
`/data`, `restartPolicyType: NEVER` (declared in `railway.json` as a cost
guard), 24 workers, order 21, modulus 144. Service *k* takes the stride class
\(\{r : r \equiv k \pmod 6\}\) so that clustered hard parts spread across
containers instead of piling into one. All six confirmed running 24 parts each.

Resumability: a part whose scan JSON already exists is skipped, so a restarted
container continues rather than redoing work.

## Retrieval and verification (remaining)

`collect.sh` downloads each volume via `railway volume files download /e024`;
`merge_verify.py` then checks, and fails loudly on: every service reporting
`COMPLETE` with no failed parts; every file matching the sha256 its container
recorded; the parts forming the full residue system 0…143 exactly once; each
part's scan JSON self-describing as the part it is filed under; the per-part
coverage identity `profile == c16_blocked + survivors`; and any part lacking a
class file reported explicitly so a short profile list is never mistaken for a
complete one. The harvest itself must then be run with the **local, already
anchored** instrument.

A stronger check than the gate's is available and staged (`crosscheck_n19.py`):
the calibration wrote complete order-19 class files, so the amd64 class can be
compared **as a set of graph6 strings** against the recorded arm64 order-19
class at modulus 16 — ruling out the failure mode equal counts cannot (a part
dropping one subtree and double-counting another).

## Not done, and why

- **`geng -X<k>`** shifts the split level (`splitlevel += splitlevinc`), and a
  *negative* increment would shrink `A` and with it the 4.9 h wall floor —
  plausibly to ~2 h and ~$3. It was **not** used: it changes the generator's
  recorded invocation, and adding an unverified partition parameter
  immediately after a careful gate is a poor trade against a run that is
  already launched and finishes overnight. Recorded here as a measured,
  concrete option for a future rung, not as a regret.
- The modulus-512 leg of the calibration was cut once moduli 16 and 64
  determined `A` and `B`; the model predicted it would be ~7× the unsplit cost,
  which was enough to reject it.

## Verification performed

Image build asserts two generator counts with independently confirmed expected
values (17 and 12 at order 8; the first published attempt asserted 17 for the
edge-bounded invocation, which is 12 — caught by the build, fixed, not a
generator fault). Extractor validated by known-answer test against recorded
order-20 data. Driver smoke-tested end-to-end locally before deployment. Gate
compared locally against the dossier. Partition exactness re-checked on the new
build at the production modulus.

## Dossier impact

**None from this operation.** Two mathematical results now sit on disk that no
ledger records, and both require a research session before they may be cited:
the `E024` order-21 rung when it lands, and the `E028` order-30 rung (run B,
\(M=29\): 0 survivors, 49,882,612 nodes, 4,195.9 s, not capped), after which
the E028 ladder was stopped per the recorded `S027` post-close decision.

## Handoff

- The run is live and unattended; expected wall clock ~7 h from 2026-07-25 ~23:15.
- Remaining operational follow-up: collect, merge/verify, then hand the merged
  part set to a research session for the harvest.
- Cost to date is dominated by the production run: ~355 core-hours ≈ $10.
- Files a later operator should read: this record; the staged build context and
  scripts (`Dockerfile`, `cloud.py`, `gatecheck.py`, `collect.sh`,
  `merge_verify.py`, `crosscheck_n19.py`, `project.py`); `E019/README.md`;
  `E022/data/provenance.json` for the arm64 pin this operation did not touch.
