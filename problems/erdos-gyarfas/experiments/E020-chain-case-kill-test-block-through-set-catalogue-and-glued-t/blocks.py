#!/usr/bin/env python3
"""E020 - chain-case kill test for the case-(5b) cut-vertex constraint system
(P-002, session S021, worker leg W1; serves attempt A022).

Question. The residual object of case (5b) (A019/L042), when H = B - u has a
cut vertex, is a chain of blocks whose prefix/suffix through-sets are forced
into membership constraints (A019 W1-T14; extended in A022 by the 1- and
0-closure batteries), while the total through-set S must avoid P-2 and meet
P and P-1.  Pre-registered kill condition for the arithmetic-only exclusion
route (S021 brief): exhibit a vertex-taut C4-free two-terminal graph WITH a
cut vertex, exactly two degree-2 vertices (the terminals), power-freeness
dropped, realizing the full forced constraint system.  This experiment
searches for such a witness constructively: catalogue small 2-connected
C4-free blocks with <= 2 degree-2 vertices (both terminal), compute their
through-sets, search the Minkowski arithmetic over realized through-set
pairs, then GLUE the best candidates at a cut vertex and verify every
constraint directly on the glued graph.

Constraint levels on a chain witness (names as in A022):
  L1 "kill"  - the pre-registered system: W1-T14 memberships at every cut
               (prefix/suffix meets P-2, bridge variant P-1), total S avoids
               P-2, total S meets P and meets P-1, plus the structural frame
               (profile, C4-free, taut, expected cuts).
  L2 "ext"   - adds A022's closure batteries at every cut: prefix/suffix
               meets (P-1 union {1}) [W1-T12 at the cut vertex] and meets
               (P union {1,2}) [terminal-merge 0-closures].
  L3 "full"  - adds the saturation batteries: Mersenne saturation at both
               terminals (W1-T12 pattern), power saturation at both
               terminals (A022 W1-T4), cut-vertex Mersenne saturation on
               each non-bridge side (A022 W1-T3(ii)), and, where a side has
               attachment degree >= 3, the total Mersenne / P-2-at-terminal
               / merge-power batteries (A022 W1-T3(iii)-(v)).

Graph primitives are copied verbatim from E018/scan.py (there in turn from
E015/bipscan.py, anchored against the independent E010 pipeline and the
recorded spectra of CLAIMS.md); paths_with_essential is copied verbatim from
E018/mod4.py.  Everything is re-anchored below (K4, K_{3,3}-e, Petersen,
Petersen-e, and the A014 T5 bridge composite as a new chain-level anchor).

Commands (run from the repository root):
    python3 .../blocks.py anchors
    python3 .../blocks.py catalogue [n ...]     # default 4..12
    python3 .../blocks.py search
    python3 .../blocks.py all                   # anchors + catalogue + search
Deterministic; no randomness; integers and integer bitmasks only.
"""

import itertools
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
GENG = "geng"

# --- primitives copied verbatim from E018/scan.py ----------------------------


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


def path_lengths(adjacency, a, b):
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


# --- copied verbatim from E018/mod4.py ---------------------------------------


def paths_with_essential(adjacency, a, b):
    """(set of simple a-b path lengths, mask of vertices on some a-b path)."""
    assert a != b
    out = set()
    essential = 0
    target = 1 << b
    stack = [(a, 1 << a, 0)]
    while stack:
        v, used, length = stack.pop()
        row = adjacency[v] & ~used
        if row & target:
            out.add(length + 1)
            essential |= used | target
        row &= ~target
        while row:
            low = row & -row
            w = low.bit_length() - 1
            row ^= low
            stack.append((w, used | low, length + 1))
    return out, essential


# --- arithmetic layer ---------------------------------------------------------

P_SET = frozenset({4, 8, 16, 32, 64})           # powers 2^k, k>=2
P_MINUS_1 = frozenset({3, 7, 15, 31, 63})       # Mersenne lengths
P_MINUS_2 = frozenset({2, 6, 14, 30, 62})       # forbidden through-lengths


def mask_of(values):
    m = 0
    for v in values:
        m |= 1 << v
    return m


P_MASK = mask_of(P_SET)
PM1_MASK = mask_of(P_MINUS_1)
PM2_MASK = mask_of(P_MINUS_2)
ONE_MASK = 1 << 1
TWO_MASK = 1 << 2


def minkowski(A, B):
    return {x + y for x in A for y in B}


