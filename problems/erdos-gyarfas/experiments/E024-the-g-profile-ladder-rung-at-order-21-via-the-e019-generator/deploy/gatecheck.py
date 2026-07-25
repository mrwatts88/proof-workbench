#!/usr/bin/env python3
"""O012 step 2 — the blocking anchor re-gate for the linux/amd64 rebuild.

The repository pins `genc48` by sha256.  A different-architecture rebuild
breaks that pin, so the cloud binary is a NEW INSTRUMENT and none of its output
is citable until it reproduces, field for field, what the arm64 build recorded.

This script does the comparison locally, against the files already in the
dossier.  It compares:

    anchors_pypy.json      the 146-check suite  (vs E019/data and E024/data)
    cubic24_check.json     the cubic order-24 positive control, set-equal to
                           E005 and equal to Markstroem Table 3's count of 4
    crosscheck_mindeg3.json  genc48 vs the filtered stock-geng stream, as
                           labelg-canonical SETS, orders 12-17

Wall-clock fields and the interpreter string are excluded from the comparison
(they are expected to differ); EVERY other field must match exactly.  A
difference anywhere is a gate failure.

Usage:  python3 gatecheck.py <downloaded-gate-dir>
"""
import json
import os
import sys

REPO = "/Users/mattwatts/code/rh/problems/erdos-gyarfas/experiments"
E019 = os.path.join(REPO, "E019-dedicated-c4-c8-free-generator-geng-prune-"
                          "plugin-and-the-ord", "data")
E024 = os.path.join(REPO, "E024-the-g-profile-ladder-rung-at-order-21-via-"
                          "the-e019-generator", "data")

VOLATILE = {"interpreter", "wall", "seconds", "genc48_wall", "stream_wall"}


def strip(obj):
    if isinstance(obj, dict):
        return {k: strip(v) for k, v in obj.items() if k not in VOLATILE}
    if isinstance(obj, list):
        return [strip(v) for v in obj]
    return obj


def diff(a, b, path=""):
    """Every leaf disagreement between two stripped JSON trees."""
    out = []
    if type(a) is not type(b):
        return ["%s: type %s vs %s" % (path or ".", type(a).__name__,
                                       type(b).__name__)]
    if isinstance(a, dict):
        for k in sorted(set(a) | set(b)):
            if k not in a:
                out.append("%s.%s: missing on the recorded side" % (path, k))
            elif k not in b:
                out.append("%s.%s: missing on the cloud side" % (path, k))
            else:
                out += diff(a[k], b[k], "%s.%s" % (path, k))
    elif isinstance(a, list):
        if len(a) != len(b):
            out.append("%s: length %d vs %d" % (path, len(a), len(b)))
        for i, (x, y) in enumerate(zip(a, b)):
            out += diff(x, y, "%s[%d]" % (path, i))
    elif a != b:
        out.append("%s: %r vs %r" % (path, a, b))
    return out


def compare(name, recorded_path, cloud_dir, failures):
    cloud_path = os.path.join(cloud_dir, name)
    if not os.path.exists(cloud_path):
        failures.append("%s: MISSING from the cloud output" % name)
        return
    if not os.path.exists(recorded_path):
        failures.append("%s: no recorded file at %s" % (name, recorded_path))
        return
    with open(recorded_path) as fh:
        rec = strip(json.load(fh))
    with open(cloud_path) as fh:
        new = strip(json.load(fh))
    d = diff(rec, new)
    if d:
        failures.append("%s: %d difference(s)" % (name, len(d)))
        for line in d[:25]:
            failures.append("    %s" % line)
    else:
        print("  OK  %s — identical to %s (ignoring %s)"
              % (name, os.path.relpath(recorded_path, REPO),
                 ", ".join(sorted(VOLATILE))))


def main():
    cloud_dir = sys.argv[1]
    print("gate comparison: %s" % cloud_dir)
    failures = []

    compare("anchors_pypy.json", os.path.join(E019, "anchors_pypy.json"),
            cloud_dir, failures)
    compare("anchors_pypy.json", os.path.join(E024, "anchors_pypy.json"),
            cloud_dir, failures)
    compare("cubic24_check.json", os.path.join(E019, "cubic24_check.json"),
            cloud_dir, failures)
    compare("crosscheck_mindeg3.json",
            os.path.join(E019, "crosscheck_mindeg3.json"), cloud_dir, failures)

    man_path = os.path.join(cloud_dir, "gate_manifest.json")
    if not os.path.exists(man_path):
        failures.append("gate_manifest.json: MISSING — the gate did not finish")
    else:
        with open(man_path) as fh:
            man = json.load(fh)
        prov = man.get("provenance", {})
        part = man.get("stages", {}).get("partition", {})
        print("\n  architecture      : %s (%s)" % (prov.get("architecture"),
                                                   prov.get("kernel")))
        print("  interpreter       : %s" % prov.get("interpreter"))
        print("  cpu_count         : %s" % prov.get("cpu_count"))
        print("  genc48 sha256     : %s   <-- the amd64 pin" %
              prov.get("genc48_sha256"))
        print("  geng   sha256     : %s" % prov.get("geng_reference_sha256"))
        print("  scan.py sha256    : %s" % prov.get("scan_py_sha256"))
        print("  prune_c8.c sha256 : %s" % prov.get("prune_c8_c_sha256"))
        print("  partition check   : order %s, modulus %s, unsplit %s, "
              "split total %s, exact=%s, nonempty %s/%s, max share %s"
              % (part.get("order"), part.get("modulus"), part.get("unsplit"),
                 part.get("split_total"), part.get("exact"),
                 part.get("nonempty_parts"), part.get("modulus"),
                 part.get("max_part_share")))
        # scan.py and prune_c8.c must be byte-identical to the dossier's
        import hashlib

        def sha(p):
            h = hashlib.sha256()
            with open(p, "rb") as fh:
                for c in iter(lambda: fh.read(1 << 20), b""):
                    h.update(c)
            return h.hexdigest()

        src = os.path.join(REPO, "E019-dedicated-c4-c8-free-generator-geng-"
                                 "prune-plugin-and-the-ord")
        for key, path in (("scan_py_sha256", os.path.join(src, "scan.py")),
                          ("prune_c8_c_sha256",
                           os.path.join(src, "prune_c8.c"))):
            local = sha(path)
            if prov.get(key) != local:
                failures.append("%s differs: cloud %s vs local %s"
                                % (key, prov.get(key), local))
            else:
                print("  OK  %s matches the dossier byte for byte" % key)
        if not part.get("exact"):
            failures.append("production-modulus partition check is not exact")

    print("")
    if failures:
        print("GATE FAILED")
        for f in failures:
            print("  " + f)
        return 1
    print("GATE PASSED — the amd64 build reproduces every recorded anchor.")
    print("Its output may now be cited, under the architecture-tagged pin "
          "above (recorded beside, not replacing, the arm64 pin).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
