# Chapter outlines: Weeks 2–10

Proposed organization for instructor review, 2026-11-11.
Each week remains one chapter. The hierarchy is now chapter,
section, then topic subsection: the new section headings group
the existing numbered topics, which remain the bottom level.
There are no finer subdivisions below those topics.
Week 1's accepted outline is recorded in
[its working outline](research/week1-outline-2026-10-28.md).

All 54 original topics are retained. The additions below
strengthen anytime search, inadmissible heuristic guidance,
learning from failure, discrepancy search, beam search, and
symmetry reduction. Some topics move within their chapter,
and their descriptions clarify missing prerequisites,
examples, and limits. Week 10 also regains the short closing
synthesis already present in its draft. These are proposals
for the next rewrite; the chapter sources have not been
reorganized in this pass.

Each method's treatment should connect a concrete example,
its operation, its guarantees and assumptions, and its costs.
Use the existing examples across subsection boundaries rather
than repeatedly introducing new problems. Citations belong
beside the claims they support. A short annotated Further
reading section closes each chapter; it is omitted from the
conceptual outlines below. The bibliography remains separate.

## Week 2: Constraints and SAT

Purpose: describe choices and restrictions, then show how
search and deductions cooperate in CSP and SAT solvers.
Keep each representation's modeling and solving story together.

### Part I: Constraint satisfaction problems

Develop a direct constraint model, solve it with a fixed
choice order, then improve deductions and ordering. Teach
current domains before using their sizes to choose a variable.

1. **Describing a constraint satisfaction problem.** Develop
   variables, domains, constraints, partial assignments, and
   solutions through our four-vertex graph coloring instance.
   Distinguish an unassigned variable from one whose current
   domain has no possible value.
2. **Searching by making and undoing choices.** Explain
   backtracking with a fixed variable/value order, checking
   assigned constraints, rejecting a failed branch, and
   restoring its changes. Establish finite exhaustive search
   before adding inference or ordering heuristics.
3. **Deducing consequences of assignments.** Work through
   forward checking, shrinking domains, and branch failure.
   Introduce the two-color triangle here before reusing it
   in SAT. Distinguish sound exclusion from examining every
   state, and explain why undone choices restore domains.
4. **Choosing variables and values.** Use those current
   domains to motivate most-constrained first and
   least-constraining first, including degree ties and the
   work required to score a choice. Separate promising
   ordering from sound reasons to remove possibilities.

### Part II: Satisfiability

Encode the same feasibility task for a Boolean solver, then
reuse the ideas of decisions, deductions, and backtracking.
This is the book's main SAT foundation; WalkSAT comes in Week 6.

1. **Expressing constraints as SAT.** Introduce propositions,
   literals, clauses, and CNF through concrete coloring rules.
   Show actual clauses before finite quantified shorthand
   and its grounded expansion. Justify both directions of
   the encoding and explain how a satisfying assignment
   decodes to a coloring. Keep auxiliary variables and compact
   equisatisfiable CNF focused on avoiding encoding blowup.
2. **Combining decisions and deductions in SAT.** Explain
   unit propagation, conflicts, branching, and backtracking.
   Trace a decision that forces deductions and then fails;
   contrast one failed branch with exhaustion proving
   unsatisfiability. Connect briefly to practical SAT solving
   without developing a full clause-learning solver.

3. **Learning from failure.** Derive a nogood from one failed
   branch and explain why it excludes other failing choices.
   Trace a learned clause, a backjump over an irrelevant
   decision, and the resulting propagation. Connect this to
   dependency-directed and dynamic backtracking, distinguishing
   jumping back from preserving independent assignments.
   Use Ginsberg's dynamic backtracking as a reading connection;
   keep full CDCL implementation outside the chapter.

## Week 3: Complete and Systematic Search

Purpose: account for alternatives and explain how exploration
order changes coverage, answer quality, and memory. Complete
means eventual examination of every state; systematic means
examination of each state at most once. Distinguish continued
traversal from early stopping and from sound pruning.

### I. Traversal, coverage, and repeated states

Connect Week 2's partial-assignment search to general state
graphs. Recall the frontier, active path, and reached set.
Distinguish finding a goal, exhausting alternatives, and
processing a state at most once before comparing methods.
Use one small graph and a stated successor order throughout.

