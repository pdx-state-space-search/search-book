# Outline review: Weeks 5–7

Reviewed 2026-11-11. This is an organizational review of
OUTLINE.md, not authorization to revise the chapters.

## Scope and interpretation

The current numbered topics are the bottom-level
subsections. The task is to interpolate meaningful sections
between those topics and each chapter. The proposals below
add that parent level and reorder existing topics; they do
not add finer subdivisions below them. Numbers in parentheses
identify the original topic numbers in OUTLINE.md.

I read the authoring skill and editorial guide, BRIEF.md,
BOOK-NOTES.md, STATUS.md, the outlines, Weeks 5–7, relevant
adjoining material, and the prior Weeks 3–5 and Weeks 6–8
reviews. The current chapter prose is evidence of teaching
needs, not an approved organization. In particular,
OUTLINE.md already remedies several older review findings.

Keep all three weeks, their topic coverage, and their
existing chapter identities. No additional application unit,
exercise sequence, or algorithm survey is needed.

## Highest-value decisions

1. Give Week 5 two sections: constructing lower bounds, then
   searching with less memory. Preserve its current topic
   order, but keep additive pattern databases out of the
   abstraction introduction until cost partitioning has
   been established.
2. Move Week 6's landscape topic immediately after its
   candidate/neighborhood topic. Define basic improvement
   and stalling there before repair and escape policies
   depend on them. Keep full incremental evaluation after
   concrete repair traces, before the escape discussion.
3. Give Week 7 separate sections for producing answers and
   assessing outcomes. Put evaluation before restart
   analysis so targets, budgets, failures, and sampling
   units are established before probability calculations.
4. Assign clear homes to recurring ideas. Week 6 introduces
   best-feasible retention and restart mechanisms; Week 7
   defines anytime behavior and analyzes observed outcomes;
   Week 10 adds certified optimality gaps.

## Week 5: Heuristics and Limited Memory

The current six topics contain two distinct, well-connected
teaching jobs. Topics 1–3 explain where justified estimates
come from. Topics 4–6 explain how a search can retain less
information while preserving the relevant lower-bound
reasoning. A two-section chapter makes that transition
visible without splitting the week.

### Recommended two-level organization

1. **Constructing lower bounds**
   - Relaxation as a source of lower bounds. (1)
   - Abstraction and pattern databases. (2)
   - Combining heuristic estimates. (3)
2. **Searching with less memory**
   - Trading memory for repeated work. (4)
   - IDA*: repeated cost-bounded exploration. (5)
   - Recursive best-first search. (6)

The first section's result is a usable, justified estimate
whose evaluation and storage costs are understood. The
second section uses that estimate while changing what the
search remembers. Topic 4 is the conceptual bridge; it
should introduce the loss of detailed frontier information
before either memory-saving algorithm appears.

### Ordering and prerequisite findings

The outline improves on the current prose, which teaches
combination before giving a concrete pattern database
(`src/05-heuristics.md:64` and `:99`). Preserve the new order.
However, the meaning of “pattern databases” in topic 2 must
be constrained. Start with one abstraction: concrete state,
abstract state, allowed moves, abstract goals and costs,
then an actual exact table lookup. That example needs its
own admissibility argument. It does not need addition yet.

Place additive databases with topic 3's cost partitioning.
The current prose moves from an ordinary abstract table to
zero-cost background moves (`:120`–`:142`). Those costs only
make sense after the reader knows why an action's charge is
being divided among components. The revised order should
not silently teach that machinery before its justification.
Use Week 4's uniform-cost search for mixed abstract costs;
do not introduce another shortest-path algorithm solely to
construct the table. Ordinary unit-cost tables can use BFS.

Keep the relaxed-optimum distinction early. A feasible
answer to a relaxed problem is generally an upper bound on
that relaxed optimum; the chapter needs a lower bound on
the original objective. This is a foundational direction
of inference, not a technical caveat to postpone until the
memory algorithms.

