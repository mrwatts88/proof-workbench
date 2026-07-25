#!/usr/bin/env python3
"""E021 — blocking-cycle interference dissection (P-002, session S022, worker W1).

Two families of nearest-known objects to the case-(5b) target profile
(connected, C4-free, exactly two degree-2 vertices a,b, all others >= 3,
power-free) are dissected against the pinched-world interference predicate:

  a cycle C (edge set) of (H,a,b) is a TWO-THROUGH-PATH SYMMETRIC DIFFERENCE
  iff there exist two distinct simple a-b paths P,Q of H with
  E(C) = E(P) symmetric-difference E(Q).

This is exactly the predicate of E013's recorded interference census
(catalogue.py `dissect`/`cores`: `e1 ^ e2 == edges` over
itertools.combinations(all_ab_paths(H,a,b), 2) — all cycles of the target
length counted, no terminal stratification in the predicate).  E021 adds the
stratification report: every blocker is classified as passing through BOTH
terminals / exactly ONE / NEITHER (a blocker through both decomposes
trivially into its two arcs; the informative strata are the other two).

Family (1): the minimum-C8-count members of the E018 profile class
(connected, C4-free, exactly two degree-2 vertices, rest >= 3) at orders
14/15/16 (recorded minima 1/2/1, class sizes 130,461 / 1,826,839 /
29,713,305).  E018's JSONs record only the min statistic, so the exemplars
are re-extracted here from the same stream (geng -q -c -f -d2 n mine:maxe,
mine = ceil((3n-2)/2)) with E018's anchored primitives imported from its own
scan.py; every member with C8 count <= 3 is collected.  Blockers: their C8s.

Family (2): the three-degree-2 boundary graphs of the {C4,C8}-free class at
orders 16 (4 graphs) and 17 (12 graphs), read from E019's
data/spotcheck_n16.json / spotcheck_n17.json (key `graphs`, filtered to
n_degree_2 == 3; all C8-free and C16-blocked per C039).  Blockers: their
C16s.  Three degree-2 vertices give three two-terminal readings; the
predicate is tested for ALL THREE pairs; a blocker is non-interference only
if it decomposes for NO pair.

Primitives are IMPORTED, not copied: E018/scan.py (g6_decode, degrees,
profile_pair, count_cycles_len, path_lengths, geng_args, ...; module loaded
under the name "scan" with its DATA constant redirected to E021/data before
any call), E018/mod4.py (paths_with_essential — the vertex-tautness
instrument of A021/C037), E013/catalogue.py (all_cycles, all_ab_paths,
isomorphic, ... — the census machinery itself, DATA likewise redirected).

Commands (run from this directory):
  pypy3 dissect.py anchors            # toolchain + census anchors (must pass first)
  pypy3 dissect.py extract N [r/m]    # family-(1) exemplar extraction (one part)
  pypy3 dissect.py harvest16          # merge the 24 order-16 parts, assert totals
  pypy3 dissect.py dissect            # both families: the interference dissection
Deterministic; standard library only; no randomness; wall clock used only
for timing fields.
"""

import importlib.util
import itertools
import json
import os
import pathlib
import subprocess
import sys
import time

# Import hygiene: loading E018/E013 modules must leave their directories
# untouched — no bytecode caches written into sibling experiments.
sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
PROB = os.path.dirname(os.path.dirname(HERE))  # problems/erdos-gyarfas
E018 = os.path.join(os.path.dirname(HERE),
                    "E018-order-16-g-profile-scan-stream-level-power-free-search-over")
E013 = os.path.join(os.path.dirname(HERE),
                    "E013-full-taut-pinched-catalogue-over-all-terminal-pairs-at-order")
E019 = os.path.join(os.path.dirname(HERE),
                    "E019-dedicated-c4-c8-free-generator-geng-prune-plugin-and-the-ord")


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


# E018 scan.py must be importable as "scan" for mod4.py's `from scan import ...`.
scan = _load("scan", os.path.join(E018, "scan.py"))
scan.DATA = DATA          # redirect BEFORE loading mod4 and before any call
mod4 = _load("e018_mod4", os.path.join(E018, "mod4.py"))
cat = _load("e013_catalogue", os.path.join(E013, "catalogue.py"))
cat.DATA = pathlib.Path(DATA)  # redirect (E013 uses a pathlib DATA)

# Recorded reference values (C036 / E018 README / E018 data files).
E018_STREAM = {14: 1706820, 15: 20629645, 16: 346573602}
E018_CLASS = {14: 130461, 15: 1826839, 16: 29713305}
E018_MIN_C8 = {14: 1, 15: 2, 16: 1}

