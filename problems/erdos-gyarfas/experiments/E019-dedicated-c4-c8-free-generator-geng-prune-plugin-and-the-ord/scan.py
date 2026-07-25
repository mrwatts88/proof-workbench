#!/usr/bin/env python3
"""E019 — the dedicated {C4,C8}-free generator and the order-17 G-profile scan.

Instrument
----------
`build/genc48` is nauty 2.9.3's geng compiled with the PREPRUNE plugin
`prune_c8.c`: geng's own `-f` removes 4-cycles natively and the plugin
removes 8-cycles at every level of geng's canonical construction path.  Its
output is therefore geng's usual isomorph-free stream intersected with "no
C8" (see prune_c8.c for the completeness argument, and `anchors` below for
the empirical validation against the independent `geng -f | C8-filter`
pipeline that E010-E018 used).

Target class (the class G of L039, graph part), order n:
    connected, C4-free, C8-free, exactly two vertices of degree 2 (a, b),
    all other degrees >= 3, power-free (no C4/C8/C16 at order <= 17);
membership additionally needs S(H,a,b) cap {2,6,14} = empty (P-2 truncated to
path lengths <= 16).

Verdicts (L039/L041/C036):
  - a survivor satisfying the S-condition is a member of G, hence the reduct
    of a tight 1-atom of order n+1, and STATEMENT 0.1 IS FALSE (L025 R4);
  - an empty scan at order 17 lifts the tight-1-atom order bound from >= 18
    to >= 19 and the G-member bound from >= 17 to >= 18.

ONLY the unconditional filters reduce the reported class: the degree profile,
power-freeness, and the S-condition (L039).  Conditional structure facts from
L042 (2-connectivity, non-bipartiteness, ...) are recorded on survivors as
data and never prune.

Graph primitives are copied verbatim from E018/scan.py (which copied them
from E015/bipscan.py, anchored there against the independent E010 pipeline
and the recorded spectra of CLAIMS.md) and are re-anchored here.

Commands
--------
    python3 scan.py anchors            # fixed anchors + generator validation
    python3 scan.py count N [r/m]      # generator-only counts (geng -u), fast
    python3 scan.py run N [r/m] [--verify-all]
    python3 scan.py harvest N m
Deterministic; no randomness; integers and integer bitmasks only.
"""

import glob
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
BUILD = os.path.join(HERE, "build")
GENC48 = os.path.join(BUILD, "genc48")                     # our generator
GENG = os.path.join(BUILD, "nauty2_9_3", "geng")           # stock geng, same source
LABELG = "labelg"                                          # nauty 2.9.3, installed

# --- primitives copied verbatim from E018/scan.py ---------------------------
# (which copied them from E015/bipscan.py; anchored against the independent
#  E010 pipeline and known spectra)


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


def path_lengths(adjacency, a, b):
    """Exact set of lengths (in edges) of simple a-b paths (bitmask DFS)."""
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


# --- generator plumbing ------------------------------------------------------


def mine_for(n):
    """Degree sum >= 4 + 3(n-2) for the two-degree-2 profile."""
    return (3 * n - 2 + 1) // 2


def gen_args(binary, n, mine=None, maxe=None, part=None, extra=(), count_only=False):
    if mine is None:
        mine = mine_for(n)
    if maxe is None:
        maxe = n * (n - 1) // 2
    args = [binary, "-q"]
    if count_only:
        args.append("-u")
    args.extend(extra)
    args.extend([str(n), "%d:%d" % (mine, maxe)])
    if part is not None:
        args.append(part)
    return args


def run_generator(args, capture_lines=True):
    """Run a generator; return (lines, stderr_text).  stderr is redirected to a
    temporary file so that a full stdout pipe can never deadlock against it."""
    errpath = os.path.join(
        DATA, ".stderr.%d.%d.txt" % (os.getpid(), int(time.time() * 1000) % 1000000))
    os.makedirs(DATA, exist_ok=True)
    with open(errpath, "w+") as errfh:
        if capture_lines:
            proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=errfh,
                                    bufsize=1 << 20)
            out = proc.stdout.read().split()
            code = proc.wait()
        else:
            proc = subprocess.Popen(args, stdout=subprocess.DEVNULL, stderr=errfh)
            out = []
            code = proc.wait()
        errfh.seek(0)
        err = errfh.read()
    os.remove(errpath)
    assert code == 0, "%r exited with %r" % (args[0], code)
    return [x.decode() if isinstance(x, bytes) else x for x in out], err


def parse_summary(err):
    """Parse the plugin's SUMMARY lines: totals and per-level node counts."""
    total = {}
    levels = {}
    for line in err.splitlines():
        if line.startswith(">C prune_c8"):
            for token in line.split()[2:]:
                key, _, val = token.partition("=")
                total[key] = float(val) if key == "cpu" else int(val)
        elif line.startswith(">L "):
            fields = dict(t.split("=") for t in line.split()[1:])
            levels[int(fields["level"])] = {
                "calls": int(fields["calls"]), "rejects": int(fields["rejects"])}
    return total, levels


def canonical_set(lines):
    """Canonical graph6 forms via nauty's labelg (installed 2.9.3)."""
    if not lines:
        return set()
    payload = "\n".join(lines) + "\n"
    proc = subprocess.run([LABELG, "-q"], input=payload.encode(),
                          stdout=subprocess.PIPE)
    assert proc.returncode == 0
    return set(proc.stdout.decode().split())


