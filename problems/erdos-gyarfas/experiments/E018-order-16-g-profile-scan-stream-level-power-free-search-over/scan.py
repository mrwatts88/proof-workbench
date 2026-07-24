#!/usr/bin/env python3
"""E018 — the order-16 G-profile scan (P-002, session S020).

Target class (the class G of L039 / A019 W1-T3, graph part):
    connected, C4-free, exactly two vertices of degree 2, all others >= 3,
    power-free (no C4/C8/C16 at order <= 16).
For each power-free survivor, the terminal pair (a, b) is the unique pair of
degree-2 vertices and the through-set S = S(H, a, b) (all simple a-b path
lengths) decides G-membership: S ∩ {2, 6, 14} = ∅ (the elements of P-2
reachable at these orders).

Verdicts (L039/L041):
  - a survivor with the S-condition is a member of G: its 2-path closure is a
    tight 1-atom of order n+1 and STATEMENT 0.1 IS FALSE (L025 R4) — the
    disproof protocol applies;
  - an empty scan at order 16 lifts the tight-1-atom order bound from >= 17
    to >= 18 (L041's case (5) then needs |V(H)| >= 17; cases (2)/(4) already
    give >= 39 / >= 20).

Generation: nauty geng, exactly as anchored in E010-E016:
    geng -q -c -f -d2 n mine:maxe [res/mod]
with mine = ceil((3n-2)/2)  (degree sum >= 4 + 3(n-2))
and  maxe = C(n,2)          (coverage-safe; the Reiman bound predicts no
                             C4-free graph above n(1+sqrt(4n-3))/4 edges —
                             35 at n=16 — and the scan records the maximum
                             edge count actually seen as a check).

Filter chain per stream graph (cheapest first):
    degree profile (exactly two 2s, rest >=3)  ->  C8-free  ->  C16-free
    (C4-freeness is geng's -f, anchored; survivors are re-checked in full).

Graph primitives are copied verbatim from E015/bipscan.py (anchored there and
in E012/E010 against independent pipelines and known spectra); path_lengths
follows E016/verify.py's enumerator, rewritten on bitmasks and re-anchored
here against the recorded S-sets of K_{3,3}-e and Petersen-e.

Commands:
    python3 scan.py anchors                    # fixed anchors + primitives
    python3 scan.py calibrate 8 9 10 11 12 13  # class counts vs E016 A6
    python3 scan.py run N [r/m]                # one production part
    python3 scan.py harvest N m                # merge parts, assert coverage
Deterministic; no randomness; integers and integer bitmasks only.
"""

import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
GENG = "geng"

# --- primitives copied verbatim from E015/bipscan.py ------------------------
# (anchored there against the independent E010 pipeline and known spectra)


def g6_decode(text):
    data = [ord(c) - 63 for c in text.strip()]
    assert data and 0 <= min(data) and max(data) <= 63
    n = data[0]
    assert n < 63, "long-form graph6 not needed here"
    bits = []
    for value in data[1:]:
        bits.extend((value >> shift) & 1 for shift in range(5, -1, -1))
    need = n * (n - 1) // 2
    assert len(bits) >= need and not any(bits[need:])
    adjacency = [0] * n
    k = 0
    for j in range(1, n):
        for i in range(j):
            if bits[k]:
                adjacency[i] |= 1 << j
                adjacency[j] |= 1 << i
            k += 1
    return adjacency


def degrees(adjacency):
    return [row.bit_count() for row in adjacency]


def has_c4(adjacency):
    n = len(adjacency)
    for u in range(n):
        for v in range(u + 1, n):
            if (adjacency[u] & adjacency[v]).bit_count() >= 2:
                return True
    return False


def from_edges(n, edges):
    adjacency = [0] * n
    for u, v in edges:
        assert u != v and not adjacency[u] >> v & 1
        adjacency[u] |= 1 << v
        adjacency[v] |= 1 << u
    return adjacency


def bipartition(adjacency):
    n = len(adjacency)
    colour = [-1] * n
    masks = [0, 0]
    for root in range(n):
        if colour[root] != -1:
            continue
        colour[root] = 0
        masks[0] |= 1 << root
        stack = [root]
        while stack:
            u = stack.pop()
            row = adjacency[u]
            while row:
                low = row & -row
                v = low.bit_length() - 1
                row ^= low
                if colour[v] == -1:
                    colour[v] = 1 - colour[u]
                    masks[colour[v]] |= 1 << v
                    stack.append(v)
                elif colour[v] == colour[u]:
                    return None
    return masks[0], masks[1]


