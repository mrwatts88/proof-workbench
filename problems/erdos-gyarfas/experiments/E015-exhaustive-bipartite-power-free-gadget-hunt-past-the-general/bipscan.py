"""E015: exhaustive bipartite power-free gadget hunt (A017 T3/T4, ledger L035).

A017 T3 (bipartite assembly criterion): if a finite simple connected BIPARTITE
graph H is power-free (no cycle of length 2^k, k >= 2) and has at most two
vertices of degree < 3 -- with degrees >= 1 summing to >= 3 when there are two,
and degree 1 or 2 when there is one -- then statement 0.1 is FALSE.  No path
enumeration, tautness test, or external import is involved: the parity of the
through-set is fixed by the colour classes, so the ring/pendant machinery of
L025/L034 applies to every such graph.

A017 T4 (completeness): every power-free (D)-gadget with parity-constant
through-set -- i.e. every witness of the L034 congruence channels (i) all-odd S
and (iii) S subseteq 2+4Z -- is either vertex-taut, hence bipartite (T2), or
already yields a disproof through L027 (a 1-atom or a min-degree-3 power-free
graph).  So scanning bipartite graphs is exhaustive for those channels modulo
the standing 1-atom relativization.

Search class at order n (this script): connected, bipartite, C4-free, minimum
degree >= 2, at most two vertices of degree 2 (all others >= 3).  Terminal
degree-1 cases are covered at order n+1 by the pendant reduction (A014 T1 /
A017 T3 case B2): stripping the pendant of a degree-1 terminal lands in this
class one order down, so scanning orders <= N here covers every hit of order
<= N+1 that has a degree-1 vertex.

Generation: genbg -c -Z1 -d2 p q mine:0 for every split p+q = n admitted by
A017 T5 (the C4-free counting bound 3q-4 <= C(p,2) and 3p-4 <= C(q,2)); -Z1
("two vertices in the second class have at most 1 common neighbour") is exactly
C4-freeness for bipartite graphs, and mine = ceil((3n-2)/2) from the degree sum
3(n-2)+2+2.  Splits rejected by T5 contain no member of the class, so skipping
them keeps the scan exhaustive.

Power-freeness test: no C4 (asserted, from -Z1), no C8, no C16 (n >= 16), no
C32 (n >= 32).  Bipartite graphs have no odd cycles, so this is the complete
power-free condition for n <= 63.

Usage:
  python3 bipscan.py anchors        # implementation + known-spectrum controls
  python3 bipscan.py crosscheck 12  # genbg class == geng(E010 stream) class
  python3 bipscan.py run 12 13 ... 22
"""

from __future__ import annotations

import argparse
import json
import pathlib
import platform
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE / "data"


# --- primitives copied verbatim from E012/scan_pairs.py ---------------------
# (anchored there against the independent E010 pipeline)

def g6_decode(text: str) -> list[int]:
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


def degrees(adjacency: list[int]) -> list[int]:
    return [row.bit_count() for row in adjacency]


def has_c4(adjacency: list[int]) -> bool:
    n = len(adjacency)
    for u in range(n):
        for v in range(u + 1, n):
            if (adjacency[u] & adjacency[v]).bit_count() >= 2:
                return True
    return False


def from_edges(n: int, edges: list[tuple[int, int]]) -> list[int]:
    adjacency = [0] * n
    for u, v in edges:
        assert u != v and not adjacency[u] >> v & 1
        adjacency[u] |= 1 << v
        adjacency[v] |= 1 << u
    return adjacency


# --- new machinery ----------------------------------------------------------

def bipartition(adjacency: list[int]) -> tuple[int, int] | None:
    """Return (maskX, maskY) of the 2-colouring, or None if not bipartite.

    Assumes a connected graph (the colouring of each component is chosen
    independently; for connected graphs it is unique up to swap).
    """
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


def bfs_dist(adjacency: list[int], source: int, allowed: int) -> list[int]:
    """Distances from `source` inside the vertex set `allowed` (bitmask)."""
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


