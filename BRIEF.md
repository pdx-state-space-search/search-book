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
- Never modify syllabus/archive materials. Commit only when
  explicitly requested; pushes require separate permission.

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

## Review through Week 2 — 2026-10-27 Pacific

Assume only basic CS and concepts already explained here.
Introduce notation through concrete choices, name a problem
when returning to its example, and use diagrams and added
explanation where they help. Use graph coloring consistently
after explicitly relating it to map coloring.

Discuss a problem informally as a collection of parameter
instantiations, an instance as particular parameter choices,
and a class as a collection of problems with a stated
property. Defer full formal problem descriptions to an
algorithms textbook. Define what n measures before discussing
growth in n. Explain nodes as candidate records and node
counts as a machine-independent work measure, with the usual
polynomial-per-node assumption stated and qualified.

Week 2 supplies the main SAT foundation: propositions,
literals, CNF, finite quantified shorthand and grounded
expansion, encoding correctness, backtracking, variable/value
ordering, forward checking, and unit propagation. Quantifier
indices range over explicit finite sets; this is not a new
QBF topic. Omit AC-3 entirely for now, including Week 10.
Name most-constrained-first and least-constraining-first.

Readings include Tsang and Crawford–Auton on TABLEAU.
WalkSAT belongs in the local-search week. All contents
labels should agree with chapter titles. Longer chapters
are acceptable when the extra material supplies clarity.

## Bibliography and reading advice — 2026-10-27 Pacific

Maintain a bibliography for the whole book, separate from
suggested readings. Cite sources for named concepts such as
the Markov property where they are introduced. Distinguish
descriptions of suggested readings from instructions to the
reader. When returning to one worked example, identify our
particular instance rather than implying a claim about the
problem in general.

## Outline-first authoring — 2026-10-28 Pacific

Start chapters with a two-level outline, one level at a time:
establish top-level sections before subsections, then draft
prose. Reconsider Week 1's organization at the top level
before rewriting it. Add emergent behavior as another
philosophical focus alongside computational difficulty.
Keep Week 1 as one chapter, grouped into Part I (Why Search?)
and Part II (Modeling and Assessing Search). This supersedes
the proposed split into separate reading chapters and preserves
the mapping between chapters and weeks. Both outline levels are accepted for rewriting. Place
Problems, Instances, and Models first in Part II, leaving
three main sections in Part I and five in Part II. Give the
opening examples only the brief problem/instance distinction
needed by Part I. Reuse existing prose where appropriate.

## Pseudocode presentation — 2026-10-29 Pacific

Typeset pseudocode like an algorithms textbook, rather than
as typewriter text. Use ← for assignment and one statement
per line. Preserve clear control-flow indentation and
mathematical typography in the rendered book.
Keep the header to a brief task sentence: the operation's
name in capitals, its inputs in context, and its result or
effect. The surrounding text provides the details.

## Coverage and guidance — 2026-11-11 Pacific

Use Bart's definitions: complete search eventually examines
all states in the stated space; systematic search examines
each state at most once. Distinguish continued traversal from
an early-stopping solver. Duplicate filtering precedes state
examination; actual reopening or regeneration can repeat it.
Sound pruning may preserve solution or optimality guarantees
without examining all states. State those guarantees directly.

Teach anytime search explicitly, beginning with deterministic
branch-and-bound before stochastic policies and certificates.
Give admissibility a full treatment including the positive
value of inadmissible guidance. Distinguish ordering estimates
from justified pruning/certification bounds. The outline adds
this coverage; fuller chapter treatments follow its review.

## Approved topic additions — 2026-11-11 Pacific

Add learning from failure (Week 2), limited discrepancy search
(Week 3), beam search (Week 5), and worked symmetry reduction
(Week 8). All four are approved core coverage, with concrete
examples and the existing chapter/topic hierarchy preserved.
Keep their treatment focused within the ten-week scope.

Bart reports that learning from failure, symmetry reduction,
and limited discrepancy search connect to work at CIRL during
his time there. Reflect that in reading choices and retain it
for the Epilogue's history discussion. Ginsberg's Dynamic
Backtracking is a relevant CIRL source; GRASP remains a
separate connection for the SAT clause-learning example.
