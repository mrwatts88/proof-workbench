"""Part 2 of E005: reproduce Markström's order-24 census internally.

Target claims (Markström 2004, Section 4 and Table 3): the smallest cubic
graphs with no C4 and no C8 have 24 vertices, there are exactly four of
them, and exactly one of the four is planar.

Method: nauty's geng generates every connected 4-cycle-free cubic graph on
n vertices (`geng -c -f -d3 -D3 n m`, m = 3n/2); a Python filter keeps the
graphs with no 8-cycle, re-testing C4-freeness independently on every graph
with the E004 codegree criterion.  Disconnected cubic {C4,C8}-free graphs
on <= 24 vertices cannot exist once all orders <= 22 are empty, because a
smallest component would itself be a connected cubic {C4,C8}-free graph on
<= 12 vertices, so the connected census settles the class.

Subcommands:
  anchors            geng sanity counts against OEIS A002851 (connected
                     cubic graphs: 5, 19, 85, 509 at n = 8, 10, 12, 14)
                     plus a rejection control: the Petersen graph (the only
                     C4-free connected cubic graph of order 10 with girth
                     >= 5 ... generated here as the full order-10 C4-free
                     class) must be rejected by the C8 filter.
  generate n         run geng into data/n<order>/parts/ (parallel res/mod
                     splitting for n >= 22)
  filter n           filter the parts, verify survivors, write
                     data/survivors_n<order>.g6 and print the census line
  all                anchors, then generate+filter for even n = 14..24

Deterministic and exact; the only nondeterminism is process scheduling,
which affects file ordering only (survivors are sorted before use).
"""

from __future__ import annotations

import argparse
import multiprocessing
import pathlib
import platform
import shutil
import subprocess
import sys
import time

import e005lib

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE / "data"
GENG_PARTS = {22: 24, 24: 120}   # res/mod splitting for the two big orders
WORKERS = 10
WITNESS_LENGTHS = (3, 7, 15)


def geng_command(n: int, part: int | None, parts: int | None) -> list[str]:
    command = ["geng", "-q", "-c", "-f", "-d3", "-D3", str(n), f"{3 * n // 2}"]
    if part is not None:
        command.append(f"{part}/{parts}")
    return command


def run_generate(n: int) -> None:
    parts_dir = DATA / f"n{n}" / "parts"
    parts_dir.mkdir(parents=True, exist_ok=True)
    parts = GENG_PARTS.get(n)
    if parts is None:
        out = parts_dir / "part_all.g6"
        with out.open("w") as handle:
            subprocess.run(geng_command(n, None, None), stdout=handle, check=True)
        print(f"n={n}: generated single part")
        return
    jobs = []
    for part in range(parts):
        out = parts_dir / f"part_{part:03d}.g6"
        if out.exists() and (parts_dir / f"part_{part:03d}.done").exists():
            continue
        jobs.append((part, out))
    running: list[tuple[int, pathlib.Path, subprocess.Popen, object]] = []
    while jobs or running:
        while jobs and len(running) < WORKERS:
            part, out = jobs.pop(0)
            handle = out.open("w")
            process = subprocess.Popen(
                geng_command(n, part, parts), stdout=handle
            )
            running.append((part, out, process, handle))
        finished = [entry for entry in running if entry[2].poll() is not None]
        if not finished:
            time.sleep(1)
            continue
        for entry in finished:
            part, out, process, handle = entry
            running.remove(entry)
            handle.close()
            if process.returncode != 0:
                raise RuntimeError(
                    f"geng part {part} failed with {process.returncode}"
                )
            (out.parent / f"part_{part:03d}.done").touch()
            print(f"n={n}: part {part}/{parts} done", flush=True)


def filter_part(path: pathlib.Path) -> tuple[int, int, list[str]]:
    sat = e005lib.load_e004()
    total = 0
    c4_failures = 0
    survivors: list[str] = []
    with path.open() as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            adjacency = e005lib.g6_decode(line)
            total += 1
            if not sat.codegree_c4_free(adjacency):
                c4_failures += 1
                continue
            if not sat.has_cycle_of_length(adjacency, 8):
                survivors.append(line)
    return total, c4_failures, survivors