def has_cycle_len(adjacency: list[int], length: int) -> bool:
    """Exact: does the graph contain a simple cycle of exactly `length` edges?

    Canonicalization: the cycle's minimum vertex is the start s, and the search
    only uses vertices >= s.  Direction is fixed by requiring the first step to
    be smaller than the last.  Pruning: from a vertex v reached after k edges,
    the walk must return to s within length-k edges, so dist_allowed(v,s) must
    be <= length-k.
    """
    n = len(adjacency)
    if length < 3 or length > n:
        return False
    full = (1 << n) - 1
    for s in range(n - length + 1):
        allowed = full & ~((1 << s) - 1)
        dist = bfs_dist(adjacency, s, allowed)
        nbrs_s = adjacency[s] & allowed
        # first step u, last step w, with u < w
        row = nbrs_s
        while row:
            low = row & -row
            u = low.bit_length() - 1
            row ^= low
            if dist[u] > length - 1:
                continue
            # DFS over paths s,u,...  of `length-1` edges ending adjacent to s
            # at a vertex w > u.
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


def count_cycles_len(adjacency: list[int], length: int) -> int:
    """Exact number of simple cycles of exactly `length` edges."""
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


def cycle_spectrum_bruteforce(adjacency: list[int]) -> set[int]:
    """All cycle lengths, by exhaustive enumeration (small graphs only)."""
    n = len(adjacency)
    full = (1 << n) - 1
    lengths: set[int] = set()
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
                # close the cycle; fix direction by first < last
                last = v
                if first < last:
                    lengths.add(k + 1)
    return lengths


def power_lengths(n: int) -> list[int]:
    out = []
    k = 2
    while 2 ** k <= n:
        out.append(2 ** k)
        k += 1
    return out


def power_free(adjacency: list[int]) -> tuple[bool, list[int]]:
    """(is power-free, list of power lengths present)."""
    present = [L for L in power_lengths(len(adjacency)) if has_cycle_len(adjacency, L)]
    return (not present), present


# --- generation -------------------------------------------------------------

def split_admissible(p: int, q: int) -> bool:
    """A017 T5: the C4-free counting bound for the search class."""
    return 3 * q - 4 <= p * (p - 1) // 2 and 3 * p - 4 <= q * (q - 1) // 2


def min_edges(n: int) -> int:
    """Degree sum >= 3(n-2) + 2 + 2 = 3n - 2."""
    return -((-(3 * n - 2)) // 2)


def genbg_stream(p: int, q: int, mine: int):
    cmd = ["genbg", "-q", "-c", "-Z1", "-d2", str(p), str(q), f"{mine}:0"]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True, bufsize=1 << 20)
    assert proc.stdout is not None
    for line in proc.stdout:
        line = line.strip()
        if line:
            yield line
    proc.wait()
    assert proc.returncode == 0, f"genbg failed: {cmd}"


def geng_stream(n: int, mine: int):
    cmd = ["geng", "-q", "-c", "-f", "-d1", str(n), f"{mine}:0"]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True, bufsize=1 << 20)
    assert proc.stdout is not None
    for line in proc.stdout:
        line = line.strip()
        if line:
            yield line
    proc.wait()
    assert proc.returncode == 0, f"geng failed: {cmd}"


def genbg_plain(p: int, q: int, mine: int):
    """Every connected bipartite graph with parts (p,q) and >= mine edges."""
    cmd = ["genbg", "-q", "-c", str(p), str(q), f"{mine}:0"]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True, bufsize=1 << 20)
    assert proc.stdout is not None
    for line in proc.stdout:
        line = line.strip()
        if line:
            yield line
    proc.terminate()
    proc.wait()


def geng_all(n: int):
    """Every connected graph of order n (anchor use only)."""
    cmd = ["geng", "-q", "-c", str(n)]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True, bufsize=1 << 20)
    assert proc.stdout is not None
    for line in proc.stdout:
        line = line.strip()
        if line:
            yield line
    proc.wait()
    assert proc.returncode == 0, f"geng failed: {cmd}"


