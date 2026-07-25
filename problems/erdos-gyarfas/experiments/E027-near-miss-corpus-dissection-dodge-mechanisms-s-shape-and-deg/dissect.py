#!/usr/bin/env python3
"""E027 -- near-miss corpus dissection (P-002, session S026; A026 plan step 1).

The census (E026/C046) left exactly one viable hypothesis set for the
(F-S) interpolation lemma: the exactly-two profile.  This instrument
dissects the stored contrast -- the 9,061 vertex-taut gapped pairs
(the near-miss corpus) against the eight profile objects -- to extract
the mechanism by which "min degree >= 3 off the terminals" forces the
poison lengths.  PRE-REGISTERED QUESTIONS (fixed before production):

  Q1 (S-shape; corpus rows + profile objects, stored S).  A pair can
     dodge poison p three ways: DISTANCE (min S > p), SHORT
     (max S < p), INTERIOR (min S < p < max S, p not in S).  Which
     mechanisms carry the 6- and 14-dodges, by order and by ndeg2?
     Sub-question D1: do taut pairs in this class have upper-interval
     through-sets -- no gaps at or above 7 strictly inside
     [min S, max S]?  (All eight profile objects satisfy it, S cap
     [6,inf) an interval; Petersen-e and the order-14 exemplar
     satisfy it too, their 6-dodges being boundary/interior gaps AT 6
     with [7, max S] full.)  If corpus dodges are all range dodges
     (distance/short) with D1 intact, the lemma decomposes into a
     class-wide interval theorem plus a profile-specific range
     theorem; interior gaps >= 7 in the corpus kill that decomposition.

  Q2 (range structure).  Distributions of min S (= d(a,b), asserted),
     max S, n-1 - max S, and the 5/7 and 13/15 sandwich flags at
     interior misses.  The profile objects all have max S = n-1
     (Hamiltonian a-b paths); how far below n-1 do near-miss maxima
     sit?

  Q3 (degree-2 geometry; the subdivision frame).  A near-miss member
     with ndeg2 = k > 2 is a partial subdivision of a smaller
     two-terminal graph H* (suppress every non-terminal degree-2
     vertex; corridors become weighted edges), while the profile is
     exactly the subdivision-free stratum H = H*.  Per dodge-carrying
     member: chain decomposition of the induced graph on degree-2
     vertices (chain sizes; terminals' chains, same-chain flag per
     row), corridor weights, H* order, H* simplicity, and -- the
     class-constraint erosion test -- whether the simple part of H*
     contains a C4 or C8 (H {C4,C8}-free does NOT bound H*'s short
     cycles; if H* routinely carries C4/C8, subdivision is literally
     the mechanism that escapes the class constraint).

  Q4 (odd-adjustment supply).  Presence/counts of C3, C5, C6, C7 in
     dodge members vs a stride control vs the eight profile objects
     (the +-1 length adjustments that interval-saturate S ride on
     short odd cycles; the profile objects have full spectrum
     [3,n] minus {4,8}).

  CONTROL.  A deterministic stride sample of class members at orders
     18/19/20 (dodge or not), with full path enumeration on every
     degree-2 pair: the D1 gap statistics of ORDINARY taut pairs (do
     non-dodge pairs carry interior gaps >= 7 anyway?), plus the same
     member-level geometry.  L035 SOUNDNESS ALARM: every taut pair on
     a non-bipartite member must show both parities in S (parity-
     constancy <=> bipartiteness for taut pairs); any violation halts.

Imports (read-only, the E026 -> E021/E019 chain): g6_decode, degrees,
bfs_dist, bipartition, has_cycle_len, count_cycles_len, has_path_len,
paths_with_essential, petersen_minus_e, class file access.  E026/data
is listed before and after the import and asserted unchanged.  New
code: the S-shape classifiers, chain/corridor decomposition, the
smoothing construction, cycle counters, tallies.  Deterministic;
stdlib only; wall clock in timing fields only.  E024 (order-21 rung,
running) is never touched; production here runs single-process at
nice 15.

Commands (anchors under BOTH interpreters before production):
  dissect.py anchors    # micro-tests, named objects, corpus totals
  dissect.py corpus     # Q1/Q2/Q3/Q4 over the 9,061 rows + 8 profile objects
  dissect.py control    # stride control with full enumeration (the slow leg)
  dissect.py report     # merge + the contrast tables
"""

import json
import os
import sys
import time

sys.dont_write_bytecode = True
import importlib.util                   # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
EXPS = os.path.dirname(HERE)
E026_DIR = os.path.join(
    EXPS, "E026-s-gap-census-over-the-c4-c8-free-classes-at-orders-10-20-poi")
E026_DATA = os.path.join(E026_DIR, "data")


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


_before = sorted(os.listdir(E026_DATA))
census = _load("e026_census", os.path.join(E026_DIR, "census.py"))
_after = sorted(os.listdir(E026_DATA))
assert _before == _after, "importing E026/census.py changed E026/data"
# rebind every output path to E027/data; E026 and its ancestors stay read-only
os.makedirs(DATA, exist_ok=True)
census.DATA = DATA
census.scan.DATA = DATA
census.e021.DATA = DATA
census.e021.scan.DATA = DATA
import pathlib                           # noqa: E402
census.e021.cat.DATA = pathlib.Path(DATA)