1. **Depth-first search.** Follow one branch and retain the
   alternatives needed to return. Compare path-local cycle
   checks with a global reached set, distinguishing states
   from repeated path records. Explain finite and infinite
   coverage and the storage behind low-memory claims.
2. **Breadth-first search.** Trace queue order, parent records,
   and duplicate handling on the same graph. Establish
   minimum transition count and the equal-positive-cost
   condition for minimum cost. Make goal-test timing explicit
   when counting generated records and frontier storage.

### II. Controlling exploration with limits and bounds

A depth cutoff leaves work unresolved; iterative deepening
returns to it. An objective bound can prove that a branch
need not be explored to obtain the required optimum. Keep
these reasons for stopping a branch distinct.

1. **Depth limits, cutoff, and failure.** Specify what a
   bounded traversal excludes. Explain how child outcomes
   combine into a solution, complete failure, or a cutoff,
   including dead ends at the boundary. Show why an earlier
   deep arrival does not necessarily dominate a later shallow
   one with more remaining depth.
2. **Iterative deepening.** Build on that result contract to
   find shallow answers with modest retained memory. Make
   deliberate repeated work explicit, comparing branching
   trees with chains. State the conditions for eventual
   success and for terminating with complete failure.
3. **Limited discrepancy search.** Reuse Week 2's value-ordering
   advice in a small binary decision tree. Count departures
   from the preferred choice and trace increasing discrepancy
   limits, including one early wrong recommendation. Compare
   with depth limits and ordinary backtracking. State the
   finite-tree conditions for eventual all-state coverage and
   identify repeated examinations across iterations. No
   cost-to-go estimate is required.

### III. Optimization and anytime answers

Move from limits on exploration to bounds on the objective,
then retain useful answers while continuing the search.

1. **Branch-and-bound.** Derive a simple objective bound on
   an actual graph or partition, then trace incumbent updates
   and pruning. Reuse Week 1's upper/lower-bound distinction
   to explain the coverage needed for optimality. Begin with
   a bound requiring no new heuristic-construction machinery;
   account for ties and the limits of infinite-space claims.

2. **Anytime search and improving incumbents.** Use
   branch-and-bound to introduce an interruptible search that
   retains its best feasible answer while continuing work.
   Show first feasibility, successive improvements, and an
   eventual proof as distinct milestones. Explain what can
   be returned before a feasible answer exists. Anytime
   behavior does not require randomness or a quality bound;
   Weeks 7 and 10 develop these different possibilities.

## Week 4: Best-First Search

Purpose: give priorities an explicit meaning and connect each
selection rule to the result its first accepted goal supports.
Extend Week 3's route example with unequal costs and a concrete
remaining-cost estimate before introducing formal properties.

### I. Priorities and competing arrivals

Establish the common queue mechanism through observable
choices and competing routes, then name its bookkeeping.

1. **Priorities for choosing the next path.** Motivate cost
   already paid and estimated cost remaining, then compare
   ordering by g, h, and g+h on the route instance. Explain
   the estimate's meaning before its notation. Distinguish
   choosing promising work from proving work unnecessary.
2. **Retaining and improving arrivals.** Begin with a state
   reached expensively and then cheaply. Explain best-known
   costs, parent records, strict improvements, and stale queue
   entries using those two arrivals. Distinguish a reached
   state, a queued record, an expansion, and finalization.

### II. Searching by cost or estimated proximity

Contrast two policies using the same queue and cost model.
Their different guarantees motivate combining g and h.

1. **Uniform-cost search.** Trace minimum-cost-prefix order
   and show why generating a goal is insufficient to stop.
   Establish the conditions for an optimal returned route,
   separating finite-graph termination from infinite-space
   progress assumptions.
2. **Greedy best-first search.** Show how favoring estimated
   proximity can find a costly answer on the same instance.
   Distinguish useful guidance from a cost guarantee and
   qualify coverage by the space and duplicate policy.

### III. Combining guidance with guarantees

Use UCS's reasoning again with a justified completion bound.
Give admissibility, accuracy, consistency, and useful ordering
separate jobs. A lower bound is one use of an estimate.

