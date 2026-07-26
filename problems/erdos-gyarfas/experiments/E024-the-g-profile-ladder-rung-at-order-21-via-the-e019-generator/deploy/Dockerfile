# E024 on Railway — installs the GATED linux/amd64 instrument (O012, O014).
#
# This image does NOT compile nauty. That is deliberate, and it is not an
# optimisation.
#
# WHY: nauty's ./configure appends `-march=native` to the flags it uses for
# gtoolsW.o, nautyW1.o, nautilW1.o, naugraphW1.o, schreierW.o — the exact
# objects genc48 links against. `-march=native` tunes the code to the CPU of
# whatever machine happens to run the build, and a cloud builder is not a fixed
# machine. So compiling from source produces a DIFFERENT BINARY on a different
# builder, with a different sha256.
#
# The consequence that matters: THE ANCHOR GATE CANNOT BE RE-ESTABLISHED BY
# REBUILDING. The gate attaches to a hash; a rebuild does not reproduce the
# hash; therefore a rebuilt binary is a new instrument needing a new gate.
# Verified the hard way — a rebuild on a digest-pinned base still failed the
# hash assertion (O014).
#
# So the gated binaries are committed to the repository under
# E019/prebuilt/linux-amd64/ and installed here, with their hashes checked.
# To build a NEW instrument on purpose, use Dockerfile.rebuild-from-source and
# put it through the full gate before citing anything it produces.
FROM pypy:3.11-bookworm@sha256:0af1bf1000884bb8b652038944fdee15ad949b6cc6940162a8156306f9618112

COPY rh /rh

ENV E019=/rh/experiments/E019-dedicated-c4-c8-free-generator-geng-prune-plugin-and-the-ord

# Install the gated instrument and prove it is the gated one.
#
# These hashes ARE the gate. A binary matching them is the build that passed
# the 146-check anchor suite, the cubic order-24 positive control, the stream
# cross-check at orders 12-17 and the production-modulus partition check. If
# any check below fails, the build fails here on purpose: something is not the
# gated instrument, and it must be re-gated rather than shipped.
RUN set -eux; \
    mkdir -p "$E019/build/nauty2_9_3"; \
    install -m 0755 "$E019/prebuilt/linux-amd64/genc48" "$E019/build/genc48"; \
    install -m 0755 "$E019/prebuilt/linux-amd64/geng"   "$E019/build/nauty2_9_3/geng"; \
    install -m 0755 "$E019/prebuilt/linux-amd64/labelg" /usr/local/bin/labelg; \
    echo "e8e839f6d5ef90dafafe4e87d3d9fee502b0bbce7000902cc65dbcba57cf4bb0  $E019/build/genc48" | sha256sum -c -; \
    echo "886e88a231350c7a2f55c54be081e38ce5868d8a6ad339ed8b8d4e25024aa299  $E019/build/nauty2_9_3/geng" | sha256sum -c -; \
    echo "c28c5273c4852dfa13131dbe2080c24e2cc0cb882f9899ed028edcb63af1d7dd  /usr/local/bin/labelg" | sha256sum -c -; \
    echo "968421be062ceb40a969d1b82f7c5127e1a33189933a1c69dfa20c7874efe5d6  $E019/scan.py" | sha256sum -c -; \
    echo "0cbeb2e3876951cb6e1891da842ab1ea04837502349421307f67b7dc1a5111a4  $E019/prune_c8.c" | sha256sum -c -; \
    test "$("$E019/build/genc48" -q -c -f -d2 8 | wc -l)" = "17"; \
    test "$("$E019/build/genc48" -q -c -f -d2 8 10:28 | wc -l)" = "12"; \
    test "$("$E019/build/nauty2_9_3/geng" -q -c -f -d2 8 | wc -l)" = "28"; \
    test "$("$E019/build/genc48" -q -c -f -d2 8 | labelg -q | sort -u | wc -l)" = "17"; \
    echo "GATED INSTRUMENT CONFIRMED — hashes match and the binaries execute here"

ENV PYTHONDONTWRITEBYTECODE=1 \
    E024_DATA=/data/e024 \
    E024_ORDER=21 \
    E024_MOD=144 \
    E024_WORKERS=24 \
    E024_MODE=gate

WORKDIR /rh/experiments/E024-the-g-profile-ladder-rung-at-order-21-via-the-e019-generator
CMD ["pypy3", "-u", "cloud.py"]