g6_decode = census.g6_decode
degrees = census.degrees
bipartition = census.bipartition
bfs_dist = census.bfs_dist
has_cycle_len = census.has_cycle_len
count_cycles_len = census.count_cycles_len
has_path_len = census.has_path_len
paths_with_essential = census.paths_with_essential
petersen_minus_e = census.petersen_minus_e
class_files = census.class_files
read_lines = census.read_lines
interpreter = census.scan.interpreter

N14_G6 = census.N14_G6
N19_G6 = census.N19_G6

CORPUS_TOTAL = 9061
CORPUS_PER_ORDER = {12: 8, 14: 8, 16: 371, 17: 24, 18: 2727, 19: 167, 20: 5756}
PROFILE_TOTAL = 8
ROW_RECHECK_STRIDE = 250      # full-enumeration re-verification stride (corpus)
CONTROL_STRIDE = {18: 600, 19: 400, 20: 3000}   # member stride per class part


# ----------------------------------------------------------------------
# S-shape classifiers (pure functions of the stored S list)


def dodge_type(S, poison):
    """DISTANCE / SHORT / INTERIOR for a poison known to be absent."""
    assert poison not in S
    lo, hi = S[0], S[-1]
    if poison < lo:
        return "distance"
    if poison > hi:
        return "short"
    return "interior"


def gap_positions(S):
    """Missing lengths strictly inside [min S, max S]."""
    present = set(S)
    return [l for l in range(S[0] + 1, S[-1]) if l not in present]


def shape_record(S, n):
    """Q1/Q2 shape facts for one sorted through-set."""
    lo, hi = S[0], S[-1]
    gaps = gap_positions(S)
    present = set(S)
    return {
        "lo": lo, "hi": hi, "ham": hi == n - 1, "n1_minus_hi": (n - 1) - hi,
        "gaps": gaps,
        "gaps7plus": [l for l in gaps if l >= 7],
        "parities": sorted({l % 2 for l in S}),
        "sandwich6": (5 in present) and (7 in present),
        "sandwich14": (13 in present) and (15 in present),
    }


# ----------------------------------------------------------------------
# degree-2 geometry (member level)


def deg2_chains(adjacency, deg):
    """Components of the induced graph on degree-2 vertices.

    Each component of H[D2] is a path or a cycle (induced degrees
    <= 2).  Returns (chains, is_cycle_flags): chains as sorted vertex
    lists in path order where applicable.
    """
    n = len(adjacency)
    d2 = [v for v in range(n) if deg[v] == 2]
    d2set = set(d2)
    seen = set()
    chains, cycle_flags = [], []
    for v in d2:
        if v in seen:
            continue
        comp = [v]
        seen.add(v)
        frontier = [v]
        while frontier:
            u = frontier.pop()
            row = adjacency[u]
            while row:
                low = row & -row
                w = low.bit_length() - 1
                row ^= low
                if w in d2set and w not in seen:
                    seen.add(w)
                    comp.append(w)
                    frontier.append(w)
        sub_deg = {u: bin(adjacency[u] & _mask(comp)).count("1") for u in comp}
        is_cycle = all(x == 2 for x in sub_deg.values()) and len(comp) >= 3
        chains.append(sorted(comp))
        cycle_flags.append(is_cycle)
    return chains, cycle_flags


def _mask(vertices):
    m = 0
    for v in vertices:
        m |= 1 << v
    return m


def smooth(adjacency, keep):
    """Suppress every degree-2 vertex not in `keep`; corridors become
    weighted edges.  Returns (n_star, weighted_edges, simple, loops)
    where weighted_edges is a sorted list of (u, v, weight) with u, v
    indices into the kept vertex list, u <= v; simple is True when no
    parallel edges and no loops arise; loops counts corridor loops."""
    n = len(adjacency)
    deg = degrees(adjacency)
    kept = [v for v in range(n) if deg[v] != 2 or v in keep]
    index = {v: i for i, v in enumerate(kept)}
    kept_set = set(kept)
    edges = []
    for v in kept:
        row = adjacency[v]
        while row:
            low = row & -row
            w = low.bit_length() - 1
            row ^= low
            if w in kept_set:
                if v < w:
                    edges.append((index[v], index[w], 1))
                continue
            # walk the corridor of suppressed degree-2 vertices
            prev, cur, weight = v, w, 1
            while cur not in kept_set:
                nxt_row = adjacency[cur]
                nxt_row &= ~(1 << prev)
                assert nxt_row and nxt_row & (nxt_row - 1) == 0, \
                    "suppressed vertex without exactly one forward edge"
                nxt = nxt_row.bit_length() - 1
                prev, cur, weight = cur, nxt, weight + 1
            # each corridor is discovered twice, once from each kept end:
            # as (v, w, ...) here and as (cur, prev, ...) from the other
            # side (w / prev are the first suppressed vertices seen).
            # (v, w) == (cur, prev) is impossible, so keeping the
            # lexicographically smaller endpoint pair keeps exactly one
            # copy -- including corridor loops (v == cur, w != prev).
            if (v, w) < (cur, prev):
                a_i, b_i = index[v], index[cur]
                edges.append((min(a_i, b_i), max(a_i, b_i), weight))
    edges.sort()
    loops = sum(1 for u, v, _ in edges if u == v)
    pair_counts = {}
    for u, v, _ in edges:
        if u != v:
            pair_counts[(u, v)] = pair_counts.get((u, v), 0) + 1
    simple = loops == 0 and all(c == 1 for c in pair_counts.values())
    return len(kept), edges, simple, loops


