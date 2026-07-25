#!/usr/bin/env python3
"""Cross-architecture, cross-modulus set equality of the order-19 class.

The gate's partition check compares COUNTS.  This is the stronger statement:
the {C4,C8}-free order-19 class produced by the linux/amd64 build at the
production modulus must be the same SET of graphs, graph6 string for graph6
string, as the one the arm64 build produced at modulus 16 and the dossier
already records (E022, 74,589 graphs over 16 parts).

Equal counts plus equal sets rules out the failure mode counts alone cannot:
a part that drops one subtree and double-counts another.

Usage:  python3 crosscheck_n19.py <downloaded-calib-dir>
"""
import collections
import os
import sys

E022 = ("/Users/mattwatts/code/rh/problems/erdos-gyarfas/experiments/"
        "E022-the-g-profile-ladder-at-orders-18-and-19-via-the-e019-genera/"
        "data")


def load(paths):
    """graph6 -> (edges, n_degree2, power_free); flags duplicates."""
    rows = {}
    dupes = []
    for path in paths:
        with open(path) as fh:
            for line in fh:
                if line.startswith("#") or not line.strip():
                    continue
                g6, edges, n2, pf = line.split()[:4]
                if g6 in rows:
                    dupes.append((g6, path))
                rows[g6] = (edges, n2, pf)
    return rows, dupes


def main():
    calib_dir = sys.argv[1]
    local_paths = [os.path.join(E022, f) for f in sorted(os.listdir(E022))
                   if f.startswith("class_n19_part") and f.endswith(".txt")]
    local, local_dupes = load(local_paths)
    print("laptop  (arm64, mod 16): %d files, %d graphs, %d duplicates"
          % (len(local_paths), len(local), len(local_dupes)))
    assert not local_dupes, local_dupes[:5]

    by_mod = collections.defaultdict(list)
    for f in sorted(os.listdir(calib_dir)):
        if f.startswith("class_n19_part") and f.endswith(".txt"):
            by_mod[f.rsplit("of", 1)[1][:-4]].append(os.path.join(calib_dir, f))

    if not by_mod:
        print("no order-19 class files found in %s" % calib_dir)
        return 1

    failures = []
    for mod in sorted(by_mod, key=int):
        cloud, dupes = load(by_mod[mod])
        only_local = set(local) - set(cloud)
        only_cloud = set(cloud) - set(local)
        mismatched = [g for g in (set(local) & set(cloud))
                      if local[g] != cloud[g]]
        ok = (not dupes and not only_local and not only_cloud
              and not mismatched and len(cloud) == len(local))
        print("cloud (amd64, mod %-4s): %3d files, %d graphs, %d duplicates | "
              "only-laptop %d, only-cloud %d, field-mismatch %d  -> %s"
              % (mod, len(by_mod[mod]), len(cloud), len(dupes),
                 len(only_local), len(only_cloud), len(mismatched),
                 "SET-EQUAL" if ok else "MISMATCH"))
        if not ok:
            failures.append(mod)
            for g in list(only_local)[:3]:
                print("    only on the laptop: %s" % g)
            for g in list(only_cloud)[:3]:
                print("    only in the cloud : %s" % g)
            for g in mismatched[:3]:
                print("    fields differ %s: laptop %s vs cloud %s"
                      % (g, local[g], cloud[g]))

    print("")
    if failures:
        print("CROSS-CHECK FAILED at moduli: %s" % failures)
        return 1
    print("CROSS-CHECK PASSED — the amd64 build reproduces the recorded "
          "order-19 class exactly, as a set, at every modulus tested.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
