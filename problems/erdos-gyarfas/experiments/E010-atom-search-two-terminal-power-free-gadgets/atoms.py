"""E010: exhaustive search for atoms (A011) at small orders.

An atom would disprove statement 0.1 via the ring/doubling assemblies of
A011 (lemmas R3/R4):

  1-atom: connected, power-free ({C4,C8}-free suffices for n <= 15;
          {C4,C8,C16}-free for 16 <= n <= 31), exactly one vertex of
          degree < 3, that vertex of degree 1 or 2, all others >= 3.
  2-atom: connected, power-free, exactly two sub-cubic vertices a, b with
          deg(a)+deg(b) >= 3 (each >= 1), all others >= 3, and the set S of
          simple a-b path lengths satisfying max(S) < 2*min(S).

Coverage argument for orders searched here (recorded in A011): an atom with
both terminals of degree >= 3 would itself be a minimum-degree-3 power-free
graph, excluded through order 18 by C023/L022; an atom with exactly one
sub-cubic vertex is a 1-atom; so enumerating connected graphs with minimum
degree >= 1 and at most two sub-cubic vertices covers every atom on <= n
vertices.  The stream is geng -c -f -d1 with the edge lower bound
ceil((3n-4)/2) implied by the degree profile (valid for every graph in the
class, so no atom is lost).

Everything downstream of geng is re-checked: degree profile from the decoded
adjacency, C4 by the independent codegree test, C8/C16 by the E004 detector
(anchored in E004/E005/E006).  Path-length sets are enumerated by DFS over
simple paths with a BFS distance cross-check (min S must equal dist(a,b)).

Anchors (subcommand `anchors`):
  A1  geng connected cubic counts at n = 8, 10, 12 equal OEIS A002851
      (5, 19, 85).
  A2  the pipeline restricted to zero sub-cubic vertices at n = 14
      reproduces the recorded C4-free min-degree-3 connected class size
      6059 (C016) with zero {C4,C8}-free survivors (L017/L018 frontier).
  A3  K_{3,3}-e: S = {3,5} (so ratio 5/3), cycle spectrum {4,6}.
  A4  the L=3 Bondy-Vince ring of K_{3,3}-e has cycle spectrum exactly
      {4,6,9,11,13,15} -- the spectrum quoted for their Figure 1 (C024),
      an external published anchor for the ring builder and the detector.
  A5  the Petersen graph spectrum is {5,6,8,9} and deleting one edge
      leaves both degree-2 endpoints as forced terminals with min S = 2
      impossible (dist >= 2 check) -- consistency probes of the S machinery.

Usage:
  python3 atoms.py anchors
  python3 atoms.py run 6 7 8 9 10 11 12 13 14 15
  python3 atoms.py ring <graph6> <a> <b> <L>   # assemble and test a ring
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import pathlib
import platform
import subprocess
import sys
from collections import deque

HERE = pathlib.Path(__file__).resolve().parent
E005 = HERE.parent / "E005-markstrom-24-vertex-graphs-verification-and-reproduction"
DATA = HERE / "data"


def load(name: str, path: pathlib.Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


e005lib = load("e005lib", E005 / "e005lib.py")
sat = e005lib.load_e004()

POWERS = {4, 8, 16, 32, 64, 128, 256, 512, 1024}


def degrees(adjacency: list[int]) -> list[int]:
    return [row.bit_count() for row in adjacency]


def spectrum(adjacency: list[int]) -> list[int]:
    n = len(adjacency)
    return [
        length
        for length in range(3, n + 1)
        if sat.has_cycle_of_length(adjacency, length)
    ]


def power_free(adjacency: list[int]) -> bool:
    n = len(adjacency)
    for power in sorted(POWERS):
        if power > n:
            return True
        if sat.has_cycle_of_length(adjacency, power):
            return False
    return True


def bfs_distance(adjacency: list[int], a: int, b: int) -> int:
    seen = 1 << a
    frontier = [a]
    dist = 0
    while frontier:
        if any(v == b for v in frontier):
            return dist
        dist += 1
        nxt = []
        for v in frontier:
            free = adjacency[v] & ~seen
            while free:
                low = free & -free
                free ^= low
                nxt.append(low.bit_length() - 1)
                seen |= low
        frontier = nxt
    raise AssertionError("disconnected input to bfs_distance")


def path_lengths(adjacency: list[int], a: int, b: int) -> set[int]:
    """All lengths of simple a-b paths, by DFS over visited bitmasks."""
    lengths: set[int] = set()
    stack = [(a, 1 << a, 0)]
    while stack:
        vertex, visited, length = stack.pop()
        if vertex == b:
            lengths.add(length)
            continue
        free = adjacency[vertex] & ~visited
        while free:
            low = free & -free
            free ^= low
            stack.append((low.bit_length() - 1, visited | low, length + 1))
    assert lengths, "no a-b path: input not connected"
    assert min(lengths) == bfs_distance(adjacency, a, b), "DFS/BFS mismatch"
    return lengths


def build_ring(adjacency: list[int], a: int, b: int, copies: int) -> list[int]:
    """The A011 ring R_L: identify b of copy i with a of copy i+1 (mod L)."""
    n = len(adjacency)
    assert copies >= 3
    order = copies * (n - 1)
    keep = [v for v in range(n) if v != b]
    index = {v: i for i, v in enumerate(keep)}

    def vid(copy: int, v: int) -> int:
        if v == b:
            copy, v = (copy + 1) % copies, a
        return copy * (n - 1) + index[v]

    ring = [0] * order
    for copy in range(copies):
        for u in range(n):
            row = adjacency[u]
            while row:
                low = row & -row
                row ^= low
                v = low.bit_length() - 1
                if u < v:
                    x, y = vid(copy, u), vid(copy, v)
                    assert x != y
                    ring[x] |= 1 << y
                    ring[y] |= 1 << x
    return ring


def graph6_encode(adjacency: list[int]) -> str:
    n = len(adjacency)
    assert n <= 62
    bits = []
    for j in range(1, n):
        for i in range(j):
            bits.append(1 if adjacency[i] >> j & 1 else 0)
    while len(bits) % 6:
        bits.append(0)
    chars = [chr(63 + n)]
    for i in range(0, len(bits), 6):
        value = 0
        for bit in bits[i : i + 6]:
            value = value << 1 | bit
        chars.append(chr(63 + value))
    return "".join(chars)


K33_MINUS_E = None  # built in k33_minus_e()


def k33_minus_e() -> tuple[list[int], int, int]:
    """K_{3,3} minus one edge; terminals are the ex-endpoints (degree 2)."""
    parts = ([0, 1, 2], [3, 4, 5])
    adjacency = [0] * 6
    for u in parts[0]:
        for v in parts[1]:
            if (u, v) == (0, 3):
                continue
            adjacency[u] |= 1 << v
            adjacency[v] |= 1 << u
    return adjacency, 0, 3


def petersen() -> list[int]:
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 4), (4, 0),
        (5, 7), (7, 9), (9, 6), (6, 8), (8, 5),
        (0, 5), (1, 6), (2, 7), (3, 8), (4, 9),
    ]
    adjacency = [0] * 10
    for u, v in edges:
        adjacency[u] |= 1 << v
        adjacency[v] |= 1 << u
    return adjacency


def anchors() -> None:
    checks = 0

    def ok(condition: bool, message: str) -> None:
        nonlocal checks
        assert condition, message
        checks += 1

    # A1: cubic counts vs OEIS A002851.
    for n, expected in ((8, 5), (10, 19), (12, 85)):
        run = subprocess.run(
            ["geng", "-c", "-d3", "-D3", "-u", str(n)],
            capture_output=True, text=True,
        )
        count = int(run.stderr.split(">Z")[1].split()[0])
        ok(count == expected, f"A1: cubic count at {n}: {count} != {expected}")

    # A2: zero-sub-cubic restriction at n=14 reproduces C016's 6059 with no
    # {C4,C8}-free survivors.
    total = 0
    survivors = 0
    process = subprocess.Popen(
        ["geng", "-q", "-c", "-f", "-d3", "14"],
        stdout=subprocess.PIPE, text=True,
    )
    for line in process.stdout:
        line = line.strip()
        if not line:
            continue
        adjacency = e005lib.g6_decode(line)
        ok_row = all(d >= 3 for d in degrees(adjacency))
        assert ok_row and sat.codegree_c4_free(adjacency)
        total += 1
        if not sat.has_cycle_of_length(adjacency, 8):
            survivors += 1
    assert process.wait() == 0
    ok(total == 6059, f"A2: C4-free min-deg-3 class at 14 is {total} != 6059")
    ok(survivors == 0, "A2: unexpected {C4,C8}-free survivor at 14")

    # A3: K_{3,3}-e through-set and spectrum.
    adjacency, a, b = k33_minus_e()
    ok(path_lengths(adjacency, a, b) == {3, 5}, "A3: S(K33-e) != {3,5}")
    ok(spectrum(adjacency) == [4, 6], "A3: spectrum(K33-e) != {4,6}")

    # A4: Bondy-Vince Figure 1 ring spectrum (C024).
    ring = build_ring(adjacency, a, b, 3)
    ok(len(ring) == 15, "A4: ring order != 15")
    ok(all(d >= 3 for d in degrees(ring)), "A4: ring degree < 3")
    ok(
        spectrum(ring) == [4, 6, 9, 11, 13, 15],
        f"A4: ring spectrum {spectrum(ring)} != [4,6,9,11,13,15]",
    )

    # A5: Petersen probes.
    pet = petersen()
    ok(spectrum(pet) == [5, 6, 8, 9], "A5: Petersen spectrum wrong")
    minus = [row for row in pet]
    minus[0] &= ~(1 << 1)
    minus[1] &= ~(1 << 0)
    lengths = path_lengths(minus, 0, 1)
    ok(min(lengths) == bfs_distance(minus, 0, 1) >= 2, "A5: distance probe")

    print(f"anchors: all {checks} checks passed")


def classify(line: str, n: int) -> dict | None:
    """Full downstream filter for one geng graph; returns a finding or None."""
    adjacency = e005lib.g6_decode(line)
    assert len(adjacency) == n
    degs = degrees(adjacency)
    assert all(d >= 1 for d in degs), "geng -d1 violated"
    sub = [v for v in range(n) if degs[v] < 3]
    if len(sub) > 2:
        return None
    assert sat.codegree_c4_free(adjacency), "geng -f emitted a C4 graph"
    if sat.has_cycle_of_length(adjacency, 8):
        return None
    if n >= 16 and sat.has_cycle_of_length(adjacency, 16):
        return None
    # Power-free member of the class: every case is reportable.
    finding = {
        "graph6": line,
        "degrees_below_3": {str(v): degs[v] for v in sub},
        "spectrum": spectrum(adjacency),
    }
    if len(sub) == 0:
        finding["kind"] = "min-degree-3 counterexample (!!)"
        return finding
    if len(sub) == 1:
        finding["kind"] = "1-atom (!!)"
        return finding
    a, b = sub
    if degs[a] + degs[b] < 3:
        finding["kind"] = "excluded-(1,1)"
        return finding
    lengths = sorted(path_lengths(adjacency, a, b))
    ratio = max(lengths) / min(lengths)
    finding["terminals"] = [a, b]
    finding["S"] = lengths
    finding["ratio"] = ratio
    finding["kind"] = "2-ATOM (!!)" if ratio < 2 else "2-atom-candidate-ratio>=2"
    return finding


def run(orders: list[int]) -> None:
    DATA.mkdir(exist_ok=True)
    for n in orders:
        mine = -(-(3 * n - 4) // 2)
        command = ["geng", "-q", "-c", "-f", "-d1", str(n), f"{mine}:0"]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, text=True)
        total = 0
        in_class = 0
        findings: list[dict] = []
        for line in process.stdout:
            line = line.strip()
            if not line:
                continue
            total += 1
            adjacency = e005lib.g6_decode(line)
            degs = degrees(adjacency)
            if sum(1 for d in degs if d < 3) > 2:
                continue
            in_class += 1
            finding = classify(line, n)
            if finding is not None:
                findings.append(finding)
        assert process.wait() == 0
        alarms = [f for f in findings if "!!" in f["kind"]]
        summary = {
            "n": n,
            "geng_command": " ".join(command),
            "geng_stream_total": total,
            "at_most_two_subcubic": in_class,
            "power_free_findings": findings,
            "atoms_found": len(alarms),
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
        }
        path = DATA / f"atoms_n{n}.json"
        path.write_text(json.dumps(summary, indent=2))
        print(
            f"n={n}: stream={total} class={in_class} "
            f"power-free findings={len(findings)} ATOMS={len(alarms)}"
        )
        for f in findings:
            print(f"  {f['kind']}: {f['graph6']} "
                  f"S={f.get('S')} ratio={f.get('ratio')} "
                  f"spectrum={f['spectrum']}")


def profile(orders: list[int]) -> None:
    """Calibration: through-ratio distribution when power-freeness is NOT
    required.  Same stream, graphs with exactly two sub-cubic vertices and
    degree sum >= 3; reports how many have ratio < 2 and whether any of
    those are C8-free (they cannot be, through order 15, by `run`)."""
    DATA.mkdir(exist_ok=True)
    for n in orders:
        mine = -(-(3 * n - 4) // 2)
        command = ["geng", "-q", "-c", "-f", "-d1", str(n), f"{mine}:0"]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, text=True)
        examined = 0
        below2 = 0
        below2_c8free = 0
        min_ratio = None
        sample: list[dict] = []
        for line in process.stdout:
            line = line.strip()
            if not line:
                continue
            adjacency = e005lib.g6_decode(line)
            degs = degrees(adjacency)
            sub = [v for v in range(len(degs)) if degs[v] < 3]
            if len(sub) != 2 or degs[sub[0]] + degs[sub[1]] < 3:
                continue
            examined += 1
            lengths = path_lengths(adjacency, sub[0], sub[1])
            ratio = max(lengths) / min(lengths)
            if min_ratio is None or ratio < min_ratio:
                min_ratio = ratio
            if ratio < 2:
                below2 += 1
                c8free = not sat.has_cycle_of_length(adjacency, 8)
                if c8free:
                    below2_c8free += 1
                if len(sample) < 8:
                    sample.append(
                        {
                            "graph6": line,
                            "S": sorted(lengths),
                            "ratio": ratio,
                            "spectrum": spectrum(adjacency),
                        }
                    )
        assert process.wait() == 0
        summary = {
            "n": n,
            "two_subcubic_examined": examined,
            "ratio_below_2": below2,
            "ratio_below_2_and_c8_free": below2_c8free,
            "min_ratio": min_ratio,
            "sample_ratio_below_2": sample,
        }
        (DATA / f"profile_n{n}.json").write_text(json.dumps(summary, indent=2))
        print(
            f"n={n}: examined={examined} ratio<2: {below2} "
            f"(C8-free among them: {below2_c8free}) min_ratio={min_ratio}"
        )


def ring_command(graph6: str, a: int, b: int, copies: int) -> None:
    adjacency = e005lib.g6_decode(graph6)
    ring = build_ring(adjacency, a, b, copies)
    spec = spectrum(ring)
    print(f"ring order {len(ring)}, min degree {min(degrees(ring))}")
    print(f"spectrum: {spec}")
    print(f"graph6: {graph6_encode(ring)}")
    powers = sorted(p for p in POWERS if p <= len(ring))
    hit = [p for p in powers if p in spec]
    print(f"power lengths present: {hit or 'NONE'}")


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("anchors")
    runp = sub.add_parser("run")
    runp.add_argument("orders", nargs="+", type=int)
    profp = sub.add_parser("profile")
    profp.add_argument("orders", nargs="+", type=int)
    ringp = sub.add_parser("ring")
    ringp.add_argument("graph6")
    ringp.add_argument("a", type=int)
    ringp.add_argument("b", type=int)
    ringp.add_argument("copies", type=int)
    args = parser.parse_args()
    if args.command == "anchors":
        anchors()
    elif args.command == "run":
        run(args.orders)
    elif args.command == "profile":
        profile(args.orders)
    else:
        ring_command(args.graph6, args.a, args.b, args.copies)


if __name__ == "__main__":
    main()
