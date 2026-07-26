"""E030 - mechanism check for A029 T2 (the triangle expansion parity hole).

Builds a bipartite cubic 3-connected graph of girth 6 and large diameter as a
cyclic Haar graph H(n;{0,1,b}), triangle-expands one vertex, deletes an edge
on a shortest cycle far from the triangle, and verifies every structural
assertion of A029 T2 (i)-(v) directly.

Scope: this instance has girth 6, so it is NOT {C4,C8}-free and is NOT a class
member.  What is verified is the MECHANISM - the connectivity argument, the
cycle-spectrum containment, the k in {0,1,2} parity bookkeeping, and the
"even lengths cost 2*rho" bound.  Class membership needs girth >= 10, which is
the X004 import.
"""
import sys
from collections import deque
from itertools import combinations

def haar(n, b):
    """Cyclic Haar graph H(n;{0,1,b}): parts u_0..u_{n-1}, w_0..w_{n-1}."""
    E = set()
    for i in range(n):
        for s in (0, 1, b):
            E.add(frozenset((i, n + (i + s) % n)))
    return 2 * n, E

def adj(N, E):
    a = {v: set() for v in range(N)}
    for e in E:
        u, v = tuple(e)
        a[u].add(v); a[v].add(u)
    return a

def bfs(a, s):
    d = {s: 0}; q = deque([s])
    while q:
        u = q.popleft()
        for w in a[u]:
            if w not in d:
                d[w] = d[u] + 1; q.append(w)
    return d

def girth(N, E):
    a = adj(N, E); best = 10 ** 9
    for s in range(N):
        d = {s: 0}; par = {s: None}; q = deque([s])
        while q:
            u = q.popleft()
            for w in a[u]:
                if w not in d:
                    d[w] = d[u] + 1; par[w] = u; q.append(w)
                elif w != par[u]:
                    best = min(best, d[u] + d[w] + 1)
    return best

def diameter(N, E):
    a = adj(N, E)
    return max(max(bfs(a, s).values()) for s in range(N))

def connected_after(N, E, removed):
    a = adj(N, E)
    start = next(v for v in range(N) if v not in removed)
    seen = {start}; q = deque([start])
    while q:
        u = q.popleft()
        for w in a[u]:
            if w not in removed and w not in seen:
                seen.add(w); q.append(w)
    return len(seen) == N - len(removed)

def is_k_connected(N, E, k):
    """Brute force: no vertex set of size < k separates."""
    for r in range(1, k):
        for cut in combinations(range(N), r):
            if not connected_after(N, E, set(cut)):
                return False, cut
    return True, None

def expand_triangle(N, E, v):
    """Replace v by a triangle.  v itself is reused as the first triangle
    vertex and keeps its first neighbour; N and N+1 are new and take the
    other two.  So the vertex set is 0..N+1 with no isolated leftover."""
    a = adj(N, E)
    nb = sorted(a[v])
    assert len(nb) == 3
    F = set(e for e in E if v not in e)
    T = [v, N, N + 1]
    for i in range(3):
        F.add(frozenset((T[i], nb[i])))
    for i in range(3):
        F.add(frozenset((T[i], T[(i + 1) % 3])))
    return N + 2, F, T

def paths_up_to(N, E, s, t, maxlen, T):
    """All (length, #triangle-edges-used) pairs for s-t paths of length<=maxlen."""
    a = adj(N, E); a2 = adj(N, E)
    dt = bfs(a2, t)
    Tset = set(T)
    tri_edges = {frozenset((T[i], T[(i + 1) % 3])) for i in range(3)}
    out = set()
    def dfs(u, seen, ln, k):
        if u == t:
            out.add((ln, k)); return
        if ln >= maxlen: return
        for w in a[u]:
            if w in seen: continue
            if ln + 1 + dt.get(w, 10 ** 9) > maxlen: continue
            kk = k + (1 if frozenset((u, w)) in tri_edges else 0)
            seen.add(w); dfs(w, seen, ln + 1, kk); seen.remove(w)
    dfs(s, {s}, 0, 0)
    return out

def spectrum_upto(N, E, L):
    """All cycle lengths <= L, by DFS from each vertex (small L only)."""
    a = adj(N, E); found = set()
    for s in range(N):
        def dfs(u, seen, ln):
            for w in a[u]:
                if w == s and ln >= 2:
                    found.add(ln + 1)
                elif w not in seen and w > s and ln + 1 < L:
                    seen.add(w); dfs(w, seen, ln + 1); seen.remove(w)
        dfs(s, {s}, 0)
    return found

