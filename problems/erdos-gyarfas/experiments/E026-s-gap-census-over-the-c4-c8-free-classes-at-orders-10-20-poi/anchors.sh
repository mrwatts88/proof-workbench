#!/bin/sh
# E026 anchor gate: the E021 45-check suite (through the import) plus the
# new census checks, under BOTH interpreters, before any production run.
set -e
cd "$(dirname "$0")"
mkdir -p data
echo "== E026 anchors under CPython =="
python3 census.py anchors > data/anchors_cpython.log 2>&1
tail -n 2 data/anchors_cpython.log
echo "== E026 anchors under PyPy =="
pypy3 census.py anchors > data/anchors_pypy.log 2>&1
tail -n 2 data/anchors_pypy.log
