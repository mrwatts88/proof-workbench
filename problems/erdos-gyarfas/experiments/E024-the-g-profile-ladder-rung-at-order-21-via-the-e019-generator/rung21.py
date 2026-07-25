#!/usr/bin/env python3
"""E024 — the G-profile ladder rung at order 21 (P-002, session S023
close-of-session background leg; results NOT citable until harvested).

Thin driver over E022/ladder.py's `load_scan` (which imports E019/scan.py
by file path and redirects its DATA constant), so the instrument — the
sha256-pinned genc48 PREPRUNE generator, the 146-check anchor suite, and
the run/harvest/spotcheck commands — is E019's, unchanged, and every
output lands in E024/data.  E019's and E022's trees are only read.

Stages (status written to data/rung21_status.json as it goes):
  0. anchors  — the 146-check suite under PyPy (gate; abort on failure).
  B. rung 21  — `run 21 r/16 --verify-all` for r = 0..15, 8 concurrent
                subprocesses (projected ~21 h wall on 8 workers from the
                recorded x8.25 order-20 growth), then `harvest 21 16`
                and `spotcheck 21 4`.

Run:      pypy3 rung21.py            # full pipeline (the S023 launch)
          pypy3 rung21.py part r/16  # one part (used by the pipeline)
Deterministic; wall-clock timings only.
"""
import importlib.util
import json
import os
import subprocess
import sys
import time

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
E022 = os.path.abspath(os.path.join(
    HERE, os.pardir,
    "E022-the-g-profile-ladder-at-orders-18-and-19-via-the-e019-genera"))
STATUS = os.path.join(DATA, "rung21_status.json")
PYPY = "pypy3"

spec = importlib.util.spec_from_file_location(
    "e022_ladder", os.path.join(E022, "ladder.py"))
ladder = importlib.util.module_from_spec(spec)
sys.modules["e022_ladder"] = ladder
spec.loader.exec_module(ladder)

state = {"stages": {}, "interpreter_note": "pypy3 throughout",
         "launched_by": "S023 at session close; not citable until "
                        "harvested by a later session"}


def record(stage, **kw):
    state["stages"].setdefault(stage, {}).update(kw)
    with open(STATUS, "w") as fh:
        json.dump(state, fh, indent=1)


def main():
    os.makedirs(DATA, exist_ok=True)

    if len(sys.argv) > 1 and sys.argv[1] == "part":
        mod = ladder.load_scan(DATA)
        mod.cmd_run(["21", sys.argv[2], "--verify-all"])
        return

    # Stage 0: anchors gate (146 checks through the same import path).
    t0 = time.time()
    record("0_anchors", status="running")
    mod = ladder.load_scan(DATA)
    try:
        mod.cmd_anchors([])
    except SystemExit as e:
        if e.code not in (0, None):
            record("0_anchors", status="FAILED")
            record("abort", reason="anchor suite failed; no rung run")
            raise
    record("0_anchors", status="passed",
           seconds=round(time.time() - t0, 1))

    # Stage B: 16 parts, 8 concurrent, then harvest + spotcheck.
    t0 = time.time()
    record("B_rung21", status="running")
    parts = list(range(16))
    running = {}
    failed = []
    log = open(os.path.join(DATA, "run21.log"), "w")
    while parts or running:
        while parts and len(running) < 8:
            p = parts.pop(0)
            running[p] = subprocess.Popen(
                [PYPY, os.path.abspath(__file__), "part", "%d/16" % p],
                cwd=HERE, stdout=log, stderr=subprocess.STDOUT, text=True)
        done = [p for p, pr in running.items() if pr.poll() is not None]
        if not done:
            time.sleep(30)
            continue
        for p in done:
            if running[p].returncode != 0:
                failed.append(p)
            del running[p]
            record("B_rung21", parts_finished=16 - len(parts) - len(running),
                   failed_parts=failed)
    log.close()
    if failed:
        record("B_rung21", status="FAILED", failed_parts=failed,
               seconds=round(time.time() - t0, 1))
        sys.exit(1)
    # Harvest + spotcheck through the redirected module ONLY (writes to
    # E024/data; E022's tree is never written).
    mod2 = ladder.load_scan(DATA)
    mod2.cmd_harvest(["21", "16"])
    mod2.cmd_spotcheck(["21", "4"])
    record("B_rung21", status="harvested+spotchecked",
           seconds=round(time.time() - t0, 1))
    record("finished", wall_seconds=round(time.time() - t0, 1))
    print("rung21 complete")


if __name__ == "__main__":
    main()
