#!/usr/bin/env python3
"""E025 — trunk-split power-collision realization tables of the ten named
objects (P-002, session S024; the (F) program's opening probe).

Under L049 (T5, the trimming theorem) every cycle of a vertex-taut pair
(H,a,b) is the symmetric difference of two simple a-b paths, and a witnessing
pair can be taken in TRUNK-IDENTICAL ARC FORM: P = Ta A1 Tb, Q = Ta A2 Tb,
where A1, A2 are the two u-v arcs of the cycle and Ta (a..u), Tb (v..b) are
shared trunks meeting the cycle only at u resp. v.  By L048(iii) the
case-(5b) residual object's entire power-freeness is the non-realization of
power lengths by such pairs: Spec(H) = { x + y - 2s : trunk-split pairs },
x = len(P), y = len(Q), s = |Ta| + |Tb| = |E(P) & E(Q)|.

This experiment builds, for each of the ten named objects (the eight
G-profile members at orders 19-20, Petersen-e, and the order-14 full-triple
exemplar), the complete table of realizations of every POWER cycle (their
C8s / C16s):

  * the all-pairs layer: every witnessing pair (P,Q) with E(P) xor E(Q) =
    E(C), recorded as (x, y, s) multiplicities — exactly E021's census
    semantics, re-derived per cycle and asserted equal to E021's
    dissect_pair on every object;
  * the trunk-split layer: the subset of witnessing pairs in trunk-identical
    arc form (P minus Q is a single arc), each recorded with its full shape
    (x, y, s, ax, ay, ta, tb): arc lengths ax + ay = len(C), trunk lengths
    ta + tb = s, x = ta + ax + tb, y = ta + ay + tb — every structural
    invariant asserted per pair.

A pair (P,Q) with symmetric difference a single cycle C is trunk-split iff
E(P) \\ E(Q) is connected (then it is one u-v arc of C, its complement the
other, and the shared part splits into the two end trunks; each direction is
asserted, not assumed).

Membership reading (the point of the probe): each realized length is
classified against the forced-membership classes of the case-(5b) object —
P = {4,8,16,32,64} (powers), P1 = P - 1 (Mersenne), P2 = P - 2 (the
forbidden through-lengths) — and the PRE-REGISTERED per-cycle existential
patterns below are evaluated mechanically.  The pattern list is fixed in
this file before the first table was built:

  has_P    : some trunk-split realization has x or y a power        (2^k in S is forced)
  has_P1   : ... x or y Mersenne                                    (2^k - 1 in S is forced)
  has_PP   : ... x and y BOTH powers        (2^i + 2^j - 2s = 2^k)
  has_P1P1 : ... x and y BOTH Mersenne      (2^i + 2^j - 2 - 2s = 2^k)
  has_forced_pair : ... x and y both in P u P1 (forced classes only)
  has_equal: ... x = y (equal split — invisible to the length SET S)
  has_s0   : ... s = 0 (disjoint pair, the L033 corner)
  has_P2 / all_P2 : x or y in P2 for some / for every realization
                    (data reading only: the calibration objects have
                    S cap P2 empty, so P2 patterns cannot be mechanisms)

A candidate (F) mechanism must be a pattern that holds for EVERY power cycle
of ALL TEN objects — including both calibration objects (A021 discipline:
they realize the forced memberships without being power-free, so whatever
holds on them consumes power-freeness, not the hypotheses).

Commands (run from this directory; production pypy3, cross-check python3):
  pypy3   tables.py anchors     # E021's 45-check suite + 12 new-code anchors
  pypy3   tables.py tables      # build data/realization_tables.json
  pypy3   tables.py patterns    # evaluate the pre-registered patterns
  python3 tables.py tables data/realization_tables_cpython.json   # cross-check

Primitives are IMPORTED from E021/dissect.py (which loads E018 scan.py,
E018 mod4.py, E013 catalogue.py); no census / path / cycle / tautness
primitive is re-implemented.  New code: the trunk-split classifier and the
pattern evaluator.  All data writes land in E025/data.  Deterministic;
stdlib only; wall clock only in timing fields.
"""

import itertools
import importlib.util
import json
import os
import pathlib
import sys
import time

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
EXPS = os.path.dirname(HERE)
E013_DIR = os.path.join(
    EXPS, "E013-full-taut-pinched-catalogue-over-all-terminal-pairs-at-order")
