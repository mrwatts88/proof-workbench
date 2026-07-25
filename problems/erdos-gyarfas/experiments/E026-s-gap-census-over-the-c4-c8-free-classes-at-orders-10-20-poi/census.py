#!/usr/bin/env python3
"""E026 -- the S-gap census at the window bottom (P-002, session S025; A025 T5).

(F-S) (A025 T4) claims: in the window [18,35], every vertex-taut
(5b)-profile pair (H,a,b) with 4,8 not in Spec(H) has S cap {6,14}
nonempty.  This census runs its first kill test over every
{C4,C8}-free class member on disk at orders 10-20:

  orders 10-16   E019/data/class_n{10..16}.txt          (complete classes)
  order  17      E019/data/class_n17_part{0..15}of16.txt (complete)
  orders 18-19   E022/data/class_n1[89]_part{0..15}of16.txt (complete)
  order  20      E022/data/class_n20_part{r}of16.txt for the 11 parts
                 r in {0,1,2,4,5,8,9,10,11,12,15} that scan.py's
                 SAVE_LIMIT left complete on disk -- 572,519 of the
                 2,569,481-graph class (the "572,530 saved" in the S022
                 record counted the 11 header lines).  Parts 3/6/7/13/14 saved no
                 class file (each exceeded SAVE_LIMIT); their members
                 are NOT censused, except that the four recorded
                 part-14 profile members (profile_n20_part14.g6) are
                 censused as a separately labelled supplementary
                 stratum.  Order-20 tallies are therefore a
                 per-part-complete SAMPLE, never a class total.

Per member H and per unordered pair {a,b} of its degree-2 vertices:

  bit2  = 2 in S(H,a,b)    (common neighbour -- exact, trivial)
  bit6  = 6 in S(H,a,b)    (exact-length simple-path existence DFS)
  bit14 = 14 in S(H,a,b)   (same; trivially False when 14 > n-1)

A pair is GAPPED when bit6 = bit14 = False -- the P-2 dodge at these
orders (2 is tallied separately: the closure identity puts 2 in S out
of play only for adjacency reasons, and the recorded frontier objects
dodge it; 30 > n-1 cannot occur below order 31).  Every gapped pair
gets the full treatment: paths_with_essential (E018/mod4, the anchored
full enumerator) recomputes S exactly and its 6/14 verdicts are
asserted against the bits; tautness = essential mask covers V(H); C16
presence via has_cycle_len (+ count_cycles_len when present) and an
assertion against the class line's power_free flag (at n >= 16 that
flag is exactly C16-freeness, C4/C8 being absent by construction).
Members with exactly two degree-2 vertices always get the full
treatment -- they are the (F-S) hypothesis stratum.

  * a vertex-taut GAPPED pair on an exactly-two member KILLS (F-S) as
    stated (pre-registered outcome (ii), A025 T5) -- flagged loudly;
  * a vertex-taut gapped pair on any other member is the nearest
    in-window realization of the dodge and is recorded in full;
  * the gap6/gap14/gap-both tallies per order are the gap-vs-order
    curve of outcome (i).

Every STRIDE-th pair (deterministic, no randomness) and the first five
pairs of every part are additionally recomputed by
paths_with_essential and the three bits asserted -- a continuous
cross-algorithm check through production; the sampled pairs' tautness
is tallied as a by-product.  Every 500th member at n >= 16 has its
power_free class-line flag re-verified by has_cycle_len.

New code here: the exact-length existence DFS (iterative, over simple
paths, admissible pruning by full-graph BFS distance from b -- a
partial path of length k at v cannot finish in exactly L edges if
k + dist(v,b) > L; bipartite members get the parity shortcut, every
a-b path length there being congruent to d(a,b) mod 2) and the
tallying.  Everything else is imported: E019/scan.py by E022's
load_scan pattern (DATA rebound here, E019 read-only, generator paths
untouched and never invoked) and E021/dissect.py -> E018/mod4.py by
E025's pattern.  No generator runs; the census only reads recorded
class files.  Deterministic; stdlib only; wall clock in timing fields
only.

Commands (production pypy3; anchors under BOTH interpreters first):
  census.py anchors            # E021's 45-check suite + the new checks
  census.py census-small       # orders 10-17 in one process
  census.py census N R         # one part: N in 18/19/20, R the part no.
  census.py supp14             # the four recorded part-14 profile members
  census.py harvest            # merge, assert identities, verdict block
"""