def bfs_dist(adjacency, source, allowed):
    n = len(adjacency)
    dist = [n + 1] * n
    dist[source] = 0
    frontier = 1 << source
    seen = frontier
    d = 0
    while frontier:
        d += 1
        nxt = 0
        row = frontier
        while row:
            low = row & -row
            u = low.bit_length() - 1
            row ^= low
            nxt |= adjacency[u] & allowed & ~seen
        seen |= nxt
        frontier = nxt
        rem = nxt
        while rem:
            low = rem & -rem
            rem ^= low
            dist[low.bit_length() - 1] = d
    return dist


def has_cycle_len(adjacency, length):
    n = len(adjacency)
    if length < 3 or length > n:
        return False
    full = (1 << n) - 1
    for s in range(n - length + 1):
        allowed = full & ~((1 << s) - 1)
        dist = bfs_dist(adjacency, s, allowed)
        nbrs_s = adjacency[s] & allowed
        row = nbrs_s
        while row:
            low = row & -row
            u = low.bit_length() - 1
            row ^= low
            if dist[u] > length - 1:
                continue
            targets = nbrs_s & ~((1 << (u + 1)) - 1)
            if not targets:
                continue
            stack = [(u, (1 << s) | (1 << u), 1)]
            while stack:
                v, used, k = stack.pop()
                if k == length - 1:
                    if (1 << v) & targets:
                        return True
                    continue
                remaining = length - 1 - k
                row2 = adjacency[v] & allowed & ~used
                while row2:
                    low2 = row2 & -row2
                    w = low2.bit_length() - 1
                    row2 ^= low2
                    if dist[w] <= remaining + 1 and remaining >= 1:
                        stack.append((w, used | low2, k + 1))
    return False


def count_cycles_len(adjacency, length):
    n = len(adjacency)
    if length < 3 or length > n:
        return 0
    full = (1 << n) - 1
    total = 0
    for s in range(n - length + 1):
        allowed = full & ~((1 << s) - 1)
        dist = bfs_dist(adjacency, s, allowed)
        nbrs_s = adjacency[s] & allowed
        row = nbrs_s
        while row:
            low = row & -row
            u = low.bit_length() - 1
            row ^= low
            if dist[u] > length - 1:
                continue
            targets = nbrs_s & ~((1 << (u + 1)) - 1)
            if not targets:
                continue
            stack = [(u, (1 << s) | (1 << u), 1)]
            while stack:
                v, used, k = stack.pop()
                if k == length - 1:
                    if (1 << v) & targets:
                        total += 1
                    continue
                remaining = length - 1 - k
                row2 = adjacency[v] & allowed & ~used
                while row2:
                    low2 = row2 & -row2
                    w = low2.bit_length() - 1
                    row2 ^= low2
                    if dist[w] <= remaining + 1 and remaining >= 1:
                        stack.append((w, used | low2, k + 1))
    return total


def cycle_spectrum_bruteforce(adjacency):
    n = len(adjacency)
    full = (1 << n) - 1
    lengths = set()
    for s in range(n):
        allowed = full & ~((1 << s) - 1)
        stack = [(s, 1 << s, 0, -1)]
        while stack:
            v, used, k, first = stack.pop()
            row = adjacency[v] & allowed & ~used
            while row:
                low = row & -row
                w = low.bit_length() - 1
                row ^= low
                if k == 0:
                    stack.append((w, used | low, 1, w))
                else:
                    stack.append((w, used | low, k + 1, first))
            if k >= 2 and (adjacency[v] >> s) & 1:
                last = v
                if first < last:
                    lengths.add(k + 1)
    return lengths


def power_lengths(n):
    out = []
    k = 2
    while 2 ** k <= n:
        out.append(2 ** k)
        k += 1
    return out


def power_free(adjacency):
    present = [L for L in power_lengths(len(adjacency)) if has_cycle_len(adjacency, L)]
    return (not present), present


# --- new machinery for E018 --------------------------------------------------