# --- anchors -----------------------------------------------------------------

PETERSEN_EDGES = [
    (0, 1), (1, 2), (2, 3), (3, 4), (4, 0),
    (5, 7), (7, 9), (9, 6), (6, 8), (8, 5),
    (0, 5), (1, 6), (2, 7), (3, 8), (4, 9),
]

# Heawood graph: the (3,6)-cage, bipartite, order 14, girth 6, 21 C8s (E015).
HEAWOOD_EDGES = [(i, (i + 1) % 14) for i in range(14)] + [
    (0, 5), (2, 7), (4, 9), (6, 11), (8, 13), (10, 1), (12, 3)]


def g6_encode(adjacency):
    n = len(adjacency)
    assert n < 63
    bits = []
    for j in range(1, n):
        for i in range(j):
            bits.append((adjacency[i] >> j) & 1)
    while len(bits) % 6:
        bits.append(0)
    out = [chr(n + 63)]
    for k in range(0, len(bits), 6):
        value = 0
        for b in bits[k:k + 6]:
            value = (value << 1) | b
        out.append(chr(value + 63))
    return "".join(out)


def cycle_graph(n):
    return from_edges(n, [(i, (i + 1) % n) for i in range(n)])


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


# The three generator-validation class variants.  Each is a geng switch set
# that is nonempty in the {C4,C8}-free world at the listed orders; for each we
# compare genc48's output with the independent
#     stock geng (same switches) | has_cycle_len(.,8) filter
# pipeline, as SETS of labelg canonical forms (not merely as counts).
VARIANTS = {
    # connected, C4-free, min degree >= 2, no edge restriction
    "d2": (["-c", "-f", "-d2"], [8, 9, 10, 11, 12], 1, 0),
    # connected, C4-free, min degree >= 1 (a different geng degree regime)
    "d1": (["-c", "-f", "-d1"], [6, 7, 8, 9, 10], 1, 0),
    # connected, C4-free, subcubic with min degree 2 (the near-target regime)
    "sub3": (["-c", "-f", "-d2", "-D3"], [8, 9, 10, 11, 12, 13], 1, 0),
    # the bipartite code path (geng's -b uses a different `make*graph`
    # extension table, so it is anchored separately) -- E015's regime
    "bipd1": (["-c", "-f", "-b", "-d1"], [8, 9, 10], 1, 0),
    "bipd2": (["-c", "-f", "-b", "-d2"], [10, 11, 12, 13], 1, 0),
}


