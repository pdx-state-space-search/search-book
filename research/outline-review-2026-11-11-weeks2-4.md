# Outline review: Weeks 2–4

Reviewed 2026-11-11. Scope: organization, prerequisites,
teaching load, and continuity in OUTLINE.md. This note
proposes a level of sections **between the chapter and the
existing numbered topics**. The existing topics remain the
bottom-level subsections. It adds no finer outline level.

Only this research note was written. Chapters, OUTLINE.md,
BOOK-NOTES.md, and other project files were not edited. No
commit, push, build, or algorithm test was needed for this
organizational review.

## Materials and governing decisions

Read the authoring skill, its editorial guide and examples,
BRIEF.md, BOOK-NOTES.md, STATUS.md, OUTLINE.md, the notation
reference, Weeks 2–4, relevant passages of Weeks 1 and 5,
and the earlier Week 2 and Weeks 3–5 review reports.

The current request supersedes OUTLINE.md's opening claim
that the numbered items are main sections. The root editor
should correct that introductory description when applying
the newly requested hierarchy.

Keep ten weeks and one chapter per week. Keep CSP/SAT,
backtracking, forward checking, and unit propagation in
Week 2; DFS/BFS/IDDFS and branch-and-bound in Week 3;
UCS/greedy/A* and duplicate handling in Week 4. Do not add
AC-3. No new algorithm topic is needed in these weeks.

The most consequential current feedback is in
[BOOK-NOTES.md](../BOOK-NOTES.md): Week 2 should have CSP
and SAT parts, and Week 3 should distinguish complete from
systematic search under the instructor's stated meanings.
The latter requires an explicit editorial decision; it is
not merely a title correction.

## Main assessment

The allocation is strong and the existing topic sequence
mostly follows the right dependencies. Grouping should make
the teaching purposes visible rather than redistribute
algorithms for visual symmetry.

Three changes have the largest payoff:

- Give Week 2 the requested CSP/SAT division and consider
  forward checking before variable/value ordering, so the
  ordering rules use already demonstrated current domains.
- Give Week 3 two sections: traversal and coverage, followed
  by limits and bounds. State why a temporary cutoff differs
  from a sound proof that a branch is unnecessary.
- Give Week 4 a shared queue foundation, the contrasting
  cost-only and estimate-only methods, then A* and the
  conditions and costs of reliable guidance.

Missing bridges can fit in the new section introductions
or the existing topic descriptions. They do not justify
adding another outline level or more algorithms.

## Week 2: Constraints and SAT

### Proposed two-level organization

The numbers in parentheses are the existing OUTLINE.md
topic numbers, retained here to make the mapping explicit.

**Part I: Constraint Satisfaction Problems**

1. **Describing a constraint satisfaction problem.** (1)
2. **Searching by making and undoing choices.** (2)
3. **Deducing consequences of assignments.** (4)
4. **Choosing variables and values.** (3)

**Part II: Satisfiability**

1. **Expressing constraints as SAT.** (5)
2. **Combining decisions and deductions in SAT.** (6)

The parts do different jobs: Part I builds and solves a
direct constraint model; Part II expresses such a model
in Boolean logic and reuses decision/deduction/backtracking
ideas in that representation. Unequal numbers of subsections
are appropriate. SAT encoding is intrinsically substantial.

### Ordering and prerequisite bridges

The proposed outline already repairs the chapter draft's
largest organizational problem. The draft introduces SAT
syntax and graph encodings before returning to CSP search.
Keeping the CSP treatment together avoids switching from
variables/domains to Boolean clauses and back again before
either approach has a complete story.

The suggested swap of topics 3 and 4 is a teaching preference,
not a technical correction. MRV asks about the sizes of
current domains; LCV estimates the consequences of a choice
for other variables. A forward-checking trace gives both
quantities concrete meaning. The sequence becomes model,
basic search, deductions, then better ordering.

Basic backtracking should initially use a stated fixed order
and direct checks against assigned variables. It can then
incorporate forward checking without depending on an
unexplained domain-maintenance mechanism. Make and undo one
failed choice before introducing trail terminology. Week 8
owns the implementation comparison of copying and trails.

Retaining the original order 1, 2, 3, 4 is also defensible
if topic 1 or 2 already demonstrates current domains and
topic 3 explains its one-step lookahead. It is a weaker
default for novices because it requires predicting the
effects of a method not yet taught. Whichever order is
chosen, do not present MRV/LCV as correctness conditions:
they select work; sound inference can remove work.