1. **A* and admissible estimates.** Explain g+h as a completion
   lower bound and use a retained optimal-route prefix to
   justify accepting a goal on minimum removal. State the
   duplicate policy and progress assumptions with the claim.
2. **Admissibility and useful overestimates.** Explain the
   never-overestimate condition and the optimality argument
   it enables. Contrast optimism with predictive accuracy and
   ranking useful choices. Trace an inadmissible estimate
   finding a useful answer sooner, and a case where it misleads.
   Explain deliberate weighting and greedy guidance without
   promising universal speedups. Separate the estimate used
   to order work from an admissible bound used to prune or
   certify it; arbitrary overestimates provide no cost ratio.
3. **Consistency, finalization, and reopening.** Introduce
   consistency when asking whether a state's first expansion
   can be final. Trace an admissible but inconsistent estimate
   requiring reopening, and explain what consistency adds.
4. **The practical cost of guidance.** Compare heuristic
   strength, evaluation work, repeated expansions, and
   frontier storage across the chapter's methods. Explain why
   fewer expansions need not mean less time. Motivate Week 5's
   construction and memory choices; leave detailed profiling
   and representation engineering to Week 8.

## Week 5: Heuristics and Limited Memory

Purpose: construct useful estimates, distinguish guidance from
justified lower bounds, and study searches retaining less of
the frontier. Match the construction to the required answer
guarantee and the cost of obtaining and using the estimate.

### I. Constructing estimates for bounds and guidance

Start with one relaxation and one abstraction before asking
when several estimates can safely be combined.

1. **Relaxation as a source of lower bounds.** Introduce the
   tile puzzle's rules before Manhattan distance. Explain why
   the relaxed optimum is safe and an arbitrary relaxed answer
   need not be. Reconnect this reasoning to admissibility
   from Week 4.
2. **Abstraction and pattern databases.** Work from a concrete
   state to one abstract state, its permitted moves, and an
   actual table lookup. Show construction of a single database
   and account for preprocessing, storage, and lookup costs.
   Establish this example before introducing additive tables.
3. **Combining heuristic estimates.** Explain maximum
   combination and derive safe addition through cost
   partitioning. Use the preceding examples to show what
   would be counted twice by naive addition. Explain the
   zero-cost abstract moves and suitable shortest-path
   construction that the chosen cost partition introduces.

4. **Constructing useful inadmissible heuristics.** Show why
   a cheap feasible plan in a relaxed problem may guide search
   even though it is not a lower bound on the original optimum.
   Use relaxed-plan heuristics as a concrete construction;
   relate learned or corrected estimates to the same distinction.
   Evaluate ranking, runtime, and returned quality as well as
   prediction error. Keep a separate justified bound when a
   proof or certified gap is needed.

### II. Searching with less memory

Build directly on Week 3's repeated bounded traversals and
Week 4's account of frontier storage.

1. **Trading memory for repeated work.** Identify what A*
   retains and what is lost when frontier details are
   discarded. Motivate regeneration and retained summaries;
   include heuristic tables in the total memory budget.
2. **IDA*: repeated cost-bounded exploration.** Trace actual
   threshold changes and minimum-exceeded updates. Explain
   testing the threshold before a goal and preserving the
   successful path during restoration. Connect optimality,
   progress, and memory to the stated rules and the greatest
   depth reached, rather than an undefined solution depth.
3. **Recursive best-first search.** Use a concrete tree to
   show backed-up bounds, branch switching, and regeneration.
   Explain its guarantee, progress assumptions, and exhausted
   branches explicitly. Compare the information retained by
   A*, IDA*, and RBFS and the repeated work each permits.

4. **Beam search and selective retention.** Specify one
   level-by-level beam policy with width, ranking, goal-test,
   and duplicate rules. Trace a discarded branch that contains
   a solution, even with an admissible ranking estimate.
   Contrast permanent deletion with IDA*/RBFS regeneration
   and greedy best-first search's retained alternatives.
   Account for generated children and path storage as well as
   beam width; use beam-stack only as a reading connection.

## Week 6: Local Search and Repair

