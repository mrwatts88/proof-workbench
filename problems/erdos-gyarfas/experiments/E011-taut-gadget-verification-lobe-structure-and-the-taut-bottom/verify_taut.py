"""E011: computational verification for A012 (T2 lobe structure, T3 taut
bottom rungs, T1 scaffold constructions).

Everything here is implemented independently of E004/E005/E010 (own graph6
decoder, own C4/cycle detectors, own path machinery), so agreement with the
recorded E010 profile counts anchors both pipelines at once.

Checks:

  T3 prediction (the theorem, tested on real graphs): every connected
  C4-free graph with exactly two sub-cubic vertices a, b (degree sum >= 3,
  taken as terminals -- a (D)-gadget) whose through-set satisfies S = {1} or
  2 in S subseteq {2,3} must be NON-taut (some vertex on no simple a-b
  path).  One taut example would refute A012 T3.

  T2 prediction: in every non-taut gadget of the class, each connected
  component K of the inessential vertices has exactly one essential
  neighbor c (the lobe attachment), all edges at K stay inside K + {c},
  and every vertex of K has degree >= 3.  One component with two essential
  neighbors would refute the lobe decomposition.

  Taut pinched survey: the taut gadgets with ratio < 2 are collected
  verbatim -- by T3 they must all have s_min >= 3; they are the concrete
  target shapes for the next rung (taut s_min = 3).

Anchors:

  A1  K_{3,3}-e: taut, S = {3,5}, spectrum {4,6}  (A011/E010 gadget).
  A2  T1(i) scaffold, Petersen stand-ins: two disjoint Petersen graphs
      joined by a bridge (terminals its endpoints): S = {1}, essential set
      exactly the two terminals, two lobes with single attachments,
      spectrum {5,6,8,9} (the union; the bridge lies on no cycle).
  A3  T1(ii) scaffold, Petersen stand-ins: two disjoint Petersen graphs
      G, G' plus new vertices a, w, b and edges aw, wb, a-x (x in G),
      w-y (y in G'): S = {2}, essential set exactly {a,w,b}, two lobes
      (V(G) at a, V(G') at w), spectrum {5,6,8,9}, degrees a=2 b=1 w=3.
      Petersen is NOT power-free (8 in its spectrum): the anchor validates
      the graph-theoretic claims of the T1 constructions (through-set,
      essential set, spectrum confinement, degree profile); power-freeness
      in T1 itself comes from the hypothetical counterexample ingredient.
  A4  stream/profile counts at n = 12, 13 reproduce the E010 records:
      stream 52,331 / 389,734; examined 1,690 / 16,106; ratio<2 22 / 116;
      C8-free among ratio<2: 0 / 0.

Usage:
  python3 verify_taut.py anchors
  python3 verify_taut.py run 12 13
"""

from __future__ import annotations

import argparse
import json
import pathlib
import platform
import subprocess

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE / "data"

EXPECTED = {  # E010 recorded profile numbers (README + data/profile_n*.json)
    12: {"stream": 52331, "examined": 1690, "below2": 22, "below2_c8free": 0},
    13: {"stream": 389734, "examined": 16106, "below2": 116, "below2_c8free": 0},
}


# --- graph machinery (independent implementations) -------------------------

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


def has_cycle_len(adjacency: list[int], length: int) -> bool:
    """Cycle of exactly `length`: DFS from each root over larger-index
    vertices only (each cycle is found at its minimum vertex)."""
    assert length >= 3
    n = len(adjacency)
    for root in range(n):
        allowed = ~((1 << (root + 1)) - 1)  # vertices > root
        stack = [(root, 1 << root, 0)]
        while stack:
            vertex, visited, dist = stack.pop()
            if dist == length - 1:
                if adjacency[vertex] >> root & 1:
                    return True
                continue
            free = adjacency[vertex] & allowed & ~visited
            while free:
                low = free & -free
                free ^= low
                stack.append((low.bit_length() - 1, visited | low, dist + 1))
    return False


def spectrum(adjacency: list[int]) -> list[int]:
    n = len(adjacency)
    return [L for L in range(3, n + 1) if has_cycle_len(adjacency, L)]


def bfs_dist(adjacency: list[int], a: int, b: int) -> int:
    seen = 1 << a
    frontier = [a]
    dist = 0
    while frontier:
        if b in frontier:
            return dist
        dist += 1
        nxt = []
        for v in frontier:
            free = adjacency[v] & ~seen
            while free:
                low = free & -free
                free ^= low
                seen |= low
                nxt.append(low.bit_length() - 1)
        frontier = nxt
    raise AssertionError("disconnected input")


