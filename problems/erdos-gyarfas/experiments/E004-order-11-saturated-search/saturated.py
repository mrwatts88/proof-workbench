#!/usr/bin/env python3
"""Exhaustive order-11 search for saturated counterexamples (P-002, E004).

At order n <= 15 the only power-of-two cycle lengths that fit are 4 and 8,
and the only Mersenne witness lengths 2^k - 1 that fit in a simple path are
3 and 7.  A saturated counterexample of such an order (A005/L008) is
therefore exactly a graph with minimum degree at least 3, no 4-cycle, no
8-cycle, in which every nonedge is joined by a simple path of length 3 or 7.

The generator assigns one fixed nonincreasing degree sequence, completes all
undecided neighbours of the least unfinished vertex, and rejects an edge
exactly when it closes a path of length 3 or 7 between its endpoints, which
is equivalent to creating a C4 or C8 at that step.  Every labelled graph
with the target degrees and no C4/C8 is reached exactly once.  Leaves are
re-verified with independent detectors and classified by the saturation
condition.

Degree-sequence coverage: a C4-free graph has at most one common neighbour
per vertex pair, so sum(C(d_v,2)) <= C(n,2); with minimum degree 3 and even
degree sum this leaves finitely many sequences, and any graph can be
relabelled so that its degrees are nonincreasing.

Optional canonical restriction of vertex 0's neighbourhood (--symmetry):
within each block of equal-degree vertices, N(0) may be assumed to occupy a
prefix of the block, because permutations inside a block fix the degree
placement and some such permutation moves N(0) to the prefixes.
"""

from __future__ import annotations

import argparse
import itertools
import math
import platform
import sys
from collections import Counter
from collections.abc import Iterator
from dataclasses import dataclass, field

WITNESS_LENGTHS = (3, 7)  # Mersenne path lengths 2^k - 1 realizable at n <= 15
REJECT_LENGTHS = (3, 7)   # closing these paths creates C4 or C8


# ----------------------------------------------------------------- detectors

def has_uv_path_of_length(adjacency: list[int], u: int, v: int, length: int) -> bool:
    """Is there a simple path with exactly `length` edges from u to v?"""
    if length <= 0:
        return False
    v_bit = 1 << v

    def extend(current: int, used: int, left: int) -> bool:
        if left == 1:
            return bool(adjacency[current] & v_bit & ~used)
        available = adjacency[current] & ~used & ~v_bit
        while available:
            bit = available & -available
            available ^= bit
            if extend(bit.bit_length() - 1, used | bit, left - 1):
                return True
        return False

    return extend(u, 1 << u, length)


def creates_power_cycle(adjacency: list[int], u: int, v: int) -> bool:
    """Would adding the absent edge uv close a 4-cycle or an 8-cycle?"""
    return any(
        has_uv_path_of_length(adjacency, u, v, path_length)
        for path_length in REJECT_LENGTHS
    )


def has_cycle_of_length(adjacency: list[int], length: int) -> bool:
    """Independent whole-graph cycle detector (as validated in E001/E002)."""
    n = len(adjacency)
    if length > n:
        return False

    def extend(start: int, current: int, used: int, vertices: int) -> bool:
        if vertices == length:
            return bool(adjacency[current] & (1 << start))
        available = adjacency[current] & ~used
        while available:
            bit = available & -available
            available ^= bit
            nxt = bit.bit_length() - 1
            if extend(start, nxt, used | bit, vertices + 1):
                return True
        return False

    for start in range(n):
        first_steps = adjacency[start] & ~((1 << (start + 1)) - 1)
        while first_steps:
            bit = first_steps & -first_steps
            first_steps ^= bit
            nxt = bit.bit_length() - 1
            if extend(start, nxt, (1 << start) | bit, 2):
                return True
    return False


def codegree_c4_free(adjacency: list[int]) -> bool:
    """Independent C4 test: no two vertices share two common neighbours."""
    n = len(adjacency)
    return all(
        (adjacency[u] & adjacency[v]).bit_count() <= 1
        for u in range(n)
        for v in range(u + 1, n)
    )


