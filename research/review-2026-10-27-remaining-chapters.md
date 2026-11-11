# Review synthesis: Weeks 3–10

Reviewed 2026-10-27 Pacific using search-book-authoring and
its editorial guide. Every section of all eight chapters was
read, including pseudocode, formulas, examples, readings,
and transitions. Three independent review workstreams wrote
the detailed findings below; the root editor read the chapters
and reconciled their evidence and priorities.

The chapters need a substantive teaching revision before
being considered finished. The central algorithms and worked
arithmetic generally withstand careful scrutiny. One definite
technical specification error was found, in Week 9's exception
for solved game values. The larger recurring problem is that
several difficult methods have rules and hypothetical numbers
without a complete instance and trace connecting them.

Weeks 3–10 were reviewed without changing their source.
The new bibliography is infrastructure; these chapters still
need point-of-use citations and some additional sources.
Passing checks does not resolve those teaching or citation gaps.

## First priority: correct the game-value specification

At [Week 9, line 279](../src/09-adversarial.md#transposition-tables),
a solved full-game value is allowed as an exception to exact
fixed-horizon reuse. This can change the function defined
earlier: a nonterminal state with static evaluation zero
can have a proven full-game value +1. At horizon zero the
specified truncated value is still zero. The same mismatch
can occur at a depth-one root with that state as its child.

Use matching-horizon values to reproduce the stated truncated
function, or explicitly define solved states as an additional
leaf rule before the horizon test. Using solved information
can be desirable, but the semantics must say so. Root checked
this counterexample against the chapter's definition.
See W9-1 in the detailed review.

## Chapter revision queue

| Week | Most important repair beyond citations |
| --- | --- |
| 3 | Specify how depth-limited calls propagate cutoff versus complete failure. Give branch-and-bound an actual graph or partition and a derived bound. |
| 4 | Motivate a remaining-cost estimate concretely before its formal properties; distinguish reached, closed, and stale records in plain language. |
| 5 | Show an actual abstract projection, cost assignment, and database lookup. Trace RBFS through a bound update, branch switch, and regeneration; state its guarantee explicitly. |
| 6 | Establish the traveling-salesperson tour and cyclic edge order before deriving 2-opt, or remove this extra example. Preserve the strong coloring/SAT/partition repair traces. |
| 7 | Define anytime optimization and its feasibility limit. Supply one completely specified annealing policy and an accept/reject trace tracking current and best candidates. |
| 8 | Turn the scheduling horizon into explicit start domains, completion deadlines, precedence, and machine nonoverlap constraints. |
| 9 | Repair solved-value semantics; give one complete fixed-MAX alpha-beta recursion and a deeper window/return trace. Establish a small rule-based game for reuse. |
| 10 | Trace both bidirectional queues through the correct stopping test, and one complete MCTS iteration including MIN selection and backup. Give MAPF/CBS a concrete conflict split and explain LaCAM*'s objective qualification. |

These are priorities, not a requirement to add a new large
example for every named method. Reuse instances and diagrams
where that reduces the reader's prerequisite load. Keep
planning and scheduling compact within the ten-week scope.

## Bibliography and source support

The book-wide bibliography now contains every work in the
current weekly reading lists, plus sources for Markov states
and the new CNF explanation. First-use citations were added
in Weeks 1–2. Weeks 3–10 still leave the reader to infer source
support from optional reading lists. Add citations beside
the relevant concepts, matching the variant and assumptions
actually taught.

Some subjects need sources beyond those existing lists:
branch-and-bound, 2-opt, Metropolis acceptance and annealing
convergence, evolutionary and large-neighborhood search,
work stealing/action models, transposition-table semantics,
chance search, bidirectional stopping, and CBS. The detailed
reviews identify verified candidates and access limits.
Do not attach a convenient historic citation to a modern
implementation claim it has not been checked to support.

The remaining chapters' reading annotations mostly describe
sources; they do not currently conflate direct instructions
with findings as the old Week 2 annotations did. Add marked
reading advice where useful, rather than treating the lack
of advice itself as a technical error.

## Preserve the draft's strengths

Retain its explicit distinction between feasibility and
optimality, justified pruning and promising order, candidate
quality and search effort. Duplicate handling, reopenings,
goal-test timing, finite/infinite progress, zero-cost cases,
cost partitioning, fixed-MAX utilities, pending parallel work,
and stochastic failures are handled with unusual care.
The revision should explain these qualifications more
concretely rather than discard them to shorten chapters.

On narrow screens, several SVG labels are too small to read
comfortably inline despite valid layout. Full-size links and
alternatives help, but advertise those links or provide a
readable narrow presentation. Automated overflow checks do
not establish figure legibility.

## Evidence and limits

Detailed reports give exact source lines, evidence, proposed
repairs, full-section coverage, and source-access records:

- [Weeks 3–5](review-2026-10-27-weeks3-5.md).
- [Weeks 6–8](review-2026-10-27-weeks6-8.md).
- [Weeks 9–10](review-2026-10-27-weeks9-10.md).

Reviewers inspected the checks' implementations, reran the
relevant existing suites, and performed additional finite
calculations. These included all 181,440 reachable 8-puzzle
states and their Manhattan consistency checks, 3,321 extra
finite zero-cost IDA*/RBFS cases, coloring move deltas,
partition escape barriers, irregular minimax trees/windows,
and the chapter arithmetic. Selected primary-source passages
were checked for suspect or unfamiliar claims. Rendered
figures and teaching content received manual inspection in
addition to the browser smoke checks.

This evidence does not prove general correctness, audit all
cited papers, or supply missing instructional explanations.
Existing suites omit some important behaviors, including
depth-limit result propagation, transposition compatibility,
MCTS updates, and full certificate traces. Their passing
results must not be presented as coverage of those claims.
Instructor judgment and a subsequent teaching revision remain.
