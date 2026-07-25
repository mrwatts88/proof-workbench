#!/usr/bin/env python3
"""E022 -- collect the per-order production statistics into one table.

Reads the part tallies written by `ladder.py run` and prints/writes the row
that goes into the README: class size, degree-2 histogram, profile counts,
power-free counts, survivors, edge maxima, tree nodes, prune rejects,
generator CPU, and the Python wall figures (sum over parts and slowest part).

    <python> summary.py [N ...]
writes data/summary.json.
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")


def collect(root, n, parts):
    acc = {
        "order": n, "parts": parts, "root": os.path.relpath(root, HERE),
        "class": 0, "profile": 0, "c16_blocked": 0, "survivors": 0,
        "power_free_in_class": 0, "tree_nodes": 0, "prune_rejects": 0,
        "generator_cpu": 0.0, "python_wall_sum": 0.0, "python_wall_max": 0.0,
        "max_edges_in_class": 0, "max_edges_in_profile": 0,
    }
    deg2, pfdeg2 = {}, {}
    rows_in_files = 0
    for r in range(parts):
        with open(os.path.join(root, "scan_n%d_part%dof%d.json" % (n, r, parts))) as fh:
            t = json.load(fh)
        cpath = os.path.join(root, "class_n%d_part%dof%d.txt" % (n, r, parts))
        with open(cpath) as fh:
            rows_in_files += sum(1 for line in fh if not line.startswith("#"))
        acc["class"] += t["generated_c4c8_free"]
        acc["profile"] += t["profile"]
        acc["c16_blocked"] += t["c16_blocked"]
        acc["survivors"] += len(t["survivors"])
        acc["power_free_in_class"] += t["power_free_in_class"]
        acc["tree_nodes"] += t["prune_total"]["calls"]
        acc["prune_rejects"] += t["prune_total"]["rejects"]
        acc["generator_cpu"] += t["prune_total"]["cpu"]
        acc["python_wall_sum"] += t["seconds"]
        acc["python_wall_max"] = max(acc["python_wall_max"], t["seconds"])
        acc["max_edges_in_class"] = max(acc["max_edges_in_class"], t["max_edges_in_class"])
        acc["max_edges_in_profile"] = max(acc["max_edges_in_profile"],
                                          t["max_edges_in_profile"])
        assert t["verify_all"], "part %d/%d ran without --verify-all" % (r, parts)
        for k, v in t["deg2_hist"].items():
            deg2[int(k)] = deg2.get(int(k), 0) + v
        for k, v in t["power_free_deg2_hist"].items():
            pfdeg2[int(k)] = pfdeg2.get(int(k), 0) + v
    acc["generator_cpu"] = round(acc["generator_cpu"], 1)
    acc["python_wall_sum"] = round(acc["python_wall_sum"], 1)
    acc["deg2_hist"] = {str(k): v for k, v in sorted(deg2.items())}
    acc["power_free_deg2_hist"] = {str(k): v for k, v in sorted(pfdeg2.items())}
    acc["min_deg2_in_class"] = min(deg2) if deg2 else None
    acc["power_free_min_deg2"] = min(pfdeg2) if pfdeg2 else None
    acc["bucket_0"] = deg2.get(0, 0)
    acc["bucket_1"] = deg2.get(1, 0)
    acc["bucket_2"] = deg2.get(2, 0)
    acc["power_free_bucket_0"] = pfdeg2.get(0, 0)
    acc["power_free_bucket_1"] = pfdeg2.get(1, 0)
    acc["power_free_bucket_2"] = pfdeg2.get(2, 0)
    acc["class_file_rows"] = rows_in_files
    assert acc["profile"] == acc["c16_blocked"] + acc["survivors"], "coverage identity"
    assert acc["profile"] == acc["bucket_2"], "profile != the 2-bucket"
    assert rows_in_files == acc["class"], (
        "the saved class files hold %d graphs but the tallies say %d"
        % (rows_in_files, acc["class"]))
    return acc


def main():
    rows = [collect(DATA, 18, 16), collect(DATA, 19, 16)]
    split24 = os.path.join(DATA, "split24")
    if os.path.exists(os.path.join(split24, "scan_n19_part23of24.json")):
        rows.append(collect(split24, 19, 24))
    for row in rows:
        cnt = os.path.join(DATA, "count_n%d.json" % row["order"])
        if row["parts"] == 16 and os.path.exists(cnt):
            with open(cnt) as fh:
                c = json.load(fh)
            row["unsplit_count"] = c["out"]
            row["unsplit_tree_nodes"] = c["prune_calls"]
            row["unsplit_wall"] = c["wall"]
            row["unsplit_matches_parts"] = (c["out"] == row["class"])
            assert row["unsplit_matches_parts"], "unsplit count != summed parts"
    with open(os.path.join(DATA, "summary.json"), "w") as fh:
        json.dump(rows, fh, indent=1)
    print(json.dumps(rows, indent=1))


if __name__ == "__main__":
    main()