def canonical(lines: list[str]) -> list[str]:
    if not lines:
        return []
    proc = subprocess.run(
        ["labelg", "-q"], input="\n".join(lines) + "\n",
        capture_output=True, text=True, check=True,
    )
    return [x.strip() for x in proc.stdout.split() if x.strip()]


# --- the class test ---------------------------------------------------------

def in_class(adjacency: list[int]) -> bool:
    """Connected bipartite C4-free, min degree >= 2, at most two of degree 2."""
    deg = degrees(adjacency)
    if min(deg) < 2:
        return False
    if sum(1 for d in deg if d < 3) > 2:
        return False
    if has_c4(adjacency):
        return False
    return bipartition(adjacency) is not None


def classify(g6: str) -> dict:
    adjacency = g6_decode(g6)
    n = len(adjacency)
    deg = degrees(adjacency)
    assert not has_c4(adjacency), f"-Z1 leaked a C4: {g6}"
    parts = bipartition(adjacency)
    assert parts is not None, f"genbg produced a non-bipartite graph: {g6}"
    subcubic = [v for v in range(n) if deg[v] < 3]
    free, present = power_free(adjacency)
    record = {
        "graph6": g6,
        "n": n,
        "edges": sum(deg) // 2,
        "subcubic": [(v, deg[v]) for v in subcubic],
        "powers_present": present,
        "power_free": free,
    }
    record["c8_count"] = count_cycles_len(adjacency, 8)
    if len(subcubic) == 2:
        maskx = parts[0]
        a, b = subcubic
        same = ((maskx >> a) & 1) == ((maskx >> b) & 1)
        record["terminals_same_part"] = same
        record["through_parity"] = "even" if same else "odd"
    return record


# --- commands ---------------------------------------------------------------