# E013 data/cores.json census, quoted verbatim (the anchor targets).
E013_CORES_CENSUS = {
    0: {"c8_count": 3, "c8_as_path_symdiff": 3},
    1: {"c8_count": 3, "c8_as_path_symdiff": 3},
    2: {"c8_count": 5, "c8_as_path_symdiff": 5},
    3: {"c8_count": 7, "c8_as_path_symdiff": 7},   # Petersen-e
    4: {"c8_count": 5, "c8_as_path_symdiff": 5},
}
PETERSEN_E_CORE_INDEX = 3


# --- the dissection engine ---------------------------------------------------

def blockers_of_length(adjacency, length):
    """All simple cycles of the given length as (vertex_mask, edge_frozenset),
    via E013's enumerator (each cycle exactly once)."""
    return [(mask, edges) for (l, mask, edges) in cat.all_cycles(adjacency)
            if l == length]


def dissect_pair(adjacency, a, b, blockers):
    """The E013-semantics interference census of `blockers` for terminals
    (a,b), plus the stratification.  Returns (per_blocker list, combos dict,
    n_paths, S sorted).

    per_blocker[i]: {"stratum", "decomposable", "n_decomposing_pairs",
                     "combos": {key: count}} in the order of `blockers`.
    Cross-instrument assertions: E018 path_lengths == E013 all_ab_paths
    lengths == mod4 paths_with_essential lengths.
    """
    paths = cat.all_ab_paths(adjacency, a, b)
    lengths_013 = {l for (l, _, _) in paths}
    lengths_018 = scan.path_lengths(adjacency, a, b)
    lengths_m4, essential = mod4.paths_with_essential(adjacency, a, b)
    assert lengths_013 == lengths_018 == lengths_m4, "path-set instruments disagree"

    index = {}
    for i, (mask, edges) in enumerate(blockers):
        assert edges not in index, "duplicate cycle edge set"
        index[edges] = i
    per = [{"stratum": None, "decomposable": False,
            "n_decomposing_pairs": 0, "combos": {}} for _ in blockers]
    for i, (mask, edges) in enumerate(blockers):
        in_a = bool(mask >> a & 1)
        in_b = bool(mask >> b & 1)
        per[i]["stratum"] = ("both" if in_a and in_b
                             else "one" if in_a or in_b else "neither")
    combos_total = {}
    for (l1, m1, e1), (l2, m2, e2) in itertools.combinations(paths, 2):
        sym = e1 ^ e2
        i = index.get(frozenset(sym))
        if i is None:
            continue
        shared = len(e1 & e2)
        key = "%d+%d-2*%d" % (min(l1, l2), max(l1, l2), shared)
        per[i]["decomposable"] = True
        per[i]["n_decomposing_pairs"] += 1
        per[i]["combos"][key] = per[i]["combos"].get(key, 0) + 1
        combos_total[key] = combos_total.get(key, 0) + 1
    # Structural theorem check: a blocker through both terminals splits into
    # its two arcs, which are simple a-b paths; it must be decomposable.
    for i, rec in enumerate(per):
        if rec["stratum"] == "both":
            assert rec["decomposable"], "arc decomposition missed — engine bug"
    return per, combos_total, len(paths), sorted(lengths_013), essential


# --- anchors -----------------------------------------------------------------