def is_connected(adjacency: list[int]) -> bool:
    seen = 1
    frontier = 1
    while frontier:
        neighbours = 0
        scan = frontier
        while scan:
            bit = scan & -scan
            scan ^= bit
            neighbours |= adjacency[bit.bit_length() - 1]
        frontier = neighbours & ~seen
        seen |= frontier
    return seen == (1 << len(adjacency)) - 1


def is_bipartite(adjacency: list[int]) -> bool:
    n = len(adjacency)
    colour = [-1] * n
    for root in range(n):
        if colour[root] >= 0:
            continue
        colour[root] = 0
        queue = [root]
        while queue:
            vertex = queue.pop()
            scan = adjacency[vertex]
            while scan:
                bit = scan & -scan
                scan ^= bit
                other = bit.bit_length() - 1
                if colour[other] < 0:
                    colour[other] = 1 - colour[vertex]
                    queue.append(other)
                elif colour[other] == colour[vertex]:
                    return False
    return True


def is_saturated(adjacency: list[int]) -> bool:
    """Does every nonedge have a simple path of length 3 or 7 across it?"""
    n = len(adjacency)
    for u in range(n):
        for v in range(u + 1, n):
            if adjacency[u] & (1 << v):
                continue
            if not any(
                has_uv_path_of_length(adjacency, u, v, path_length)
                for path_length in WITNESS_LENGTHS
            ):
                return False
    return True


def edge_list(adjacency: list[int]) -> str:
    edges = []
    for u, neighbours in enumerate(adjacency):
        for v in range(u + 1, len(adjacency)):
            if neighbours & (1 << v):
                edges.append(f"{u}-{v}")
    return ",".join(edges)


# ------------------------------------------------------------ search spaces

def feasible_degree_sequences(n: int) -> list[tuple[int, ...]]:
    """All nonincreasing sequences with degrees >= 3, even sum, and the
    C4-free codegree bound sum(C(d,2)) <= C(n,2).  No other filter."""
    pair_budget = math.comb(n, 2)
    sequences = []
    for ascending in itertools.combinations_with_replacement(range(3, n), n):
        sequence = tuple(reversed(ascending))
        if sum(sequence) % 2:
            continue
        if sum(math.comb(degree, 2) for degree in sequence) > pair_budget:
            continue
        sequences.append(sequence)
    return sequences


def canonical_root_neighbourhoods(target: tuple[int, ...]) -> list[tuple[int, ...]]:
    """Neighbour sets for vertex 0 restricted to per-block prefixes."""
    n = len(target)
    blocks: list[list[int]] = []
    for vertex in range(1, n):
        if blocks and target[vertex] == target[blocks[-1][0]]:
            blocks[-1].append(vertex)
        else:
            blocks.append([vertex])
    needed = target[0]

    result: list[tuple[int, ...]] = []

    def place(block_index: int, still_needed: int, chosen: list[int]) -> None:
        if still_needed == 0:
            result.append(tuple(chosen))
            return
        if block_index == len(blocks):
            return
        block = blocks[block_index]
        for take in range(min(still_needed, len(block)) + 1):
            place(block_index + 1, still_needed - take, chosen + block[:take])

    place(0, needed, [])
    return result


@dataclass
class SearchResult:
    nodes: int = 0
    complete_graphs: int = 0
    saturated: int = 0
    survivors: list[str] = field(default_factory=list)
    leaf_cycle_profile: Counter[str] = field(default_factory=Counter)