def path_lengths(adjacency, a, b):
    """Exact set of lengths (in edges) of simple a-b paths (bitmask DFS).

    Iterative counterpart of E016/verify.py path_lengths; anchored below
    against the recorded S-sets of K_{3,3}-e ({3,5}) and Petersen-e
    ({4,5,7,8}).
    """
    assert a != b
    out = set()
    target = 1 << b
    stack = [(a, 1 << a, 0)]
    while stack:
        v, used, length = stack.pop()
        row = adjacency[v] & ~used
        if row & target:
            out.add(length + 1)
        row &= ~target
        while row:
            low = row & -row
            w = low.bit_length() - 1
            row ^= low
            stack.append((w, used | low, length + 1))
    return out


def cut_vertices(adjacency):
    """Vertices whose deletion disconnects the graph (input assumed connected)."""
    n = len(adjacency)
    full = (1 << n) - 1
    cuts = []
    for v in range(n):
        allowed = full & ~(1 << v)
        root = 0 if v != 0 else 1
        dist = bfs_dist(adjacency, root, allowed)
        if any(dist[w] > n for w in range(n) if w != v):
            cuts.append(v)
    return cuts


def profile_pair(deg):
    """The two degree-2 vertices if the profile is (exactly two 2s, rest >=3);
    otherwise None."""
    a = b = -1
    for v, d in enumerate(deg):
        if d == 2:
            if a == -1:
                a = v
            elif b == -1:
                b = v
            else:
                return None
        elif d < 2:
            return None
    if b == -1:
        return None
    return a, b


P_SET = frozenset({4, 8, 16, 32, 64})          # powers 2^k, k>=2, up to order 64
P_MINUS_1 = frozenset({3, 7, 15, 31, 63})      # Mersenne lengths
P_MINUS_2 = frozenset({2, 6, 14, 30, 62})      # forbidden through-lengths


def analyse_survivor(g6, adjacency):
    """Full report on a power-free profile member (expected to be rare)."""
    deg = degrees(adjacency)
    pair = profile_pair(deg)
    assert pair is not None
    a, b = pair
    is_pf, present = power_free(adjacency)
    assert is_pf and not present and not has_c4(adjacency)
    spec = sorted(cycle_spectrum_bruteforce(adjacency))
    s_set = sorted(path_lengths(adjacency, a, b))
    s = set(s_set)
    return {
        "g6": g6,
        "n": len(adjacency),
        "edges": sum(deg) // 2,
        "degree_2_pair": [a, b],
        "spectrum": spec,
        "S": s_set,
        "S_hits_P_minus_2": sorted(s & P_MINUS_2),
        "in_G": not (s & P_MINUS_2),
        "S_meets_P": sorted(s & P_SET),
        "S_meets_P_minus_1": sorted(s & P_MINUS_1),
        "bipartite": bipartition(adjacency) is not None,
        "cut_vertices": cut_vertices(adjacency),
        "ab_adjacent": bool(adjacency[a] >> b & 1),
    }


def geng_args(n, mine=None, maxe=None, part=None):
    if mine is None:
        mine = (3 * n - 2 + 1) // 2  # ceil((3n-2)/2)
    if maxe is None:
        maxe = n * (n - 1) // 2
    args = [GENG, "-q", "-c", "-f", "-d2", str(n), "%d:%d" % (mine, maxe)]
    if part is not None:
        args.append(part)
    return args


