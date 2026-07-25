#!/usr/bin/env python3
"""E023 — T5 kill rungs and the constructive verification of the trimming
construction (P-002, session S023).

Candidate lemma T5 (A023): if (H,a,b) is vertex-taut (every vertex on a
simple a-b path), then every cycle of H is an interference cycle — the edge
symmetric difference of two simple a-b paths.

This experiment runs the two remaining pre-registered kill rungs and then
verifies, instance by instance, the two steps of the S023 trimming proof:

  Lemma A (cycle-edge essentiality): in a vertex-taut pair, every edge that
  lies on a cycle lies on a simple a-b path.

  Trimming construction: let C be a cycle, pq an edge of C, R a simple a-b
  path containing pq.  Let u be the FIRST vertex of V(C) along R and v the
  LAST (u != v because p != q both lie on R and on C).  Write R_a = R[a..u],
  R_b = R[v..b]; their interiors avoid C and they are disjoint.  Let A1, A2
  be the two u-v arcs of C.  Then P = R_a A1 R_b and Q = R_a A2 R_b are
  simple a-b paths with E(P) xor E(Q) = E(C).

Commands (run from this directory; production under pypy3, anchors under
both interpreters):
  pypy3 rungs.py anchors            # E021's 45-check suite through the import
  pypy3 rungs.py smallworld13       # kill rung 1: exhaustive in-class order 13
  pypy3 rungs.py tautcal            # calibrate the new slice loop vs E021's
                                    #   recorded tautgeneral aggregates (4-7)
  pypy3 rungs.py tautslice N MINE MAXE TAG   # kill rung 2: sparse slices
  pypy3 rungs.py constructive general 4 5 6 7
  pypy3 rungs.py constructive slice N MINE MAXE TAG
  pypy3 rungs.py constructive named # the 8 profile objects + calibration pair

Primitives are IMPORTED from E021/dissect.py (which itself imports E018's
scan.py, E018's mod4.py and E013's catalogue.py); no census / path / cycle /
tautness primitive is re-implemented here.  The only new code is the slice
driver loop (mirroring E021 cmd_tautgeneral with edge bounds) and the
constructive checker (path-order reconstruction + arc split + assertions).
All data writes are redirected to E023/data.  Deterministic; stdlib only.
"""

import importlib.util
import json
import os
import pathlib
import subprocess
import sys
import time

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
EXPS = os.path.dirname(HERE)
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
# Redirect every data write to E023/data (dissect.py pointed them at E021).
e021.DATA = DATA
e021.scan.DATA = DATA
e021.cat.DATA = pathlib.Path(DATA)
scan = e021.scan
cat = e021.cat
mod4 = e021.mod4

# Recorded E021 tautgeneral aggregates (data/tautgeneral.json; C042 lineage).
E021_TAUTGENERAL = {"orders": [4, 5, 6, 7], "pairs": 19476,
                    "taut_pairs": 12313, "cycles_tested": 723926,
                    "non_decomposable": 0}

# The order-19 exemplar (C043; unique profile member at order 19).
N19_G6 = "R???C@?GC_B?@_aAA_aP?W_?BO@Gc?"
# The order-14 full-triple calibration exemplar (A023 T7).
N14_G6 = "M?AA@?WcKWHOWOL??"


# --- kill rung 1: exhaustive in-class at order 13 -----------------------------

def cmd_smallworld13(_args):
    """E021's cmd_smallworld at order 13 (exhaustive over the profile class,
    power-freeness dropped, every cycle of every member tested).  Output is
    redirected to E023/data and renamed per-order."""
    e021.cmd_smallworld(["13"])
    src = os.path.join(DATA, "smallworld_full_spectrum.json")
    dst = os.path.join(DATA, "smallworld_n13.json")
    os.replace(src, dst)
    print("-> %s" % dst)


# --- kill rung 2: the sparse general-graph slices ------------------------------