import json
import os
import sys
import time

sys.dont_write_bytecode = True          # never write into imported trees
import importlib.util                   # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
EXPS = os.path.dirname(HERE)
E019_DIR = os.path.join(
    EXPS, "E019-dedicated-c4-c8-free-generator-geng-prune-plugin-and-the-ord")
E021_DIR = os.path.join(
    EXPS, "E021-blocking-cycle-interference-dissection-exemplar-extraction-a")
E022_DIR = os.path.join(
    EXPS, "E022-the-g-profile-ladder-at-orders-18-and-19-via-the-e019-genera")
E019_DATA = os.path.join(E019_DIR, "data")
E022_DATA = os.path.join(E022_DIR, "data")


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def _load_e019_scan():
    """E022's load_scan pattern: import E019/scan.py read-only, rebind DATA."""
    before = sorted(os.listdir(E019_DATA))
    mod = _load("e019_scan", os.path.join(E019_DIR, "scan.py"))
    after = sorted(os.listdir(E019_DATA))
    assert before == after, "importing E019/scan.py changed E019/data"
    assert mod.DATA == E019_DATA, "unexpected DATA in E019 scan.py"
    mod.DATA = DATA
    os.makedirs(DATA, exist_ok=True)
    return mod


scan = _load_e019_scan()
e021 = _load("e021_dissect", os.path.join(E021_DIR, "dissect.py"))
e021.DATA = DATA
e021.scan.DATA = DATA
import pathlib                           # noqa: E402
e021.cat.DATA = pathlib.Path(DATA)
paths_with_essential = e021.mod4.paths_with_essential

g6_decode = scan.g6_decode
degrees = scan.degrees
bipartition = scan.bipartition
bfs_dist = scan.bfs_dist
has_cycle_len = scan.has_cycle_len
count_cycles_len = scan.count_cycles_len
path_lengths = scan.path_lengths

STRIDE = 4999                 # deterministic cross-check stride over pairs
MEMBER_STRIDE = 500           # power_free-flag re-verification stride
POISONS = (2, 6, 14)

N19_G6 = "R???C@?GC_B?@_aAA_aP?W_?BO@Gc?"
N14_G6 = "M?AA@?WcKWHOWOL??"

EXPECTED_CLASS = {10: 14, 11: 0, 12: 94, 13: 10, 14: 778, 15: 168,
                  16: 7615, 17: 2580, 18: 108447, 19: 74589, 20: 572519}
# 572,519 graphs: the S022 record's "572,530 saved" was a line count that
# included the 11 class-file header lines; the scan_n20 part tallies (the
# authoritative figures) sum to 572,519 over the on-disk parts -- asserted
# in anchor c15c.
N20_PARTS_ON_DISK = (0, 1, 2, 4, 5, 8, 9, 10, 11, 12, 15)
N20_PARTS_MISSING = (3, 6, 7, 13, 14)
N20_CLASS_TOTAL = 2569481     # recorded full class size (scan_n20_harvest)


# ----------------------------------------------------------------------
# the one new primitive


