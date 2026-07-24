"""E012: all-terminal-pair falsification search for A013 T8 (`L030`).

The theorem under test: no vertex-taut C4-free (D)-gadget (H,a,b) has
through-set S(H,a,b) subseteq {3,4,5}.  A (D)-gadget of order n is connected,
C4-free, has minimum degree >= 1, at most two sub-cubic vertices (both
terminals), and degree sum >= 3(n-2)+1+1 = 3n-4, i.e. at least
ceil((3n-4)/2) edges -- exactly the E010/E011 geng stream class.  So scanning
EVERY admissible terminal pair of EVERY stream graph at order n is an
exhaustive search for order-n counterexamples to the theorem.  This includes
terminal pairs with both degrees >= 3, which E011/C028 never examined.

Soundness of the two prefilters (both necessary conditions for a taut pair
with S subseteq {3,4,5}, so rejecting on them loses no theorem targets):

  * 3 <= dist(a,b) <= 5: s_min = dist(a,b) and s_min must lie in {3,4,5}.
  * dist(a,v) + dist(v,b) <= 5 for every v: a vertex at position i of a
    simple a-b path of length ell <= 5 has dist(a,v) <= i and
    dist(v,b) <= ell - i.

Survivors get an exact all-simple-paths DFS that aborts on the first a-b
arrival of length >= 6; if the DFS completes, S subseteq {3,4,5} holds
exactly and tautness is decided from the essential-vertex mask.  A taut
survivor would REFUTE A013 T8 and is recorded verbatim.

Anchors:

  A1  K_{3,3}-e (terminals the degree-2 vertices): the scan machinery,
      applied directly, reports it taut with S = {3,5} -- the positive
      control that a real gadget would be caught -- and has_c4 confirms it
      is excluded from every C4-free stream.
  A2  T8 endgame dichotomy on ALL three-matchings structures at k in
      {2, 4} (2 + 216 = 218 structures: phi, psi perfect matchings on X, Z;
      sigma a bijection): each graph has a C4 exactly when some x satisfies
      sigma(phi(x)) = psi(sigma(x)) (the Case A block), and each C4-free one
      has longest a-b path >= 7 and is rejected by the scan.  This is an
      instance-exhaustive check of the proof's final dichotomy.
  A3  the five taut pinched gadgets recorded by E011 (S = {6,...,11}) are
      rejected by the distance prefilter (d(a,b) = 6).
  A4  P4 has four sub-cubic vertices: no admissible pair, graph skipped.
  A5  stream totals at each order equal the E010 records.

Usage:
  python3 scan_pairs.py anchors
  python3 scan_pairs.py run 6 7 8 9 10 11 12 13 14
"""

from __future__ import annotations

import argparse
import itertools
import json
import pathlib
import platform
import subprocess
import time

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE / "data"
E011_DATA = (
    HERE.parent
    / "E011-taut-gadget-verification-lobe-structure-and-the-taut-bottom"
    / "data"
)

STREAM_EXPECTED = {  # E010 recorded stream totals (C027)
    6: 4, 7: 5, 8: 36, 9: 84, 10: 918, 11: 4058,
    12: 52331, 13: 389734, 14: 5605161, 15: 61813970,
}


# --- primitives copied verbatim from E011/verify_taut.py --------------------
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


def k33_minus_e() -> tuple[list[int], int, int]:
    adjacency = [0] * 6
    for u in (0, 1, 2):
        for v in (3, 4, 5):
            if (u, v) == (0, 3):
                continue
            adjacency[u] |= 1 << v
            adjacency[v] |= 1 << u
    return adjacency, 0, 3


# --- new machinery ----------------------------------------------------------

def bfs_all(adjacency: list[int], source: int) -> list[int]:
    n = len(adjacency)
    dist = [-1] * n
    dist[source] = 0
    seen = 1 << source
    frontier = [source]
    d = 0
    while frontier:
        d += 1
        nxt = []
        for v in frontier:
            free = adjacency[v] & ~seen
            while free:
                low = free & -free
                free ^= low
                seen |= low
                w = low.bit_length() - 1
                dist[w] = d
                nxt.append(w)
        frontier = nxt
    return dist


def paths_bounded(adjacency: list[int], a: int, b: int):
    """All-simple-paths DFS from a.  Returns (S, essential_mask) when every
    simple a-b path has length <= 5; returns None on the first arrival at b
    with length >= 6 (the pair is then not a theorem target)."""
    lengths: set[int] = set()
    essential = 0
    stack = [(a, 1 << a, 0)]
    while stack:
        vertex, visited, dist = stack.pop()
        if vertex == b:
            if dist >= 6:
                return None
            lengths.add(dist)
            essential |= visited
            continue
        free = adjacency[vertex] & ~visited
        while free:
            low = free & -free
            free ^= low
            stack.append((low.bit_length() - 1, visited | low, dist + 1))
    assert lengths, "disconnected input"
    return lengths, essential


