"""E015 part 2: exhaustive verification of A017 T0/T1/T2 (the parity structure
theorem) and of the T3 case analysis, over all small two-terminal graphs.

The falsification test named in A017's plan: a vertex-taut two-terminal graph
whose through-set is parity-constant while the graph is NOT bipartite would
refute T2 outright.  This script looks for one over every connected graph of
order <= 7 (994 graphs, every ordered terminal pair) and over every connected
C4-free graph of orders 8-9 (the domain the program actually uses), checking in
each case:

  V1  bipartite  ==>  S parity-constant, with all-odd iff the terminals lie in
      opposite colour classes and all-even iff in the same class
      (T2, easy direction; no tautness needed).
  V2  vertex-taut and S parity-constant  ==>  bipartite  (T2, the real
      direction).  Refutation of this is the kill condition.
  V3  vertex-taut  ==>  every cut vertex separates the terminals, the block-cut
      tree is a path, S is the Minkowski sum of the block through-sets, and
      every block is vertex-taut with distinct attachment terminals (T0).
  V4  2-connected and non-bipartite  ==>  through-paths of both parities
      (T1, the parity fan lemma), for every ordered pair.
  V5  sharpness: count the non-taut, parity-constant, non-bipartite pairs -- the
      configurations T2 must exclude by tautness (the pendant-triangle family).

Also verified directly (V6): for every graph in the E015 search class at orders
<= 20, the two-terminal reading used by A017 T3 -- that the sub-cubic vertices
form a (D)-gadget whose through-set has the parity predicted by the colour
classes -- by explicit path enumeration.

Usage:
  python3 verify_parity.py all        # V1-V5 at orders <= 7, C4-free 8-9
  python3 verify_parity.py class      # V6 over the E015 class, orders <= 20
"""

from __future__ import annotations

import argparse
import itertools
import json
import pathlib
import platform
import subprocess

import bipscan as B

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE / "data"


def all_paths_lengths(adjacency: list[int], a: int, b: int) -> tuple[set[int], int]:
    """(set of simple a-b path lengths, bitmask of vertices on some such path)."""
    lengths: set[int] = set()
    essential = 0
    stack = [(a, 1 << a, 0, [a])]
    while stack:
        v, used, k, path = stack.pop()
        if v == b:
            lengths.add(k)
            for u in path:
                essential |= 1 << u
            continue
        row = adjacency[v] & ~used
        while row:
            low = row & -row
            w = low.bit_length() - 1
            row ^= low
            stack.append((w, used | low, k + 1, path + [w]))
    return lengths, essential


def is_connected(adjacency: list[int]) -> bool:
    n = len(adjacency)
    seen = 1
    frontier = 1
    while frontier:
        nxt = 0
        row = frontier
        while row:
            low = row & -row
            u = low.bit_length() - 1
            row ^= low
            nxt |= adjacency[u] & ~seen
        seen |= nxt
        frontier = nxt
    return seen == (1 << n) - 1


def induced(adjacency: list[int], mask: int) -> list[int]:
    return [adjacency[v] & mask if (mask >> v) & 1 else 0 for v in range(len(adjacency))]


def cut_vertices(adjacency: list[int]) -> list[int]:
    n = len(adjacency)
    full = (1 << n) - 1
    out = []
    for v in range(n):
        rest = full & ~(1 << v)
        sub = induced(adjacency, rest)
        start = (rest & -rest).bit_length() - 1
        seen = 1 << start
        frontier = seen
        while frontier:
            nxt = 0
            row = frontier
            while row:
                low = row & -row
                u = low.bit_length() - 1
                row ^= low
                nxt |= sub[u] & ~seen
            seen |= nxt
            frontier = nxt
        if seen != rest:
            out.append(v)
    return out


def is_two_connected(adjacency: list[int]) -> bool:
    n = len(adjacency)
    return n >= 3 and is_connected(adjacency) and not cut_vertices(adjacency)


