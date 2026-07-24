"""Shared helpers for E005: graph6 codec and imports of E004's validated detectors.

The cycle/path detectors are imported from E004 (`saturated.py`), where they
carry five recorded validation anchors; this module adds only graph6
decoding/encoding (needed to talk to nauty's geng/labelg/planarg) and its
self-tests. Adjacency graphs are `list[int]` bitmasks exactly as in E004.
"""

from __future__ import annotations

import importlib.util
import pathlib
import sys

_E004_DIR = (
    pathlib.Path(__file__).resolve().parent.parent
    / "E004-order-11-saturated-search"
)


def load_e004():
    """Import E004's saturated.py as a module without running its CLI."""
    spec = importlib.util.spec_from_file_location(
        "e004_saturated", _E004_DIR / "saturated.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules["e004_saturated"] = module
    spec.loader.exec_module(module)
    return module


# ------------------------------------------------------------------- graph6

def g6_decode(line: str) -> list[int]:
    """Decode a graph6 string (n <= 62) to bitmask adjacency."""
    data = [ord(ch) - 63 for ch in line.strip()]
    if any(value < 0 or value > 63 for value in data):
        raise ValueError(f"invalid graph6 characters: {line!r}")
    n = data[0]
    if n == 63:
        raise ValueError("graph6 with n >= 63 not supported here")
    bits_needed = n * (n - 1) // 2
    words = data[1:]
    if len(words) != (bits_needed + 5) // 6:
        raise ValueError(f"wrong graph6 length for n={n}: {line!r}")
    adjacency = [0] * n
    index = 0
    for v in range(1, n):
        for u in range(v):
            word = words[index // 6]
            bit = (word >> (5 - (index % 6))) & 1
            if bit:
                adjacency[u] |= 1 << v
                adjacency[v] |= 1 << u
            index += 1
    return adjacency


def g6_encode(adjacency: list[int]) -> str:
    """Encode bitmask adjacency (n <= 62) as a graph6 string."""
    n = len(adjacency)
    if n >= 63:
        raise ValueError("graph6 with n >= 63 not supported here")
    bits = []
    for v in range(1, n):
        for u in range(v):
            bits.append(1 if adjacency[u] & (1 << v) else 0)
    while len(bits) % 6:
        bits.append(0)
    chars = [chr(n + 63)]
    for i in range(0, len(bits), 6):
        word = 0
        for bit in bits[i : i + 6]:
            word = (word << 1) | bit
        chars.append(chr(word + 63))
    return "".join(chars)


def degrees(adjacency: list[int]) -> list[int]:
    return [row.bit_count() for row in adjacency]


def nonedges(adjacency: list[int]) -> list[tuple[int, int]]:
    n = len(adjacency)
    return [
        (u, v)
        for u in range(n)
        for v in range(u + 1, n)
        if not adjacency[u] & (1 << v)
    ]


def self_check() -> None:
    sat = load_e004()
    # K4 in graph6 is "C~": every one of the six upper-triangle bits set.
    k4 = g6_decode("C~")
    assert degrees(k4) == [3, 3, 3, 3]
    assert sat.has_cycle_of_length(k4, 3) and sat.has_cycle_of_length(k4, 4)
    # Round trip on K4 and on a 5-cycle built from E004's ring().
    assert g6_encode(k4) == "C~"
    ring5 = sat.ring(5)
    assert g6_decode(g6_encode(ring5)) == ring5
    # E004's L016 double-theta graph at k=4 round-trips and keeps its
    # recorded properties (no C4/C8/C16, a length-15 witness path).
    theta = sat.l016_graph(4)
    again = g6_decode(g6_encode(theta))
    assert again == theta
    for forbidden in (4, 8, 16):
        assert not sat.has_cycle_of_length(again, forbidden)
    assert sat.has_uv_path_of_length(again, 0, 2, 15)
    print("e005lib self-checks passed")


if __name__ == "__main__":
    self_check()