def longest_ab_path(adjacency: list[int], a: int, b: int) -> int:
    best = 0
    stack = [(a, 1 << a, 0)]
    while stack:
        vertex, visited, dist = stack.pop()
        if vertex == b:
            best = max(best, dist)
            continue
        free = adjacency[vertex] & ~visited
        while free:
            low = free & -free
            free ^= low
            stack.append((low.bit_length() - 1, visited | low, dist + 1))
    return best


def candidate_pairs(degs: list[int]) -> list[tuple[int, int]]:
    """Unordered terminal pairs (a,b) compatible with condition (D): every
    sub-cubic vertex must be a terminal, and deg(a)+deg(b) >= 3."""
    n = len(degs)
    sub = [v for v in range(n) if degs[v] < 3]
    if len(sub) > 2:
        return []
    if len(sub) == 2:
        s, t = sub
        return [(s, t)] if degs[s] + degs[t] >= 3 else []
    if len(sub) == 1:
        s = sub[0]
        return [(s, v) for v in range(n) if v != s]
    return [(u, v) for u in range(n) for v in range(u + 1, n)]


def scan_pair(adjacency, dist_of, a, b):
    """Decide whether (H,a,b) is a taut (D)-pair with S subseteq {3,4,5}.
    Returns (verdict, S, essential) with verdict in:
      'reject-dist', 'reject-eccentric', 'reject-long', 'nontaut', 'TAUT'."""
    da, db = dist_of[a], dist_of[b]
    if not 3 <= da[b] <= 5:
        return "reject-dist", None, None
    n = len(adjacency)
    if any(da[v] + db[v] > 5 for v in range(n)):
        return "reject-eccentric", None, None
    result = paths_bounded(adjacency, a, b)
    if result is None:
        return "reject-long", None, None
    lengths, essential = result
    assert min(lengths) == da[b], "DFS/BFS mismatch"
    assert lengths <= {3, 4, 5}
    if essential == (1 << n) - 1:
        return "TAUT", sorted(lengths), essential
    return "nontaut", sorted(lengths), essential


# --- anchors ----------------------------------------------------------------

def perfect_matchings(elems: tuple[int, ...]):
    if not elems:
        yield ()
        return
    first, rest = elems[0], elems[1:]
    for i in range(len(rest)):
        other = rest[i]
        for sub in perfect_matchings(rest[:i] + rest[i + 1:]):
            yield ((first, other),) + sub


def three_matchings(k, phi_pairs, psi_pairs, sigma):
    """X = 0..k-1, Z = k..2k-1, a = 2k, b = 2k+1; edges: a-X, b-Z, the two
    internal matchings, and the cross bijection x ~ sigma(x)."""
    a, b = 2 * k, 2 * k + 1
    edges = [(a, x) for x in range(k)] + [(b, k + z) for z in range(k)]
    edges += list(phi_pairs)
    edges += [(k + u, k + v) for u, v in psi_pairs]
    edges += [(x, k + sigma[x]) for x in range(k)]
    return from_edges(2 * k + 2, edges), a, b


