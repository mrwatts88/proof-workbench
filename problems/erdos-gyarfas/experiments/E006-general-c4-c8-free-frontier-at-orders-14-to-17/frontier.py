"""E006: exhaust the general {C4,C8}-free frontier at orders 14-17.

Class searched at each order n: connected graphs, minimum degree >= 3, no
C4 (geng's -f plus an independent codegree re-test on every graph), no C8
(the E004 whole-graph detector).  Survivors at n >= 16 are additionally
tested for C16.

Logical reading (written out in attempt A007): a minimum-order
counterexample to C001 is connected, so if no connected counterexample of
any order <= N exists, no counterexample of order <= N exists at all.  For
n <= 15 a connected counterexample is exactly a connected {C4,C8}-free
graph of minimum degree >= 3; for 16 <= n <= 31 it is exactly such a graph
with no C16 either.  Emptiness at orders 14-16 therefore proves that every
counterexample has at least 17 vertices; emptiness at 17 lifts this to 18.

Generation is delegated to nauty's geng (version recorded at run time),
validated here by the anchors below; everything downstream of geng is
checked twice (codegree C4 re-test; C8/C16 by the E004 detector, whose own
anchors are in E004 and e005lib).

Anchors (subcommand `anchors`):
  A1  geng connected cubic counts at n = 8, 10, 12, 14 equal OEIS A002851
      (5, 19, 85, 509).
  A2  cross-validation against the independent E004 search: the pipeline
      at orders 11, 12, 13 finds C4-free min-degree-3 classes of sizes
      geng reports, and zero {C4,C8}-free graphs, matching E004's stronger
      labelled result (C011/L017).
  A3  rejection control: the order-10 C4-free cubic class (contains the
      Petersen graph) is wiped out by the C8 filter, matching E002.
  A4  positive control for the C16 test: the Markstroem graph (E005,
      verified) contains a C16; E004's l016_graph(4) does not.
  A5  geng's -f (4-cycle-free) semantics: total squarefree graph counts at
      n = 5..8 equal OEIS A006786 (18, 44, 117, 351; entry fetched
      2026-07-23).

Usage:
  python3 frontier.py anchors
  python3 frontier.py run 14 15 16      # writes data/, prints census lines
  python3 frontier.py run 17 --parts 24 --workers 8
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import multiprocessing
import pathlib
import platform
import shutil
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
E005 = HERE.parent / "E005-markstrom-24-vertex-graphs-verification-and-reproduction"
DATA = HERE / "data"
WITNESS_LENGTHS = (3, 7, 15)


def load(name: str, path: pathlib.Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


e005lib = load("e005lib", E005 / "e005lib.py")
sat = e005lib.load_e004()


def geng_command(n: int, part: int | None, parts: int | None) -> list[str]:
    command = ["geng", "-q", "-c", "-f", "-d3", str(n)]
    if part is not None:
        command.append(f"{part}/{parts}")
    return command


def filter_stream(arguments: tuple[int, int | None, int | None]) -> dict:
    """Run one geng (part) and filter its stream; return exact counts."""
    n, part, parts = arguments
    process = subprocess.Popen(
        geng_command(n, part, parts), stdout=subprocess.PIPE, text=True
    )
    total = 0
    survivors: list[str] = []
    for line in process.stdout:
        line = line.strip()
        if not line:
            continue
        total += 1
        adjacency = e005lib.g6_decode(line)
        assert len(adjacency) == n
        assert all(row.bit_count() >= 3 for row in adjacency), "degree < 3"
        assert sat.codegree_c4_free(adjacency), "geng -f emitted a C4 graph"
        if not sat.has_cycle_of_length(adjacency, 8):
            survivors.append(line)
    code = process.wait()
    if code != 0:
        raise RuntimeError(f"geng exited {code} for n={n} part={part}")
    return {"n": n, "part": part, "total": total, "survivors": survivors}


def analyse_survivor(line: str) -> dict:
    adjacency = e005lib.g6_decode(line)
    n = len(adjacency)
    spectrum = [
        length
        for length in range(3, n + 1)
        if sat.has_cycle_of_length(adjacency, length)
    ]
    planar = None
    if shutil.which("planarg"):
        # planarg copies exactly the planar inputs to stdout; no -p (its
        # >>planar_code<< header appears even for nonplanar input)
        run = subprocess.run(
            ["planarg", "-q"], input=line + "\n",
            capture_output=True, text=True,
        )
        planar = run.stdout.strip() != "" if run.returncode == 0 else None
    profile = {3: 0, 7: 0, 15: 0}
    unwitnessed = 0
    for u, v in e005lib.nonedges(adjacency):
        found = [
            length
            for length in WITNESS_LENGTHS
            if sat.has_uv_path_of_length(adjacency, u, v, length)
        ]
        for length in found:
            profile[length] += 1
        if not found:
            unwitnessed += 1
    return {
        "g6": line,
        "order": n,
        "degrees": sorted(e005lib.degrees(adjacency), reverse=True),
        "spectrum": spectrum,
        "has_C16": 16 in spectrum,
        "planar": planar,
        "bipartite": sat.is_bipartite(adjacency),
        "witness_counts": profile,
        "unwitnessed_nonedges": unwitnessed,
        "counterexample": not any(
            length in spectrum for length in (4, 8, 16, 32)
        ),
    }


def run_order(n: int, parts: int | None, workers: int) -> None:
    DATA.mkdir(exist_ok=True)
    if parts is None:
        results = [filter_stream((n, None, None))]
    else:
        with multiprocessing.Pool(workers) as pool:
            results = pool.map(
                filter_stream, [(n, part, parts) for part in range(parts)]
            )
    total = sum(r["total"] for r in results)
    survivors = sorted(line for r in results for line in r["survivors"])
    (DATA / f"survivors_n{n}.g6").write_text(
        "".join(line + "\n" for line in survivors)
    )
    print(
        f"n={n}: c4_free_min_deg3_connected={total} "
        f"c4c8_free={len(survivors)}",
        flush=True,
    )
    analyses = [analyse_survivor(line) for line in survivors]
    (DATA / f"survivors_n{n}.json").write_text(json.dumps(analyses, indent=1))
    counterexamples = [a for a in analyses if a["counterexample"]]
    for analysis in analyses:
        print(
            f"  survivor g6={analysis['g6']} degrees={analysis['degrees']} "
            f"spectrum={analysis['spectrum']} planar={analysis['planar']} "
            f"counterexample={analysis['counterexample']}"
        )
    print(
        f"n={n}: counterexamples_to_C001={len(counterexamples)}", flush=True
    )


def run_anchors() -> None:
    e005lib.self_check()
    for n, expected in ((8, 5), (10, 19), (12, 85), (14, 509)):
        run = subprocess.run(
            ["geng", "-u", "-c", "-d3", "-D3", str(n)],
            capture_output=True, text=True,
        )
        count = -1
        for token in run.stderr.split():
            if token.isdigit():
                count = int(token)
                break
        assert count == expected, f"A1 fail n={n}: {count} != {expected}"
        print(f"A1 geng n={n} connected cubic = {count} (A002851 {expected})")
    for n in (11, 12, 13):
        result = filter_stream((n, None, None))
        print(
            f"A2 n={n}: c4_free_min_deg3={result['total']} "
            f"c4c8_free={len(result['survivors'])} (E004: 0)"
        )
        assert not result["survivors"], f"A2 fail: survivor at n={n}"
    cubic10 = subprocess.run(
        ["geng", "-q", "-c", "-f", "-d3", "-D3", "10", "15"],
        capture_output=True, text=True,
    )
    lines = [line for line in cubic10.stdout.split() if line]
    kept = [
        line
        for line in lines
        if not sat.has_cycle_of_length(e005lib.g6_decode(line), 8)
    ]
    assert lines and not kept
    print(f"A3 order-10 C4-free cubic class: {len(lines)} graphs, all have C8")
    hog = json.loads((E005 / "hog51419.json").read_text())
    markstrom = [0] * 24
    for u, row in enumerate(hog["adjacencyList"]):
        for v in row:
            markstrom[u] |= 1 << v
    assert sat.has_cycle_of_length(markstrom, 16)
    assert not sat.has_cycle_of_length(sat.l016_graph(4), 16)
    print("A4 C16 detector: Markstroem yes, l016_graph(4) no")
    for n, expected in ((5, 18), (6, 44), (7, 117), (8, 351)):
        run = subprocess.run(
            ["geng", "-u", "-f", str(n)], capture_output=True, text=True
        )
        count = -1
        for token in run.stderr.split():
            if token.isdigit():
                count = int(token)
                break
        assert count == expected, f"A5 fail n={n}: {count} != {expected}"
        print(f"A5 geng -f n={n} squarefree graphs = {count} (A006786 {expected})")
    print("anchors passed")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["anchors", "run"])
    parser.add_argument("orders", nargs="*", type=int)
    parser.add_argument("--parts", type=int, default=None)
    parser.add_argument("--workers", type=int, default=8)
    arguments = parser.parse_args()
    print(f"Python {platform.python_version()} on {platform.platform()}")
    geng_path = shutil.which("geng")
    print(f"geng={geng_path}")
    if arguments.mode == "anchors":
        run_anchors()
        return
    for n in arguments.orders:
        assert 4 <= n <= 31, "C32 handling not implemented"
        run_order(n, arguments.parts, arguments.workers)


if __name__ == "__main__":
    main()
