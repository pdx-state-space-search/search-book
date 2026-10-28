# Week 1: Models, States, and Problems

How can a system choose what to do when it cannot jump directly
from its current situation to its goal? A route planner must
consider roads between locations. A robot must account for how
its actions change the world. A game program must consider the
moves available to both players. A useful first step is to
model the task as situations and possible transitions.

A search algorithm operates on the representation we provide:
states, actions, transition rules, and a test for success.
That representation shapes what it can solve and what its
answer means. Before improving an algorithm, we need to know
exactly which problem it is solving.

## A problem as a model

A search problem has five basic ingredients:

- A **state space**: the situations that may be considered.
- An **initial state**: where the process begins.
- **Actions**: choices available from each state.
- A **transition model**: the result of applying an action.
- A **goal test**: whether a state meets the objective.

When actions have different costs, the model also assigns a
cost to each transition. A path's cost is the sum of its
transition costs. Unless stated otherwise, our pathfinding
examples use nonnegative costs.

Consider a route planner for a small road network. States
might be towns, actions roads leaving a town, and transitions
travel along those roads. The initial state is the starting
town. The goal test checks whether the current town is the
destination. To minimize travel time, each road's cost is its
travel time rather than its physical length.

A model deliberately simplifies. A real road network has
traffic, closures, weather, and uncertain travel times. A toy
model may ignore them. Leaving out irrelevant detail can make
a problem easier to solve. But if an omitted detail changes
which route is best, the model may no longer answer the real
question. Search can be correct with respect to a model and
still produce a poor recommendation when the model is
inadequate.

In our basic model, a transition is deterministic: given a
state and an applicable action, its result is fixed. Some
actions instead have several possible outcomes. A robot may
slip; a card draw may have several results. Representing those
tasks faithfully requires additional machinery, such as
probabilities or adversarial choices. We begin with the simpler
model to understand the role of search order.

## State and history

A state summarizes everything about the past that matters for
the future. Two histories can share a state when future legal
choices, consequences, and goal evaluation are equivalent.

For route finding, "at Pine" may be enough when road costs
and availability depend only on location. With limited fuel,
location alone is insufficient. A state may need both location
and remaining fuel: "at Pine with 12 liters." A deadline may
require including time. Leaving fuel out can make an impossible
route look possible.

This is related to the **Markov property**: the present state
contains the information needed to determine relevant next
transitions without consulting the whole past. If a rule says
that a robot may not visit a room twice, its current room is
not enough. A state containing the current room and the set of
visited rooms makes the rule checkable, at the price of a much
larger state space.

A distinction between states is useful only if it matters to
the task. If two identical boxes can exchange names without
changing any legal action or objective, retaining their names
may create artificial duplicates. Removing a distinction
requires an argument that the remaining representation still
captures the future. [Week 8](08-engineering.md) returns to
this issue as canonicalization.

An **instance** is one specified member of a problem family.
"Find a minimum-cost path in a weighted graph" describes a
family. A particular graph, start, destination, and edge costs
form an instance. Performance on one instance is evidence
about that instance, not automatically the whole family.

## Paths, nodes, and states

A **path** is a sequence of transitions. A **state** is the
situation at a point along that sequence. A search **node**
usually combines a state with information about a path that
reached it, such as its parent, depth, and path cost.

Suppose S can reach G through either S–A–G or S–B–G. When
history does not affect future choices, both routes reach the
same state G. An unmerged search tree nevertheless has a
separate node for each route. Its two G nodes represent two
paths to one state.

[![A state graph merges two routes to G; a search tree has a distinct G node for each route.](figures/states-and-paths.svg)](figures/states-and-paths.svg)

*The state graph identifies one shared state. The search tree
unfolds the paths by which that state can be reached.*

Two nodes for one state may have different path costs. For
minimum-cost search, a cheaper arrival can dominate a more
expensive one if all relevant future choices are the same.
Keeping only the expensive arrival can lose the cheapest
solution. Merging arrivals is also unsafe if the representation
omits history that affects future choices.

The **state graph** is the abstract network defined by the
model: vertices are states and directed edges are legal
transitions. It exists mathematically even if never stored.
A search tree unfolds paths from the initial state and can be
generated a little at a time.

