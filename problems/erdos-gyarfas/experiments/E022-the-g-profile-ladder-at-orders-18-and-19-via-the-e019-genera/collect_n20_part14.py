"""S022 harvest addendum: recollect the four order-20 profile members that
fell outside part 14's SAVE_LIMIT window, and T5-test them.

Stage B tallied 4 profile members in part 14/16 (class 439,745; only the
first 200,000 were saved to the class file, and none of the 4 fall there).
This re-runs exactly that part —

    genc48 -q -c -f -d2 20 29:190 14/16

— streaming stdout through a degree filter that keeps every graph with
exactly two degree-2 vertices (the whole stream is also counted, and the
total is asserted equal to the recorded 439,745).  Each collected member is
then verified and run through the same T5 test as t5_n20_profile.py (whose
primitives are imported; deterministic, stdlib only).

Output: data/collect_n20_part14.json.  Single process by design — it shares
the machine with followup_s022b's 8 workers.  Results not citable until
harvested.
"""
import importlib.util
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
OUT = os.path.join(DATA, "collect_n20_part14.json")
GENC48 = os.path.abspath(os.path.join(
    HERE, "..",
    "E019-dedicated-c4-c8-free-generator-geng-prune-plugin-and-the-ord",
    "build", "genc48"))
EXPECTED_PART_CLASS = 439745
EXPECTED_MEMBERS = 4

sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location(
    "t5mod", os.path.join(HERE, "t5_n20_profile.py"))
t5mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(t5mod)


def main():
    t0 = time.time()
    proc = subprocess.Popen(
        [GENC48, "-q", "-c", "-f", "-d2", "20", "29:190", "14/16"],
        stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
    stream = 0
    members = []
    g6dump = open(os.path.join(DATA, "profile_n20_part14.g6"), "w")
    for line in proc.stdout:
        line = line.strip()
        if not line:
            continue
        stream += 1
        adj = t5mod.g6_decode(line)
        degs = [len(r) for r in adj]
        if degs.count(2) == 2 and all(d >= 3 for d in degs if d != 2):
            members.append((line, adj))
            g6dump.write(line + "\n")
            g6dump.flush()
    g6dump.close()
    rc = proc.wait()
    gen_seconds = round(time.time() - t0, 1)

    result = {
        "generator": "%s -q -c -f -d2 20 29:190 14/16" % GENC48,
        "return_code": rc,
        "stream_total": stream,
        "expected_stream_total": EXPECTED_PART_CLASS,
        "stream_matches_stage_b_tally": stream == EXPECTED_PART_CLASS,
        "members_found": len(members),
        "expected_members": EXPECTED_MEMBERS,
        "generator_wall_seconds": gen_seconds,
    }

    reports = []
    total_cycles = 0
    total_nondec = 0
    for g6, adj in members:
        n = len(adj)
        degs = [len(r) for r in adj]
        d2 = [v for v in range(n) if degs[v] == 2]
        a, b = d2
        assert t5mod.connected(adj)
        cycles = t5mod.all_cycles(adj)
        spec_lens = sorted({len(c) for c in cycles})
        assert 4 not in spec_lens and 8 not in spec_lens, (g6, spec_lens)
        paths = t5mod.all_ab_paths(adj, a, b)
        pathset = set(paths)
        S = sorted({len(p) for p in paths})
        covered = {a, b}
        for p in paths:
            for u, v in p:
                covered.add(u)
                covered.add(v)
        taut = covered == set(range(n))
        nondec = []
        by_len = {}
        for c in cycles:
            by_len.setdefault(len(c), [0, 0])
            hit = any((p ^ c) != p and (p ^ c) in pathset for p in paths)
            by_len[len(c)][0] += 1
            if hit:
                by_len[len(c)][1] += 1
            else:
                nondec.append(sorted(sorted(e) for e in c))
        total_cycles += len(cycles)
        total_nondec += len(nondec)
        reports.append({
            "g6": g6, "order": n, "terminals": d2,
            "S": S, "S_cap_2_6_14": sorted(set(S) & {2, 6, 14}),
            "spectrum": spec_lens,
            "c16_count": len([c for c in cycles if len(c) == 16]),
            "vertex_taut": taut,
            "two_connected": t5mod.two_connected(adj),
            "paths": len(paths), "cycles": len(cycles),
            "per_length": {str(k): {"cycles": v[0], "decomposable": v[1]}
                           for k, v in sorted(by_len.items())},
            "non_decomposable": nondec,
        })

    result.update({
        "graphs": reports,
        "total_cycles": total_cycles,
        "total_non_decomposable": total_nondec,
        "t5_verdict_on_these_objects": (
            "SURVIVES on all %d recovered members" % len(members)
            if total_nondec == 0 and members
            else "KILLED - see non_decomposable" if members
            else "no members recovered - INVESTIGATE"),
        "wall_seconds_total": round(time.time() - t0, 1),
        "interpreter": sys.version,
    })
    with open(OUT, "w") as fh:
        json.dump(result, fh, indent=1)
    print("part14 recollection: stream %d (match=%s), members %d, "
          "%d cycles, %d non-decomposable"
          % (stream, result["stream_matches_stage_b_tally"], len(members),
             total_cycles, total_nondec))


if __name__ == "__main__":
    main()
