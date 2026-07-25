#!/usr/bin/env pypy3
"""E024 in the cloud — the order-21 G-profile ladder rung on Railway (O012).

Same relationship to the instrument as `rung21.py`: this is a *driver*.  Every
mathematical operation is E019/scan.py's, reached through E022/ladder.py's
`load_scan`, which redirects scan.py's DATA constant and leaves E019's tree
read-only.  Nothing here computes a graph property.

What is different from `rung21.py`, and only this:

  * the parts are a res/mod split at a *larger* modulus (E024_MOD, default
    512) instead of 16, and each container runs an assigned subset of them.
    Partition-independence of genc48's res/mod split is the standing
    precedent C043; the `gate` mode below re-checks it at the production
    modulus on this build before any production part runs;
  * a `gate` mode that runs the whole re-anchoring suite this architecture
    needs before its output may be cited (O012 step 2);
  * after the parts finish, the class files are filtered to the degree-profile
    members (n_degree_2 == 2) so the decisive order-21 measurement can be made
    locally on a few dozen graph6 strings instead of shipping the whole class
    back.  The filter is plain text selection over a column scan.py already
    writes, and every filtered count is asserted against the `profile` field
    of that part's scan JSON.

Modes (E024_MODE):
    gate            anchors + cubic-24 positive control + stream cross-check
                    + production-modulus partition check + provenance hashes
    run             run the parts named by E024_PARTS, then extract + manifest
    part <r>/<mod>  one part (spawned by `run`)

Environment:
    E024_DATA     output directory (the mounted volume)      [/data/e024]
    E024_ORDER    order to scan                              [21]
    E024_MOD      res/mod modulus                            [512]
    E024_PARTS    "a-b" | "k/S" (stride) | "0,3,9"           [all]
    E024_WORKERS  concurrent parts in this container         [8]
    E024_HOLD     keep the container alive after finishing   [1]

Deterministic; wall-clock timings only.
"""
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import time

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
E022 = os.path.abspath(os.path.join(
    HERE, os.pardir,
    "E022-the-g-profile-ladder-at-orders-18-and-19-via-the-e019-genera"))

DATA = os.environ.get("E024_DATA", "/data/e024")
ORDER = int(os.environ.get("E024_ORDER", "21"))
MOD = int(os.environ.get("E024_MOD", "512"))
WORKERS = int(os.environ.get("E024_WORKERS", "8"))
HOLD = os.environ.get("E024_HOLD", "1") == "1"

spec = importlib.util.spec_from_file_location(
    "e022_ladder", os.path.join(E022, "ladder.py"))
ladder = importlib.util.module_from_spec(spec)
sys.modules["e022_ladder"] = ladder
spec.loader.exec_module(ladder)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def say(msg):
    print("[e024] %s" % msg)
    sys.stdout.flush()


def write_json(name, obj):
    os.makedirs(DATA, exist_ok=True)
    path = os.path.join(DATA, name)
    with open(path, "w") as fh:
        json.dump(obj, fh, indent=1, sort_keys=True)
    return path


def parse_parts(spec_text, mod):
    """"a-b" inclusive | "k/S" stride | comma list | "" = every part."""
    if not spec_text:
        return list(range(mod))
    spec_text = spec_text.strip()
    if "/" in spec_text:
        k, s = spec_text.split("/")
        k, s = int(k), int(s)
        assert 0 <= k < s, "bad stride %r" % spec_text
        return [r for r in range(mod) if r % s == k]
    if "-" in spec_text:
        a, b = spec_text.split("-")
        a, b = int(a), int(b)
        assert 0 <= a <= b < mod, "bad range %r" % spec_text
        return list(range(a, b + 1))
    out = [int(x) for x in spec_text.split(",") if x.strip()]
    assert all(0 <= r < mod for r in out), "bad list %r" % spec_text
    return out


# ----------------------------------------------------------------- gate ----

def count_only(mod_scan, n, part=None):
    """Emitted-graph count for one genc48 invocation; counts, not graphs."""
    args = mod_scan.gen_args(mod_scan.GENC48, n, extra=["-c", "-f", "-d2"],
                             part=part)
    proc = subprocess.Popen(args, stdout=subprocess.PIPE,
                            stderr=subprocess.DEVNULL, bufsize=1 << 20)
    total = 0
    for _ in proc.stdout:
        total += 1
    assert proc.wait() == 0, "genc48 failed on %r" % (part,)
    return total