Cycles make the distinction striking. If A leads to B and B
back to A, paths include A–B–A–B and arbitrarily longer
repetitions. The graph has two states, but the path tree is
infinite. An algorithm can repeatedly explore this infinite
tree even though the underlying graph is finite. A rule for
handling repeated states is part of an algorithm, not an
optional implementation detail.

## Explicit and implicit graphs

An **explicit graph** lists states and transitions directly.
Many search problems instead define a graph **implicitly**:
encode a state and generate legal successors only when needed.

In a sliding-tile puzzle, a board configuration is a state.
An action slides a neighboring tile into the blank. The
successor operation examines the blank's neighbors and creates
the resulting boards. We do not first list every possible
board. Similarly, a game program generates legal moves from
a position rather than storing all positions in advance.

An implicit representation saves storage when the algorithm
explores only a small part of the space. It also places a
correctness obligation on the successor generator. Omitting a
legal transition can hide a solution. Introducing an illegal
transition can produce an answer that cannot be executed.
A fast search over the wrong graph solves the wrong problem.

Some state spaces are finite. A puzzle with fixed pieces and
cells has a finite number of configurations, even if that
number is enormous. Others are infinite: an unbounded counter
can give infinitely many states. A finite graph can in
principle be exhausted. An infinite one cannot be entirely
inspected in finite time.

This does not prevent useful guarantees in infinite spaces.
An algorithm might eventually examine every state at every
finite depth. If a solution has finite depth, that can be
enough to find it. It may still run forever when no solution
exists. Finding an existing solution and terminating with a
proof of failure are different promises.

## Growth makes simple search expensive

Suppose each node has exactly b children and we explore
through depth d, with the initial node at depth zero. Without
merging or pruning, the total number of nodes is

**1 + b + b² + … + bᵈ.**

For b > 1, the sum is (b^(d+1) − 1)/(b − 1). With branching
factor 4 and depth 8, it is 87,381 nodes. At depth 12, it is
22,369,621. Four extra levels increase the dominant term by
4⁴ = 256. At an illustrative rate of one million nodes per
second, the latter count needs about 22 seconds. At depth 20,
the same model has about 1.47 trillion nodes, requiring
roughly 17 days at that unchanged rate.

These are counts for a uniform tree, not measured predictions
for arbitrary problems. Real branching varies. Duplicate
states can merge. Constraints can rule out branches. Memory
or expensive successor generation can lower throughput. The
calculation explains why a small increase in depth can
nevertheless change what is practical.

The meaning of a step matters too. Moving one square and
moving through an entire corridor give different depths and
branching factors. A macro action may reduce depth while
making successor generation harder. It must also preserve
solutions: replacing all ordinary actions with an incomplete
set of macros can delete necessary paths.

Combinatorial growth is not limited to paths. Assigning one
of k values to each of n variables gives kⁿ complete
assignments before considering constraints. Ordering n
distinct objects gives n! permutations. An input can be small
even when its implied space of alternatives is huge. Search
tries to exploit structure so that only a useful fraction of
those alternatives must actually be examined.

## What counts as a solution?

A valid solution and an optimal solution are different goals.
In an unweighted graph, path length counts edges. In a
weighted graph, path cost adds edge costs. Five cheap edges
can cost less than three expensive edges.

**Completeness** means that an algorithm eventually finds a
solution whenever one exists, under its stated assumptions.
**Optimality** means that the solution it returns has the
best objective value. Neither follows merely from calling a
procedure a search algorithm.

A method following one infinite branch can miss a solution
on another branch. A method stopping at the first goal can
return an expensive route while a cheaper one remains
unexplored. Equal positive edge costs make fewest-edge and
minimum-cost paths coincide; unequal costs need different
reasoning.

Assumptions also govern termination. In an infinite graph,
positive costs alone do not ensure that cost-ordered search
will reach every more expensive node: costs could shrink
along an infinite path. A common sufficient assumption is a
fixed positive lower bound on every transition cost, together
with finite branching. On a finite graph, an argument can
instead use finite duplicate-aware exploration.