Purpose: improve complete candidates using local changes,
while making feasibility, reachability, and the meaning of
stalled progress explicit. Return to the familiar coloring
and partitioning instances before adding another problem.

### I. Candidates and landscapes

Establish what can change and why strict improvement alone
can stop short of a solution or optimum.

1. **Candidates, objectives, and neighborhoods.** Establish
   complete but possibly infeasible assignments, permitted
   changes, and the candidate graph they induce. Distinguish
   feasibility from a penalty score, and check whether the
   neighborhood can reach the relevant candidates.
2. **Local minima, plateaus, and barriers.** Use our number
   partitioning instance to explain strict descent, sideways
   moves, and uphill barriers. Show how changing the
   neighborhood changes a local optimum. Distinguish checking
   every neighbor from merely finding no improvement in a
   sample; neither certifies a global optimum by itself.

### II. Repairing violated constraints

Use the landscape vocabulary to explain actual repair
policies, including moves that do not strictly improve.

1. **Local improvement and constraint repair.** Give a
   complete min-conflicts policy and trace it on our coloring
   instance, with explicit initialization, selection, ties,
   and stopping rules. Connect to Week 1's emergent behavior
   example while separating that trace from a guarantee.
2. **SAT repair and WalkSAT.** Explain clause violations,
   variable flips, and one stated repair policy, including
   its noise and tie rules. Compare its retained information
   with Week 2's backtracking SAT solver. A satisfying assignment
   certifies success; a failed budgeted run does not certify
   unsatisfiability.

### III. Move costs and sustained progress

Separate reducing the cost of a move from changing the
trajectory to escape a stalled region.

1. **Evaluating changes incrementally.** Derive coloring and
   partition deltas. Then introduce the symmetric closed-tour
   problem and cyclic edge order immediately before its 2-opt
   update. Account for accepted-move bookkeeping as well as
   proposal evaluation, and check deltas against full scores.
2. **Escaping and remembering useful answers.** Explain
   restarts, tabu memory, and compound moves using the earlier
   obstacles. Retain the best feasible candidate separately
   from the current one. Distinguish trajectory memory from
   exhaustive coverage; reserve restart probability and cost
   analysis for Week 7.

## Week 7: Stochastic Search and Anytime Optimization

Purpose: specify randomized search policies and assess their
outcomes under finite budgets. Use annealing for the main
complete policy and trace; populations and hybrids provide
compact comparisons rather than separate algorithm surveys.

### I. Designing stochastic optimizers

Begin with what a run must return, then examine different
ways to generate and retain useful candidates.

1. **Anytime search: keeping an answer available.** Extend
   Week 3's deterministic example to stochastic anytime
   optimization through feasible incumbents and current
   versus best candidates. Explain what interruption can
   return before feasibility is reached. State the budget and
   whether success means feasibility or a specified quality
   target; improvement alone supplies no optimality gap.
   Contrast interruption at an unknown time with a contract
   algorithm given its budget in advance; discuss progress
   profiles and the cost of retaining an available answer.
2. **Simulated annealing.** Connect proposal, acceptance,
   objective scale, temperature, and cooling in one fully
   specified budgeted policy. Trace accepted and rejected
   proposals, tracking both current and best candidates.
   Distinguish finite-budget behavior from asymptotic claims.
3. **Populations and evolutionary search.** Explain
   selection, variation, replacement, and retained best
   answers through a small population. Preserve representation
   validity and distinguish diversity from independent trials;
   keep the treatment to one concrete policy.
4. **Hybrids and restricted exact search.** Explain iterated
   local search and large-neighborhood repair using coloring
   or partitioning, rather than an unexplained scheduling
   model. Show what is fixed, what may change, and which
   solver handles that restricted problem. Distinguish an
   exact inner result from the outer search's guarantees.

### II. Allocating and evaluating computation

Once a run is specified, decide how to divide a budget among
runs and how to interpret their outcomes.

1. **Restarts and expected effort.** Define a capped trial,
   its success target, and its cutoff-dependent probability
   before deriving success and time calculations. State the
   independence assumptions and include failed attempts and
   differing trial durations. Explain cutoff choices, startup
   costs, and why shared state can change the calculation.