def rev_targets(tmask, targets):
    """mask of {f - x : f in targets, x in T, f - x >= 1} for T given as mask."""
    out = 0
    row = tmask
    while row:
        low = row & -row
        x = low.bit_length() - 1
        row ^= low
        for f in targets:
            if f - x >= 1:
                out |= 1 << (f - x)
    return out


def chain_eval(tsets, bridges):
    """Set-level evaluation of the chain constraint system.

    tsets   : list of through-sets (sets of ints), blocks left to right
    bridges : list of bool, True where the block is a bridge (T must be {1})
    Returns (kill_ok, ext_ok, detail dict).  Constraint names:
      pre14/suf14@i : A019 W1-T14 memberships at cut i (1-based)
      mers_pre/suf@i: A022 closure battery, (P-1 union {1}) membership
      pow_pre/suf@i : A022 closure battery, (P union {1,2}) membership
      total_avoid / total_pow / total_mers
    """
    m = len(tsets)
    assert m >= 2 and len(bridges) == m
    for T, br in zip(tsets, bridges):
        if br:
            assert T == {1}
    detail = {}
    prefixes = [set(tsets[0])]
    for i in range(1, m):
        prefixes.append(minkowski(prefixes[-1], tsets[i]))
    suffixes = [set(tsets[-1])]
    for i in range(m - 2, -1, -1):
        suffixes.insert(0, minkowski(tsets[i], suffixes[0]))
    S = prefixes[-1]
    for i in range(1, m):            # cut c_i between block i-1 and block i (0-based)
        A = prefixes[i - 1]
        Z = suffixes[i]
        pre_bridge = bridges[i - 1]
        suf_bridge = bridges[i]
        detail["pre14@%d" % i] = bool(A & (P_MINUS_1 if pre_bridge else P_MINUS_2))
        detail["suf14@%d" % i] = bool(Z & (P_MINUS_1 if suf_bridge else P_MINUS_2))
        detail["mers_pre@%d" % i] = bool(A & P_MINUS_1) or (1 in A)
        detail["mers_suf@%d" % i] = bool(Z & P_MINUS_1) or (1 in Z)
        detail["pow_pre@%d" % i] = bool(A & P_SET) or (1 in A) or (2 in A)
        detail["pow_suf@%d" % i] = bool(Z & P_SET) or (1 in Z) or (2 in Z)
    detail["total_avoid"] = not (S & P_MINUS_2)
    detail["total_pow"] = bool(S & P_SET)
    detail["total_mers"] = bool(S & P_MINUS_1)
    kill_names = [k for k in detail
                  if k.startswith("pre14") or k.startswith("suf14")
                  or k.startswith("total")]
    ext_names = list(detail)
    kill_ok = all(detail[k] for k in kill_names)
    ext_ok = all(detail[k] for k in ext_names)
    return kill_ok, ext_ok, detail


# --- construction -------------------------------------------------------------


def glue2(adj1, x1, y1, adj2, x2, y2):
    """Identify y1 (block 1) with x2 (block 2).  Returns (adj, a, b, c)."""
    n1, n2 = len(adj1), len(adj2)
    remap = {}
    nxt = n1
    for v in range(n2):
        if v == x2:
            remap[v] = y1
        else:
            remap[v] = nxt
            nxt += 1
    edges = []
    for u in range(n1):
        row = adj1[u] & ~((1 << (u + 1)) - 1)
        while row:
            low = row & -row
            v = low.bit_length() - 1
            row ^= low
            edges.append((u, v))
    for u in range(n2):
        row = adj2[u] & ~((1 << (u + 1)) - 1)
        while row:
            low = row & -row
            v = low.bit_length() - 1
            row ^= low
            edges.append((remap[u], remap[v]))
    adj = from_edges(n1 + n2 - 1, edges)
    return adj, x1, remap[y2], y1


def glue_bridge(adj1, x1, y1, adj2, x2, y2):
    """Join y1 (block 1) to x2 (block 2) by a bridge.  (adj, a, b, c1, c2)."""
    n1, n2 = len(adj1), len(adj2)
    edges = []
    for u in range(n1):
        row = adj1[u] & ~((1 << (u + 1)) - 1)
        while row:
            low = row & -row
            v = low.bit_length() - 1
            row ^= low
            edges.append((u, v))
    for u in range(n2):
        row = adj2[u] & ~((1 << (u + 1)) - 1)
        while row:
            low = row & -row
            v = low.bit_length() - 1
            row ^= low
            edges.append((n1 + u, n1 + v))
    edges.append((y1, n1 + x2))
    adj = from_edges(n1 + n2, edges)
    return adj, x1, n1 + y2, y1, n1 + x2