For a feasibility problem, finding one satisfying assignment
is enough. For an optimization problem, an **incumbent** is
the best feasible complete solution found so far. Its value
bounds what the optimum can be, but does not prove that no
better solution exists. A lower bound or exhaustive argument
can provide that missing evidence. A useful practical method
may return an incumbent before it can certify optimality.

To make this concrete, imagine minimizing the difference
between the sums in two groups of positive integers. A split
with difference 4 is a feasible candidate and establishes
that the optimum is at most 4. Since the difference is never
negative, zero is a lower bound. Until another argument
closes the gap, the optimum might be 0, 1, 2, 3, or 4,
subject to properties of the instance. Finding a split with
difference zero immediately proves optimality: the upper and
lower bounds coincide.

## Feasibility and computational difficulty

Complexity theory classifies problem families as input size
grows. **P** consists of decision problems solvable in
polynomial time by a deterministic algorithm. A polynomial
bound, such as n² or n³, is an abstraction of scalability,
not a stopwatch prediction. Constants, representation, and
machine costs still matter.

**NP** consists of decision problems whose yes-instances have
certificates of polynomially bounded length that can be
verified in polynomial time. A certificate must establish a
yes-answer; no certificate can make the verifier accept a
no-instance. Being in NP does not mean that a problem is
known to be hard.

For reachability in an explicit finite graph, a simple path
is a short certificate: check each edge and its destination.
Such a path needs at most |V| − 1 edges if the start and goal
are distinct. Reachability is also in P; easy verification
does not imply difficult discovery. For graph coloring with
a fixed number of colors, a complete color assignment is a
certificate that can be checked edge by edge.

An **NP-complete** problem is in NP and every problem in NP
can be transformed to it by a polynomial-time reduction. A
reduction translates instances while preserving yes-answers
and no-answers. If any NP-complete problem has a polynomial
time algorithm, every problem in NP does, and P = NP. Whether
P = NP remains open.

**NP-hard** means at least as hard as all problems in NP under
the stated kind of reduction. An NP-hard problem need not
itself be a decision problem or belong to NP. The term does
not mean impossible or unsolvable. Exact algorithms can solve
small or structured instances, and useful approximations or
heuristics may work on much larger ones.

Input representation matters. A number written in binary can
represent a large magnitude with few bits. An algorithm
polynomial in that magnitude can be exponential in its bit
length. Likewise, an implicit graph may have exponentially
many states relative to the compact instance that defines it.
We must say what n measures before interpreting a complexity
bound.

Worst-case complexity also leaves room for instance structure.
A family can contain both easy and hard instances. Constraints
may nearly force every choice in one instance while providing
little information in another. A good experiment therefore
identifies the instances being studied instead of treating a
complexity classification as a measured runtime forecast.

## From models to algorithms

A model identifies choices and consequences. A search method
chooses the order in which to investigate those choices and
which information to retain. Three practical questions follow:

- Can the model expose impossible choices before a complete
  candidate is built?
- Can a path or objective estimate identify promising work?
- Can we discard work without losing a required solution or
  guarantee?

The next chapter develops constraints as a way to express and
propagate restrictions. [Week 3](03-systematic.md) develops
systematic exploration. These are complementary views of the
same problem: reasoning about a large space without
materializing or examining all of it.

## Further reading

- Russell and Norvig, [*Artificial Intelligence: A Modern
  Approach*](https://aima.cs.berkeley.edu/), 4th US edition
  (2020), chapter 3.
  A longer introduction to problem formulation and search
  vocabulary. The course book supplies the necessary basics.
- Karp, [“Reducibility Among Combinatorial Problems”](https://doi.org/10.1007/978-1-4684-2001-2_9)
  (1972). The foundational reduction framework; an extension
  for readers who want the formal complexity theory.
- Khemani, [*Search Methods in Artificial Intelligence*](https://www.cambridge.org/core/books/search-methods-in-artificial-intelligence/contents/D2DE03267943183B66EF635E65048691)
  (2024), particularly its search-space coverage. The publisher
  TOC informed this book's topic selection; access to the book
  is not required for this course text.
