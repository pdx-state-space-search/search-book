# Editorial guide

Use these standards to make chapters feel like one course.
Current topic allocation and specific editorial decisions
live in [BRIEF.md](../../../../BRIEF.md); do not duplicate
or override that evolving scope here.

## Reader and voice

Write for a reader with basic CS, algorithms, and programming
experience, but little search background. Rely on concepts
already developed in the book, not familiarity with an AI
textbook. Name the prerequisite when a later explanation
depends on it, with a short reminder or a useful link.

Use direct, connected prose with concrete subjects and active
verbs. Speak as a technically careful teacher reasoning with
the reader. An occasional "we" can carry a worked derivation;
it should not turn the chapter into a transcript of the
assistant's work. Keep production history and author-role
discussion in the book's designated front/back matter.

Explain purpose as well as mechanics. The reader should be
able to say why a choice or assumption matters, not merely
repeat a definition. Keep necessary technical qualifications
close to the claim they support. Avoid both unsupported
certainty and a thicket of exceptions before the main idea
has been established.

Do not write in slogans, promotional claims, or repeated
question-and-answer fragments. Prefer a paragraph developing
one idea. Use lists for genuinely parallel choices, tables
for comparisons, and headings for meaningful topic changes.
Do not substitute a table of terms for the explanation that
makes those terms intelligible.

## Explanatory sequence

Establish the outline at two levels in successive passes,
following the skill's outline-first workflow. At the top
level, give each section one clear teaching job and arrange
sections so their prerequisites are already available.
At the second level, identify the explanations and worked
examples needed to carry out those jobs. Do not let an
accumulation of individually useful additions determine
the chapter's organization by accident.

When reorganizing a draft, identify repeated explanations
and give each its main home. A brief reminder may support
a later argument, but a second introduction usually signals
an ordering or transition problem. A split should give each
reading a coherent purpose and a useful stopping point.

A useful pattern is concrete situation → named choices →
representation → method → worked behavior → justified result.
Adapt it to the section. A definitions section, an algorithm
section, and an experimental-methods section need not have
identical structures.

Introduce the meaning before the notation. In a CSP, first
explain what choice a variable represents and what its values
mean; then introduce its domain and symbolic notation.
Likewise, explain the information an estimate represents
before writing a priority formula.

On returning to a specific example, say "In our number
partitioning instance…" or "Return to the graph coloring
instance…". Use "In pathfinding…" for a general claim about
the problem, not for a claim about one chosen graph. Supply the
relevant groups, graph, objective, or state if the reader
needs them. Nearby sentences can then use ordinary pronouns.
Do not force a full problem restatement into every paragraph.

Keep examples continuous across a transition when useful.
For this book, graph coloring follows the explicit mapping
from map regions to vertices and borders to edges. Do not
silently alternate between regions and vertices. Identify a
new instance, such as changing to a two-color triangle.

A familiar-sounding problem can still need an introduction.
Before using a sliding-tile puzzle, a scheduling objective,
or a repair move to explain something else, explain its
relevant rules or use an already established example.
A preview may name later material, but the current argument
must not depend on an unexplained preview.

## Definitions and mathematical language

Use enough formalism to remove ambiguity and support the
learning objective. Avoid turning an informal introduction
into a full treatment of formal languages, encodings, or
complexity theory when an algorithms text can supply that
background. In this course's introduction, problems collect
parameter instantiations and an instance fixes parameters;
a complexity class groups problems by a stated property.

Define n before saying a problem takes time in n. State
whether it counts vertices, variables, items, bits, or another
quantity. Search depth is a property of a representation and
need not equal the chosen instance-size measure. Keep local
uses of overloaded symbols clear; consult the notation page
rather than assuming every symbol has one global meaning.

Distinguish the model's objective from the solver's effort.
Partition imbalance and schedule length evaluate answers;
node counts, elapsed seconds, and peak memory measure work.
Path cost is an objective when the answer is an action
sequence. A node is a candidate record the program processes;
a tree depicts how records are related. Explain that meaning
before relying on "visiting" a drawn node.

Node counts are useful machine-independent work measures for
a defined algorithm and counting convention. Distinguish
creation from expansion, and repeated work from distinct
states. State the usual polynomial-per-node assumption when
using counts to explain growth, while accounting for expensive
successor generation and heuristic work. Do not imply equal
time per node across all algorithms or implementations.

When finite quantified notation abbreviates a propositional
encoding, identify the finite index sets and the meanings of
the indexed variable names. Show an actual grounded expansion:
universal repetition becomes conjunction and finite existence
becomes disjunction. Do not accidentally introduce a different
logic or solver problem through unexplained notation.

## Algorithms, examples, and guarantees

Preserve these strengths of the existing draft:

- Small worked cases with enough initial data to reproduce
  the choices and arithmetic.
- Explanations of why inference, pruning, or a bound is sound.
- Explicit assumptions attached to completeness, optimality,
  memory, and termination claims.
- Attention to state identity, repeated arrivals, and retained
  information, rather than relying on algorithm names.