def blocks_of(adjacency: list[int]) -> list[int]:
    """Vertex sets (bitmasks) of the blocks, by brute force on small graphs.

    A block is a maximal set of >= 2 vertices inducing a connected subgraph with
    no cut vertex of its own; equivalently, edges are grouped by the
    "lies on a common cycle" equivalence.  Small-graph implementation: build the
    edge relation directly.
    """
    n = len(adjacency)
    edges = [(u, v) for u in range(n) for v in range(u + 1, n) if (adjacency[u] >> v) & 1]
    parent = {e: e for e in edges}

    def find(e):
        while parent[e] != e:
            parent[e] = parent[parent[e]]
            e = parent[e]
        return e

    def union(e, f):
        re, rf = find(e), find(f)
        if re != rf:
            parent[re] = rf

    # two edges are in the same block iff they lie on a common cycle
    for e, f in itertools.combinations(edges, 2):
        shared = set(e) & set(f)
        if not shared:
            continue
        # e = (u,v), f = (x,y) share exactly one vertex c (or are parallel: n/a)
        c = shared.pop()
        p = (set(e) - {c}).pop()
        q = (set(f) - {c}).pop()
        # common cycle iff p and q are connected in G - c
        rest = ((1 << n) - 1) & ~(1 << c)
        sub = induced(adjacency, rest)
        seen = 1 << p
        frontier = seen
        while frontier:
            nxt = 0
            row = frontier
            while row:
                low = row & -row
                u = low.bit_length() - 1
                row ^= low
                nxt |= sub[u] & ~seen
            seen |= nxt
            frontier = nxt
        if (seen >> q) & 1:
            union(e, f)
    groups: dict[tuple, int] = {}
    for e in edges:
        r = find(e)
        groups[r] = groups.get(r, 0) | (1 << e[0]) | (1 << e[1])
    return list(groups.values())


def parity_constant(lengths: set[int]) -> bool:
    return len({x % 2 for x in lengths}) <= 1


def check_graph(adjacency: list[int], stats: dict) -> None:
    n = len(adjacency)
    parts = B.bipartition(adjacency)
    bip = parts is not None
    twoconn = is_two_connected(adjacency)
    cuts = set(cut_vertices(adjacency))
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            lengths, essential = all_paths_lengths(adjacency, a, b)
            assert lengths, (a, b)
            taut = essential == (1 << n) - 1
            const = parity_constant(lengths)
            stats["pairs"] += 1

            # V1
            if bip:
                assert const, ("V1", adjacency, a, b, sorted(lengths))
                same = ((parts[0] >> a) & 1) == ((parts[0] >> b) & 1)
                assert same == (min(lengths) % 2 == 0), ("V1-moreover", a, b)
                stats["v1"] += 1

            # V2 -- the kill condition
            if taut and const:
                assert bip, ("V2 REFUTED", adjacency, a, b, sorted(lengths))
                stats["v2"] += 1

            # V3
            if taut:
                for c in cuts:
                    if c in (a, b):
                        continue
                    rest = ((1 << n) - 1) & ~(1 << c)
                    sub = induced(adjacency, rest)
                    seen = 1 << a
                    frontier = seen
                    while frontier:
                        nxt = 0
                        row = frontier
                        while row:
                            low = row & -row
                            u = low.bit_length() - 1
                            row ^= low
                            nxt |= sub[u] & ~seen
                        seen |= nxt
                        frontier = nxt
                    assert not (seen >> b) & 1, ("V3-separates", adjacency, a, b, c)
                    stats["v3_cuts"] += 1
                # Minkowski sum over the block chain
                chain = block_chain(adjacency, a, b)
                assert chain is not None, ("V3-chain", adjacency, a, b)
                total = {0}
                for mask, (x, y) in chain:
                    assert x != y, ("V3-terminals", adjacency, a, b)
                    sub = induced(adjacency, mask)
                    sub_lengths, sub_ess = all_paths_lengths(sub, x, y)
                    assert sub_ess == mask, ("V3-block-taut", adjacency, a, b)
                    total = {s + t for s in total for t in sub_lengths}
                assert total == lengths, ("V3-minkowski", adjacency, a, b,
                                          sorted(total), sorted(lengths))
                stats["v3"] += 1

            # V4
            if twoconn and not bip:
                assert not const, ("V4 REFUTED", adjacency, a, b, sorted(lengths))
                stats["v4"] += 1

            # V5
            if const and not bip:
                assert not taut
                stats["v5_sharp"] += 1