Part II needs a brief motivation before Boolean syntax:
the same feasibility task can be encoded for a general SAT
solver. The new variables represent propositions about the
original choices. The encoding must preserve existence of
solutions, and a satisfying assignment must decode to a
valid original answer. This is a representation bridge,
not a new complexity-theory detour.

The existing examples need a local continuity repair when
the sections move. Forward checking currently refers to
the two-color triangle "from the SAT encoding." Once CSPs
come first, introduce that triangle where it is first used
in the CSP part, then explicitly return to it in the SAT
part. Keep the four-vertex, three-color instance as the main
successful example; do not silently change its color set.

### Load and essential coverage

Topic 5 is the most heavily loaded bottom-level subsection
in these weeks. It covers propositional meaning, literals,
clauses, CNF, compact encodings, finite quantified shorthand,
grounding, and both directions of encoding correctness.
The grouping does not by itself make that load disappear.

Preserve the accepted scope, but sequence the explanation
inside that subsection: concrete Boolean statements before
connectives; a small CNF before the general coloring
encoding; actual clauses before compact indexed shorthand.
Treat Tseitin conversion as a short explanation of why CNF
need not cause an exponential representation increase, not
a second major construction competing with coloring. No
new subheadings below this existing topic are proposed.

Topic 6 should include one decision that produces a
propagation conflict and a backtrack, as well as the easy
propagation-only chain already in the draft. Otherwise the
title promises the interaction of choices and deductions
but the worked SAT example shows only deductions. Reusing
the two-color triangle can expose why one branch conflict
does not establish unsatisfiability and why exhausting both
truth choices does.

Keep the practical-SAT connection short. Naming conflict
learning and nonchronological backtracking can orient the
reader, but full CDCL would overload the week's foundational
job. WalkSAT remains in Week 6. AC-3 remains omitted.

### Handoff to Week 3

Close with the common search structure: a current partial
assignment, alternatives still available, deductions, and
restoration. Week 3 generalizes the exploration policy to
state graphs. It should identify CSP backtracking as a
depth-first traversal of partial assignments instead of
teaching recursion and backtracking again from scratch.

## Week 3: Complete and Systematic Search

The title follows the instructor's note. Its terminology
needs the separate treatment below before chapter revision.

### Proposed two-level organization

**Section I: Traversal, Coverage, and Repeated States**

1. **Depth-first search.** (1)
2. **Breadth-first search.** (2)

**Section II: Controlling Exploration with Limits and Bounds**

1. **Depth limits, cutoff, and failure.** (3)
2. **Iterative deepening.** (4)
3. **Branch-and-bound.** (5)

This preserves all topic headings and their order. Section I
compares two traversal policies and their retained state.
Section II examines two different reasons to stop exploring
a branch: a chosen resource limit and evidence that its
answers cannot improve the incumbent.

The second section is coherent if its introduction states
that distinction explicitly. A depth cutoff leaves a
question unresolved; iterative deepening revisits it under
a larger allowance. A valid optimization bound can remove
a branch permanently while preserving the required answer.
Do not let the common word "bound" imply identical logic.

A three-section alternative can isolate branch-and-bound
as an optimization capstone. That would give it a section
with one subsection; it is reasonable if the eventual worked
example grows substantially, but is unnecessary now. The
two-section organization is the stronger default.

### Terminology: preserve the instructor's distinction

BOOK-NOTES.md asks to distinguish search that is complete
— "will eventually examine all states" — from systematic
search — "will examine each state at most once."

The current sources use different meanings. Week 1 defines
complete as eventually finding a solution when one exists;
Week 2 repeats that solution-finding definition. Week 3
opens by defining systematic search through its account of
alternatives, allowing deliberate repeated work. The new
outline must flag this conflict rather than silently
substituting the current prose's definitions for the note.

Three details need to be settled explicitly:

- **What counts as examining a state?** A duplicate can be
  generated or checked and then discarded without expansion.
  At-most-once expansion is different from at-most-once
  generation or even at-most-once comparison. Week 1 already
  distinguishes states, records, generation, and expansion.
