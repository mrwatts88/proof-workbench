#!/usr/bin/env python3
"""E016 - verification of the 1-atom closure correspondence and the minimality
reductions used in A019 (session S019, worker W1).

All computations are exact, exhaustive and deterministic: no randomness, no
sampling, no heuristics.  Graph generation is delegated to nauty's ``geng``
(anchored below against the recorded ``C027`` stream counts); every graph
property is recomputed from scratch by explicit enumeration.

Checks
------
A1  closure identity        Spec(H +_j ab) = Spec(H) u (S(H,a,b) + j), j=0,1,2
A2  case dichotomy          degree bookkeeping of B-u in every A019 case
A3  saturation construction H + az is tight-1-atom-shaped, spectrum identity
A4  C027 stream anchor      stream counts at orders 6-11 and universal C8
A5  fixed anchors           K4, K_{3,3}-e, Petersen, Petersen-e spectra

Usage:  python3 verify.py [all|a1|a2|a3|a4|a5]
"""

from __future__ import annotations

import subprocess
import sys
import time
from itertools import combinations

GENG = "geng"

# --------------------------------------------------------------------------
# graph6 decoding and exact enumeration primitives
# --------------------------------------------------------------------------


def parse_graph6(line: str):
    """Return adjacency-set list for a graph6 string (orders < 63 only)."""
    s = line.strip()
    if s.startswith(">>graph6<<"):
        s = s[10:]
    data = [ord(c) - 63 for c in s]
    n = data[0]
    if n >= 63:
        raise ValueError("order >= 63 not supported")
    bits = []
    for d in data[1:]:
        for i in range(5, -1, -1):
            bits.append((d >> i) & 1)
    adj = [set() for _ in range(n)]
    k = 0
    for j in range(1, n):
        for i in range(j):
            if bits[k]:
                adj[i].add(j)
                adj[j].add(i)
            k += 1
    return adj


