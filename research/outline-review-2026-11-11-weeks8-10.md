# Outline review: Weeks 8–10

Reviewed 2026-11-11. Review only. This note proposes an
intermediate section level in OUTLINE.md; it does not revise
the outline or chapters.

The existing numbered topics are the bottom-level
subsections. The proposed structure below is therefore
**chapter → section → topic subsection**. It adds no finer
subsections beneath those topics. One omitted topic from the
existing Week 10 draft is proposed for restoration at the
same level as the other topic subsections.

## Basis and principal decisions

Read the repository authoring skill and editorial guide,
BRIEF.md, BOOK-NOTES.md, STATUS.md, OUTLINE.md, notation,
the complete Weeks 8–10 chapters, and the relevant earlier
reviews. Inspected earlier chapter headings and passages
for the dependencies on A*, lower bounds, anytime answers,
and stochastic evaluation. This is an organizational review,
not a fresh source audit or algorithm-validation campaign.

The current outline already repairs important omissions
identified in the earlier reviews: scheduling deadlines,
a concrete game, a recursive alpha–beta account, a positive
bidirectional trace, one MCTS iteration, and an actual MAPF
conflict. Those repairs should survive grouping. Their
presence in an outline does not mean the draft has already
implemented them.

The highest-value organizational decisions are:

1. Week 8 has two teaching purposes: engineer a solver,
   then use familiar methods to model two applications.
   Make that boundary visible rather than treating the
   applications as further performance techniques.
2. In Week 9, establish depth-limited minimax before
   alpha–beta. First define the answer being computed;
   then explain how to compute and reuse it efficiently.
3. Group Week 10's two path-structure topics together by
   moving MAPF immediately after bidirectional search.
   Finish with MCTS and a brief comparative synthesis.
4. Restore the existing draft's “Guidance and proof in new
   methods” as a short peer topic. It is a useful course
   conclusion, provided it compares the methods already
   taught rather than starting a learned-search survey.

The introduction to OUTLINE.md still calls the numbered
items “main sections” and postpones subsections. That is
superseded by the user's current clarification and should
be corrected when the root editor changes the outline.

## Week 8: Engineering Search

The proposed topic order is sound. Measurement first gives
representation and concurrency choices an empirical purpose.
Representation then precedes ownership and restoration, and
those precede coordinating multiple workers. The current
draft begins with representation and places measurement
later; the outline's new order is an improvement.

Two sections are sufficient. A separate top-level section
for parallelism would be defensible, but unnecessary: the
parallel topic already has its own subsection, and it extends
the same concern with retained information and ownership.

### A. Engineering a search implementation

1. **Measuring work, time, and memory.** Establish the task,
   result checks, counting rules, profile, and retained
   storage against which an implementation change is judged.
2. **Representing states for frequent operations.** Connect
   compact data, bitsets, locality, equality, hashing, and
   canonicalization to actual repeated operations.
3. **Creating, sharing, and restoring search state.** Compare
   copying, persistent data, trails, and reconstruction by
   the information each search order must keep available.
4. **Parallel work and global guarantees.** Extend ownership
   and coverage to workers, queues, and messages; explain
   what permits declaring completion or accepting a bound.

### B. Modeling planning and scheduling applications

5. **Planning as an implicit graph.** Derive the courier's
   states and actions, then connect its delete relaxation
   to the earlier lower-bound argument.
6. **Scheduling as constraints and optimization.** Specify
   the bounded scheduling model, derive its bounds, and
   check the known optimal schedule against the constraints.

**Why this boundary matters.** Planning and scheduling are
not demonstrations that packing data or adding workers
makes a solver faster. The current applications contain no
such measured experiment. Their job is to integrate the
earlier modeling, propagation, search, and bound ideas.
The section introduction should say so explicitly. Calling
them applications of the *course's methods*, rather than
of parallel search, makes the chapter's second purpose honest.

The connection to engineering can still be concrete. The
courier's facts illustrate an encodable state and implicit
successor generation; a scheduling assignment illustrates
partial records and reversible constraint changes. Brief
callbacks suffice. Building a benchmark or a parallel
implementation for either application would exceed the
compact application role.

**Prerequisites and scope.** Week 7 owns how to compare
randomized outcomes, seeds, failures, and budgets. Week 8
owns which operations consume time and which records consume
memory. Refer back to Week 7 rather than repeating its
experimental-methods treatment. Similarly, Weeks 2–5 already
establish restoration, duplicate dominance, relaxation, and
memory tradeoffs; Week 8 makes their representation and
lifetime obligations concrete.