def paths_and_essential(adjacency: list[int], a: int, b: int) -> tuple[set[int], int]:
    """(through-set S, bitmask of essential vertices) by DFS over all
    simple a-b paths; min S is cross-checked against BFS distance."""
    lengths: set[int] = set()
    essential = 0
    stack = [(a, 1 << a, 0)]
    while stack:
        vertex, visited, dist = stack.pop()
        if vertex == b:
            lengths.add(dist)
            essential |= visited
            continue
        free = adjacency[vertex] & ~visited
        while free:
            low = free & -free
            free ^= low
            stack.append((low.bit_length() - 1, visited | low, dist + 1))
    assert lengths, "disconnected input"
    assert min(lengths) == bfs_dist(adjacency, a, b), "DFS/BFS mismatch"
    return lengths, essential


def lobe_components(adjacency: list[int], essential: int) -> list[tuple[int, list[int]]]:
    """Components of the inessential vertices, each with its list of
    essential neighbors (T2 predicts exactly one per component)."""
    n = len(adjacency)
    rest = ((1 << n) - 1) & ~essential
    out = []
    while rest:
        seed = rest & -rest
        comp = seed
        frontier = seed
        while frontier:
            grow = 0
            f = frontier
            while f:
                low = f & -f
                f ^= low
                grow |= adjacency[low.bit_length() - 1]
            grow &= rest & ~comp
            comp |= grow
            frontier = grow
        rest &= ~comp
        attach = 0
        c = comp
        while c:
            low = c & -c
            c ^= low
            attach |= adjacency[low.bit_length() - 1] & essential
        out.append((comp, [v for v in range(n) if attach >> v & 1]))
    return out


# --- fixed graphs -----------------------------------------------------------

def k33_minus_e() -> tuple[list[int], int, int]:
    adjacency = [0] * 6
    for u in (0, 1, 2):
        for v in (3, 4, 5):
            if (u, v) == (0, 3):
                continue
            adjacency[u] |= 1 << v
            adjacency[v] |= 1 << u
    return adjacency, 0, 3


def petersen(offset: int, size: int) -> list[tuple[int, int]]:
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 4), (4, 0),
        (5, 7), (7, 9), (9, 6), (6, 8), (8, 5),
        (0, 5), (1, 6), (2, 7), (3, 8), (4, 9),
    ]
    return [(u + offset, v + offset) for u, v in edges]


def from_edges(n: int, edges: list[tuple[int, int]]) -> list[int]:
    adjacency = [0] * n
    for u, v in edges:
        assert u != v and not adjacency[u] >> v & 1
        adjacency[u] |= 1 << v
        adjacency[v] |= 1 << u
    return adjacency


# --- anchors ----------------------------------------------------------------

def anchors() -> None:
    checks = 0

    def ok(condition: bool, message: str) -> None:
        nonlocal checks
        assert condition, message
        checks += 1

    # A1: K_{3,3}-e is taut with S={3,5}, spectrum {4,6}.
    adj, a, b = k33_minus_e()
    S, ess = paths_and_essential(adj, a, b)
    ok(S == {3, 5}, "A1: S(K33-e) != {3,5}")
    ok(ess == (1 << 6) - 1, "A1: K33-e not taut")
    ok(spectrum(adj) == [4, 6], "A1: spectrum(K33-e) != {4,6}")

    # A2: T1(i) scaffold -- two Petersens + bridge, terminals its endpoints.
    edges = petersen(0, 10) + petersen(10, 10) + [(0, 10)]
    adj = from_edges(20, edges)
    a, b = 0, 10
    S, ess = paths_and_essential(adj, a, b)
    ok(S == {1}, "A2: bridge scaffold S != {1}")
    ok(ess == (1 << a) | (1 << b), "A2: essential set != terminals")
    lobes = lobe_components(adj, ess)
    ok(len(lobes) == 2, "A2: expected two lobes")
    ok(all(len(att) == 1 for _, att in lobes), "A2: multi-attachment lobe")
    ok(spectrum(adj) == [5, 6, 8, 9], "A2: spectrum != Petersen union")
    degs = degrees(adj)
    ok(degs[a] == 4 and degs[b] == 4, "A2: terminal degrees != 4")
    ok(all(degs[v] >= 3 for v in range(20) if v not in (a, b)),
       "A2: non-terminal degree < 3")

    # A3: T1(ii) scaffold -- two Petersens + a,w,b; edges aw, wb, a-x, w-y.
    a, w, b = 20, 21, 22
    x, y = 0, 10
    edges = petersen(0, 10) + petersen(10, 10) + [(a, w), (w, b), (a, x), (w, y)]
    adj = from_edges(23, edges)
    S, ess = paths_and_essential(adj, a, b)
    ok(S == {2}, "A3: scaffold S != {2}")
    ok(ess == (1 << a) | (1 << w) | (1 << b), "A3: essential set != {a,w,b}")
    lobes = lobe_components(adj, ess)
    ok(len(lobes) == 2, "A3: expected two lobes")
    attachments = sorted(att[0] for _, att in lobes if len(att) == 1)
    ok(attachments == [a, w], "A3: lobe attachments != {a, w}")
    ok(spectrum(adj) == [5, 6, 8, 9], "A3: spectrum != Petersen union")
    degs = degrees(adj)
    ok((degs[a], degs[b], degs[w]) == (2, 1, 3), "A3: a,b,w degrees wrong")
    ok(all(degs[v] >= 3 for v in range(23) if v not in (a, b)),
       "A3: non-terminal degree < 3")

    print(f"anchors: all {checks} checks passed")


