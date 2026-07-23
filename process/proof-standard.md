# Proof standard

## Minimum standard for every candidate

A candidate must:

- prove exactly the current version of `STATEMENT.md`;
- use consistent definitions and quantified domains;
- identify all imported results and verify every hypothesis;
- expose dependencies between nontrivial claims;
- handle boundary, equality, and degenerate cases;
- justify existence, convergence, interchange, choice, and regularity steps when
  used;
- distinguish exhaustive computation from sampling;
- contain no unresolved obligation that blocks the conclusion.

“Obvious,” “generic,” “similarly,” and “without loss of generality” are prompts for
an audit, not justifications.

## Proof promotion gate

`complete` + `proved` requires:

1. a coherent `PROOF.md` with no conclusion-blocking gap;
2. every used claim marked `proved`, `assumed`, or `imported` with support;
3. no `open`, `in_progress`, or `blocked` proof obligation;
4. at least two adversarial review records;
5. all critical and major review findings resolved and cross-referenced;
6. one final statement-to-conclusion audit independent of the discovery narrative;
7. reproducible verification for any computation essential to the proof;
8. a standalone reviewed LaTeX source named by `latex_file` in `problem.json`;
9. a PDF compiled from it by Tectonic, named by `pdf_file`, with the compiler
   version recorded in `latex_engine`.

The two reviews should be meaningfully distinct—for example, a line-by-line logic
audit and a hypothesis/counterexample audit.

The LaTeX source is a publication-quality restatement of the exact reviewed
argument, not a replacement for canonical Markdown records. It must identify the
statement version and the review records. Run `proofctl.py typeset <slug>` to
compile it with Tectonic, retain the source and PDF, and record the compiler
version. A missing compiler blocks promotion; agents repair the toolchain rather
than silently omitting the PDF.

## Disproof promotion gate

`complete` + `disproved` requires:

1. an explicit object or construction satisfying every hypothesis;
2. an exact demonstration that the conclusion fails;
3. at least one reproduction review from the statement;
4. reproducible computation or a certificate if enumeration is essential.

## Partial results

A rigorous lemma or special case can be marked proved in `CLAIMS.md` while the main
claim remains open. State its exact scope and do not promote the dossier outcome.
Reusable results may also be distilled into `knowledge/`.

## Formal proof assistants

A checked formal proof is strong evidence only for the encoded theorem under the
encoded axioms and trusted kernel. Record the theorem statement, toolchain version,
axioms, and build command, and still audit correspondence with `STATEMENT.md`.
