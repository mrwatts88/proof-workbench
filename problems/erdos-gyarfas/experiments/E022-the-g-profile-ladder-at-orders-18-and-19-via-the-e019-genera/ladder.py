#!/usr/bin/env python3
"""E022 -- the G-profile ladder at orders 18 and 19.

Thin wrapper around `E019/scan.py`.  The instrument itself -- the `genc48`
PREPRUNE generator, the E015 cycle primitives, the 146-check anchor suite and
the scan/harvest/count/spotcheck commands -- belongs to E019 and is NOT copied
here.  This module imports `E019/scan.py` from its own file path and redirects
that module's `DATA` constant to E022's data directory, so E019's tree is only
ever read.  `GENC48`/`GENG` (absolute paths into `E019/build`) are reused
unchanged, which is the point: the same sha256-checked nauty 2.9.3 build.

Guarantees enforced here
------------------------
* `sys.dont_write_bytecode` is set before the import, so not even a
  `__pycache__` entry is written into E019.
* `E019/data` is listed immediately before and after the import and the two
  listings must agree -- an explicit check that the import has no side effect
  on E019's data.
* every output path used by scan.py is derived from its module-level `DATA`,
  which is rebound before any command is dispatched.

Usage
-----
    <python> ladder.py [--data SUBDIR] <command> [args ...]

`<command>` is any E019/scan.py command (`anchors`, `count`, `run`, `harvest`,
`spotcheck`, `probe`, `crosscheck`, `subcubic`, `cubic24`); its arguments are
passed through verbatim.  `--data SUBDIR` puts the outputs in
`E022/data/SUBDIR` instead of `E022/data` (used for the 24-part order-19
partition check, so that its files never collide with the 16-part run).

Extra commands defined here
---------------------------
    provenance                 sha256 of the imported scan.py and of genc48
    splitcheck N A B           compare the order-N class from the A-part run
                               (data/) with the one from the B-part run
                               (data/split<B>/) as labelg canonical SETS, and
                               cross-check every aggregate in the two harvests
"""

import hashlib
import json
import os
import subprocess
import sys

sys.dont_write_bytecode = True          # never write into E019/__pycache__
import importlib.util                   # noqa: E402  (after the flag above)

HERE = os.path.dirname(os.path.abspath(__file__))
E019 = os.path.abspath(os.path.join(
    HERE, os.pardir,
    "E019-dedicated-c4-c8-free-generator-geng-prune-plugin-and-the-ord"))
SCAN_PY = os.path.join(E019, "scan.py")
E019_DATA = os.path.join(E019, "data")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_scan(data_dir):
    """Import E019/scan.py and redirect its DATA constant to `data_dir`."""
    before = sorted(os.listdir(E019_DATA))
    spec = importlib.util.spec_from_file_location("e019_scan", SCAN_PY)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    after = sorted(os.listdir(E019_DATA))
    assert before == after, (
        "importing E019/scan.py changed E019/data: %r"
        % (set(after) ^ set(before)))
    assert not os.path.exists(os.path.join(E019, "__pycache__", "scan.pyc")), \
        "bytecode written into E019"
    # the only rebinding: every output path in scan.py is DATA-relative
    assert mod.DATA == E019_DATA, "unexpected DATA in scan.py: %r" % mod.DATA
    mod.DATA = data_dir
    os.makedirs(data_dir, exist_ok=True)
    # the generator paths are absolute into E019/build and are reused as-is
    assert os.path.exists(mod.GENC48) and os.path.exists(mod.GENG)
    return mod


def cmd_provenance(mod, data_dir, _args):
    row = {
        "scan_py": SCAN_PY,
        "scan_py_sha256": sha256(SCAN_PY),
        "genc48": mod.GENC48,
        "genc48_sha256": sha256(mod.GENC48),
        "geng_reference": mod.GENG,
        "geng_reference_sha256": sha256(mod.GENG),
        "prune_c8_c_sha256": sha256(os.path.join(E019, "prune_c8.c")),
        "labelg": subprocess.run(["which", "labelg"], stdout=subprocess.PIPE)
                            .stdout.decode().strip(),
        "interpreter": mod.interpreter(),
        "data_dir": data_dir,
    }
    with open(os.path.join(data_dir, "provenance.json"), "w") as fh:
        json.dump(row, fh, indent=1)
    print(json.dumps(row, indent=1))