def cmd_anchors(_args):
    checks = 0

    def ok(cond, label):
        nonlocal checks
        assert cond, "ANCHOR FAILED: %s" % label
        checks += 1

    # ---- primitive anchors (E018 suite, re-run on the copied primitives) ----

    # K4: spectrum {3,4}, not power-free, no profile pair (all degree 3).
    k4 = from_edges(4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
    ok(cycle_spectrum_bruteforce(k4) == {3, 4}, "K4 spectrum")
    ok(power_free(k4) == (False, [4]), "K4 power lengths")
    ok(profile_pair(degrees(k4)) is None, "K4 profile")
    ok(has_c4(k4), "K4 has a C4")

    # K_{3,3}-e: spectrum {4,6}, S = {3,5} between the two degree-2 vertices.
    k33e = from_edges(6, [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5),
                          (2, 3), (2, 4)])
    ok(cycle_spectrum_bruteforce(k33e) == {4, 6}, "K33-e spectrum")
    ok(profile_pair(degrees(k33e)) == (2, 5), "K33-e degree-2 pair")
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

    # Petersen-e: in the profile class at order 10; S = {4,5,7,8} (C031).
    pe_edges = [e for e in PETERSEN_EDGES if e != (0, 1)]
    pe = from_edges(10, pe_edges)
    ok(profile_pair(degrees(pe)) == (0, 1), "Petersen-e degree-2 pair")
    ok(path_lengths(pe, 0, 1) == {4, 5, 7, 8}, "Petersen-e S = {4,5,7,8}")
    ok(cycle_spectrum_bruteforce(pe) == {5, 6, 8, 9}, "Petersen-e spectrum")
    ok(has_cycle_len(pe, 8), "Petersen-e C8-blocked")
    ok(not has_c4(pe), "Petersen-e C4-free")

    # 2-closure of Petersen-e (L039): Spec(H+u) = Spec(H) u (S+2) = {5,...,10}.
    closure = [row << 1 for row in pe]
    closure = [0] + closure
    closure[0] = (1 << 1) | (1 << 2)
    closure[1] |= 1
    closure[2] |= 1
    ok(cycle_spectrum_bruteforce(closure) == {5, 6, 7, 8, 9, 10},
       "2-closure of Petersen-e spectrum {5..10}")
    ok(power_free(closure) == (False, [8]), "closure not power-free (6 in S+2)")

    # Heawood: order 14, bipartite, spectrum {6,8,10,12,14}, 21 C8s (E015).
    hea = from_edges(14, HEAWOOD_EDGES)
    ok(degrees(hea) == [3] * 14, "Heawood cubic")
    ok(cycle_spectrum_bruteforce(hea) == {6, 8, 10, 12, 14}, "Heawood spectrum")
    ok(count_cycles_len(hea, 8) == 21, "Heawood 21 C8s")
    ok(bipartition(hea) is not None, "Heawood bipartite")

    # cut_vertices / bipartition sanity.
    p4 = from_edges(4, [(0, 1), (1, 2), (2, 3)])
    ok(cut_vertices(p4) == [1, 2], "P4 cut vertices")
    c5 = cycle_graph(5)
    ok(cut_vertices(c5) == [], "C5 2-connected")
    ok(bipartition(c5) is None, "C5 odd")
    ok(bipartition(p4) is not None, "P4 bipartite")

    # graph6 round trip (needed by the named-object membership anchors).
    for adjacency in (k4, pet, pe, hea, c5):
        ok(g6_decode(g6_encode(adjacency)) == adjacency, "g6 round trip")

    # path_lengths against the recursive E016 reference on every connected
    # graph of order <= 7 and every vertex pair.
    lines6, _ = run_generator([GENG, "-q", "-c", "6"])
    lines7, _ = run_generator([GENG, "-q", "-c", "7"])
    pairs_checked = 0
    for raw in lines6 + lines7:
        adjacency = g6_decode(raw)
        n = len(adjacency)
        nbrs = [[w for w in range(n) if adjacency[v] >> w & 1] for v in range(n)]
        for a in range(n):
            for b in range(a + 1, n):
                assert path_lengths(adjacency, a, b) == _path_lengths_reference(
                    nbrs, a, b), "path_lengths mismatch at %r" % raw
                pairs_checked += 1
    ok(len(lines6) == 112 and len(lines7) == 853, "connected graph counts 6,7")
    ok(pairs_checked == 112 * 15 + 853 * 21, "pair count sanity")

    # ---- generator anchors --------------------------------------------------

    # A. Set equality with the independent pipeline, three class variants.
    comparisons = []
    for name, (switches, orders, _lo, _hi) in VARIANTS.items():
        for n in orders:
            args_new = [GENC48, "-q"] + switches + [str(n)]
            args_ref = [GENG, "-q"] + switches + [str(n)]
            new_lines, err = run_generator(args_new)
            ref_lines, _ = run_generator(args_ref)
            kept = [g for g in ref_lines
                    if not has_cycle_len(g6_decode(g), 8)]
            new_set = canonical_set(new_lines)
            ref_set = canonical_set(kept)
            ok(len(new_set) == len(new_lines), "%s n=%d genc48 isomorph-free" % (name, n))
            ok(new_set == ref_set,
               "%s n=%d set equality (%d vs %d)"
               % (name, n, len(new_set), len(ref_set)))
            ok(len(new_lines) > 0, "%s n=%d nonempty" % (name, n))
            # every generated graph really is C4-free and C8-free
            for g in new_lines:
                adjacency = g6_decode(g)
                assert not has_c4(adjacency) and not has_cycle_len(adjacency, 8), \
                    "genc48 emitted a C4/C8 at %s n=%d: %s" % (name, n, g)
            checks += 1
            total, _levels = parse_summary(err)
            comparisons.append({
                "variant": name, "switches": switches, "order": n,
                "genc48": len(new_lines), "geng_stream": len(ref_lines),
                "geng_c8_free": len(kept),
                "prune_calls": total.get("calls"), "prune_rejects": total.get("rejects"),
            })

    # B. Named objects: in-class and out-of-class membership.
    pet_c = canonical_set([g6_encode(pet)])
    pe_c = canonical_set([g6_encode(pe)])
    hea_c = canonical_set([g6_encode(hea)])
    out10, _ = run_generator([GENC48, "-q", "-c", "-f", "-d2", "10"])
    set10 = canonical_set(out10)
    ok(not (pet_c & set10), "Petersen NOT generated (has a C8)")
    ok(not (pe_c & set10), "Petersen-e NOT generated (has a C8)")
    ref10, _ = run_generator([GENG, "-q", "-c", "-f", "-d2", "10"])
    ref10_set = canonical_set(ref10)
    ok(pet_c <= ref10_set and pe_c <= ref10_set,
       "Petersen and Petersen-e ARE in the unpruned C4-free stream")
    out14, _ = run_generator([GENC48, "-q", "-c", "-f", "-d2", "-D3", "14"])
    ok(not (hea_c & canonical_set(out14)), "Heawood NOT generated (has a C8)")

    # cycles: C5,C6,C7 and C9..C13 are {C4,C8}-free and 2-regular, so each is
    # the unique member of its order in `-c -f -d2 n n:n`; C8 must be absent.
    for length in (5, 6, 7, 9, 10, 11, 12, 13):
        outc, _ = run_generator(
            [GENC48, "-q", "-c", "-f", "-d2", str(length), "%d:%d" % (length, length)])
        ok(canonical_set(outc) == canonical_set([g6_encode(cycle_graph(length))]),
           "C%d generated" % length)
    out8, _ = run_generator(
        [GENC48, "-q", "-c", "-f", "-d2", "8", "8:8"])
    ok(out8 == [], "C8 NOT generated")
    ok(canonical_set(run_generator([GENG, "-q", "-c", "-f", "-d2", "8", "8:8"])[0])
       == canonical_set([g6_encode(cycle_graph(8))]), "C8 IS in the geng stream")

    # K4 has a C4, so `-f` must exclude it from both instruments.
    k4_c = canonical_set([g6_encode(k4)])
    ok(not (k4_c & canonical_set(run_generator([GENG, "-q", "-c", "-f", "4"])[0])),
       "K4 excluded by -f (stock geng)")
    ok(not (k4_c & canonical_set(run_generator([GENC48, "-q", "-c", "-f", "4"])[0])),
       "K4 excluded by -f (genc48)")

    # C. res/mod splitting is a partition under pruning.
    for n, mod in ((12, 7), (13, 5), (14, 11)):
        whole, _ = run_generator(gen_args(GENC48, n, extra=["-c", "-f", "-d2"]))
        pieces = []
        for r in range(mod):
            piece, _ = run_generator(
                gen_args(GENC48, n, extra=["-c", "-f", "-d2"], part="%d/%d" % (r, mod)))
            pieces.extend(piece)
        ok(sorted(pieces) == sorted(whole),
           "res/mod partition at n=%d mod=%d (%d vs %d)"
           % (n, mod, len(pieces), len(whole)))

    print("anchors: %d checks passed (%s)" % (checks, interpreter()))
    os.makedirs(DATA, exist_ok=True)
    with open(os.path.join(DATA, "anchors_%s.json" % interpreter_tag()), "w") as fh:
        json.dump({"checks": checks, "interpreter": interpreter(),
                   "comparisons": comparisons}, fh, indent=1)


