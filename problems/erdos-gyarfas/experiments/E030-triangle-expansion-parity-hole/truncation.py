from collections import deque
def petersen():
    E=set()
    for i in range(5):
        E.add(frozenset((i,(i+1)%5))); E.add(frozenset((i,i+5))); E.add(frozenset((i+5,(i+2)%5+5)))
    return 10,E
def adj(N,E):
    a={v:set() for v in range(N)}
    for e in E:
        u,v=tuple(e); a[u].add(v); a[v].add(u)
    return a
def truncate(N,E):
    """replace every vertex by a triangle; vertex v -> (v,k) for its k-th nbr"""
    a=adj(N,E); idx={}; c=0
    for v in range(N):
        for w in sorted(a[v]):
            idx[(v,w)]=c; c+=1
    F=set()
    for v in range(N):
        nb=sorted(a[v])
        for i in range(len(nb)):
            for j in range(i+1,len(nb)):
                F.add(frozenset((idx[(v,nb[i])],idx[(v,nb[j])])))   # triangle
    for e in E:
        u,v=tuple(e); F.add(frozenset((idx[(u,v)],idx[(v,u)])))     # link edge
    return c,F,idx
def spectrum(N,E,L):
    a=adj(N,E); found=set()
    for s in range(N):
        def dfs(u,seen,ln):
            for w in a[u]:
                if w==s and ln>=2: found.add(ln+1)
                elif w not in seen and w>s and ln+1<L:
                    seen.add(w); dfs(w,seen,ln+1); seen.remove(w)
        dfs(s,{s},0)
    return found
def connected_after(N,E,rem):
    a=adj(N,E); st=next(v for v in range(N) if v not in rem)
    seen={st}; q=deque([st])
    while q:
        u=q.popleft()
        for w in a[u]:
            if w not in rem and w not in seen: seen.add(w); q.append(w)
    return len(seen)==N-len(rem)
def kconn(N,E,k):
    from itertools import combinations
    for r in range(1,k):
        for cut in combinations(range(N),r):
            if not connected_after(N,E,set(cut)): return False,cut
    return True,None
def through(N,E,s,t):
    a=adj(N,E); res=set()
    def dfs(u,seen,ln):
        if u==t: res.add(ln); return
        for w in a[u]:
            if w not in seen:
                seen.add(w); dfs(w,seen,ln+1); seen.remove(w)
    dfs(s,{s},0); return res

n,E=petersen()
N,F,idx=truncate(n,E)
print("truncated Petersen: order=%d edges=%d"%(N,len(F)))
print("  cubic:", set(len(s) for s in adj(N,F).values())=={3})
sp=sorted(spectrum(N,F,13))
print("  cycle lengths <13:",sp)
print("  C4-free:",4 not in sp,"  C8-free:",8 not in sp)
ok,cut=kconn(N,F,3); print("  3-connected:",ok,cut)
# delete a LINK edge
a_,b_=idx[(0,1)],idx[(1,0)]
H=set(F); H.remove(frozenset((a_,b_)))
dg=sorted(len(s) for s in adj(N,H).values())
print("H = trunc(P) - link edge: deg-2 count=%d min deg=%d"%(dg.count(2),dg[0]))
ok2,cut2=kconn(N,H,2); print("  2-connected (=> vertex-taut):",ok2,cut2)
S=through(N,H,a_,b_)
print("  S = [%d..%d], interval? %s"%(min(S),max(S),set(range(min(S),max(S)+1))==S))
print("  min S =",min(S),"   8 in S ?",8 in S,"   14 in S ?",14 in S)
print("  => (INT) refuted at order %d (8 <= max S, 8 not in S): %s"%(N, 8 not in S and max(S)>=8))
