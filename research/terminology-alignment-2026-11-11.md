# Complete and systematic search: terminology audit

Date: 2026-11-11.

Scope: read-only audit of Weeks 1–5, the introduction, and
notation, with a brief integration scan of later chapters.
No chapter files were edited for this audit.

The latest user decision is authoritative:

- Complete search will eventually examine all states.
- Systematic search examines each state at most once.

The audit applies those meanings directly. Finding a solution
whenever one exists is a separate guarantee. Soundly pruning
a subtree does not count as examining its descendants.

## Suggested shared wording

> A search is **complete** if it will eventually examine
> every state in the space being searched. It is
> **systematic** if it examines each state at most once.
> These are separate properties: a search can have either,
> both, or neither.

Follow this short definition with the model and counting
conventions, rather than loading them into its first sentence.

> State which space the claim concerns. A traversal from an
> initial state ordinarily searches the states reachable by
> the model's transitions. It does not promise to reach a
> disconnected part of a larger space.

> Examining a state means selecting it for search processing:
> testing its goal or constraint conditions, deciding whether
> to prune its branch, or considering its successors. Merely
> generating or ranking another record does not examine the
> state again. Duplicate and stale records can be rejected
> before another examination.

> A solver may stop after finding an answer. That stopped
> run has not examined every state it leaves unexplored.
> When discussing complete traversal, we mean the version
> that continues its exploration instead of stopping at the
> first solution.

For infinite spaces, explain once that eventual examination
means each particular state is examined after finite work.
It does not mean infinitely many states are processed in a
finite run. Assume finite operations at each step of the
algorithm when making these progress claims.

The universe must be fixed by the stated model before the
search runs. In particular, do not shrink it afterward to
the states left by pruning. A fixed variable-order model
can legitimately define its reachable partial assignments;
constraint pruning within that model still skips states.

## Essential distinctions

### Early stopping and continuing through goals

Current DFS, BFS, IDDFS, UCS, greedy, and A* pseudocode return
as soon as an accepted goal is found. Their solution-finding
or optimality guarantees remain useful and can be stated
directly. They are not full traversals on those successful
early-stopped runs.

Continuing after a goal must also consider that goal's legal
successors unless the model defines goals as terminal. On
S→G→T, recording the goal G but never expanding it leaves T
unexamined. Merely replacing a goal return with a print or
record operation is insufficient if a later return or branch
still prevents successor exploration.

Prefer preserving the existing solution-returning algorithms
and naming their continued traversal variants in prose.
There is no need to turn every algorithm listing into a
full enumeration routine to establish the terminology.

### Repeated generation and repeated examination

Many edges can generate records for the same state. A
reached-set check can discard those records before another
substantive examination. Such a method can be systematic
despite generating duplicates.

The distinction must match actual operations. If a version
goal-tests every duplicate before filtering it, it really
does repeat that aspect of examination. Reopening a state
for another search step is also repeated examination.

Record creation and ranking remain real computational work,
even when counted separately from examination. This matters
for A*: computing h for several queued arrivals may repeat
heuristic work before the one substantive examination. If
the book instead chooses to count every such evaluation as
an examination, consistent A* needs a corresponding caching
assumption before it can be called systematic. The selected
candidate convention makes that extra assumption unnecessary
while leaving the overhead visible in generated-node counts
and per-node work.

In shortest-path search, g is information about a route to
a state. Treating every new g as a different state solely to
avoid classifying reopening as repeated examination would
change the established model.

### Pruning and certificates

When a partial assignment violates a constraint, a solver
can rule out all of its extensions without examining each
extension. When a branch bound cannot improve an incumbent,
the same principle can establish optimality. Those are valid
proofs that avoid complete state enumeration.

The examined branch root and its unexamined descendants
must stay distinct. Words such as accounted for, covered,
or represented can explain a correctness proof, but cannot
be used to count descendants as examined or retain a claim
of complete enumeration of the original space.

## Classification of the actual variants