# --- the graph-level verifier ---------------------------------------------------


def component_mask(adjacency, start, banned):
    seen = 1 << start
    stack = [start]
    while stack:
        u = stack.pop()
        row = adjacency[u] & ~seen & ~banned
        while row:
            low = row & -row
            v = low.bit_length() - 1
            row ^= low
            seen |= low
            stack.append(v)
    return seen


def iter_bits(mask):
    while mask:
        low = mask & -mask
        mask ^= low
        yield low.bit_length() - 1


def analyze_witness(adj, a, b, expect_cuts):
    """Verify every chain-case constraint directly on the glued graph."""
    n = len(adj)
    full = (1 << n) - 1
    deg = degrees(adj)
    checks = {}
    checks["connected"] = component_mask(adj, 0, 0) == full
    checks["c4_free"] = not has_c4(adj)
    two = sorted(v for v in range(n) if deg[v] == 2)
    checks["profile"] = (two == sorted((a, b)) and min(deg) >= 2)
    cuts = cut_vertices(adj)
    checks["cuts_as_expected"] = sorted(cuts) == sorted(expect_cuts)
    S, ess = paths_with_essential(adj, a, b)
    checks["taut"] = ess == full
    checks["total_avoid"] = not (S & P_MINUS_2)
    checks["total_pow"] = bool(S & P_SET)
    checks["total_mers"] = bool(S & P_MINUS_1)
    pathcache = {}

    def P(x, y):
        key = (x, y) if x < y else (y, x)
        if key not in pathcache:
            pathcache[key] = path_lengths(adj, key[0], key[1])
        return pathcache[key]

    per_cut = {}
    for c in expect_cuts:
        banned = 1 << c
        side_a = component_mask(adj, a, banned) & ~banned
        side_b = component_mask(adj, b, banned) & ~banned
        assert side_a & side_b == 0
        d_pre = (adj[c] & side_a).bit_count()
        d_suf = (adj[c] & side_b).bit_count()
        A = P(a, c)
        Z = P(c, b)
        info = {"c": c, "d_pre": d_pre, "d_suf": d_suf,
                "A": sorted(A), "Z": sorted(Z)}
        checks["minkowski@%d" % c] = (S == minkowski(A, Z))
        checks["pre14@%d" % c] = bool(A & (P_MINUS_2 if d_pre >= 2 else P_MINUS_1))
        checks["suf14@%d" % c] = bool(Z & (P_MINUS_2 if d_suf >= 2 else P_MINUS_1))
        checks["mers_pre@%d" % c] = (1 in A) or bool(A & P_MINUS_1)
        checks["mers_suf@%d" % c] = (1 in Z) or bool(Z & P_MINUS_1)
        checks["pow_pre@%d" % c] = (1 in A) or (2 in A) or bool(A & P_SET)
        checks["pow_suf@%d" % c] = (1 in Z) or (2 in Z) or bool(Z & P_SET)
        # cut-vertex Mersenne saturation (A022 W1-T3(ii)), per non-bridge side
        if d_pre >= 2:
            ok = True
            for x in iter_bits(side_a & ~(1 << a) & ~adj[c]):
                if not (P(x, c) & P_MINUS_1):
                    ok = False
                    break
            checks["cutsat_pre@%d" % c] = ok
        if d_suf >= 2:
            ok = True
            for x in iter_bits(side_b & ~(1 << b) & ~adj[c]):
                if not (P(x, c) & P_MINUS_1):
                    ok = False
                    break
            checks["cutsat_suf@%d" % c] = ok
        # cut-vertex power saturation (A022 W1-T3(v) with c in the pair),
        # per non-bridge side: merge x with c inside the side graph
        for tag, side, dside, term in (("pre", side_a, d_pre, a),
                                       ("suf", side_b, d_suf, b)):
            if dside < 2:
                continue
            hyp = (1 << c) | side
            ok = True
            for x in iter_bits(side & ~(1 << term) & ~adj[c]):
                if adj[x] & adj[c] & hyp:
                    continue                 # common neighbour inside the side
                if not (P(x, c) & P_SET):
                    ok = False
                    break
            checks["cutpow_%s@%d" % (tag, c)] = ok
        # d>=3 batteries (A022 W1-T3(iii)-(v)) on whichever sides qualify
        for tag, side, dside, term in (("pre", side_a, d_pre, a),
                                       ("suf", side_b, d_suf, b)):
            if dside < 3:
                continue
            side_vertices = [v for v in iter_bits(side | (1 << c)) if v != term]
            hyp1 = (1 << c) | side          # vertex set of the side graph
            ok_m = ok_p2 = ok_pw = True
            for x in side_vertices:
                if not (P(term, x) & P_MINUS_2):
                    ok_p2 = False
                    break
            for x, y in itertools.combinations(side_vertices, 2):
                if adj[x] >> y & 1:
                    continue
                if not (P(x, y) & P_MINUS_1):
                    ok_m = False
                    break
            for x, y in itertools.combinations(side_vertices, 2):
                if adj[x] >> y & 1:
                    continue
                if adj[x] & adj[y] & hyp1:
                    continue                 # common neighbour inside the side
                if not (P(x, y) & P_SET):
                    ok_pw = False
                    break
            checks["d3_pm2_at_term_%s@%d" % (tag, c)] = ok_p2
            checks["d3_mers_all_%s@%d" % (tag, c)] = ok_m
            checks["d3_pow_all_%s@%d" % (tag, c)] = ok_pw
        per_cut[c] = info
    # terminal saturations on the whole graph
    for tag, term, other in (("a", a, b), ("b", b, a)):
        ok = True
        for z in range(n):
            if z == term or adj[term] >> z & 1:
                continue
            if not (P(term, z) & P_MINUS_1):
                ok = False
                break
        checks["sat_%s" % tag] = ok                      # W1-T12 pattern
        ok = True
        for z in range(n):
            if z in (term, other) or adj[term] >> z & 1:
                continue
            if adj[term] & adj[z]:
                continue
            if not (P(term, z) & P_SET):
                ok = False
                break
        checks["powsat_%s" % tag] = ok                   # A022 W1-T4
    frame = ["connected", "c4_free", "profile", "cuts_as_expected", "taut"]
    kill_names = frame + [k for k in checks
                          if k.startswith(("pre14", "suf14", "total", "minkowski"))]
    ext_names = kill_names + [k for k in checks
                              if k.startswith(("mers_", "pow_"))]
    full_names = list(checks)
    result = {
        "n": n, "a": a, "b": b, "cuts": expect_cuts,
        "S": sorted(S),
        "per_cut": per_cut,
        "bipartite": bipartition(adj) is not None,
        "checks": checks,
        "L1_kill": all(checks[k] for k in kill_names),
        "L2_ext": all(checks[k] for k in ext_names),
        "L3_full": all(checks[k] for k in full_names),
        "failed": sorted(k for k in checks if not checks[k]),
    }
    return result