def scan_stream(n, part=None, collect_class=False):
    """Run geng and the filter chain; return the tally dictionary.

    collect_class: additionally count C8s per profile member (calibration
    orders only; too expensive at order 16 and not needed there).
    """
    args = geng_args(n, part=part)
    t0 = time.time()
    proc = subprocess.Popen(args, stdout=subprocess.PIPE, bufsize=1 << 20)
    stream = 0
    profile = 0
    c8_blocked = 0
    c16_blocked = 0
    survivors = []
    max_edges_seen = 0
    min_c8 = None
    assert proc.stdout is not None
    for raw in proc.stdout:
        stream += 1
        line = raw.decode().strip()
        adjacency = g6_decode(line)
        deg = degrees(adjacency)
        pair = profile_pair(deg)
        if pair is None:
            continue
        profile += 1
        e = sum(deg) // 2
        if e > max_edges_seen:
            max_edges_seen = e
        if collect_class:
            c8s = count_cycles_len(adjacency, 8)
            if c8s:
                c8_blocked += 1
                if min_c8 is None or c8s < min_c8:
                    min_c8 = c8s
            elif n >= 16 and has_cycle_len(adjacency, 16):
                c16_blocked += 1
            else:
                survivors.append(analyse_survivor(line, adjacency))
        else:
            if has_cycle_len(adjacency, 8):
                c8_blocked += 1
            elif n >= 16 and has_cycle_len(adjacency, 16):
                c16_blocked += 1
            else:
                survivors.append(analyse_survivor(line, adjacency))
    code = proc.wait()
    assert code == 0, "geng exited with %r" % code
    return {
        "order": n,
        "part": part or "0/1",
        "geng": " ".join(args),
        "stream": stream,
        "profile": profile,
        "c8_blocked": c8_blocked,
        "c16_blocked": c16_blocked,
        "survivors": survivors,
        "max_edges_seen": max_edges_seen,
        "min_c8_in_class": min_c8,
        "seconds": round(time.time() - t0, 1),
        "interpreter": sys.version.split()[0]
        + ("/PyPy" if hasattr(sys, "pypy_version_info") else "/CPython"),
    }


# --- anchors -----------------------------------------------------------------

PETERSEN_EDGES = [
    (0, 1), (1, 2), (2, 3), (3, 4), (4, 0),
    (5, 7), (7, 9), (9, 6), (6, 8), (8, 5),
    (0, 5), (1, 6), (2, 7), (3, 8), (4, 9),
]


