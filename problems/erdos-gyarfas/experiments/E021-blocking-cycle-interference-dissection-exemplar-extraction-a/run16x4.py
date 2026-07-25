#!/usr/bin/env python3
"""E021 — order-16 family-(1) extraction driver: 24 res/mod parts, at most
FOUR concurrent worker processes (S022 machine-sharing allocation: the
sibling worker holds 8 of 12 cores).  Each part is `pypy3 dissect.py extract
16 r/24`.  Skips parts whose output JSON already exists (restartable)."""

import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
SLOTS = 4
PARTS = 24
PYPY = "pypy3"

pending = [r for r in range(PARTS)
           if not os.path.exists(
               os.path.join(DATA, "extract_n16_part%dof24.json" % r))]
print("parts to run: %s" % pending)
running = {}
t0 = time.time()
failures = []
while pending or running:
    while pending and len(running) < SLOTS:
        r = pending.pop(0)
        proc = subprocess.Popen(
            [PYPY, os.path.join(HERE, "dissect.py"), "extract", "16",
             "%d/24" % r],
            cwd=HERE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        running[r] = proc
        print("[%.0fs] started part %d (%d running)"
              % (time.time() - t0, r, len(running)))
    done = [r for r, p in running.items() if p.poll() is not None]
    for r in done:
        proc = running.pop(r)
        out = proc.stdout.read().decode().strip()
        if proc.returncode != 0:
            failures.append(r)
            print("[%.0fs] PART %d FAILED (rc=%d):\n%s"
                  % (time.time() - t0, r, proc.returncode, out))
        else:
            print("[%.0fs] part %d done: %s"
                  % (time.time() - t0, r, out.splitlines()[-1]))
    if not done:
        time.sleep(5)
print("all parts finished in %.0fs wall; failures: %s"
      % (time.time() - t0, failures))
sys.exit(1 if failures else 0)
