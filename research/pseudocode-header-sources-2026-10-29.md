# Pseudocode header examples from two textbooks

Read-only source research, 2026-10-29. These are narrow observations
from specific examples, not a claim that all algorithm textbooks use
the same format.

## CLRS, fourth edition

- The publisher identifies the linked book as the fourth edition of
  *Introduction to Algorithms* by Cormen, Leiserson, Rivest, and Stein:
  [MIT Press book page](https://mitpress.mit.edu/9780262367509/introduction-to-algorithms/).
- Cormen's official typesetting documentation for CLRS 4e says that a
  codebox usually starts with a procedure name and its parameters; it
  also notes exceptions. It gives `INSERTION-SORT(A, n)` as the
  example on printed book page 19. The first line is a procedure
  signature, followed immediately by code. It does not put separate
  `Input:` or `Output:` labels in that codebox. The documentation does
  not set out preconditions or postconditions as header fields:
  [CLRS 4e pseudocode typesetting guide](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/11599/clrscode4e.pdf),
  PDF page 6 (zero-based page 5), printed page reference 19.
- The same guide's “typical structure” discussion explicitly qualifies
  this as usual, not universal, and mentions a no-procedure-name
  exception on printed page 504. It is therefore safest to describe
  CLRS's observed convention as “often a procedure signature first,”
  not as a mandatory signature for every codebox. Same source, PDF
  page 6.
- MIT Press also hosts the official 4e “Pseudocode and Figures as
  PDFs” download linked from the book page:
  [supplement ZIP](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/11599/Pseudocode-and-Figures_PDF.zip).
  Its pseudocode archive includes an `Insertion-Sort.pdf` example.
  The official guide provides the directly verifiable page reference
  and source example above.

## Dasgupta, Papadimitriou, and Vazirani

- The UC San Diego author site identifies the book and its authors:
  [book page](https://cseweb.ucsd.edu/~dasgupta/book/). The chapter
  PDFs are hosted by coauthor Umesh Vazirani at Berkeley.
- In Chapter 1, the recursive multiplication example is Figure 1.1,
  printed page 25 (PDF page 5, zero-based page 4). It begins with
  `function multiply(x, y)`, then two explicit lines identifying the
  input and output, then the body. The input line includes the domain
  constraint `y ≥ 0`; the output line says the result is their
  product. So the signature and the input/output contract appear
  separately at the head:
  [Chapter 1 PDF](https://people.eecs.berkeley.edu/~vazirani/algorithms/chap1.pdf).
- Another instance is `extended-Euclid(a, b)`, Figure 1.6, printed
  page 31 (PDF page 11, zero-based page 10). It likewise uses a
  function signature followed by `Input:` and `Output:` lines. The
  latter specifies both the gcd and the Bezout relation. Same Chapter
  1 PDF.
- This chapter shows explicit input/output header rows for those
  figures. It does not establish that every algorithm in the book
  does so, and these examples do not use a separately labeled
  precondition/postcondition block.

## Access and verification notes

The CLRS publisher exposes the full text of the Cormen-authored
typesetting guide and a downloadable pseudocode supplement, rather than
a public full-book PDF. Its example is explicitly tied to fourth
edition page 19 in that primary source. The DPV Berkeley chapter PDF is
author-hosted and directly displays the two labeled header examples.
Page numbering above gives both printed book pages and PDF page
positions to avoid ambiguity.

## Root inspection of Bart's pseuf examples

Read the README, all five algorithm examples, the qsort LaTeX
wrapper, and relevant formatter output routines under
/local/src/pseuf without modifying that repository.

- examples/qsort.pseu:11 uses a natural task sentence naming
  qsort, the array role, and its identifier.
- examples/gauss-sum.pseu:2 states the task of adding the
  integers from one through n.
- examples/shuffle.pseu:2 and the two other shuffle variants
  similarly put the argument's role in a To ... sentence.
- These examples do not establish a separate, consistent
  returned-value/effects header. The result treatment for
  this book still needs an explicit choice; do not claim
  that pseuf already supplies a Produces convention.

The formatter emphasizes identifiers and keywords while
allowing ordinary prose. The relevant lesson is the natural
language task header, not a required formal signature.
Keep Bart's newer assignment-arrow and one-statement-per-line
requirements even where older examples use other conventions.

Root also downloaded the two cited primary PDFs to the ignored
build tree and rendered the referenced CLRS-guide page 6 and
DPV chapter page 5 with Ghostscript. Visually verified the
CLRS guide's explanatory paragraph and TeX declaration example,
and DPV's actual multiplication header with Input/Output rows.
The CLRS guide page contains source for its example, not a
rendered reproduction of the whole book page. DPV's shown
pseudocode uses a typewriter face, further demonstrating that
textbook layout conventions vary; Bart's proportional-font
preference remains this book's requirement.

Proposed direction for discussion: retain a standalone capital
algorithm title, replace the function-declaration header with
a concise To ... task sentence incorporating argument roles,
and follow it with one short sentence specifying returned
value or effects. For DFS, distinguish the returned path copy
from restoration of the mutable input path. No chapter or
skill changes were made during this comparison.