def g6_encode(adjacency):
    n = len(adjacency)
    assert n < 63
    bits = []
    for j in range(1, n):
        for i in range(j):
            bits.append(adjacency[i] >> j & 1)
    while len(bits) % 6:
        bits.append(0)
    out = [chr(n + 63)]
    for k in range(0, len(bits), 6):
        val = 0
        for bit in bits[k:k + 6]:
            val = val << 1 | bit
        out.append(chr(val + 63))
    return "".join(out)


# --- block catalogue ------------------------------------------------------------


def geng_args(n):
    mine = (3 * n - 2 + 1) // 2
    maxe = n * (n - 1) // 2
    return [GENG, "-q", "-c", "-f", "-d2", str(n), "%d:%d" % (mine, maxe)]


def catalogue_order(n, two_only=False):
    """Enumerate taut 2-connected C4-free blocks with <=2 degree-2 vertices.

    two_only: restrict to the exactly-two-degree-2 profile (one terminal
    pair per graph) - used at order 14, where the one-/zero-degree-2 pair
    enumeration is beyond this experiment's CPython budget.  The stream and
    le2deg2 counters still count the full class."""
    t0 = time.time()
    proc = subprocess.Popen(geng_args(n), stdout=subprocess.PIPE, bufsize=1 << 20)
    stream = le2 = twodeg2 = twoconn = 0
    records = []
    assert proc.stdout is not None
    for line in proc.stdout:
        stream += 1
        adj = g6_decode(line.decode())
        deg = degrees(adj)
        twos = [v for v in range(n) if deg[v] == 2]
        if len(twos) > 2:
            continue
        le2 += 1
        if len(twos) == 2:
            twodeg2 += 1
        if two_only and len(twos) != 2:
            continue
        if cut_vertices(adj):
            continue
        twoconn += 1
        g6 = line.decode().strip()
        if len(twos) == 2:
            pairs = [(twos[0], twos[1])]
        elif len(twos) == 1:
            pairs = [(twos[0], y) for y in range(n) if y != twos[0]]
        else:
            pairs = list(itertools.combinations(range(n), 2))
        for x, y in pairs:
            T, ess = paths_with_essential(adj, x, y)
            if ess != (1 << n) - 1:
                continue
            records.append({"n": n, "g6": g6, "x": x, "y": y,
                            "dx": deg[x], "dy": deg[y], "T": sorted(T)})
    proc.wait()
    assert proc.returncode == 0
    out = {"n": n, "geng": " ".join(geng_args(n)), "stream": stream,
           "two_only": two_only,
           "le2deg2": le2, "exactly2deg2": twodeg2, "twoconn_le2deg2": twoconn,
           "taut_terminal_pairs": len(records),
           "end_usable": sum(1 for r in records if min(r["dx"], r["dy"]) == 2),
           "seconds": round(time.time() - t0, 1), "records": records}
    os.makedirs(DATA, exist_ok=True)
    with open(os.path.join(DATA, "catalogue_n%d.json" % n), "w") as fh:
        json.dump(out, fh)
    print("n=%2d stream=%8d le2deg2=%7d 2conn=%6d tautpairs=%6d end=%6d  %.1fs"
          % (n, stream, le2, twoconn, len(records), out["end_usable"],
             out["seconds"]))
    return out