def run_tautslice(n, mine, maxe, tag, write=True):
    """E021 cmd_tautgeneral semantics with explicit edge bounds: over the
    geng -q -c n mine:maxe stream, count vertex pairs of graphs having at
    least one cycle, restrict to vertex-taut pairs, and test every cycle of
    the graph for two-through-path decomposability."""
    t0 = time.time()
    cmd = ["geng", "-q", "-c", str(n), "%d:%d" % (mine, maxe)]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=1 << 20)
    graphs = cyclic = total_pairs = taut_pairs = cyc = bad = 0
    badex = []
    assert proc.stdout is not None
    for raw in proc.stdout:
        g6 = raw.decode().strip()
        adjacency = scan.g6_decode(g6)
        graphs += 1
        cycles = cat.all_cycles(adjacency)
        if not cycles:
            continue
        cyclic += 1
        blockers = [(m, e) for (l, m, e) in cycles]
        for a in range(n):
            for b in range(a + 1, n):
                total_pairs += 1
                s, ess = mod4.paths_with_essential(adjacency, a, b)
                if not s or ess != (1 << n) - 1:
                    continue
                taut_pairs += 1
                per, combos, n_paths, S, _ = e021.dissect_pair(
                    adjacency, a, b, blockers)
                cyc += len(per)
                nondec = [i for i, r in enumerate(per)
                          if not r["decomposable"]]
                bad += len(nondec)
                if nondec and len(badex) < 8:
                    badex.append({
                        "g6": g6, "terminals": [a, b],
                        "nondec_cycle_lengths":
                            [cycles[i][0] for i in nondec],
                        "strata": [per[i]["stratum"] for i in nondec]})
    assert proc.wait() == 0, "geng failed"
    out = {"order": n, "geng": " ".join(cmd), "graphs": graphs,
           "graphs_with_cycles": cyclic, "pairs": total_pairs,
           "taut_pairs": taut_pairs, "cycles_tested": cyc,
           "non_decomposable": bad, "counterexamples": badex,
           "seconds": round(time.time() - t0, 1),
           "interpreter": "%s %s" % (sys.implementation.name,
                                     sys.version.split()[0])}
    print("tautslice n=%d e=%d:%d graphs=%d cyclic=%d pairs=%d taut=%d "
          "cycles=%d NONDEC=%d %.1fs"
          % (n, mine, maxe, graphs, cyclic, total_pairs, taut_pairs, cyc,
             bad, out["seconds"]))
    for ex in badex:
        print("  counterexample:", ex)
    if write:
        os.makedirs(DATA, exist_ok=True)
        with open(os.path.join(DATA, "tautslice_%s.json" % tag), "w") as fh:
            json.dump(out, fh, indent=1)
    return out


def cmd_tautslice(args):
    n, mine, maxe = int(args[0]), int(args[1]), int(args[2])
    tag = args[3] if len(args) > 3 else "n%d_e%d_%d" % (n, mine, maxe)
    run_tautslice(n, mine, maxe, tag)


def cmd_tautcal(_args):
    """Calibration: the new slice loop over orders 4-7 with the full edge
    range must reproduce E021's recorded tautgeneral aggregates exactly."""
    agg = {"pairs": 0, "taut_pairs": 0, "cycles_tested": 0,
           "non_decomposable": 0}
    for n in E021_TAUTGENERAL["orders"]:
        out = run_tautslice(n, 0, n * (n - 1) // 2, "cal_n%d" % n,
                            write=False)
        for k in agg:
            agg[k] += out[k]
    for k in agg:
        assert agg[k] == E021_TAUTGENERAL[k], (k, agg[k], E021_TAUTGENERAL[k])
    print("tautcal: new slice loop reproduces E021 tautgeneral aggregates "
          "exactly: %s" % agg)
    with open(os.path.join(DATA, "tautcal.json"), "w") as fh:
        json.dump({"recorded": E021_TAUTGENERAL, "reproduced": agg,
                   "interpreter": "%s %s" % (sys.implementation.name,
                                             sys.version.split()[0])},
                  fh, indent=1)


# --- the constructive verifier ------------------------------------------------

def edge_set_to_seq(a, b, edges):
    """Reconstruct the vertex sequence of a simple a-b path from its edge
    set; every structural property of a simple path is asserted (degree-1
    endpoints, degree-2 interior, single component, no repeats)."""
    adj = {}
    for (u, v) in edges:
        adj.setdefault(u, []).append(v)
        adj.setdefault(v, []).append(u)
    assert len(adj[a]) == 1 and len(adj[b]) == 1, "endpoint degree != 1"
    for w, nb in adj.items():
        assert len(nb) == (1 if w in (a, b) else 2), "interior degree != 2"
    seq = [a]
    prev, cur = None, a
    while cur != b:
        nxt = [w for w in adj[cur] if w != prev]
        assert len(nxt) == 1, "walk ambiguity"
        prev, cur = cur, nxt[0]
        seq.append(cur)
        assert len(seq) <= len(edges) + 1, "walk exceeds edge count"
    assert len(seq) == len(edges) + 1, "edge set is not a single a-b path"
    assert len(set(seq)) == len(seq), "vertex repeat"
    return seq


