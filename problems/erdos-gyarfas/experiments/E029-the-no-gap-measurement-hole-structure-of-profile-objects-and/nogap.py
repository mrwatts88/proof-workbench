#!/usr/bin/env python3
"""E029 — the no-gap measurement.

Two questions, both answered from data already on disk; nothing is generated.

  (A) Do the recorded exactly-two-profile objects satisfy (INT), i.e. is
      S(H,a,b) an interval above 8?  Which hole values occur at all?
  (B) In the E027 near-miss corpus (9,061 vertex-taut gapped pairs, all with
      >= 4 degree-2 vertices), at what degree-2 count does the first hole of
      value >= 8 appear, and what is the minimum degree-2 count needed to open
      a hole at each value?

(A) recomputes S from the graph6 strings with the E019 primitives (exact path
enumeration).  (B) reads E027's stored per-row hole lists.

Usage:  pypy3 nogap.py anchors      # must pass before any production reading
        pypy3 nogap.py run          # writes data/nogap.json
"""

import sys, os, json

HERE = os.path.dirname(os.path.abspath(__file__))
EXP = os.path.dirname(HERE)
E019 = os.path.join(EXP, "E019-dedicated-c4-c8-free-generator-geng-prune-plugin-and-the-ord")
E022 = os.path.join(EXP, "E022-the-g-profile-ladder-at-orders-18-and-19-via-the-e019-genera")
E024 = os.path.join(EXP, "E024-the-g-profile-ladder-rung-at-order-21-via-the-e019-generator")
E027 = os.path.join(EXP, "E027-near-miss-corpus-dissection-dodge-mechanisms-s-shape-and-deg")
sys.path.insert(0, E019)
import scan  # noqa: E402  (E019 primitives: g6_decode, degrees, profile_pair,
             #                path_lengths, has_c4, from_edges, g6_encode)

# The order-19 first-ever profile member (C043) and the order-14 calibration
# object (A023/C042), both recorded in STATE.md.
N19_MEMBER = "R???C@?GC_B?@_aAA_aP?W_?BO@Gc?"
CALIB14 = "M?AA@?WcKWHOWOL??"

PETERSEN_EDGES = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0),
                  (5, 7), (7, 9), (9, 6), (6, 8), (8, 5),
                  (0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]


def analyse(adj, g6=None):
    """S, its holes, and every class condition re-derived from the graph."""
    deg = scan.degrees(adj)
    pair = scan.profile_pair(deg)
    assert pair is not None, ("not an exactly-two-degree-2 profile", g6)
    a, b = pair
    S = sorted(scan.path_lengths(adj, a, b))
    assert S, ("no a-b path", g6)
    s = set(S)
    lo, hi = S[0], S[-1]
    gaps = [x for x in range(lo, hi) if x not in s]
    return {
        "g6": g6, "n": len(adj), "edges": sum(deg) // 2, "terminals": [a, b],
        "lo": lo, "hi": hi, "gaps": gaps,
        "max_gap": max(gaps) if gaps else None,
        "int_ok": all(g < 8 for g in gaps),          # (INT): S contains [8, max S]
        "hamiltonian": hi == len(adj) - 1,
        "c4_free": not scan.has_c4(adj),
        "S": S,
    }


def petersen_minus_e():
    adj = scan.from_edges(10, PETERSEN_EDGES)
    adj[0] &= ~(1 << 1)
    adj[1] &= ~(1 << 0)
    return adj


def read_g6_column(path):
    out = []
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if line and not line.startswith("#"):
                out.append(line.split()[0])
    return out


def profile_objects():
    rows = []
    for g6 in read_g6_column(os.path.join(E024, "data",
                                          "profile_n21_mod144_merged.txt")):
        r = analyse(scan.g6_decode(g6), g6); r["source"] = "E024 n=21"; rows.append(r)
    for g6 in read_g6_column(os.path.join(E022, "data", "profile_n20_part14.g6")):
        r = analyse(scan.g6_decode(g6), g6); r["source"] = "E022 n=20 part14"; rows.append(r)
    r = analyse(scan.g6_decode(N19_MEMBER), N19_MEMBER)
    r["source"] = "C043 n=19"; rows.append(r)
    return rows


def corpus_frontier():
    path = os.path.join(E027, "data", "corpus_rows_compact.json")
    corpus = json.load(open(path))
    holes = {}
    for row in corpus:
        for g in row["gaps"]:
            cur = holes.get(g)
            holes[g] = row["ndeg2"] if cur is None else min(cur, row["ndeg2"])
    viol = [r for r in corpus if any(g >= 8 for g in r["gaps"])]
    by_ndeg2 = {}
    for r in corpus:
        by_ndeg2.setdefault(r["ndeg2"], [0, 0])
        by_ndeg2[r["ndeg2"]][0] += 1
    for r in viol:
        by_ndeg2[r["ndeg2"]][1] += 1
    return {
        "corpus_rows": len(corpus),
        "rows_with_hole_ge_8": len(viol),
        "min_ndeg2_per_hole_value": dict((str(k), v) for k, v in sorted(holes.items())),
        "rows_and_violations_by_ndeg2":
            dict((str(k), {"rows": v[0], "with_hole_ge_8": v[1]})
                 for k, v in sorted(by_ndeg2.items())),
        "min_ndeg2_with_hole_ge_8": min([r["ndeg2"] for r in viol]) if viol else None,
        "max_hole_value_anywhere": max([g for r in corpus for g in r["gaps"]] or [None]),
    }


