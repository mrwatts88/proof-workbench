#!/bin/sh
# E026 production census over the on-disk classes at orders 18-20.
# Deliberately throttled: N workers (default 3) at nice 15, because E024
# (the order-21 rung) owns 8 of the 12 cores for the whole session.
# Orders 10-17 (census-small) are run separately before this script.
set -e
cd "$(dirname "$0")"
PY=${PY:-pypy3}
N=${N:-3}
echo "[census] order 18, 16 parts, $N workers"
printf '%s\n' 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 \
  | xargs -P "$N" -I PART nice -n 15 "$PY" census.py census 18 PART \
  >> data/run_census.log 2>&1
echo "[census] order 19, 16 parts, $N workers"
printf '%s\n' 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 \
  | xargs -P "$N" -I PART nice -n 15 "$PY" census.py census 19 PART \
  >> data/run_census.log 2>&1
echo "[census] order 20, the 11 SAVE_LIMIT-complete parts, $N workers"
printf '%s\n' 0 1 2 4 5 8 9 10 11 12 15 \
  | xargs -P "$N" -I PART nice -n 15 "$PY" census.py census 20 PART \
  >> data/run_census.log 2>&1
echo "[census] supp14 stratum + harvest"
nice -n 15 "$PY" census.py supp14 >> data/run_census.log 2>&1
"$PY" census.py harvest | tee -a data/run_census.log
echo "[census] done"