# --- the search -------------------------------------------------------------------


def load_catalogues():
    records = []
    counts = {}
    for name in sorted(os.listdir(DATA)):
        if not name.startswith("catalogue_n"):
            continue
        with open(os.path.join(DATA, name)) as fh:
            payload = json.load(fh)
        counts[payload["n"]] = {k: payload[k] for k in
                                ("stream", "le2deg2", "exactly2deg2",
                                 "twoconn_le2deg2", "taut_terminal_pairs",
                                 "end_usable")}
        records.extend(payload["records"])
    return records, counts


def end_table(records):
    """Distinct end-usable through-sets -> up to 3 smallest block witnesses."""
    table = {}
    for r in sorted(records, key=lambda r: (r["n"], r["g6"])):
        if min(r["dx"], r["dy"]) != 2:
            continue
        x, y = r["x"], r["y"]
        dx, dy = r["dx"], r["dy"]
        if dx != 2:
            x, y = y, x
            dx, dy = dy, dx
        key = frozenset(r["T"])
        table.setdefault(key, [])
        if len(table[key]) < 3:
            table[key].append({"n": r["n"], "g6": r["g6"], "x": x, "y": y,
                               "dy": dy, "T": sorted(key)})
    return table


def pair_search(table):
    """All unordered pairs {T1,T2} of realized end through-sets, both meeting
    P-2, whose Minkowski sum avoids P-2 and meets P and P-1 (kill level);
    ext level additionally requires each T to meet (P-1 u {1}) and (P u {1,2})."""
    keys = sorted(table, key=lambda k: (table[k][0]["n"], sorted(k)))
    masks = {k: mask_of(k) for k in keys}
    hits = []
    for i, k1 in enumerate(keys):
        m1 = masks[k1]
        if not m1 & PM2_MASK:
            continue
        d1 = rev_targets(m1, P_MINUS_2)
        pw1 = rev_targets(m1, P_SET)
        mr1 = rev_targets(m1, P_MINUS_1)
        for k2 in keys[i:]:
            m2 = masks[k2]
            if not m2 & PM2_MASK:
                continue
            if m2 & d1:
                continue                      # total S would meet P-2
            if not m2 & pw1:
                continue                      # total S must meet P
            if not m2 & mr1:
                continue                      # total S must meet P-1
            ext = all(m & (PM1_MASK | ONE_MASK) and
                      m & (P_MASK | ONE_MASK | TWO_MASK)
                      for m in (m1, m2))
            order = table[k1][0]["n"] + table[k2][0]["n"] - 1
            hits.append({"T1": sorted(k1), "T2": sorted(k2),
                         "order": order, "ext": ext})
    hits.sort(key=lambda h: (h["order"], not h["ext"], h["T1"], h["T2"]))
    return hits


