"""Part 1 of E005: verify the House of Graphs "Markstroem Graph" (id 51419).

Input: hog51419.json, the graph page downloaded verbatim from
https://houseofgraphs.org/api/graphs/51419 on 2026-07-23.

Checks performed on the adjacencyList graph:
  1. order 24, cubic, connected;
  2. no C4 and no C8 (independent codegree test plus the E004 whole-graph
     detector), girth and full cycle spectrum for lengths 3..24;
  3. contains C16 (so it is not a counterexample to C001);
  4. the JSON's canonicalForm graph6 string denotes the same graph up to
     isomorphism (checked with nauty labelg when available);
  5. planarity (checked with nauty planarg when available);
  6. L008 saturation profile: for every nonedge uv, which Mersenne path
     lengths (3, 7, 15) occur between u and v — equivalently whether adding
     uv would create a C4, C8, or C16.  At order 24 a C32 is impossible, so
     the graph is edge-maximal power-cycle-free iff every nonedge has such
     a witness.

Deterministic, exact, standard library only (nauty tools via subprocess).
"""

from __future__ import annotations

import json
import pathlib
import platform
import shutil
import subprocess

import e005lib

HERE = pathlib.Path(__file__).resolve().parent
WITNESS_LENGTHS = (3, 7, 15)  # 2^k - 1 for cycles C4, C8, C16 (C32 > 24)


def adjacency_from_json(path: pathlib.Path) -> tuple[list[int], str]:
    payload = json.loads(path.read_text())
    lists = payload["adjacencyList"]
    n = len(lists)
    adjacency = [0] * n
    for u, row in enumerate(lists):
        for v in row:
            adjacency[u] |= 1 << v
    # the JSON must be symmetric and loop-free
    for u in range(n):
        assert not adjacency[u] & (1 << u), "loop in HoG data"
        for v in range(n):
            if adjacency[u] & (1 << v):
                assert adjacency[v] & (1 << u), "asymmetric HoG data"
    matrix = payload["adjacencyMatrix"]
    for u in range(n):
        for v in range(n):
            assert matrix[u][v] == bool(adjacency[u] & (1 << v)), (
                "adjacencyMatrix and adjacencyList disagree"
            )
    return adjacency, payload["entity"]["canonicalForm"]


def canonical(g6: str) -> str:
    result = subprocess.run(
        ["labelg", "-q"], input=g6 + "\n", capture_output=True, text=True
    )
    assert result.returncode == 0, result.stderr
    return result.stdout.strip()


def is_planar(g6: str) -> bool:
    # planarg copies exactly the planar inputs to stdout; nonplanar inputs
    # produce no output.  (Do NOT pass -p: it emits a >>planar_code<<
    # header unconditionally, which a nonemptiness test misreads.)
    result = subprocess.run(
        ["planarg", "-q"], input=g6 + "\n", capture_output=True, text=True
    )
    assert result.returncode == 0, result.stderr
    return result.stdout.strip() != ""


def main() -> None:
    sat = e005lib.load_e004()
    e005lib.self_check()

    adjacency, hog_canonical_form = adjacency_from_json(HERE / "hog51419.json")
    n = len(adjacency)
    print(f"Python {platform.python_version()}")
    print(f"order={n} degrees_cubic={set(e005lib.degrees(adjacency)) == {3}}")
    assert n == 24
    assert set(e005lib.degrees(adjacency)) == {3}
    assert sat.is_connected(adjacency)
    print("connected=True")

    assert sat.codegree_c4_free(adjacency), "C4 found by codegree test"
    spectrum = [
        length
        for length in range(3, n + 1)
        if sat.has_cycle_of_length(adjacency, length)
    ]
    print(f"cycle_spectrum={spectrum}")
    assert 4 not in spectrum and 8 not in spectrum, "power cycle C4/C8 present"
    assert 16 in spectrum, "expected a C16 (graph would otherwise refute C001)"
    girth = spectrum[0]
    print(f"girth={girth} no_C4=True no_C8=True has_C16=True")
    print(f"bipartite={sat.is_bipartite(adjacency)}")

    ours = e005lib.g6_encode(adjacency)
    if shutil.which("labelg"):
        same = canonical(ours) == canonical(hog_canonical_form)
        print(f"isomorphic_to_hog_canonicalForm={same}")
        assert same, "adjacencyList and canonicalForm graphs differ"
    else:
        print("labelg not available; skipped canonical comparison")

    if shutil.which("planarg"):
        print(f"planar={is_planar(ours)}")
    else:
        print("planarg not available; skipped planarity")

    # L008 saturation profile over all nonedges.
    missing = e005lib.nonedges(adjacency)
    profile = {3: 0, 7: 0, 15: 0}
    unwitnessed: list[tuple[int, int]] = []
    for u, v in missing:
        found = [
            length
            for length in WITNESS_LENGTHS
            if sat.has_uv_path_of_length(adjacency, u, v, length)
        ]
        for length in found:
            profile[length] += 1
        if not found:
            unwitnessed.append((u, v))
    print(
        f"nonedges={len(missing)} with_path3={profile[3]} "
        f"with_path7={profile[7]} with_path15={profile[15]}"
    )
    print(f"nonedges_without_any_witness={len(unwitnessed)}")
    saturated = not unwitnessed
    print(f"edge_maximal_power_cycle_free={saturated}")
    if unwitnessed and len(unwitnessed) <= 40:
        print(f"unwitnessed_pairs={unwitnessed}")


if __name__ == "__main__":
    main()