def erange(mine, n):
    """geng edge-range token.  NOTE: a bare "m:" is parsed by geng as the exact
    edge count m, so the upper bound must be written out explicitly."""
    return "%d:%d" % (mine, n * (n - 1) // 2)


def geng_stream(args):
    """Yield adjacency lists from `geng -q <args>`."""
    proc = subprocess.Popen(
        [GENG, "-q"] + [str(a) for a in args],
        stdout=subprocess.PIPE,
        text=True,
    )
    assert proc.stdout is not None
    for line in proc.stdout:
        if line.strip():
            yield parse_graph6(line)
    proc.stdout.close()
    rc = proc.wait()
    if rc != 0:
        raise RuntimeError("geng failed with code %d" % rc)


def spectrum(adj):
    """Exact set of cycle lengths (>=3) of a simple graph."""
    n = len(adj)
    lengths = set()

    for v in range(n):
        path = [v]
        visited = {v}

        def dfs(cur):
            for w in adj[cur]:
                if w == v:
                    if len(path) >= 3:
                        lengths.add(len(path))
                elif w > v and w not in visited:
                    visited.add(w)
                    path.append(w)
                    dfs(w)
                    path.pop()
                    visited.remove(w)

        dfs(v)
    return lengths


def path_lengths(adj, a, b):
    """Exact set of lengths (in edges) of simple a-b paths."""
    if a == b:
        return set()
    out = set()
    visited = {a}

    def dfs(cur, length):
        for w in adj[cur]:
            if w == b:
                out.add(length + 1)
            elif w not in visited:
                visited.add(w)
                dfs(w, length + 1)
                visited.remove(w)

    dfs(a, 0)
    return out


def spectrum_missing_one(adj, a, b):
    """Lengths of cycles that do NOT contain both a and b."""
    n = len(adj)
    lengths = set()

    for v in range(n):
        path = [v]
        visited = {v}

        def dfs(cur):
            for w in adj[cur]:
                if w == v:
                    if len(path) >= 3 and not (a in visited and b in visited):
                        lengths.add(len(path))
                elif w > v and w not in visited:
                    visited.add(w)
                    path.append(w)
                    dfs(w)
                    path.pop()
                    visited.remove(w)

        dfs(v)
    return lengths


def degrees(adj):
    return [len(s) for s in adj]


def is_connected(adj):
    n = len(adj)
    if n == 0:
        return True
    seen = {0}
    stack = [0]
    while stack:
        v = stack.pop()
        for w in adj[v]:
            if w not in seen:
                seen.add(w)
                stack.append(w)
    return len(seen) == n


def components(adj):
    """Return list of vertex sets of the connected components."""
    n = len(adj)
    seen = set()
    out = []
    for s in range(n):
        if s in seen:
            continue
        comp = {s}
        stack = [s]
        seen.add(s)
        while stack:
            v = stack.pop()
            for w in adj[v]:
                if w not in seen:
                    seen.add(w)
                    comp.add(w)
                    stack.append(w)
        out.append(comp)
    return out


def induced(adj, keep):
    """Induced subgraph on the sorted vertex set `keep`; returns adjacency list."""
    order = sorted(keep)
    index = {v: i for i, v in enumerate(order)}
    sub = [set() for _ in order]
    for v in order:
        for w in adj[v]:
            if w in index:
                sub[index[v]].add(index[w])
    return sub


def add_edge(adj, x, y):
    new = [set(s) for s in adj]
    new[x].add(y)
    new[y].add(x)
    return new


def add_apex(adj, x, y):
    """H + u with N(u) = {x, y}; u is the new last vertex."""
    new = [set(s) for s in adj]
    u = len(new)
    new.append({x, y})
    new[x].add(u)
    new[y].add(u)
    return new


def identify(adj, x, y):
    """H/(x=y).  Requires xy not an edge and no common neighbour (simplicity)."""
    assert y not in adj[x]
    assert not (adj[x] & adj[y])
    n = len(adj)
    keep = [v for v in range(n) if v != y]
    index = {v: i for i, v in enumerate(keep)}
    new = [set() for _ in keep]
    for v in keep:
        for w in adj[v]:
            t = x if w == y else w
            if t != v:
                new[index[v]].add(index[t])
    for w in adj[y]:
        if w != x:
            new[index[x]].add(index[w])
            new[index[w]].add(index[x])
    return new


POWERS = {2 ** k for k in range(2, 12)}


def power_free(spec):
    return not (spec & POWERS)


# --------------------------------------------------------------------------
# A1 - the closure identity
# --------------------------------------------------------------------------


def check_a1(max_order=8):
    """Spec(B_j) = Spec(H) u (S + j) for j = 2 (apex), 1 (edge), 0 (identify)."""
    total = 0
    pairs = 0
    for n in range(4, max_order + 1):
        for adj in geng_stream(["-c", n]):
            total += 1
            spec_h = spectrum(adj)
            for a, b in combinations(range(n), 2):
                S = path_lengths(adj, a, b)
                pairs += 1
                # j = 2: always legal
                b2 = add_apex(adj, a, b)
                assert spectrum(b2) == spec_h | {s + 2 for s in S}, (n, a, b, "j2")
                # j = 1: legal iff ab is not already an edge
                if b not in adj[a]:
                    b1 = add_edge(adj, a, b)
                    assert spectrum(b1) == spec_h | {s + 1 for s in S}, (n, a, b, "j1")
                    # j = 0: legal iff additionally a,b have no common neighbour
                    if not (adj[a] & adj[b]):
                        b0 = identify(adj, a, b)
                        spec0 = spectrum(b0)
                        # exact form: cycles of H missing at least one of a,b,
                        # together with the a-b path lengths
                        assert spec0 == spectrum_missing_one(adj, a, b) | S, (
                            n, a, b, "j0-exact")
                        # the inclusion actually used by A019
                        assert spec0 <= spec_h | S, (n, a, b, "j0-incl")
                        # under the A019 hypotheses 1,2 are not in S, so no
                        # length-<3 degeneracy can arise
                        assert 1 not in S and 2 not in S
    print("A1  closure identity: %d connected graphs, %d vertex pairs, all identities hold"
          % (total, pairs))


# --------------------------------------------------------------------------
# A2 - the A019 case dichotomy (degree bookkeeping, power-freeness dropped)
# --------------------------------------------------------------------------


def tight_shape(adj):
    """Exactly one vertex of degree < 3, of degree exactly 2; connected."""
    d = degrees(adj)
    low = [v for v, dv in enumerate(d) if dv < 3]
    return is_connected(adj) and len(low) == 1 and d[low[0]] == 2, (low[0] if len(low) == 1 else None)


def check_a2(max_order=9):
    """Every tight-1-atom-shaped B falls in exactly one A019 case, and the
    reduct predicted by that case has the predicted degree profile."""
    counts = {
        "cut/deg3-side": 0,
        "cut/both>=4": 0,
        "noncut/(3,>=4)": 0,
        "noncut/(>=4,>=4)": 0,
        "noncut/(3,3)": 0,
    }
    seen = 0
    for n in range(5, max_order + 1):
        mine = (3 * n - 4 + 1) // 2  # ceil((3n-4)/2)
        for adj in geng_stream(["-c", "-d2", n, erange(mine, n)]):
            ok, u = tight_shape(adj)
            if not ok:
                continue
            seen += 1
            a, b = sorted(adj[u])
            da, db = len(adj[a]), len(adj[b])
            keep = [v for v in range(n) if v != u]
            H = induced(adj, keep)
            comps = components(H)
            cut = len(comps) > 1
            assert len(comps) <= 2
            if cut:
                if da == 3 or db == 3:
                    counts["cut/deg3-side"] += 1
                    # the degree-3 side is a strictly smaller tight-1-atom shape
                    hit = False
                    for comp in comps:
                        sub = induced(H, comp)
                        okc, _ = tight_shape(sub)
                        if okc:
                            hit = True
                            assert len(comp) <= n - 2
                    assert hit, ("cut deg3 side must give a tight shape", n)
                else:
                    counts["cut/both>=4"] += 1
                    for comp in comps:
                        sub = induced(H, comp)
                        assert min(degrees(sub)) >= 3, ("cut both>=4", n)
                        assert len(comp) <= n - 2
            else:
                d = degrees(H)
                low = [v for v, dv in enumerate(d) if dv < 3]
                if da == 3 and db == 3:
                    counts["noncut/(3,3)"] += 1
                    assert len(low) == 2 and all(d[v] == 2 for v in low)
                elif da >= 4 and db >= 4:
                    counts["noncut/(>=4,>=4)"] += 1
                    assert not low
                else:
                    counts["noncut/(3,>=4)"] += 1
                    assert len(low) == 1 and d[low[0]] == 2
                    assert is_connected(H) and len(H) == n - 1
    print("A2  case dichotomy: %d tight-1-atom-shaped graphs, orders 5-%d" % (seen, max_order))
    for k in sorted(counts):
        print("      %-18s %d" % (k, counts[k]))


# --------------------------------------------------------------------------
# A3 - the saturation construction H + az
# --------------------------------------------------------------------------


def check_a3(max_order=9):
    """In the (3,3)/non-cut case, adding any edge at a terminal of H = B-u
    yields a tight-1-atom-shaped graph of order |B|-1, with spectrum
    Spec(H) u (P(a,z) + 1)."""
    seen = 0
    built = 0
    for n in range(5, max_order + 1):
        mine = (3 * n - 4 + 1) // 2
        for adj in geng_stream(["-c", "-d2", n, erange(mine, n)]):
            ok, u = tight_shape(adj)
            if not ok:
                continue
            a, b = sorted(adj[u])
            if len(adj[a]) != 3 or len(adj[b]) != 3:
                continue
            keep = [v for v in range(n) if v != u]
            H = induced(adj, keep)
            if not is_connected(H):
                continue
            seen += 1
            spec_h = spectrum(H)
            ia = keep.index(a)
            ib = keep.index(b)
            for z in range(len(H)):
                if z == ia or z in H[ia]:
                    continue
                G = add_edge(H, ia, z)
                if z == ib:
                    # W1-T12 case z = b: both terminals reach degree 3, so G
                    # has minimum degree 3 -- a counterexample shape, not a
                    # tight-1-atom shape
                    assert min(degrees(G)) >= 3, ("saturation z=b", n)
                else:
                    okz, wz = tight_shape(G)
                    assert okz and wz == ib, ("saturation shape", n)
                assert len(G) == n - 1
                P = path_lengths(H, ia, z)
                assert spectrum(G) == spec_h | {p + 1 for p in P}, ("saturation spec", n)
                built += 1
    print("A3  saturation construction: %d (3,3)/non-cut reducts, %d lifts H+az verified"
          % (seen, built))


# --------------------------------------------------------------------------
# A4 - C027 stream anchor
# --------------------------------------------------------------------------

C027_STREAM = {6: 4, 7: 5, 8: 36, 9: 84, 10: 918, 11: 4058}


def check_a4(max_order=11):
    """Reproduce the C027 stream counts (connected, C4-free, min degree >= 1,
    at most two sub-cubic vertices, >= ceil((3n-4)/2) edges) and confirm that
    every member contains a C8."""
    for n in range(6, max_order + 1):
        mine = (3 * n - 4 + 1) // 2
        stream = 0
        klass = 0
        powerfree = 0
        t0 = time.time()
        for adj in geng_stream(["-c", "-f", "-d1", n, erange(mine, n)]):
            stream += 1
            d = degrees(adj)
            if sum(1 for dv in d if dv < 3) > 2:
                continue
            klass += 1
            if power_free(spectrum(adj)):
                powerfree += 1
        expect = C027_STREAM.get(n)
        flag = "" if expect is None else (
            " (C027 stream %d %s)" % (expect, "OK" if expect == stream else "MISMATCH"))
        assert expect is None or expect == stream, (n, stream, expect)
        assert powerfree == 0, (n, powerfree)
        print("A4  order %2d: stream %8d, class %6d, power-free %d, %.1fs%s"
              % (n, stream, klass, powerfree, time.time() - t0, flag))


# --------------------------------------------------------------------------
# A5 - fixed anchors
# --------------------------------------------------------------------------


def from_edges(n, edges):
    adj = [set() for _ in range(n)]
    for x, y in edges:
        adj[x].add(y)
        adj[y].add(x)
    return adj


def check_a5():
    k4 = from_edges(4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
    assert spectrum(k4) == {3, 4}
    # K_{3,3} - e, terminals the two degree-2 vertices (0 and 3)
    k33 = from_edges(6, [(0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)])
    assert spectrum(k33) == {4, 6}, spectrum(k33)
    assert path_lengths(k33, 0, 3) == {3, 5}, path_lengths(k33, 0, 3)
    pet_edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0),
                 (5, 7), (7, 9), (9, 6), (6, 8), (8, 5),
                 (0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]
    pet = from_edges(10, pet_edges)
    assert degrees(pet) == [3] * 10
    assert spectrum(pet) == {5, 6, 8, 9}, spectrum(pet)
    pet_e = from_edges(10, [e for e in pet_edges if e != (0, 1)])
    assert spectrum(pet_e) == {5, 6, 8, 9}, spectrum(pet_e)
    assert path_lengths(pet_e, 0, 1) == {4, 5, 7, 8}, path_lengths(pet_e, 0, 1)
    # the L025 R4 doubling: Petersen-e closed by a 2-path is NOT power-free
    closed = add_apex(pet_e, 0, 1)
    assert spectrum(closed) == {5, 6, 8, 9} | {6, 7, 9, 10}
    assert not power_free(spectrum(closed))
    print("A5  fixed anchors: K4, K_{3,3}-e, Petersen, Petersen-e, closure of Petersen-e: OK")


# --------------------------------------------------------------------------
# A6 - how restrictive is Mersenne saturation? (kill test for the W1-T13 lever)
# --------------------------------------------------------------------------

MERSENNE = {2 ** k - 1 for k in range(2, 12)}


def saturated_at(adj, a):
    """True iff every z with az not an edge, z != a, is joined to a by a simple
    path of some length 2^k - 1 (k >= 2)."""
    for z in range(len(adj)):
        if z == a or z in adj[a]:
            continue
        if not (path_lengths(adj, a, z) & MERSENNE):
            return False
    return True


def check_a6(max_order=13):
    """Frequency of Mersenne saturation at a degree-2 vertex, power-freeness
    dropped.  A019 W1-T12 forces it at BOTH terminals of the residual object;
    if it is generically satisfied the lever is weak.

    Edge bound: two vertices of degree 2, the rest >= 3, so
    2|E| >= 4 + 3(n-2) = 3n-2, i.e. |E| >= ceil((3n-2)/2) = (3n-1)//2.
    """
    for n in range(8, max_order + 1):
        mine = (3 * n - 1) // 2
        klass = 0
        sat_one = 0
        sat_both = 0
        c8free = 0
        t0 = time.time()
        for adj in geng_stream(["-c", "-f", "-d2", n, erange(mine, n)]):
            d = degrees(adj)
            low = [v for v, dv in enumerate(d) if dv == 2]
            if len(low) != 2 or sum(1 for dv in d if dv < 3) != 2:
                continue
            klass += 1
            if power_free(spectrum(adj)):
                c8free += 1
            s = [saturated_at(adj, v) for v in low]
            if any(s):
                sat_one += 1
            if all(s):
                sat_both += 1
        print("A6  order %2d: C4-free two-degree-2 class %7d, power-free %d, "
              "saturated at one %6d, at both %6d, %.1fs"
              % (n, klass, c8free, sat_one, sat_both, time.time() - t0))


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    if what in ("all", "a5"):
        check_a5()
    if what in ("all", "a1"):
        check_a1()
    if what in ("all", "a2"):
        check_a2()
    if what in ("all", "a3"):
        check_a3()
    if what in ("all", "a4"):
        check_a4()
    if what in ("all", "a6"):
        check_a6()


if __name__ == "__main__":
    main()