def smooth_simple_adjacency(n_star, edges):
    """Adjacency of the SIMPLE part of H* (loops dropped, parallel
    edges collapsed) -- the object whose unweighted C4/C8 status
    measures class-constraint erosion under subdivision."""
    adj = [0] * n_star
    for u, v, _ in edges:
        if u != v:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    return adj


def triangle_count(adjacency):
    """Each triangle counted once: edge (v, w) with v < w, third
    vertex u > w."""
    n = len(adjacency)
    t = 0
    for v in range(n):
        for w in range(v + 1, n):
            if adjacency[v] >> w & 1:
                common = adjacency[v] & adjacency[w]
                common &= ~((1 << (w + 1)) - 1)
                t += bin(common).count("1")
    return t


def member_geometry(g6):
    adjacency = g6_decode(g6)
    n = len(adjacency)
    deg = degrees(adjacency)
    chains, cycle_flags = deg2_chains(adjacency, deg)
    assert not any(cycle_flags), "degree-2 cycle component (disconnected?)"
    return {
        "g6": g6, "order": n,
        "ndeg2": sum(1 for d in deg if d == 2),
        "max_deg": max(deg),
        "chain_sizes": sorted(len(c) for c in chains),
        "c3": triangle_count(adjacency),
        "c5": has_cycle_len(adjacency, 5),
        "c6": has_cycle_len(adjacency, 6),
        "c7": has_cycle_len(adjacency, 7),
        "_adjacency": adjacency, "_deg": deg, "_chains": chains,
    }


def row_geometry(geo, a, b):
    """Row-level geometry on top of member geometry."""
    adjacency = geo["_adjacency"]
    n = geo["order"]
    chains = geo["_chains"]
    chain_of = {}
    for c in chains:
        for v in c:
            chain_of[v] = tuple(c)
    keep = {a, b}
    n_star, edges, simple, loops = smooth(adjacency, keep)
    weights = sorted(w for _, _, w in edges)
    rec = {
        "a_chain": len(chain_of[a]), "b_chain": len(chain_of[b]),
        "same_chain": chain_of[a] == chain_of[b],
        "n_star": n_star, "shrink": n - n_star,
        "star_simple": simple, "star_loops": loops,
        "corridor_weights": [w for w in weights if w > 1],
    }
    total = sum(w for _, _, w in edges)
    m = sum(bin(r).count("1") for r in adjacency) // 2
    assert total == m, "smoothing lost edges: %s" % geo["g6"]
    star_adj = smooth_simple_adjacency(n_star, edges)
    rec["star_c4"] = has_cycle_len(star_adj, 4)
    rec["star_c8"] = has_cycle_len(star_adj, 8)
    return rec


# ----------------------------------------------------------------------
# loading the corpus and the profile rows


def load_corpus():
    with open(os.path.join(E026_DATA, "census_summary.json")) as fh:
        summary = json.load(fh)
    rows = summary["taut_gapped_pairs"]
    assert len(rows) == CORPUS_TOTAL
    per = {}
    for r in rows:
        per[r["order"]] = per.get(r["order"], 0) + 1
    assert per == CORPUS_PER_ORDER, "corpus per-order mismatch: %r" % per
    assert not summary["fs_kill_candidates"]
    return rows, summary


def load_profile_rows():
    rows = []
    for part in range(16):
        path = os.path.join(E026_DATA, "census_n19_part%dof16.json" % part)
        with open(path) as fh:
            rows.extend(json.load(fh)["exactly_two_members"])
    for part in census.N20_PARTS_ON_DISK:
        path = os.path.join(E026_DATA, "census_n20_part%dof16.json" % part)
        with open(path) as fh:
            rows.extend(json.load(fh)["exactly_two_members"])
    with open(os.path.join(E026_DATA, "census_n20supp14.json")) as fh:
        rows.extend(json.load(fh)["exactly_two_members"])
    assert len(rows) == PROFILE_TOTAL
    assert sum(1 for r in rows if r["order"] == 19) == 1
    assert sum(1 for r in rows if r["order"] == 20) == 7
    for r in rows:
        assert r["n_degree2"] == 2 and r["vertex_taut"] and not r["gapped"]
        assert 6 in r["S"] and 14 in r["S"]
    return rows


# ----------------------------------------------------------------------
# tallies


def blank_shape_tally():
    keys = ("distance", "short", "interior")
    return {
        "rows": 0,
        "dodge6": {k: 0 for k in keys},
        "dodge14": {k: 0 for k in keys},
        "joint": {},
        "rows_with_gap7plus": 0,
        "gap7plus_positions": {},
        "lo_hist": {}, "hi_hist": {}, "n1_minus_hi_hist": {},
        "ham_rows": 0,
        "interior6_sandwich": 0, "interior6": 0,
        "interior14_sandwich": 0, "interior14": 0,
    }


def add_shape(tly, shape, d6, d14):
    tly["rows"] += 1
    tly["dodge6"][d6] += 1
    tly["dodge14"][d14] += 1
    key = d6 + "/" + d14
    tly["joint"][key] = tly["joint"].get(key, 0) + 1
    if shape["gaps7plus"]:
        tly["rows_with_gap7plus"] += 1
        for l in shape["gaps7plus"]:
            tly["gap7plus_positions"][str(l)] = \
                tly["gap7plus_positions"].get(str(l), 0) + 1
    for name, val in (("lo_hist", shape["lo"]), ("hi_hist", shape["hi"]),
                      ("n1_minus_hi_hist", shape["n1_minus_hi"])):
        tly[name][str(val)] = tly[name].get(str(val), 0) + 1
    if shape["ham"]:
        tly["ham_rows"] += 1
    if d6 == "interior":
        tly["interior6"] += 1
        if shape["sandwich6"]:
            tly["interior6_sandwich"] += 1
    if d14 == "interior":
        tly["interior14"] += 1
        if shape["sandwich14"]:
            tly["interior14_sandwich"] += 1


