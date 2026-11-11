# Week 1: working outline

Updated for discussion, 2026-10-28. The top-level organization
is accepted: one Week 1 chapter containing Part I and Part II.
Both outline levels are accepted for rewriting. Bart moved
Problems, Instances, and Models to the start of Part II; the
examples supply a brief informal problem/instance distinction
for Part I. The rewrite keeps the chapter file and week mapping.

## Assessment before the rewrite

The preceding roughly 4,000-word draft had two overlapping
teaching jobs: motivate search, and establish a language for modeling
and assessing it. Its top-level order was exploration;
models/states/instances; growth; quality/effort; states/records/
paths; implicit generation; guarantees; transition; readings.

The split between models and later state mechanics interrupts
the representation discussion. Node counts appear before the
full explanation of nodes as program records. Objective value,
feasibility, optimality, and evidence return in several places
without a clear main home. The examples occupy about 850
words and the growth/complexity block about 1,000; adding
another philosophical section to this sequence would increase
the need for stronger organization.

The accepted organization uses two named parts with distinct
purposes inside the same Week 1 chapter. This requires
regrouping the existing sections, rather than cutting the
current file at its midpoint.

## Part I: Why Search?

1. **Three problems, three kinds of answer**
   - **Graph coloring: a feasible assignment.** Map regions
     to vertices, state the edge rules, and check a coloring.
   - **Number partitioning: a better candidate.** Define
     imbalance and compare the two existing partitions.
   - **Pathfinding: a route and its cost.** Compare the direct
     road with the cheaper two-road route; the answer includes
     the path, not just the destination.
2. **Combinatorial growth and practical limits**
   - **Counting complete candidates.** Define size measures
     before counting colorings or binary choices.
   - **Growth against a resource budget.** Explain the
     practical knee and why hardware and selective exploration
     change which instances fit a budget.
   - **NP-hard problems and useful instances.** Introduce
     decision questions, P, NP, NP-completeness, and NP-hardness
     compactly; distinguish general hardness from one run's
     difficulty without assuming P differs from NP.
3. **Emergent behavior from simple search rules**
   - **Local changes and global patterns.** Use repeated
     coloring repairs to connect simple choices and their
     interactions with the behavior of the whole search.
   - **Understanding the resulting behavior.** Examine
     progress, stalls, and cycles; distinguish an observed
     pattern from a guarantee about all runs or instances.

## Part II: Modeling and Assessing Search

4. **Problems, instances, and models**
   - **A problem and one of its instances.** Identify varying
     parameters and the particular data fixed in each example.
   - **What the model specifies.** Choices, constraints,
     desired answers, and objectives, using the same examples.
   - **How a model can miss the intended task.** Explain
     simplifying assumptions and why solving the model is
     useful only when it captures the relevant requirements.
5. **States and possible changes**
   - **Choosing what a state represents.** Contrast partial
     assignments with complete candidates and route states.
   - **Retaining enough information.** Use fuel and relevant
     history to motivate sufficient states and the Markov
     property.
   - **Generating possibilities on demand.** Explain legal
     transitions, implicit spaces, and the obligation to
     generate the intended possibilities.
6. **States, records, and paths**
   - **What the program stores and processes.** Connect
     candidate records and parent links to paths, state graphs,
     and search-tree drawings.
   - **Repeated arrivals and cycles.** Show different records
     for one state, when arrivals can be merged, and why a
     finite graph can still yield infinitely many paths.
7. **Answer quality and search effort**
   - **What an objective measures.** Distinguish partition
     imbalance, route cost, and the work spent discovering them.
   - **Counting the program's work.** Explain generated and
     expanded records, duplicates, and regular-tree counts;
     place the existing node-budget figure here.
   - **From counts to time and memory.** Explain the counting
     convention, machine independence, polynomial per-node
     work, and the costs hidden by a single expansion count.
8. **Evidence and guarantees**
   - **A feasible answer and a best answer.** State what a
     checked coloring or route establishes and what optimality
     additionally requires.
   - **Completeness, termination, and failure.** Distinguish
     finding an existing answer from finishing without one;
     connect guarantees to the stated space and search policy.
   - **Bounds and an optimality certificate.** Use the
     existing partitions to introduce incumbents and
     L ≤ C* ≤ U, then show why meeting bounds proves optimality.

Use a short opening to introduce the chapter's two purposes.
Close with the modeling and evidence questions that lead into
Week 2, followed by one short Further reading section for the
whole chapter, linked to the shared bibliography. These are
framing passages, not additional conceptual sections.

## Where the existing material goes

| Current material | Proposed home |
| --- | --- |
| Opening timetable discussion | Condense into the opening; use coloring for the developed construction/repair comparison. |
| Three illustrated problems | Part I, section 1. |
| Model/instance definitions | Part II, section 4. |
| Growth arithmetic and complexity classes | Candidate counts and complexity in Part I, section 2; full tree counts and node-budget figure in Part II, section 7. |
| State representations and model fidelity | Part II, section 5; retain model fidelity in Part II, section 4. |
| Records, paths, graph/tree distinction, repeats | Part II, section 6. |
| Implicit generation and finite/infinite spaces | Integrate with states and transitions; connect cycles to records/paths. |
| Quality/effort and node-count accounting | Part II, section 7. |
| Answers, bounds, guarantees, algorithm transition | Part II, section 8. |
| Further reading | One short chapter-end list, using the existing shared bibliography. |

## Emergent behavior: intended treatment

Use emergence for system-level patterns arising through
interacting simpler rules. Melanie Mitchell's
[Complex Systems: Network Thinking, §2](https://sfi-edu.s3.amazonaws.com/sfi-edu/production/uploads/sfi-com/dev/uploads/filer/67/c4/67c4bcce-7e58-4819-8aed-9a67163dd441/06-10-036.pdf)
provides a candidate source for that framing. The selected
introductory passage was checked; this is not a full-paper
review or a new student reading assignment.

For this book, I propose using repeated local recoloring as
an entry point: each change affects neighboring conflicts,
and their interaction shapes the overall trajectory. The
interesting behavior includes coordinated solutions, stalls,
and cycles. A short illustrated example can connect simple
mechanisms to behavior that needs observation and explanation.
Finding an answer alone should not be the definition of
emergence, and emergence supplies no success guarantee.
This is a proposed application of the framing to our course,
not a claim that Mitchell analyzes our coloring solver.

The chapter can then motivate two complementary questions:
how much computation a space demands, and what behavior a
search mechanism produces as it interacts with that space.
Part II supplies the representation and evidence
needed to investigate both questions.

## Organizational consequences

Part I has three main sections and Part II has five.
The eight sections and their 22 subsections give the accepted
organization for the rewrite. The part
labels group that outline within one weekly chapter.

Part I counts complete candidates before discussing growth.
Part II introduces program records before full tree-node
counts and their budget figure. This ordering avoids making
an unexplained node count carry the motivation. The later
work accounting extends the earlier candidate count rather
than repeating its explanation.

Examples introduce feasibility, quality, and paths concretely;
section 8 gives guarantees their main explicit treatment.
Keep reminders brief, preserve the complexity qualifications,
and defer full formal problem descriptions to an algorithms
text. The emergence section supplies a philosophical thread,
with one familiar example rather than a new topic survey.

The chapter remains Week 1. Preserve later week labels,
chapter numbering, and the existing chapter file. No physical
split or link migration is needed. The authoring pass implements this accepted outline; further
changes follow instructor review.