def has_path_len(adjacency, a, b, L, dist_b, bip_parity):
    """Is there a simple a-b path with exactly L edges?

    dist_b = bfs_dist(adjacency, b, full) in the FULL graph (admissible:
    distances in any subgraph are >= full-graph distances, so pruning on
    them never removes a completion).  bip_parity is None for
    non-bipartite graphs, else all a-b path lengths are == dist_b[a]
    mod 2 and off-parity L is refused outright.
    """
    n = len(adjacency)
    if L < 1 or L > n - 1 or dist_b[a] > L:
        return False
    if bip_parity is not None and (L - dist_b[a]) % 2:
        return False
    target = 1 << b
    stack = [(a, 1 << a, L)]            # (vertex, used-mask, edges remaining)
    while stack:
        v, used, rem = stack.pop()
        row = adjacency[v] & ~used
        if rem == 1:
            if row & target:
                return True
            continue
        row &= ~target                   # b may only be the final step
        while row:
            low = row & -row
            w = low.bit_length() - 1
            row ^= low
            if dist_b[w] < rem:          # need exactly rem-1 more edges
                stack.append((w, used | low, rem - 1))
    return False


# ----------------------------------------------------------------------
# per-member census


def blank_tally():
    return {
        "members": 0, "members_lt2": 0, "exactly_two_members": 0,
        "pairs": 0, "bit2": 0, "bit6": 0, "bit14": 0,
        "gap6": 0, "gap14": 0, "gap_both": 0,
        "gap_both_taut": 0, "members_with_gap": 0,
        "stride_checks": 0, "stride_taut": 0,
        "flag_rechecks": 0, "bipartite_members": 0,
    }


def full_pair_record(adjacency, g6, n, a, b, ndeg2, pf, bits):
    """The anchored full enumerator on one pair; asserts the bits."""
    s, essential = paths_with_essential(adjacency, a, b)
    assert (2 in s) == bits[0] and (6 in s) == bits[1] and (14 in s) == bits[2], \
        "bit search disagrees with paths_with_essential on %s (%d,%d)" % (g6, a, b)
    taut = essential == (1 << n) - 1
    c16 = has_cycle_len(adjacency, 16)
    if n >= 16:
        assert pf == (not c16), "power_free flag wrong on %s" % g6
    return {
        "g6": g6, "order": n, "terminals": [a, b], "n_degree2": ndeg2,
        "S": sorted(s), "vertex_taut": taut,
        "bit2": bits[0], "bit6": bits[1], "bit14": bits[2],
        "gapped": not (bits[1] or bits[2]),
        "c16_present": c16,
        "c16_count": count_cycles_len(adjacency, 16) if c16 else 0,
        "power_free_flag": pf,
    }


