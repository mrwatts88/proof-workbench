#!/usr/bin/env python3
"""Exact small-graph checks for P-002.

The first census enumerates every labelled simple graph through seven vertices.
The second independently generates every labelled cubic graph through eight
vertices by completing the neighbours of the least unfinished vertex.
"""

from __future__ import annotations

import argparse
import itertools
import platform
from collections.abc import Iterator


def has_four_cycle(adjacency: list[int]) -> bool:
    """Return whether two vertices have at least two common neighbours."""
    for u in range(len(adjacency)):
        for v in range(u + 1, len(adjacency)):
            if (adjacency[u] & adjacency[v]).bit_count() >= 2:
                return True
    return False


def has_cycle_of_length(adjacency: list[int], length: int) -> bool:
    """Search exactly for a simple cycle of the requested length."""
    n = len(adjacency)
    if length > n:
        return False
    if length == 4:
        return has_four_cycle(adjacency)

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
        # Requiring start to be the least cycle vertex avoids redundant searches.
        allowed = adjacency[start] & ~((1 << (start + 1)) - 1)
        while allowed:
            bit = allowed & -allowed
            allowed ^= bit
            nxt = bit.bit_length() - 1
            if extend(start, nxt, (1 << start) | bit, 2):
                return True
    return False


def has_power_of_two_cycle(adjacency: list[int]) -> bool:
    length = 4
    while length <= len(adjacency):
        if has_cycle_of_length(adjacency, length):
            return True
        length *= 2
    return False


def cycle_graph(n: int) -> list[int]:
    adjacency = [0] * n
    for vertex in range(n):
        other = (vertex + 1) % n
        adjacency[vertex] |= 1 << other
        adjacency[other] |= 1 << vertex
    return adjacency


def self_check() -> None:
    assert has_power_of_two_cycle(cycle_graph(4))
    assert not has_power_of_two_cycle(cycle_graph(6))
    assert has_power_of_two_cycle(cycle_graph(8))


def all_simple_graphs(n: int) -> Iterator[list[int]]:
    edges = [(u, v) for u in range(n) for v in range(u + 1, n)]
    for edge_mask in range(1 << len(edges)):
        if edge_mask.bit_count() * 2 < 3 * n:
            continue
        adjacency = [0] * n
        for index, (u, v) in enumerate(edges):
            if edge_mask & (1 << index):
                adjacency[u] |= 1 << v
                adjacency[v] |= 1 << u
        if min(map(int.bit_count, adjacency), default=0) >= 3:
            yield adjacency


def labelled_regular_graphs(n: int, degree: int) -> Iterator[list[int]]:
    """Generate each labelled simple degree-regular graph exactly once."""
    remaining = [degree] * n
    adjacency = [0] * n

    def viable(first: int) -> bool:
        if sum(remaining[first:]) % 2:
            return False
        unfinished = [v for v in range(first, n) if remaining[v]]
        return all(remaining[v] <= len(unfinished) - 1 for v in unfinished)

    def complete() -> Iterator[list[int]]:
        try:
            vertex = next(v for v, residual in enumerate(remaining) if residual)
        except StopIteration:
            yield adjacency.copy()
            return

        candidates = [
            other
            for other in range(vertex + 1, n)
            if remaining[other] > 0
        ]
        needed = remaining[vertex]
        if len(candidates) < needed:
            return

        for neighbours in itertools.combinations(candidates, needed):
            remaining[vertex] = 0
            for other in neighbours:
                remaining[other] -= 1
                adjacency[vertex] |= 1 << other
                adjacency[other] |= 1 << vertex

            if min(remaining, default=0) >= 0 and viable(vertex + 1):
                yield from complete()

            for other in neighbours:
                remaining[other] += 1
                adjacency[vertex] ^= 1 << other
                adjacency[other] ^= 1 << vertex
            remaining[vertex] = needed

    if n * degree % 2 == 0 and degree < n:
        yield from complete()


def report_simple(max_n: int) -> None:
    print("all labelled simple graphs with minimum degree at least 3")
    for n in range(4, max_n + 1):
        tested = 0
        cubic = 0
        avoiding = 0
        for adjacency in all_simple_graphs(n):
            tested += 1
            cubic += all(mask.bit_count() == 3 for mask in adjacency)
            avoiding += not has_power_of_two_cycle(adjacency)
        print(
            f"n={n}: tested={tested}, cubic={cubic}, "
            f"avoiding_power_cycle={avoiding}"
        )


def report_cubic(max_n: int) -> None:
    print("all labelled cubic graphs")
    for n in range(4, max_n + 1, 2):
        tested = 0
        avoiding = 0
        for adjacency in labelled_regular_graphs(n, 3):
            tested += 1
            avoiding += not has_power_of_two_cycle(adjacency)
        print(f"n={n}: tested={tested}, avoiding_power_cycle={avoiding}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--simple-through", type=int, default=7)
    parser.add_argument("--cubic-through", type=int, default=8)
    args = parser.parse_args()

    print(f"Python {platform.python_version()}")
    self_check()
    print("cycle-detector self-checks passed")
    report_simple(args.simple_through)
    report_cubic(args.cubic_through)


if __name__ == "__main__":
    main()