def bridge_search(table):
    """[end, bridge, end] chains: set-level evaluation via chain_eval."""
    keys = sorted(table, key=lambda k: (table[k][0]["n"], sorted(k)))
    hits = []
    for i, k1 in enumerate(keys):
        if not mask_of(k1) & PM2_MASK:
            continue
        for k2 in keys[i:]:
            if not mask_of(k2) & PM2_MASK:
                continue
            kill_ok, ext_ok, _ = chain_eval([set(k1), {1}, set(k2)],
                                            [False, True, False])
            if kill_ok:
                order = table[k1][0]["n"] + table[k2][0]["n"]
                hits.append({"T1": sorted(k1), "T2": sorted(k2),
                             "order": order, "ext": ext_ok})
    hits.sort(key=lambda h: (h["order"], not h["ext"], h["T1"], h["T2"]))
    return hits


def mid_table(records):
    """Distinct mid-usable through-sets -> up to 3 smallest block witnesses.
    A mid block's terminals are both cut vertices; any taut catalogued block
    qualifies (its degree-2 vertices, if any, are terminals by construction)."""
    table = {}
    for r in sorted(records, key=lambda r: (r["n"], r["g6"])):
        key = frozenset(r["T"])
        table.setdefault(key, [])
        if len(table[key]) < 3:
            table[key].append({"n": r["n"], "g6": r["g6"], "x": r["x"],
                               "y": r["y"], "T": sorted(key)})
    return table


def mid_search(end_tbl, mid_tbl):
    """[end, mid, end] chains, all blocks 2-connected: set-level evaluation.

    Necessary memberships used as prefilters: T1 and T3 meet P-2 (W1-T14 at
    c1 prefix / c2 suffix); the full system is chain_eval."""
    end_keys = sorted((k for k in end_tbl if set(k) & P_MINUS_2),
                      key=lambda k: (end_tbl[k][0]["n"], sorted(k)))
    mid_keys = sorted(mid_tbl, key=lambda k: (mid_tbl[k][0]["n"], sorted(k)))
    mid_masks = [(k, mask_of(k)) for k in mid_keys]
    revs = {k: rev_targets(mask_of(k), P_MINUS_2) for k in end_keys}
    hits = []
    for i, k1 in enumerate(end_keys):
        r1 = revs[k1]
        for k3 in end_keys[i:]:
            r3 = revs[k3]
            base = end_tbl[k1][0]["n"] + end_tbl[k3][0]["n"]
            for k2, m2 in mid_masks:
                if not (m2 & r1):        # A_2 = T1+T2 must meet P-2
                    continue
                if not (m2 & r3):        # Z_1 = T2+T3 must meet P-2
                    continue
                kill_ok, ext_ok, _ = chain_eval([set(k1), set(k2), set(k3)],
                                                [False, False, False])
                if kill_ok:
                    order = base + mid_tbl[k2][0]["n"] - 2
                    hits.append({"T1": sorted(k1), "T2": sorted(k2),
                                 "T3": sorted(k3), "order": order,
                                 "ext": ext_ok})
    hits.sort(key=lambda h: (h["order"], not h["ext"], h["T1"], h["T2"]))
    return hits


def glue3(w1, w2, w3):
    """[end, mid, end]: identify w1.y with w2.x and w2.y with w3.y (w3.x is b)."""
    adjA = g6_decode(w1["g6"])
    adjB = g6_decode(w2["g6"])
    adjC = g6_decode(w3["g6"])
    adjAB, a, yB, c1 = glue2(adjA, w1["x"], w1["y"], adjB, w2["x"], w2["y"])
    adjABC, a2, b, c2 = glue2(adjAB, a, yB, adjC, w3["y"], w3["x"])
    assert a2 == a
    return adjABC, a, b, c1, c2


def verify_hits(table, hits, kind, budget):
    """Glue and fully verify candidate pairs; return verified witnesses."""
    verified = []
    for h in hits[:budget]:
        w1 = table[frozenset(h["T1"])][0]
        w2 = table[frozenset(h["T2"])][0]
        adj1 = g6_decode(w1["g6"])
        adj2 = g6_decode(w2["g6"])
        if kind == "m2":
            adj, a, b, c = glue2(adj1, w1["x"], w1["y"], adj2, w2["y"], w2["x"])
            expect = [c]
        else:
            adj, a, b, c1, c2 = glue_bridge(adj1, w1["x"], w1["y"],
                                            adj2, w2["y"], w2["x"])
            expect = [c1, c2]
        res = analyze_witness(adj, a, b, expect)
        res["kind"] = kind
        res["blocks"] = [w1, w2]
        res["g6"] = g6_encode(adj)
        verified.append(res)
    return verified