def _load_split(mod, root, n, parts):
    """Read one res/mod split of order n: the part tallies and the saved class."""
    g6 = []
    generated = 0
    agg = {"profile": 0, "c16_blocked": 0, "survivors": 0}
    deg2 = {}
    pf_deg2 = {}
    max_e = 0
    for r in range(parts):
        jpath = os.path.join(root, "scan_n%d_part%dof%d.json" % (n, r, parts))
        cpath = os.path.join(root, "class_n%d_part%dof%d.txt" % (n, r, parts))
        with open(jpath) as fh:
            tally = json.load(fh)
        assert tally["order"] == n and tally["part"] == "%d/%d" % (r, parts)
        generated += tally["generated_c4c8_free"]
        agg["profile"] += tally["profile"]
        agg["c16_blocked"] += tally["c16_blocked"]
        agg["survivors"] += len(tally["survivors"])
        max_e = max(max_e, tally["max_edges_in_class"])
        for k, v in tally["deg2_hist"].items():
            deg2[int(k)] = deg2.get(int(k), 0) + v
        for k, v in tally["power_free_deg2_hist"].items():
            pf_deg2[int(k)] = pf_deg2.get(int(k), 0) + v
        assert os.path.exists(cpath), (
            "class file missing for part %d/%d -- the part exceeded scan.py's "
            "SAVE_LIMIT and the graphs were not saved" % (r, parts))
        rows = 0
        with open(cpath) as fh:
            for line in fh:
                if line.startswith("#"):
                    continue
                g6.append(line.split()[0])
                rows += 1
        assert rows == tally["generated_c4c8_free"], (
            "class file %s holds %d graphs but the tally says %d"
            % (cpath, rows, tally["generated_c4c8_free"]))
    return {"generated": generated, "g6": g6, "max_edges_in_class": max_e,
            "deg2_hist": {str(k): v for k, v in sorted(deg2.items())},
            "power_free_deg2_hist": {str(k): v for k, v in sorted(pf_deg2.items())},
            **agg}


def cmd_splitcheck(mod, data_dir, args):
    """Partition check: the same order, split two different ways, compared as
    labelg canonical SETS (not merely as counts)."""
    n, a, b = int(args[0]), int(args[1]), int(args[2])
    root_a = os.path.join(HERE, "data")
    root_b = os.path.join(HERE, "data", "split%d" % b)
    A = _load_split(mod, root_a, n, a)
    B = _load_split(mod, root_b, n, b)
    set_a = mod.canonical_set(A["g6"])
    set_b = mod.canonical_set(B["g6"])
    row = {
        "order": n,
        "split_a": {"parts": a, "root": root_a,
                    **{k: v for k, v in A.items() if k != "g6"},
                    "canonical_forms": len(set_a)},
        "split_b": {"parts": b, "root": root_b,
                    **{k: v for k, v in B.items() if k != "g6"},
                    "canonical_forms": len(set_b)},
        "totals_equal": A["generated"] == B["generated"],
        "isomorph_free_a": len(set_a) == len(A["g6"]),
        "isomorph_free_b": len(set_b) == len(B["g6"]),
        "set_equal": set_a == set_b,
        "aggregates_equal": all(
            A[k] == B[k] for k in ("profile", "c16_blocked", "survivors",
                                   "max_edges_in_class", "deg2_hist",
                                   "power_free_deg2_hist")),
        "interpreter": mod.interpreter(),
    }
    out = os.path.join(HERE, "data", "splitcheck_n%d_%dvs%d.json" % (n, a, b))
    with open(out, "w") as fh:
        json.dump(row, fh, indent=1)
    print(json.dumps(row, indent=1))
    assert row["totals_equal"], "part totals differ"
    assert row["isomorph_free_a"] and row["isomorph_free_b"], "duplicates found"
    assert row["set_equal"], "the two splits produced different graph sets"
    assert row["aggregates_equal"], "the two splits disagree on an aggregate"
    print("PARTITION CHECK PASSED: order %d, %d-part and %d-part runs are "
          "set-equal (%d canonical forms)" % (n, a, b, len(set_a)))


EXTRA = {"provenance": cmd_provenance, "splitcheck": cmd_splitcheck}


def main():
    argv = sys.argv[1:]
    sub = None
    if argv and argv[0] == "--data":
        sub = argv[1]
        argv = argv[2:]
    data_dir = os.path.join(HERE, "data", sub) if sub else os.path.join(HERE, "data")
    if not argv:
        print(__doc__)
        sys.exit(1)
    cmd, rest = argv[0], argv[1:]
    mod = load_scan(data_dir)
    if cmd in EXTRA:
        EXTRA[cmd](mod, data_dir, rest)
        return
    table = {
        "anchors": mod.cmd_anchors, "count": mod.cmd_count,
        "probe": mod.cmd_probe, "cubic24": mod.cmd_cubic24,
        "subcubic": mod.cmd_subcubic, "spotcheck": mod.cmd_spotcheck,
        "crosscheck": mod.cmd_crosscheck, "run": mod.cmd_run,
        "harvest": mod.cmd_harvest,
    }
    if cmd not in table:
        print(__doc__)
        sys.exit(1)
    table[cmd](rest)


if __name__ == "__main__":
    main()