def main():
    n, b = 52, 5
    N, E = haar(n, b)
    g = girth(N, E); D = diameter(N, E)
    print("base H(%d;{0,1,%d}): N=%d edges=%d girth=%d diameter=%d" % (n, b, N, len(E), g, D))
    degs = set(len(s) for s in adj(N, E).values())
    print("  cubic:", degs == {3}, " bipartite:", all(len(e & set(range(n))) == 1 for e in E))
    assert degs == {3} and g == 6
    ok3, cut = is_k_connected(N, E, 3)
    print("  3-connected (brute force over cuts of size 1,2):", ok3, cut)
    assert ok3
    # need diameter >= g to place v; Moore bound says N > 1+3(2^(g-1)-1) forces it
    print("  Moore threshold for diameter>=%d is order > %d; order is %d" % (g, 1 + 3 * (2 ** (g - 1) - 1), N))
    print("  diameter >= g ?", D >= g)
    assert D >= g

    a = adj(N, E)
    # pick edge ab on a shortest cycle: any edge is (girth 6, edge-transitive-ish); verify
    ab = (0, n)
    assert frozenset(ab) in E
    Eab = set(E); Eab.remove(frozenset(ab))
    dab = bfs(adj(N, Eab), ab[0])[ab[1]]
    print("  chosen edge %s: shortest cycle through it has length %d (= girth %d ?) %s"
          % (str(ab), dab + 1, g, dab + 1 == g))
    assert dab + 1 == g
    # pick v at distance >= g from {a,b}
    da, db = bfs(a, ab[0]), bfs(a, ab[1])
    cands = [x for x in range(N) if x not in ab and min(da[x], db[x]) >= g]
    print("  vertices at distance >= %d from {a,b}: %d" % (g, len(cands)))
    assert cands
    v = cands[0]
    rho_base = min(da[v], db[v])
    print("  chosen v=%d at distance %d" % (v, rho_base))

    M, F1, T = expand_triangle(N, E, v)
    print("F1 = triangle expansion at v: order=%d edges=%d" % (M, len(F1)))
    print("  cubic:", set(len(s) for s in adj(M, F1).values()) == {3})
    ok3b, cutb = is_k_connected(M, F1, 3)
    print("  (i) F1 3-connected:", ok3b, cutb)
    assert ok3b
    spec = spectrum_upto(M, F1, g)
    print("  (ii) cycle lengths < %d present: %s  (expect {3} only)" % (g, sorted(spec - {g})))
    assert spec - {g} == {3}

    H = set(F1); H.remove(frozenset(ab))
    dg = sorted(len(s) for s in adj(M, H).values())
    print("H = F1 - ab: order=%d  degree-2 count=%d  min degree=%d" % (M, dg.count(2), dg[0]))
    assert dg.count(2) == 2 and dg[0] == 2 and dg[2] == 3
    ok2, cut2 = is_k_connected(M, H, 2)
    print("  H 2-connected (hence vertex-taut):", ok2, cut2)
    assert ok2

    aH = adj(M, H)
    dTa = min(bfs(aH, ab[0])[x] for x in T)
    dTb = min(bfs(aH, ab[1])[x] for x in T)
    rho = min(dTa, dTb)
    print("  rho = d({a,b},T) in H = %d   (2*rho = %d)" % (rho, 2 * rho))

    maxlen = 2 * rho + 2
    pairs = paths_up_to(M, H, ab[0], ab[1], maxlen, T)
    lens = sorted(set(l for l, k in pairs))
    print("  through-lengths <= %d : %s" % (maxlen, lens))
    print("  (iii) min S = %d ; g-1 = %d ; equal? %s ; odd? %s"
          % (min(lens), g - 1, min(lens) == g - 1, min(lens) % 2 == 1))
    assert min(lens) == g - 1 and min(lens) % 2 == 1
    bad = [(l, k) for l, k in pairs if (l % 2 == 0) != (k == 1)]
    print("  (iv) parity law  'even <=> exactly one triangle edge'  violations: %d" % len(bad))
    assert not bad
    evens = sorted(l for l in lens if l % 2 == 0)
    print("  (iv) smallest even through-length = %s ; 2*rho = %d ; >= ? %s"
          % (evens[0] if evens else None, 2 * rho, (evens[0] >= 2 * rho) if evens else True))
    assert all(l >= 2 * rho for l in evens)
    holes = [h for h in range(min(lens) + 1, maxlen + 1) if h not in lens]
    print("  (v) HOLE at min S + 1 = %d ? %s" % (min(lens) + 1, (min(lens) + 1) not in lens))
    print("  (v) all missing values in (min S, %d] : %s" % (maxlen, holes))
    assert (min(lens) + 1) not in lens
    # T2 claims exactly this: every EVEN value in [g, 2*rho) is absent.
    claimed = [h for h in range(g, 2 * rho) if h % 2 == 0]
    print("  (v) T2's claimed even holes in [g, 2*rho) = %s ; all absent? %s"
          % (claimed, all(h not in lens for h in claimed)))
    assert all(h not in lens for h in claimed)
    extra_odd = [h for h in holes if h % 2 == 1]
    print("  (v) EXTRA odd holes not claimed by T2 (harmless, recorded): %s" % extra_odd)
    print("\nALL ASSERTIONS PASSED")

main()