def anchors():
    """Every check must reproduce an independently recorded quantity."""
    ok = []

    # a1 Petersen-e: C037 records S = {4,5,7,8}, spectrum {5,6,8,9}.
    r = analyse(petersen_minus_e())
    assert r["S"] == [4, 5, 7, 8], r["S"]
    assert r["gaps"] == [6] and r["int_ok"] and not r["hamiltonian"]
    assert r["c4_free"]
    ok.append("a1 Petersen-e S={4,5,7,8}, hole at 6 only, non-Hamiltonian")

    # a2 the order-14 calibration object: A025 T3 records its S gapped exactly
    #    at 6; A027's kill discipline records it Hamiltonian and exactly-two.
    r = analyse(scan.g6_decode(CALIB14), CALIB14)
    assert r["n"] == 14 and r["gaps"] == [6], (r["n"], r["gaps"])
    assert r["hamiltonian"]
    ok.append("a2 order-14 calibration object: n=14, hole at 6 only, Hamiltonian")

    # a3 the order-19 member: C043 records S = [5,18], C4-free.
    r = analyse(scan.g6_decode(N19_MEMBER), N19_MEMBER)
    assert r["n"] == 19 and r["lo"] == 5 and r["hi"] == 18 and r["gaps"] == []
    assert r["c4_free"]
    ok.append("a3 order-19 member: S = [5,18] exactly, no holes")

    # a4 the order-21 rung: C049 records 19 members, all with max S = 20, and
    #    exactly one with 6 not in S, that one having d(a,b) = 4.
    rows = [x for x in profile_objects() if x["source"] == "E024 n=21"]
    assert len(rows) == 19, len(rows)
    assert all(x["hamiltonian"] and x["hi"] == 20 for x in rows)
    gapped6 = [x for x in rows if 6 in x["gaps"]]
    assert len(gapped6) == 1, len(gapped6)
    assert gapped6[0]["lo"] == 4, gapped6[0]["lo"]
    ok.append("a4 order-21 rung: 19 members, all max S = 20, exactly one with "
              "6 not in S and that one has min S = 4")

    # a5 the E027 corpus size: C047 records 9,061 rows.
    assert corpus_frontier()["corpus_rows"] == 9061
    ok.append("a5 E027 corpus = 9,061 rows")

    # a6 graph6 round-trip on every object read.
    for x in profile_objects():
        assert scan.g6_encode(scan.g6_decode(x["g6"])) == x["g6"], x["g6"]
    ok.append("a6 graph6 round-trip on every profile object")

    return ok


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "anchors"
    for line in anchors():
        print("PASS " + line)
    if mode == "anchors":
        print("anchors: all passed")
        return
    assert mode == "run", mode
    rows = profile_objects()
    holes = sorted(set([g for r in rows for g in r["gaps"]]))
    out = {
        "interpreter": sys.version.split()[0],
        "pypy": hasattr(sys, "pypy_version_info"),
        "profile_objects": {
            "checked": len(rows),
            "int_violations": sum(0 if r["int_ok"] else 1 for r in rows),
            "hamiltonian": sum(1 for r in rows if r["hamiltonian"]),
            "c4_free": sum(1 for r in rows if r["c4_free"]),
            "hole_values_occurring": holes,
            "gapped": [{"source": r["source"], "n": r["n"], "lo": r["lo"],
                        "hi": r["hi"], "gaps": r["gaps"], "g6": r["g6"]}
                       for r in rows if r["gaps"]],
        },
        "corpus": corpus_frontier(),
        "rows": rows,
    }
    if not os.path.isdir(os.path.join(HERE, "data")):
        os.makedirs(os.path.join(HERE, "data"))
    with open(os.path.join(HERE, "data", "nogap.json"), "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    p = out["profile_objects"]
    print("profile objects checked      : %d" % p["checked"])
    print("  (INT) violations           : %d" % p["int_violations"])
    print("  Hamiltonian / C4-free      : %d / %d" % (p["hamiltonian"], p["c4_free"]))
    print("  hole values occurring      : %s" % p["hole_values_occurring"])
    c = out["corpus"]
    print("corpus rows                  : %d" % c["corpus_rows"])
    print("  rows with a hole >= 8      : %d" % c["rows_with_hole_ge_8"])
    print("  min ndeg2 with a hole >= 8 : %s" % c["min_ndeg2_with_hole_ge_8"])
    print("  min ndeg2 per hole value   : %s" % c["min_ndeg2_per_hole_value"])
    print("  max hole value anywhere    : %s" % c["max_hole_value_anywhere"])


if __name__ == "__main__":
    main()