- **What is the scope of eventual coverage?** All reachable
  states, all relevant possibilities, and all paths are
  different sets. A goal-returning algorithm normally stops
  early; an optimization algorithm may soundly prune states.
  Neither literally examines every state on every run.
- **How are coverage and at-most-once behavior reported?**
  They are separate properties of a specified algorithm and
  duplicate policy, not properties supplied by an algorithm
  name or by the chapter title.

For example, with examination understood as expansion,
finite-graph DFS with a global reached set can cover each
reachable state once if allowed to exhaust the graph.
Path-local DFS can revisit a state through different routes.
IDDFS deliberately expands upper-level states again across
iterations. Depth-limited search can avoid repeated expansion
yet omit deeper states. Branch-and-bound can establish an
optimum without examining the states in pruned subtrees.

These examples make the requested distinction useful; they
also show why the text cannot label every algorithm in the
chapter systematic under the at-most-once definition.
Week 4's admissible but inconsistent A* may reopen states,
and Week 5's IDA*/RBFS deliberately regenerate work. Their
descriptions must use the same terminology decision.

Recommendation: retain the requested distinction as an
explicit teaching issue and resolve the counted operation
and coverage qualification before rewriting definitions.
A chapter about completeness and systematicity can include
methods that sacrifice at-most-once processing to save
memory. Do not rename repeated node occurrences as distinct
states merely to make a method meet the definition.

### Missing bridges and overloaded responsibilities

The first section needs a short opening that connects Week 2
to graphs: a partial assignment is one kind of search state;
other models can reach the same state by different paths.
Recall the frontier as generated work still eligible for
expansion, and distinguish it from the reached set and the
active path. These are bridges, not new peer subsections.

Use the same small directed graph for DFS and BFS and draw
it before tracing either. The existing S/A/B/C/G graph is
adequate. Fix successor order and show both the pending
alternatives and returned route. This directly explains
why low retained search memory, exhaustive coverage, and
minimum path length are separate claims.

Cycle policy belongs inside DFS and BFS. It is not enough
to place a general warning in the introduction. A global
reached set consumes memory and can suppress repeated states;
a path-local test prevents a cycle on the current route
while allowing arrivals through other routes. Section I's
comparison should make that tradeoff visible.

The earlier review's depth-limited specification gap remains
relevant. Topic 3 must explain how child outcomes combine:
one cutoff can prevent an overall failure result even when
other branches fail. Distinguish an actual eligible
continuation excluded at the boundary from a dead leaf.
The IDDFS stopping argument depends on this result contract.

Topic 4 should make deliberate regeneration explicit, not
bury it in the complexity formula. Preserve the contrast
between a branching tree, where late layers dominate, and
a chain, where repeated prefixes incur quadratic work.
This prepares Week 5's memory tradeoffs without introducing
IDA* prematurely.

Branch-and-bound needs an actual instance whose bound the
reader can calculate. Start with a bound already justified
by the objective: accumulated nonnegative path cost, or a
simple number-partitioning bound using a familiar model.
The current unexplained values 12, 9, and 10 cannot carry
the new proof technique. Week 1 already introduced feasible
incumbents and global lower bounds; recall them briefly,
then add the genuinely new idea: a bound for the completions
of one branch.

Keep full heuristic design in Week 5. Week 3 can mention
that a remaining-cost bound can strengthen a path bound,
but should not require admissibility terminology or a
construction not yet taught to understand basic pruning.
The finite example should establish the main mechanism
before the infinite-space qualifications.

### Handoff to Week 4

The useful unresolved problem is that shallowest paths may
be expensive. Week 4 will select among frontier entries
using path cost and estimates. Repeat the obligation that
discarding an arrival requires the retained information to
cover its useful futures. The depth-limited example, where
a shallower arrival has more remaining allowance, prepares
the weighted example, where a cheaper arrival matters.

## Week 4: Best-First Search

### Proposed two-level organization

**Section I: Priorities and Competing Arrivals**

1. **Priorities for choosing the next path.** (1)
2. **Retaining and improving arrivals.** (2)

**Section II: Searching by Cost or Estimated Proximity**

1. **Uniform-cost search.** (3)
2. **Greedy best-first search.** (4)

**Section III: A* and the Conditions for Useful Guidance**

1. **A* and admissible estimates.** (5)
2. **Consistency, finalization, and reopening.** (6)
3. **The practical cost of guidance.** (7)

