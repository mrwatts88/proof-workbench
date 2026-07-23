#!/usr/bin/env python3
"""Exact labelled search at the edge-minimal P-002 frontier.

Vertices are assigned a nonincreasing target degree sequence.  The generator
completes all undecided neighbours of the least unfinished vertex, rejects an
edge immediately if it creates a 4-cycle, and forbids edges between vertices
whose target degrees both exceed three (A001/L002).
"""

from __future__ import annotations

import argparse
import itertools
import math
import platform
from collections import Counter
from collections.abc import Iterator
from dataclasses import dataclass, field


def has_cycle_of_length(adjacency: list[int], length: int) -> bool:
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


def is_connected(adjacency: list[int]) -> bool:
    seen = 1
    frontier = 1
    while frontier:
        neighbours = 0
        scan = frontier
        while scan:
            bit = scan & -scan
            scan ^= bit
            vertex = bit.bit_length() - 1
            neighbours |= adjacency[vertex]
        frontier = neighbours & ~seen
        seen |= frontier
    return seen == (1 << len(adjacency)) - 1


def creates_four_cycle(adjacency: list[int], u: int, v: int) -> bool:
    """Test whether adding the absent edge uv closes a length-three path."""
    scan = adjacency[u]
    while scan:
        bit = scan & -scan
        scan ^= bit
        neighbour = bit.bit_length() - 1
        if adjacency[neighbour] & adjacency[v]:
            return True
    return False


def edge_list(adjacency: list[int]) -> str:
    edges = []
    for u, neighbours in enumerate(adjacency):
        for v in range(u + 1, len(adjacency)):
            if neighbours & (1 << v):
                edges.append(f"{u}-{v}")
    return ",".join(edges)


def feasible_degree_sequences(n: int) -> Iterator[tuple[int, ...]]:
    """Sequences not excluded by C4 codegree counting and A001/L002."""
    pair_budget = math.comb(n, 2)
    for ascending in itertools.combinations_with_replacement(range(3, n), n):
        sequence = tuple(reversed(ascending))
        if sum(sequence) % 2:
            continue
        if sum(math.comb(degree, 2) for degree in sequence) > pair_budget:
            continue
        low_vertices = sum(degree == 3 for degree in sequence)
        if any(degree > low_vertices for degree in sequence if degree > 3):
            continue
        yield sequence


@dataclass
class SearchResult:
    nodes: int = 0
    c4_free: int = 0
    connected: int = 0
    with_eight_cycle: int = 0
    avoiding_eight_cycle: int = 0
    first_survivor: str | None = None
    profiles: Counter[str] = field(default_factory=Counter)


def survivor_profile(adjacency: list[int], target: tuple[int, ...]) -> str:
    if all(degree == 3 for degree in target):
        neighbours = [
            vertex
            for vertex in range(1, len(target))
            if adjacency[0] & (1 << vertex)
        ]
        internal_edges = sum(
            bool(adjacency[u] & (1 << v))
            for u, v in itertools.combinations(neighbours, 2)
        )
        return f"cubic:N0_internal_edges={internal_edges}"

    if target[:2] == (4, 4) and all(degree == 3 for degree in target[2:]):
        common = adjacency[0] & adjacency[1]
        shared = common.bit_count()
        if shared == 0:
            return "4,4:shared_low_neighbours=0"
        common_vertex = (common & -common).bit_length() - 1
        low_neighbours = adjacency[common_vertex] & ~0b11
        leaf_neighbour = (low_neighbours & -low_neighbours).bit_length() - 1
        high_incidence = (
            bool(adjacency[0] & (1 << leaf_neighbour))
            + bool(adjacency[1] & (1 << leaf_neighbour))
        )
        return f"4,4:shared=1,common_low_neighbour_type={high_incidence}"

    return "other"


