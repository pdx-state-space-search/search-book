# Notation and assumptions

Notation describes a mathematical object; its representation
in a program is a separate choice. A state might be a tuple,
a bit vector, or a small structure, but equality must still
mean equality of all information relevant to future choices.

| Symbol or term | Meaning |
| --- | --- |
| s, t | States; s₀ is an initial state. |
| n (path search) | A node: a candidate record, often with path information. |
| n (instance size) | The size measure specified for that analysis. |
| successor | A state reachable by one legal transition. |
| c(s,t) | Cost of a transition from s to t. |
| g(n) | Cost of the path represented by node n. |
| g_best(s) | Cheapest path cost to s found so far. |
| h(s) | Estimated remaining cost to a goal. |
| h*(s) | Actual cheapest remaining cost; ∞ if no goal is reachable. |
| f(n) | A priority; for A*, g(n) + h(state(n)). |
| C* | Optimal objective value; path cost in pathfinding. |
| U | Objective value of a feasible incumbent, an upper bound. |
| L | A justified lower bound on the optimum. |
| b | Branching factor in a simplified uniform-tree analysis. |
| d | Depth of a shallowest goal. |
| m | Maximum depth, when it exists. |
| frontier / OPEN | Generated nodes still eligible for expansion. |
| expanded | A node whose successors have been considered. |
| incumbent | Best complete feasible solution found so far. |
| domain D(X) | Values still allowed for CSP variable X. |
| constraint | A relation specifying permitted combinations. |

## Costs and search-space assumptions

Unless a chapter says otherwise, examples of shortest-path
search have nonnegative edge costs, and goal heuristics are
zero. Guarantees about termination on an infinite graph
require additional assumptions. A common sufficient
condition is finite branching and edge costs bounded below
by a fixed positive number ε. Saying merely that every edge
has positive cost does not imply such a global lower bound.
Finite graphs and finite trees are stated explicitly when
an argument relies on finiteness.

A cost estimate h is **admissible** if h(s) ≤ h*(s). The
standard examples here also use h(s) ≥ 0. It is
**consistent** if h(s) ≤ c(s,t) + h(t) for every transition.
Consistency supplies an extra relation between neighbors;
admissibility alone does not imply it. An optimal graph
search using an inconsistent admissible heuristic may have
to expand a state again when a cheaper path is discovered.

A minimization bound L concerns the solution objective,
such as imbalance or path cost, rather than search effort
such as nodes examined or elapsed time. It is useful only
if justified by the stated model. A feasible incumbent
supplies U. A candidate that violates constraints supplies
neither a feasible answer nor a valid upper bound on the optimum.

## State, path and duplicate conventions

A state describes a possibility. A node is a record of one
occurrence of that state during search. It can retain how
the state was reached, including a parent link or other path
information. There can be many nodes for one state.
A path contains its sequence of transitions; its cost is the
sum of their costs.

Removing a repeated state from a search is safe only when
the retained information dominates the discarded work for
the problem being solved. Finding one cheapest path is not
the same task as enumerating every path. If legal moves or
costs depend on history, put the relevant history in the
state before applying ordinary state-based duplicate tests.

A tie-breaking rule decides the order of equal-priority
choices. The main guarantees usually permit many such
rules, but worked traces and reproducible experiments must
specify one. A priority queue may contain stale records;
a record's stored path cost must be checked against the
current best known cost when the algorithm uses lazy updates.

## Objectives and randomness

Optimization chapters minimize an objective unless they
explicitly say otherwise. A higher game utility is better
for the player whose perspective defines that utility.
Game-search and MCTS chapters state the perspective before
combining values from different turns.

Random restarts and independent random seeds are different
from independent problem instances. Experimental claims
state the unit being sampled. A timeout is a failed or
censored observation under its stated budget; it is not a
successful run whose runtime equals the cutoff.

The symbol ∞ is a mathematical sentinel rather than an
instruction to use a particular machine integer. Arithmetic
in pseudocode is exact unless numerical behavior is part of
the discussion.