def cmd_search(_args):
    records, counts = load_catalogues()
    table = end_table(records)
    mids = mid_table(records)
    print("catalogue: %d taut terminal pairs, %d distinct end through-sets, "
          "%d distinct mid through-sets"
          % (len(records), len(table), len(mids)))
    t0 = time.time()
    hits2 = pair_search(table)
    hits3 = bridge_search(table)
    print("m=2 pairs passing kill level: %d (ext level: %d)  [%.1fs]"
          % (len(hits2), sum(h["ext"] for h in hits2), time.time() - t0))
    print("m=3-bridge pairs passing kill level: %d (ext level: %d)"
          % (len(hits3), sum(h["ext"] for h in hits3)))
    t0 = time.time()
    hits3m = mid_search(table, mids)
    print("m=3-mid triples passing kill level: %d (ext level: %d)  [%.1fs]"
          % (len(hits3m), sum(h["ext"] for h in hits3m), time.time() - t0))
    result = {"counts_by_order": counts,
              "distinct_end_T": len(table),
              "distinct_mid_T": len(mids),
              "m2_kill_pairs": len(hits2),
              "m2_ext_pairs": sum(h["ext"] for h in hits2),
              "m3_kill_pairs": len(hits3),
              "m3_ext_pairs": sum(h["ext"] for h in hits3),
              "m3mid_kill_triples": len(hits3m),
              "m3mid_ext_triples": sum(h["ext"] for h in hits3m),
              "m2_first_hits": hits2[:25], "m3_first_hits": hits3[:25],
              "m3mid_first_hits": hits3m[:25]}
    verified = verify_hits(table, hits2, "m2", 40)
    verified += verify_hits(table, hits3, "m3bridge", 10)
    for h in hits3m[:15]:
        w1 = table[frozenset(h["T1"])][0]
        w2 = mids[frozenset(h["T2"])][0]
        w3 = table[frozenset(h["T3"])][0]
        adj, a, b, c1, c2 = glue3(w1, w2, w3)
        res = analyze_witness(adj, a, b, [c1, c2])
        res["kind"] = "m3mid"
        res["blocks"] = [w1, w2, w3]
        res["g6"] = g6_encode(adj)
        verified.append(res)
    best = {}
    for level in ("L1_kill", "L2_ext", "L3_full"):
        good = [v for v in verified if v[level]]
        good.sort(key=lambda v: v["n"])
        best[level] = good[0] if good else None
    result["verified"] = verified
    result["best"] = best
    os.makedirs(DATA, exist_ok=True)
    with open(os.path.join(DATA, "search_results.json"), "w") as fh:
        json.dump(result, fh, indent=1)
    for level in ("L1_kill", "L2_ext", "L3_full"):
        w = best[level]
        if w is None:
            print("%s: NO verified witness among examined candidates" % level)
        else:
            print("%s: VERIFIED witness  order=%d kind=%s  S=%s  g6=%s"
                  % (level, w["n"], w["kind"], w["S"], w["g6"]))
            print("    blocks: %s" % json.dumps(w["blocks"]))
            if w["failed"]:
                print("    failed checks: %s" % w["failed"])
    return result


# --- anchors --------------------------------------------------------------------