E021_DIR = os.path.join(
    EXPS, "E021-blocking-cycle-interference-dissection-exemplar-extraction-a")
E022_DIR = os.path.join(
    EXPS, "E022-the-g-profile-ladder-at-orders-18-and-19-via-the-e019-genera")


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


e021 = _load("e021_dissect", os.path.join(E021_DIR, "dissect.py"))
e021.DATA = DATA
e021.scan.DATA = DATA
e021.cat.DATA = pathlib.Path(DATA)
scan = e021.scan
cat = e021.cat
mod4 = e021.mod4

P_SET = scan.P_SET            # {4, 8, 16, 32, 64}
P_MINUS_1 = scan.P_MINUS_1    # {3, 7, 15, 31, 63}
P_MINUS_2 = scan.P_MINUS_2    # {2, 6, 14, 30, 62}

N19_G6 = "R???C@?GC_B?@_aAA_aP?W_?BO@Gc?"
N14_G6 = "M?AA@?WcKWHOWOL??"


def length_class(v):
    if v in P_SET:
        return "P"
    if v in P_MINUS_1:
        return "P1"
    if v in P_MINUS_2:
        return "P2"
    return "o"


# --- the trunk-split classifier ----------------------------------------------

def arc_endpoints(edge_set):
    """For a nonempty edge set that is a subset of a single cycle: return the
    pair (endpoints, ok) where ok is True iff the set is a single arc
    (connected).  Every vertex degree is <= 2 automatically; a disjoint union
    of k arcs has exactly 2k degree-1 vertices, so ok iff that count is 2."""
    deg = {}
    for (p, q) in edge_set:
        deg[p] = deg.get(p, 0) + 1
        deg[q] = deg.get(q, 0) + 1
    ends = sorted(v for v, d in deg.items() if d == 1)
    assert all(d <= 2 for d in deg.values()), "not a subgraph of a cycle"
    return ends, len(ends) == 2


def shared_trunks(shared, a, b, u, v):
    """Decompose the shared edge set of a trunk-split pair into the two end
    trunks.  Asserts the L049 arc-form structure: the shared edges form at
    most two path components, one containing a (attached to u or v), one
    containing b; returns (ta, tb) edge counts.  A trivial trunk (a in {u,v})
    contributes 0."""
    if not shared:
        assert a in (u, v) and b in (u, v) and a != b
        return 0, 0
    adj = {}
    for (p, q) in shared:
        adj.setdefault(p, []).append(q)
        adj.setdefault(q, []).append(p)
    assert all(len(nb) <= 2 for nb in adj.values()), "trunk vertex degree > 2"
    seen = set()
    comps = []
    for start in adj:
        if start in seen:
            continue
        comp = {start}
        seen.add(start)
        frontier = [start]
        while frontier:
            w = frontier.pop()
            for nb in adj[w]:
                if nb not in comp:
                    comp.add(nb)
                    seen.add(nb)
                    frontier.append(nb)
        comps.append(comp)
    assert len(comps) <= 2, "shared part has > 2 components"
    ta = tb = 0
    used = 0
    for comp in comps:
        n_edges = sum(1 for (p, q) in shared if p in comp)
        assert n_edges == len(comp) - 1, "trunk component is not a tree/path"
        endpoints = sorted(w for w in comp if len(adj[w]) == 1)
        assert len(endpoints) == 2, "trunk component is not a path"
        if a in comp:
            assert u in comp or v in comp, "a-trunk misses the cycle"
            assert set(endpoints) == {a, u} or set(endpoints) == {a, v}
            ta = n_edges
        elif b in comp:
            assert u in comp or v in comp, "b-trunk misses the cycle"
            assert set(endpoints) == {b, u} or set(endpoints) == {b, v}
            tb = n_edges
        else:
            raise AssertionError("shared component contains neither terminal")
        used += 1
    assert used == len(comps)
    if ta == 0:
        assert a in (u, v), "empty a-trunk but a not on the cycle split"
    if tb == 0:
        assert b in (u, v), "empty b-trunk but b not on the cycle split"
    return ta, tb


