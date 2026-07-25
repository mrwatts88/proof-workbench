#!/bin/sh
# E022 second-algorithm verification of the near-miss stratum, plus the
# boundary-exemplar dump.  `spotcheck` recomputes the FULL cycle spectrum of
# every class member with at most 4 degree-2 vertices with the brute-force
# enumerator (no code path shared with has_cycle_len) and asserts 4, 8 absent
# and the recorded C16 verdict; `exemplar` does the same on the 0-, 1- and
# 2-degree-2 buckets and records the full analysis of whatever is there.
# Single process on purpose: it runs alongside the 8-worker production.
#
#   sh checks.sh
cd "$(dirname "$0")" || exit 1
set -e
pypy3 exemplar.py 18 2 > data/exemplars_n18.log 2>&1
pypy3 exemplar.py 19 2 > data/exemplars_n19.log 2>&1
pypy3 ladder.py spotcheck 18 4 > data/spotcheck_n18.log 2>&1
pypy3 ladder.py spotcheck 19 4 > data/spotcheck_n19.log 2>&1
cat data/exemplars_n18.log
cat data/spotcheck_n18.log
cat data/spotcheck_n19.log
echo "checks done"