IDA* needs two explicit reminders: Week 3's depth-limited
traversal and minimum-exceeded cost thresholds from this
week's lower-bound view. A cost threshold is not a depth
limit, and “try again with a larger bound” is not a random
restart. The next-bound calculation, exhaustion result,
path-cycle policy and memory assumptions must stay together
inside its existing topic.

RBFS is the chapter's hardest conceptual step. Its topic
needs a real small tree, not merely stipulated changing
bound values. Show which descendants are forgotten, which
sibling summaries remain, and why returning to a branch
requires regeneration. Compare it with IDA* only after that
operation is visible. A carefully chosen shared tree could
reduce example overhead, but forcing identical traces is
less useful than making regeneration observable.

### Scope and overlap

Week 4 owns why g+h supports A* and how improved arrivals
are handled. Week 5 should recall that contract, then teach
construction and retention. It should not repeat a full
A* proof or repeat heuristic-strength discussion as an
independent survey.

The table storage in topic 2 and search storage in topic 4
must be combined in the eventual accounting. “Linear search
memory” does not make a large pattern database disappear.
Week 8 can deepen representation and measurement; Week 5
must already state which retained structures are counted.

Do not confuse abstraction with Week 8's state equality or
canonicalization. An abstraction deliberately forgets
distinctions to produce an optimistic problem. An exact
state identity must preserve the distinctions needed for
the actual problem's future behavior.

The current six-topic load is already substantial. The
highest-value additions are the missing concrete database
and RBFS traces, not further heuristic or memory-bounded
algorithm families. Keep the scheduling-bound connection
as a brief forward reference to Week 8.

## Week 6: Local Search and Repair

This chapter changes the meaning of a search state and the
evidence retained by a search. Week 5 sometimes regenerates
forgotten work while maintaining lower-bound reasoning.
Week 6 follows candidate changes without maintaining full
coverage. That boundary should be explicit near the start;
small memory alone does not distinguish the two approaches.

### Recommended two-level organization

1. **Candidates and landscapes**
   - Candidates, objectives, and neighborhoods. (1)
   - Local minima, plateaus, and barriers. (4)
2. **Searching and repairing candidates**
   - Local improvement and constraint repair. (2)
   - SAT repair and WalkSAT. (3)
   - Evaluating changes incrementally. (5)
   - Escaping and remembering useful answers. (6)

The first section explains the space being searched and
what improvement can and cannot reveal. The second applies
concrete policies, reduces their move cost, and explains
how to continue when improvement stalls. Unequal topic
counts are preferable to inventing an arbitrary third
section joining efficiency and escape solely to obtain
three equal pairs.

### Ordering and prerequisite findings

Move the landscape topic before min-conflicts and WalkSAT.
The current prose and outline use “sideways,” “stalled
regions,” and escape before their main landscape treatment.
The earlier neighborhood definition is not enough to
explain the difference among a local minimum, a plateau,
and a genuine barrier. The known number-partitioning
instance can give these terms concrete meanings first.

Basic descent needs a clear home, although it does not
need another bottom-level topic. Inside topic 4, explain
the simple baseline of accepting a strictly improving
neighbor until none is available. This makes a local
minimum an operational limitation rather than a geometric
word. Distinguish inspecting all neighbors from sampling
some: a stalled sampled run has not certified local
optimality. The current chapter's final guarantee discussion
(`src/06-local.md:315`) should be distributed into these
relevant topics rather than lost when the outline is used.

Do not make min-conflicts synonymous with global steepest
descent. It selects a conflicted variable and a preferred
value; its scope of selection and tie policy determine the
actual moves. A complete stated policy needs to say whether
the current value is eligible, what to do on ties, and when
to stop. WalkSAT likewise needs one explicitly identified
variant if the aim is an executable policy rather than a
family description. Landscape vocabulary can then explain
its sideways or worsening choices without a forward gap.

