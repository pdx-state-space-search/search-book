# About this book

State-space search solves a problem by choosing which
possibilities to consider, which to keep, and which to rule
out. A few simple choices can make the difference between
examining a hundred states and examining a trillion. Those
choices also determine what a solver can promise: a solution,
the best solution, a useful answer before a deadline, or a
proof that no solution exists.

This book is a short introduction for a ten-week course at
Portland State University. It assumes an undergraduate
algorithms course, basic discrete mathematics, and some
experience implementing programs in an ordinary imperative
language. It does not assume previous study of artificial
intelligence. The algorithms are described without tying
them to a particular programming language.

The goal is to learn to model a problem, choose and explain a
search method, implement it carefully, and evaluate its
behavior. That requires more than recognizing algorithm
names. We will ask what information an algorithm retains,
what its ordering rule means, why a pruning step is sound,
and which assumptions make its guarantees true.

## A route through ten weeks

Each chapter supplies one week's core reading. Chapters are
intended to be short enough to read carefully, with worked
examples that reward tracing by hand. Definitions are
introduced where they are used; the
[notation reference](notation.md) collects conventions for
later consultation. The chapters build on one another, so
"self-contained" means that the course text supplies the
needed search background, rather than that every chapter
repeats all earlier definitions.

| Week | Main question |
| --- | --- |
| 1 | What is the space we are searching? |
| 2 | How can constraints rule out choices early? |
| 3 | How can systematic exploration establish completeness? |
| 4 | How should costs and estimates order the frontier? |
| 5 | Where do useful heuristics come from, and what if memory fills? |
| 6 | How can a complete candidate solution be repaired? |
| 7 | How can randomness help, and how do we measure its effect? |
| 8 | What makes search efficient on actual machines? |
| 9 | What changes when another player chooses the next move? |
| 10 | How do these foundations support stronger search methods? |

Constraint satisfaction appears early because it makes the
role of modeling and inference especially clear. Complete
search and best-first search then develop complementary
ways to explore possibilities. Local and stochastic methods
trade some guarantees for the ability to improve candidates
quickly. Engineering matters throughout, with a chapter
focused on representation, memory, and parallel work.
Planning and scheduling provide applications without taking
over the course. The final two weeks introduce adversarial
search and extensions that connect the basics to research.

## Four questions to keep asking

**What counts as a state?** A state must retain enough
information to determine the legal choices and their
consequences. Two situations that look alike on a diagram
may require different states if their resources or histories
affect what happens next.

**What counts as a solution?** Finding any legal assignment,
finding a cheapest path, minimizing a scheduling objective,
and choosing a move against an opponent are different
problems. A method's guarantee makes sense only after the
problem is stated precisely.

**What justifies discarding work?** A bound can establish
that a branch cannot improve the incumbent. Propagation can
establish that a partial assignment cannot be extended.
Duplicate detection can establish that another path already
represents the relevant possibilities. A plausible guess by
itself establishes none of these things.

**What did the experiment actually measure?** A solver's
runtime depends on its instances, representation, stopping
rule, and machine. For randomized methods, one run is one
observation. A comparison should let someone else understand
both what succeeded and what failed.

## Examples and algorithms

Figures link to their full-size SVG originals; open a figure
to enlarge it independently of the surrounding text.

The book returns to small graphs, graph coloring, sliding
tiles, number partitioning, and simple games. Small examples
are not evidence that an algorithm scales. They let us see
exactly what the algorithm does before studying why it
sometimes scales and sometimes does not.

Pseudocode uses assignment, loops, conditionals, sets, and
queues in their ordinary imperative sense. It is an
algorithm description rather than a ready-to-run program.
Important implementation choices, such as priority-queue
stale entries or collision-safe state comparison, are
explained in words. There are no programming-language
listings or exercises in this draft.

A statement that a method is complete or optimal always
belongs to a particular version of that method under stated
assumptions. Changing duplicate handling, the goal test, a
cost assumption, or the meaning of the heuristic can change
the result. Treat these details as part of the algorithm.

## Further reading and draft status

The short reading lists at chapter ends point to sources
that explain a central idea in greater depth or connect it
to an application. They are extensions, not an additional
required textbook. The [reading guide](reading-guide.md)
explains how to use them.

This is a first editorial draft prepared with AI assistance
for instructor review. Algorithms and worked numerical
examples receive explicit checks, but these checks do not
replace review of the teaching choices and explanations.
The source tree includes an editorial status record outside
the student-facing chapters.

The text and original figures are offered under
[CC BY-SA 4.0](attribution.md). References to other works do
not change those works' licenses.