def partition_check(mod_scan, n, mod):
    """O012 step 3's obligation: the production modulus must partition the
    class exactly.  Whole run vs the sum of all `mod` parts, same switches."""
    t0 = time.time()
    whole = count_only(mod_scan, n)
    sizes = [count_only(mod_scan, n, "%d/%d" % (r, mod)) for r in range(mod)]
    total = sum(sizes)
    nonempty = [s for s in sizes if s]
    row = {
        "order": n, "modulus": mod, "unsplit": whole, "split_total": total,
        "exact": whole == total,
        "nonempty_parts": len(nonempty), "empty_parts": mod - len(nonempty),
        "max_part": max(sizes), "max_part_share": round(max(sizes) / float(whole), 4),
        "seconds": round(time.time() - t0, 1),
    }
    assert row["exact"], json.dumps(row)
    return row


def cmd_gate():
    say("GATE — this build is a new instrument until every check below passes")
    mod_scan = ladder.load_scan(DATA)
    prov = {
        "architecture": subprocess.run(["uname", "-m"], stdout=subprocess.PIPE,
                                       text=True).stdout.strip(),
        "kernel": subprocess.run(["uname", "-sr"], stdout=subprocess.PIPE,
                                 text=True).stdout.strip(),
        "interpreter": mod_scan.interpreter(),
        "cpu_count": os.cpu_count(),
        "genc48_sha256": sha256(mod_scan.GENC48),
        "geng_reference_sha256": sha256(mod_scan.GENG),
        "scan_py_sha256": sha256(ladder.SCAN_PY),
        "prune_c8_c_sha256": sha256(os.path.join(ladder.E019, "prune_c8.c")),
        "nauty": "2.9.3 (sha256 9fc4edae...1b5b, verified in the image build)",
    }
    say("provenance: %s" % json.dumps(prov, sort_keys=True))

    stages = {}

    t0 = time.time()
    say("stage 1/4 — the 146-check anchor suite")
    mod_scan.cmd_anchors([])
    stages["anchors"] = {"seconds": round(time.time() - t0, 1),
                         "output": "anchors_%s.json" % mod_scan.interpreter_tag()}

    t0 = time.time()
    say("stage 2/4 — cubic order-24 positive control (Markstrom Table 3 = 4)")
    mod_scan.cmd_cubic24([])
    stages["cubic24"] = {"seconds": round(time.time() - t0, 1),
                         "output": "cubic24_check.json"}

    t0 = time.time()
    say("stage 3/4 — set-equality cross-check against the stock geng stream")
    mod_scan.cmd_crosscheck(["mindeg3", "12", "13", "14", "15", "16", "17"])
    stages["crosscheck"] = {"seconds": round(time.time() - t0, 1),
                            "output": "crosscheck_mindeg3.json"}

    t0 = time.time()
    say("stage 4/4 — partition check at the production modulus %d" % MOD)
    stages["partition"] = partition_check(mod_scan, 16, MOD)

    manifest = {"gate": "PASSED", "provenance": prov, "stages": stages,
                "order": ORDER, "modulus": MOD}
    write_json("gate_manifest.json", manifest)
    say("GATE PASSED — %s" % json.dumps(stages, sort_keys=True))
    say("compare anchors_*.json / cubic24_check.json / crosscheck_mindeg3.json "
        "against the recorded E019 files before citing anything")
    return 0


# ------------------------------------------------------------------ run ----

def scan_path(r, order=None, mod=None):
    return os.path.join(DATA, "scan_n%d_part%dof%d.json"
                        % (order or ORDER, r, mod or MOD))


def class_path(r, order=None, mod=None):
    return os.path.join(DATA, "class_n%d_part%dof%d.txt"
                        % (order or ORDER, r, mod or MOD))


def cmd_part(spec_text, order):
    mod_scan = ladder.load_scan(DATA)
    mod_scan.cmd_run([str(order), spec_text, "--verify-all"])
    return 0