2. **Evaluating stochastic outcomes.** Organize comparisons
   around instances, seeds, targets, budgets, quality, success,
   failures, and timeouts. Separate parameter selection from
   final evaluation. Make the experimental record explicit,
   distinguishing variation across seeds from variation across
   instances and equal work from equal elapsed time.

## Week 8: Engineering Search

Purpose: measure and improve search operations while
preserving the intended model, then apply the course's
methods to two compact practical models.

### I. Implementing and measuring solvers

Use a defined sequential baseline and bottleneck measurements
before changing representations or distributing work.

1. **Measuring work, time, and memory.** Identify expensive
   operations and account for retained data. Explain why
   expansion counts, throughput, and peak memory describe
   different costs. Separate profiling one implementation
   from Week 7's comparison across stochastic runs.
2. **Representing states for frequent operations.** Compare
   compact structures, bitsets, locality, equality, hashing,
   and justified canonicalization on concrete state data.
   Treat hashing as a lookup aid, not proof of state equality;
   preserve relevant future behavior when merging states.
3. **Symmetry and representative states.** Use interchangeable
   coloring labels to justify fixing one vertex's color.
   Show why every solution has a representative, and which
   labeled answers the restriction removes. Distinguish
   symmetry-breaking constraints from canonical state keys;
   preserve goals, objective values, and answer reconstruction.
   Explain when preassigned or meaningful labels invalidate
   the reduction. Relate coverage of the reduced space to
   coverage of the original space explicitly.
4. **Creating, sharing, and restoring search state.** Compare
   copies, persistent data, trails, and reconstruction.
   Reuse Week 2's restoration requirement and Week 4's path
   records; explain which information must remain valid and
   available before considering parallel ownership.
5. **Parallel work and global guarantees.** Explain work
   distribution, state ownership, communication, and in-flight
   work. Connect termination and bounds to all workers' work,
   not just an empty local queue. Include communication and
   additional search effort when assessing speedup.

### II. Applying search to planning and scheduling

These are modeling applications, not demonstrations that
parallel execution is faster. Reuse earlier search methods
and bounds to show how model choices determine the answer.

1. **Planning as an implicit graph.** Use the courier model
   to connect facts, actions, and goals to successor generation
   and path search. Derive a delete-relaxation bound under
   explicit assumptions. Reuse Week 5's distinction between
   a relaxed optimum and a merely feasible relaxed plan.
2. **Scheduling as constraints and optimization.** State
   machine and task assumptions, start-time domains, completion
   deadlines, precedence, and capacity constraints. Derive
   work and precedence bounds, combine them soundly, and check
   the existing schedule against them. Distinguish failure at
   one deadline from impossibility at every deadline.

## Week 9: Adversarial Search

Purpose: choose actions when an opponent controls replies.
Define the value being computed before optimizing its
computation. Develop one small rule-based game throughout
and reuse it for sampled search in Week 10.

### I. Game states and values

Start with the game model and exact terminal utilities,
then specify the approximation introduced by a horizon.

1. **Game states, turns, and outcomes.** Establish legal
   moves, terminal utilities, relevant history, and a fixed
   MAX perspective through a fully described finite game.
   State the two-player, zero-sum, perfect-information model
   and its treatment of repeated positions.
2. **Minimax.** Derive values from the players' choices and
   trace a move decision. Explain the guarantee against an
   adversarial reply, its assumptions, and its computational
   cost; distinguish an optimal action from a cooperative
   route to the most attractive leaf.
3. **Depth limits and evaluation.** Define the truncated
   search's value and terminal-before-horizon handling.
   Explain horizon effects and a concrete evaluator using
   the same utility perspective. State how extensions or
   solved states change the leaf semantics before any cached
   value is allowed to substitute for this computation.

### II. Pruning, deadlines, and reuse

Keep the value definition fixed while reducing work or
choosing how much work can finish before a deadline.

1. **Alpha-beta pruning and move ordering.** Give one complete
   recursive account and a nested trace for the chosen leaf
   semantics. Distinguish exact values from returned bounds
   and ordering hints from sound cutoffs. Explain why pruning
   preserves minimax's answer and how order changes the work
   saved.