Keep incremental evaluation after the repair examples.
The algorithms can initially score their small candidates
by a full recount. Once the reader has seen actual moves,
the delta formulas answer a motivated cost question. Moving
the whole three-example delta treatment ahead of the first
repair algorithm would delay the chapter's central behavior
with implementation detail. Keeping it before escape also
prepares Week 7's many stochastic proposals and its warning
that equal iteration counts need not mean equal effort.

The signed partition difference and the score delta must
remain distinct. The difference between group sums records
information needed for updates; the objective is its
absolute value. Week 7's acceptance rule uses the change
in objective, not the signed group difference itself.

The tour remains a compact representation example, not a
new application unit. The outline already recognizes the
missing closed-tour definition, but placing it in topic 1
would leave an unfamiliar model waiting through several
other topics. Prefer familiar coloring and partitioning
examples there, then introduce the closed-tour task in
topic 5 immediately before its first substantive use.
Remove or defer earlier unexplained references to tour
moves. Before the 2-opt delta, identify the removed edges,
reconnection and reversed segment. Only then does the
symmetry condition explain why interior edge costs need
no change. Week 7 may reuse this established representation
for its crossover counterexample.

### Scope and overlap

The existing coloring example also appears in Week 1.
Week 6 should restore that familiar instance, then add
initialization, selection, tie handling, stopping and the
information retained. Repeating only the successful
two-move trace would not justify a full later treatment.

Keep the main escape choices here: restart from a new
candidate, remember recent moves, or enlarge the move set.
Show their relation to the earlier obstacle. A plateau
can have an exit reachable by sideways moves; a genuine
barrier requires worsening somewhere along every route
to a better region under the stated neighborhood. The
partition example supports the stronger claim only with
the small plateau argument identified in the earlier
review. A single displayed uphill path does not prove
that uphill motion is necessary.

Introduce best-feasible retention before a policy can lose
an earlier useful answer. The current candidate may become
worse, and a low-penalty infeasible candidate is not an
answer. These are the mechanics Week 7 will name as anytime
behavior. Avoid a full anytime survey here.

Retain the nuanced conclusions. A successful SAT repair
certifies satisfiability; an unsuccessful bounded run does
not certify unsatisfiability. A zero partition imbalance
can certify optimality using the known lower bound zero.
Thus “local search cannot prove optimality” would be too
strong; the central limit concerns coverage and what a
stalled positive-score run establishes.

## Week 7: Stochastic Search and Anytime Optimization

The chapter has a natural distinction between defining a
search policy and interpreting evidence about that policy.
The current six-topic order alternates policy material
with probability analysis, then leaves experimental
definitions until last. Those definitions should precede
the quantitative restart model that depends on them.

### Recommended two-level organization

1. **Producing answers under a budget**
   - Keeping an answer available. (1)
   - Simulated annealing. (2)
   - Populations and evolutionary search. (4)
   - Hybrids and restricted exact search. (5)
2. **Evaluating outcomes and expected effort**
   - Evaluating stochastic outcomes. (6)
   - Restarts and expected effort. (3)

The second section starts with what an experiment observes
and concludes with a quantitative model that uses those
observations. Restart mechanics have already been taught
in Week 6, so this reorder does not postpone an algorithmic
prerequisite. It moves only the reliability/cost analysis.

The alternate order, restart analysis then evaluation, is
also workable if it better fits the whole-book synthesis.
In that case define the target and budget in the anytime
setup, and define one capped trial, its cutoff-dependent
success probability, and the meaning of failure before
the restart formulas. Do not silently depend on definitions
still waiting in the evaluation topic. The key requirement
is the dependency, not a mandatory numerical topic order.

### Ordering and prerequisite findings

