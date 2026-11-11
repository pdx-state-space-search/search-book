# Independent review: Week 1 rewrite

Reviewed 2026-10-28 against the accepted two-part outline.
Review-only: no chapter, check, or skill files were edited.

## Scope and outcome

Read all of `src/01-models.md`, the authoring skill and its
editorial guide/examples, BRIEF.md, BOOK-NOTES.md, STATUS.md,
notation, the accepted outline, bibliography, and the opening
of Week 2. Compared the previous chapter's organization with
the preserved revision snapshot. Inspected relevant figure
source and check coverage. Rendering is being checked by the
root agent and is outside this review's evidence.

There is one required factual wording correction. I found no
additional substantive prerequisite, mathematical, guarantee,
or example-identity defect in the rewritten chapter.

## Required correction

### Medium: the closed-road example reverses the omission

Anchor: `src/01-models.md:324`–325.

The text says that a model which "omits a closed road" can
recommend an unusable path. Omitting that road from the
network prevents a route from using it. The intended failure
is omission of the road's closure while leaving the road
available in the model.

Concrete repair: write "A route model that omits the fact
that a road is closed can similarly recommend an unusable
path," or "A route model that treats a closed road as usable
can similarly recommend an unusable path."

This matters because the paragraph teaches the difference
between solving a model correctly and modeling the task
correctly. The current example asserts the opposite
consequence of its stated modeling choice.

## Organization and novice prerequisites

- The accepted order is implemented: examples, growth, and
  emergence in Part I; problems/instances/models, states,
  records/paths, quality/effort, and guarantees in Part II.
- The brief informal problem/instance distinction at lines
  107–113 supports the complexity discussion without making
  Part I depend on Part II. The later treatment explains the
  relationship to complexity classes rather than restarting
  the examples without purpose.
- States and transitions precede records, search trees, and
  node accounting. Node counts now refer to program work
  already explained to the reader.
- Examples introduce feasibility and quality concretely;
  the later guarantees section gives evidence its formal
  role. The return to the zero-imbalance partition is useful
  because it introduces the incumbent and meeting bounds.
- Mathematical prerequisites are appropriate to the stated
  algorithms background. No later algorithm is required to
  follow the current chapter. Later-week links are previews.
- The roughly 4,600 source words exceed the nominal weekly
  target, but Week 1 growth is explicitly permitted. I found
  no reason to cut a necessary explanation merely to meet
  the target. Reading-load judgment remains with Bart.

## Technical and example checks

- The graph remains vertices A–D, edges AB, AC, BC, CD,
  with red/green/blue. The prose, alternative text, caption,
  and graph-coloring figure source agree on the feasible
  assignment A=red, B=green, C=blue, D=red.
- Independently calculated the new repair trace rather than
  relying on its description. With all vertices initially
  red, C=blue minimizes its incident conflicts and reduces
  total conflicts from four to one. B=green then minimizes
  its incident conflicts and reduces the total to zero.
  The final assignment matches the original figure.
- Independently calculated the separate two-vertex example:
  synchronous red/red to blue/blue to red/red has period
  two. Its graph, color set, and simultaneous rule are
  explicitly identified as a separate example, so it does
  not falsely claim a cycle for the sequential trace.
- Partition sums, nonnegativity argument, path costs, total
  assignment counts, geometric node counts, illustrative
  times, budget depths, and hardware-speedup arithmetic are
  sound. Candidate-space size is not presented as a general
  lower bound on solver effort.
- P/NP/NP-completeness do not presume P differs from NP.
  The text separates hardness of a problem from the
  difficulty of one instance and does not infer exponential
  lower bounds from NP-hardness.
- State sufficiency, repeated arrivals, and cycles are
  consistent with the notation page. Duplicate removal is
  conditional on retained continuations/costs; no general
  "visited once" rule is asserted.
- Completeness is separated from termination without a
  solution. The repair examples carry no completeness or
  optimality promise. The interval L ≤ C* ≤ U correctly
  concerns minimization, feasible incumbents, and justified
  lower bounds.

## Citation support and limits

Opened Mitchell's primary author working paper and checked
the selected §2 passage on PDF page 3 (printed page 2):
[Complex Systems: Network Thinking](https://sfi-edu.s3.amazonaws.com/sfi-edu/production/uploads/sfi-com/dev/uploads/filer/67/c4/67c4bcce-7e58-4819-8aed-9a67163dd441/06-10-036.pdf).
The passage supports the local-to-global interaction
perspective used in lines 245–253. The chapter does not
claim that Mitchell analyzes this coloring rule or proves
that finding a solution alone constitutes emergence.
The two small examples are an entry point into trajectory
behavior, not evidence for complex behavior on large cases.
This was a selected-passage check, not full-paper review.

The Minton citation is attached to repair methods rather
than to a new performance claim. Its DOI did not open in
the browser tool during this review; I did not claim a
full-paper check or rely on unrelated search results as
evidence. Existing point-of-use citations for state-space
modeling, the Markov property, and complexity are retained.

## Existing check coverage

`checks/check_examples.py:9`–34 checks 81 assignments,
the pictured feasible coloring, impossibility of completing
A=B=red, partition optimum, binary-tree counts/times,
3²⁰, budget depths, and the millionfold logarithm. Its later
Week 6 repair check concerns another trace; it does not
validate the new Week 1 trace or synchronous cycle.

An ephemeral independent Python calculation in this review
checked minimum-conflict choices, the new 4→1→0 totals,
the final figure assignment, and the separate period-two
cycle. No new test file was written. A small extension to
the existing example check would preserve these new claims
as regressions; it is a useful follow-up, not evidence that
the current explanation is incorrect.

The book check verifies source conventions, title/contents
agreement, generated links, and basic figure presence. It
does not establish mathematical claims or instructional
cohesion. No broad suite was rerun here because the root
agent is handling the build and rendered validation.

## Root resolution

Corrected the required road example to “treats a closed road
as usable.” Also simplified the first use of incident-edge
terminology and reflowed paragraphs. The independent review's
line numbers refer to the reviewed draft before that reflow;
its quoted passages and section anchors identify the findings.
Root independently checked both new finite traces as well.