| Variant | Completeness and systematicity |
| --- | --- |
| Continued DFS on a finite tree of distinct states | Complete and systematic. |
| Continued DFS on a finite graph with a global reached set | Complete over reachable states and systematic. |
| DFS with only an active-path cycle check | May reexamine a merged state on another path; therefore not systematic in general. Continued traversal covers a finite reachable graph because it has only finitely many simple paths. |
| DFS with a global reached set on an infinite graph | Can be systematic and still miss states forever down another branch. |
| Continued BFS with a global reached set and finite branching | Complete over reachable states and systematic. Each state has some finite-depth route and only finitely many predecessors in layer order. |
| Depth-limited DFS | Generally incomplete for the unrestricted space. Path-local checking or acting on an improved depth budget can repeat states, so systematicity is not automatic. |
| Continued IDDFS with finite branching | Complete over reachable states, but not systematic: the root and upper levels are repeatedly examined. |
| Branch-and-bound | Sound bounds can prove the optimum while leaving states unexamined. Systematicity depends on the state representation and duplicate policy. |
| UCS with stale-entry filtering and nonnegative costs | Each substantive state examination has its optimal g, so no reopening is needed; it is systematic. Continued finite-graph traversal is complete over reachable states. |
| A* with consistent h and stale-entry filtering | Systematic under the stated nonnegative-cost assumptions. Continued finite-graph traversal is complete over reachable states. |
| A* that reopens improved states | Not systematic in general; the current worked example examines A twice. Continued finite-graph traversal can still be complete. |
| IDA* and RBFS with their current regeneration policies | Not systematic in general. They repeatedly examine states while trading work for retained memory. |

The complete traversal labels above assume no early goal
return and no extra pruning of the target universe.

For an infinite cost-ordered search, do not replace the
current finite-goal guarantee with an unqualified claim of
state-enumeration completeness. A useful sufficient condition
for UCS is finite branching and a fixed ε>0 lower bound on
edge costs. A* additionally needs finite heuristic values
for a simple eventual-examination argument: a reachable state
with h=∞ can be postponed forever behind infinitely many
finite-priority states. The current early-chapter integration
does not need that extra general theorem.

## Specific changes in Week 1

### Counting the program's work, around lines 472–490

Define examined alongside generated and expanded. Expanded
is narrower: a goal or pruned candidate can be examined
without producing successors. Explain that node-examination
counts can include repeated states.

Keep the existing statement that pruning removes a subtree
of completions. Add or preserve the implication that those
completions need not be generated or examined.

### Completeness, termination, and failure, lines 569–586

Replace the current definition, which says complete means
finding a solution whenever one exists. Introduce the two
user-defined properties together, with the reachable-space
and stopped-run qualifications above.

State solution-finding separately. A full traversal with a
correct goal test will encounter every goal in its target
space. A solver may also find an answer or prove failure
without examining every state, by justified pruning.

Retain the existing cautions about infinite branches,
discarding a useful arrival, and cycling repair rules.
Finding a solution, eventual state examination, termination,
and optimality remain distinct claims.

## Specific changes in Week 2

### Backtracking search, lines 274–280

Replace “backtracking is complete if…” with a direct solver
guarantee such as:

> For finite domains, backtracking will find a solution if
> one exists when it eventually tries every value not ruled
> out by sound deductions and restores branch state
> correctly. Sound pruning can avoid examining many states
> without losing a solution.

Ordering changes when work is examined. Pruning removes
work. Their distinct contributions should remain explicit.

A deterministic rule choosing one next variable and trying
each remaining value once can avoid repeated partial
assignments. That supports systematicity, even though
pruning and early stopping prevent complete enumeration.
Do not claim that all backtracking policies are systematic:
branching over different assignment orders can duplicate a
partial assignment, as Week 1 already explains.

### Forward checking, lines 333 and 364–370

“Places this deduction within systematic CSP search” is
unnecessarily broad. Prefer backtracking CSP search unless
the no-reexamination policy is specified nearby.

Delete the second old definition of a complete solver.
Explain instead that sound deductions preserve all solutions
of the current branch, while finite backtracking explores
the remaining choices. The two-color triangle proof excludes
all solutions without examining all complete assignments.

### SAT section, lines 372–402

Rename “Propagation and complete search in SAT” to
“Propagation and backtracking in SAT.” Replace “A complete
SAT search can choose…” with “A backtracking SAT solver can
choose…”.

“Trying both truth values as needed gives a systematic search”
needs the explicit no-repeat decision policy, or can simply
say that it explores the remaining choices. Satisfying a
clause through propagation is not examination of every
truth assignment that clause permits.

Replace “complete coverage” at the end with the actual
proof obligation: every possible satisfying assignment has
been ruled out. That is a logical statement, not a claim
that every assignment was examined.