Topic 2 is internally broad, but the audience's systems
background makes it manageable if one state representation
anchors the discussion. Avoid a disconnected catalogue of
bit tricks, processor features, and allocation strategies.
Keep correctness constraints close to the associated choice:
hashes are not equality, keys must remain stable, and a
canonical representation must preserve reconstructible
answers as well as reachability and costs.

Topic 4 should teach ownership and global accounting through
one small concurrent-search scenario. It need not teach
work-stealing protocols, distributed termination detection,
and a complete HDA* implementation. One queued item, one
in-progress expansion, and one in-flight message can explain
why local emptiness or a found goal is insufficient. A shared
queue orders currently queued records; it does not reproduce
the serial expansion sequence when workers overlap.

The scheduling application still needs actual finite domains:
with integer horizon H and task duration p, starts range
from 0 through H−p. Precedence and half-open execution
intervals make “finish by H” and machine capacity concrete.
That is a prerequisite bridge inside topic 6, not another
scheduling subsection. Retain the distinction between one
failed horizon and infeasibility for every horizon.

## Week 9: Adversarial Search

The main repair is ordering. Current outline topic 4 should
precede topic 3. Otherwise the chapter first develops efficient
evaluation of a full game tree, then introduces the practical
value function on which the subsequent deadline and reuse
topics depend. The reordered chapter defines both exact and
truncated answers before optimizing their computation.

The order of existing topics becomes **1, 2, 4, 3, 5, 6, 7**.
Numbering below follows that new reading order.

### A. Defining game-search values

1. **Game states, turns, and outcomes.** Introduce a finite
   game from its rules; establish actions, terminal values,
   relevant history, and the fixed MAX perspective.
2. **Minimax.** Derive full-game values and a move decision
   from the players' choices, then explain cost and correctness.
3. **Depth limits and evaluation.** Define depth-limited
   minimax and its leaf semantics; show what a horizon
   evaluator estimates and why deeper values can differ.

### B. Computing and reusing bounded game searches

4. **Alpha-beta pruning and move ordering.** Compute the
   stated minimax function with sound cutoffs, distinguishing
   an exact root result from bounded interior returns.
5. **Iterative deepening under a deadline.** Use completed
   searches to provide a move and guide later ordering;
   distinguish answer availability from improving play.
6. **Reusing transpositions safely.** Reuse earlier work
   only when state, remaining horizon, evaluation semantics,
   and bound type answer the current query.

### C. Extending the game model to chance

7. **Chance outcomes.** Contrast a probability-weighted
   continuation with an opponent's choice, and identify the
   boundary of the perfect-information model.

**What topic 3 must establish.** “Depth limits and evaluation”
should explicitly mean *depth-limited minimax*, not merely
a list of evaluation features and horizon warnings. Explain
terminal handling before a horizon cutoff and state which
function the procedure returns. The core alpha–beta routine
can then include that leaf rule from its first presentation,
without a second algorithm or a later patch.

The old solved-value defect is directly relevant to this
organization. A genuinely solved state can have value +1
while its horizon-zero heuristic value is 0. Substituting
the solved value changes a function defined to return the
heuristic at that cutoff. Either define solved-state handling
as part of the leaf semantics from the outset, or explain
that it deliberately changes the truncated function. This
decision belongs before the transposition compatibility rule,
as the existing outline's topic 4 already anticipates.

**Why the second section holds together.** Alpha–beta preserves
the answer to a stated query while reducing work; iterative
deepening changes the query's horizon; transposition reuse
must determine whether an old answer applies to the new
query. That progression gives the table's horizon and bound
fields a reason to exist. Introducing tables earlier would
require forward references to those meanings.

The alpha–beta trace should include both a MIN cutoff and
a nested MAX cutoff. Bound classification needs an actual
call/window/result example. These are parts of the existing
alpha–beta and reuse topics, not reasons for more outline
levels. Keep one utility convention throughout. A separate
negamax treatment would dilute the introductory argument;
a short warning about mixing conventions is sufficient.

**The shared game is an enabling decision.** Choose the game
before drafting the mathematical trace. Its rules must make
legal actions, a terminal result, at least a few plies, a
horizon evaluation, and a repeated state intelligible. The
same game should support Week 10's rollout and backup.
An abstract tree alone does not establish state identity,
legal-move generation, or a rollout policy. Do not make
chess vocabulary carry those prerequisites for a novice.