2. **Iterative deepening under a deadline.** Explain completed
   iterations, fallback moves, and the principal variation.
   Show how earlier iterations can guide move order.
   Distinguish having a usable answer from monotone gains
   in playing strength as the horizon increases.
3. **Reusing transpositions safely.** Match state identity,
   horizon, evaluation semantics, and bound type to the query.
   Demonstrate compatible reuse and an incompatible case.
   Distinguish a reusable value or bound from a move-ordering
   hint; resolve the draft's solved-value exception explicitly.

### III. Extending the game model

Keep this a short closing bridge. Random events in the game
and randomness used by a search algorithm play different roles.

1. **Chance outcomes.** Introduce probability-weighted
   continuation values on a small extension of the game.
   Distinguish chance from an opponent's choice and explain
   why deterministic alpha-beta rules do not transfer
   automatically. Point toward Week 10's sampled evaluation
   while retaining the limits of the current game model.

## Week 10: Beyond the Basics

Purpose: use the course's existing ideas about guidance,
coverage, bounds, and evidence to assess selected extensions.
Keep MAPF a compact application and LaCAM a reading connection.
The final synthesis should tie methods together rather than
start another survey of new algorithms.

### I. Trading solution quality for search effort

Extend A* and branch-and-bound, separating the priority used
to choose work from the bounds used to certify an answer.

1. **Bounded suboptimal search.** Use weighted A* to show
   how a changed priority can trade solution quality for
   search order under stated assumptions. Preserve the
   required improvement/reopening policy and actual path
   costs. A weaker quality guarantee is not a promise of
   faster runtime on every instance.
2. **Anytime search with certified gaps.** Connect feasible
   incumbents, maintained coverage, and admissible lower
   bounds to additive or multiplicative certificates. Include
   pending work and the incumbent in the global bound.
   Contrast this certificate with Week 7's best-so-far answer;
   do not treat a weighted search key as a lower bound.

### II. Coordinating path searches

Independent pieces of search must be combined into a valid
global answer. Joining two directions and resolving conflicts
between agents illustrate different coordination requirements.

1. **Bidirectional shortest-path search.** Trace both queues,
   joined routes, and the stopping comparison on one graph.
   Explain why a first meeting is insufficient. State the
   need for a known goal, reverse successor generation, and
   correct handling of stale or exhausted queues.
2. **Multiple agents sharing a graph.** Work through one
   collision and constraint split. Define the objective,
   waiting and arrival rules, and compatible individual paths
   before discussing configuration search. Connect to the
   qualified completeness and optimality claims in the LaCAM
   readings, making LaCAM*'s cost model explicit; keep its
   internal machinery outside the core treatment.

### III. Sampling and assessing search methods

Return explicitly to Week 9's game and Week 7's distinction
between a useful observed outcome and a proved guarantee.

1. **Monte Carlo tree search.** Trace selection, expansion,
   rollout, and backup through the established small game.
   Show how a sampled reward updates counts and means before
   using them in an exploration-versus-exploitation score.
   Explain unvisited actions, reward perspective at MAX and
   MIN, and the distinction between sampling policy and final
   move recommendation. Distinguish adaptive rollout samples
   from independent trials or modeled chance probabilities;
   sampled values are not minimax certificates.
2. **Guidance and proof in new methods.** Close with a short
   comparison of what the chapter's returned answers certify.
   Use learned guidance as one example: changing order,
   pruning possibilities, and replacing a bound require
   different arguments. Reconnect model, retained information,
   stopping rule, and measured behavior without introducing
   another algorithm family.

## Editorial findings and limits

The flat outlines already covered the main methods. Their
largest organizational gap was the lack of intermediate
teaching purposes: an algorithm list alone did not show
when the reader was learning a model, a search policy, or
the evidence supporting its result. The new sections make
those transitions explicit without adding a finer topic level.

The most useful ordering changes are forward checking before
CSP ordering rules, landscapes before repair policies, restart
analysis after the policies it can restart, and game-value
semantics before alpha-beta and cached reuse. Week 10 keeps
MAPF with path search and closes with MCTS and synthesis.
The tour example now enters where its delta is actually used.