def run_parts(order, mod, parts, workers, label=""):
    """Worker pool over `parts`; returns {part: wall_seconds} and failures.
    Parts whose scan JSON already exists are skipped, so a restarted container
    resumes instead of redoing finished work."""
    todo = [r for r in parts if not os.path.exists(scan_path(r, order, mod))]
    say("%sorder %d, modulus %d: %d assigned, %d done, %d to run, %d workers"
        % (label, order, mod, len(parts), len(parts) - len(todo), len(todo),
           workers))
    queue, running, times, failed, done = list(todo), {}, {}, [], 0
    t_start = time.time()
    while queue or running:
        while queue and len(running) < workers:
            r = queue.pop(0)
            running[r] = (subprocess.Popen(
                [sys.executable, os.path.abspath(__file__), "part",
                 "%d/%d" % (r, mod), str(order)], cwd=HERE), time.time())
        finished = [r for r, (p, _) in running.items() if p.poll() is not None]
        if not finished:
            time.sleep(5)
            continue
        for r in finished:
            proc, t0 = running.pop(r)
            times[r] = round(time.time() - t0, 1)
            done += 1
            if proc.returncode != 0:
                failed.append(r)
                say("%spart %d/%d FAILED rc=%d" % (label, r, mod,
                                                   proc.returncode))
            if done % max(1, len(todo) // 20) == 0 or done == len(todo):
                say("%s[%d/%d] last %d/%d in %.1fs, mean %.1fs, elapsed %.1fs"
                    % (label, done, len(todo), r, mod, times[r],
                       sum(times.values()) / float(len(times)),
                       time.time() - t_start))
    return times, failed, round(time.time() - t_start, 1)


def cmd_calib():
    """Measure what wide splitting actually costs, before spending the order-21
    budget on a guess.

    geng assigns whole subtrees at its split level (maxn-4), so every part must
    walk the tree ABOVE that level before it can tell which subtrees are its
    own.  That upper-tree cost is paid once per part, so the total work grows
    with the modulus while the largest part shrinks -- and the right production
    modulus is wherever those two trends cross.

    Order 19 is the calibration order: small enough to sweep several moduli,
    large enough to be representative, and already on record (E022's harvest:
    74,589 {C4,C8}-free graphs, 11,226.8 cpu-seconds over 16 parts), so each
    sweep is simultaneously an exactness check of the split and a cross-check
    of this build against the recorded rung."""
    order = int(os.environ.get("E024_CALIB_ORDER", "19"))
    mods = [int(m) for m in
            os.environ.get("E024_CALIB_MODS", "16,64,128,512").split(",")]
    expected = os.environ.get("E024_CALIB_EXPECT")
    expected = int(expected) if expected else None
    rows = []
    for mod in mods:
        times, failed, wall = run_parts(order, mod, list(range(mod)), WORKERS,
                                        label="mod%d " % mod)
        assert not failed, "calibration parts failed: %s" % failed
        generated = 0
        cpu = 0.0
        for r in range(mod):
            with open(scan_path(r, order, mod)) as fh:
                tally = json.load(fh)
            generated += tally["generated_c4c8_free"]
            cpu += tally["seconds"]
        row = {"order": order, "modulus": mod, "generated": generated,
               "cpu_seconds": round(cpu, 1), "wall_seconds": wall,
               "max_part_seconds": max(times.values()) if times else 0.0,
               "mean_part_seconds": round(cpu / mod, 1),
               "workers": WORKERS}
        if expected is not None:
            row["matches_recorded_class_size"] = (generated == expected)
            assert row["matches_recorded_class_size"], (
                "modulus %d produced %d graphs, recorded is %d"
                % (mod, generated, expected))
        rows.append(row)
        say("CALIB %s" % json.dumps(row, sort_keys=True))
    base = rows[0]["cpu_seconds"]
    for row in rows:
        row["overhead_vs_mod%d" % rows[0]["modulus"]] = round(
            row["cpu_seconds"] / base, 3)
    write_json("calib_n%d.json" % order, {"rows": rows})
    say("CALIBRATION COMPLETE")
    for row in rows:
        say("  mod %4d: cpu %8.1fs (x%.2f)  max part %7.1fs  wall %7.1fs"
            % (row["modulus"], row["cpu_seconds"],
               row["overhead_vs_mod%d" % rows[0]["modulus"]],
               row["max_part_seconds"], row["wall_seconds"]))
    return 0


def extract_profile(parts):
    """Pull the degree-profile members (exactly two degree-2 vertices) out of
    the class files.  scan.py already writes n_degree_2 as column 3; this only
    selects, and every selection is asserted against that part's scan JSON."""
    rows = []
    missing_class = []
    for r in sorted(parts):
        with open(scan_path(r)) as fh:
            tally = json.load(fh)
        if not os.path.exists(class_path(r)):
            # scan.py only writes the class file when the part stayed under
            # its SAVE_LIMIT; record the gap rather than paper over it.
            missing_class.append({"part": r,
                                  "generated": tally["generated_c4c8_free"],
                                  "profile": tally["profile"]})
            continue
        found = 0
        with open(class_path(r)) as fh:
            for line in fh:
                if line.startswith("#"):
                    continue
                fields = line.split()
                if len(fields) == 4 and fields[2] == "2":
                    rows.append("%s %s %s %s %d" % (fields[0], fields[1],
                                                    fields[2], fields[3], r))
                    found += 1
        assert found == tally["profile"], (
            "part %d: class file has %d profile members, scan JSON says %d"
            % (r, found, tally["profile"]))
    path = os.path.join(DATA, "profile_n%d_mod%d.txt" % (ORDER, MOD))
    with open(path, "w") as fh:
        fh.write("# graph6 edges n_degree2 power_free part"
                 "   (degree-profile members, order %d, mod %d)\n"
                 % (ORDER, MOD))
        for row in rows:
            fh.write(row + "\n")
    return path, len(rows), missing_class


def cmd_run(parts):
    os.makedirs(DATA, exist_ok=True)
    times, failed, wall = run_parts(ORDER, MOD, parts, WORKERS)
    t_start = time.time() - wall

    if failed:
        write_json("run_manifest_%s.json" % os.environ.get("E024_TAG", "x"),
                   {"status": "FAILED", "failed_parts": failed,
                    "seconds": times})
        say("FAILED parts: %s" % failed)
        return 1

    path, n_profile, missing = extract_profile(parts)
    outputs = {}
    for r in sorted(parts):
        outputs["scan_n%d_part%dof%d.json" % (ORDER, r, MOD)] = \
            sha256(scan_path(r))
        if os.path.exists(class_path(r)):
            outputs["class_n%d_part%dof%d.txt" % (ORDER, r, MOD)] = \
                sha256(class_path(r))
    manifest = {
        "status": "COMPLETE", "order": ORDER, "modulus": MOD,
        "parts": sorted(parts), "part_seconds": times,
        "wall_seconds": round(time.time() - t_start, 1),
        "cpu_seconds_sum": round(sum(times.values()), 1),
        "profile_members_extracted": n_profile,
        "profile_file": os.path.basename(path),
        "parts_without_class_file": missing,
        "workers": WORKERS,
        "sha256": outputs,
    }
    write_json("run_manifest_%s.json" % os.environ.get("E024_TAG", "x"),
               manifest)
    say("COMPLETE — %d parts, %.1fs wall, %.1f core-seconds, "
        "%d profile members extracted, %d parts missing a class file"
        % (len(parts), manifest["wall_seconds"], manifest["cpu_seconds_sum"],
           n_profile, len(missing)))
    say("E024-CLOUD-COMPLETE")
    return 0


def main():
    mode = os.environ.get("E024_MODE", "gate")
    if len(sys.argv) > 1 and sys.argv[1] == "part":
        order = int(sys.argv[3]) if len(sys.argv) > 3 else ORDER
        return cmd_part(sys.argv[2], order)
    if mode == "gate":
        rc = cmd_gate()
    elif mode == "calib":
        rc = cmd_calib()
    elif mode == "run":
        rc = cmd_run(parse_parts(os.environ.get("E024_PARTS", ""), MOD))
    else:
        say("unknown E024_MODE %r" % mode)
        return 2
    if HOLD:
        say("holding the container so the volume stays reachable; "
            "stop the service when the results are downloaded")
        while True:
            time.sleep(600)
            say("idle heartbeat (rc=%d)" % rc)
    return rc


if __name__ == "__main__":
    sys.exit(main())