def interpreter():
    return sys.version.split()[0] + (
        "/PyPy" if hasattr(sys, "pypy_version_info") else "/CPython")


def interpreter_tag():
    return "pypy" if hasattr(sys, "pypy_version_info") else "cpython"


# --- the scan ----------------------------------------------------------------

# E018/E016 A6 profile-class sizes over the *unpruned* C4-free stream; here the
# C8-free part of each is 0 (C027 through 15, C036 at 16).
KNOWN_EMPTY = (14, 15, 16)

# Save the generated class verbatim (graph6, edges, #degree-2 vertices) when a
# part emits at most this many graphs.  The whole point of the instrument is
# that the class is tiny, so this is essentially always on.
SAVE_LIMIT = 200000


def scan(n, part=None, verify_all=False):
    """Generate the {C4,C8}-free class and apply the unconditional filters."""
    args = gen_args(GENC48, n, extra=["-c", "-f", "-d2"], part=part)
    errpath = os.path.join(DATA, ".err_n%d_%s.txt" % (n, (part or "all").replace("/", "of")))
    os.makedirs(DATA, exist_ok=True)
    t0 = time.time()
    with open(errpath, "w+") as errfh:
        proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=errfh,
                                bufsize=1 << 20)
        generated = 0
        profile = 0
        c16_blocked = 0
        survivors = []
        max_edges_seen = 0
        max_edges_class = 0
        deg2_hist = {}
        pf_deg2_hist = {}
        pf_exemplars = []
        kept = []
        assert proc.stdout is not None
        for raw in proc.stdout:
            generated += 1
            line = raw.decode().strip()
            adjacency = g6_decode(line)
            # Independent re-verification of the generation layer on EVERY
            # generated graph (not only survivors): power_free tests C4, C8 and
            # C16 by the E015 cycle detector, so it re-derives geng's -f and
            # the plugin's C8 rejection without trusting either.
            is_pf, present = power_free(adjacency)
            assert 4 not in present, "generator emitted a C4: %s" % line
            assert 8 not in present, "generator emitted a C8: %s" % line
            if verify_all:
                assert not has_c4(adjacency), "generator emitted a C4: %s" % line
                assert not has_cycle_len(adjacency, 8), \
                    "generator emitted a C8: %s" % line
            deg = degrees(adjacency)
            # proximity statistic: how many sub-cubic (degree-2) vertices does
            # this {C4,C8}-free graph have?  The target profile is exactly 2.
            n2 = sum(1 for d in deg if d == 2)
            deg2_hist[n2] = deg2_hist.get(n2, 0) + 1
            edges = sum(deg) // 2
            if edges > max_edges_class:
                max_edges_class = edges
            if generated <= SAVE_LIMIT:
                kept.append("%s %d %d %d" % (line, edges, n2, int(is_pf)))
            if is_pf:
                # power-free with minimum degree 2: n2 == 1 would be a tight
                # 1-atom, n2 == 0 a counterexample outright (L025/L036)
                pf_deg2_hist[n2] = pf_deg2_hist.get(n2, 0) + 1
                if n2 <= 3:
                    pf_exemplars.append({"g6": line, "edges": edges,
                                         "n_degree_2": n2})
            pair = profile_pair(deg)
            if pair is None:
                continue
            profile += 1
            # independent re-check of the generation layer on every member of
            # the reported class (not only on survivors)
            assert not has_c4(adjacency), "profile member with a C4: %s" % line
            assert not has_cycle_len(adjacency, 8), "profile member with a C8: %s" % line
            e = sum(deg) // 2
            if e > max_edges_seen:
                max_edges_seen = e
            if n >= 16 and has_cycle_len(adjacency, 16):
                c16_blocked += 1
            else:
                survivors.append(analyse_survivor(line, adjacency))
        code = proc.wait()
        errfh.seek(0)
        err = errfh.read()
    assert code == 0, "genc48 exited with %r" % code
    os.remove(errpath)
    # coverage identity, per part: in-profile {C4,C8}-free = C16 + survivors
    assert profile == c16_blocked + len(survivors)
    total, levels = parse_summary(err)
    assert total.get("out") == generated, (
        "generator reported out=%r but %d graphs were read"
        % (total.get("out"), generated))
    if generated <= SAVE_LIMIT:
        suffix = ("_part%s" % part.replace("/", "of")) if part else ""
        with open(os.path.join(DATA, "class_n%d%s.txt" % (n, suffix)), "w") as fh:
            fh.write("# graph6 edges n_degree2 power_free"
                     "   ({C4,C8}-free class, order %d)\n" % n)
            for row in kept:
                fh.write(row + "\n")
    return {
        "order": n,
        "part": part or "0/1",
        "generator": " ".join(args),
        "generated_c4c8_free": generated,
        "profile": profile,
        "c16_blocked": c16_blocked,
        "survivors": survivors,
        "max_edges_in_profile": max_edges_seen,
        "max_edges_in_class": max_edges_class,
        "deg2_hist": {str(k): v for k, v in sorted(deg2_hist.items())},
        "min_deg2_in_class": min(deg2_hist) if deg2_hist else None,
        "power_free_in_class": sum(pf_deg2_hist.values()),
        "power_free_deg2_hist": {str(k): v for k, v in sorted(pf_deg2_hist.items())},
        "power_free_min_deg2": min(pf_deg2_hist) if pf_deg2_hist else None,
        "power_free_exemplars": pf_exemplars,
        "prune_total": total,
        "prune_levels": {str(k): v for k, v in sorted(levels.items())},
        "verify_all": verify_all,
        "seconds": round(time.time() - t0, 1),
        "interpreter": interpreter(),
    }


