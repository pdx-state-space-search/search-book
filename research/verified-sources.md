# Verified editorial sources

Checked by the root editor, 2026-10-21 Pacific / 2026-10-22 UTC.
This file records metadata/coverage checks, not full-text review.

## Khemani

Deepak Khemani, Search Methods in Artificial Intelligence,
Cambridge University Press, 2024.

Publisher TOC:
https://www.cambridge.org/core/books/search-methods-in-artificial-intelligence/contents/D2DE03267943183B66EF635E65048691

Publisher front matter:
https://assets.cambridge.org/97810092/84325/frontmatter/9781009284325_frontmatter.pdf

Verified broad chapters include search spaces, blind and heuristic
search, stochastic local search, A* variants, decomposition, games,
planning, deduction, machine learning and constraint satisfaction.
Coverage informs our selection, without importing textbook prose,
figures, chapter summaries or detailed exposition. Our sequence
moves CSP/SAT early and adds explicit systems/evaluation coverage.

## Course-linked Korf reading

Richard E. Korf, A Complete Anytime Algorithm for Number
Partitioning, Artificial Intelligence 106(2), 181–203, 1998.
DOI: https://doi.org/10.1016/S0004-3702(98)00086-1

Author bibliography:
https://web.cs.ucla.edu/~korf/publications.html

Instructor-hosted paper:
https://web.cecs.pdx.edu/bart/cs510cs/papers/korf-ckk.pdf

Verified title/venue/metadata and relevance to the prior syllabus.
No source prose or figures reused. The paper's core connection is
heuristic solutions extended into complete anytime search.

## mdBook

Installed version: 0.5.2, verified by mdbook --version.
Official configuration:
https://rust-lang.github.io/mdBook/format/configuration/general.html
https://rust-lang.github.io/mdBook/format/configuration/renderers.html

The project uses the built-in HTML renderer and local custom CSS,
without extra preprocessors or MathJax.

## Chapter reference checks

Added during integration below. Candidate citations supplied by
chapter drafters are not treated as verified until checked.

## Root verification during recovery, 2026-10-22 Pacific

Publisher/author metadata checked directly for:
- Mackworth, Consistency in Networks of Relations (1977),
  Artificial Intelligence 8(1), 99–118. DOI in week 2 matches
  publisher and author bibliography, cs.ubc.ca/~mack/.
- Minton, Johnston, Philips, Laird, Minimizing Conflicts (1992),
  DOI 10.1016/0004-3702(92)90007-K; publisher author list
  confirms Philips spelling and year.
- Glover, Tabu Search—Part I (1989), DOI
  10.1287/ijoc.1.3.190; publisher metadata and abstract checked.
- Lourenço, Martin, Stützle, Iterated Local Search (2003),
  Handbook of Metaheuristics, pp. 320–353. Springer page
  confirms authors and DOI 10.1007/0-306-48056-5_11.
- Johnson, Aragon, McGeoch, Schevon (1989), Optimization by
  Simulated Annealing, Part I: Graph Partitioning; publisher
  DOI 10.1287/opre.37.6.865 and title/year checked.
- Engineering references: see 08-notes.md.

These are metadata and relevance checks, not full-paper review.

## Final reference reconciliation — 2026-10-22 Pacific

Recovered chapter citations were checked during recovery;
their DOI/author/publisher evidence and IEEE access limitation
are recorded in recovery-review.md. Engineering references
are in 08-notes.md. Final-review-sources.md records the last
metadata checks for AIMA, Dechter, Davis/Logemann/Loveland,
and Kirkpatrick/Gelatt/Vecchi. No cited paper was
comprehensively audited.

The root additionally retrieved the Crossref records for
10.1145/368273.368557 and 10.1126/science.220.4598.671.
These publisher deposited records confirm the chapter
titles, author lists, dates, and DOIs; selected metadata is
saved in final-citation-metadata.json. The ACM and Science
full-text access limitations remain. No correctness claim
is based on the secondary catalog spot checks in the
source-review note.

The authors' AIMA site identifies the 4th US edition and
chapter 3 as “Solving Problems by Searching”:
https://aima.cs.berkeley.edu/
Its editions page identifies the edition as 2020:
https://aima.eecs.berkeley.edu/translations.html

## Week 2 and SAT repair readings — 2026-10-27 Pacific

- Edward P.K. Tsang, Foundations of Constraint Satisfaction,
  Academic Press, 1993. Author's page confirms the original
  publication and distinguishes the corrected 2014 reprint:
  https://www.bracil.net/edward/FCS.html
  The page is a metadata/scope check, not access to the book.
- James M. Crawford and Larry D. Auton, Experimental Results
  on the Crossover Point in Satisfiability Problems, AAAI-93,
  pp. 21–27. Primary conference PDF:
  https://cdn.aaai.org/AAAI/1993/AAAI93-004.pdf
  Checked metadata and selected TABLEAU/experiment passages.
  The final printed page is 27; corrected an initially supplied
  21–26 range. The annotated reading distinguishes the paper's
  random-SAT crossover from a fixed-budget growth illustration.
- Bart Selman, Henry A. Kautz, Bram Cohen, Noise Strategies
  for Improving Local Search, AAAI-94, pp. 337–343:
  https://cdn.aaai.org/AAAI/1994/AAAI94-051.pdf
  Checked metadata and selected SAT local-search/noise passages.
  Used in Week 6's annotated reading, not the introductory SAT
  list. The chapter describes the WalkSAT family rather than
  reproducing a specific original implementation listing.

These checks do not claim comprehensive audits of the works.
No source prose, figures, or algorithm listings were adapted.