def run_filter(n: int) -> None:
    sat = e005lib.load_e004()
    parts_dir = DATA / f"n{n}" / "parts"
    part_files = sorted(parts_dir.glob("part_*.g6"))
    assert part_files, f"no parts generated for n={n}"
    expected_parts = GENG_PARTS.get(n, 1)
    assert len(part_files) == expected_parts, (
        f"n={n}: found {len(part_files)} parts, expected {expected_parts}"
    )
    for part in part_files:
        done = part.with_suffix(".done")
        assert expected_parts == 1 or done.exists(), f"incomplete part {part}"

    if len(part_files) > 1:
        with multiprocessing.Pool(WORKERS) as pool:
            results = pool.map(filter_part, part_files)
    else:
        results = [filter_part(part_files[0])]
    total = sum(r[0] for r in results)
    c4_failures = sum(r[1] for r in results)
    survivors = sorted(line for r in results for line in r[2])
    assert c4_failures == 0, (
        f"geng -f emitted {c4_failures} graphs with a C4; assumptions violated"
    )

    out = DATA / f"survivors_n{n}.g6"
    out.write_text("".join(line + "\n" for line in survivors))
    print(
        f"n={n}: c4_free_cubic_connected={total} "
        f"c4c8_free={len(survivors)}",
        flush=True,
    )

    for index, line in enumerate(survivors):
        adjacency = e005lib.g6_decode(line)
        assert set(e005lib.degrees(adjacency)) == {3}
        assert sat.is_connected(adjacency)
        assert sat.codegree_c4_free(adjacency)
        assert not sat.has_cycle_of_length(adjacency, 4)
        assert not sat.has_cycle_of_length(adjacency, 8)
        spectrum = [
            length
            for length in range(3, len(adjacency) + 1)
            if sat.has_cycle_of_length(adjacency, length)
        ]
        planar = None
        if shutil.which("planarg"):
            # planarg copies exactly the planar inputs to stdout; no -p
            # (its >>planar_code<< header appears even for nonplanar input)
            run = subprocess.run(
                ["planarg", "-q"],
                input=line + "\n",
                capture_output=True,
                text=True,
            )
            assert run.returncode == 0, run.stderr
            planar = run.stdout.strip() != ""
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
        print(f"survivor[{index}] g6={line}")
        print(f"  spectrum={spectrum}")
        print(
            f"  planar={planar} bipartite={sat.is_bipartite(adjacency)} "
            f"witness3={profile[3]} witness7={profile[7]} "
            f"witness15={profile[15]} unwitnessed_nonedges={unwitnessed}"
        )


def run_anchors() -> None:
    sat = e005lib.load_e004()
    e005lib.self_check()
    # OEIS A002851: connected cubic graphs on 8, 10, 12, 14 vertices.
    for n, expected in ((8, 5), (10, 19), (12, 85), (14, 509)):
        run = subprocess.run(
            ["geng", "-u", "-c", "-d3", "-D3", str(n)],
            capture_output=True,
            text=True,
        )
        # geng -u reports ">Z <count> graphs generated ..." on stderr
        count = -1
        for token in run.stderr.split():
            if token.isdigit():
                count = int(token)
                break
        assert count == expected, f"geng cubic count n={n}: {count} != {expected}"
        print(f"anchor geng n={n} connected cubic = {count} (A002851: {expected})")
    # Rejection control: every connected C4-free cubic graph of order 10
    # contains a C8 (E002 proved this for the labelled class), so the filter
    # must reject the entire order-10 class, which includes Petersen.
    run = subprocess.run(
        ["geng", "-q", "-c", "-f", "-d3", "-D3", "10", "15"],
        capture_output=True,
        text=True,
    )
    lines = [line for line in run.stdout.split() if line]
    kept = 0
    for line in lines:
        adjacency = e005lib.g6_decode(line)
        if not sat.has_cycle_of_length(adjacency, 8):
            kept += 1
    print(
        f"anchor n=10 C4-free cubic class: {len(lines)} graphs, "
        f"{kept} pass the no-C8 filter (E002: 0 expected)"
    )
    assert kept == 0
    # Positive control against over-rejection of C8-free graphs: K4 has no
    # C8 and must pass; the 3-cube (bipartite, girth 4) fails only the C4
    # test, and its C8 detection must fire (it is Hamiltonian on 8 vertices).
    k4 = e005lib.g6_decode("C~")
    assert not sat.has_cycle_of_length(k4, 8)
    cube = sat.cube_graph()
    assert sat.has_cycle_of_length(cube, 8)
    print("anchor controls: K4 passes no-C8; cube's C8 detected")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["anchors", "generate", "filter", "all"])
    parser.add_argument("order", nargs="?", type=int)
    arguments = parser.parse_args()
    print(f"Python {platform.python_version()} on {platform.platform()}")
    if arguments.mode == "anchors":
        run_anchors()
    elif arguments.mode == "generate":
        run_generate(arguments.order)
    elif arguments.mode == "filter":
        run_filter(arguments.order)
    else:
        run_anchors()
        for n in (14, 16, 18, 20, 22, 24):
            run_generate(n)
            run_filter(n)


if __name__ == "__main__":
    main()