def search_sequence(
    target: tuple[int, ...],
    *,
    reject_lengths: tuple[int, ...] = REJECT_LENGTHS,
    symmetry: bool = True,
    classify_leaf_c8: bool = False,
    classify_saturation: bool = True,
) -> SearchResult:
    """Enumerate labelled graphs with the exact target degrees, rejecting an
    edge exactly when it closes a path whose length is in reject_lengths."""
    n = len(target)
    remaining = list(target)
    adjacency = [0] * n
    result = SearchResult()

    def viable(first: int) -> bool:
        unfinished = [v for v in range(first, n) if remaining[v]]
        if sum(remaining[v] for v in unfinished) % 2:
            return False
        return all(remaining[v] <= len(unfinished) - 1 for v in unfinished)

    def rejected(u: int, v: int) -> bool:
        return any(
            has_uv_path_of_length(adjacency, u, v, path_length)
            for path_length in reject_lengths
        )

    def add_edge(u: int, v: int) -> None:
        adjacency[u] |= 1 << v
        adjacency[v] |= 1 << u
        remaining[u] -= 1
        remaining[v] -= 1

    def remove_edge(u: int, v: int) -> None:
        adjacency[u] ^= 1 << v
        adjacency[v] ^= 1 << u
        remaining[u] += 1
        remaining[v] += 1

    def handle_leaf() -> None:
        assert all(residual == 0 for residual in remaining)
        degrees = tuple(neighbours.bit_count() for neighbours in adjacency)
        assert degrees == target
        if 3 in reject_lengths:
            assert codegree_c4_free(adjacency)
        if 7 in reject_lengths:
            assert not has_cycle_of_length(adjacency, 8)
        result.complete_graphs += 1
        if classify_leaf_c8:
            key = "with_C8" if has_cycle_of_length(adjacency, 8) else "no_C8"
            result.leaf_cycle_profile[key] += 1
            if key == "with_C8":
                return
        if not classify_saturation:
            return
        if is_saturated(adjacency):
            result.saturated += 1
            assert is_connected(adjacency)
            assert not is_bipartite(adjacency)
            result.survivors.append(edge_list(adjacency))

    def apply_neighbour_set(vertex: int, neighbours: tuple[int, ...]) -> None:
        added: list[int] = []
        valid = True
        for other in neighbours:
            if rejected(vertex, other):
                valid = False
                break
            add_edge(vertex, other)
            added.append(other)
        if valid and remaining[vertex] == 0 and viable(vertex + 1):
            complete()
        for other in reversed(added):
            remove_edge(vertex, other)

    def choose(vertex: int, candidates: list[int], index: int, still_needed: int) -> None:
        result.nodes += 1
        if still_needed == 0:
            if viable(vertex + 1):
                complete()
            return
        for position in range(index, len(candidates) - still_needed + 1):
            other = candidates[position]
            if remaining[other] == 0:
                continue
            if rejected(vertex, other):
                continue
            add_edge(vertex, other)
            choose(vertex, candidates, position + 1, still_needed - 1)
            remove_edge(vertex, other)

    def complete() -> None:
        try:
            vertex = next(v for v, residual in enumerate(remaining) if residual)
        except StopIteration:
            handle_leaf()
            return
        if vertex == 0 and symmetry:
            for neighbours in canonical_root_neighbourhoods(target):
                apply_neighbour_set(vertex, neighbours)
            return
        candidates = [
            other
            for other in range(vertex + 1, n)
            if remaining[other] > 0
        ]
        if len(candidates) < remaining[vertex]:
            return
        choose(vertex, candidates, 0, remaining[vertex])

    complete()
    return result


# ------------------------------------------------------------- self checks

def ring(n: int) -> list[int]:
    adjacency = [0] * n
    for vertex in range(n):
        other = (vertex + 1) % n
        adjacency[vertex] |= 1 << other
        adjacency[other] |= 1 << vertex
    return adjacency


def graph_from_edges(n: int, edges: list[tuple[int, int]]) -> list[int]:
    adjacency = [0] * n
    for u, v in edges:
        adjacency[u] |= 1 << v
        adjacency[v] |= 1 << u
    return adjacency


def cube_graph() -> list[int]:
    edges = []
    for mask in range(8):
        for bit in range(3):
            other = mask ^ (1 << bit)
            if mask < other:
                edges.append((mask, other))
    return graph_from_edges(8, edges)


