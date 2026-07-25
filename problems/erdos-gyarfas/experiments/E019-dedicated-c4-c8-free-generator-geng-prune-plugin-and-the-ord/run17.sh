#!/bin/sh
# E019 production driver: the order-17 G-profile scan, 16 parts, 8 concurrent.
# Each part spawns its own generator
#     build/genc48 -q -c -f -d2 17 25:136 r/16
# and writes data/scan_n17_part{r}of16.json.  --verify-all re-checks C4- and
# C8-freeness independently on every generated graph (the volume is small
# enough that this costs nothing).  Resumable: re-running only redoes the
# parts whose JSON is missing is NOT automatic -- delete the parts you want
# recomputed, or re-run the whole thing (it is deterministic).
#
#   sh run17.sh
#   pypy3 scan.py harvest 17 16
cd "$(dirname "$0")" || exit 1
seq 0 15 | xargs -P 8 -n 1 -I PART pypy3 scan.py run 17 PART/16 --verify-all