def cmd_anchors(_args):
    checks = 0

    def ok(cond, label):
        nonlocal checks
        assert cond, "ANCHOR FAILED: %s" % label
        checks += 1

    # -- toolchain anchors through the E018 import ---------------------------
    pe_edges = [e for e in scan.PETERSEN_EDGES if e != (0, 1)]
    pe = scan.from_edges(10, pe_edges)
    ok(scan.profile_pair(scan.degrees(pe)) == (0, 1), "Petersen-e profile pair")
    ok(scan.path_lengths(pe, 0, 1) == {4, 5, 7, 8}, "Petersen-e S={4,5,7,8}")
    ok(scan.count_cycles_len(pe, 8) == 7, "Petersen-e has 7 C8s (C031)")
    ok(scan.cycle_spectrum_bruteforce(pe) == {5, 6, 8, 9}, "Petersen-e spectrum")
    ok(not scan.has_c4(pe), "Petersen-e C4-free")

    k33e = scan.from_edges(6, [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5),
                               (2, 3), (2, 4)])
    ok(scan.profile_pair(scan.degrees(k33e)) == (2, 5), "K33-e profile pair")
    ok(scan.path_lengths(k33e, 2, 5) == {3, 5}, "K33-e S={3,5}")

    pet = scan.from_edges(10, scan.PETERSEN_EDGES)
    ok(scan.count_cycles_len(pet, 5) == 12 and scan.count_cycles_len(pet, 6) == 10,
       "Petersen 12 pentagons / 10 hexagons")

    # mod4 tautness instrument on Petersen-e: taut (A021 T3 order-10 witness).
    s_m4, ess = mod4.paths_with_essential(pe, 0, 1)
    ok(s_m4 == {4, 5, 7, 8} and ess == (1 << 10) - 1,
       "Petersen-e vertex-taut with S={4,5,7,8} (mod4 instrument)")

    # Order-8 profile class = exactly one member, no survivor (E016 A6/E018).
    tally = scan.scan_stream(8, collect_class=True)
    ok(tally["profile"] == 1 and not tally["survivors"]
       and tally["min_c8_in_class"] == 1,
       "order-8 class: 1 member, C8-blocked with min count 1")

    # -- census anchors: reproduce E013 cores.json on all five blocks --------
    cores = json.loads((pathlib.Path(E013) / "data" / "cores.json").read_text())
    ok(cores["distinct_core_count"] == 5, "five distinct E013 cores")
    ok(cores["petersen_minus_e_core_indices"] == [PETERSEN_E_CORE_INDEX],
       "core 3 is Petersen-e")
    recorded_census = {e["core_index"]: e for e in cores["c8_census"]}
    for core in cores["cores"]:
        i = core["index"]
        adjacency = core["adjacency_rows"]
        x, y = core["terminals"]
        blockers = blockers_of_length(adjacency, 8)
        ok(len(blockers) == E013_CORES_CENSUS[i]["c8_count"],
           "core %d C8 count" % i)
        ok(scan.count_cycles_len(adjacency, 8) == len(blockers),
           "core %d: E018 counter == E013 enumerator" % i)
        per, combos, n_paths, S, _ = dissect_pair(adjacency, x, y, blockers)
        ok(sum(1 for r in per if r["decomposable"])
           == E013_CORES_CENSUS[i]["c8_as_path_symdiff"],
           "core %d decomposable count" % i)
        ok(combos == recorded_census[i]["symdiff_combos"],
           "core %d symdiff_combos exact match" % i)
        ok(S == core["S"], "core %d through-set" % i)
    # Petersen-e core independently rebuilt and matched.
    core3 = next(c for c in cores["cores"] if c["index"] == 3)
    ok(cat.isomorphic(core3["adjacency_rows"], pe), "core 3 iso Petersen-e")

    # -- C16 machinery anchor -------------------------------------------------
    c16 = scan.from_edges(16, [(i, (i + 1) % 16) for i in range(16)])
    b16 = blockers_of_length(c16, 16)
    ok(len(b16) == 1, "C16 cycle graph has one 16-cycle")
    per, combos, n_paths, S, _ = dissect_pair(c16, 0, 8, b16)
    ok(per[0]["stratum"] == "both" and per[0]["decomposable"]
       and per[0]["n_decomposing_pairs"] == 1 and S == [8],
       "C16 antipodal arcs decompose the 16-cycle")

    # One-terminal-stratum positive control: C8 with a pendant 2-path at
    # vertex 0, terminals = the pendant tip and cycle vertex 4.  The two
    # through-paths wrap opposite arcs through the attachment vertex, and
    # their symmetric difference is exactly the C8 — a one-terminal blocker
    # CAN be an interference cycle, and the engine must find it.
    tail = scan.from_edges(10, [(i, (i + 1) % 8) for i in range(8)]
                           + [(0, 8), (8, 9)])
    b8 = blockers_of_length(tail, 8)
    ok(len(b8) == 1, "tail graph has one C8")
    per, combos, n_paths, S, _ = dissect_pair(tail, 9, 4, b8)
    ok(per[0]["stratum"] == "one" and per[0]["decomposable"]
       and n_paths == 2,
       "one-terminal C8 decomposed via the attachment vertex")

    # Negative control: a C8 hanging off the through-traffic by a bridge.
    # Terminals 8,9 joined by two internally disjoint 2-paths (via 10, 11);
    # the C8 (0..7) attaches to 10 by the bridge 10-0.  Exactly two
    # through-paths exist, their symmetric difference is the C4 {8,10,9,11},
    # never the C8: the C8 must land in stratum `neither`, not decomposable.
    hung = scan.from_edges(12, [(i, (i + 1) % 8) for i in range(8)]
                           + [(8, 10), (10, 9), (8, 11), (11, 9), (10, 0)])
    b8 = blockers_of_length(hung, 8)
    ok(len(b8) == 1, "hung graph has one C8")
    per, combos, n_paths, S, _ = dissect_pair(hung, 8, 9, b8)
    ok(per[0]["stratum"] == "neither" and not per[0]["decomposable"]
       and n_paths == 2,
       "bridge-hung C8 not decomposable (negative control)")

    # Family-(2) data anchor: one spotcheck graph's recorded spectrum is
    # reproduced by the E013 enumerator (full re-check happens in `dissect`).
    spot = json.loads((pathlib.Path(E019) / "data" / "spotcheck_n16.json")
                      .read_text())
    entry = [g for g in spot["graphs"] if g["n_degree_2"] == 3][0]
    adjacency = scan.g6_decode(entry["g6"])
    spectrum = sorted({l for (l, _, _) in cat.all_cycles(adjacency)})
    ok(spectrum == entry["spectrum"], "spotcheck spectrum reproduced")

    print("anchors: all %d checks passed (%s %s)"
          % (checks, sys.implementation.name, sys.version.split()[0]))