def realization_tables(adjacency, a, b, power_lengths):
    """All-pairs and trunk-split realization tables of every power cycle of
    (H,a,b).  Returns (per_cycle list, n_paths, S sorted, spectrum sorted,
    essential_mask)."""
    paths = cat.all_ab_paths(adjacency, a, b)
    lengths_m4, essential = mod4.paths_with_essential(adjacency, a, b)
    assert {l for (l, _, _) in paths} == lengths_m4, "path instruments disagree"
    cycles = cat.all_cycles(adjacency)
    spectrum = sorted({l for (l, _, _) in cycles})
    power_cycles = [(l, m, e) for (l, m, e) in cycles if l in power_lengths]
    index = {}
    for i, (l, m, e) in enumerate(power_cycles):
        assert e not in index, "duplicate cycle edge set"
        index[e] = i
    per = [{
        "length": l,
        "vertices": [w for w in range(len(adjacency)) if m >> w & 1],
        "stratum": ("both" if (m >> a & 1) and (m >> b & 1)
                    else "one" if (m >> a & 1) or (m >> b & 1) else "neither"),
        "n_pairs": 0,
        "combos_all": {},
        "n_trunk_split": 0,
        "ts": {},
        "uv_pairs": set(),
    } for (l, m, e) in power_cycles]
    for (l1, m1, e1), (l2, m2, e2) in itertools.combinations(paths, 2):
        sym = e1 ^ e2
        i = index.get(sym)
        if i is None:
            continue
        rec = per[i]
        length = rec["length"]
        shared = e1 & e2
        s = len(shared)
        x, y = min(l1, l2), max(l1, l2)
        assert x + y - 2 * s == length, "A021 T1 identity fails at t=1"
        key = "%d+%d-2*%d" % (x, y, s)
        rec["n_pairs"] += 1
        rec["combos_all"][key] = rec["combos_all"].get(key, 0) + 1
        diff1 = e1 - e2
        diff2 = e2 - e1
        assert diff1 and diff2, "path pair with containment"
        ends1, ok1 = arc_endpoints(diff1)
        ends2, ok2 = arc_endpoints(diff2)
        assert ok1 == ok2, "one-sided arc connectivity"
        if not ok1:
            continue
        assert ends1 == ends2, "arc endpoint mismatch"
        u, v = ends1
        ta, tb = shared_trunks(shared, a, b, u, v)
        assert ta + tb == s, "trunk split does not account for shared edges"
        ax, ay = len(diff1), len(diff2)
        assert ax + ay == length, "arcs do not partition the cycle"
        assert l1 == ta + ax + tb and l2 == ta + ay + tb, "length identity"
        if (l1, ax) > (l2, ay):
            ax, ay = ay, ax
        tkey = "%d,%d,%d|%d,%d|%d,%d" % (x, y, s, ax, ay, ta, tb)
        rec["n_trunk_split"] += 1
        rec["ts"][tkey] = rec["ts"].get(tkey, 0) + 1
        rec["uv_pairs"].add((u, v))
    for rec in per:
        rec["n_distinct_uv"] = len(rec.pop("uv_pairs"))
        assert rec["n_pairs"] > 0, "SOUNDNESS ALARM: power cycle with no " \
            "witnessing pair (contradicts L049)"
        assert rec["n_trunk_split"] > 0, "SOUNDNESS ALARM: power cycle " \
            "with no trunk-split realization (contradicts L049 arc form)"
        xy = []
        for tkey, count in rec["ts"].items():
            xys = tkey.split("|")[0].split(",")
            x, y, s = int(xys[0]), int(xys[1]), int(xys[2])
            xy.append((x, y, s, count))
        rec["ts_class_pairs"] = sorted({
            "%s,%s" % (length_class(x), length_class(y))
            for (x, y, s, c) in xy})
        rec["flags"] = {
            "has_P": any(length_class(x) == "P" or length_class(y) == "P"
                         for (x, y, s, c) in xy),
            "has_P1": any(length_class(x) == "P1" or length_class(y) == "P1"
                          for (x, y, s, c) in xy),
            "has_PP": any(length_class(x) == "P" and length_class(y) == "P"
                          for (x, y, s, c) in xy),
            "has_P1P1": any(length_class(x) == "P1"
                            and length_class(y) == "P1"
                            for (x, y, s, c) in xy),
            "has_forced_pair": any(
                length_class(x) in ("P", "P1")
                and length_class(y) in ("P", "P1")
                for (x, y, s, c) in xy),
            "has_equal": any(x == y for (x, y, s, c) in xy),
            "has_s0": any(s == 0 for (x, y, s, c) in xy),
            "has_P2": any(length_class(x) == "P2" or length_class(y) == "P2"
                          for (x, y, s, c) in xy),
            "all_P2": all(length_class(x) == "P2" or length_class(y) == "P2"
                          for (x, y, s, c) in xy),
        }
        rec["ts_min_s"] = min(s for (x, y, s, c) in xy)
        rec["ts_max_s"] = max(s for (x, y, s, c) in xy)
    return per, len(paths), sorted(lengths_m4), spectrum, essential