def cycle_arcs(cedges, u, v):
    """Split a cycle edge set into its two u-v arcs (u != v on the cycle)."""
    adj = {}
    for (x, y) in cedges:
        adj.setdefault(x, []).append(y)
        adj.setdefault(y, []).append(x)
    assert u in adj and v in adj and u != v
    arcs = []
    for first in adj[u]:
        arc = [tuple(sorted((u, first)))]
        prev, cur = u, first
        while cur != v:
            nxt = [w for w in adj[cur] if w != prev]
            assert len(nxt) == 1
            prev, cur = cur, nxt[0]
            arc.append(tuple(sorted((prev, cur))))
        arcs.append(frozenset(arc))
    a1, a2 = arcs
    assert not (a1 & a2) and (a1 | a2) == cedges, "arc split failed"
    return a1, a2


def constructive_pair(adjacency, a, b, cycles, paths):
    """For every cycle C and EVERY edge pq of C: assert Lemma A (some a-b
    path contains pq) and run the trimming construction from the first such
    path, asserting every step.  Returns (cycle_count, edge_instances)."""
    pathsets = {e for (_, _, e) in paths}
    edge_instances = 0
    for (clen, cmask, cedges) in cycles:
        cvset = set()
        for (x, y) in cedges:
            cvset.add(x)
            cvset.add(y)
        for pq in sorted(cedges):
            edge_instances += 1
            R = None
            for (l, m, e) in paths:
                if pq in e:
                    R = e
                    break
            assert R is not None, ("LEMMA A FAILS", pq)
            seq = edge_set_to_seq(a, b, R)
            hits = [i for i, w in enumerate(seq) if w in cvset]
            assert hits, "path through a C-edge misses V(C)"
            ui, vi = hits[0], hits[-1]
            u, v = seq[ui], seq[vi]
            assert u != v, "first and last C-hits coincide"
            ra = frozenset(tuple(sorted((seq[i], seq[i + 1])))
                           for i in range(ui))
            rb = frozenset(tuple(sorted((seq[i], seq[i + 1])))
                           for i in range(vi, len(seq) - 1))
            # trimming invariants: trunk interiors avoid V(C), trunks disjoint
            assert all(w not in cvset for w in seq[:ui]), "prefix hits C"
            assert all(w not in cvset for w in seq[vi + 1:]), "suffix hits C"
            a1, a2 = cycle_arcs(cedges, u, v)
            p = ra | a1 | rb
            q = ra | a2 | rb
            seqp = edge_set_to_seq(a, b, p)
            seqq = edge_set_to_seq(a, b, q)
            assert p != q and (p ^ q) == cedges, "symmetric difference != C"
            assert p in pathsets and q in pathsets, \
                "constructed path missing from census path list"
    return len(cycles), edge_instances


def constructive_stream(n, mine, maxe, label):
    t0 = time.time()
    cmd = ["geng", "-q", "-c", str(n), "%d:%d" % (mine, maxe)]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=1 << 20)
    graphs = taut_pairs = ncycles = ninst = 0
    assert proc.stdout is not None
    for raw in proc.stdout:
        adjacency = scan.g6_decode(raw.decode())
        graphs += 1
        cycles = cat.all_cycles(adjacency)
        if not cycles:
            continue
        for a in range(n):
            for b in range(a + 1, n):
                s, ess = mod4.paths_with_essential(adjacency, a, b)
                if not s or ess != (1 << n) - 1:
                    continue
                taut_pairs += 1
                paths = cat.all_ab_paths(adjacency, a, b)
                nc, ni = constructive_pair(adjacency, a, b, cycles, paths)
                ncycles += nc
                ninst += ni
    assert proc.wait() == 0
    sec = round(time.time() - t0, 1)
    print("constructive %s: graphs=%d taut_pairs=%d cycle_instances=%d "
          "edge_instances=%d ALL PASS %.1fs"
          % (label, graphs, taut_pairs, ncycles, ninst, sec))
    return {"label": label, "geng": " ".join(cmd), "graphs": graphs,
            "taut_pairs": taut_pairs, "cycle_instances": ncycles,
            "edge_instances": ninst, "seconds": sec}