# ----------------------------------------------------------------------
# commands


def cmd_corpus(_args):
    t0 = time.time()
    rows, _ = load_corpus()
    profile = load_profile_rows()
    shape_by_order = {}
    geo_cache = {}
    member_rows = {}
    rechecks = 0
    for i, r in enumerate(rows):
        S, n, g6 = r["S"], r["order"], r["g6"]
        a, b = r["terminals"]
        assert r["vertex_taut"] and r["gapped"]
        assert 6 not in S and 14 not in S
        assert r["c16_present"] == (r["c16_count"] > 0)
        assert S == sorted(S) and S[0] >= 1
        adjacency = None
        if g6 not in geo_cache:
            geo_cache[g6] = member_geometry(g6)
            member_rows[g6] = []
        member_rows[g6].append(i)
        geo = geo_cache[g6]
        adjacency = geo["_adjacency"]
        assert geo["ndeg2"] == r["n_degree2"]
        dist_b = bfs_dist(adjacency, b, (1 << n) - 1)
        assert dist_b[a] == S[0], "min S != d(a,b) on %s" % g6
        # L035 soundness alarm: taut + non-bipartite => both parities
        assert bipartition(adjacency) is None, "bipartite corpus member"
        assert len({l % 2 for l in S}) == 2, \
            "L035 violation (parity-constant taut S) on %s" % g6
        if i % ROW_RECHECK_STRIDE == 0:
            s2, essential = paths_with_essential(adjacency, a, b)
            assert sorted(s2) == S, "stored S mismatch on %s" % g6
            assert essential == (1 << n) - 1
            rechecks += 1
        shape = shape_record(S, n)
        d6 = dodge_type(S, 6)
        d14 = dodge_type(S, 14)
        tly = shape_by_order.setdefault(n, blank_shape_tally())
        add_shape(tly, shape, d6, d14)
        r["_shape"], r["_d6"], r["_d14"] = shape, d6, d14
    # profile objects: shape + geometry (H* = H expected)
    profile_out = []
    for r in profile:
        S, n, g6 = r["S"], r["order"], r["g6"]
        a, b = r["terminals"]
        geo = member_geometry(g6)
        shape = shape_record(S, n)
        assert not shape["gaps7plus"], \
            "profile object with a gap >= 7: %s" % g6
        assert shape["ham"], "profile object without Hamiltonian a-b path"
        rg = row_geometry(geo, a, b)
        assert rg["shrink"] == 0 and rg["star_simple"], \
            "profile object not subdivision-free"
        s2, essential = paths_with_essential(geo["_adjacency"], a, b)
        assert sorted(s2) == S and essential == (1 << n) - 1
        profile_out.append({
            "g6": g6, "order": n, "S": S, "shape": shape,
            "geometry": {k: v for k, v in geo.items()
                         if not k.startswith("_")},
            "row_geometry": rg,
        })
    # member-level geometry + per-row smoothing for the corpus
    member_out = []
    row_geo_tally = {}
    for g6, geo in geo_cache.items():
        member_out.append({k: v for k, v in geo.items()
                           if not k.startswith("_")})
        for i in member_rows[g6]:
            r = rows[i]
            a, b = r["terminals"]
            rg = row_geometry(geo, a, b)
            n = r["order"]
            t = row_geo_tally.setdefault(n, {
                "rows": 0, "same_chain": 0, "a_or_b_in_long_chain": 0,
                "shrink_hist": {}, "star_c4": 0, "star_c8": 0,
                "star_c4_or_c8": 0, "star_nonsimple": 0,
                "corridor_weight_hist": {},
            })
            t["rows"] += 1
            t["same_chain"] += rg["same_chain"]
            t["a_or_b_in_long_chain"] += (rg["a_chain"] > 1 or rg["b_chain"] > 1)
            t["shrink_hist"][str(rg["shrink"])] = \
                t["shrink_hist"].get(str(rg["shrink"]), 0) + 1
            t["star_c4"] += rg["star_c4"]
            t["star_c8"] += rg["star_c8"]
            t["star_c4_or_c8"] += (rg["star_c4"] or rg["star_c8"])
            t["star_nonsimple"] += (not rg["star_simple"])
            for w in rg["corridor_weights"]:
                t["corridor_weight_hist"][str(w)] = \
                    t["corridor_weight_hist"].get(str(w), 0) + 1
            r["_rg"] = rg
    # cycle-profile tallies (member level) for dodge members
    cyc_tally = {}
    for g6, geo in geo_cache.items():
        n = geo["order"]
        t = cyc_tally.setdefault(n, {"members": 0, "c3_pos": 0, "c3_total": 0,
                                     "c5": 0, "c6": 0, "c7": 0})
        t["members"] += 1
        t["c3_pos"] += geo["c3"] > 0
        t["c3_total"] += geo["c3"]
        t["c5"] += geo["c5"]
        t["c6"] += geo["c6"]
        t["c7"] += geo["c7"]
    # Q5: the (reduced order, max S) frontier -- does corridor excess buy
    # exactly the short-range tautness the profile cannot have?
    frontier = {}
    compact = []
    for r in rows:
        n, rg, shape = r["order"], r["_rg"], r["_shape"]
        n_star = rg["n_star"]
        key = (r["_d14"], n, n_star, shape["hi"])
        frontier[key] = frontier.get(key, 0) + 1
        compact.append({
            "g6": r["g6"], "terminals": r["terminals"], "n": n,
            "ndeg2": r["n_degree2"], "lo": shape["lo"], "hi": shape["hi"],
            "d6": r["_d6"], "d14": r["_d14"],
            "gaps": shape["gaps"], "n_star": n_star,
            "star_c4": rg["star_c4"], "star_c8": rg["star_c8"],
            "star_simple": rg["star_simple"],
            "weights": rg["corridor_weights"],
            "same_chain": rg["same_chain"],
            "power_free_member": not r["c16_present"],
        })
    frontier_rows = [{"d14": k[0], "n": k[1], "n_star": k[2], "hi": k[3],
                      "rows": v} for k, v in sorted(frontier.items())]
    # the class-constraint-erosion exceptions: rows whose reduced simple
    # graph is still {C4,C8}-free
    exceptions = [c for c in compact
                  if not c["star_c4"] and not c["star_c8"]]
    out = {
        "rows": len(rows), "distinct_members": len(geo_cache),
        "row_rechecks": rechecks,
        "shape_by_order": {str(k): v for k, v in sorted(shape_by_order.items())},
        "row_geometry_by_order": {str(k): v
                                  for k, v in sorted(row_geo_tally.items())},
        "cycles_by_order": {str(k): v for k, v in sorted(cyc_tally.items())},
        "profile_objects": profile_out,
        "frontier": frontier_rows,
        "star_class_free_exceptions": exceptions,
        "seconds": round(time.time() - t0, 2),
        "interpreter": interpreter(),
    }
    with open(os.path.join(DATA, "corpus_rows_compact.json"), "w") as fh:
        json.dump(compact, fh, indent=0)
    with open(os.path.join(DATA, "corpus_dissection.json"), "w") as fh:
        json.dump(out, fh, indent=1)
    print("corpus: rows=%d members=%d rechecks=%d  %.1fs"
          % (len(rows), len(geo_cache), rechecks, out["seconds"]))
    for n in sorted(shape_by_order):
        t = shape_by_order[n]
        print(" n=%d rows=%d  d6=%r  d14=%r  gap7plus=%d ham=%d"
              % (n, t["rows"], t["dodge6"], t["dodge14"],
                 t["rows_with_gap7plus"], t["ham_rows"]))