Several gaps require better treatment within existing topics,
not more algorithms: combining depth-limit outcomes; tracing
an actual branch-and-bound instance; projecting and looking
up a pattern database; showing RBFS regeneration; specifying
annealing and repair policies completely; stating scheduling
constraints; and tracing bidirectional and MCTS decisions.
These continue the earlier
[chapter review](research/review-2026-10-27-remaining-chapters.md).

### Completeness and systematicity

Resolved according to Bart's definitions: a complete search
will eventually examine every state in its stated space;
a systematic search examines each state at most once.
The early chapters and notation now use these meanings.
Continued traversal, early stopping, and sound exclusion are
distinct. A pruned state's descendants are not counted as
examined. Solution-finding and optimality guarantees are
stated directly when complete enumeration is unnecessary.
Reopening and regeneration can sacrifice systematicity.

### Anytime behavior and inadmissible guidance

Anytime search now begins with deterministic branch-and-bound
in Week 3. Week 7 develops interruption, budgets, and empirical
progress; Week 10 adds certified gaps. This makes answer
availability a general search property rather than a synonym
for stochastic optimization.

Week 4 explains what admissibility buys and why one might
choose another estimate. Week 5 develops constructions for
both roles. Week 10 reconnects aggressive ordering with a
separate lower bound. The literature supports using even
arbitrary non-admissible ordering while retaining admissible
bounds for certificates; see the
[source review](research/anytime-inadmissible-sources-2026-11-11.md).

### Approved additions and the CIRL connection

Bart approved all four additions on 2026-11-11: learning from
failure in Week 2, limited discrepancy search in Week 3, beam
search in Week 5, and worked symmetry reduction in Week 8.
They remain bottom-level topic subsections within the existing
weeks. Incremental replanning remains a reading possibility.
The [literature review](research/literature-topic-gaps-2026-11-11.md)
records the rationale and sources; its earlier optional status
for these four topics is superseded by this decision.

Bart identifies the last three recommendations in the original
list—learning from failure, symmetry reduction, and limited
discrepancy search—with work at CIRL while he was there.
Use that connection in choosing readings, and reserve his
personal account for the Epilogue. Relevant reading connections
include Ginsberg's
[Dynamic Backtracking](https://arxiv.org/abs/cs/9308101),
Crawford, Ginsberg, Luks, and Roy's symmetry-breaking work,
and Harvey and Ginsberg's limited discrepancy search.
Attribute each algorithm to its own source; the earlier GRASP
recommendation is a separate SAT conflict-learning connection.

### Reading load and scope

Give each addition one concrete example and its central
argument. Reuse the SAT conflict, a small ordered decision
tree, the route graph, and the coloring instance. These topics
should replace vague practical-solver and canonicalization
passages where possible. Avoid expanding them into full CDCL,
dynamic-backtracking, beam-stack, or group-theory treatments.

The SAT encoding subsection, Week 7's policy comparisons,
and Week 10 remain the main pressure points. Keep CNF
conversion a concise supporting explanation, annealing the
main stochastic trace, and population/hybrid alternatives
compact. Week 10 needs an actual bidirectional trace and an
MCTS iteration; MAPF gets one conflict split and reading
connections, not a full second planning course.

The shared examples and prerequisites should carry the load:
coloring from Weeks 1–2 into repair, the route graph through
Weeks 3–4 and later path methods, partitioning for landscape
and annealing behavior, and one game through Weeks 9–10.
Each return should restate the data needed locally. The
chance section and closing synthesis are deliberately short;
sections need not receive equal space.

Keep recurring material in its main home. Week 3 develops
coverage and traversal memory; Week 4 handles improved
arrivals and cost guarantees; Week 5 constructs heuristics
and studies regeneration. Week 7 analyzes stochastic runs,
Week 8 profiles implementations, and Week 10 adds quality
certificates. Later uses recall those ideas and add the new
application rather than restart their introductions.

Detailed organization reviews:

- [Weeks 2–4](research/outline-review-2026-11-11-weeks2-4.md).
- [Weeks 5–7](research/outline-review-2026-11-11-weeks5-7.md).
- [Weeks 8–10](research/outline-review-2026-11-11-weeks8-10.md).