# --- family (1): exemplar extraction -----------------------------------------

C8_COLLECT_MAX = 3


def cmd_extract(args):
    n = int(args[0])
    part = args[1] if len(args) > 1 else None
    geng_args = scan.geng_args(n, part=part)
    t0 = time.time()
    proc = subprocess.Popen(geng_args, stdout=subprocess.PIPE, bufsize=1 << 20)
    stream = 0
    profile = 0
    min_c8 = None
    hist = {}
    exemplars = []
    c8_free = []
    assert proc.stdout is not None
    for raw in proc.stdout:
        stream += 1
        line = raw.decode().strip()
        adjacency = scan.g6_decode(line)
        pair = scan.profile_pair(scan.degrees(adjacency))
        if pair is None:
            continue
        profile += 1
        c = scan.count_cycles_len(adjacency, 8)
        if c == 0:
            # would contradict C036/C027 lineage; analyse in full and flag
            c8_free.append(scan.analyse_survivor(line, adjacency)
                           if not scan.has_cycle_len(adjacency, 16)
                           else {"g6": line, "c16_blocked": True})
            continue
        if min_c8 is None or c < min_c8:
            min_c8 = c
        hist[c] = hist.get(c, 0) + 1
        if c <= C8_COLLECT_MAX:
            exemplars.append({"g6": line, "c8_count": c})
    assert proc.wait() == 0, "geng failed"
    tally = {
        "order": n,
        "part": part or "0/1",
        "geng": " ".join(geng_args),
        "stream": stream,
        "profile": profile,
        "min_c8": min_c8,
        "c8_count_hist": {str(k): v for k, v in sorted(hist.items())},
        "exemplars_le%d" % C8_COLLECT_MAX: exemplars,
        "c8_free_members": c8_free,
        "seconds": round(time.time() - t0, 1),
        "interpreter": "%s %s" % (sys.implementation.name,
                                  sys.version.split()[0]),
    }
    if part is None:
        assert stream == E018_STREAM[n], (stream, E018_STREAM[n])
        assert profile == E018_CLASS[n], (profile, E018_CLASS[n])
        assert min_c8 == E018_MIN_C8[n], (min_c8, E018_MIN_C8[n])
        assert not c8_free, "C8-FREE PROFILE MEMBER — contradicts C036 lineage"
        name = "extract_n%d.json" % n
    else:
        name = "extract_n%d_part%s.json" % (n, part.replace("/", "of"))
    os.makedirs(DATA, exist_ok=True)
    with open(os.path.join(DATA, name), "w") as fh:
        json.dump(tally, fh, indent=1)
    print("n=%d part=%s stream=%d profile=%d min_c8=%s exemplars<=%d: %d "
          "c8free=%d %.1fs -> %s"
          % (n, tally["part"], stream, profile, min_c8, C8_COLLECT_MAX,
             len(exemplars), len(c8_free), tally["seconds"], name))
    if c8_free:
        print(json.dumps(c8_free, indent=2))
        print("*** C8-FREE PROFILE MEMBER AT ORDER %d — REPORT UPWARD ***" % n)


def cmd_harvest16(_args):
    total_stream = 0
    total_profile = 0
    min_c8 = None
    hist = {}
    exemplars = []
    c8_free = []
    seconds = 0.0
    for r in range(24):
        path = os.path.join(DATA, "extract_n16_part%dof24.json" % r)
        assert os.path.exists(path), "missing part %d/24" % r
        with open(path) as fh:
            tally = json.load(fh)
        assert tally["order"] == 16 and tally["part"] == "%d/24" % r
        total_stream += tally["stream"]
        total_profile += tally["profile"]
        if tally["min_c8"] is not None:
            if min_c8 is None or tally["min_c8"] < min_c8:
                min_c8 = tally["min_c8"]
        for k, v in tally["c8_count_hist"].items():
            hist[int(k)] = hist.get(int(k), 0) + v
        exemplars.extend(tally["exemplars_le%d" % C8_COLLECT_MAX])
        c8_free.extend(tally["c8_free_members"])
        seconds += tally["seconds"]
    assert total_stream == E018_STREAM[16], (total_stream, E018_STREAM[16])
    assert total_profile == E018_CLASS[16], (total_profile, E018_CLASS[16])
    assert min_c8 == E018_MIN_C8[16], (min_c8, E018_MIN_C8[16])
    assert sum(hist.values()) + len(c8_free) == total_profile
    assert not c8_free, "C8-FREE PROFILE MEMBER — contradicts C036"
    result = {
        "order": 16,
        "parts": 24,
        "geng": " ".join(scan.geng_args(16, part="r/24")),
        "stream": total_stream,
        "profile": total_profile,
        "min_c8": min_c8,
        "c8_count_hist_low": {str(k): hist[k] for k in sorted(hist) if k <= 12},
        "exemplars_le%d" % C8_COLLECT_MAX: exemplars,
        "c8_free_members": c8_free,
        "cpu_seconds_sum": round(seconds, 1),
    }
    with open(os.path.join(DATA, "extract_n16.json"), "w") as fh:
        json.dump(result, fh, indent=1)
    print("harvest16: stream=%d profile=%d min_c8=%d exemplars<=%d: %d "
          "cpu=%.1fs" % (total_stream, total_profile, min_c8, C8_COLLECT_MAX,
                         len(exemplars), seconds))