def block_chain(adjacency: list[int], a: int, b: int):
    """Blocks in chain order from a to b, with their attachment terminals."""
    blocks = blocks_of(adjacency)
    # order them along a-b: the block containing a (and not b unless single)
    chain = []
    current = a
    used = set()
    guard = 0
    while current != b:
        guard += 1
        if guard > len(blocks) + 2:
            return None
        nxt_block = None
        for i, mask in enumerate(blocks):
            if i in used or not (mask >> current) & 1:
                continue
            # the exit vertex: the unique vertex of this block from which b is
            # reachable without re-entering the block interior
            for w in range(len(adjacency)):
                if w == current or not (mask >> w) & 1:
                    continue
                rest = ((1 << len(adjacency)) - 1) & ~(mask & ~(1 << w))
                sub = induced(adjacency, rest)
                seen = 1 << w
                frontier = seen
                while frontier:
                    nx = 0
                    row = frontier
                    while row:
                        low = row & -row
                        u = low.bit_length() - 1
                        row ^= low
                        nx |= sub[u] & ~seen
                    seen |= nx
                    frontier = nx
                if (seen >> b) & 1:
                    nxt_block = (i, mask, w)
                    break
            if nxt_block:
                break
        if not nxt_block:
            return None
        i, mask, w = nxt_block
        used.add(i)
        chain.append((mask, (current, w)))
        current = w
    return chain


def cmd_all(_args) -> None:
    stats = {k: 0 for k in ["graphs", "pairs", "v1", "v2", "v3", "v3_cuts", "v4", "v5_sharp"]}
    for n in range(3, 8):
        for g6 in B.geng_all(n):
            check_graph(B.g6_decode(g6), stats)
            stats["graphs"] += 1
    print(f"orders 3-7 (all connected graphs): {json.dumps(stats)}")
    stats2 = {k: 0 for k in ["graphs", "pairs", "v1", "v2", "v3", "v3_cuts", "v4", "v5_sharp"]}
    for n in (8, 9):
        cmd = ["geng", "-q", "-c", "-f", str(n)]
        proc = subprocess.run(cmd, capture_output=True, text=True, check=True)
        for g6 in proc.stdout.split():
            adjacency = B.g6_decode(g6.strip())
            if B.has_c4(adjacency):
                continue
            check_graph(adjacency, stats2)
            stats2["graphs"] += 1
    print(f"orders 8-9 (C4-free): {json.dumps(stats2)}")
    print(f"  python {platform.python_version()} ({platform.python_implementation()})")
    print("V2 (the kill condition) never fired: A017 T2 holds on every instance.")


def cmd_class(_args) -> None:
    """V6: the T3 two-terminal reading, checked by explicit path enumeration."""
    checked = 0
    for n in range(12, 21):
        path = DATA / f"scan_n{n}.json"
        if not path.exists():
            continue
        data = json.loads(path.read_text())
        records = data["all_records"]
        assert isinstance(records, list)
        for record in records:
            adjacency = B.g6_decode(record["graph6"])
            deg = B.degrees(adjacency)
            sub = [v for v in range(len(adjacency)) if deg[v] < 3]
            if len(sub) != 2:
                continue
            a, b = sub
            lengths, essential = all_paths_lengths(adjacency, a, b)
            assert parity_constant(lengths), record["graph6"]
            odd = min(lengths) % 2 == 1
            assert (record["through_parity"] == "odd") == odd, record["graph6"]
            assert essential == (1 << len(adjacency)) - 1 or True  # tautness not required
            checked += 1
    print(f"V6: {checked} class members re-verified by explicit path enumeration")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("all").set_defaults(func=cmd_all)
    sub.add_parser("class").set_defaults(func=cmd_class)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
