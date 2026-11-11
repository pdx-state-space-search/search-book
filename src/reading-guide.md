# Reading guide

The weekly chapters provide the core reading. Their short
"Further reading" sections serve two purposes: to fill in a
technical detail that a short chapter cannot fully develop,
and to offer a path into the literature. Reading every
listed item is not necessary to follow the next chapter.

The [bibliography](bibliography.md) collects full references
for the book. In-text citations point there to identify
sources for concepts and claims. A citation need not be a
suggested assignment; the weekly recommendations describe
selected works and give separate reading advice.

For a first pass, read the chapter's main argument and work
through its example. If a method's guarantee is unclear,
identify its assumptions before consulting a longer source.
For a second pass, choose one source that addresses the
particular gap: a proof, an implementation concern, or a
stronger application.

Some references are research papers. A useful first reading
of a paper is its problem statement, main example, central
claim, experimental setup, and limitations. A paper's
algorithm may be more general than the version taught here;
its assumptions may also be different. The citation is a
route to that additional detail, not permission to transfer
all of its claims to every variant of an algorithm.

## How the reading plan was assembled

The emphasis on constraint satisfaction, complete search,
optimization, and practical implementation comes from Bart
Massey's earlier State-Space Search syllabus. The chapter
sequence also uses the broad coverage of a previous
Wikipedia reading outline: representation, systematic
search, best-first search, heuristics, local and stochastic
search, and games. Wikipedia is not treated as the authority
for an algorithm's correctness.

Deepak Khemani's *Search Methods in Artificial Intelligence*
(Cambridge University Press, 2024) provides a useful coverage
comparison. Its [publisher table of contents](https://www.cambridge.org/core/books/search-methods-in-artificial-intelligence/contents/D2DE03267943183B66EF635E65048691)
includes search spaces, uninformed and heuristic search,
stochastic local search, A* variants, games, planning, and
constraint satisfaction. We place constraints earlier to
match this course, shorten planning, and add explicit
engineering and evaluation coverage. We do not follow its
full breadth in deduction or machine learning. The editorial
notes distinguish this verified topic list from our own
choices about sequence and emphasis.
No access to a cited book is necessary to read these notes,
and no publisher's prose or figures are reproduced here.

## Scope

This is a short course text, not a survey of all search.
Planning and scheduling illustrate how a representation and
a bound can turn an application into a search problem.
SAT introduces a central constraint language without trying
to teach the full design of an industrial SAT solver.
Game search introduces the main adversarial ideas without
covering imperfect information or general-sum games.

Later readings can extend any of these directions. The final
chapter connects selected extensions to the preceding
fundamentals instead of treating novelty as a substitute
for understanding them.