def census_member(line, order, tally, gapped_rows, two_rows, counter):
    parts = line.split()
    assert len(parts) == 4, "bad class line: %r" % line
    g6, edges_s, ndeg2_s, pf_s = parts
    adjacency = g6_decode(g6)
    n = len(adjacency)
    assert n == order
    deg = degrees(adjacency)
    ndeg2 = int(ndeg2_s)
    d2 = [v for v in range(n) if deg[v] == 2]
    assert len(d2) == ndeg2, "degree-2 count mismatch on %s" % g6
    assert min(deg) >= 2
    assert sum(deg) == 2 * int(edges_s)
    pf = pf_s == "1"
    if n < 16:
        assert pf, "power_free flag must be 1 below order 16: %s" % g6
    tally["members"] += 1
    if tally["members"] % MEMBER_STRIDE == 0 and n >= 16:
        assert pf == (not has_cycle_len(adjacency, 16)), \
            "power_free flag wrong on %s" % g6
        tally["flag_rechecks"] += 1
    if ndeg2 < 2:
        tally["members_lt2"] += 1
        return
    exactly_two = ndeg2 == 2
    if exactly_two:
        tally["exactly_two_members"] += 1
    bip = bipartition(adjacency)
    parity = 0 if bip is not None else None
    if bip is not None:
        tally["bipartite_members"] += 1
    dists = {b: bfs_dist(adjacency, b, (1 << n) - 1) for b in d2}
    member_gap = False
    for i in range(len(d2)):
        a = d2[i]
        for j in range(i + 1, len(d2)):
            b = d2[j]
            dist_b = dists[b]
            bit2 = bool(adjacency[a] & adjacency[b])
            bit6 = has_path_len(adjacency, a, b, 6, dist_b, parity)
            bit14 = has_path_len(adjacency, a, b, 14, dist_b, parity)
            bits = (bit2, bit6, bit14)
            tally["pairs"] += 1
            counter[0] += 1
            tally["bit2"] += bit2
            tally["bit6"] += bit6
            tally["bit14"] += bit14
            gap_both = not (bit6 or bit14)
            if not bit6:
                tally["gap6"] += 1
            if not bit14:
                tally["gap14"] += 1
            if gap_both:
                tally["gap_both"] += 1
                member_gap = True
            need_full = gap_both or exactly_two
            stride_hit = counter[0] % STRIDE == 0 or tally["pairs"] <= 5
            if need_full or stride_hit:
                row = full_pair_record(adjacency, g6, n, a, b, ndeg2, pf, bits)
                if stride_hit and not need_full:
                    tally["stride_checks"] += 1
                    tally["stride_taut"] += row["vertex_taut"]
                if gap_both:
                    tally["gap_both_taut"] += row["vertex_taut"]
                    # only TAUT gapped rows are stored (the non-taut ones,
                    # ~540k across the run, are tallied but not kept: they
                    # fail the (F-S)-relevance test, and their identities
                    # are reproducible by re-running the part)
                    if row["vertex_taut"]:
                        gapped_rows.append(row)
                        print("!! VERTEX-TAUT GAPPED PAIR order %d %s (%d,%d) "
                              "ndeg2=%d S=%r" % (n, g6, a, b, ndeg2, row["S"]))
                        if exactly_two:
                            print("!!!! (F-S) KILL CANDIDATE (exactly-two "
                                  "member): %s" % g6)
                if exactly_two:
                    two_rows.append(row)
    if member_gap:
        tally["members_with_gap"] += 1


def census_lines(lines, order, label):
    t0 = time.time()
    tally = blank_tally()
    gapped_rows, two_rows = [], []
    counter = [0]
    for line in lines:
        if not line or line.startswith("#"):
            continue
        census_member(line, order, tally, gapped_rows, two_rows, counter)
    out = {
        "label": label, "order": order, "tally": tally,
        "taut_gapped_pairs": gapped_rows, "exactly_two_members": two_rows,
        "stride": STRIDE, "member_stride": MEMBER_STRIDE,
        "seconds": round(time.time() - t0, 2),
        "interpreter": scan.interpreter(),
    }
    path = os.path.join(DATA, "census_%s.json" % label)
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1)
    print("census %s: members=%d pairs=%d gap6=%d gap14=%d gap_both=%d "
          "taut-gapped=%d exactly2=%d  %.1fs" %
          (label, tally["members"], tally["pairs"], tally["gap6"],
           tally["gap14"], tally["gap_both"], tally["gap_both_taut"],
           tally["exactly_two_members"], out["seconds"]))
    return out


def class_files(order, part=None):
    if 10 <= order <= 16:
        return [os.path.join(E019_DATA, "class_n%d.txt" % order)]
    if order == 17:
        root = E019_DATA
    else:
        root = E022_DATA
    if part is None:
        parts = range(16) if order != 20 else N20_PARTS_ON_DISK
        return [os.path.join(root, "class_n%d_part%dof16.txt" % (order, r))
                for r in parts]
    if order == 20:
        assert part in N20_PARTS_ON_DISK, \
            "order-20 part %d has no class file (SAVE_LIMIT)" % part
    return [os.path.join(root, "class_n%d_part%dof16.txt" % (order, part))]


def read_lines(path):
    with open(path) as fh:
        return fh.read().splitlines()


# ----------------------------------------------------------------------
# commands