def named_graphs() -> dict[str, tuple[list[int], set[int]]]:
    """Anchor graphs with their known cycle spectra."""
    out: dict[str, tuple[list[int], set[int]]] = {}

    c6 = from_edges(6, [(i, (i + 1) % 6) for i in range(6)])
    out["C6"] = (c6, {6})

    k33 = from_edges(6, [(u, v) for u in (0, 1, 2) for v in (3, 4, 5)])
    out["K33"] = (k33, {4, 6})

    cube = from_edges(8, [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7),
    ])
    out["Q3"] = (cube, {4, 6, 8})

    petersen_edges = [(i, (i + 1) % 5) for i in range(5)]
    petersen_edges += [(i, i + 5) for i in range(5)]
    petersen_edges += [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
    out["Petersen"] = (from_edges(10, petersen_edges), {5, 6, 8, 9})

    # Heawood graph = incidence graph of the Fano plane (LCF [5,-5]^7).
    heawood = [(i, (i + 1) % 14) for i in range(14)]
    lcf = [5, -5] * 7
    for i, shift in enumerate(lcf):
        j = (i + shift) % 14
        if i < j:
            heawood.append((i, j))
    out["Heawood"] = (from_edges(14, sorted(set(heawood))), {6, 8, 10, 12, 14})

    return out


def cmd_anchors(_args) -> None:
    checks = 0
    named = named_graphs()

    # A1: known cycle spectra, via both implementations.
    for name, (adjacency, spectrum) in named.items():
        brute = cycle_spectrum_bruteforce(adjacency)
        assert brute == spectrum, (name, sorted(brute), sorted(spectrum))
        checks += 1
        for L in range(3, len(adjacency) + 1):
            assert has_cycle_len(adjacency, L) == (L in spectrum), (name, L)
            checks += 1
        assert has_c4(adjacency) == (4 in spectrum), name
        checks += 1

    # A2: bipartiteness detector on the named graphs.
    for name, expected in [("C6", True), ("K33", True), ("Q3", True),
                           ("Petersen", False), ("Heawood", True)]:
        assert (bipartition(named[name][0]) is not None) is expected, name
        checks += 1
    parts = bipartition(named["Heawood"][0])
    assert parts is not None and bin(parts[0]).count("1") == 7
    checks += 1

    # A3: power-freeness verdicts on the named graphs.
    for name, expected in [("C6", True), ("K33", False), ("Q3", False),
                           ("Petersen", False), ("Heawood", False)]:
        assert power_free(named[name][0])[0] is expected, name
        checks += 1

    # A4: class membership.
    assert not in_class(named["K33"][0])       # has C4
    assert not in_class(named["C6"][0])        # six degree-2 vertices
    assert in_class(named["Heawood"][0])       # cubic bipartite girth 6
    assert not in_class(named["Petersen"][0])  # not bipartite
    checks += 4

    # A5: has_cycle_len agrees with the independent brute-force enumerator on
    # EVERY connected graph of order <= 7 (2 + 6 + 21 + 112 + 853 = 994),
    # bipartite or not, and on every connected bipartite graph of order 8-10
    # produced by genbg at low edge counts.
    sample = 0
    for n_small in (3, 4, 5, 6, 7):
        for g6 in geng_all(n_small):
            adjacency = g6_decode(g6)
            brute = cycle_spectrum_bruteforce(adjacency)
            for L in range(3, len(adjacency) + 1):
                assert has_cycle_len(adjacency, L) == (L in brute), (g6, L)
                checks += 1
            sample += 1
    assert sample == 994, sample
    bipartite_sample = 0
    for p, q in [(4, 4), (4, 5), (5, 5), (5, 6)]:
        for g6 in genbg_plain(p, q, p + q - 1):
            adjacency = g6_decode(g6)
            brute = cycle_spectrum_bruteforce(adjacency)
            for L in range(3, len(adjacency) + 1):
                assert has_cycle_len(adjacency, L) == (L in brute), (g6, L)
                checks += 1
            bipartite_sample += 1
            if bipartite_sample >= 2000:
                break
        if bipartite_sample >= 2000:
            break
    assert bipartite_sample >= 1000, bipartite_sample
    checks += 1

    # A5b: long-cycle detection (the C8/C16 tests the scan actually relies on)
    # against known facts.  C_m has spectrum {m}; the hypercube Q4 is
    # bipancyclic (cycles of every even length from 4 to 16).
    for m in (8, 12, 16, 20):
        cyc = from_edges(m, [(i, (i + 1) % m) for i in range(m)])
        for L in range(3, m + 1):
            assert has_cycle_len(cyc, L) == (L == m), (m, L)
            checks += 1
    q4_edges = [(u, u ^ (1 << i)) for u in range(16) for i in range(4) if u < (u ^ (1 << i))]
    q4 = from_edges(16, q4_edges)
    assert degrees(q4) == [4] * 16
    for L in range(3, 17):
        assert has_cycle_len(q4, L) == (L % 2 == 0 and L >= 4), L
        checks += 1

    # A6: T5's counting bound never rejects a realizable split -- checked
    # against genbg itself at the small orders where both are cheap.
    for n in range(8, 15):
        for p in range(2, n // 2 + 1):
            q = n - p
            if split_admissible(p, q):
                continue
            found = 0
            for g6 in genbg_stream(p, q, min_edges(n)):
                if in_class(g6_decode(g6)):
                    found += 1
                    break
            assert found == 0, (n, p, q)
            checks += 1

    print(f"anchors: all {checks} checks pass")
    print(f"  python {platform.python_version()} ({platform.python_implementation()})")


def cmd_crosscheck(args) -> None:
    """The genbg-generated class equals the bipartite part of the E010 stream."""
    n = args.n
    # E010 stream flags, exactly as in E010/E011/E012/E013.
    e010_mine = -((-(3 * n - 4)) // 2)
    from_geng = [g6 for g6 in geng_stream(n, e010_mine) if in_class(g6_decode(g6))]
    from_genbg = []
    for p in range(2, n // 2 + 1):
        q = n - p
        if not split_admissible(p, q):
            continue
        for g6 in genbg_stream(p, q, min_edges(n)):
            if in_class(g6_decode(g6)):
                from_genbg.append(g6)
    a = set(canonical(from_geng))
    b = set(canonical(from_genbg))
    print(f"n={n}: geng-derived {len(from_geng)} raw / {len(a)} canonical; "
          f"genbg-derived {len(from_genbg)} raw / {len(b)} canonical")
    assert a == b, (
        f"class mismatch at n={n}: only-geng={sorted(a - b)[:5]} "
        f"only-genbg={sorted(b - a)[:5]}"
    )
    print(f"n={n}: cross-check PASSES ({len(a)} graphs)")


def cmd_run(args) -> None:
    DATA.mkdir(exist_ok=True)
    for n in args.orders:
        started = time.time()
        mine = min_edges(n)
        splits = []
        hits = []
        c8_free = []
        records: list[dict] = []
        totals = {"generated": 0, "in_class": 0, "power_free": 0}
        power_hist: dict[str, int] = {}
        c8_hist: dict[str, int] = {}
        subcubic_hist: dict[str, int] = {}
        for p in range(2, n // 2 + 1):
            q = n - p
            if not split_admissible(p, q):
                splits.append({"p": p, "q": q, "skipped": "T5 counting bound"})
                continue
            generated = 0
            kept = 0
            for g6 in genbg_stream(p, q, mine):
                generated += 1
                adjacency = g6_decode(g6)
                deg = degrees(adjacency)
                if sum(1 for d in deg if d < 3) > 2:
                    continue
                kept += 1
                record = classify(g6)
                records.append(record)
                key = ",".join(str(x) for x in record["powers_present"]) or "none"
                power_hist[key] = power_hist.get(key, 0) + 1
                c8_key = str(record["c8_count"])
                c8_hist[c8_key] = c8_hist.get(c8_key, 0) + 1
                prof = ",".join(str(d) for _, d in record["subcubic"]) or "cubic-or-better"
                subcubic_hist[prof] = subcubic_hist.get(prof, 0) + 1
                if 8 not in record["powers_present"]:
                    c8_free.append(record)
                if record["power_free"]:
                    hits.append(record)
            splits.append({"p": p, "q": q, "generated": generated, "in_class": kept})
            totals["generated"] += generated
            totals["in_class"] += kept
        totals["power_free"] = len(hits)
        elapsed = time.time() - started
        min_c8 = min((r["c8_count"] for r in records), default=None)
        extremal = [r for r in records if r["c8_count"] == min_c8][:20]
        out = {
            "n": n,
            "min_edges": mine,
            "generator": f"genbg -q -c -Z1 -d2 p q {mine}:0",
            "splits": splits,
            "totals": totals,
            "power_length_histogram": power_hist,
            "c8_count_histogram": c8_hist,
            "subcubic_profile_histogram": subcubic_hist,
            "min_c8_count": min_c8,
            "min_c8_exemplars": extremal,
            "all_records": records if len(records) <= 5000 else "omitted (>5000)",
            "c8_free": c8_free,
            "hits": hits,
            "seconds": round(elapsed, 1),
            "interpreter": f"{platform.python_implementation()} {platform.python_version()}",
        }
        (DATA / f"scan_n{n}.json").write_text(json.dumps(out, indent=2) + "\n")
        status = "HIT" if hits else "empty"
        print(f"n={n}: in-class {totals['in_class']} / generated "
              f"{totals['generated']}; C8-free {len(c8_free)}; "
              f"power-free {len(hits)} [{status}] ({elapsed:.1f}s)")
        if hits:
            print("  *** POWER-FREE BIPARTITE GADGET FOUND -- A017 T3 applies ***")
            for record in hits:
                print("   ", json.dumps(record))
            sys.exit(2)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("anchors").set_defaults(func=cmd_anchors)
    p_cross = sub.add_parser("crosscheck")
    p_cross.add_argument("n", type=int)
    p_cross.set_defaults(func=cmd_crosscheck)
    p_run = sub.add_parser("run")
    p_run.add_argument("orders", type=int, nargs="+")
    p_run.set_defaults(func=cmd_run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
