# Source audit — MathOverflow question 512914 (partial; thread body unread)

- Date: 2026-07-24 (session `S021`)
- URL (user-supplied):
  <https://mathoverflow.net/questions/512914/has-it-been-verified-exhaustively-that-every-minimum-degree-3-graph-on-at-most-1>
- Access status: **the thread body has not been read.** Direct fetch of
  `mathoverflow.net` and of `api.stackexchange.com` is blocked in this
  harness, and the browser extension was not connected during the session.
  Everything below rests on one answer quoted verbatim by the user in-session
  plus internal cross-checks. Upgrading this audit requires reading the full
  thread (especially the **question body**, whose claimed "reduction" is the
  load-bearing step of the quoted answer).

## The user-supplied quote (verbatim)

> Done, following your reduction: there are 510,489 cubic graphs on 20
> vertices (matching A002851, so the enumeration is complete), of which
> 36,101 are C4-free and none are also C8-free. Hence there is no cubic — and
> therefore no minimum-degree-3 — C4,C8-free graph on 20 vertices, settling
> n=20. (geng -c -d3 -D3 20, filtered; C4/C8 detection cross-checked against
> an independent routine, 0 disagreements.) Thank you.

## Audit verdict, itemized

1. **"510,489 cubic graphs on 20 vertices" — corroborated.** A002851
   (connected cubic graphs) gives 510,489 at order 20. Stage A of
   `E019/followup_s021.py` recounts this with stock geng
   (`-c -d3 -D3 20 30:30`).
2. **"36,101 are C4-free" — pending internal recount** (same stage A run,
   `-c -f -d3 -D3`). Recorded at reported strength until the count lands.
3. **"none are also C8-free" (no {C4,C8}-free cubic graph on 20 vertices) —
   internally corroborated, independently.** `E019`'s cubic probe (the
   PREPRUNE generator, a different instrument from the answerer's
   filter-the-stream pipeline) found the {C4,C8}-free cubic class empty at
   orders 14–22 and of size 4 at order 24 (matching Markström's Table 3 and
   `E005`). This import and the internal computation agree at order 20.
4. **"and therefore no minimum-degree-3 C4,C8-free graph on 20 vertices" —
   NOT SUPPORTED as quoted.** The inference from cubic emptiness to
   minimum-degree-3 emptiness at a fixed order is exactly the **cubic
   reduction**, which is this dossier's open proof-side deliverable (`G015`),
   currently proved only modulo case (5b) and only for the power-free
   (all powers of two) notion, not for the {C4,C8}-free-at-fixed-order class.
   No reduction of the quoted shape is in the dossier's verified stock:
   deleting an edge at a degree-≥4 vertex creates a degree-2 vertex (leaves
   the class), and suppressing a degree-2 vertex can create new 4-cycles.
   If the MO **question** contains a correct proof of a reduction that the
   answer "followed", this item upgrades on reading it; until then the
   min-degree-3 statement at order 20 is treated as **unestablished by this
   source**.
5. Independent of item 4's validity, stage B of `E019/followup_s021.py`
   (launched as the S021 close-of-session background follow-up) decides the
   min-degree-3 question at order 20 **internally and unconditionally** with
   the `E019` generator; its harvest belongs to the next session.

## Import rows

| item | statement | strength here |
|---|---|---|
| MO-1 | connected cubic count at order 20 is 510,489 (A002851) | **corroborated exactly** (stage A recount, stock geng: 510,489) |
| MO-2 | 36,101 of them are C4-free | **corroborated exactly** (stage A recount, stock geng `-f`: 36,101) |
| MO-3 | no {C4,C8}-free cubic graph on 20 vertices | reported and independently corroborated by `E019` (probe cubic, order 20 = 0) |
| MO-4 | no {C4,C8}-free min-degree-3 graph on 20 vertices | the *inference* in the quote remains **not usable** (unread claimed reduction; its general form is the open `G015`) — but the *statement* is now **established internally without it**: stage B of the harvest (`followup_s021.json`) finds the class empty at order 20 by direct generation, 16/16 parts. `C040`/`L047` carry it; nothing rests on this thread |

**Harvest note (same day):** stage A reproduced MO-1 and MO-2 exactly, so
the answerer's raw computation is fully corroborated; only the quoted
cubic→min-degree-3 inference stays rejected. Reading the thread body
(the question's claimed "reduction", other answers) remains the named
follow-up for `G014` item (7), now of purely archival interest for this
order since stage B superseded the conclusion.

Nothing from this thread may support a proof step beyond the strengths above.
The thread should be re-read in full (question body, all answers, comments,
timestamps, usernames) before any strength upgrade; that reading is a named
follow-up.
