# State-Space Search

**ChatGPT and Bart Massey**

## About this book

Many important problems give us a clear way to recognize a
good answer while leaving an enormous number of possibilities
to consider. We can check whether a timetable has clashes,
whether a configuration meets its constraints, or how evenly
a partition divides a workload. Discovering a satisfactory
answer can be much harder than checking one. State-space
search organizes that discovery: represent the possibilities,
explore promising choices, and use what we learn to avoid
unnecessary work.

This course approaches state-space search as a technique for
solving tractable instances of NP-hard problems. A hard
problem family can contain many instances that we can solve
with suitable representations, inference, bounds, and search
policies. The practical question is how far those methods
extend the range we can handle with available time and
memory. Sometimes we need any feasible answer; sometimes we
want a better candidate, an optimum, or evidence that no
solution exists. We will study both how to obtain answers
and what the search establishes about them.

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

**What counts as a state?** A state may be a partial
assignment, a complete candidate, or a situation along a
plan. It must retain enough information to evaluate the
relevant choices and their consequences. Resources or
history can make two apparently identical candidates
different for the search.

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
search effort includes time, nodes examined, and memory.
These differ from the quality of the answer, such as a
schedule's completion time or a route's length. Measurements
depend on the instances, representation, stopping rule, and
machine. For randomized methods, one run is one observation.
A comparison should make both successes and failures visible.

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

This is a course draft undergoing instructor review and
revision. Algorithms and worked numerical
examples receive explicit checks, but these checks do not
replace review of the teaching choices and explanations.
The source tree includes an editorial status record outside
the student-facing chapters.

The text and original figures are offered under
[CC BY-SA 4.0](attribution.md). References to other works do
not change those works' licenses.