# --- the stream check -------------------------------------------------------

def run(orders: list[int]) -> None:
    DATA.mkdir(exist_ok=True)
    for n in orders:
        mine = -(-(3 * n - 4) // 2)
        command = ["geng", "-q", "-c", "-f", "-d1", str(n), f"{mine}:0"]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, text=True)
        stream = 0
        examined = 0
        below2 = 0
        below2_c8free = 0
        t3_class = 0
        t3_taut_violations: list[str] = []
        nontaut = 0
        lobes_checked = 0
        lobe_violations: list[str] = []
        taut_pinched: list[dict] = []
        for line in process.stdout:
            line = line.strip()
            if not line:
                continue
            stream += 1
            adjacency = g6_decode(line)
            assert len(adjacency) == n
            degs = degrees(adjacency)
            sub = [v for v in range(n) if degs[v] < 3]
            if len(sub) != 2 or degs[sub[0]] + degs[sub[1]] < 3:
                continue
            assert not has_c4(adjacency), "geng -f emitted a C4 graph"
            examined += 1
            a, b = sub
            S, ess = paths_and_essential(adjacency, a, b)
            assert ess >> a & 1 and ess >> b & 1
            taut = ess == (1 << n) - 1

            # T2 check on every non-taut gadget.
            if not taut:
                nontaut += 1
                for comp, attach in lobe_components(adjacency, ess):
                    lobes_checked += 1
                    good = len(attach) == 1 and all(
                        degs[v] >= 3
                        for v in range(n)
                        if comp >> v & 1
                    )
                    if not good:
                        lobe_violations.append(line)

            # T3 check: S={1} or 2 in S subseteq {2,3} forces non-taut.
            if S == {1} or (2 in S and S <= {2, 3}):
                t3_class += 1
                if taut:
                    t3_taut_violations.append(line)

            ratio = max(S) / min(S)
            if ratio < 2:
                below2 += 1
                if not has_cycle_len(adjacency, 8):
                    below2_c8free += 1
                if taut:
                    taut_pinched.append(
                        {
                            "graph6": line,
                            "terminals": [a, b],
                            "S": sorted(S),
                            "ratio": ratio,
                            "spectrum": spectrum(adjacency),
                        }
                    )
        assert process.wait() == 0

        expected = EXPECTED.get(n)
        if expected is not None:
            assert stream == expected["stream"], (n, stream)
            assert examined == expected["examined"], (n, examined)
            assert below2 == expected["below2"], (n, below2)
            assert below2_c8free == expected["below2_c8free"]

        for entry in taut_pinched:
            assert min(entry["S"]) >= 3, f"T3 refuted at {entry['graph6']}"
        assert not t3_taut_violations, f"T3 refuted: {t3_taut_violations[:3]}"
        assert not lobe_violations, f"T2 refuted: {lobe_violations[:3]}"

        summary = {
            "n": n,
            "geng_command": " ".join(command),
            "stream_total": stream,
            "examined_two_subcubic_sum3": examined,
            "ratio_below_2": below2,
            "ratio_below_2_and_c8_free": below2_c8free,
            "t3_class_size_S1_or_2in_S23": t3_class,
            "t3_taut_violations": t3_taut_violations,
            "nontaut_gadgets": nontaut,
            "lobe_components_checked": lobes_checked,
            "lobe_violations": lobe_violations,
            "taut_pinched": taut_pinched,
            "e010_counts_reproduced": expected is not None,
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
        }
        (DATA / f"taut_n{n}.json").write_text(json.dumps(summary, indent=2))
        print(
            f"n={n}: stream={stream} examined={examined} "
            f"t3-class={t3_class} (taut violations: {len(t3_taut_violations)}) "
            f"nontaut={nontaut} lobes={lobes_checked} "
            f"(violations: {len(lobe_violations)}) "
            f"ratio<2: {below2} taut-pinched: {len(taut_pinched)}"
        )
        for entry in taut_pinched:
            print(
                f"  taut pinched: {entry['graph6']} S={entry['S']} "
                f"spectrum={entry['spectrum']}"
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