# --- the dissection ----------------------------------------------------------

def family1_dissect():
    reports = []
    for n in (14, 15, 16):
        path = os.path.join(DATA, "extract_n%d.json" % n)
        with open(path) as fh:
            tally = json.load(fh)
        for entry in tally["exemplars_le%d" % C8_COLLECT_MAX]:
            g6 = entry["g6"]
            adjacency = scan.g6_decode(g6)
            deg = scan.degrees(adjacency)
            pair = scan.profile_pair(deg)
            assert pair is not None
            a, b = pair
            assert not scan.has_c4(adjacency)
            blockers = blockers_of_length(adjacency, 8)
            assert len(blockers) == entry["c8_count"], "count mismatch"
            assert scan.count_cycles_len(adjacency, 8) == len(blockers)
            per, combos, n_paths, S, essential = dissect_pair(
                adjacency, a, b, blockers)
            n_vertices = len(adjacency)
            taut = essential == (1 << n_vertices) - 1
            spectrum = sorted({l for (l, _, _) in cat.all_cycles(adjacency)})
            s_set = set(S)
            strata = {"both": 0, "one": 0, "neither": 0}
            strata_dec = {"both": 0, "one": 0, "neither": 0}
            for rec, (mask, edges) in zip(per, blockers):
                strata[rec["stratum"]] += 1
                if rec["decomposable"]:
                    strata_dec[rec["stratum"]] += 1
            reports.append({
                "family": 1, "order": n, "g6": g6,
                "terminals": [a, b], "edges": sum(deg) // 2,
                "c8_count": len(blockers),
                "S": S, "spectrum": spectrum,
                "n_through_paths": n_paths,
                "vertex_taut": taut,
                "two_connected": not scan.cut_vertices(adjacency),
                "bipartite": scan.bipartition(adjacency) is not None,
                "S_meets_P": sorted(s_set & scan.P_SET),
                "S_meets_P_minus_1": sorted(s_set & scan.P_MINUS_1),
                "S_hits_P_minus_2": sorted(s_set & scan.P_MINUS_2),
                "blockers": [
                    {"vertices": [v for v in range(n_vertices)
                                  if mask >> v & 1],
                     "stratum": rec["stratum"],
                     "decomposable": rec["decomposable"],
                     "n_decomposing_pairs": rec["n_decomposing_pairs"],
                     "combos": rec["combos"]}
                    for rec, (mask, edges) in zip(per, blockers)],
                "strata_totals": strata,
                "strata_decomposable": strata_dec,
                "all_blockers_decomposable":
                    all(r["decomposable"] for r in per),
            })
    return reports


