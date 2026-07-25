"""S022 chained Tier-3 stage D (orchestrator-launched, mid-wait): the
min-degree-3 {C4,C8}-free sweep at order 21.

Waits for followup_s022.py to finish (polls data/followup_s022.json for its
"finished" stage), re-passes the anchor gate, then runs

    genc48 -q -c -f -d3 21 32:210 r/16        (mine = ceil(3*21/2) = 32)

16 parts, 8 concurrent — the C040 pattern one order up (S021 stage B ran
order 20 the same way).  Expected empty; an empty sweep would lift L047's
counterexample floor to 22 AT HARVEST (nothing is claimed here).  A nonzero
part output is preserved verbatim (a power-free member would be pivot-grade;
see STATE.md pivot triggers).

Results are NOT citable until harvested by a session.  Output:
  data/mindeg3_n21_part{r}of16.g6   (expected empty files)
  data/mindeg3_n21_summary.json
"""
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
STATUS = os.path.join(DATA, "followup_s022.json")
OUT = os.path.join(DATA, "mindeg3_n21_summary.json")
GENC48 = os.path.join(HERE, "..",
                      "E019-dedicated-c4-c8-free-generator-geng-prune-plugin-and-the-ord",
                      "build", "genc48")
GENC48 = os.path.abspath(GENC48)
N, MINE, MAXE, MOD = 21, 32, 210, 16


def stage_a_done():
    try:
        with open(STATUS) as fh:
            return "finished" in json.load(fh)["stages"]
    except Exception:
        return False


def main():
    waited = 0
    while not stage_a_done():
        time.sleep(60)
        waited += 60
        if waited > 8 * 3600:
            with open(OUT, "w") as fh:
                json.dump({"status": "ABORTED",
                           "reason": "followup_s022 not finished after 8 h"},
                          fh, indent=1)
            sys.exit(1)

    # Anchor gate, re-passed after the wait (process rule; ~4 s).
    r = subprocess.run(["pypy3", "ladder.py", "anchors"], cwd=HERE,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                       text=True)
    if r.returncode != 0:
        with open(OUT, "w") as fh:
            json.dump({"status": "ABORTED", "reason": "anchor gate failed",
                       "tail": r.stdout[-400:]}, fh, indent=1)
        sys.exit(1)

    t0 = time.time()
    parts = list(range(MOD))
    running = {}
    outputs = {}
    rcs = {}
    while parts or running:
        while parts and len(running) < 8:
            p = parts.pop(0)
            path = os.path.join(DATA, "mindeg3_n%d_part%dof%d.g6" % (N, p, MOD))
            outputs[p] = path
            running[p] = subprocess.Popen(
                [GENC48, "-q", "-c", "-f", "-d3", str(N),
                 "%d:%d" % (MINE, MAXE), "%d/%d" % (p, MOD)],
                stdout=open(path, "w"), stderr=subprocess.DEVNULL)
        done = [p for p, pr in running.items() if pr.poll() is not None]
        if not done:
            time.sleep(20)
            continue
        for p in done:
            rcs[p] = running[p].returncode
            del running[p]

    counts = {}
    for p, path in outputs.items():
        with open(path) as fh:
            counts[str(p)] = sum(1 for _ in fh)
    total = sum(counts.values())
    result = {
        "status": "done",
        "order": N,
        "generator": "%s -q -c -f -d3 %d %d:%d r/%d" % (GENC48, N, MINE, MAXE, MOD),
        "parts": MOD,
        "return_codes": {str(p): rcs[p] for p in sorted(rcs)},
        "per_part_output_counts": counts,
        "total_output": total,
        "verdict_pending_harvest": ("EMPTY (would lift L047 to 22 at harvest)"
                                    if total == 0 else
                                    "NONZERO OUTPUT - preserve and analyse at "
                                    "harvest; see pivot triggers"),
        "wall_seconds": round(time.time() - t0, 1),
        "anchor_gate": "146 checks re-passed post-wait (pypy3)",
    }
    with open(OUT, "w") as fh:
        json.dump(result, fh, indent=1)
    print("mindeg3 n=21 sweep: total output %d, %.0f s wall"
          % (total, result["wall_seconds"]))


if __name__ == "__main__":
    main()