def anchors() -> None:
    checks = 0

    def ok(condition: bool, message: str) -> None:
        nonlocal checks
        assert condition, message
        checks += 1

    # A1: K_{3,3}-e is caught by the scan as a taut S={3,5} pair, and is
    # C4-ridden (so absent from every C4-free stream).
    adj, a, b = k33_minus_e()
    dist_of = [bfs_all(adj, v) for v in range(6)]
    verdict, S, _ = scan_pair(adj, dist_of, a, b)
    ok(verdict == "TAUT" and S == [3, 5], "A1: K33-e not reported taut {3,5}")
    ok(has_c4(adj), "A1: K33-e should contain a C4")
    ok(candidate_pairs(degrees(adj)) == [(0, 3)], "A1: pair enumeration")

    # A2: the T8 endgame dichotomy, exhaustively at k = 2 and 4.
    total = 0
    with_c4 = 0
    for k in (2, 4):
        matchings = list(perfect_matchings(tuple(range(k))))
        for phi_pairs in matchings:
            phi = {}
            for u, v in phi_pairs:
                phi[u], phi[v] = v, u
            for psi_pairs in matchings:
                psi = {}
                for u, v in psi_pairs:
                    psi[u], psi[v] = v, u
                for sigma in itertools.permutations(range(k)):
                    total += 1
                    adj, a, b = three_matchings(k, phi_pairs, psi_pairs, sigma)
                    degs = degrees(adj)
                    ok(all(degs[v] == 3 for v in range(2 * k)),
                       "A2: X/Z degree != 3")
                    block = any(sigma[phi[x]] == psi[sigma[x]]
                                for x in range(k))
                    c4 = has_c4(adj)
                    ok(c4 == block, "A2: C4 <-> Case-A block failed")
                    if c4:
                        with_c4 += 1
                        continue
                    ok(longest_ab_path(adj, a, b) >= 7,
                       "A2: C4-free structure lacks a length>=7 a-b path")
                    dist_of = [bfs_all(adj, v) for v in range(2 * k + 2)]
                    verdict, _, _ = scan_pair(adj, dist_of, a, b)
                    ok(verdict == "reject-long",
                       "A2: scan failed to reject C4-free structure")
    ok(total == 218, f"A2: expected 218 structures, saw {total}")
    ok(0 < with_c4 < total, "A2: both dichotomy branches must occur")

    # A3: the five E011 taut pinched gadgets are rejected on distance.
    pinched = 0
    for n in (12, 13):
        payload = json.loads((E011_DATA / f"taut_n{n}.json").read_text())
        for entry in payload["taut_pinched"]:
            adj = g6_decode(entry["graph6"])
            ta, tb = entry["terminals"]
            dist_of = {ta: bfs_all(adj, ta), tb: bfs_all(adj, tb)}
            verdict, _, _ = scan_pair(adj, dist_of, ta, tb)
            ok(verdict == "reject-dist",
               f"A3: {entry['graph6']} not rejected on distance")
            pinched += 1
    ok(pinched == 5, f"A3: expected 5 E011 taut pinched gadgets, saw {pinched}")

    # A4: P4 has four sub-cubic vertices -- no admissible pair.
    p4 = from_edges(4, [(0, 1), (1, 2), (2, 3)])
    ok(candidate_pairs(degrees(p4)) == [], "A4: P4 should yield no pairs")

    print(f"anchors: all {checks} checks passed")


# --- the stream scan --------------------------------------------------------

def run(orders: list[int]) -> None:
    DATA.mkdir(exist_ok=True)
    for n in orders:
        started = time.time()
        mine = -(-(3 * n - 4) // 2)
        command = ["geng", "-q", "-c", "-f", "-d1", str(n), f"{mine}:0"]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, text=True)
        stream = 0
        eligible = 0
        pair_counts = {
            "pairs": 0, "reject-dist": 0, "reject-eccentric": 0,
            "reject-long": 0, "nontaut": 0, "TAUT": 0,
        }
        taut_hits: list[dict] = []
        nontaut_s345: list[dict] = []
        for line in process.stdout:
            line = line.strip()
            if not line:
                continue
            stream += 1
            adjacency = g6_decode(line)
            degs = degrees(adjacency)
            pairs = candidate_pairs(degs)
            if not pairs:
                continue
            assert not has_c4(adjacency), "geng -f emitted a C4 graph"
            eligible += 1
            dist_of = [bfs_all(adjacency, v) for v in range(n)]
            for a, b in pairs:
                pair_counts["pairs"] += 1
                verdict, S, essential = scan_pair(adjacency, dist_of, a, b)
                pair_counts[verdict] += 1
                if verdict == "TAUT":
                    taut_hits.append(
                        {"graph6": line, "terminals": [a, b], "S": S}
                    )
                elif verdict == "nontaut":
                    nontaut_s345.append(
                        {"graph6": line, "terminals": [a, b], "S": S,
                         "essential": essential}
                    )
        assert process.wait() == 0
        expected = STREAM_EXPECTED.get(n)
        if expected is not None:
            assert stream == expected, (n, stream, expected)
        assert not taut_hits, f"A013 T8 REFUTED: {taut_hits[:3]}"

        summary = {
            "n": n,
            "geng_command": " ".join(command),
            "stream_total": stream,
            "stream_matches_e010": expected is not None,
            "eligible_graphs_le2_subcubic": eligible,
            "pair_counts": pair_counts,
            "taut_hits": taut_hits,
            "nontaut_S345_pairs": nontaut_s345,
            "seconds": round(time.time() - started, 1),
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
        }
        (DATA / f"pairs_n{n}.json").write_text(json.dumps(summary, indent=2))
        print(
            f"n={n}: stream={stream} eligible={eligible} "
            f"pairs={pair_counts['pairs']} "
            f"[dist {pair_counts['reject-dist']} / ecc "
            f"{pair_counts['reject-eccentric']} / long "
            f"{pair_counts['reject-long']} / nontaut-S345 "
            f"{pair_counts['nontaut']} / TAUT {pair_counts['TAUT']}] "
            f"({summary['seconds']}s)"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("anchors")
    runp = sub.add_parser("run")
    runp.add_argument("orders", nargs="+", type=int)
    args = parser.parse_args()
    if args.command == "anchors":
        anchors()
    else:
        run(args.orders)


if __name__ == "__main__":
    main()