def family2_dissect():
    reports = []
    for n in (16, 17):
        path = pathlib.Path(E019) / "data" / ("spotcheck_n%d.json" % n)
        spot = json.loads(path.read_text())
        boundary = [g for g in spot["graphs"] if g["n_degree_2"] == 3]
        expected = {16: 4, 17: 12}[n]
        assert len(boundary) == expected, (n, len(boundary))
        for entry in boundary:
            g6 = entry["g6"]
            adjacency = scan.g6_decode(g6)
            deg = scan.degrees(adjacency)
            deg2 = [v for v in range(n) if deg[v] == 2]
            assert len(deg2) == 3 and min(deg) == 2
            assert all(d >= 3 for v, d in enumerate(deg) if v not in deg2)
            assert not scan.has_c4(adjacency)
            cycles = cat.all_cycles(adjacency)
            spectrum = sorted({l for (l, _, _) in cycles})
            assert spectrum == entry["spectrum"], "spectrum mismatch vs E019"
            assert 4 not in spectrum and 8 not in spectrum and 16 in spectrum
            blockers = [(mask, edges) for (l, mask, edges) in cycles
                        if l == 16]
            assert scan.count_cycles_len(adjacency, 16) == len(blockers)
            pair_results = {}
            per_by_pair = {}
            for a, b in itertools.combinations(deg2, 2):
                per, combos, n_paths, S, essential = dissect_pair(
                    adjacency, a, b, blockers)
                taut = essential == (1 << n) - 1
                key = "%d,%d" % (a, b)
                per_by_pair[key] = per
                pair_results[key] = {
                    "terminals": [a, b],
                    "n_through_paths": n_paths,
                    "S": S,
                    "vertex_taut": taut,
                    "decomposable_per_blocker":
                        [r["decomposable"] for r in per],
                    "stratum_per_blocker": [r["stratum"] for r in per],
                    "n_decomposing_pairs":
                        [r["n_decomposing_pairs"] for r in per],
                }
            n_blockers = len(blockers)
            any_pair = [any(pair_results[k]["decomposable_per_blocker"][i]
                            for k in pair_results) for i in range(n_blockers)]
            reports.append({
                "family": 2, "order": n, "g6": g6,
                "degree_2_vertices": deg2, "edges": sum(deg) // 2,
                "c16_count": n_blockers,
                "spectrum": spectrum,
                "two_connected": not scan.cut_vertices(adjacency),
                "bipartite": scan.bipartition(adjacency) is not None,
                "blocker_vertices": [[v for v in range(n) if mask >> v & 1]
                                     for (mask, edges) in blockers],
                "per_pair": pair_results,
                "decomposable_for_some_pair": any_pair,
                "all_blockers_decomposable_some_pair": all(any_pair),
            })
    return reports


def family0_dissect():
    """Calibration family: the five E013 equality blocks (P10 = Petersen-e,
    A11, B11, C12, D14), re-dissected with the same engine so their strata
    are recorded alongside the new families (the census itself is re-proved
    in `anchors`)."""
    cores = json.loads((pathlib.Path(E013) / "data" / "cores.json").read_text())
    names = {0: "A11", 1: "B11", 2: "C12", 3: "P10-Petersen-e", 4: "D14"}
    reports = []
    for core in cores["cores"]:
        i = core["index"]
        adjacency = core["adjacency_rows"]
        x, y = core["terminals"]
        blockers = blockers_of_length(adjacency, 8)
        per, combos, n_paths, S, essential = dissect_pair(
            adjacency, x, y, blockers)
        n_vertices = len(adjacency)
        strata = {"both": 0, "one": 0, "neither": 0}
        strata_dec = {"both": 0, "one": 0, "neither": 0}
        for rec in per:
            strata[rec["stratum"]] += 1
            strata_dec[rec["stratum"]] += rec["decomposable"]
        reports.append({
            "family": 0, "block": names[i], "order": n_vertices,
            "terminals": [x, y], "c8_count": len(blockers), "S": S,
            "vertex_taut": essential == (1 << n_vertices) - 1,
            "n_through_paths": n_paths,
            "blockers": [
                {"vertices": [v for v in range(n_vertices) if mask >> v & 1],
                 "stratum": rec["stratum"],
                 "decomposable": rec["decomposable"],
                 "n_decomposing_pairs": rec["n_decomposing_pairs"]}
                for rec, (mask, edges) in zip(per, blockers)],
            "strata_totals": strata,
            "strata_decomposable": strata_dec,
            "all_blockers_decomposable": all(r["decomposable"] for r in per),
        })
    return reports