def cmd_count(args):
    """Generator-only counts (geng -u): the feasibility measurement."""
    orders = []
    part = None
    for a in args:
        if "/" in a:
            part = a
        else:
            orders.append(int(a))
    rows = []
    for n in orders:
        t0 = time.time()
        _out, err = run_generator(
            gen_args(GENC48, n, extra=["-c", "-f", "-d2"], part=part, count_only=True),
            capture_lines=False)
        total, levels = parse_summary(err)
        row = {"order": n, "part": part or "0/1", "out": total.get("out"),
               "prune_calls": total.get("calls"),
               "prune_rejects": total.get("rejects"),
               "generator_cpu": total.get("cpu"),
               "wall": round(time.time() - t0, 1),
               "levels": {str(k): v for k, v in sorted(levels.items())},
               "generator": " ".join(gen_args(GENC48, n, extra=["-c", "-f", "-d2"],
                                              part=part, count_only=True))}
        rows.append(row)
        print("n=%2d part=%s  {C4,C8}-free out=%d  tree nodes=%d  rejects=%d  "
              "%.2fs" % (n, row["part"], row["out"], row["prune_calls"],
                         row["prune_rejects"], row["wall"]))
        with open(os.path.join(DATA, "count_n%d%s.json" % (
                n, "" if part is None else "_part" + part.replace("/", "of"))), "w") as fh:
            json.dump(row, fh, indent=1)
    return rows


