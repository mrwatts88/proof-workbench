#!/bin/sh
# E022 partition check: the SAME order-19 scan split a DIFFERENT way -- 24
# parts instead of 16, 8 concurrent.  Outputs go to data/split24/ so that they
# can never collide with the 16-part run.  `ladder.py splitcheck 19 16 24`
# then compares the two runs as labelg canonical SETS.
#
#   sh run19b.sh
#   pypy3 ladder.py --data split24 harvest 19 24
#   pypy3 ladder.py splitcheck 19 16 24
cd "$(dirname "$0")" || exit 1
mkdir -p data/split24
seq 0 23 | xargs -P 8 -n 1 -I PART pypy3 ladder.py --data split24 run 19 PART/24 \
    --verify-all > data/run19b.log 2>&1
echo "run19b done"