def cmd_anchors(_args):
    checks = 0

    def ok(cond, label):
        nonlocal checks
        assert cond, "ANCHOR FAILED: %s" % label
        checks += 1

    # K4: spectrum {3,4}, not power-free, no profile pair (all degree 3).
    k4 = from_edges(4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
    ok(cycle_spectrum_bruteforce(k4) == {3, 4}, "K4 spectrum")
    ok(power_free(k4) == (False, [4]), "K4 power lengths")
    ok(profile_pair(degrees(k4)) is None, "K4 profile")

    # K_{3,3}-e: spectrum {4,6}, S = {3,5} between the two degree-2 vertices.
    k33e = from_edges(6, [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4)])
    ok(cycle_spectrum_bruteforce(k33e) == {4, 6}, "K33-e spectrum")
    pair = profile_pair(degrees(k33e))
    ok(pair == (2, 5), "K33-e degree-2 pair")
    ok(path_lengths(k33e, 2, 5) == {3, 5}, "K33-e S = {3,5}")
    ok(has_c4(k33e), "K33-e has a C4")

    # Petersen: cubic, spectrum {5,6,8,9}, C4-free, has C8.
    pet = from_edges(10, PETERSEN_EDGES)
    ok(degrees(pet) == [3] * 10, "Petersen cubic")
    ok(cycle_spectrum_bruteforce(pet) == {5, 6, 8, 9}, "Petersen spectrum")
    ok(not has_c4(pet), "Petersen C4-free")
    ok(has_cycle_len(pet, 8) and not has_cycle_len(pet, 4), "Petersen C8 yes C4 no")
    ok(count_cycles_len(pet, 5) == 12 and count_cycles_len(pet, 6) == 10,
       "Petersen 12 pentagons 10 hexagons")

    # Petersen-e: in the profile class at order 10; S = {4,5,7,8} (C031);
    # blocked by C8 (spectrum {5,6,8,9}); its closure spectrum gains S+2.
    pe_edges = [e for e in PETERSEN_EDGES if e != (0, 1)]
    pe = from_edges(10, pe_edges)
    pair = profile_pair(degrees(pe))
    ok(pair == (0, 1), "Petersen-e degree-2 pair")
    ok(path_lengths(pe, 0, 1) == {4, 5, 7, 8}, "Petersen-e S = {4,5,7,8}")
    ok(cycle_spectrum_bruteforce(pe) == {5, 6, 8, 9}, "Petersen-e spectrum")
    ok(has_cycle_len(pe, 8), "Petersen-e C8-blocked")
    ok(not has_c4(pe), "Petersen-e C4-free")
    # 2-closure (L039): Spec(H+u) = Spec(H) ∪ (S+2) = {5,...,10}.
    closure = [row << 1 for row in pe]  # shift vertices up; u becomes vertex 0
    closure = [0] + closure
    closure[0] = (1 << 1) | (1 << 2)   # u ~ a(=old 0), b(=old 1)
    closure[1] |= 1
    closure[2] |= 1
    ok(cycle_spectrum_bruteforce(closure) == {5, 6, 7, 8, 9, 10},
       "2-closure of Petersen-e spectrum {5..10}")
    ok(power_free(closure) == (False, [8]), "closure not power-free (6 in S+2)")

    # analyse_survivor exercised on a synthetic power-free profile member:
    # C6 with two opposite vertices given pendant-triangle... instead use the
    # theta-free construction: subdivide one edge of K4 twice (S-condition
    # fails there), so build the 7-vertex graph: K4 with edge (2,3) replaced
    # by the path 2-4... — simplest verified object: take C5 plus a chord
    # path. We use the prism-minus... Rather than invent an unrecorded
    # object, run the analysis on the smallest profile-class member found by
    # geng at order 8 (E016 A6: exactly one exists) and assert its shape.
    tally = scan_stream(8, collect_class=True)
    ok(tally["profile"] == 1, "order-8 class size 1 (E016 A6)")
    ok(tally["survivors"] == [], "order-8: no power-free member (E016 A6)")

    # path_lengths cross-check against the recursive reference on every
    # connected graph of order <= 7 and every vertex pair (E016-style).
    proc = subprocess.Popen(
        [GENG, "-q", "-c", "6"], stdout=subprocess.PIPE)
    lines6 = proc.stdout.read().split()
    assert proc.wait() == 0
    proc = subprocess.Popen(
        [GENG, "-q", "-c", "7"], stdout=subprocess.PIPE)
    lines7 = proc.stdout.read().split()
    assert proc.wait() == 0
    pairs_checked = 0
    for raw in lines6 + lines7:
        adjacency = g6_decode(raw.decode())
        n = len(adjacency)
        nbrs = [[w for w in range(n) if adjacency[v] >> w & 1] for v in range(n)]
        for a in range(n):
            for b in range(a + 1, n):
                ref = _path_lengths_reference(nbrs, a, b)
                got = path_lengths(adjacency, a, b)
                assert got == ref, "path_lengths mismatch at %r" % raw
                pairs_checked += 1
    ok(pairs_checked == 2 * (112 * 15 + 853 * 21) // 2, "pair count sanity")

    # cut_vertices: path P4 has cuts {1,2}; C5 has none; bridge composite.
    p4 = from_edges(4, [(0, 1), (1, 2), (2, 3)])
    ok(cut_vertices(p4) == [1, 2], "P4 cut vertices")
    c5 = from_edges(5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)])
    ok(cut_vertices(c5) == [], "C5 2-connected")
    ok(bipartition(c5) is None, "C5 odd")
    ok(bipartition(from_edges(4, [(0, 1), (1, 2), (2, 3)])) is not None, "P4 bipartite")

    print("anchors: %d checks passed (%s)" % (checks, sys.version.split()[0]))


def _path_lengths_reference(nbrs, a, b):
    """E016/verify.py path_lengths, verbatim shape (recursive, list-based)."""
    if a == b:
        return set()
    out = set()
    visited = {a}

    def dfs(cur, length):
        for w in nbrs[cur]:
            if w == b:
                out.add(length + 1)
            elif w not in visited:
                visited.add(w)
                dfs(w, length + 1)
                visited.remove(w)

    dfs(a, 0)
    return out


# E016 A6 class sizes (corrected run): order -> exactly-two-degree-2 class size.
E016_A6 = {8: 1, 9: 2, 10: 22, 11: 125, 12: 1139, 13: 10966}