def cmd_control(_args):
    t0 = time.time()
    tallies = {}
    member_records = []
    checked = 0
    for order in (18, 19, 20):
        stride = CONTROL_STRIDE[order]
        seen = 0
        tly = tallies.setdefault(order, {
            "members": 0, "pairs": 0, "taut_pairs": 0,
            "pairs_with_gap7plus": 0, "gap7plus_positions": {},
            "gapped_pairs": 0, "ham_pairs": 0,
            "n1_minus_hi_hist": {}, "c3_pos_members": 0,
            "bit6_pairs": 0, "bit14_pairs": 0,
        })
        for path in class_files(order):
            for line in read_lines(path):
                if not line or line.startswith("#"):
                    continue
                seen += 1
                if seen % stride:
                    continue
                g6 = line.split()[0]
                geo = member_geometry(g6)
                adjacency = geo["_adjacency"]
                n = geo["order"]
                deg = geo["_deg"]
                d2 = [v for v in range(n) if deg[v] == 2]
                assert bipartition(adjacency) is None, \
                    "bipartite control member %s" % g6
                tly["members"] += 1
                tly["c3_pos_members"] += geo["c3"] > 0
                member_records.append(
                    {k: v for k, v in geo.items() if not k.startswith("_")})
                for i in range(len(d2)):
                    for j in range(i + 1, len(d2)):
                        a, b = d2[i], d2[j]
                        s, essential = paths_with_essential(adjacency, a, b)
                        S = sorted(s)
                        taut = essential == (1 << n) - 1
                        tly["pairs"] += 1
                        checked += 1
                        if not taut:
                            continue
                        tly["taut_pairs"] += 1
                        assert len({l % 2 for l in S}) == 2, \
                            "L035 violation on control %s" % g6
                        shape = shape_record(S, n)
                        if shape["gaps7plus"]:
                            tly["pairs_with_gap7plus"] += 1
                            for l in shape["gaps7plus"]:
                                tly["gap7plus_positions"][str(l)] = \
                                    tly["gap7plus_positions"].get(str(l), 0) + 1
                        if 6 not in s and 14 not in s:
                            tly["gapped_pairs"] += 1
                        if 6 in s:
                            tly["bit6_pairs"] += 1
                        if 14 in s:
                            tly["bit14_pairs"] += 1
                        if shape["ham"]:
                            tly["ham_pairs"] += 1
                        tly["n1_minus_hi_hist"][str(shape["n1_minus_hi"])] = \
                            tly["n1_minus_hi_hist"].get(
                                str(shape["n1_minus_hi"]), 0) + 1
    out = {
        "stride": CONTROL_STRIDE,
        "tallies": {str(k): v for k, v in sorted(tallies.items())},
        "member_geometry": member_records,
        "full_enumerations": checked,
        "seconds": round(time.time() - t0, 2),
        "interpreter": interpreter(),
    }
    with open(os.path.join(DATA, "control_sample.json"), "w") as fh:
        json.dump(out, fh, indent=1)
    print("control: enumerations=%d  %.1fs" % (checked, out["seconds"]))
    for n in sorted(tallies):
        t = tallies[n]
        print(" n=%d members=%d pairs=%d taut=%d gap7plus=%d gapped=%d ham=%d"
              % (n, t["members"], t["pairs"], t["taut_pairs"],
                 t["pairs_with_gap7plus"], t["gapped_pairs"], t["ham_pairs"]))