The historical source title and “complete truth assignment”
retain their existing meanings. NP-complete also remains
unchanged.

## Specific changes in Week 3

### Title and opening, lines 1–20

Use the requested title, “Complete and Systematic Search,”
and reconcile contents/navigation titles. The opening must
stop defining systematic as keeping explicit alternatives.
Start from the two independent properties, then explain
that the chapter compares traversal policies, duplicate
policies, repetition, and pruning.

### DFS, lines 67–88

Explicitly classify the displayed path-local DFS as capable
of examining the same state along several different paths.
In the existing graph, if search continues past goals,
G is encountered through S→A→C→G and S→B→G.

The finite-tree coverage claim already says “unless it stops
with a solution”; retain that precision and connect it to
complete traversal. A tree's nodes need not be distinct
underlying states. Global reached-set DFS is the relevant
systematic graph variant.

### BFS, lines 158–162

Replace “With finite branching and a goal at finite depth,
BFS is complete” with separate statements:

- The displayed solver eventually finds a finite-depth goal
  under finite branching and returns a shallowest goal.
- Continued BFS with a reached set examines each reachable
  state exactly once, assuming it explores successors after
  recording goals.

The second statement establishes both requested properties.

### Depth limits, lines 185–215

Consider renaming the result “Complete failure” to “Failure”
or “Exhausted” and update the IDDFS test consistently. It is
a failure certificate, not necessarily complete examination
of the original state space. Cutoff remains distinct.

A fixed limit may omit reachable states. Depth-aware
reprocessing can be necessary for correctness, and then it
is not systematic. Do not promise that a global Boolean
visited set fixes this; the existing counterexample is good.

### IDDFS, lines 245–282

Replace “IDDFS is complete for such goals” with the direct
shallowest-goal guarantee. Add that continued finite-branching
IDDFS eventually examines every reachable state, while its
repeated upper levels mean it is not systematic.

The existing root-visited-d+1-times explanation supplies
immediate evidence; use the same examined/visited convention
consistently. Retain finite graph path-cycle exhaustion and
infinite-space nontermination qualifications.

### Branch-and-bound, lines 288–372

Replace “adds optimization to systematic exploration” with
“uses bounds to avoid branches that cannot improve a known
answer.” The actual algorithm can repeat states and skips
others, so neither property follows from its name.

Keep the finite-tree optimality argument. Say explicitly
that its proof can finish without complete enumeration:
unexamined branches cannot improve the final incumbent.
Do not change the set of states being quantified over to
the unpruned set and then claim completeness.

When there is no solution, exhaustion plus sound exclusion
proves failure. A bound of infinity may itself rule out a
branch, so the general proof need not be described as literal
examination of every state even in that case.

### Suggested readings, around line 410

Preserve Korf's exact paper title “A Complete Anytime
Algorithm for Number Partitioning.” Change the description
from “complete exploration and an eventual optimality proof”
to an eventual optimality proof or exact optimization.
The source title is not a license to reintroduce the old
course definition through the explanatory prose.

## Integration in Weeks 4–5 and references

- Week 4, line 119: replace “stale if it is ever examined”
  with “stale if it is ever removed.” The stale test precedes
  substantive examination under the proposed convention.
- Week 4, lines 101–108: explain that UCS and consistent
  A* can be systematic despite multiple queued records,
  while the general reopening loop need not be.
- Week 4, lines 186–190: qualify complete greedy traversal
  with continuing after goals, covering a finite reachable
  graph, and correct duplicate handling. The displayed
  cost-improvement implementation need not be systematic;
  h order can expand an expensive arrival before a cheaper
  one is discovered.
- Week 4, lines 277–282: connect the twice-expanded A to
  the systematicity definition explicitly. The optimality
  proof remains intact.
- Week 5, lines 251–257 and 345–366: state that IDA* and
  RBFS regeneration can repeat state examination. Avoid
  treating all tree-based or frontier-based methods as
  systematic.
- Week 5, lines 381–384: change “a systematic account of
  every unexplored branch” to “an explicit account of
  unexplored alternatives,” or equivalent ordinary prose.
- Introduction, Week 3 table: ask how to examine every
  state and avoid repeated work. The existing question
  “How can systematic exploration establish completeness?”
  obscures the independence of the two properties.
