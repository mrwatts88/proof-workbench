"""S021 close-of-session background follow-up runs (orchestrator-launched).

Three stages, run sequentially so the machine is never oversubscribed:

  A. Corroborate the MathOverflow-512914 answer's cubic figures at order 20
     with stock geng: count connected cubic graphs (expect A002851(20) =
     510,489) and connected C4-free cubic graphs (the answer says 36,101).
  B. The min-degree-3 {C4,C8}-free sweep at order 20 with genc48 (16 parts,
     8 concurrent).  Empty output settles n = 20 for the class internally
     and unconditionally -- the MO thread's cubic-to-min-degree-3 step is
     not known to be valid, so this run is what actually decides n = 20.
     Any survivor is saved verbatim and additionally tested for C16.
  C. The Tier 3 bipartite leg at order 24 with genc48 -b (16 parts, 8
     concurrent), the E015 class one order past its order-23 harvest;
     survivors (expect none through the profile filter) saved verbatim.

Results land in data/followup_s021.json plus per-part g6 files.  This is a
follow-up harvest: nothing here may be cited by S021's ledgers; the next
session harvests it (AGENTS.md, unfinished-background-job rule).
"""

import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
BUILD = os.path.join(HERE, "build", "nauty2_9_3")
GENC48 = os.path.join(HERE, "build", "genc48")
GENG_STOCK = "/opt/homebrew/bin/geng"

sys.path.insert(0, HERE)
from scan import g6_decode, has_cycle_len, degrees  # noqa: E402  (E019's anchored copies)

CONCURRENCY = 8


def geng_count(binary, args):
    """Run a generator in -u mode; return the graph count from '>Z ... generated'."""
    proc = subprocess.run([binary, "-u"] + args, capture_output=True, text=True)
    assert proc.returncode == 0, proc.stderr
    for line in proc.stderr.splitlines():
        if ">Z" in line and "generated" in line:
            for tok in line.replace(">Z", " ").split():
                if tok.isdigit():
                    return int(tok)
    raise AssertionError("no >Z count line: %r" % proc.stderr)


def run_parts(tag, binary, common, n, erange, mod):
    """Run <mod> res/mod parts with CONCURRENCY concurrent processes.

    Returns (survivor lines, per-part counts, wall seconds)."""
    t0 = time.time()
    procs = {}
    outfiles = {}
    counts = {}
    pending = list(range(mod))
    running = []
    os.makedirs(DATA, exist_ok=True)
    while pending or running:
        while pending and len(running) < CONCURRENCY:
            r = pending.pop(0)
            path = os.path.join(DATA, "%s_part%dof%d.g6" % (tag, r, mod))
            fh = open(path, "w")
            outfiles[r] = path
            procs[r] = subprocess.Popen(
                [binary, "-q"] + common + [str(n), erange, "%d/%d" % (r, mod)],
                stdout=fh, stderr=subprocess.DEVNULL)
            running.append(r)
        time.sleep(2)
        for r in list(running):
            if procs[r].poll() is not None:
                assert procs[r].returncode == 0, "%s part %d failed" % (tag, r)
                running.remove(r)
    lines = []
    for r in range(mod):
        with open(outfiles[r]) as fh:
            part_lines = [ln.strip() for ln in fh if ln.strip()]
        counts[r] = len(part_lines)
        lines.extend(part_lines)
    return lines, counts, round(time.time() - t0, 1)


def main():
    report = {"owner": "S021 follow-up (orchestrator-launched background run)",
              "concurrency": CONCURRENCY}

    # A. MO-512914 corroboration at order 20 (stock geng, independent of genc48)
    t0 = time.time()
    cubic20 = geng_count(GENG_STOCK, ["-c", "-d3", "-D3", "20", "30:30"])
    c4free_cubic20 = geng_count(GENG_STOCK, ["-c", "-f", "-d3", "-D3", "20", "30:30"])
    report["stageA"] = {
        "cubic_n20": cubic20, "A002851_expect": 510489,
        "c4free_cubic_n20": c4free_cubic20, "mo_512914_reports": 36101,
        "wall_s": round(time.time() - t0, 1),
    }
    print("stage A: cubic20=%d (expect 510489), C4-free cubic20=%d (MO says 36101)"
          % (cubic20, c4free_cubic20), flush=True)

    # B. min-degree-3 {C4,C8}-free sweep at order 20
    lines, counts, wall = run_parts(
        "mindeg3_n20", GENC48, ["-c", "-f", "-d3"], 20, "30:190", 16)
    survivors = []
    for ln in lines:
        adj = g6_decode(ln)
        assert min(degrees(adj)) >= 3
        assert not has_cycle_len(adj, 4) and not has_cycle_len(adj, 8)
        survivors.append({"g6": ln, "has_c16": has_cycle_len(adj, 16)})
    report["stageB"] = {
        "class_c4c8free_mindeg3_n20": len(lines), "per_part": counts,
        "survivors": survivors, "wall_s": wall,
    }
    print("stage B: {C4,C8}-free min-deg-3 n=20 count = %d (wall %.0fs)"
          % (len(lines), wall), flush=True)

    # C. bipartite order 24 (E015 class, new instrument)
    lines, counts, wall = run_parts(
        "bip_n24", GENC48, ["-c", "-f", "-b", "-d2"], 24, "35:276", 16)
    survivors = []
    for ln in lines:
        adj = g6_decode(ln)
        deg2 = sum(1 for d in degrees(adj) if d == 2)
        survivors.append({"g6": ln, "num_deg2": deg2,
                          "profile": deg2 <= 2,
                          "has_c16": has_cycle_len(adj, 16)})
    report["stageC"] = {
        "class_bip_c4c8free_d2_n24": len(lines), "per_part": counts,
        "survivors": survivors, "wall_s": wall,
    }
    print("stage C: bipartite {C4,C8}-free -d2 n=24 count = %d (wall %.0fs)"
          % (len(lines), wall), flush=True)

    out = os.path.join(DATA, "followup_s021.json")
    with open(out, "w") as fh:
        json.dump(report, fh, indent=1)
    print("wrote %s" % out, flush=True)
    hits = ([s for s in report["stageB"]["survivors"] if not s["has_c16"]]
            + [s for s in report["stageC"]["survivors"]
               if s["profile"] and not s["has_c16"]])
    if hits:
        print("ATTENTION: power-free-relevant survivor(s) found -- do not "
              "integrate without the disproof protocol", flush=True)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
