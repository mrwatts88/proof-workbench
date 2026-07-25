"""S022 close-of-session background follow-up (orchestrator-launched).

Stages (results are NOT citable until harvested by a later session):
  0. anchors  — the 146-check suite under PyPy, re-passed before the
                extension run (process rule; this session's earlier pass
                was CPython+PyPy pre-production).
  A. exemplar — the order-19 profile exemplar's full cycle set against
                A023 T5 (exemplar_t5.py; minutes).
  B. rung 20  — the order-20 G-profile scan, 16 parts, 8 concurrent
                (projected ~2.3e11 tree nodes, 2.5-3 h on 8 workers),
                then harvest + spotcheck.
  C. count 19 — the order-19 independent unsplit count (single process,
                ~3.3 h), completing C043's named partition follow-up.

B and C run concurrently (8+1 processes); A and 0 run first.  Every stage
writes its own files under data/; this driver records stage status and
timings in data/followup_s022.json as it goes, so a partial run is
harvestable.  Deterministic throughout; timings are wall-clock only.

Run:  pypy3 followup_s022.py   (from this directory or anywhere)
"""
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
STATUS = os.path.join(DATA, "followup_s022.json")
PYPY = "pypy3"

state = {"stages": {}, "interpreter_note": "pypy3 throughout",
         "launched_by": "S022 orchestrator at session close"}


def record(stage, **kw):
    state["stages"].setdefault(stage, {}).update(kw)
    with open(STATUS, "w") as fh:
        json.dump(state, fh, indent=1)


def run(cmd, **kw):
    return subprocess.run(cmd, cwd=HERE, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT, text=True, **kw)


def main():
    os.makedirs(DATA, exist_ok=True)

    # Stage 0: anchors gate.
    t0 = time.time()
    record("0_anchors", status="running")
    r = run([PYPY, "ladder.py", "anchors"])
    ok = r.returncode == 0
    record("0_anchors", status="passed" if ok else "FAILED",
           seconds=round(time.time() - t0, 1), tail=r.stdout[-400:])
    if not ok:
        record("abort", reason="anchor suite failed; no extension run")
        sys.exit(1)

    # Stage A: the exemplar T5 test.
    t0 = time.time()
    record("A_exemplar_t5", status="running")
    r = run([PYPY, "exemplar_t5.py"])
    record("A_exemplar_t5",
           status="done" if r.returncode == 0 else "FAILED",
           seconds=round(time.time() - t0, 1), tail=r.stdout[-400:])

    # Stages B and C concurrently: rung 20 (8 workers) + count 19 (1).
    t0 = time.time()
    record("B_rung20", status="running")
    record("C_count19", status="running")
    count_proc = subprocess.Popen(
        [PYPY, "ladder.py", "count", "19"], cwd=HERE,
        stdout=open(os.path.join(DATA, "count19.log"), "w"),
        stderr=subprocess.STDOUT, text=True)

    parts = list(range(16))
    running = {}
    failed_parts = []
    log20 = open(os.path.join(DATA, "run20.log"), "w")
    while parts or running:
        while parts and len(running) < 8:
            p = parts.pop(0)
            proc = subprocess.Popen(
                [PYPY, "ladder.py", "run", "20", "%d/16" % p, "--verify-all"],
                cwd=HERE, stdout=log20, stderr=subprocess.STDOUT, text=True)
            running[p] = proc
        done = [p for p, pr in running.items() if pr.poll() is not None]
        if not done:
            time.sleep(10)
            continue
        for p in done:
            if running[p].returncode != 0:
                failed_parts.append(p)
            del running[p]
    log20.close()
    if failed_parts:
        record("B_rung20", status="FAILED", failed_parts=failed_parts,
               seconds=round(time.time() - t0, 1))
    else:
        r = run([PYPY, "ladder.py", "harvest", "20", "16"])
        h_ok = r.returncode == 0
        record("B_rung20",
               status="harvested" if h_ok else "HARVEST-FAILED",
               seconds=round(time.time() - t0, 1), tail=r.stdout[-1200:])
        if h_ok:
            r = run([PYPY, "ladder.py", "spotcheck", "20", "4"])
            record("B_rung20_spotcheck",
                   status="done" if r.returncode == 0 else "FAILED",
                   tail=r.stdout[-400:])

    rc = count_proc.wait()
    record("C_count19", status="done" if rc == 0 else "FAILED",
           seconds=round(time.time() - t0, 1))

    record("finished", at_stage_wall_seconds=round(time.time() - t0, 1))
    print("followup_s022 complete")


if __name__ == "__main__":
    main()
