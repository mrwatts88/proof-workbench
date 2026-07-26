# The gated linux/amd64 build of the E019 instrument

These are the exact binaries that **passed the anchor re-gate on 2026-07-25**
(`O012`). They are committed so that a future cloud run does not have to rebuild
the instrument and re-establish its validity from scratch.

`build/` is git-ignored here because `build.sh` re-creates the *arm64* binaries
from a sha256-checked tarball. This directory is different: it is a **gated
artifact**, kept because the gate is expensive and attaches to the hash.

| file | sha256 | bytes |
|---|---|---|
| `genc48` | `e8e839f6d5ef90dafafe4e87d3d9fee502b0bbce7000902cc65dbcba57cf4bb0` | 175,224 |
| `geng` | `886e88a231350c7a2f55c54be081e38ce5868d8a6ad339ed8b8d4e25024aa299` | 174,744 |
| `labelg` | `c28c5273c4852dfa13131dbe2080c24e2cc0cb882f9899ed028edcb63af1d7dd` | 524,176 |

These are **linux/amd64 ELF executables**. They do not run on the arm64 laptop
and are not a substitute for `build.sh`. The arm64 pin
(`genc48 = f0d9ca22…341e`) is unchanged and remains the primary instrument for
all local work.

`labelg` had no recorded pin before this; its hash is recorded here because the
anchor suite uses it for canonical forms.

## Provenance

- Built inside the `O012` image from nauty 2.9.3, tarball sha256
  `9fc4edae04f88a0f5883985be3b39cf7f898fd6cc96e96b9ee25452743cc1b5b`, verified
  in the build.
- Compile line identical to `E019/build.sh`: same objects, same
  `-DMAXN=WORDSIZE -DWORDSIZE=32`, same `-DPREPRUNE=prune_c8
  -DSUMMARY=summary_c8`, `-O3 -fomit-frame-pointer`.
- Base image `pypy:3.11-bookworm`, resolved digest
  `sha256:0af1bf1000884bb8b652038944fdee15ad949b6cc6940162a8156306f9618112`
  (PyPy 7.3.23 / Python 3.11.15 — the same interpreter version as the laptop).
- Extracted from the running gate service over `railway ssh` and verified
  locally against the pins above before being committed.

## Why the gate does not have to be repeated

**The gate attaches to the hash, not to the build event.** A binary whose
sha256 equals the pin above *is* the instrument that passed the 146-check
anchor suite, the cubic order-24 positive control, the stream cross-check at
orders 12–17, and the production-modulus partition check. Nothing about it is
re-established by re-running those checks.

So, on a future cloud run:

1. Build the image. It compiles from source as before, then **asserts** the
   resulting `genc48` and `geng` hashes against the pins above.
2. **If the assertion passes, the run needs no re-gate** — you are holding the
   gated instrument.
3. **If it fails, the build fails loudly.** That is the intended behaviour: a
   toolchain or base-image change has produced a *different* instrument, and a
   different instrument must be re-gated before any of its output is citable.
   Do not weaken the assertion to get past it.

### The build is NOT reproducible — this was tested, and it failed

`O014` rebuilt the instrument from identical sources on a **digest-pinned** base
image and got a **different `genc48`**. Cause: nauty's `./configure` appends
`-march=native` to the flags used for `gtoolsW.o`, `nautyW1.o`, `nautilW1.o`,
`naugraphW1.o`, `schreierW.o` — exactly the objects `genc48` links. That tunes
code generation to the CPU of whichever machine runs the build, and a cloud
builder is not a fixed machine.

So step 1 above is **not** "compile and hope the hash matches". The image
installs these committed binaries and verifies them. Compiling from source is
`Dockerfile.rebuild-from-source`, and it produces a **new instrument that needs
a new gate**.

Note also that identical hashes across several cloud builds prove nothing about
reproducibility: layer caching returns the same layer without recompiling. Four
builds agreed during `O012`; the first genuinely independent recompile
disagreed.

If a new gate is ever run deliberately, set `CFLAGS`/`MORECFLAGS` without
`-march=native` first. The build then becomes reproducible *and* portable, and
a rebuild self-certifies against its pin. That is a different binary and needs
its own gate.

## Restoring without a compiler

If the toolchain has drifted and you need the gated instrument rather than a
new one, copy these files into `build/` in the image instead of compiling:

```dockerfile
COPY prebuilt/linux-amd64/genc48 $E019/build/genc48
COPY prebuilt/linux-amd64/geng   $E019/build/nauty2_9_3/geng
COPY prebuilt/linux-amd64/labelg /usr/local/bin/labelg
```

then verify the hashes and proceed. This is a legitimate fallback precisely
because the pins identify the gated instrument; it is not a way to skip the
gate for a binary that never passed one.