def named_objects():
    """The eight profile objects in existence (C043 + harvests), the
    order-14 full-triple exemplar (A023 T7) and Petersen-e (A021)."""
    objs = []
    pe_edges = [e for e in scan.PETERSEN_EDGES if e != (0, 1)]
    objs.append(("petersen-e", scan.from_edges(10, pe_edges), 0, 1))
    for g6 in [N14_G6, N19_G6]:
        adjacency = scan.g6_decode(g6)
        pair = scan.profile_pair(scan.degrees(adjacency))
        assert pair is not None, g6
        objs.append((g6, adjacency, pair[0], pair[1]))
    t5 = json.loads(pathlib.Path(
        E022_DIR, "data", "t5_n20_profile.json").read_text())
    assert len(t5["graphs"]) == 3
    for entry in t5["graphs"]:
        adjacency = scan.g6_decode(entry["g6"])
        a, b = entry["terminals"]
        assert scan.profile_pair(scan.degrees(adjacency)) == (a, b)
        objs.append((entry["g6"], adjacency, a, b))
    part14 = [ln.strip() for ln in pathlib.Path(
        E022_DIR, "data", "profile_n20_part14.g6").read_text().splitlines()
        if ln.strip()]
    assert len(part14) == 4
    for g6 in part14:
        adjacency = scan.g6_decode(g6)
        pair = scan.profile_pair(scan.degrees(adjacency))
        assert pair is not None, g6
        objs.append((g6, adjacency, pair[0], pair[1]))
    return objs


def cmd_constructive(args):
    mode = args[0]
    os.makedirs(DATA, exist_ok=True)
    if mode == "general":
        orders = [int(x) for x in args[1:]]
        out = [constructive_stream(n, 0, n * (n - 1) // 2, "general_n%d" % n)
               for n in orders]
        name = "constructive_general.json"
    elif mode == "slice":
        n, mine, maxe = int(args[1]), int(args[2]), int(args[3])
        tag = args[4] if len(args) > 4 else "n%d_e%d_%d" % (n, mine, maxe)
        out = [constructive_stream(n, mine, maxe, "slice_%s" % tag)]
        name = "constructive_slice_%s.json" % tag
    elif mode == "named":
        out = []
        for label, adjacency, a, b in named_objects():
            t0 = time.time()
            n = len(adjacency)
            s, ess = mod4.paths_with_essential(adjacency, a, b)
            assert s and ess == (1 << n) - 1, "named object not vertex-taut"
            cycles = cat.all_cycles(adjacency)
            paths = cat.all_ab_paths(adjacency, a, b)
            nc, ni = constructive_pair(adjacency, a, b, cycles, paths)
            sec = round(time.time() - t0, 1)
            print("constructive named %s (n=%d, terminals %d,%d): "
                  "cycles=%d edge_instances=%d ALL PASS %.1fs"
                  % (label, n, a, b, nc, ni, sec))
            out.append({"label": label, "order": n, "terminals": [a, b],
                        "cycle_instances": nc, "edge_instances": ni,
                        "seconds": sec})
        name = "constructive_named.json"
    else:
        raise SystemExit("constructive general|slice|named ...")
    with open(os.path.join(DATA, name), "w") as fh:
        json.dump({"runs": out,
                   "interpreter": "%s %s" % (sys.implementation.name,
                                             sys.version.split()[0])},
                  fh, indent=1)
    print("-> %s" % name)


def main():
    cmds = {
        "anchors": lambda a: e021.cmd_anchors(a),
        "smallworld13": cmd_smallworld13,
        "tautcal": cmd_tautcal,
        "tautslice": cmd_tautslice,
        "constructive": cmd_constructive,
    }
    if len(sys.argv) < 2 or sys.argv[1] not in cmds:
        print(__doc__)
        sys.exit(1)
    os.makedirs(DATA, exist_ok=True)
    cmds[sys.argv[1]](sys.argv[2:])


if __name__ == "__main__":
    main()