# --- the ten named objects ----------------------------------------------------

def named_objects():
    """The ten objects with their recorded reference data (loaded from the
    experiments that produced them; every recorded field is asserted against
    the fresh computation in cmd_tables)."""
    objs = []

    cores = json.loads(
        (pathlib.Path(E013_DIR) / "data" / "cores.json").read_text())
    core3 = next(c for c in cores["cores"] if c["index"] == 3)
    census3 = next(e for e in cores["c8_census"] if e["core_index"] == 3)
    objs.append({
        "tag": "P10-Petersen-e",
        "adjacency": core3["adjacency_rows"],
        "g6": None,
        "terminals": tuple(core3["terminals"]),
        "power_lengths": (8,),
        "ref": {"S": core3["S"], "n_power_cycles": 7,
                "combos_total": census3["symdiff_combos"]},
        "calibration": True,
    })

    fam1 = json.loads(
        (pathlib.Path(E021_DIR) / "data" / "interference_family1.json")
        .read_text())
    n14 = next(g for g in fam1["graphs"] if g["g6"] == N14_G6)
    objs.append({
        "tag": "N14-exemplar",
        "adjacency": scan.g6_decode(N14_G6),
        "g6": N14_G6,
        "terminals": tuple(n14["terminals"]),
        "power_lengths": (8,),
        "ref": {"S": n14["S"], "spectrum": n14["spectrum"],
                "n_power_cycles": n14["c8_count"],
                "n_paths": n14["n_through_paths"],
                "per_blocker": n14["blockers"]},
        "calibration": True,
    })

    n19 = json.loads(
        (pathlib.Path(E022_DIR) / "data" / "exemplar_t5_n19.json").read_text())
    assert n19["graph6"] == N19_G6
    objs.append({
        "tag": "N19-profile",
        "adjacency": scan.g6_decode(N19_G6),
        "g6": N19_G6,
        "terminals": tuple(n19["terminals"]),
        "power_lengths": (16,),
        "ref": {"S": n19["path_lengths"], "n_paths": n19["paths"],
                "n_cycles_total": n19["cycles_total"],
                "n_power_cycles": n19["per_length"]["16"]["cycles"]},
        "calibration": False,
    })

    t5n20 = json.loads(
        (pathlib.Path(E022_DIR) / "data" / "t5_n20_profile.json").read_text())
    part14 = json.loads(
        (pathlib.Path(E022_DIR) / "data" / "collect_n20_part14.json")
        .read_text())
    for label, src in (("N20-%s", t5n20["graphs"]),
                       ("N20p14-%s", part14["graphs"])):
        for k, g in enumerate(src):
            objs.append({
                "tag": label % chr(ord("A") + k),
                "adjacency": scan.g6_decode(g["g6"]),
                "g6": g["g6"],
                "terminals": tuple(g["terminals"]),
                "power_lengths": (16,),
                "ref": {"S": g["S"], "spectrum": g["spectrum"],
                        "n_power_cycles": g["c16_count"],
                        "n_paths": g["paths"],
                        "n_cycles_total": g["cycles"]},
                "calibration": False,
            })
    assert len(objs) == 10
    return objs


# --- anchors ------------------------------------------------------------------