def cmd_report(_args):
    with open(os.path.join(DATA, "corpus_dissection.json")) as fh:
        corpus = json.load(fh)
    with open(os.path.join(DATA, "control_sample.json")) as fh:
        control = json.load(fh)
    print("== Q1 dodge mechanisms (corpus rows) ==")
    print(" order |  rows | d6 dist/short/int | d14 dist/short/int | gap7+ | ham")
    for n, t in sorted(corpus["shape_by_order"].items(), key=lambda kv: int(kv[0])):
        d6, d14 = t["dodge6"], t["dodge14"]
        print(" %5s | %5d | %5d/%5d/%5d | %6d/%5d/%5d | %5d | %3d"
              % (n, t["rows"], d6["distance"], d6["short"], d6["interior"],
                 d14["distance"], d14["short"], d14["interior"],
                 t["rows_with_gap7plus"], t["ham_rows"]))
    print("\n== D1 upper-interval control (taut pairs, stride sample) ==")
    for n, t in sorted(control["tallies"].items(), key=lambda kv: int(kv[0])):
        print(" n=%s taut=%d gap7plus=%d (%.2f%%) positions=%r"
              % (n, t["taut_pairs"], t["pairs_with_gap7plus"],
                 100.0 * t["pairs_with_gap7plus"] / max(1, t["taut_pairs"]),
                 t["gap7plus_positions"]))
    print("\n== Q3 subdivision frame (corpus rows) ==")
    for n, t in sorted(corpus["row_geometry_by_order"].items(),
                       key=lambda kv: int(kv[0])):
        print(" n=%s rows=%d same_chain=%d term_in_chain=%d star C4=%d C8=%d "
              "either=%d nonsimple=%d shrink=%r"
              % (n, t["rows"], t["same_chain"], t["a_or_b_in_long_chain"],
                 t["star_c4"], t["star_c8"], t["star_c4_or_c8"],
                 t["star_nonsimple"], t["shrink_hist"]))
    print("\n== Q4 odd-cycle supply ==")
    for n, t in sorted(corpus["cycles_by_order"].items(),
                       key=lambda kv: int(kv[0])):
        print(" n=%s dodge-members=%d C3>0: %d (%.1f%%) C5: %d C6: %d C7: %d"
              % (n, t["members"], t["c3_pos"],
                 100.0 * t["c3_pos"] / max(1, t["members"]),
                 t["c5"], t["c6"], t["c7"]))
    print("\n== profile objects ==")
    for p in corpus["profile_objects"]:
        sh = p["shape"]
        print(" n=%d lo=%d hi=%d gaps=%r C3=%d C5=%s star=(%d,%s)"
              % (p["order"], sh["lo"], sh["hi"], sh["gaps"],
                 p["geometry"]["c3"], p["geometry"]["c5"],
                 p["row_geometry"]["shrink"],
                 p["row_geometry"]["star_simple"]))


# ----------------------------------------------------------------------
# the chord-exchange calculus on a Hamiltonian a-b path
#
# For a pair with a Hamiltonian a-b path P (positions 0..M), every
# non-path edge is a chord (v_i, v_j), i < j, of span sigma = j - i.
# Rerouting P along pairwise interior-disjoint chords yields a simple
# a-b path of length M - sum(sigma_k - 1): each such length is REAL
# (soundness by construction).  In a {C4,C8}-free graph a span-3 chord
# is impossible (chord + 3 path edges = C4) and a span-7 chord is
# impossible (C8) -- asserted.  The DP below computes the full
# downset of achievable savings.


def find_ham_path(adjacency, a, b):
    """One Hamiltonian a-b path as a vertex list, or None."""
    n = len(adjacency)
    full = (1 << n) - 1
    dist_b = bfs_dist(adjacency, b, full)
    target = 1 << b
    stack = [(a, 1 << a, [a])]
    while stack:
        v, used, path = stack.pop()
        rem = n - 1 - (len(path) - 1)      # edges still needed
        if rem == 0:
            if v == b:
                return path
            continue
        row = adjacency[v] & ~used
        if rem > 1:
            row &= ~target
        while row:
            low = row & -row
            w = low.bit_length() - 1
            row ^= low
            if dist_b[w] <= rem - 1:
                stack.append((w, used | low, path + [w]))
    return None


