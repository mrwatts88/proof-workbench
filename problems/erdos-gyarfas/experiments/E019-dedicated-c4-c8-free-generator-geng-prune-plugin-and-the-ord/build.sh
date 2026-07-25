#!/bin/sh
# E019 build script -- the dedicated {C4,C8}-free generator.
#
#   sh build.sh
#
# Produces, under build/ (which is git-ignored: it holds the imported nauty
# source tree and compiled binaries, neither of which belongs in the dossier):
#
#   build/nauty2_9_3/geng   -- stock nauty 2.9.3 geng, built from source here;
#                              used as the *independent* reference instrument
#                              in the anchor suite (it is also byte-compatible
#                              in behaviour with the installed /opt/homebrew
#                              geng that E010-E018 used).
#   build/genc48            -- the same geng.c compiled with our PREPRUNE
#                              plugin (prune_c8.c): {C4,C8}-free generation.
#
# Source provenance: nauty 2.9.3, the exact tarball Homebrew verifies for the
# installed nauty formula (https://pallini.di.uniroma1.it/nauty2_9_3.tar.gz),
# taken from the Homebrew download cache after `brew fetch --build-from-source
# nauty`.  Its sha256 is checked below before extraction.
set -eu

HERE=$(cd "$(dirname "$0")" && pwd)
BUILD="$HERE/build"
SRC="$BUILD/nauty2_9_3"
SHA256=9fc4edae04f88a0f5883985be3b39cf7f898fd6cc96e96b9ee25452743cc1b5b
CACHE="$HOME/Library/Caches/Homebrew/downloads"
TARBALL=${NAUTY_TARBALL:-"$CACHE/ea04fccef13c434500ec7eb989e59abb7c72375679bf5333cf39f2fe430ae84e--nauty2_9_3.tar.gz"}

mkdir -p "$BUILD"
if [ ! -d "$SRC" ]; then
    echo "$SHA256  $TARBALL" | shasum -a 256 -c -
    tar -xzf "$TARBALL" -C "$BUILD"
fi
echo "$SHA256  $TARBALL" | shasum -a 256 -c -

cd "$SRC"
# NB: the tarball ships a stub `makefile` that only prints config.txt, so the
# presence of `makefile` is not a usable "already configured" test.
[ -f config.log ] || ./configure
make geng

# Same objects and same word size as the stock geng rule in nauty's makefile
# (W1 = -DMAXN=WORDSIZE -DWORDSIZE=32), plus the plugin.
CC=${CC:-cc}
CFLAGS=${CFLAGS:--O3 -fomit-frame-pointer}
OBJ="gtoolsW.o nautyW1.o nautilW1.o naugraphW1.o schreierW.o naurng.o"
# shellcheck disable=SC2086
$CC $CFLAGS -DMAXN=WORDSIZE -DWORDSIZE=32 \
    -DPREPRUNE=prune_c8 -DSUMMARY=summary_c8 \
    -I"$SRC" -o "$BUILD/genc48" "$SRC/geng.c" "$HERE/prune_c8.c" $OBJ

echo "built: $SRC/geng and $BUILD/genc48"
"$BUILD/genc48" -q -c -f -d2 8 10:28 | wc -l
