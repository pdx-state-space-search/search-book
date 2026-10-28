# Editorial brief

Authoritative user decisions, 2026-10-21 Pacific.

Create a ten-week, self-contained introductory text for PSU
CS 410/510 State-Space Search, based on the syllabus in
../front-matter/syllabus.md and the earlier Wikipedia outline.
Audience: algorithms and systems prerequisites; fluent imperative
programming, but little prior AI/search knowledge.

- mdBook only. Source Markdown in src/. No PDF, EPUB or exercises.
- Target 2,500–3,500 words per weekly chapter, preferably fewer
  than ten conventional pages. This is a reading-load target,
  not a guarantee of pagination in reflowable HTML.
- Language-neutral; short precise imperative pseudocode only
  when it substantially helps. No implementation source code.
- Develop basics through explanations, original worked examples,
  explicit assumptions, short correctness arguments and diagrams.
- Compress planning and scheduling into applications; preserve
  CSP/SAT, complete search, local/stochastic search, heuristics,
  implementation performance and introductory adversarial search.
- Light, annotated bibliography with publicly reachable primary
  readings where possible. Do not invent citations or results.
- Original prose is under CC BY-SA 4.0. Wikipedia adaptation
  requires an exact revision, article/authors-history link, license,
  affected section and description of edits in research/source-log.md
  and the reader-facing attribution page. Do not copy copyrighted
  textbook prose or figures. Khemani TOC informs coverage only.
- New diagrams should be original SVGs, readable at high zoom,
  with descriptive alternatives; no unconfigured Mermaid dependency.
- Keep notation and assumptions explicit: state versus node/path,
  solution versus optimality, finite/infinite spaces, positive costs,
  duplicate handling, goal test timing, A* reopenings.
- Use repeated examples where useful: weighted directed graphs,
  sliding tiles, graph coloring, number partitioning, small games.
- Do not read or reuse student submissions or grading records.
- Never modify syllabus/archive materials. Never commit or push.

## Chapter allocation

1. Models, state spaces and computational foundations.
2. Constraint satisfaction, SAT, backtracking and propagation.
3. Systematic search: DFS/BFS/iterative deepening, branch and bound.
4. Best-first search: UCS, greedy and A*; duplicate handling.
5. Heuristic design and memory-bounded search, IDA*, RBFS.
6. Local search, neighborhoods, repair and landscapes.
7. Stochastic optimization, hybrids and honest evaluation.
8. Engineering search: memory, concurrency, planning/scheduling.
9. Adversarial search: minimax, alpha–beta, evaluation.
10. Beyond the basics: bounded/anytime, bidirectional search,
    Monte Carlo tree search and selected recent directions.

## Campaign

Draft all chapters, integrate notation and references, independently
check algorithms and numerical examples, build mdBook, inspect
rendered figures/pages, and retain a precise review log and remaining
issues. Lower-cost drafting/research agents work on bounded tasks;
the root editor integrates and verifies all work.

## Instructor revision decisions — 2026-10-27 Pacific

BOOK-NOTES.md and the follow-up discussion guide the next
authoring pass. The introduction and Week 1 should center
state-space search as a technique for solving tractable
instances of NP-hard problems. Introduce feasibility and
candidate optimization alongside pathfinding, explain the
practical growth knee, and distinguish objective value,
path cost, and computational search effort.

Week 1 may grow to supply the missing explanations and
small examples. Retain basic complexity definitions without
an opening detour into easy problem families. Do not include
the proposed historical claim about early AI hardware
optimism until specific sources have been checked.

List ChatGPT and Bart Massey together as authors. Credit
them in the title block and metadata, without an interstitial
authorship paragraph. Reserve an Epilogue at the end for
discussion of the book's history and authorship. This
supersedes the earlier role-based credit wording.
A complete first draft does not imply that instructional
authoring and revision are finished.