def chord_exchange_downset(adjacency, path):
    """(spans, savings_set) for the disjoint-chord exchange calculus."""
    n = len(adjacency)
    M = len(path) - 1
    pos = {v: i for i, v in enumerate(path)}
    assert len(pos) == n == M + 1, "not a Hamiltonian path"
    chords = []
    for i, v in enumerate(path):
        row = adjacency[v]
        while row:
            low = row & -row
            w = low.bit_length() - 1
            row ^= low
            j = pos[w]
            if j > i + 1:
                chords.append((i, j))
    spans = sorted(j - i for i, j in chords)
    for s in spans:
        assert s not in (3, 7), "span-%d chord contradicts C4/C8-freeness" % s
    # DP over suffixes: savings achievable from position i onward
    by_start = {}
    for i, j in chords:
        by_start.setdefault(i, []).append(j)
    reach = [0] * (M + 2)                  # bitmask of savings
    reach[M] = 1                            # empty suffix: saving 0
    reach[M + 1] = 1
    for i in range(M - 1, -1, -1):
        mask = reach[i + 1]                 # skip position i
        for j in by_start.get(i, ()):
            mask |= reach[j] << (j - i - 1)  # take chord (i, j)
        reach[i] = mask
    savings = [s for s in range(M) if reach[0] >> s & 1]
    return spans, savings


def cmd_exchange(_args):
    t0 = time.time()
    profile = load_profile_rows()
    out = []
    print("== first-order disjoint-chord exchange on Hamiltonian paths ==")
    for r in profile:
        g6, n = r["g6"], r["order"]
        a, b = r["terminals"]
        adjacency = g6_decode(g6)
        S = set(r["S"])
        M = n - 1
        path = find_ham_path(adjacency, a, b)
        assert path is not None, "profile object lost its Hamiltonian path"
        spans, savings = chord_exchange_downset(adjacency, path)
        generated = sorted(M - s for s in savings)
        for l in generated:
            assert l in S, "generated length %d not in S on %s (SOUNDNESS)" \
                % (l, g6)
        target = [l for l in range(r["S"][0], M + 1)]
        missed = [l for l in target if l not in generated]
        out.append({
            "g6": g6, "order": n, "terminals": [a, b],
            "ham_path": path, "chord_spans": spans,
            "generated": generated, "S": r["S"], "missed": missed,
        })
        print(" n=%d chords=%d spans=%r" % (n, len(spans), spans))
        print("   generated %d of %d lengths in [%d, %d]; missed %r"
              % (len(target) - len(missed), len(target),
                 target[0], M, missed))
    # the 36 Hamiltonian corpus rows (order 18, interior-14): the same
    # calculus must respect their holes (soundness re-check on dodgers)
    rows, _ = load_corpus()
    ham_rows = [r for r in rows
                if r["S"][-1] == r["order"] - 1]
    print(" corpus Hamiltonian dodge rows: %d" % len(ham_rows))
    corpus_out = []
    for r in ham_rows:
        adjacency = g6_decode(r["g6"])
        a, b = r["terminals"]
        S = set(r["S"])
        M = r["order"] - 1
        path = find_ham_path(adjacency, a, b)
        assert path is not None
        spans, savings = chord_exchange_downset(adjacency, path)
        generated = sorted(M - s for s in savings)
        for l in generated:
            assert l in S, "generated length %d not in S on %s (SOUNDNESS)" \
                % (l, r["g6"])
        corpus_out.append({
            "g6": r["g6"], "order": r["order"], "terminals": [a, b],
            "chord_spans": spans, "generated": generated, "S": r["S"],
        })
    covered = sum(1 for c in corpus_out
                  if set(c["generated"]) == set(range(
                      min(c["generated"]), c["order"])))
    print("   corpus ham rows where calculus fills an interval: %d" % covered)
    res = {"profile": out, "corpus_ham_rows": corpus_out,
           "seconds": round(time.time() - t0, 2),
           "interpreter": interpreter()}
    with open(os.path.join(DATA, "exchange_test.json"), "w") as fh:
        json.dump(res, fh, indent=1)


# ----------------------------------------------------------------------
# anchors


