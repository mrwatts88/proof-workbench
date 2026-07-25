#!/bin/sh
# E022 process gate (problem.json): the E019 146-check anchor suite must
# re-pass under BOTH interpreters before any extension run.  CPython first,
# then PyPy; `set -e` aborts the whole gate on the first failure.  No pipes:
# a pipeline's exit status would mask a failing interpreter under POSIX sh.
#
#   sh anchors.sh
cd "$(dirname "$0")" || exit 1
set -e
mkdir -p data
echo "== CPython =="
python3 ladder.py anchors > data/anchors_cpython.log 2>&1
cat data/anchors_cpython.log
echo "== PyPy =="
pypy3 ladder.py anchors > data/anchors_pypy.log 2>&1
cat data/anchors_pypy.log
echo "ANCHOR GATE PASSED under both interpreters"