def cmd_dissect(_args):
    t0 = time.time()
    fam0 = family0_dissect()
    fam1 = family1_dissect()
    t1 = time.time()
    fam2 = family2_dissect()
    t2 = time.time()
    os.makedirs(DATA, exist_ok=True)
    meta = {"interpreter": "%s %s" % (sys.implementation.name,
                                      sys.version.split()[0]),
            "family1_seconds": round(t1 - t0, 1),
            "family2_seconds": round(t2 - t1, 1)}
    with open(os.path.join(DATA, "interference_family0.json"), "w") as fh:
        json.dump({"meta": meta, "graphs": fam0}, fh, indent=1)
    with open(os.path.join(DATA, "interference_family1.json"), "w") as fh:
        json.dump({"meta": meta, "graphs": fam1}, fh, indent=1)
    with open(os.path.join(DATA, "interference_family2.json"), "w") as fh:
        json.dump({"meta": meta, "graphs": fam2}, fh, indent=1)
    print("== family (0): the five E013 equality blocks (calibration) ==")
    for r in fam0:
        print(" %s order %d C8s=%d taut=%s strata tot/dec: both %d/%d "
              "one %d/%d neither %d/%d all-dec=%s"
              % (r["block"], r["order"], r["c8_count"], r["vertex_taut"],
                 r["strata_totals"]["both"], r["strata_decomposable"]["both"],
                 r["strata_totals"]["one"], r["strata_decomposable"]["one"],
                 r["strata_totals"]["neither"],
                 r["strata_decomposable"]["neither"],
                 r["all_blockers_decomposable"]))

    # -- summary tables -------------------------------------------------------
    print("== family (1): min-C8 exemplars (blockers = C8s) ==")
    for n in (14, 15, 16):
        rows = [r for r in fam1 if r["order"] == n]
        strata = {"both": [0, 0], "one": [0, 0], "neither": [0, 0]}
        for r in rows:
            for rec in r["blockers"]:
                strata[rec["stratum"]][0] += 1
                strata[rec["stratum"]][1] += rec["decomposable"]
        taut_count = sum(r["vertex_taut"] for r in rows)
        bad = [r for r in rows if not r["all_blockers_decomposable"]]
        print(" order %d: %d exemplars (C8<=%d), taut %d/%d; "
              "strata tot/dec: both %d/%d one %d/%d neither %d/%d; "
              "non-interference graphs: %d"
              % (n, len(rows), C8_COLLECT_MAX, taut_count, len(rows),
                 strata["both"][0], strata["both"][1],
                 strata["one"][0], strata["one"][1],
                 strata["neither"][0], strata["neither"][1], len(bad)))
        for r in bad:
            print("   NON-INTERFERENCE: %s terminals=%s" %
                  (r["g6"], r["terminals"]))
            for rec in r["blockers"]:
                print("     C8 %s stratum=%s decomposable=%s"
                      % (rec["vertices"], rec["stratum"],
                         rec["decomposable"]))
    print("== family (2): three-degree-2 boundary graphs (blockers = C16s) ==")
    for n in (16, 17):
        rows = [r for r in fam2 if r["order"] == n]
        total = sum(r["c16_count"] for r in rows)
        allpair = sum(sum(r["decomposable_for_some_pair"]) for r in rows)
        bad = [r for r in rows if not r["all_blockers_decomposable_some_pair"]]
        print(" order %d: %d graphs, %d C16 blockers, decomposable for some "
              "pair: %d, non-interference graphs: %d"
              % (n, len(rows), total, allpair, len(bad)))
        for r in rows:
            per_pair = " | ".join(
                "%s: %s" % (k, "".join(
                    "Y" if x else "N"
                    for x in v["decomposable_per_blocker"]))
                for k, v in sorted(r["per_pair"].items()))
            print("   %s deg2=%s C16s=%d  [%s]"
                  % (r["g6"], r["degree_2_vertices"], r["c16_count"],
                     per_pair))
        for r in bad:
            print("   NON-INTERFERENCE (no pair decomposes some blocker): %s"
                  % r["g6"])


def cmd_smallworld(args):
    """Supplementary probe for the candidate-lemma direction: over the FULL
    exactly-two-degree-2 profile class at small orders (power-freeness
    dropped, the E016-A6/mod4 world), is EVERY cycle of EVERY vertex-taut
    member a two-through-path symmetric difference — or is the interference
    property special to the C8s of the min-C8 exemplars?  Tabulates, per
    order: taut members, cycles tested, non-decomposable cycles by stratum,
    and the count of taut members with at least one non-interference cycle.
    Also tallies the same for the non-taut members (control)."""
    orders = [int(x) for x in args] or [10, 11, 12]
    out = {}
    for n in orders:
        t0 = time.time()
        proc = subprocess.Popen(scan.geng_args(n), stdout=subprocess.PIPE,
                                bufsize=1 << 20)
        stats = {
            "class": 0, "taut": 0,
            "taut_cycles": 0, "taut_cycles_nondec": 0,
            "taut_nondec_by_stratum": {"both": 0, "one": 0, "neither": 0},
            "taut_members_with_nondec": 0,
            "nontaut_cycles": 0, "nontaut_cycles_nondec": 0,
            "nontaut_members_with_nondec": 0,
            "taut_nondec_examples": [],
        }
        assert proc.stdout is not None
        for raw in proc.stdout:
            line = raw.decode().strip()
            adjacency = scan.g6_decode(line)
            pair = scan.profile_pair(scan.degrees(adjacency))
            if pair is None:
                continue
            stats["class"] += 1
            a, b = pair
            cycles = cat.all_cycles(adjacency)
            blockers = [(mask, edges) for (l, mask, edges) in cycles]
            per, combos, n_paths, S, essential = dissect_pair(
                adjacency, a, b, blockers)
            taut = essential == (1 << n) - 1
            nondec = [i for i, r in enumerate(per) if not r["decomposable"]]
            if taut:
                stats["taut"] += 1
                stats["taut_cycles"] += len(blockers)
                stats["taut_cycles_nondec"] += len(nondec)
                for i in nondec:
                    stats["taut_nondec_by_stratum"][per[i]["stratum"]] += 1
                if nondec:
                    stats["taut_members_with_nondec"] += 1
                    if len(stats["taut_nondec_examples"]) < 8:
                        stats["taut_nondec_examples"].append({
                            "g6": line, "terminals": [a, b],
                            "nondec_cycle_lengths":
                                [cycles[i][0] for i in nondec],
                            "strata": [per[i]["stratum"] for i in nondec],
                        })
            else:
                stats["nontaut_cycles"] += len(blockers)
                stats["nontaut_cycles_nondec"] += len(nondec)
                if nondec:
                    stats["nontaut_members_with_nondec"] += 1
        assert proc.wait() == 0
        stats["seconds"] = round(time.time() - t0, 1)
        out[n] = stats
        print("n=%d class=%d taut=%d | taut cycles %d nondec %d "
              "(both %d / one %d / neither %d) in %d members | "
              "nontaut cycles %d nondec %d in %d members | %.1fs"
              % (n, stats["class"], stats["taut"], stats["taut_cycles"],
                 stats["taut_cycles_nondec"],
                 stats["taut_nondec_by_stratum"]["both"],
                 stats["taut_nondec_by_stratum"]["one"],
                 stats["taut_nondec_by_stratum"]["neither"],
                 stats["taut_members_with_nondec"],
                 stats["nontaut_cycles"], stats["nontaut_cycles_nondec"],
                 stats["nontaut_members_with_nondec"], stats["seconds"]))
    os.makedirs(DATA, exist_ok=True)
    with open(os.path.join(DATA, "smallworld_full_spectrum.json"), "w") as fh:
        json.dump({"interpreter": "%s %s" % (sys.implementation.name,
                                             sys.version.split()[0]),
                   "orders": {str(k): v for k, v in out.items()}}, fh,
                  indent=1)


