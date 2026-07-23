#!/usr/bin/env python3
"""Search a tightly delimited cubic family for a local-route survivor.

The vertices 0,...,12 induce the path 0-1-...-12.  Vertices 13,...,17
are independent and each receives three neighbours on the path.  The two
path endpoints receive two such neighbours and every internal path vertex
receives one, so every vertex in the completed graph is cubic.
"""

from __future__ import annotations

from itertools import combinations
import platform


PATH_ORDER = 13
OUTSIDE_ORDER = 5
ORDER = PATH_ORDER + OUTSIDE_ORDER
FORBIDDEN_LENGTHS = (4, 8, 16)


def add_edge(adjacency: list[int], u: int, v: int) -> None:
    adjacency[u] |= 1 << v
    adjacency[v] |= 1 << u


def remove_edge(adjacency: list[int], u: int, v: int) -> None:
    adjacency[u] &= ~(1 << v)
    adjacency[v] &= ~(1 << u)


def neighbours(mask: int):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def has_cycle_of_length(adjacency: list[int], length: int) -> bool:
    """Return whether the simple graph has a simple cycle of exact length."""

    for start in range(ORDER):
        start_bit = 1 << start

        def extend(current: int, used: int, depth: int) -> bool:
            if depth == length:
                return bool(adjacency[current] & start_bit)
            candidates = adjacency[current] & ~used
            # Make start the least vertex on the cycle to avoid redundant roots.
            candidates &= ~((1 << (start + 1)) - 1)
            for nxt in neighbours(candidates):
                if extend(nxt, used | (1 << nxt), depth + 1):
                    return True
            return False

        for second in neighbours(adjacency[start] & ~((1 << (start + 1)) - 1)):
            if extend(second, start_bit | (1 << second), 2):
                return True
    return False


def cycle_lengths(adjacency: list[int]) -> list[int]:
    return [
        length
        for length in range(3, ORDER + 1)
        if has_cycle_of_length(adjacency, length)
    ]


def degree(adjacency: list[int], vertex: int) -> int:
    return adjacency[vertex].bit_count()


def cycle_graph(length: int) -> list[int]:
    adjacency = [0] * ORDER
    for vertex in range(length):
        add_edge(adjacency, vertex, (vertex + 1) % length)
    return adjacency


def self_check() -> None:
    path = [0] * ORDER
    for vertex in range(ORDER - 1):
        add_edge(path, vertex, vertex + 1)
    assert not any(
        has_cycle_of_length(path, length) for length in FORBIDDEN_LENGTHS
    )
    for target in FORBIDDEN_LENGTHS:
        adjacency = cycle_graph(target)
        for length in FORBIDDEN_LENGTHS:
            assert has_cycle_of_length(adjacency, length) == (length == target)


def search() -> tuple[list[int] | None, dict[str, int]]:
    adjacency = [0] * ORDER
    for vertex in range(PATH_ORDER - 1):
        add_edge(adjacency, vertex, vertex + 1)

    remaining = [1] * PATH_ORDER
    remaining[0] = remaining[-1] = 2
    stats = {
        "nodes": 0,
        "completed": 0,
        "pruned_capacity": 0,
        "pruned_c4": 0,
        "pruned_c8": 0,
        "rejected_c16": 0,
    }

    def visit(outside_index: int, previous: tuple[int, int, int]) -> list[int] | None:
        stats["nodes"] += 1
        hubs_left = OUTSIDE_ORDER - outside_index
        if sum(remaining) != 3 * hubs_left:
            stats["pruned_capacity"] += 1
            return None
        if any(value < 0 or value > hubs_left for value in remaining):
            stats["pruned_capacity"] += 1
            return None
        if outside_index == OUTSIDE_ORDER:
            stats["completed"] += 1
            if has_cycle_of_length(adjacency, 16):
                stats["rejected_c16"] += 1
                return None
            return adjacency.copy()

        available = [vertex for vertex, value in enumerate(remaining) if value]
        hub = PATH_ORDER + outside_index
        for triple in combinations(available, 3):
            # Outside vertices are interchangeable; canonicalize their triples.
            if triple < previous:
                continue
            for vertex in triple:
                remaining[vertex] -= 1
                add_edge(adjacency, hub, vertex)

            if has_cycle_of_length(adjacency, 4):
                stats["pruned_c4"] += 1
            elif has_cycle_of_length(adjacency, 8):
                stats["pruned_c8"] += 1
            else:
                result = visit(outside_index + 1, triple)
                if result is not None:
                    return result

            for vertex in triple:
                remove_edge(adjacency, hub, vertex)
                remaining[vertex] += 1
        return None

    result = visit(0, (-1, -1, -1))
    return result, stats


def validate(adjacency: list[int]) -> None:
    assert all(degree(adjacency, vertex) == 3 for vertex in range(ORDER))
    for u in range(PATH_ORDER):
        for v in range(u + 1, PATH_ORDER):
            expected = v == u + 1
            assert bool(adjacency[u] & (1 << v)) == expected
    for length in FORBIDDEN_LENGTHS:
        assert not has_cycle_of_length(adjacency, length)


def main() -> None:
    self_check()
    print("self-checks passed")
    result, stats = search()
    print(f"Python {platform.python_version()}")
    print("family=P13_plus_5_independent_cubic_hubs")
    print("stats=" + ",".join(f"{key}:{value}" for key, value in stats.items()))
    if result is None:
        print("survivor=none")
        return
    validate(result)
    edges = [
        (u, v)
        for u in range(ORDER)
        for v in neighbours(result[u])
        if u < v
    ]
    print("survivor=found")
    print("edges=" + " ".join(f"{u}-{v}" for u, v in edges))
    print("cycle_lengths=" + ",".join(map(str, cycle_lengths(result))))


if __name__ == "__main__":
    main()
