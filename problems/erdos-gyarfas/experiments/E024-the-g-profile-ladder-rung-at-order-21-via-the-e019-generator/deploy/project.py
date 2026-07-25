#!/usr/bin/env python3
"""Turn the order-19 modulus sweep into a production choice for order 21.

Model, straight from geng.c: a part walks the whole search tree down to the
split level (n-4) before it can tell which subtrees are its own, then does
1/mod of the work below.  So

    total_cpu(mod) = mod * A + B

with A the work above the split level (paid once PER PART) and B the work
below it (shared).  Two measured moduli determine A and B.

Consequences that drive the decision:
  * cost is proportional to total_cpu(mod), so widening is NOT free;
  * you cannot use more workers than parts, so mod >= workers;
  * with mod == workers every part runs in one wave and the wall clock is the
    LARGEST part, not the mean.

Order-21 numbers are the order-19 ones scaled by the recorded rung-to-rung
growth (E022: order 19 -> 20 is x6.61 in cpu-seconds); the 20 -> 21 factor is
swept over a range because it is not yet known.

A Railway service on the Pro plan is capped at 24 vCPU (the 1,000 vCPU service
ceiling divided by the 42-replica maximum), while os.cpu_count() inside the
container reports the host's 48.  The sweep was run with more workers than that
quota, so each part's recorded `seconds` is WALL time under contention and
overstates its CPU cost by (workers / 24).  Pass that ratio as the second
argument to correct it; ratios between moduli are unaffected, absolute
core-hours are.

Usage:  python3 project.py <calib_n19.json> [oversubscription_factor]
"""
import json
import sys

PRICE_PER_VCPU_HOUR = 20.0 / 730.0          # $20 / vCPU-month
VCPU_PER_SERVICE = 24


def main():
    with open(sys.argv[1]) as fh:
        rows = json.load(fh)["rows"]
    over = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0
    if over != 1.0:
        print("correcting for %.2fx oversubscription (workers > 24 vCPU quota)"
              % over)
    rows.sort(key=lambda r: r["modulus"])
    for r in rows:
        r["cpu_seconds"] = r["cpu_seconds"] / over
        r["max_part_seconds"] = r["max_part_seconds"] / over
        print("measured: order %d mod %4d -> cpu %9.1fs  max part %8.1fs  "
              "wall %8.1fs  generated %d"
              % (r["order"], r["modulus"], r["cpu_seconds"],
                 r["max_part_seconds"], r["wall_seconds"], r["generated"]))

    if len(rows) < 2:
        print("need at least two moduli to fit the model")
        return 1

    lo, hi = rows[0], rows[-1]
    A = (hi["cpu_seconds"] - lo["cpu_seconds"]) / float(
        hi["modulus"] - lo["modulus"])
    B = lo["cpu_seconds"] - lo["modulus"] * A
    print("\nfit at order %d:  total_cpu(mod) = mod * %.1fs + %.1fs" %
          (lo["order"], A, B))
    print("  per-part upper-tree cost A = %.1f s" % A)
    print("  shared lower-tree cost  B = %.1f s (%.2f core-hours)"
          % (B, B / 3600.0))
    for r in rows:
        pred = r["modulus"] * A + B
        print("  check mod %4d: predicted %9.1fs vs measured %9.1fs (%+.1f%%)"
              % (r["modulus"], pred, r["cpu_seconds"],
                 100.0 * (pred - r["cpu_seconds"]) / r["cpu_seconds"]))

    # how skewed are the parts?  max_part / (cpu/mod)
    print("\npart-size skew (max / mean):")
    skews = []
    for r in rows:
        mean = r["cpu_seconds"] / r["modulus"]
        skews.append(r["max_part_seconds"] / mean)
        print("  mod %4d: mean %7.1fs, max %8.1fs -> skew x%.2f"
              % (r["modulus"], mean, r["max_part_seconds"], skews[-1]))
    skew = max(skews)

    print("\norder-21 projection (one wave: mod == workers, %d vCPU/service), "
          "skew x%.2f" % (VCPU_PER_SERVICE, skew))
    print("%-8s %-7s %-5s %12s %10s %10s" %
          ("growth", "mod=W", "svcs", "total core-h", "wall (h)", "cost $"))
    for growth in (6.0, 6.6, 8.0):
        scale = 6.61 * growth              # order 19 -> 20 -> 21
        A21, B21 = A * scale, B * scale
        for mod in (24, 48, 72, 96, 144, 192, 240):
            total = (mod * A21 + B21) / 3600.0
            wall = (total / mod) * skew
            svcs = (mod + VCPU_PER_SERVICE - 1) // VCPU_PER_SERVICE
            print("%-8.1f %-7d %-5d %12.1f %10.2f %10.2f"
                  % (growth, mod, svcs, total, wall,
                     total * PRICE_PER_VCPU_HOUR))
        print("")
    print("Read the middle block (growth x6.6) as the central case; the outer "
          "two bound it.\nPick the smallest wall you are willing to pay for -- "
          "cost rises with mod, wall falls.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