def cmd_anchors(_args):
    checks = []

    def ok(name, cond):
        assert cond, "anchor failed: %s" % name
        checks.append(name)

    # a1: classifier micro-tests on synthetic S sets
    ok("a1a", dodge_type([7, 8], 6) == "distance")
    ok("a1b", dodge_type([7, 8], 14) == "short")
    ok("a1c", dodge_type([3, 15], 6) == "interior")
    ok("a1d", dodge_type([3, 15], 14) == "interior")
    ok("a1e", gap_positions([3, 15]) == list(range(4, 15)))
    ok("a1f", gap_positions([4, 5, 7, 8]) == [6])
    sh = shape_record([4, 5, 7, 8], 10)
    ok("a1g", sh["gaps7plus"] == [] and sh["n1_minus_hi"] == 1
       and not sh["ham"] and sh["sandwich6"])
    sh = shape_record([5, 7, 9, 12, 13, 15, 17], 18)
    ok("a1h", sh["gaps7plus"] == [8, 10, 11, 14, 16] and sh["ham"])

    # a2: Petersen-e -- S = {4,5,7,8}, taut, interior-6, short-14
    adjacency = petersen_minus_e()
    deg = degrees(adjacency)
    d2 = [v for v in range(10) if deg[v] == 2]
    ok("a2a", d2 == [0, 5])
    s, essential = paths_with_essential(adjacency, 0, 5)
    ok("a2b", sorted(s) == [4, 5, 7, 8] and essential == (1 << 10) - 1)
    ok("a2c", dodge_type(sorted(s), 6) == "interior")
    ok("a2d", dodge_type(sorted(s), 14) == "short")
    ok("a2e", shape_record(sorted(s), 10)["n1_minus_hi"] == 1)
    # geometry: exactly-two, subdivision-free, no triangles in Petersen-e
    geo = member_geometry(_g6(adjacency))
    ok("a2f", geo["ndeg2"] == 2 and geo["chain_sizes"] == [1, 1])
    ok("a2g", geo["c3"] == 0 and geo["c5"] and geo["c6"])
    rg = row_geometry(geo, 0, 5)
    ok("a2h", rg["shrink"] == 0 and rg["star_simple"]
       and not rg["star_c4"] and rg["star_c8"])   # Petersen-e keeps its C8s

    # a3: the order-14 exemplar -- S = [3,13] minus {6}: interior-6, short-14
    adjacency = g6_decode(N14_G6)
    deg = degrees(adjacency)
    d2 = [v for v in range(14) if deg[v] == 2]
    ok("a3a", len(d2) >= 2)
    found = None
    for i in range(len(d2)):
        for j in range(i + 1, len(d2)):
            s, essential = paths_with_essential(adjacency, d2[i], d2[j])
            if essential == (1 << 14) - 1 and sorted(s) == \
                    [3, 4, 5, 7, 8, 9, 10, 11, 12, 13]:
                found = (d2[i], d2[j])
    ok("a3b", found is not None)
    S = [3, 4, 5, 7, 8, 9, 10, 11, 12, 13]
    ok("a3c", dodge_type(S, 6) == "interior" and dodge_type(S, 14) == "short")
    ok("a3d", shape_record(S, 14)["ham"])
    ok("a3e", shape_record(S, 14)["gaps7plus"] == [])

    # a4: chain decomposition micro-test -- 6-cycle with one chord
    # vertices 0..5 in a hexagon, chord (0,3): degree-2 set {1,2,4,5},
    # chains {1,2} and {4,5}
    hexa = census.scan.from_edges(6, [(0, 1), (1, 2), (2, 3), (3, 4),
                                      (4, 5), (5, 0), (0, 3)])
    deg = degrees(hexa)
    chains, flags = deg2_chains(hexa, deg)
    ok("a4a", sorted(sorted(c) for c in chains) == [[1, 2], [4, 5]])
    ok("a4b", not any(flags))

    # a5: smoothing micro-test -- once-subdivided K4, keep two
    # subdivision vertices as terminals
    edges = []
    base = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    nxt = 4
    subv = {}
    for (u, v) in base:
        edges += [(u, nxt), (nxt, v)]
        subv[(u, v)] = nxt
        nxt += 1
    sk4 = census.scan.from_edges(10, edges)
    a, b = subv[(0, 1)], subv[(2, 3)]
    n_star, wedges, simple, loops = smooth(sk4, {a, b})
    ok("a5a", n_star == 6 and simple and loops == 0)
    ok("a5b", sorted(w for _, _, w in wedges) == [1, 1, 1, 1, 2, 2, 2, 2])
    ok("a5c", sum(w for _, _, w in wedges) == 12)
    star_adj = smooth_simple_adjacency(n_star, wedges)
    ok("a5d", has_cycle_len(star_adj, 4))   # K4 pattern has C4s in the
    # simple part (the two weight-1 paths through a and b + weight-2 edges)

    # a6: triangle counter -- K4 has 4, Petersen-e has 0, hexagon+chord 0
    ok("a6a", triangle_count(census.scan.from_edges(4, base)) == 4)
    ok("a6b", triangle_count(petersen_minus_e()) == 0)
    ok("a6c", triangle_count(hexa) == 0)

    # a7: corpus + profile loading identities
    rows, summary = load_corpus()
    ok("a7a", len(rows) == CORPUS_TOTAL)
    profile = load_profile_rows()
    ok("a7b", len(profile) == PROFILE_TOTAL)
    n19 = [r for r in profile if r["order"] == 19]
    ok("a7c", len(n19) == 1 and n19[0]["g6"] == N19_G6)
    ok("a7d", n19[0]["S"] == list(range(5, 19)))
    # first corpus row: full re-verification
    r = rows[0]
    adjacency = g6_decode(r["g6"])
    s, essential = paths_with_essential(adjacency, *r["terminals"])
    ok("a7e", sorted(s) == r["S"]
       and (essential == (1 << r["order"]) - 1) == r["vertex_taut"])

    out = {"checks": len(checks), "names": checks,
           "interpreter": interpreter()}
    tag = "pypy" if "PyPy" in interpreter() else "cpython"
    with open(os.path.join(DATA, "anchors_dissect_%s.json" % tag), "w") as fh:
        json.dump(out, fh, indent=1)
    print("anchors: %d/%d checks passed [%s]"
          % (len(checks), len(checks), interpreter()))


def _g6(adjacency):
    """Minimal graph6 encoder for anchor use only (n <= 62)."""
    n = len(adjacency)
    bits = []
    for j in range(1, n):
        for i in range(j):
            bits.append(1 if adjacency[i] >> j & 1 else 0)
    while len(bits) % 6:
        bits.append(0)
    chars = [chr(63 + n)]
    for k in range(0, len(bits), 6):
        val = 0
        for bt in bits[k:k + 6]:
            val = val * 2 + bt
        chars.append(chr(63 + val))
    return "".join(chars)


def main():
    cmds = {"anchors": cmd_anchors, "corpus": cmd_corpus,
            "control": cmd_control, "report": cmd_report,
            "exchange": cmd_exchange}
    cmds[sys.argv[1]](sys.argv[2:])


if __name__ == "__main__":
    main()