def cmd_anchors(_args):
    e021.cmd_anchors(None)          # the imported 45-check suite must pass
    checks = 0

    def ok(cond, label):
        nonlocal checks
        assert cond, "E025 ANCHOR FAILED: %s" % label
        checks += 1

    # 1-3. C16 cycle graph, antipodal terminals: exactly one realization,
    # trunk-split, shape (8,8,0), arcs (8,8), trunks (0,0).
    c16 = scan.from_edges(16, [(i, (i + 1) % 16) for i in range(16)])
    per, n_paths, S, spectrum, ess = realization_tables(c16, 0, 8, (16,))
    ok(len(per) == 1 and per[0]["n_pairs"] == 1
       and per[0]["n_trunk_split"] == 1, "C16 graph: one trunk-split pair")
    ok(per[0]["ts"] == {"8,8,0|8,8|0,0": 1}, "C16 graph: shape (8,8,0)")
    ok(per[0]["flags"]["has_equal"] and per[0]["flags"]["has_s0"]
       and per[0]["flags"]["has_PP"], "C16 graph: equal/s0/PP flags")

    # 4-5. Tail graph (C8 + pendant 2-path at vertex 0, terminals 9 and 4):
    # one blocker, one pair, trunk-split with trunks (2,0), shape (6,6,2).
    tail = scan.from_edges(10, [(i, (i + 1) % 8) for i in range(8)]
                           + [(0, 8), (8, 9)])
    per, n_paths, S, spectrum, ess = realization_tables(tail, 9, 4, (8,))
    ok(len(per) == 1 and per[0]["n_trunk_split"] == 1
       and per[0]["ts"] == {"6,6,2|4,4|2,0": 1},
       "tail graph: trunk-split (6,6,2), trunks (2,0)")
    ok(per[0]["stratum"] == "one", "tail graph stratum")

    # 6-8. Weave control: C6 (0..5) + chord 1-4, a=6 attached at 0, b=7 at 3.
    # The C6 has both a trunk-split realization (5,5,2 via the two pure arcs)
    # and a NON-trunk-split witnessing pair (5,7,3: one path uses the chord,
    # the other weaves both sides) — the classifier must separate them.
    weave = scan.from_edges(8, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5),
                                (5, 0), (1, 4), (6, 0), (7, 3)])
    per, n_paths, S, spectrum, ess = realization_tables(weave, 6, 7, (4,))
    ok(len(per) == 2 and all(r["n_trunk_split"] >= 1 for r in per),
       "weave graph: both chord C4s trunk-split-realized")
    # C6 is not a power length; rerun the tables treating 6 as "power" to
    # exercise the classifier on the C6's witnessing pairs.
    per6, _, _, _, _ = realization_tables(weave, 6, 7, (6,))
    ok(len(per6) == 1, "weave graph: one C6")
    rec = per6[0]
    ok(rec["combos_all"].get("5+5-2*2") == 1
       and rec["combos_all"].get("5+7-2*3") == 1,
       "weave graph: both witnessing pairs found")
    ok(rec["ts"] == {"5,5,2|3,3|1,1": 1} and rec["n_trunk_split"] == 1
       and rec["n_pairs"] == 2,
       "weave graph: weaving pair excluded from the trunk-split layer")

    # 9. Petersen-e via core 3: all-pairs combos equal the recorded E013
    # census (the new enumerator against the recorded data).
    cores = json.loads(
        (pathlib.Path(E013_DIR) / "data" / "cores.json").read_text())
    core3 = next(c for c in cores["cores"] if c["index"] == 3)
    census3 = next(e for e in cores["c8_census"] if e["core_index"] == 3)
    x, y = core3["terminals"]
    per, n_paths, S, spectrum, ess = realization_tables(
        core3["adjacency_rows"], x, y, (8,))
    combos_total = {}
    for rec in per:
        for k, c in rec["combos_all"].items():
            combos_total[k] = combos_total.get(k, 0) + c
    ok(combos_total == census3["symdiff_combos"],
       "Petersen-e: all-pairs combos == recorded E013 census")

    # 10. Petersen-e cross-engine: per-cycle n_pairs equals E021
    # dissect_pair's n_decomposing_pairs on the same blocker order.
    blockers = e021.blockers_of_length(core3["adjacency_rows"], 8)
    per_e021, combos_e021, np_e021, S_e021, _ = e021.dissect_pair(
        core3["adjacency_rows"], x, y, blockers)
    ok([r["n_pairs"] for r in per] ==
       [r["n_decomposing_pairs"] for r in per_e021]
       and n_paths == np_e021 and S == S_e021,
       "Petersen-e: per-cycle pair counts match E021 dissect_pair")

    # 11. N14 exemplar: per-blocker all-pairs combos equal the recorded E021
    # family-1 dissection data (matched by blocker vertex set).
    fam1 = json.loads(
        (pathlib.Path(E021_DIR) / "data" / "interference_family1.json")
        .read_text())
    n14 = next(g for g in fam1["graphs"] if g["g6"] == N14_G6)
    a14, b14 = n14["terminals"]
    per, n_paths, S, spectrum, ess = realization_tables(
        scan.g6_decode(N14_G6), a14, b14, (8,))
    by_vertices = {tuple(r["vertices"]): r for r in per}
    ok(len(per) == n14["c8_count"] == 3, "N14: three C8 blockers")
    match = all(
        by_vertices[tuple(rb["vertices"])]["combos_all"] == rb["combos"]
        and by_vertices[tuple(rb["vertices"])]["stratum"] == rb["stratum"]
        for rb in n14["blockers"])
    ok(match, "N14: per-blocker combos == recorded E021 family-1 data")

    # 12. Tautness instrument agreement on the N19 profile member.
    n19adj = scan.g6_decode(N19_G6)
    per, n_paths, S, spectrum, ess = realization_tables(n19adj, 7, 8, ())
    ok(ess == (1 << 19) - 1 and n_paths == 398,
       "N19: vertex-taut with 398 through-paths (recorded)")

    print("E025 anchors: all %d new checks passed (%s %s)"
          % (checks, sys.implementation.name, sys.version.split()[0]))