def search_sequence(target: tuple[int, ...]) -> SearchResult:
    n = len(target)
    remaining = list(target)
    adjacency = [0] * n
    result = SearchResult()

    def permitted(u: int, v: int) -> bool:
        return not (target[u] > 3 and target[v] > 3)

    def viable(first: int) -> bool:
        unfinished = [v for v in range(first, n) if remaining[v]]
        if sum(remaining[v] for v in unfinished) % 2:
            return False
        for v in unfinished:
            capacity = sum(
                other != v and permitted(v, other) for other in unfinished
            )
            if remaining[v] > capacity:
                return False
        return True

    def complete() -> None:
        result.nodes += 1
        try:
            vertex = next(v for v, residual in enumerate(remaining) if residual)
        except StopIteration:
            result.c4_free += 1
            if not is_connected(adjacency):
                return
            result.connected += 1
            result.profiles[survivor_profile(adjacency, target)] += 1
            if has_cycle_of_length(adjacency, 8):
                result.with_eight_cycle += 1
            else:
                result.avoiding_eight_cycle += 1
                if result.first_survivor is None:
                    result.first_survivor = edge_list(adjacency)
            return

        candidates = [
            other
            for other in range(vertex + 1, n)
            if remaining[other] > 0 and permitted(vertex, other)
        ]
        needed = remaining[vertex]
        if len(candidates) < needed:
            return

        for neighbours in itertools.combinations(candidates, needed):
            added: list[int] = []
            valid = True
            remaining[vertex] = 0
            for other in neighbours:
                if creates_four_cycle(adjacency, vertex, other):
                    valid = False
                    break
                adjacency[vertex] |= 1 << other
                adjacency[other] |= 1 << vertex
                remaining[other] -= 1
                added.append(other)
                if remaining[other] < 0:
                    valid = False
                    break

            if valid and viable(vertex + 1):
                complete()

            for other in added:
                remaining[other] += 1
                adjacency[vertex] ^= 1 << other
                adjacency[other] ^= 1 << vertex
            remaining[vertex] = needed

    complete()
    return result


def cycle_graph(n: int) -> list[int]:
    adjacency = [0] * n
    for vertex in range(n):
        other = (vertex + 1) % n
        adjacency[vertex] |= 1 << other
        adjacency[other] |= 1 << vertex
    return adjacency


def self_check() -> None:
    assert has_cycle_of_length(cycle_graph(8), 8)
    assert not has_cycle_of_length(cycle_graph(7), 8)
    short_path = [0] * 3
    for u, v in ((0, 1), (1, 2)):
        short_path[u] |= 1 << v
        short_path[v] |= 1 << u
    assert not creates_four_cycle(short_path, 0, 2)
    path = [0] * 4
    for u, v in ((0, 1), (1, 2), (2, 3)):
        path[u] |= 1 << v
        path[v] |= 1 << u
    assert creates_four_cycle(path, 0, 3)
    assert len(list(feasible_degree_sequences(9))) == 2
    assert len(list(feasible_degree_sequences(10))) == 7


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("orders", nargs="*", type=int, default=[9, 10])
    args = parser.parse_args()

    print(f"Python {platform.python_version()}")
    self_check()
    print("self-checks passed")
    for n in args.orders:
        sequences = list(feasible_degree_sequences(n))
        print(f"n={n}: feasible_sequences={len(sequences)}")
        for sequence in sequences:
            result = search_sequence(sequence)
            print(
                f"  degrees={','.join(map(str, sequence))}"
                f" nodes={result.nodes}"
                f" c4_free={result.c4_free}"
                f" connected={result.connected}"
                f" with_C8={result.with_eight_cycle}"
                f" avoiding_C8={result.avoiding_eight_cycle}"
            )
            if result.first_survivor is not None:
                print(f"    first_survivor={result.first_survivor}")
            for profile, count in sorted(result.profiles.items()):
                print(f"    profile={profile} count={count}")


if __name__ == "__main__":
    main()