The first section gives the common mechanism. The second
contrasts paying attention only to cost already incurred
with paying attention only to estimated cost remaining.
The third explains their combination, the additional
condition permitting finalization, and the practical price
of acquiring and retaining guidance. No reordering is needed.

The final subsection also synthesizes the earlier policies;
its location under A* should not imply that queue storage
or heuristic overhead matters only for A*.

### Ordering and prerequisite bridges

The first subsection should introduce a named route instance
and an interpretable remaining-cost estimate before showing
the g/h/g+h comparison. Give the estimate a simple reason,
such as a visibly cheaper relaxed route. Do not begin with
h*, admissibility, and consistency as three unexplained
formal definitions, as the current chapter draft does.

Week 5 owns general heuristic construction. Week 4 still
needs one concrete explanation of where its example's
estimate comes from. That is a prerequisite bridge rather
than an allocation change.

Topic 2 is the other potentially overloaded subsection.
Best-known costs, strict improvement, stale entries, parent
records, and the common queue loop are difficult if shown
before any observable problem demands them. Begin with a
state reached once expensively and later cheaply. Show the
two queue records and the changed best-known cost, then
give the loop. Correctness requires retaining improvements;
lazy insertion and stale-entry skipping are one realization.
This keeps mechanics connected to their purpose.

Keeping this topic before UCS is useful because the UCS
proof depends on handling improvements correctly. Moving
all duplicate handling after the three algorithms would
make their guarantees provisional and force repetition.
The new section introduction should instead ensure that
the common mechanism has a concrete motivating trace.

UCS then establishes the first accepted-goal argument using
minimum g. Greedy supplies a focused counterexample showing
that an informative or even admissible h cannot compensate
for ignoring path cost. A* combines the two after each has
an intelligible role. This order is pedagogically sound.

Define admissibility at topic 5, when the lower-bound proof
needs it. Define consistency at topic 6, when the question
becomes whether the first expansion can be final. The
student should first see an A* policy that safely permits
reopening, then see why consistency makes reopening
unnecessary. Treating consistency as a prerequisite for
all A* would misstate the intended algorithm.

At topic 6, define finalization plainly: a promise not to
expand the state again. A reached state, an enqueued record,
an expanded state, and a finalized state are not the same.
The current reopening example is a strong illustration to
preserve. One stale non-goal record actually being skipped
would make topic 2's bookkeeping observable as well.

### Load, overlap, and the next week

Avoid repeating three full formal proof templates. UCS can
establish the retained-prefix reasoning; A* can explicitly
reuse it with a justified g+h bound. Greedy shows which
guarantee does not follow from its selection rule. Each
algorithm still needs its own assumptions close to the claim.

Week 3 owns depth versus cost, the basic global/path-local
duplicate distinction, and the meaning of an incumbent.
Week 4 owns cost improvements, stale entries, goal removal,
and reopening. Week 5 owns general relaxation, abstraction,
pattern databases, safe combination, and reduced-memory
algorithms. These boundaries prevent repeated introductions.

Topic 7 should define stronger admissible estimates and
compare evaluation work, expanded records, re-expansions,
and memory. It should motivate Week 5 rather than begin a
second heuristic-construction lesson. In particular, a
passing mention of maximum combination should point forward;
its explanation and cost-partitioning counterpart belong
together in Week 5.

Week 8 later studies implementation measurement in depth.
The present chapter still needs enough accounting to explain
why fewer expansions need not mean less elapsed time, and
why a frontier can exhaust memory. It does not need a full
benchmarking method or detailed priority-queue engineering.

## Decisions for the root editor

1. Use the requested intermediate section layer. Keep every
   existing topic as a bottom-level subsection.
2. Give Week 2 CSP and SAT parts. Prefer order 1, 2, 4, 3
   in CSPs, with the original order still a viable choice
   if current-domain mechanics are introduced earlier.
3. Keep Week 3's topic order in two sections, separated
   after BFS. Explicitly distinguish cutoff from pruning.
4. Resolve the complete/systematic vocabulary across Weeks
   1–5; do not silently overwrite the instructor's meanings.
5. Keep Week 4's order and group topics 1–2, 3–4, and 5–7.
6. Strengthen examples and transitions inside the existing
   topic descriptions. No new peer subsection or algorithm
   is necessary for these three chapters.