# --- the tables ---------------------------------------------------------------

def build_object(obj):
    adjacency = obj["adjacency"]
    n = len(adjacency)
    a, b = obj["terminals"]
    deg = scan.degrees(adjacency)
    assert not scan.has_c4(adjacency), "%s: C4 found" % obj["tag"]
    pair = scan.profile_pair(deg)
    if pair is not None:
        assert set(pair) == {a, b}, "%s: terminals != degree-2 pair" % obj["tag"]
    t0 = time.time()
    per, n_paths, S, spectrum, essential = realization_tables(
        adjacency, a, b, obj["power_lengths"])
    seconds = time.time() - t0
    taut = essential == (1 << n) - 1
    assert taut, "%s: not vertex-taut" % obj["tag"]

    ref = obj["ref"]
    assert S == sorted(ref["S"]), "%s: S mismatch vs record" % obj["tag"]
    if "spectrum" in ref:
        assert spectrum == sorted(ref["spectrum"]), \
            "%s: spectrum mismatch" % obj["tag"]
    if ref.get("n_paths") is not None:
        assert n_paths == ref["n_paths"], "%s: path count" % obj["tag"]
    if ref.get("n_power_cycles") is not None:
        assert len(per) == ref["n_power_cycles"], \
            "%s: power cycle count" % obj["tag"]
    if ref.get("n_cycles_total") is not None:
        n_cycles = len(cat.all_cycles(adjacency))
        assert n_cycles == ref["n_cycles_total"], \
            "%s: total cycle count" % obj["tag"]
    # Power spectrum sanity: exactly the declared power lengths occur.
    present = sorted(set(spectrum) & set(P_SET))
    assert present == sorted(obj["power_lengths"]), \
        "%s: power lengths in spectrum = %s" % (obj["tag"], present)

    s_set = set(S)
    flag_names = ["has_P", "has_P1", "has_PP", "has_P1P1", "has_forced_pair",
                  "has_equal", "has_s0", "has_P2", "all_P2"]
    flag_counts = {f: sum(1 for r in per if r["flags"][f]) for f in flag_names}
    return {
        "tag": obj["tag"],
        "g6": obj["g6"],
        "order": n,
        "terminals": [a, b],
        "calibration": obj["calibration"],
        "S": S,
        "S_class": {str(v): length_class(v) for v in S},
        "S_meets_P": sorted(s_set & P_SET),
        "S_meets_P1": sorted(s_set & P_MINUS_1),
        "S_meets_P2": sorted(s_set & P_MINUS_2),
        "spectrum": spectrum,
        "n_through_paths": n_paths,
        "vertex_taut": taut,
        "two_connected": not scan.cut_vertices(adjacency),
        "bipartite": scan.bipartition(adjacency) is not None,
        "power_lengths": list(obj["power_lengths"]),
        "n_power_cycles": len(per),
        "flag_counts": flag_counts,
        "cycles": per,
        "seconds": round(seconds, 2),
    }