def cmd_census_small(_args):
    for order in range(10, 18):
        lines = []
        for path in class_files(order):
            lines.extend(read_lines(path))
        census_lines(lines, order, "n%d" % order)


def cmd_census(args):
    order, part = int(args[0]), int(args[1])
    assert order in (18, 19, 20)
    [path] = class_files(order, part)
    census_lines(read_lines(path), order, "n%d_part%dof16" % (order, part))


def cmd_supp14(_args):
    lines = []
    for g6 in read_lines(os.path.join(E022_DATA, "profile_n20_part14.g6")):
        if not g6:
            continue
        adjacency = g6_decode(g6)
        edges = sum(degrees(adjacency)) // 2
        ndeg2 = sum(1 for d in degrees(adjacency) if d == 2)
        pf = "1" if not has_cycle_len(adjacency, 16) else "0"
        lines.append("%s %d %d %s" % (g6, edges, ndeg2, pf))
    census_lines(lines, 20, "n20supp14")


def cmd_harvest(_args):
    per_order, kill_rows = {}, []
    labels = (["n%d" % n for n in range(10, 18)]
              + ["n18_part%dof16" % r for r in range(16)]
              + ["n19_part%dof16" % r for r in range(16)]
              + ["n20_part%dof16" % r for r in N20_PARTS_ON_DISK])
    for label in labels:
        with open(os.path.join(DATA, "census_%s.json" % label)) as fh:
            out = json.load(fh)
        order = out["order"]
        agg = per_order.setdefault(order, blank_tally())
        for key in agg:
            agg[key] += out["tally"][key]
        for row in out["taut_gapped_pairs"]:
            assert row["vertex_taut"] and row["gapped"]
            kill_rows.append(row)
    for order, agg in sorted(per_order.items()):
        assert agg["members"] == EXPECTED_CLASS[order], \
            "order %d: censused %d members, expected %d" % (
                order, agg["members"], EXPECTED_CLASS[order])
    with open(os.path.join(DATA, "census_n20supp14.json")) as fh:
        supp = json.load(fh)
    assert supp["tally"]["members"] == 4
    # exactly-two identities against the recorded profile objects
    n19 = per_order[19]
    assert n19["exactly_two_members"] == 1
    n20 = per_order[20]
    assert n20["exactly_two_members"] == 3
    assert supp["tally"]["exactly_two_members"] == 4
    summary = {
        "per_order": {str(k): v for k, v in sorted(per_order.items())},
        "n20_coverage_note":
            "order-20 rows cover the 11 SAVE_LIMIT-complete parts "
            "%r = 572,519 of the %d-graph class; parts %r are not "
            "censused (no class file); the four recorded part-14 "
            "profile members are the separate supp14 stratum"
            % (list(N20_PARTS_ON_DISK), N20_CLASS_TOTAL,
               list(N20_PARTS_MISSING)),
        "supp14": supp["tally"],
        "supp14_rows": supp["exactly_two_members"],
        "gapped_pairs_total": sum(a["gap_both"] for a in per_order.values()),
        "taut_gapped_pairs": kill_rows,
        "fs_kill_candidates": [r for r in kill_rows if r["n_degree2"] == 2],
        "interpreter": scan.interpreter(),
    }
    path = os.path.join(DATA, "census_summary.json")
    with open(path, "w") as fh:
        json.dump(summary, fh, indent=1)
    print("\n order | members | pairs | gap6 | gap14 | gap-both | taut-gapped | exactly-two")
    for order, agg in sorted(per_order.items()):
        print(" %5d | %7d | %9d | %6d | %6d | %5d | %3d | %d" %
              (order, agg["members"], agg["pairs"], agg["gap6"],
               agg["gap14"], agg["gap_both"], agg["gap_both_taut"],
               agg["exactly_two_members"]))
    print(" supp14 (order-20 part-14 profile members): members=4 pairs=%d "
          "gap_both=%d" % (supp["tally"]["pairs"], supp["tally"]["gap_both"]))
    print("\nVERDICT: taut gapped pairs = %d; (F-S) kill candidates "
          "(exactly-two) = %d" % (len(kill_rows), len(summary["fs_kill_candidates"])))
    return summary


