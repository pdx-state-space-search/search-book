# Campaign status

## Instructor review and revision in progress

Latest revision: 2026-10-27 Pacific. All ten chapters have a
first draft. The introduction and Weeks 1–2 have been revised
from BOOK-NOTES.md and follow-up discussion. The book remains
in substantive authoring and instructor review.
Read the built version at [_build/index.html](_build/index.html).

Week 1 now illustrates graph coloring, number partitioning,
and pathfinding, and introduces problems, instances, and
classes informally. It defines size measures and explains
node counts through candidate records and per-node work.
Week 2 supplies the main SAT foundation, including CNF and
finite quantified shorthand with explicit grounded expansion.
AC-3 has been removed, not postponed to another chapter.
Forward checking and unit propagation provide the deduction
examples. Week 6 introduces SAT repair and WalkSAT.

The authors remain ChatGPT and Bart Massey, credited in the
opening title block and metadata. The closing Epilogue is
reserved for history and authorship. The proposed early-AI
hardware history remains deferred until sources are verified.

## Current draft and remaining work

- Introduction and Weeks 1–2: revised, awaiting Bart's read.
- Weeks 3–10: first drafts awaiting manual instructor review;
  Week 6 has a short SAT local-search addition.
- Ten original teaching figures. The three introductory
  diagrams include the graph reused as a CSP constraint graph.
- Week 1 is about 3,900 words; Week 2 about 2,800. Other
  chapters are about 2,100–2,500. Length follows teaching needs.
- Exercises and instructor solutions remain outside scope.
- Epilogue: history/authorship discussion reserved for later.

BOOK-NOTES.md is preserved as Bart edited it. Prior text is
recoverable from Git and the earlier revision snapshots.
No syllabus/archive material was changed, and no student
submissions or grading records were read. Local commits are
made only when explicitly requested; pushes require separate
permission.

## Current validation

mdBook builds. The source/link check reports 18 HTML pages,
558 internal links, and no errors. All weekly contents labels
now agree with the chapter titles, with a regression check.
There is one advisory word-count warning for Week 1's 3,880
words; the longer explanation follows the accepted revision
scope rather than a fixed word target.

The algorithm suite passes, including 110,592 forward-checking
CSP/partial-assignment cases. The example suite passes 8,768
SAT ground assignments, exact forward-checking domains, SAT
unit/repair examples, and the other retained examples.
The memory-bounded/bidirectional extension suite also passes.
These are finite regression checks, not general proofs.

The revision review checked encodings, counts, figures, and
beginner exposition. Its citation-page correction and clarity
suggestions were integrated; see
research/review-2026-10-27-chapter2.md. All 45 browser/view
checks pass, including navigation-overlap checks at enlarged
text sizes. The new figures and grounded formulas were
visually inspected; details are in research/review-log.md.

## Continuing

Use this status, BOOK-NOTES.md, BRIEF.md, and the latest
research/review-log.md entry for current authoring decisions.
Older completion statements refer to the first-draft milestone,
not completion of all book authoring. The 2026-10-22 validation
retains the earlier AC-3 evidence as historical material only.
