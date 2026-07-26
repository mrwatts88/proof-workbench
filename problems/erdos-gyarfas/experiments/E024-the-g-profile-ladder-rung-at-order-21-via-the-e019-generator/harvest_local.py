#!/usr/bin/env python3
"""Harvest the order-21 rung with the LOCAL, already-anchored arm64 instrument.

O012 step 5: the cloud produced the parts; the aggregation and every number
that reaches a ledger comes from the build the repository has always trusted.
This imports E019/scan.py through E022/ladder.py's `load_scan` exactly as
`rung21.py` does, redirects DATA to the merged part set, and runs the
instrument's own `harvest`, which asserts the coverage identity
profile == c16_blocked + survivors across all 144 parts.
"""
import importlib.util
import os
import sys

sys.dont_write_bytecode = True

E022 = ("/Users/mattwatts/code/rh/problems/erdos-gyarfas/experiments/"
        "E022-the-g-profile-ladder-at-orders-18-and-19-via-the-e019-genera")
MERGED = ("/private/tmp/claude-501/-Users-mattwatts-code-rh/"
          "34080fcf-635d-458d-88bf-8a372e5a8195/scratchpad/e024-merged")

spec = importlib.util.spec_from_file_location(
    "e022_ladder", os.path.join(E022, "ladder.py"))
ladder = importlib.util.module_from_spec(spec)
sys.modules["e022_ladder"] = ladder
spec.loader.exec_module(ladder)

mod = ladder.load_scan(MERGED)
print("instrument: %s" % mod.GENC48)
print("interpreter: %s" % mod.interpreter())
print("")
mod.cmd_harvest(["21", "144"])
