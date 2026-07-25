#!/bin/sh
# E022 production driver: the order-18 G-profile scan, 16 parts, 8 concurrent.
# Each part spawns its own generator
#     E019/build/genc48 -q -c -f -d2 18 26:153 r/16
# through ladder.py (E019/scan.py with DATA redirected here) and writes
# data/scan_n18_part{r}of16.json plus data/class_n18_part{r}of16.txt.
# --verify-all re-checks C4- and C8-freeness independently on every generated
# graph.  Deterministic; delete the part JSONs you want recomputed.
# No pipe: xargs' exit status must reach the caller.
#
#   sh run18.sh
#   pypy3 ladder.py harvest 18 16
cd "$(dirname "$0")" || exit 1
mkdir -p data
seq 0 15 | xargs -P 8 -n 1 -I PART pypy3 ladder.py run 18 PART/16 --verify-all \
    > data/run18.log 2>&1
echo "run18 done"