def l016_graph(k: int) -> list[int]:
    """C7 plus disjoint ears c0..c4 and c5..c2 of length 2^(k-1)-1 each."""
    ear_length = 2 ** (k - 1) - 1
    n = 7 + 2 * (ear_length - 1)
    edges = [(i, (i + 1) % 7) for i in range(7)]
    inner1 = list(range(7, 7 + ear_length - 1))
    edges += [(0, inner1[0]), (inner1[-1], 4)]
    edges += [(a, b) for a, b in itertools.pairwise(inner1)]
    inner2 = list(range(7 + ear_length - 1, n))
    edges += [(5, inner2[0]), (inner2[-1], 2)]
    edges += [(a, b) for a, b in itertools.pairwise(inner2)]
    return graph_from_edges(n, edges)


HAND_SEQUENCES_11 = [
    (7, 4) + (3,) * 9,
    (6, 5) + (3,) * 9,
    (6, 4, 4) + (3,) * 8,
    (6,) + (3,) * 10,
    (5, 5, 4) + (3,) * 8,
    (5, 4, 4, 4, 4, 4) + (3,) * 5,
    (5, 4, 4, 4) + (3,) * 7,
    (5, 4) + (3,) * 9,
    (4,) * 7 + (3,) * 4,
    (4,) * 5 + (3,) * 6,
    (4, 4, 4) + (3,) * 8,
    (4,) + (3,) * 10,
]


def self_check() -> None:
    # cycle detector on rings
    assert has_cycle_of_length(ring(8), 8)
    assert not has_cycle_of_length(ring(7), 8)
    assert has_cycle_of_length(ring(4), 4)
    assert not has_cycle_of_length(ring(9), 8)

    # exact-length path detector
    path8 = graph_from_edges(8, [(i, i + 1) for i in range(7)])
    assert has_uv_path_of_length(path8, 0, 7, 7)
    assert not has_uv_path_of_length(path8, 0, 7, 6)
    open_c8 = graph_from_edges(8, [(i, i + 1) for i in range(7)])
    assert creates_power_cycle(open_c8, 0, 7)
    open_c6 = graph_from_edges(6, [(i, i + 1) for i in range(5)])
    assert not creates_power_cycle(open_c6, 0, 5)
    open_c4 = graph_from_edges(4, [(0, 1), (1, 2), (2, 3)])
    assert creates_power_cycle(open_c4, 0, 3)

    # saturation samples: C5 yes; C6 and the bipartite cube no; K5 vacuously
    assert is_saturated(ring(5))
    assert not is_saturated(ring(6))
    assert not is_saturated(cube_graph())
    complete5 = [(0b11111 ^ (1 << v)) for v in range(5)]
    assert is_saturated(complete5)

    # the L016 double-theta graph at k=4: no C4, C8, C16; the 15-edge witness
    witness_graph = l016_graph(4)
    for power in (4, 8, 16):
        assert not has_cycle_of_length(witness_graph, power)
    assert has_uv_path_of_length(witness_graph, 0, 2, 15)
    assert has_cycle_of_length(witness_graph, 7)
    assert has_cycle_of_length(witness_graph, 17)
    assert not is_bipartite(witness_graph)

    # degree-sequence coverage
    assert feasible_degree_sequences(7) == []
    assert len(feasible_degree_sequences(9)) == 2
    assert len(feasible_degree_sequences(10)) == 7
    assert sorted(feasible_degree_sequences(11)) == sorted(HAND_SEQUENCES_11)

    # canonical root neighbourhoods: unique choice in the near-cubic case
    assert canonical_root_neighbourhoods((4,) + (3,) * 10) == [(1, 2, 3, 4)]

    # bipartiteness detector
    assert is_bipartite(cube_graph())
    assert not is_bipartite(ring(5))


# ------------------------------------------------------------------- modes