**Chance is a bridge, not a second game-search course.** Keep
one expectation calculation and the explanation of why
ordinary alpha–beta does not transfer unchanged. No separate
expectiminimax engine or hidden-information algorithm is
needed. Make the Week 10 transition explicit: sampling can
allocate computation in a deterministic game. A random
rollout is not necessarily a random event in the modeled
world, and its average is not automatically minimax.

## Week 10: Beyond the Basics

This chapter has the greatest risk of becoming a survey of
names. Each current topic requires its own model, mechanism,
example, and interpretation. The draft is only about 2,130
raw whitespace-counted words, but its missing positive
bidirectional trace, complete MCTS iteration, and concrete
MAPF split explain some of that apparent economy. A new
section layer must organize those obligations rather than
conceal them.

Three groups work if their purposes are explicit. Move MAPF
after bidirectional search and restore the draft's concluding
“Guidance and proof in new methods.” The existing-topic order
is **1, 2, 3, 5, 4**, followed by that restored peer topic.

### A. Answer quality and certificates

1. **Bounded suboptimal search.** Use weighted A* as a change
   to the known A* selection rule, with the assumptions and
   proof that support its solution-cost bound.
2. **Anytime search with certified gaps.** Connect an available
   feasible answer with retained coverage and an admissible
   lower bound; show what an additive or ratio gap establishes.

### B. Coordinating path searches

3. **Bidirectional shortest-path search.** Join forward and
   backward information, retaining the best complete route
   until the frontier comparison justifies stopping.
4. **Multiple agents sharing a graph.** Couple individual
   routes through explicit collision and arrival rules;
   show one constraint split and connect joint configuration
   search to the qualified claims in the LaCAM readings.

### C. Sampling games and assessing new methods

5. **Monte Carlo tree search.** Reuse the Week 9 game for
   a specified selection, expansion, rollout, and backup;
   distinguish sample allocation from the final decision.
6. **Guidance and proof in new methods.** Compare what the
   chapter's methods retain, return, and establish. Use
   learned guidance as one example of how ordering can
   differ from deletion or a proof-bearing bound.

**The middle grouping has a real rationale.** Bidirectional
search coordinates prefixes and suffixes. MAPF coordinates
routes that are individually valid but may be incompatible.
Both require more than an attractive local result to justify
the whole answer: the first meeting need not be shortest,
and individually shortest routes can collide. Their coupling
conditions differ, so the introduction should state the
comparison without suggesting that one algorithm or proof
solves both problems.

The weighted and anytime topics also supply tools used in
interpreting MAPF papers: early feasibility, bounded quality,
eventual optimality, and an actually established certificate
are different claims. This gives the LaCAM reading connection
a foundation before it appears.

**The ordering tradeoff is acceptable.** MCTS now comes after
four path-search subsections, making the return to Week 9's
game later. Restore the game's name, relevant rules, and
utility convention when returning to it. A clear chapter
roadmap should advertise the path-search block followed by
the game-sampling block. Moving MCTS last also gives the
conclusion a productive contrast: observed means and search
bonuses are different kinds of information from justified
cost bounds.

**Control depth explicitly.** Retaining five applications
or methods does not require giving each a full implementation:

- Weighted A*: reuse Week 4's loop and arrival rules. Teach
  the changed key and its proof, not another A* tutorial.
- Certified gaps: use one incumbent/frontier example. Give
  the coverage condition, including work still being
  generated or reopened. Do not add a catalogue of named
  anytime algorithms.
- Bidirectional search: give one complete finite-graph
  Dijkstra trace with reversed directed edges, labels,
  joins, and the successful stopping comparison. Define
  “settled” locally. Heuristic bidirectional variants remain
  outside this treatment.
- MAPF: specify one graph, starts, goals, collisions, waits,
  arrival behavior, objective, and one branch split. Show
  why every feasible solution satisfies at least one child
  constraint. This is enough to teach the decomposition
  idea; it is not a complete CBS algorithm or proof.
- LaCAM: retain reading connections, not full successor
  generation or an implementation project. Give a concrete
  meaning to the cost-model qualification before citing
  eventual optimality. Unit cost per joint time step can
  express makespan; ordinary arrival-time sums require
  compatible state and arrival conventions.
