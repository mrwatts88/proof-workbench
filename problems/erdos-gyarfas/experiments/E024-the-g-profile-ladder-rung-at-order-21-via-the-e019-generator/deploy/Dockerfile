# E024 on Railway — linux/amd64 rebuild of the E019 generator (O012 step 1).
#
# The rule this image obeys: the *instrument* is E019's, unchanged.  scan.py,
# prune_c8.c, ladder.py and E005's order-24 census file are copied in
# byte-for-byte; nauty is compiled here from the same tarball the repository
# already pins by sha256, with the same compile line as E019/build.sh (same
# objects, same word size, same PREPRUNE/SUMMARY plugin hooks).  Only the
# target architecture differs, which is exactly why the anchor suite has to
# re-pass before any output of this image is citable.
FROM pypy:3.11-bookworm

# nauty 2.9.3 — the tarball Homebrew verifies for the nauty formula, the same
# sha256 recorded in E022/data/provenance.json's build provenance.  It is
# shipped in the build context rather than fetched so the build does not
# depend on a third-party web server being reachable from the build network;
# the bytes and the hash are identical either way.
ARG NAUTY_SHA256=9fc4edae04f88a0f5883985be3b39cf7f898fd6cc96e96b9ee25452743cc1b5b

RUN apt-get update \
 && apt-get install -y --no-install-recommends build-essential ca-certificates \
 && rm -rf /var/lib/apt/lists/*

COPY nauty2_9_3.tar.gz /src/nauty2_9_3.tar.gz
RUN echo "${NAUTY_SHA256}  /src/nauty2_9_3.tar.gz" | sha256sum -c -

COPY rh /rh

ENV E019=/rh/experiments/E019-dedicated-c4-c8-free-generator-geng-prune-plugin-and-the-ord

# E019/build.sh transcribed for this image: same source, same configure, same
# geng target, same explicit compile line for genc48 (W1 word size, PREPRUNE).
RUN set -eux; \
    mkdir -p "$E019/build"; \
    tar -xzf /src/nauty2_9_3.tar.gz -C "$E019/build"; \
    cd "$E019/build/nauty2_9_3"; \
    ./configure; \
    make geng labelg; \
    cc -O3 -fomit-frame-pointer -DMAXN=WORDSIZE -DWORDSIZE=32 \
       -DPREPRUNE=prune_c8 -DSUMMARY=summary_c8 \
       -I"$E019/build/nauty2_9_3" \
       -o "$E019/build/genc48" \
       "$E019/build/nauty2_9_3/geng.c" "$E019/prune_c8.c" \
       gtoolsW.o nautyW1.o nautilW1.o naugraphW1.o schreierW.o naurng.o; \
    install -m 0755 "$E019/build/nauty2_9_3/labelg" /usr/local/bin/labelg; \
    test "$("$E019/build/genc48" -q -c -f -d2 8 | wc -l)" = "17"; \
    test "$("$E019/build/genc48" -q -c -f -d2 8 10:28 | wc -l)" = "12"; \
    sha256sum "$E019/build/genc48" "$E019/build/nauty2_9_3/geng" \
              "$E019/scan.py" "$E019/prune_c8.c"

ENV PYTHONDONTWRITEBYTECODE=1 \
    E024_DATA=/data/e024 \
    E024_ORDER=21 \
    E024_MOD=512 \
    E024_WORKERS=8 \
    E024_MODE=gate

WORKDIR /rh/experiments/E024-the-g-profile-ladder-rung-at-order-21-via-the-e019-generator
CMD ["pypy3", "-u", "cloud.py"]
