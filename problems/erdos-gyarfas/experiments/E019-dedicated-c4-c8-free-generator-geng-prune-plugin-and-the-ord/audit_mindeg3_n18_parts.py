"""S021 orchestrator audit addendum for E019's flagged min-degree-3 result.

Stream-side slice cross-check at order 18 -- the first order of the
`probe mindeg3` sweep with no full filter-the-stream reference (the full
order-18 stream is ~8e8 graphs).  Each geng res/mod part is a deterministic,
exhaustive slice of the stock stream, so checking parts r/24 gives an exact
verdict on those slices: if genc48's order-18 emptiness claim is wrong, a
{C4,C8}-free min-degree-3 graph of order 18 exists, and any part containing
it refutes the claim outright.

Instruments deliberately taken from OUTSIDE this experiment:
  - stock geng: /opt/homebrew/bin/geng (the E010-E018 anchored binary), NOT
    the tree built by build.sh;
  - C8 detector: has_cycle_len imported from E015/bipscan.py at its original
    path, NOT scan.py's copy.

Usage:  python3 audit_mindeg3_n18_parts.py <res> [<res> ...]   (mod fixed 24)
Writes data/audit_mindeg3_n18_part<res>of24.json per part.
Exit 1 if any C8-free survivor is found in a sampled slice.
"""

import importlib.util
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
E015 = os.path.normpath(os.path.join(
    HERE, "..",
    "E015-exhaustive-bipartite-power-free-gadget-hunt-past-the-general",
    "bipscan.py"))
GENG = "/opt/homebrew/bin/geng"

N = 18
MINE = 27          # ceil(3*18/2): forced by minimum degree 3
MAXE = 153         # C(18,2): coverage-safe
MOD = 24

spec = importlib.util.spec_from_file_location("bipscan", E015)
bipscan = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bipscan)
g6_decode = bipscan.g6_decode
degrees = bipscan.degrees
has_cycle_len = bipscan.has_cycle_len
from_edges = bipscan.from_edges

# anchor the imported detector before use (fixed objects, recorded verdicts)
petersen = from_edges(10, [(i, (i + 1) % 5) for i in range(5)]
                      + [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
                      + [(i, i + 5) for i in range(5)])
c8 = from_edges(8, [(i, (i + 1) % 8) for i in range(8)])
c9 = from_edges(9, [(i, (i + 1) % 9) for i in range(9)])
k4 = from_edges(4, [(a, b) for a in range(4) for b in range(a + 1, 4)])
assert has_cycle_len(petersen, 8)        # spectrum {5,6,8,9}
assert has_cycle_len(c8, 8)
assert not has_cycle_len(c9, 8)
assert not has_cycle_len(k4, 8)


def run_part(res: int) -> dict:
    part = "%d/%d" % (res, MOD)
    cmd = [GENG, "-q", "-c", "-f", "-d3", str(N),
           "%d:%d" % (MINE, MAXE), part]
    t0 = time.time()
    stream = 0
    survivors = []
    mindeg_bad = 0
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=1 << 20)
    assert proc.stdout is not None
    for raw in proc.stdout:
        stream += 1
        line = raw.decode().strip()
        adj = g6_decode(line)
        if min(degrees(adj)) < 3:
            mindeg_bad += 1     # would indicate a driver bug; count, do not skip
        if not has_cycle_len(adj, 8):
            survivors.append(line)
    rc = proc.wait()
    assert rc == 0, "geng exited %d on part %s" % (rc, part)
    assert mindeg_bad == 0, "min-degree violation in stock stream"
    row = {
        "order": N, "mine": MINE, "maxe": MAXE, "part": part,
        "geng": GENG, "detector": "E015/bipscan.py has_cycle_len",
        "stream": stream, "c8_free_survivors": survivors,
        "wall_s": round(time.time() - t0, 1),
        "python": sys.version.split()[0],
    }
    os.makedirs(DATA, exist_ok=True)
    out = os.path.join(DATA, "audit_mindeg3_n18_part%dof%d.json" % (res, MOD))
    with open(out, "w") as fh:
        json.dump(row, fh, indent=1)
    print("part %s: stream=%d C8-free=%d wall=%.1fs -> %s"
          % (part, stream, len(survivors), row["wall_s"], out))
    return row


def main() -> int:
    bad = 0
    for arg in sys.argv[1:]:
        row = run_part(int(arg))
        if row["c8_free_survivors"]:
            bad += 1
    if bad:
        print("REFUTATION: C8-free min-degree-3 graph(s) found at order 18")
        return 1
    print("all sampled parts empty: consistent with the genc48 verdict")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