def cmd_tautgeneral(args):
    """Hypothesis probe for the candidate lemma: over ALL connected graphs of
    orders 4-7 (geng -c n; no degree condition, no C4-freeness) and ALL
    vertex pairs, restrict to VERTEX-TAUT pairs (every vertex on some simple
    a-b path) and test whether every cycle is a two-through-path symmetric
    difference.  Zero failures would indicate the property rests on
    tautness alone; any failure exhibits the needed side conditions.
    Orders above 7 are omitted: dense graphs make all-pairs path-pair
    enumeration infeasible, and the probe is a hypothesis-shaping datum,
    not a census."""
    orders = [int(x) for x in args] or [4, 5, 6, 7]
    total_pairs = taut_pairs = cyc = bad = 0
    badex = []
    for n in orders:
        proc = subprocess.Popen(["geng", "-q", "-c", str(n)],
                                stdout=subprocess.PIPE)
        assert proc.stdout is not None
        for raw in proc.stdout:
            adjacency = scan.g6_decode(raw.decode())
            cycles = cat.all_cycles(adjacency)
            if not cycles:
                continue
            blockers = [(m, e) for (l, m, e) in cycles]
            for a in range(n):
                for b in range(a + 1, n):
                    total_pairs += 1
                    s, ess = mod4.paths_with_essential(adjacency, a, b)
                    if not s or ess != (1 << n) - 1:
                        continue
                    taut_pairs += 1
                    per, combos, n_paths, S, _ = dissect_pair(
                        adjacency, a, b, blockers)
                    cyc += len(per)
                    nondec = [i for i, r in enumerate(per)
                              if not r["decomposable"]]
                    bad += len(nondec)
                    if nondec and len(badex) < 8:
                        badex.append({
                            "g6": raw.decode().strip(), "terminals": [a, b],
                            "nondec_cycle_lengths":
                                [cycles[i][0] for i in nondec],
                            "strata": [per[i]["stratum"] for i in nondec]})
        assert proc.wait() == 0
    print("tautgeneral orders %s: pairs %d, taut pairs %d, cycles tested %d, "
          "NON-decomposable %d" % (orders, total_pairs, taut_pairs, cyc, bad))
    for e in badex:
        print("  counterexample:", e)
    os.makedirs(DATA, exist_ok=True)
    with open(os.path.join(DATA, "tautgeneral.json"), "w") as fh:
        json.dump({"orders": orders, "pairs": total_pairs,
                   "taut_pairs": taut_pairs, "cycles_tested": cyc,
                   "non_decomposable": bad, "counterexamples": badex,
                   "interpreter": "%s %s" % (sys.implementation.name,
                                             sys.version.split()[0])},
                  fh, indent=1)


def main():
    cmds = {
        "anchors": cmd_anchors,
        "extract": cmd_extract,
        "harvest16": cmd_harvest16,
        "dissect": cmd_dissect,
        "smallworld": cmd_smallworld,
        "tautgeneral": cmd_tautgeneral,
    }
    if len(sys.argv) < 2 or sys.argv[1] not in cmds:
        print(__doc__)
        sys.exit(1)
    cmds[sys.argv[1]](sys.argv[2:])


if __name__ == "__main__":
    main()