def petersen():
    edges = [(i, (i + 1) % 5) for i in range(5)]
    edges += [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
    edges += [(i, 5 + i) for i in range(5)]
    return from_edges(10, edges)


def petersen_minus_e():
    adj = petersen()
    adj[0] &= ~(1 << 1)
    adj[1] &= ~(1 << 0)
    return adj


def cmd_anchors(_args):
    failures = 0

    def check(name, ok):
        nonlocal failures
        print("%-52s %s" % (name, "ok" if ok else "FAIL"))
        if not ok:
            failures += 1

    k4 = from_edges(4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
    check("A1 K4 has a C4 and spectrum {3,4}",
          has_c4(k4) and cycle_spectrum_bruteforce(k4) == {3, 4})
    k33e = from_edges(6, [(u, v) for u in range(3) for v in range(3, 6)
                          if (u, v) != (0, 3)])
    check("A2 K33-e S(0,3)={3,5}, spectrum {4,6}",
          path_lengths(k33e, 0, 3) == {3, 5}
          and cycle_spectrum_bruteforce(k33e) == {4, 6})
    pet = petersen()
    check("A3 Petersen spectrum {5,6,8,9}, 3-regular, C4-free",
          cycle_spectrum_bruteforce(pet) == {5, 6, 8, 9}
          and degrees(pet) == [3] * 10 and not has_c4(pet))
    pe = petersen_minus_e()
    Tpe, ess = paths_with_essential(pe, 0, 1)
    check("A4 Petersen-e: S={4,5,7,8}, taut, 2-connected, non-bip",
          Tpe == {4, 5, 7, 8} and ess == (1 << 10) - 1
          and not cut_vertices(pe) and bipartition(pe) is None)
    comp, a, b, c1, c2 = glue_bridge(pe, 0, 1, pe, 0, 1)
    Scomp = path_lengths(comp, a, b)
    check("A5 A014-T5 composite: order 20, S={9..17}, spec {5,6,8,9}",
          len(comp) == 20 and Scomp == set(range(9, 18))
          and cycle_spectrum_bruteforce(comp) == {5, 6, 8, 9})
    deg = degrees(comp)
    check("A5b composite: cuts exactly the bridge ends, profile, taut",
          sorted(cut_vertices(comp)) == sorted((c1, c2))
          and sorted(v for v in range(20) if deg[v] == 2) == sorted((a, b))
          and paths_with_essential(comp, a, b)[1] == (1 << 20) - 1)
    kill_ok, ext_ok, detail = chain_eval([{4, 5, 7, 8}, {1}, {4, 5, 7, 8}],
                                         [False, True, False])
    # 5 pre-registered failures (both W1-T14 memberships at both cuts, and
    # the total P-2 avoidance), plus the two ext-level Mersenne constraints
    # that coincide with the W1-T14 bridge constraints at the bridge cuts
    # (1 is never in A_2 = T1+1 or Z_1 = T3+1, so the {1}-escape is vacuous).
    expected_fail = {"pre14@1", "suf14@1", "pre14@2", "suf14@2", "total_avoid",
                     "mers_suf@1", "mers_pre@2"}
    actual_fail = {k for k, v in detail.items() if not v}
    check("A6 chain_eval on the composite fails exactly the 7 recorded",
          not kill_ok and actual_fail == expected_fail)
    res = analyze_witness(comp, a, b, [c1, c2])
    graph_fail = {k for k in res["failed"]
                  if k.split("@")[0] in ("pre14", "suf14", "total_avoid")
                  or k == "total_avoid"}
    check("A7 graph-level verifier agrees on the composite's failures",
          not res["L1_kill"]
          and {k.split("@")[0] for k in res["failed"]}
          >= {"pre14", "suf14", "total_avoid"}
          and res["checks"]["minkowski@%d" % c1]
          and res["checks"]["minkowski@%d" % c2]
          and res["checks"]["taut"])
    check("A8 Minkowski identity S = A+Z at both composite cuts",
          Scomp == minkowski(path_lengths(comp, a, c1), path_lengths(comp, c1, b))
          and Scomp == minkowski(path_lengths(comp, a, c2),
                                 path_lengths(comp, c2, b)))
    check("A9 rev_targets/collision arithmetic: (P-2)+(P-2) misses P-2",
          all((x + y) not in P_MINUS_2
              for x in P_MINUS_2 for y in P_MINUS_2 if x + y <= 64))
    check("A9b same-exponent collisions land in P-2",
          all((2 ** t - 1) + (2 ** t - 1) in P_MINUS_2 for t in range(2, 5))
          and all(2 ** t + (2 ** t - 2) in P_MINUS_2 for t in range(2, 5)))
    g6 = g6_encode(pe)
    check("A10 g6 encode/decode roundtrip on Petersen-e",
          g6_decode(g6) == pe)
    print("anchors: %d failure(s)" % failures)
    return failures


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    cmd = sys.argv[1]
    args = sys.argv[2:]
    if cmd == "anchors":
        return 1 if cmd_anchors(args) else 0
    if cmd == "catalogue":
        two_only = "--two-only" in args
        orders = [int(x) for x in args if not x.startswith("--")] \
            or list(range(4, 13))
        for n in orders:
            catalogue_order(n, two_only=two_only)
        return 0
    if cmd == "search":
        cmd_search(args)
        return 0
    if cmd == "all":
        if cmd_anchors([]):
            return 1
        for n in range(4, 13):
            catalogue_order(n)
        cmd_search([])
        return 0
    print("unknown command %r" % cmd)
    return 2


if __name__ == "__main__":
    sys.exit(main())
