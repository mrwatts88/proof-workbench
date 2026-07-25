#!/bin/sh
# E022 production driver: the order-19 G-profile scan, 16 parts, 8 concurrent.
#     E019/build/genc48 -q -c -f -d2 19 28:171 r/16
# Outputs data/scan_n19_part{r}of16.json and data/class_n19_part{r}of16.txt.
#
#   sh run19.sh
#   pypy3 ladder.py harvest 19 16
cd "$(dirname "$0")" || exit 1
mkdir -p data
seq 0 15 | xargs -P 8 -n 1 -I PART pypy3 ladder.py run 19 PART/16 --verify-all \
    > data/run19.log 2>&1
echo "run19 done"