# Named probes for the design analyses (feasibility measurements only; each is
# a generator-only `-u` count, no filtering, no mathematical claim).
PROBES = {
    # the production class: connected, C4-free, min degree >= 2, profile edge bound
    "profile": (["-c", "-f", "-d2"], lambda n: ((3 * n - 2 + 1) // 2, n * (n - 1) // 2)),
    # connected, C4-free, minimum degree >= 3 -- the counterexample class itself
    # (L022: the smallest {C4,C8}-free min-degree-3 graph has order 19..24)
    "mindeg3": (["-c", "-f", "-d3"], lambda n: ((3 * n + 1) // 2, n * (n - 1) // 2)),
    # connected cubic, C4-free (C013 / Markstroem Table 3: 4 at 24, 23 at 26,
    # 251 at 28 cubic graphs with no C4 and no C8)
    "cubic": (["-c", "-f", "-d3", "-D3"], lambda n: (3 * n // 2, 3 * n // 2)),
    # the E015 bipartite class before its sub-cubic-count filter
    "bip": (["-c", "-f", "-b", "-d2"], lambda n: ((3 * n - 2 + 1) // 2, n * (n - 1) // 2)),
    # C027's class before its sub-cubic filter: min degree >= 1, edge bound for
    # "at most two sub-cubic vertices" in the worst case (both of degree 1)
    "subcubic2": (["-c", "-f", "-d1"], lambda n: ((3 * n - 4 + 1) // 2,
                                                  n * (n - 1) // 2)),
}


def cmd_probe(args):
    name = args[0]
    orders = [int(a) for a in args[1:] if "/" not in a]
    part = next((a for a in args[1:] if "/" in a), None)
    switches, bounds = PROBES[name]
    rows = []
    for n in orders:
        mine, maxe = bounds(n)
        t0 = time.time()
        _out, err = run_generator(
            gen_args(GENC48, n, mine=mine, maxe=maxe, part=part, extra=switches,
                     count_only=True), capture_lines=False)
        total, levels = parse_summary(err)
        row = {"probe": name, "switches": switches, "order": n,
               "part": part or "0/1", "mine": mine, "maxe": maxe,
               "out": total.get("out"), "prune_calls": total.get("calls"),
               "prune_rejects": total.get("rejects"),
               "generator_cpu": total.get("cpu"),
               "wall": round(time.time() - t0, 1),
               "levels": {str(k): v for k, v in sorted(levels.items())}}
        rows.append(row)
        print("%-8s n=%2d %s out=%d tree=%d rejects=%d %.1fs"
              % (name, n, "%d:%d" % (mine, maxe), row["out"], row["prune_calls"],
                 row["prune_rejects"], row["wall"]))
    os.makedirs(DATA, exist_ok=True)
    path = os.path.join(DATA, "probe_%s.json" % name)
    old = []
    if os.path.exists(path):
        with open(path) as fh:
            old = json.load(fh)
    keep = [r for r in old
            if (r["order"], r["part"]) not in {(x["order"], x["part"]) for x in rows}]
    with open(path, "w") as fh:
        json.dump(sorted(keep + rows, key=lambda r: (r["order"], r["part"])), fh, indent=1)
    return rows


E005_N24 = os.path.join(
    HERE, os.pardir,
    "E005-markstrom-24-vertex-graphs-verification-and-reproduction",
    "data", "survivors_n24.g6")


def cmd_cubic24(_args):
    """External anchor: regenerate the cubic {C4,C8}-free census at order 24
    in one step and check it against E005's independently produced file (which
    reproduces Markstroem's Table 3 count of 4)."""
    t0 = time.time()
    out, err = run_generator(
        gen_args(GENC48, 24, mine=36, maxe=36, extra=["-c", "-f", "-d3", "-D3"]))
    total, _levels = parse_summary(err)
    with open(E005_N24) as fh:
        e005 = [line.strip() for line in fh if line.strip()]
    for g in out:
        adjacency = g6_decode(g)
        assert degrees(adjacency) == [3] * 24, "not cubic: %s" % g
        assert not has_c4(adjacency) and not has_cycle_len(adjacency, 8), g
        assert has_cycle_len(adjacency, 16), "would be a counterexample: %s" % g
    mine_set = canonical_set(out)
    e005_set = canonical_set(e005)
    result = {
        "order": 24, "genc48": len(out), "e005": len(e005),
        "set_equal": mine_set == e005_set,
        "markstrom_table3": 4,
        "graph6": sorted(mine_set),
        "prune_calls": total.get("calls"), "prune_rejects": total.get("rejects"),
        "wall": round(time.time() - t0, 1), "interpreter": interpreter(),
    }
    assert result["set_equal"] and len(out) == 4, json.dumps(result, indent=1)
    os.makedirs(DATA, exist_ok=True)
    with open(os.path.join(DATA, "cubic24_check.json"), "w") as fh:
        json.dump(result, fh, indent=1)
    print(json.dumps({k: v for k, v in result.items() if k != "graph6"}, indent=1))
    print("cubic order-24 census reproduced: 4 graphs, set-equal to E005, "
          "== Markstroem Table 3")


def cmd_crosscheck(args):
    """Full filter-the-stream cross-check at production scale: run STOCK geng
    on the same switches, filter its whole stream with the E015 C8 detector,
    and compare the result with genc48's output as labelg-canonical SETS.
    This is the E010-E018 instrument on one side and the new one on the other.
    Usage: crosscheck <probe-name> <orders...>"""
    name = args[0]
    switches, bounds = PROBES[name]
    rows = []
    for n in [int(a) for a in args[1:]]:
        mine, maxe = bounds(n)
        t0 = time.time()
        new_lines, _ = run_generator(
            gen_args(GENC48, n, mine=mine, maxe=maxe, extra=switches))
        t1 = time.time()
        # stream side: read incrementally, keep only the C8-free graphs
        errpath = os.path.join(DATA, ".err_cc_%s_n%d.txt" % (name, n))
        os.makedirs(DATA, exist_ok=True)
        stream = 0
        kept = []
        with open(errpath, "w+") as errfh:
            proc = subprocess.Popen(
                gen_args(GENG, n, mine=mine, maxe=maxe, extra=switches),
                stdout=subprocess.PIPE, stderr=errfh, bufsize=1 << 20)
            for raw in proc.stdout:
                stream += 1
                line = raw.decode().strip()
                if not has_cycle_len(g6_decode(line), 8):
                    kept.append(line)
            assert proc.wait() == 0
        os.remove(errpath)
        equal = canonical_set(new_lines) == canonical_set(kept)
        row = {"probe": name, "switches": switches, "order": n,
               "mine": mine, "maxe": maxe,
               "genc48": len(new_lines), "geng_stream": stream,
               "geng_c8_free": len(kept), "set_equal": equal,
               "genc48_wall": round(t1 - t0, 1),
               "stream_wall": round(time.time() - t1, 1),
               "interpreter": interpreter()}
        assert equal, json.dumps(row, indent=1)
        rows.append(row)
        print("%s n=%2d genc48=%d  geng stream=%d -> C8-free=%d  set-equal=%s "
              "(%.1fs vs %.1fs)"
              % (name, n, row["genc48"], stream, len(kept), equal,
                 row["genc48_wall"], row["stream_wall"]))
    path = os.path.join(DATA, "crosscheck_%s.json" % name)
    old = []
    if os.path.exists(path):
        with open(path) as fh:
            old = json.load(fh)
    keep = [r for r in old if r["order"] not in {x["order"] for x in rows}]
    with open(path, "w") as fh:
        json.dump(sorted(keep + rows, key=lambda r: r["order"]), fh, indent=1)


def cmd_spotcheck(args):
    """Second-algorithm verification of the saved class: recompute the full
    cycle spectrum of every member with few degree-2 vertices by the
    brute-force enumerator (independent of has_cycle_len), and confirm
    4, 8 absent and the recorded C16 status."""
    n = int(args[0])
    limit = int(args[1]) if len(args) > 1 else 4
    rows = []
    paths = sorted(glob.glob(os.path.join(DATA, "class_n%d*.txt" % n)))
    assert paths, "no saved class files for order %d" % n
    for path in paths:
        with open(path) as fh:
            for line in fh:
                if line.startswith("#"):
                    continue
                g6, edges, n2, pf = line.split()
                if int(n2) > limit:
                    continue
                adjacency = g6_decode(g6)
                spec = cycle_spectrum_bruteforce(adjacency)
                assert 4 not in spec, "C4 in %s" % g6
                assert 8 not in spec, "C8 in %s" % g6
                assert (16 in spec) == (int(pf) == 0), \
                    "C16 status disagrees for %s" % g6
                rows.append({"g6": g6, "edges": int(edges),
                             "n_degree_2": int(n2), "power_free": int(pf) == 1,
                             "spectrum": sorted(spec)})
    out = os.path.join(DATA, "spotcheck_n%d.json" % n)
    with open(out, "w") as fh:
        json.dump({"order": n, "max_degree_2": limit, "checked": len(rows),
                   "interpreter": interpreter(), "graphs": rows}, fh, indent=1)
    print("spotcheck n=%d: %d graphs with <=%d degree-2 vertices re-verified by "
          "the brute-force spectrum enumerator (%s)"
          % (n, len(rows), limit, interpreter()))


def cmd_subcubic(args):
    """C027's own class, one instrument later: connected, C4-free, C8-free,
    minimum degree >= 1, at most two sub-cubic vertices (degree 1 or 2).
    C027 exhausted it through order 15 by filtering geng's stream."""
    for n in [int(a) for a in args]:
        mine = (3 * n - 4 + 1) // 2      # two degree-1 vertices, rest >= 3
        maxe = n * (n - 1) // 2
        gargs = gen_args(GENC48, n, mine=mine, maxe=maxe, extra=["-c", "-f", "-d1"])
        t0 = time.time()
        errpath = os.path.join(DATA, ".err_sub_n%d.txt" % n)
        os.makedirs(DATA, exist_ok=True)
        generated = 0
        by_profile = {}
        members = []
        with open(errpath, "w+") as errfh:
            proc = subprocess.Popen(gargs, stdout=subprocess.PIPE, stderr=errfh,
                                    bufsize=1 << 20)
            for raw in proc.stdout:
                generated += 1
                line = raw.decode().strip()
                adjacency = g6_decode(line)
                deg = degrees(adjacency)
                sub = sorted(d for d in deg if d < 3)
                if len(sub) > 2:
                    continue
                key = ",".join(str(d) for d in sub) or "none"
                by_profile[key] = by_profile.get(key, 0) + 1
                is_pf, present = power_free(adjacency)
                assert 4 not in present and 8 not in present, line
                members.append({"g6": line, "subcubic": sub,
                                "edges": sum(deg) // 2, "power_free": is_pf,
                                "power_lengths_present": present})
            code = proc.wait()
            errfh.seek(0)
            err = errfh.read()
        assert code == 0
        os.remove(errpath)
        total, _levels = parse_summary(err)
        pf = [m for m in members if m["power_free"]]
        row = {"order": n, "generator": " ".join(gargs), "mine": mine,
               "generated_c4c8_free": generated,
               "at_most_two_subcubic": len(members),
               "by_subcubic_profile": by_profile,
               "power_free": pf, "power_free_count": len(pf),
               "prune_calls": total.get("calls"),
               "wall": round(time.time() - t0, 1), "interpreter": interpreter()}
        with open(os.path.join(DATA, "subcubic_n%d.json" % n), "w") as fh:
            json.dump(row, fh, indent=1)
        print("n=%2d {C4,C8}-free=%d  <=2 sub-cubic=%d %s  power-free=%d  %.1fs"
              % (n, generated, len(members), by_profile, len(pf), row["wall"]))
        if pf:
            print(json.dumps(pf, indent=2))
            print("*** POWER-FREE MEMBER OF C027's CLASS AT ORDER %d ***" % n)


def cmd_run(args):
    verify_all = "--verify-all" in args
    args = [a for a in args if a != "--verify-all"]
    n = int(args[0])
    part = args[1] if len(args) > 1 else None
    tally = scan(n, part=part, verify_all=verify_all)
    os.makedirs(DATA, exist_ok=True)
    suffix = ("_part%s" % part.replace("/", "of")) if part else ""
    path = os.path.join(DATA, "scan_n%d%s.json" % (n, suffix))
    with open(path, "w") as fh:
        json.dump(tally, fh, indent=1)
    print("n=%d part=%s {C4,C8}-free=%d profile=%d c16_blocked=%d survivors=%d "
          "min#deg2=%s max_e=%d %.1fs -> %s"
          % (n, tally["part"], tally["generated_c4c8_free"], tally["profile"],
             tally["c16_blocked"], len(tally["survivors"]),
             tally["min_deg2_in_class"], tally["max_edges_in_class"],
             tally["seconds"], os.path.basename(path)))
    if n in KNOWN_EMPTY and part is None:
        assert tally["profile"] == 0, (
            "order %d profile class must be empty (C027/C036) but got %d"
            % (n, tally["profile"]))
        print("  reproduces the recorded emptiness at order %d" % n)
    if tally["survivors"]:
        print(json.dumps(tally["survivors"], indent=2))
        print("*** POWER-FREE PROFILE MEMBER AT ORDER %d — see JSON ***" % n)


def cmd_harvest(args):
    n = int(args[0])
    mod = int(args[1])
    total = {"generated_c4c8_free": 0, "profile": 0, "c16_blocked": 0}
    survivors = []
    max_e = 0
    max_e_class = 0
    deg2_hist = {}
    pf_deg2_hist = {}
    pf_exemplars = []
    seconds = 0.0
    levels = {}
    prune_calls = 0
    for r in range(mod):
        path = os.path.join(DATA, "scan_n%d_part%dof%d.json" % (n, r, mod))
        assert os.path.exists(path), "missing part %d/%d" % (r, mod)
        with open(path) as fh:
            tally = json.load(fh)
        assert tally["order"] == n and tally["part"] == "%d/%d" % (r, mod)
        for key in total:
            total[key] += tally[key]
        survivors.extend(tally["survivors"])
        max_e = max(max_e, tally["max_edges_in_profile"])
        max_e_class = max(max_e_class, tally["max_edges_in_class"])
        for k, v in tally["deg2_hist"].items():
            deg2_hist[int(k)] = deg2_hist.get(int(k), 0) + v
        for k, v in tally["power_free_deg2_hist"].items():
            pf_deg2_hist[int(k)] = pf_deg2_hist.get(int(k), 0) + v
        pf_exemplars.extend(tally["power_free_exemplars"])
        seconds += tally["seconds"]
        prune_calls += tally["prune_total"].get("calls", 0)
        for k, v in tally["prune_levels"].items():
            acc = levels.setdefault(k, {"calls": 0, "rejects": 0})
            acc["calls"] += v["calls"]
            acc["rejects"] += v["rejects"]
    # the coverage identity: in-profile {C4,C8}-free = C16-blocked + survivors
    assert total["profile"] == total["c16_blocked"] + len(survivors)
    result = {
        "order": n,
        "parts": mod,
        "generator": " ".join(gen_args(GENC48, n, extra=["-c", "-f", "-d2"],
                                       part="r/%d" % mod)),
        **total,
        "survivors": survivors,
        "max_edges_in_profile": max_e,
        "max_edges_in_class": max_e_class,
        "deg2_hist": {str(k): v for k, v in sorted(deg2_hist.items())},
        "min_deg2_in_class": min(deg2_hist) if deg2_hist else None,
        "power_free_in_class": sum(pf_deg2_hist.values()),
        "power_free_deg2_hist": {str(k): v for k, v in sorted(pf_deg2_hist.items())},
        "power_free_min_deg2": min(pf_deg2_hist) if pf_deg2_hist else None,
        "power_free_exemplars": pf_exemplars,
        "cpu_seconds_sum": round(seconds, 1),
        "prune_calls": prune_calls,
        "prune_levels": dict(sorted(levels.items(), key=lambda kv: int(kv[0]))),
    }
    out = os.path.join(DATA, "scan_n%d_harvest.json" % n)
    with open(out, "w") as fh:
        json.dump(result, fh, indent=1)
    print(json.dumps({k: v for k, v in result.items()
                      if k not in ("survivors", "prune_levels",
                                   "power_free_exemplars")}, indent=1))
    print("degree-2-vertex histogram over the {C4,C8}-free class: %s"
          % result["deg2_hist"])
    print("power-free members by degree-2 count: %s" % result["power_free_deg2_hist"])
    print("survivors: %d" % len(survivors))
    for s in survivors:
        print(json.dumps(s, indent=2))
    if not survivors:
        print("VERDICT: the order-%d G-profile class has no power-free member." % n)
    else:
        in_g = [s for s in survivors if s["in_G"]]
        print("VERDICT: %d power-free member(s), %d in G (S avoids {2,6,14})."
              % (len(survivors), len(in_g)))
        if in_g:
            print("*** G-MEMBER FOUND: tight 1-atom of order %d exists; "
                  "statement 0.1 is FALSE pending the disproof protocol ***" % (n + 1))


def main():
    cmds = {
        "anchors": cmd_anchors,
        "count": cmd_count,
        "probe": cmd_probe,
        "cubic24": cmd_cubic24,
        "subcubic": cmd_subcubic,
        "spotcheck": cmd_spotcheck,
        "crosscheck": cmd_crosscheck,
        "run": cmd_run,
        "harvest": cmd_harvest,
    }
    if len(sys.argv) < 2 or sys.argv[1] not in cmds:
        print(__doc__)
        sys.exit(1)
    cmds[sys.argv[1]](sys.argv[2:])


if __name__ == "__main__":
    main()