def cmd_tables(args):
    out_name = args[0] if args else "realization_tables.json"
    objs = named_objects()
    t0 = time.time()
    reports = []
    for obj in objs:
        rep = build_object(obj)
        reports.append(rep)
        print("%-14s n=%-2d S=%s  power=%s cycles=%d  pairs=%d ts=%d  "
              "(%.1fs)"
              % (rep["tag"], rep["order"],
                 "[%d..%d]%s" % (rep["S"][0], rep["S"][-1],
                                 "" if rep["S"] == list(range(rep["S"][0],
                                                              rep["S"][-1] + 1))
                                 else "*"),
                 rep["power_lengths"], rep["n_power_cycles"],
                 sum(r["n_pairs"] for r in rep["cycles"]),
                 sum(r["n_trunk_split"] for r in rep["cycles"]),
                 rep["seconds"]))
    os.makedirs(DATA, exist_ok=True)
    payload = {
        "meta": {
            "interpreter": "%s %s" % (sys.implementation.name,
                                      sys.version.split()[0]),
            "seconds": round(time.time() - t0, 1),
            "predicate": "all-pairs layer: E021/E013 census semantics; "
                         "trunk-split layer: L049 arc form "
                         "(P minus Q a single arc), every structural "
                         "invariant asserted per pair",
        },
        "objects": reports,
    }
    path = os.path.join(DATA, out_name) if not out_name.startswith("data/") \
        else os.path.join(HERE, out_name)
    with open(path, "w") as fh:
        json.dump(payload, fh, indent=1, sort_keys=True)
    print("-> %s (%.1fs total)" % (path, payload["meta"]["seconds"]))


def cmd_patterns(_args):
    path = os.path.join(DATA, "realization_tables.json")
    payload = json.loads(open(path).read())
    objects = payload["objects"]
    flag_names = ["has_P", "has_P1", "has_PP", "has_P1P1", "has_forced_pair",
                  "has_equal", "has_s0", "has_P2", "all_P2"]
    print("Pre-registered per-cycle existential patterns "
          "(cycles satisfying / power cycles):")
    header = "%-16s" % "object" + "".join("%12s" % f for f in flag_names)
    print(header)
    verdicts = {}
    for rep in objects:
        row = "%-16s" % rep["tag"]
        for f in flag_names:
            row += "%12s" % ("%d/%d" % (rep["flag_counts"][f],
                                        rep["n_power_cycles"]))
        print(row)
    print()
    result = {}
    for f in flag_names:
        holds_everywhere = all(
            rep["flag_counts"][f] == rep["n_power_cycles"] for rep in objects)
        fails = [
            {"object": rep["tag"],
             "failing_cycles": [i for i, r in enumerate(rep["cycles"])
                                if not r["flags"][f]]}
            for rep in objects
            if rep["flag_counts"][f] != rep["n_power_cycles"]]
        cal_ok = all(rep["flag_counts"][f] == rep["n_power_cycles"]
                     for rep in objects if rep["calibration"])
        result[f] = {
            "universal_all_ten": holds_everywhere,
            "holds_on_both_calibration_objects": cal_ok,
            "failures": fails if not holds_everywhere else [],
        }
        status = ("UNIVERSAL (all ten objects, every power cycle)"
                  if holds_everywhere else
                  "fails on %s" % ", ".join(
                      "%s (%d cycles)" % (x["object"], len(x["failing_cycles"]))
                      for x in fails))
        print("%-16s %s" % (f, status))
    # Class-pair inventory, pooled and per object.
    pooled = {}
    for rep in objects:
        mine = {}
        for r in rep["cycles"]:
            for cp in r["ts_class_pairs"]:
                mine[cp] = mine.get(cp, 0) + 1
                pooled[cp] = pooled.get(cp, 0) + 1
        result.setdefault("class_pairs_per_object", {})[rep["tag"]] = mine
    result["class_pairs_pooled_cycle_counts"] = pooled
    print("\nClass-pair inventory (number of power cycles admitting each "
          "trunk-split class pair, pooled over the ten objects):")
    for cp, c in sorted(pooled.items(), key=lambda kv: -kv[1]):
        print("  %-8s %d" % (cp, c))
    with open(os.path.join(DATA, "pattern_verdicts.json"), "w") as fh:
        json.dump(result, fh, indent=1, sort_keys=True)
    print("-> data/pattern_verdicts.json")


def main():
    cmds = {
        "anchors": cmd_anchors,
        "tables": cmd_tables,
        "patterns": cmd_patterns,
    }
    if len(sys.argv) < 2 or sys.argv[1] not in cmds:
        print(__doc__)
        sys.exit(1)
    cmds[sys.argv[1]](sys.argv[2:])


if __name__ == "__main__":
    main()