- MCTS: give one specified baseline and a complete iteration.
  A bandit-theorem derivation, neural value training, or
  survey of MCTS variants would crowd out the needed trace.

These are scope limits within the existing topic subsections,
not additional subsections or exercises.

**MCTS has a small but essential prerequisite chain.** First
define a policy as a rule for choosing a legal move. State
the terminal reward and perspective. Then show an observed
reward changing a visit count and mean, before relying on
those statistics in an exploration expression. Distinguish
the tree-selection rule, rollout policy, and final root
recommendation. At MIN nodes, both selection and backup
must remain compatible with the same utility convention.

Week 7's independence assumptions do not automatically apply
to adaptively allocated tree samples. Likewise, Week 9's
expectation over modeled chance outcomes does not make a
rollout average an exact game value. These two connections
deserve explicit sentences inside MCTS; neither requires
a statistics chapter or a new lower outline level.

**The restored conclusion earns its space.** The draft already
has the useful “Guidance and proof” material, but OUTLINE.md
omits it. Restoring a few comparative paragraphs, perhaps
with a small table, is preferable to ending on a paper list.
It should ask what a proposed method changes about ordering,
coverage, identity, bounds, and stopping, using the methods
just taught. It should not introduce another algorithm family.

Useful comparisons include a weighted priority versus an
admissible bound, a sampled mean versus a minimax value,
and a feasible joint plan versus a completed optimality
argument. Explain one concrete combination, such as an
aggressive search supplying an incumbent to a search that
maintains valid coverage. Merely listing compatible-sounding
method names would not provide the same synthesis.

## Cross-week integration and remaining decisions

The late chapters should extend earlier concepts rather
than introduce them a second time:

| Earlier home | Later use |
| --- | --- |
| Week 2: choices, propagation, restoration | Week 8 trails and scheduling; Week 10 conflict constraints |
| Weeks 3–5: coverage, arrivals, lower bounds | Week 8 parallel completion; Week 10 path certificates |
| Week 6: proposal cost and incremental updates | Week 8 profiling and representation costs |
| Week 7: incumbents and honest random evaluation | Weeks 9–10 interruption and sampled game evidence |
| Week 8: state identity and ownership | Week 9 table compatibility; Week 10 joint configurations |
| Week 9: a concrete game and utility semantics | Week 10 rollout, selection, and backup |

There are three distinct senses of “anytime” to preserve.
Week 7 retains a best feasible optimization answer once one
exists. Week 9 retains a legal move and completed horizon,
without monotone guarantees of playing strength. Week 10
adds justified quality gaps when the search retains suitable
coverage. Answer availability, measured improvement, and
certified quality should not collapse into one promise.

Bounds likewise change role. A relaxed path estimate, a
scheduling lower bound, an alpha–beta bound on game utility,
and a UCT exploration bonus are not interchangeable. Their
shared notation should not substitute for explaining what
each quantity establishes. The Week 10 synthesis is a natural
place to make that comparison visible.

The remaining authoring decisions are bounded and concrete:

1. Select the shared game for Weeks 9–10 before drafting
   either chapter's new traces.
2. Adopt explicit depth-limited leaf semantics before
   writing alpha–beta and table reuse.
3. Decide the MAPF collision, objective, and arrival rules
   together, so the worked split and LaCAM qualifications
   refer to a coherent model.
4. Preserve a short comparative ending to Week 10 while
   keeping learned guidance at the level of interpretation.

No chapter split, new week, exercises, full planning system,
full scheduling system, or full LaCAM implementation is needed.
The ten-week scope remains intact.

## Review records used

- [Weeks 6–8 review](review-2026-10-27-weeks6-8.md):
  scheduling deadlines, performance measurement, ownership,
  and the scope of the application examples.
- [Weeks 9–10 review](review-2026-10-27-weeks9-10.md):
  fixed-horizon semantics, recursive alpha–beta, the shared
  game, bidirectional and MCTS traces, the MAPF split, and
  the LaCAM objective qualification.
- [Week 8 draft](../src/08-engineering.md),
  [Week 9 draft](../src/09-adversarial.md), and
  [Week 10 draft](../src/10-frontiers.md): current teaching
  sequence and material that the outline must preserve.

Only this note was written. No chapters, outlines, feedback,
tests, syllabus files, or archive materials were changed;
no commits or pushes were made.
