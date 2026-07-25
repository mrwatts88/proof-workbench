#!/usr/bin/env python3
"""O012 step 5 (verify) — merge the downloaded production volumes into one
part set and check its integrity before anything is harvested.

Checks, in order, and every one of them fails loudly:
  1. every service reported status COMPLETE and no failed parts;
  2. every file listed in a run manifest hashes to the sha256 the container
     recorded for it, so a truncated or corrupted download cannot pass;
  3. the parts form the full residue system 0..mod-1 exactly once -- no gap,
     no part delivered twice by two services;
  4. each part's scan JSON self-describes as the order and part it is filed
     under (scan.py writes both fields, so a misfiled part is detectable);
  5. the per-part coverage identity profile == c16_blocked + survivors holds,
     which is scan.py's own invariant re-checked on this side of the wire;
  6. the extracted profile members are reported against the parts that had no
     class file, so a short list is never mistaken for a complete one.

Then it copies the merged set into <dest> so the LOCAL, already-anchored
instrument can run the harvest over it.

Usage:  python3 merge_verify.py <staging_dir> <order> <mod> <dest_dir>
"""
import hashlib
import json
import os
import shutil
import sys


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    staging, order, mod, dest = (sys.argv[1], int(sys.argv[2]),
                                 int(sys.argv[3]), sys.argv[4])
    part_dirs = sorted(os.path.join(staging, d) for d in os.listdir(staging)
                       if os.path.isdir(os.path.join(staging, d)))
    print("merging %d service volumes for order %d, modulus %d"
          % (len(part_dirs), order, mod))

    failures = []
    owner = {}            # part -> source directory
    profile_rows = []
    missing_class = []
    manifests = []

    for d in part_dirs:
        root = d
        if os.path.isdir(os.path.join(d, "e024")):
            root = os.path.join(d, "e024")
        mans = [f for f in os.listdir(root) if f.startswith("run_manifest_")]
        if not mans:
            failures.append("%s: no run manifest — that service never finished"
                            % os.path.basename(d))
            continue
        for mf in mans:
            with open(os.path.join(root, mf)) as fh:
                man = json.load(fh)
            manifests.append((os.path.basename(d), man))
            if man.get("status") != "COMPLETE":
                failures.append("%s/%s: status %r, failed parts %s"
                                % (os.path.basename(d), mf, man.get("status"),
                                   man.get("failed_parts")))
                continue
            # (2) hashes
            for name, want in sorted(man.get("sha256", {}).items()):
                path = os.path.join(root, name)
                if not os.path.exists(path):
                    failures.append("%s: %s listed in the manifest but absent"
                                    % (os.path.basename(d), name))
                elif sha256(path) != want:
                    failures.append("%s: %s sha256 mismatch (download corrupt)"
                                    % (os.path.basename(d), name))
            # (3) ownership
            for r in man.get("parts", []):
                if r in owner:
                    failures.append("part %d delivered twice: %s and %s"
                                    % (r, owner[r], os.path.basename(d)))
                owner[r] = os.path.basename(d)
            missing_class += man.get("parts_without_class_file", [])
            pf = os.path.join(root, man.get("profile_file", ""))
            if man.get("profile_file") and os.path.exists(pf):
                with open(pf) as fh:
                    profile_rows += [ln.rstrip("\n") for ln in fh
                                     if not ln.startswith("#") and ln.strip()]

    # (3) completeness
    expected = set(range(mod))
    have = set(owner)
    if have != expected:
        if expected - have:
            failures.append("missing parts: %s"
                            % sorted(expected - have)[:20])
        if have - expected:
            failures.append("unexpected parts: %s"
                            % sorted(have - expected)[:20])

    # (4) + (5) per-part self-description and coverage identity
    totals = {"generated_c4c8_free": 0, "profile": 0, "c16_blocked": 0,
              "survivors": 0, "seconds": 0.0}
    os.makedirs(dest, exist_ok=True)
    for r in sorted(have):
        src_dir = os.path.join(staging, owner[r])
        if os.path.isdir(os.path.join(src_dir, "e024")):
            src_dir = os.path.join(src_dir, "e024")
        name = "scan_n%d_part%dof%d.json" % (order, r, mod)
        path = os.path.join(src_dir, name)
        with open(path) as fh:
            tally = json.load(fh)
        if tally.get("order") != order or tally.get("part") != "%d/%d" % (r, mod):
            failures.append("%s self-describes as order %r part %r"
                            % (name, tally.get("order"), tally.get("part")))
            continue
        if tally["profile"] != tally["c16_blocked"] + len(tally["survivors"]):
            failures.append("%s violates profile == c16_blocked + survivors"
                            % name)
        totals["generated_c4c8_free"] += tally["generated_c4c8_free"]
        totals["profile"] += tally["profile"]
        totals["c16_blocked"] += tally["c16_blocked"]
        totals["survivors"] += len(tally["survivors"])
        totals["seconds"] += tally["seconds"]
        shutil.copy2(path, os.path.join(dest, name))
        cls = os.path.join(src_dir, "class_n%d_part%dof%d.txt" % (order, r, mod))
        if os.path.exists(cls):
            shutil.copy2(cls, os.path.join(dest, os.path.basename(cls)))

    merged_profile = os.path.join(dest, "profile_n%d_mod%d_merged.txt"
                                  % (order, mod))
    with open(merged_profile, "w") as fh:
        fh.write("# graph6 edges n_degree2 power_free part   "
                 "(merged degree-profile members, order %d, mod %d)\n"
                 % (order, mod))
        for row in sorted(set(profile_rows)):
            fh.write(row + "\n")

    print("")
    print("  parts present            : %d / %d" % (len(have), mod))
    print("  {C4,C8}-free generated    : %d" % totals["generated_c4c8_free"])
    print("  degree-profile members    : %d" % totals["profile"])
    print("    of those C16-blocked    : %d" % totals["c16_blocked"])
    print("    power-free survivors    : %d" % totals["survivors"])
    print("  generator cpu-seconds     : %.1f (%.1f core-hours)"
          % (totals["seconds"], totals["seconds"] / 3600.0))
    print("  profile members extracted : %d (deduped from %d rows)"
          % (len(set(profile_rows)), len(profile_rows)))
    print("  parts with no class file  : %d" % len(missing_class))
    if missing_class:
        print("    -> profile extraction is INCOMPLETE for %s"
              % [m["part"] for m in missing_class][:20])
    if len(set(profile_rows)) != totals["profile"] and not missing_class:
        failures.append("extracted %d profile members but the scan totals say "
                        "%d" % (len(set(profile_rows)), totals["profile"]))

    print("")
    if failures:
        print("MERGE FAILED — %d problem(s):" % len(failures))
        for f in failures[:40]:
            print("  " + f)
        return 1
    print("MERGE OK — %d parts verified and copied to %s" % (len(have), dest))
    print("Next: run the harvest with the LOCAL arm64 instrument over %s"
          % dest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
