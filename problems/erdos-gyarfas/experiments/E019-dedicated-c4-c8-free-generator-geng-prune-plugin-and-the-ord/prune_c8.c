/* prune_c8.c -- nauty geng plugin: incremental 8-cycle rejection.
 *
 * E019 (problem P-002, obligation G014 item 6).  Compiled into geng as
 *
 *     cc ... -DPREPRUNE=prune_c8 -DSUMMARY=summary_c8 geng.c prune_c8.c ...
 *
 * giving a dedicated {C4,C8}-free generator: geng's own -f switch removes
 * 4-cycles natively, and this plugin removes 8-cycles at every level of
 * geng's canonical construction path.
 *
 * COMPLETENESS.  geng.c (nauty 2.9.3), "PRUNE feature", lines 180-187:
 *
 *     "geng constructs the graph starting with vertex 0, then adding
 *      vertices 1,2,3,... in that order.  Each graph in the sequence is an
 *      induced subgraph of all later graphs in the sequence."
 *
 * PREPRUNE(gx,k,maxn) is called on every candidate extension gx of order k
 * (geng.c accept1 line 1748, accept1b line 1851, accept2 line 1979), and gx
 * is discarded, together with its whole subtree, when the value returned is
 * nonzero.  Containing an 8-cycle is a monotone property of subgraphs, so if
 * a target graph G of order maxn is C8-free then every graph in its
 * construction sequence -- each an induced subgraph of G -- is C8-free and
 * is therefore never rejected here.  Hence the output is exactly geng's
 * usual isomorph-free class intersected with "no C8", generated once each.
 *
 * INCREMENTALITY.  Whenever this procedure is called on a graph of order k,
 * the induced subgraph on {0,...,k-2} has already passed (it is the parent
 * in the construction path), so it is C8-free.  Every 8-cycle of the current
 * graph therefore runs through the newest vertex k-1.  We test exactly that:
 * an 8-cycle through a vertex v is v-a-*-*-*-*-b-v with a,b distinct
 * neighbours of v and a simple a-b path of six edges avoiding v.
 *
 * The test is exact and deterministic: no heuristics, no randomness, no
 * floating point.  Its output is cross-validated against the independent
 * "geng -f | has_cycle_len(.,8)" pipeline in scan.py (anchors A1-A6).
 *
 * Vertex relabelling.  nauty stores vertex j of g[i] in bit WORDSIZE-1-j
 * (most significant bit first).  We use  nb[k] = g[n-1-k] >> (WORDSIZE-n),
 * i.e. the relabelling phi(x) = n-1-x, which puts the newest vertex n-1 at
 * index 0 and gives least-significant-bit-first masks.  phi is a graph
 * isomorphism, so cycle existence is unchanged; the only thing it buys is
 * that the vertex to test is always index 0.
 */

#include "gtools.h"

#include <stdlib.h>

typedef unsigned long long c8mask;

#define C8_MAXV 64

static c8mask nbrm[C8_MAXV];   /* adjacency of the relabelled graph */
static int dist0[C8_MAXV];     /* distance in G-0 to the nearest neighbour of 0 */
static c8mask targetm;         /* admissible closing endpoints */

/* Per-level counters.  A "call" is one candidate extension offered to the
   plugin (a labelled extension, before geng's canonicity test), so these are
   node counts of the *labelled* search tree, not isomorphism-class counts. */
static unsigned long long c8_calls[C8_MAXV + 1];
static unsigned long long c8_rejects[C8_MAXV + 1];

#define LOWBIT(x) ((x) & (~(x) + 1ULL))
#define BITNO(x) (__builtin_ctzll(x))

static int
walk6(int v, c8mask used, int depth)
/* At vertex v having used `depth` edges of a would-be six-edge a-b path.
   Return 1 iff the path can be completed to a target vertex. */
{
    c8mask row, low;
    int rem, w;

    row = nbrm[v] & ~used;
    if (depth == 5) return (row & targetm) != 0ULL;

    rem = 5 - depth;   /* edges still available after stepping to w */
    while (row)
    {
        low = LOWBIT(row);
        row ^= low;
        w = BITNO(low);
        if (dist0[w] <= rem && walk6(w, used | low, depth + 1)) return 1;
    }
    return 0;
}

int
prune_c8(graph *g, int n, int maxn)
/* Nonzero iff the newest vertex of g lies on an 8-cycle. */
{
    int i, d, a, sh;
    c8mask n0, seen, frontier, nxt, row, low;

    if (n > C8_MAXV)
    {
        fprintf(stderr, ">E prune_c8: n=%d exceeds %d\n", n, C8_MAXV);
        exit(1);
    }
    ++c8_calls[n];
    if (n < 8) return FALSE;

    sh = WORDSIZE - n;
    for (i = 0; i < n; ++i) nbrm[n - 1 - i] = (c8mask)(g[i] >> sh);

    n0 = nbrm[0];
    if (__builtin_popcountll(n0) < 2) return FALSE;

    /* multi-source BFS in G-0 from N(0): dist0[w] = distance to N(0) */
    for (i = 0; i < n; ++i) dist0[i] = 99;
    row = n0;
    while (row) { low = LOWBIT(row); row ^= low; dist0[BITNO(low)] = 0; }
    seen = n0 | 1ULL;               /* vertex 0 is never entered */
    frontier = n0;
    d = 0;
    while (frontier && d < 5)
    {
        ++d;
        nxt = 0;
        row = frontier;
        while (row) { low = LOWBIT(row); row ^= low; nxt |= nbrm[BITNO(low)]; }
        nxt &= ~seen;
        seen |= nxt;
        row = nxt;
        while (row) { low = LOWBIT(row); row ^= low; dist0[BITNO(low)] = d; }
        frontier = nxt;
    }

    /* each unordered pair {a,b} of neighbours of 0 exactly once */
    row = n0;
    while (row)
    {
        low = LOWBIT(row);
        a = BITNO(low);
        row ^= low;
        if (!row) break;
        targetm = row;              /* the neighbours of 0 above a */
        if (walk6(a, 1ULL | low, 0)) { ++c8_rejects[n]; return TRUE; }
    }
    return FALSE;
}

void
summary_c8(nauty_counter nout, double cpu)
{
    int k;
    unsigned long long tc = 0, tr = 0;

    for (k = 0; k <= C8_MAXV; ++k) { tc += c8_calls[k]; tr += c8_rejects[k]; }
    fprintf(stderr, ">C prune_c8 calls=%llu rejects=%llu out=" COUNTER_FMT
            " cpu=%.2f\n", tc, tr, nout, cpu);
    for (k = 1; k <= C8_MAXV; ++k)
        if (c8_calls[k])
            fprintf(stderr, ">L level=%d calls=%llu rejects=%llu\n",
                    k, c8_calls[k], c8_rejects[k]);
}