# ----------------------------------------------------------------------
# anchors


def petersen_minus_e():
    edges = [(i, (i + 1) % 5) for i in range(5)]
    edges += [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
    edges += [(i, i + 5) for i in range(5)]
    edges.remove((0, 5))
    return scan.from_edges(10, edges)


def _pair_bits(adjacency, a, b):
    n = len(adjacency)
    dist_b = bfs_dist(adjacency, b, (1 << n) - 1)
    parity = 0 if bipartition(adjacency) is not None else None
    return (bool(adjacency[a] & adjacency[b]),
            has_path_len(adjacency, a, b, 6, dist_b, parity),
            has_path_len(adjacency, a, b, 14, dist_b, parity))


def _deg2(adjacency):
    return [v for v, d in enumerate(degrees(adjacency)) if d == 2]


def cmd_anchors(_args):
    print("== E021 45-check suite (through the import) ==")
    e021.cmd_anchors(None)
    print("== E026 census anchors ==")
    checks = []

    def ok(cond, label):
        checks.append((bool(cond), label))
        print("  %s %s" % ("ok " if cond else "FAIL", label))
        assert cond, label

    # c1: Petersen-e -- the order-10 calibration object.
    p10 = petersen_minus_e()
    a, b = _deg2(p10)
    s, essential = paths_with_essential(p10, a, b)
    ok(s == {4, 5, 7, 8}, "c1 P10 S = {4,5,7,8}")
    ok(essential == (1 << 10) - 1, "c2 P10 vertex-taut")
    bits = _pair_bits(p10, a, b)
    ok(bits == (False, False, False), "c3 P10 bits (no 2, no 6, no 14): GAPPED")
    # c4: the order-14 calibration exemplar.
    n14 = g6_decode(N14_G6)
    a, b = _deg2(n14)
    s, essential = paths_with_essential(n14, a, b)
    ok(s == set(range(3, 14)) - {6}, "c4 N14 S = [3,13] minus {6}")
    ok(essential == (1 << 14) - 1, "c5 N14 vertex-taut")
    ok(_pair_bits(n14, a, b) == (False, False, False), "c6 N14 GAPPED")
    # c7: the order-19 profile member (recorded in exemplars_n19.json).
    n19 = g6_decode(N19_G6)
    a, b = _deg2(n19)
    s, essential = paths_with_essential(n19, a, b)
    ok(s == set(range(5, 19)), "c7 N19 S = [5,18]")
    ok(essential == (1 << 19) - 1, "c8 N19 vertex-taut")
    ok(_pair_bits(n19, a, b) == (False, True, True), "c9 N19 bits: NOT gapped")
    # c10/c11: the seven recorded order-20 profile members.
    for fname, key in (("t5_n20_profile.json", "c10"),
                       ("collect_n20_part14.json", "c11")):
        with open(os.path.join(E022_DATA, fname)) as fh:
            rec = json.load(fh)
        for g in rec["graphs"]:
            adj = g6_decode(g["g6"])
            ta, tb = g["terminals"]
            s, essential = paths_with_essential(adj, ta, tb)
            ok(sorted(s) == g["S"], "%s %s S matches record" % (key, g["g6"]))
            ok((essential == (1 << 20) - 1) == g["vertex_taut"],
               "%s %s tautness matches record" % (key, g["g6"]))
            ok(count_cycles_len(adj, 16) == g["c16_count"],
               "%s %s C16 count matches record" % (key, g["g6"]))
            ok(_pair_bits(adj, ta, tb)[1:] == (True, True),
               "%s %s bits 6,14 present" % (key, g["g6"]))
    # c12: deterministic small controls for the exact-length DFS.
    path15 = scan.from_edges(15, [(i, i + 1) for i in range(14)])
    d = bfs_dist(path15, 14, (1 << 15) - 1)
    ok(has_path_len(path15, 0, 14, 14, d, 0) and
       not has_path_len(path15, 0, 14, 6, d, 0),
       "c12 P15 endpoints: length 14 yes, 6 no")
    c16g = scan.cycle_graph(16)
    d = bfs_dist(c16g, 2, (1 << 16) - 1)
    ok(has_path_len(c16g, 0, 2, 2, d, 0) and has_path_len(c16g, 0, 2, 14, d, 0)
       and not has_path_len(c16g, 0, 2, 6, d, None),
       "c13 C16 dist-2 pair: lengths {2,14} only")
    # c14: cross-algorithm sweep -- three independent enumerators agree.
    #   my bits vs E019 path_lengths vs E018 paths_with_essential, on every
    #   degree-2 pair of the full order-12/14/15 classes and the first 400
    #   order-16 members.
    swept = agreed = 0
    for order, limit in ((12, None), (14, None), (15, None), (16, 400)):
        [pth] = class_files(order)
        lines = [ln for ln in read_lines(pth) if ln and not ln.startswith("#")]
        if limit:
            lines = lines[:limit]
        for line in lines:
            g6 = line.split()[0]
            adj = g6_decode(g6)
            d2 = _deg2(adj)
            for i in range(len(d2)):
                for j in range(i + 1, len(d2)):
                    va, vb = d2[i], d2[j]
                    s1 = path_lengths(adj, va, vb)
                    s2, _ = paths_with_essential(adj, va, vb)
                    bits = _pair_bits(adj, va, vb)
                    match = (s1 == s2 and
                             bits == ((2 in s1), (6 in s1), (14 in s1)))
                    swept += 1
                    agreed += match
                    assert match, "cross-algorithm mismatch %s (%d,%d)" % (
                        g6, va, vb)
    ok(swept == agreed and swept > 3000,
       "c14 cross-algorithm sweep: %d pairs, all three agree" % swept)
    # c15: class-file inventory matches the recorded totals.
    for order in range(10, 21):
        total = 0
        for pth in class_files(order):
            total += sum(1 for ln in read_lines(pth)
                         if ln and not ln.startswith("#"))
        ok(total == EXPECTED_CLASS[order],
           "c15 order %d class file total = %d" % (order, EXPECTED_CLASS[order]))
    ok(sorted(N20_PARTS_ON_DISK + N20_PARTS_MISSING) == list(range(16)),
       "c15b order-20 part accounting")
    # c15c: class-file totals at 18-20 equal the authoritative scan-JSON
    # part tallies (and the full order-20 class is 2,569,481).
    for order, parts, expect in ((18, range(16), 108447),
                                 (19, range(16), 74589),
                                 (20, N20_PARTS_ON_DISK, 572519)):
        tot = 0
        for r in parts:
            with open(os.path.join(
                    E022_DATA, "scan_n%d_part%dof16.json" % (order, r))) as fh:
                tot += json.load(fh)["generated_c4c8_free"]
        ok(tot == expect == EXPECTED_CLASS[order],
           "c15c order %d scan tallies sum to %d" % (order, expect))
    tot = 0
    for r in range(16):
        with open(os.path.join(
                E022_DATA, "scan_n20_part%dof16.json" % r)) as fh:
            tot += json.load(fh)["generated_c4c8_free"]
    ok(tot == N20_CLASS_TOTAL,
       "c15d full order-20 class tally = %d" % N20_CLASS_TOTAL)
    # c16: the supp14 file holds exactly the four recorded g6 strings.
    supp = [ln for ln in read_lines(
        os.path.join(E022_DATA, "profile_n20_part14.g6")) if ln]
    with open(os.path.join(E022_DATA, "collect_n20_part14.json")) as fh:
        rec = json.load(fh)
    ok(supp == [g["g6"] for g in rec["graphs"]],
       "c16 supp14 identities match collect_n20_part14.json")
    out = {"checks": len(checks), "passed": sum(c for c, _ in checks),
           "labels": [lb for _, lb in checks],
           "interpreter": scan.interpreter()}
    with open(os.path.join(
            DATA, "anchors_census_%s.json" % scan.interpreter_tag()), "w") as fh:
        json.dump(out, fh, indent=1)
    print("E026 anchors: %d/%d passed (%s)"
          % (out["passed"], out["checks"], out["interpreter"]))


def cmd_analyze(_args):
    """Secondary cuts over the harvested gapped rows (reads census_summary)."""
    with open(os.path.join(DATA, "census_summary.json")) as fh:
        summary = json.load(fh)
    per = {}
    notable = []
    for row in summary["taut_gapped_pairs"]:
        n = row["order"]
        agg = per.setdefault(n, {
            "taut_gapped": 0, "ndeg2_hist": {}, "min_ndeg2": 99,
            "full_dodge": 0, "full_dodge_min_ndeg2": 99,
            "on_power_free_member": 0, "two_connected": 0,
            "distinct_members": set(),
        })
        agg["taut_gapped"] += 1
        k = row["n_degree2"]
        agg["ndeg2_hist"][k] = agg["ndeg2_hist"].get(k, 0) + 1
        agg["min_ndeg2"] = min(agg["min_ndeg2"], k)
        agg["distinct_members"].add(row["g6"])
        full_dodge = not row["bit2"]
        if full_dodge:
            agg["full_dodge"] += 1
            agg["full_dodge_min_ndeg2"] = min(agg["full_dodge_min_ndeg2"], k)
        adj = g6_decode(row["g6"])
        two_conn = not scan.cut_vertices(adj)
        agg["two_connected"] += two_conn
        if row["power_free_flag"]:
            agg["on_power_free_member"] += 1
            notable.append(dict(row, two_connected=two_conn,
                                full_dodge=full_dodge))
    for agg in per.values():
        agg["distinct_members"] = len(agg["distinct_members"])
        agg["ndeg2_hist"] = {str(k): v
                             for k, v in sorted(agg["ndeg2_hist"].items())}
    out = {"per_order": {str(k): v for k, v in sorted(per.items())},
           "power_free_taut_gapped_rows": notable,
           "note": ("power_free here means the class member itself has no "
                    "C4/C8/C16 (the class-line flag, re-verified on every "
                    "gapped row); such a member with a vertex-taut gapped "
                    "pair is the census's nearest approach to the case-(5b) "
                    "shape, still short of it by its extra degree-2 "
                    "vertices"),
           "interpreter": scan.interpreter()}
    with open(os.path.join(DATA, "analysis.json"), "w") as fh:
        json.dump(out, fh, indent=1)
    print(" order | taut-gapped | members | min ndeg2 | full P-2 dodge "
          "(min ndeg2) | on power-free member | 2-connected")
    for n, agg in sorted(per.items(), key=lambda kv: int(kv[0]) if isinstance(kv[0], str) else kv[0]):
        print(" %5s | %5d | %5d | %2d | %5d (%s) | %4d | %4d" %
              (n, agg["taut_gapped"], agg["distinct_members"],
               agg["min_ndeg2"], agg["full_dodge"],
               agg["full_dodge_min_ndeg2"] if agg["full_dodge"] else "-",
               agg["on_power_free_member"], agg["two_connected"]))
    print("power-free members carrying a taut gapped pair: %d rows" %
          len(notable))


def main():
    cmds = {"anchors": cmd_anchors, "census-small": cmd_census_small,
            "census": cmd_census, "supp14": cmd_supp14,
            "harvest": cmd_harvest, "analyze": cmd_analyze}
    cmds[sys.argv[1]](sys.argv[2:])


if __name__ == "__main__":
    main()
