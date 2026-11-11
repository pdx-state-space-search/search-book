# Campaign status

## Instructor review and revision in progress

Latest revision: 2026-11-11 Pacific. All ten chapters have a
first draft. The introduction and Weeks 1–2 have been revised
from BOOK-NOTES.md and follow-up discussion. The book remains
in substantive authoring and instructor review.
Read the built version at [_build/index.html](_build/index.html).

The early chapters now use Bart's definitions: complete means
examining every state, and systematic means examining each
state at most once. Related later references and the notation
page agree. OUTLINE.md has grouped sections and expanded
plans for anytime search and useful inadmissible heuristics.
Those fuller treatments remain authoring work; learning from failure, limited discrepancy search, beam
search, and symmetry reduction are now approved additions.

Week 1 now has Part I (Why Search?) and Part II (Modeling
and Assessing Search), following the accepted outline. It
adds emergent behavior through local repair and a contrasting
synchronous cycle, with source support. It illustrates
graph coloring, number partitioning,
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
  careful agent reviews are complete, with substantive
  revisions still needed. Week 6 has a SAT local-search addition.
- New [review synthesis](research/review-2026-10-27-remaining-chapters.md)
  prioritizes those repairs. Week 9's solved-value exception
  does not preserve its exact fixed-horizon function; the
  source remains unchanged pending the revision pass.
- Whole-book bibliography added; Weeks 1–2 now link concepts
  to sources. Later chapters still need point-of-use citations
  and some additional sources identified in the reviews.
- Ten original teaching figures. The three introductory
  diagrams include the graph reused as a CSP constraint graph.
- Week 1 is about 4,600 words; Week 2 about 3,200. Other
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

mdBook builds. The source/link check reports 19 HTML pages
and 652 checked internal links with no errors. All weekly
contents labels now agree with the chapter titles, with a regression check.
There is one advisory word-count warning for Week 1's roughly
4,600 words; the longer explanation follows the accepted
revision scope rather than a fixed word target.

The algorithm suite passes, including 110,592 forward-checking
CSP/partial-assignment cases. The example suite passes 8,768
SAT ground assignments, exact forward-checking domains, SAT
unit/repair examples, and the other retained examples.
The memory-bounded/bidirectional extension suite also passes.
These are finite regression checks, not general proofs.

The revision review checked encodings, counts, figures, and
beginner exposition. Its citation-page correction and clarity
suggestions were integrated; see
research/review-2026-10-27-chapter2.md. All 48 browser/view
checks pass, including navigation-overlap checks at enlarged
text sizes. The new figures and grounded formulas were
visually inspected; details are in research/review-log.md.

## Continuing

Week 1 was rewritten on 2026-10-28 using the accepted
[working outline](research/week1-outline-2026-10-28.md).
Problems, Instances, and Models now opens Part II. The chapter
keeps its file, title, and week mapping. Existing examples,
figures, and substantial prose were reused. It awaits Bart's
next read. Independent review in
[the rewrite report](research/review-2026-10-28-week1-rewrite.md)
found one reversed road-model example, now corrected, and no
other substantive defects. New examples were independently
checked; this is not a claim of general algorithm proof.

The latest notes on Weeks 1–2 have been applied: NP terminology,
specific instance re-entry, compact equisatisfiable CNF,
formula readability, and distinct reading advice. The
repository-local
[authoring skill](.agents/skills/search-book-authoring/SKILL.md)
captures the teaching style, worked-example conventions,
and review expectations, now including a separate bibliography
and point-of-use citations. It was used for the remaining
chapter reviews; do not mistake those reviews for completed
chapter revisions. The detailed reports and synthesis are
the next revision queue.

Use this status, BOOK-NOTES.md, BRIEF.md, and the latest
research/review-log.md entry for current authoring decisions.
Older completion statements refer to the first-draft milestone,
not completion of all book authoring. The 2026-10-22 validation
retains the earlier AC-3 evidence as historical material only.
