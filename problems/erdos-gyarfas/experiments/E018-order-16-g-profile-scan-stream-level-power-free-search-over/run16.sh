#!/bin/sh
# E018 production driver: order-16 G-profile scan, 24 parts, 10 concurrent.
# Each part spawns its own geng (geng -q -c -f -d2 16 23:120 r/24) and
# writes data/scan_n16_part{r}of24.json.  --stats additionally counts C8s
# per class member (min-C8 statistic).  Re-run: sh run16.sh
cd "$(dirname "$0")" || exit 1
seq 0 23 | xargs -P 8 -n 1 -I PART pypy3 scan.py run 16 PART/24 --stats