Keep the anytime definition first. It provides the output
contract for the policies that follow: after finding a
feasible incumbent, interruption can return the best one
retained so far. Before feasibility, that promise is not
available. Monotone incumbent quality neither promises
future improvement nor supplies a global optimality proof.
Anytime behavior is not inherently stochastic; the earlier
branch-and-bound algorithm supplies a useful connection.

Simulated annealing should remain the first substantial
new method because it directly answers Week 6's barrier
example. Preserve the outline's plan for one fully
specified finite run. Proposal selection, the acceptance
test, accepted-state updates, best-answer retention,
temperature schedule and stopping budget must describe one
algorithm. A table of acceptance probabilities alone
does not do this. Include a rejection so the distinction
between proposing and changing the candidate is visible.

A compact population example should show the complete
selection/variation/replacement cycle. Avoid turning the
topic into a catalog of operators. Representation validity
and retaining a feasible answer are essential; the known
tour counterexample can illustrate why naive crossover is
invalid without requiring another long tour instance.

Restricted exact repair already has prerequisites in
Weeks 2–3 and Week 6's compound neighborhoods. Use those
connections explicitly. The current prose uses freeing
three scheduling tasks (`src/07-stochastic.md:201`) before
Week 8 has defined its scheduling model. Reuse partitioning
or coloring for the concrete restricted subproblem, or
keep the scheduling reference purely illustrative. The
point is that exactness holds within the selected region,
not that the outer process has covered every region.
Preserve the old feasible candidate if a limited repair
does not improve it or cannot finish.

The evaluation topic should establish both experiment
types: quality at a deadline and time to a specified
target. An optimization run does not have an unambiguous
“success” event until a target is stated. Feasibility,
reaching a quality threshold and proving optimality are
different targets. State instances, seeds, measured work,
cutoffs and failures before using a symbol p for success.

Then restart analysis can explicitly condition on one
instance, a fixed target, a start distribution and a
capped trial policy. Explain independent repeated trials
before multiplying failure probabilities, and distinguish
fixed trial duration from outcome-dependent duration.
The capped policy's unsuccessful trial is a failure for
that policy; its cutoff is a censored observation about
the uncapped runtime. Evaluation first gives these terms
a purpose before the formulas need them.

Estimated success probabilities are evidence, not exact
inputs delivered by the algorithm. A restart cutoff that
looks best after tuning should not be reported as if it
had been fixed before evaluation. Keep the model's
assumptions and the empirical selection procedure close.
No general probability or statistical-inference unit is
needed; derive only what the existing restart topic uses.

### Scope and overlap

The principal scope risk is giving full survey treatment
to annealing, evolutionary methods, iterated local search,
large-neighborhood search and experimental statistics in
one week. Use annealing for the fullest policy/trace;
give populations one compact generation and hybrids one
restricted-region example. Preserve the evaluation work
instead of shrinking it to a closing checklist.

Week 6 owns the objective/neighborhood and local-delta
derivations. Week 7 uses their deltas and counts their
costs. Week 8 owns profiling and representation choices.
Repeated caveats that “fewer moves can still cost more”
should point back to that common accounting rather than
reintroducing it as a new topic each week.

Week 7 owns the anytime definition; Week 10 should recall
it while adding a maintained lower bound and certified
gap. “Current versus best” is a mechanism, “anytime” is an
output property, and a gap certificate is additional
evidence. Keeping those jobs separate prevents three
near-identical introductions and prevents treating a
good stochastic answer as an optimality certificate.

## Validation and limits

Every existing topic 1–6 appears exactly once in each
proposed chapter outline. Topic coverage and week allocation
are preserved; only the parent groupings and ordering are
proposed. The identified missing explanations belong inside
the existing topics, not in a third level of subsections.

This review did not change OUTLINE.md, chapter sources,
BOOK-NOTES.md, or the brief. It did not introduce technical
claims needing new experimental validation, recheck the
older finite calculations, or run a book build. The older
reviews provide the recorded technical checks; the present
review assesses teaching dependencies and organization.