- Honest accounting of practical time and memory and of
  randomized outcomes, failures, budgets, and sampled units.

In a trace, specify order and tie-breaking when they affect
what the reader sees. Show changed domains, queue entries,
objective values, or bounds, rather than just announcing
success. Explain what the ending establishes and what it
leaves unresolved. Use a short correctness argument where
it clarifies the mechanism; a finite check is not that proof.

Keep a plausible selection preference separate from a
justified deletion. Most-constrained-first aims to expose
failure early; least-constraining-first aims to preserve
options. Such motivations are not universal runtime or
probability guarantees. Similarly, a good candidate is not
an optimality certificate without a valid bound or other
argument excluding improvements.

State space assumptions when they affect a result: finite
versus infinite, cost restrictions, goal-test timing, and
what duplicate information permits discarding work. In games,
keep the utility perspective consistent. In stochastic work,
keep failure observations visible and distinguish independent
seeds from independently sampled problem instances.

Use imperative pseudocode for consequential algorithm detail,
not as a replacement for motivation. Explain variables and
sentinels. Include necessary restoration, stale-entry, or
reopening behavior if the claimed guarantee depends on it.
Avoid long source listings and implementation details that
do not help the reader understand the method.

## Pseudocode typography and layout

Present pseudocode in the style of an algorithms textbook:

- Typeset it with proportional text, mathematical variables,
  and clear typographic emphasis for control words. Use
  appropriate HTML and local CSS for mdBook where needed;
  fenced code blocks and other typewriter-style displays
  are not the presentation format for algorithms.
- Keep the header brief: one task sentence naming the
  operation in capitals, describing its inputs in context,
  and stating its result or effect. For example: “SEARCH
  from state *s*, reached by path *p*; returning a solution
  path or failure.” Use the same variable names as the body.
  Explain preconditions, supplied operations, and details
  such as mutation or restoration in the surrounding prose.
- Use the left arrow **←** for assignment. Reserve **=**
  for equality, rather than using it or **:=** for assignment.
- Put one statement on each line. Give control headers
  their own lines and indent their bodies to show nesting;
  do not pack a condition and its action onto one line or
  combine several updates with semicolons.
- Preserve meaningful mathematical notation and explain
  symbols and sentinels before they are needed. Check the
  rendered indentation, line breaks, and readability at
  narrow widths and enlarged text.

## Diagrams and further reading

Draw the problem itself before asking an abstract diagram
to explain an algorithm operating on it. Later diagrams can
show state changes, competing paths, pruning, or bounds.
Reuse an illustration when it genuinely represents the same
object, explaining the new interpretation as with graph
coloring and its constraint graph.

Original SVGs should have descriptive alternatives, title
and description metadata, readable labels, and links to the
full-size originals. Distinguish an illustrative growth curve
from measured solver performance. Use words/labels as well
as color. Inspect the figure in the rendered chapter, not
only in isolation; surrounding text and navigation can collide
with labels, especially at enlarged text sizes.

Maintain a book-wide bibliography separately from the short
weekly reading recommendations. Give named concepts, such
as the Markov property, and substantive borrowed claims a
source at their point of introduction. Use stable links to
the bibliography entries so readers can trace a claim without
guessing which recommended paper supports it. A bibliography
entry alone does not identify which claim it supports.

Keep further reading light and annotated: what will the reader
learn, and which portion is a useful starting point? Separate
the description of a source from instructions to the reader,
for example with a distinct **Reading suggestion:** sentence.
Do not make a source's findings sound like course instructions
or make our advice sound like the source's claim.

Prefer primary author/publisher/conference sources. Verify
title, authors, year, and supplied publication details, and
check that the source supports the claim being cited.
Distinguish metadata access, selected passage checks, and
full-paper review. Core teaching must stand without purchasing
a text.
Follow the source ledger for actual adaptations; citing an
idea or using a topic outline is not copying source material.

## Questions for the final editorial pass

- Does the agreed outline give the chapter a clear purpose
  and each section a distinct job? Have later additions
  obscured that structure or repeated another section?
- Can a reader explain the section's purpose before meeting
  its notation? Are required terms already explained?
- Does each return to an example identify the problem and
  restore the needed context? Are transitions motivated?
- Do prose, formula, trace, figure, caption, and alternative
  text describe the same instance and objective?
- Does the result follow under the stated assumptions?
  Are preference, inference, feasibility, and proof distinct?
- Are parameters, units, counting rules, and utility/cost
  conventions clear? Is computation hidden inside a step?
- Do chapter title, contents label, links, and promised later
  material agree? Is an omitted topic still accidentally
  presumed by the remaining text?
- Do named concepts and substantive claims have traceable
  citations? Are bibliography entries separate from optional
  reading advice, and do sources support the cited variant?
- Does a paragraph, diagram, or derivation earn its reading
  time? If material feels dense, add a missing explanation
  or reconsider sequencing before shortening the prose.
- What remains for instructor judgment? Do the review record
  and status distinguish that from completed technical checks?