def run_validation() -> None:
    """Anchor runs against E001 and E002 plus the symmetry identity."""
    cubic8 = (3,) * 8
    total8 = search_sequence(
        cubic8, reject_lengths=(), symmetry=False, classify_saturation=False
    )
    print(f"V1 n=8 cubic, no rejection: complete={total8.complete_graphs} (E001: 19355)")
    assert total8.complete_graphs == 19355

    cubic10 = (3,) * 10
    v2 = search_sequence(
        cubic10, reject_lengths=(3,), symmetry=False, classify_leaf_c8=True
    )
    profile = dict(v2.leaf_cycle_profile)
    print(
        f"V2 n=10 cubic, C4 rejection only: c4_free={v2.complete_graphs}"
        f" with_C8={profile.get('with_C8', 0)}"
        f" no_C8={profile.get('no_C8', 0)} (E002: 937440, 937440, 0)"
    )
    assert v2.complete_graphs == 937440
    assert profile.get("with_C8", 0) == 937440
    assert profile.get("no_C8", 0) == 0

    v3 = search_sequence(
        cubic10, reject_lengths=(3,), symmetry=True, classify_leaf_c8=True
    )
    print(
        f"V3 n=10 cubic, C4 rejection, canonical N(0): c4_free={v3.complete_graphs}"
        f" (expected 937440/84 = 11160)"
    )
    assert v3.complete_graphs == 11160
    assert v3.leaf_cycle_profile.get("no_C8", 0) == 0

    v4 = search_sequence(cubic10, reject_lengths=(3, 7), symmetry=True)
    print(f"V4 n=10 cubic, C4+C8 rejection, canonical N(0): leaves={v4.complete_graphs} (expected 0)")
    assert v4.complete_graphs == 0

    # V5: positive control against over-rejection of C8: on n=8 cubic graphs,
    # C8-free graphs exist (the 35 labelled copies of two disjoint K4's are a
    # hand-proved floor), so incremental length-7 rejection must reproduce the
    # count classified by the independent whole-graph detector.
    reject7 = search_sequence(
        cubic8, reject_lengths=(7,), symmetry=False, classify_saturation=False
    )
    classified = search_sequence(
        cubic8,
        reject_lengths=(),
        symmetry=False,
        classify_leaf_c8=True,
        classify_saturation=False,
    )
    independent_no_c8 = classified.leaf_cycle_profile.get("no_C8", 0)
    print(
        f"V5 n=8 cubic: incremental C8-free={reject7.complete_graphs}"
        f" independent C8-free={independent_no_c8} (must agree; >= 35)"
    )
    assert reject7.complete_graphs == independent_no_c8 >= 35
    print("validation anchors passed")


def run_order(n: int, *, symmetry: bool) -> None:
    # The constants (3, 7) for witnesses and (4, 8) for power cycles are the
    # complete lists only while 2^4 - 1 = 15 exceeds n - 1 and 2^4 = 16
    # exceeds n; refuse orders where the collapse no longer holds.
    assert 4 <= n <= 15, "witness/power collapse valid only for orders 4..15"
    sequences = feasible_degree_sequences(n)
    print(f"n={n}: feasible_sequences={len(sequences)} symmetry={'on' if symmetry else 'off'}")
    total_nodes = 0
    total_complete = 0
    total_saturated = 0
    for sequence in sequences:
        result = search_sequence(
            sequence, reject_lengths=REJECT_LENGTHS, symmetry=symmetry
        )
        total_nodes += result.nodes
        total_complete += result.complete_graphs
        total_saturated += result.saturated
        print(
            f"  degrees={','.join(map(str, sequence))}"
            f" nodes={result.nodes}"
            f" c4c8_free={result.complete_graphs}"
            f" saturated={result.saturated}"
        )
        for survivor in result.survivors:
            print(f"    survivor={survivor}")
        sys.stdout.flush()
    print(
        f"n={n} totals: nodes={total_nodes}"
        f" c4c8_free={total_complete} saturated={total_saturated}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("orders", nargs="*", type=int, default=[11])
    parser.add_argument("--validate", action="store_true")
    parser.add_argument("--no-symmetry", action="store_true")
    args = parser.parse_args()

    print(f"Python {platform.python_version()}")
    self_check()
    print("self-checks passed")
    if args.validate:
        run_validation()
        return
    for n in args.orders:
        run_order(n, symmetry=not args.no_symmetry)


if __name__ == "__main__":
    main()