def cmd_calibrate(args):
    orders = [int(a) for a in args] or sorted(E016_A6)
    for n in orders:
        tally = scan_stream(n, collect_class=True)
        expected = E016_A6.get(n)
        status = ""
        if expected is not None:
            assert tally["profile"] == expected, (
                "class size mismatch at %d: got %d, E016 A6 says %d"
                % (n, tally["profile"], expected))
            status = " == E016 A6"
        assert tally["c16_blocked"] == 0 or n >= 16
        print(
            "n=%2d stream=%9d class=%8d%s  c8_blocked=%8d  min_c8=%s  "
            "c16_blocked=%d  survivors=%d  max_e=%d  %.1fs"
            % (n, tally["stream"], tally["profile"], status,
               tally["c8_blocked"], tally["min_c8_in_class"],
               tally["c16_blocked"], len(tally["survivors"]),
               tally["max_edges_seen"], tally["seconds"]))
        if tally["survivors"]:
            print(json.dumps(tally["survivors"], indent=2))
            print("*** POWER-FREE PROFILE MEMBER AT ORDER %d ***" % n)
        os.makedirs(DATA, exist_ok=True)
        with open(os.path.join(DATA, "calibrate_n%d.json" % n), "w") as fh:
            json.dump(tally, fh, indent=1)


def cmd_run(args):
    stats = "--stats" in args
    args = [a for a in args if a != "--stats"]
    n = int(args[0])
    part = args[1] if len(args) > 1 else None
    tally = scan_stream(n, part=part, collect_class=stats)
    os.makedirs(DATA, exist_ok=True)
    suffix = ("_part%s" % part.replace("/", "of")) if part else ""
    path = os.path.join(DATA, "scan_n%d%s.json" % (n, suffix))
    with open(path, "w") as fh:
        json.dump(tally, fh, indent=1)
    print(
        "n=%d part=%s stream=%d profile=%d c8_blocked=%d c16_blocked=%d "
        "survivors=%d max_e=%d %.1fs -> %s"
        % (n, tally["part"], tally["stream"], tally["profile"],
           tally["c8_blocked"], tally["c16_blocked"], len(tally["survivors"]),
           tally["max_edges_seen"], tally["seconds"], os.path.basename(path)))
    if tally["survivors"]:
        print(json.dumps(tally["survivors"], indent=2))
        print("*** POWER-FREE PROFILE MEMBER AT ORDER %d — see JSON ***" % n)


def cmd_harvest(args):
    n = int(args[0])
    mod = int(args[1])
    total = {"stream": 0, "profile": 0, "c8_blocked": 0, "c16_blocked": 0}
    survivors = []
    max_e = 0
    seconds = 0.0
    for r in range(mod):
        path = os.path.join(DATA, "scan_n%d_part%dof%d.json" % (n, r, mod))
        assert os.path.exists(path), "missing part %d/%d" % (r, mod)
        with open(path) as fh:
            tally = json.load(fh)
        assert tally["order"] == n and tally["part"] == "%d/%d" % (r, mod)
        for key in total:
            total[key] += tally[key]
        survivors.extend(tally["survivors"])
        max_e = max(max_e, tally["max_edges_seen"])
        seconds += tally["seconds"]
    assert total["profile"] == (
        total["c8_blocked"] + total["c16_blocked"] + len(survivors))
    result = {
        "order": n,
        "parts": mod,
        "geng": " ".join(geng_args(n, part="r/%d" % mod)),
        **total,
        "survivors": survivors,
        "max_edges_seen": max_e,
        "cpu_seconds_sum": round(seconds, 1),
    }
    out = os.path.join(DATA, "scan_n%d_harvest.json" % n)
    with open(out, "w") as fh:
        json.dump(result, fh, indent=1)
    print(json.dumps({k: v for k, v in result.items() if k != "survivors"},
                     indent=1))
    print("survivors: %d" % len(survivors))
    for s in survivors:
        print(json.dumps(s, indent=2))
    if not survivors:
        print("VERDICT: the order-%d G-profile class has no power-free member."
              % n)
    else:
        in_g = [s for s in survivors if s["in_G"]]
        print("VERDICT: %d power-free member(s), %d in G (S avoids {2,6,14})."
              % (len(survivors), len(in_g)))
        if in_g:
            print("*** G-MEMBER FOUND: tight 1-atom of order %d exists; "
                  "statement 0.1 is FALSE pending the disproof protocol ***"
                  % (n + 1))


def main():
    cmds = {
        "anchors": cmd_anchors,
        "calibrate": cmd_calibrate,
        "run": cmd_run,
        "harvest": cmd_harvest,
    }
    if len(sys.argv) < 2 or sys.argv[1] not in cmds:
        print(__doc__)
        sys.exit(1)
    cmds[sys.argv[1]](sys.argv[2:])


if __name__ == "__main__":
    main()