- Introduction, lines 69–71: replace the suggested split
  between complete search and best-first search with
  traversal order and best-first ordering, or otherwise
  avoid implying disjoint algorithm families.
- Introduction, line 128: include systematic alongside
  complete and optimal in the statement that guarantees
  concern particular variants under explicit assumptions.
- Notation: add complete, systematic, and examined entries
  or a short conventions paragraph. Preserve the state/node
  distinction and link to Week 1's substantive explanation.

## Small spillover inventory

These are integration findings, not authorization for an
unrelated later-chapter rewrite:

- Week 6 opening, line 10, calls Week 3's methods systematic
  as a group. Say tree/frontier exploration or simply the
  methods of Week 3.
- Week 7, lines 215–218, calls earlier methods and an exact
  inner solver complete. Use exact solving or a precisely
  stated local guarantee unless literal enumeration occurs.
- Week 7, line 257, “call a complete solver” likewise means
  an exact solver in context.
- Week 10, lines 296–301, can preserve the ordering-only
  argument for actual complete traversal, but “all required
  alternatives” should mean all states, not just branches
  necessary for the desired answer.
- OUTLINE.md, lines 553–568, explicitly records this as an
  unresolved decision. Replace it with the accepted user
  definitions and their consequences. The Week 2 outline
  still contrasts sound deduction with a complete solver;
  reconcile that usage too.
- Do not rewrite complete assignments, complete candidates,
  complete frontier, NP-complete, or exact source titles.

## Validation appropriate to the revision

This is a semantic audit, not a new algorithm implementation.
The claims were checked against the current pseudocode and
small counterexamples above. No program tests were required
for this read-only note.

After edits, inspect all remaining complete/systematic uses
in affected files, build the book, and run the repository's
source/title/link checker. If the depth-limit failure label
changes in pseudocode or checks, verify all result handling
uses the same label. Numerical examples and cost guarantees
should otherwise remain unchanged.

## Review of the applied patch

The concrete source patch was reviewed on 2026-11-11 against
the saved pre-edit files in
`/tmp/search-book-terminology-sf1qfbax/src/`.

Reviewed changed text in Weeks 1–7 and 10, introduction,
notation, and SUMMARY. Algorithm bodies are unchanged, so
this review did not rerun the algorithm suites.

The main repairs adopt the requested definitions correctly.
In particular, the patch distinguishes continued traversal
from goal stopping, includes successors beyond goals unless
the model makes them terminal, identifies path-local DFS and
IDDFS repetition, and keeps pruned descendants unexamined.
The finite-graph DFS and finite-branching BFS/IDDFS coverage
claims are sound under their stated continuation conventions.
No new algorithm error was found in those claims.

### Remaining substantive wording issue

Week 1, lines 577–581, defines examination as processing a
state for “goal or constraint tests, bounds, or successor
exploration.” This is too broad for the new statement in
Week 4, lines 249–252, that consistent A* is systematic.
A* can evaluate h when ranking several improved arrivals
before any of them is selected for expansion. Those repeated
bound computations would count as repeated examination under
the literal Week 1 wording, although only one nonstale entry
is substantively processed. The notation definition at lines
37–40 should be aligned with the same clarification.

Suggested replacement convention:

> Here, an examination is a search step that selects a
> state for goal or constraint testing, branch pruning,
> or successor exploration after duplicate and stale-record
> checks. Creating or ranking another candidate record is
> separate work. Reopening a state for another such step
> is a second examination.

This does not count unexamined descendants as examined and
does not erase generation or heuristic computation from
the effort accounting. It makes the unit of examination
consistent with the actual algorithms.

### Two smaller consistency fixes

1. Week 4, line 119, still says the cost-10 goal entry is
   stale “if it is ever examined.” Change examined to
   removed. The entry is rejected before state examination
   under the new convention.
2. Week 10, lines 299–300, says completeness survives when
   “all required alternatives are eventually considered.”
   Use “every state is eventually examined.” The current
   wording could retain the former solution-preservation
   interpretation and is weaker than the literal definition.

The remaining “complete failure” result name in Week 3 is
potentially confusing but is not a false search-completeness
claim: the text defines it as exhaustion without a cutoff.
Renaming it would require matching pseudocode result labels
and is optional for this terminology repair.

The external paper titles, complete assignments/candidates,
and NP-complete terminology were correctly preserved.
