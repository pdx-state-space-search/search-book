# Week 1: Models, States, and Problems

A state-space search explores possible answers to a problem. The
answer might be a consistent assignment of values, a balanced
division of work, or a route through a network. We can often
describe the possibilities and check a proposed answer quite
directly. The difficulty is finding a useful answer among all
those possibilities.

This course treats search as a technique for solving useful
instances of NP-hard problems. Part I explains that motivation
and a complementary one: simple search rules can produce overall
behavior that deserves investigation. Part II develops the
models, representations, and evidence we need to reason about
what a search does. We will reuse three small examples throughout
the chapter and later weeks.

## Part I: Why Search?

### Three problems, three kinds of answer

#### Graph coloring: finding a feasible assignment

Map coloring gives a familiar motivation: neighboring regions
must have different colors. Represent each region by a vertex and
each shared border by an edge. The resulting **graph coloring**
problem assigns colors to vertices so that each edge has
differently colored endpoints. We will use this graph
representation throughout the book.

Take four vertices A, B, C, and D, with edges AB, AC, BC, and CD,
and allow red, green, or blue. A **constraint** states a
requirement on permitted combinations of choices; here each edge
requires different endpoint colors. A **feasible** assignment
satisfies every constraint.

[![A graph with edges AB, AC, BC, and CD has A red, B green, C blue, and D red. Every edge joins different colors.](figures/graph-coloring.svg)](figures/graph-coloring.svg)

*This graph coloring is feasible. A and D may share red because
there is no edge between them. Open the figure for a larger
view.*

An **assignment** gives colors to vertices; a **partial
assignment** leaves some vertices uncolored.

Start with no colors assigned. Choosing A=red and B=red already
violates AB. No choice for C or D can repair that violation while
those two assignments remain fixed, so we can abandon all
completions of that partial assignment. Choosing A=red, B=green,
C=blue, D=red instead gives a complete feasible answer.

We need the final assignment; the order in which the solver
assigned the colors is usually irrelevant to its validity. That
order still matters to the effort needed to find it. Starting
with strongly interacting vertices may expose conflicts earlier
than assigning isolated vertices first.

#### Number partitioning: improving a complete candidate

Divide weights 8, 7, 6, 5, and 4 into two groups. Minimize an
**objective**, the absolute difference between their sums. The
partition A={8,5,4}, B={7,6} is a complete candidate with sums 17
and 13, giving objective value 4. The partition A={6,5,4},
B={7,8} has sums 15 and 15, giving value zero. Because an
absolute difference cannot be negative, the second candidate is
optimal.

[![Two number partitions of weights 8, 7, 6, 5, and 4. Groups with sums 17 and 13 have imbalance 4; groups with sums 15 and 15 have imbalance zero.](figures/number-partitioning.svg)](figures/number-partitioning.svg)

*The objective in number partitioning measures the difference
between group sums. Both pictured partitions are feasible. Open
the figure for a larger view.*

Here every division of the items is feasible. A more constrained
version could limit each group's capacity or require specified
items to stay together. We would then seek a good objective value
among the divisions satisfying those restrictions. Scheduling
similarly combines feasibility requirements with objectives such
as finishing all work as early as possible.

A solver might construct partitions item by item or modify
complete partitions. Either way, the objective evaluates the
partition it returns. The sequence of exploratory changes need
not be part of that answer.

#### Pathfinding: finding a route

In **pathfinding**, an answer is a path through a network.
Suppose S has a direct road to G costing 20, and another route
S→A→G with each road costing 1. Reaching G supplies a route, but
the direct road is more expensive than the route through A. If we
minimize travel cost, the desired answer includes the sequence of
roads and its total cost. Merely reporting the final location G
loses the answer.

[![In a directed pathfinding graph, S leads directly to G with cost 20, or through A using two edges of cost 1 each.](figures/pathfinding.svg)](figures/pathfinding.svg)

*The two-edge path S→A→G costs 2; the one-edge path S→G costs 20.
Fewest edges and lowest cost are different goals. Open the figure
for a larger view.*

These tasks ask for different objects: an assignment, a
partition, and a path. Each has possibilities to explore, a
representation of those possibilities, and a way to judge
answers. We should choose a search method only after identifying
those features.

Graph coloring is a **problem**: the task allows different graphs
and available colors. Our particular graph and its three colors
specify one **instance**. The weights and roads above likewise
fix instances of their respective problems. We will develop this
distinction in Part II; for now it lets us distinguish a general
task from the particular data a search is working on.

### Combinatorial growth and practical limits

#### Counting complete candidates

Return to our graph coloring instance. If n is the number of
vertices and k the number of available colors, there are kⁿ
complete assignments before applying edge constraints. Our
four-vertex, three-color instance has 3⁴=81 assignments. With
twenty vertices there are 3²⁰=3,486,784,401. A compact instance
can describe billions of possible answers.

The count includes invalid colorings. Listing every assignment
and then checking its edges is nevertheless a correct way to find
a coloring or establish that none exists on a finite graph. It
becomes expensive because the list grows so rapidly. A better
search can reject A=red, B=red immediately, without constructing
every assignment to the remaining vertices. That rejection uses a
requirement shared by all completions.

#### Growth against a resource budget

Adding one vertex multiplies the unconstrained count by k. For
three colors, ten more vertices multiply it by 3¹⁰=59,049. At
first several extra choices seem inexpensive. Near a fixed time
or memory budget, a few more choices can make the instance
impractical. The required work can grow smoothly while crossing a
practical limit abruptly.

Faster hardware moves the boundary. If a computation doubles with
each added binary choice, a millionfold speedup buys about twenty
more choices at the same time budget, since 2²⁰ is about one
million. The improvement is valuable; another twenty choices
demand another factor of roughly a million. Reducing the work
through constraints or better choices can also move the boundary.
Neither observation specifies how far any particular solver will
get on every instance.

A count of possible candidates is not a proof that every
algorithm must examine them all. Nor do all candidates take the
same work to process. Part II will distinguish the size of the
possibility space from the work a solver actually does.

#### NP-hard problems and useful instances

Complexity theory groups problems by the computational resources
needed as instance size grows. Before discussing difficulty in
terms of n, always define what n measures. It might count graph
vertices, variables, items, or bits in an input representation. A
**complexity class** collects problems sharing a stated resource
property.

**P** consists of decision problems solvable in polynomial
time. A decision problem asks a yes-or-no question, such as
whether a graph can be colored with three colors.
**NP** consists of decision problems for which a yes answer
can be supported by a polynomial-length certificate checked
in polynomial time. A proposed graph coloring is a
certificate: check that each vertex has an allowed color
and every edge has differently colored endpoints. Being in NP describes verification;
it does not by itself imply hardness. Every problem in P
also belongs to NP: a verifier can simply solve it directly.

A polynomial-time **reduction** translates instances of one
decision problem into another while preserving yes-answers and
no-answers. A problem is **NP-complete** when it satisfies two
conditions: it belongs to NP, and every problem in NP reduces to
it in this sense. This definition does not require proving that
the problem lies outside P. Whether any problem in NP lies
outside P is the open question of whether P=NP. If P=NP,
NP-complete problems would have polynomial-time algorithms too.
[Karp (1972)](bibliography.md#karp-1972) develops this reduction
framework.

An **NP-hard** problem is at least as hard as all problems in NP
under the relevant reduction; it need not itself belong to NP or
be a decision problem. For optimization, we can often establish
hardness through a decision question about achieving a specified
objective threshold.

Conversely, a polynomial-time algorithm for any NP-complete
problem would imply P=NP. NP-hardness therefore does not
constitute a proof that every algorithm must take exponential
time. Nor does a count of kⁿ candidates prove that every solver
must examine them all. The significance is that we cannot count
on a known efficient general algorithm, so exploiting structure
in the instances becomes essential to practical work.

An instance may have constraints that nearly force its answer,
repeated subproblems we can reuse, or bounds that exclude most
candidates. Another instance of the same size may provide little
such help. Unsatisfiable instances can be difficult because the
search must justify ruling out every possibility. Proving
optimality can require much more work than finding a good
candidate.

A practical solver's limit depends on this structure as well as
size. There is no universal vertex count or variable count at
which a problem family becomes intractable. We want methods that
solve useful instances and experiments that reveal where those
methods succeed and fail.

### Emergent behavior from simple search rules

#### Local changes and global patterns

Return to our four-vertex coloring instance, with edges AB, AC,
BC, CD and colors red, green, blue. Instead of constructing a
partial coloring, start with every vertex red. Call an edge a
**conflict** when its endpoints share a color. All four edges
initially conflict.

Consider a local repair rule: choose a vertex involved in a
conflict, then give it a color minimizing conflicts on the edges
touching it. Here choose C first, using blue rather than green to
break the tie. That resolves AC, BC, and CD. Choose B next and
give it green, resolving the remaining AB conflict without
creating another.

| Change | A | B | C | D | Conflicting edges |
| --- | --- | --- | --- | --- | ---: |
| Initial assignment | red | red | red | red | 4 |
| Recolor C | red | red | blue | red | 1 |
| Recolor B | red | green | blue | red | 0 |

The resulting assignment is the feasible coloring pictured
earlier. Each update used neighboring colors; the whole
assignment was assembled through their interactions. Repair
methods develop this idea further; see [Minton et al.
(1992)](bibliography.md#minton-et-al-1992).

**Emergent behavior** concerns patterns at the level of a
whole system that arise through interactions among simpler
components or rules. [Mitchell (2006), §2](bibliography.md#mitchell-2006)
discusses this perspective in complex systems. In search,
it directs our attention to how individual choices combine
into a trajectory: a sequence of candidates considered by
the solver. A small trace makes those interactions visible;
understanding larger searches requires more than inspecting
one update rule in isolation.

#### Understanding the resulting behavior

Interactions can frustrate a plausible rule too. Consider a
separate graph containing just two adjacent vertices and only red
and blue. Start with both vertices red. If each simultaneously
switches color whenever it conflicts with its neighbor, both turn
blue. The conflict remains, so both turn red next. The joint
behavior is a repeating cycle, although either update alone would
have resolved the conflict.

The order of changes, the information used, and the structure of
the instance affect the resulting behavior. Observing a
coordinated solution, a repeating pattern, or stalled progress
raises questions about the mechanism producing it. One successful
trajectory does not establish that all starts will succeed; an
unsuccessful run does not establish that no solution exists.

This gives search two connected subjects of study: the
computation demanded by a large possibility space, and the
behavior produced by a mechanism exploring it. We need a precise
account of that space and mechanism to investigate either
subject. That is the purpose of Part II.

## Part II: Modeling and Assessing Search

### Problems, instances, and models

#### A problem and one of its instances

A problem describes a task with parameters that can vary. Graph
coloring specifies what to find, while leaving the graph and
available colors to be supplied. An instance fixes those
parameters: our graph with edges AB, AC, BC, CD and its three
colors is one instance. Changing the graph or available colors
gives another.

Think of the problem as the collection of allowed instantiations
of its parameters. This includes instances with feasible answers
and instances without them. In number partitioning, the weights
are parameters; our five weights specify one instance. A search
run tackles one instance, not the whole collection at once.

Keep these levels separate from a complexity class such as NP: an
instance supplies particular data, a problem collects instances
of one task, and a class collects problems with a stated
computational property. An algorithms textbook supplies the
fuller formal treatment of problem descriptions.

#### What the model specifies

A **model** specifies the choices, restrictions, and outcomes
relevant to a task. For graph coloring, it names vertices,
available colors, and edges. For number partitioning, it lists
weights and defines the imbalance. For pathfinding, it gives the
road network, start and goal, and travel costs.

The answer sought matters too. Finding any coloring with a fixed
color set is different from finding a coloring using the fewest
colors. A pathfinding model may ask for any route, the fewest
roads, or the lowest travel cost. The model must say which
question a proposed answer is meant to settle.

#### How a model can miss the intended task

Models deliberately simplify. A schedule may ignore setup time
between tasks. If setup time affects feasibility or completion
time, a solver can correctly optimize its model and still return
a poor real schedule. A route model that treats a closed road as
usable can recommend an unusable path.

Checking the solver therefore has two parts: does the model
capture the relevant requirements, and does the program correctly
solve that model? A search method cannot compensate for
requirements that were never represented.

### States and possible changes

#### Choosing what a state represents

A **state** represents one possibility in the search. It might be
a partial coloring, a complete partition, or a location and
remaining fuel. A **state space** contains the states admitted by
the representation. A **transition** changes one state into
another. These are the basic modeling ideas developed in [Russell
and Norvig (2020), chapters
3–4](bibliography.md#russell-norvig-2020).

The state space depends on the solver's design. A constructive
coloring search can start with an empty assignment and make
transitions by assigning the next vertex. A repair search starts
with every vertex colored and makes transitions by recoloring one
vertex. Its space includes assignments violating the constraints:
candidates to improve that cannot yet be returned as feasible
answers. The model's requirements and the solver's permitted
intermediate states have distinct roles.

For route finding, specify an initial state, applicable actions
and their resulting states, and a **goal test** that recognizes
an acceptable destination. Transition costs can record travel
expense. In assignment search, a transition may instead mean
making an additional decision; it need not be an action to
perform in the world.

#### Retaining enough information

A state must retain the information relevant to future choices
and evaluation. For constructive coloring, the partial assignment
determines which additional assignments are permitted. For route
finding with limited fuel, location alone is insufficient: being
at A with twelve liters and being at A with one liter can allow
different continuations. If a route rule prohibits revisiting
locations, the visited set must also be represented.

This sufficiency of the present state is related to the **Markov
property**: the present state retains the history needed to
determine future behavior. In a stochastic model, where outcomes
involve randomness, this concerns their distribution rather than
knowing exactly which outcome will occur; see [Sutton and Barto
(2018), §3.1](bibliography.md#sutton-barto-2018). Including
additional history can enlarge the state space substantially.
Omitting necessary history changes the problem that the solver
actually explores.

#### Generating possibilities on demand

An **explicit graph** stores its vertices and edges directly.
Search often uses an **implicit graph**: represent a state and
generate its successors only when needed. A **successor** is a
state reached by one permitted transition. In graph coloring,
generate extensions of the current assignment. In number
partitioning, generate other partitions by moving an item between
groups. In route finding, generate locations reachable by one
outgoing road.

This avoids first listing an enormous space, but places a
correctness obligation on the generator. Missing choices can hide
an answer, and illegal choices can produce invalid results. A
restricted move set can also disconnect the space, making some
candidates unreachable from the chosen start.

### States, records, and paths

#### What the program stores and processes

The solver operates on records: it creates a candidate, checks
it, retains information about it, and generates further
candidates from it. We call such a record a **node**. A node can
contain a state, a link to the record that produced it, and other
information the algorithm needs. Such a link is a **parent
link**. A **path** records a sequence of transitions; parent
links can retain how a state was reached. Several nodes can
represent the same state.

The **state graph** has states as vertices and transitions as
directed edges. The **search tree** draws the relationships
between records generated from a starting state. A child record
represents an additional transition from its parent. Processing a
node means doing work on its record; the program need not first
construct or store the entire drawn tree.

#### Repeated arrivals and cycles

In our graph coloring instance, suppose the solver permits
assigning A and B in either order. A=red then B=green reaches the
same partial assignment as B=green then A=red. The search tree
can have two records for that assignment. A fixed assignment
order avoids this particular duplication.

For a separate route example, let S have roads to A and B, and
let both A and B have roads to G. The routes S→A→G and S→B→G
produce different records for the state “at G”:

[![A state graph merges two routes to G; a search tree has a distinct G node for each route.](figures/states-and-paths.svg)](figures/states-and-paths.svg)

*The state graph contains one G; the search tree has two records
reaching it. Open the figure for a larger view.*

Repeated states can sometimes be merged safely. For finding one
feasible coloring, two arrivals at the same partial assignment
have the same remaining possibilities. For minimum-cost routing,
a cheaper arrival can dominate a more expensive one when their
possible continuations are identical. Keeping only an expensive
arrival can lose an optimal answer. Enumerating every path
requires a different policy again.

A **cycle** returns to a state already encountered. A graph with
roads A→B and B→A admits arbitrarily long paths through only two
states. Local repair can likewise cycle among assignments. Some
spaces are finite, such as all colorings of a fixed graph using a
fixed finite color set. Others are infinite, such as states
containing an unbounded counter. Even a finite graph can unfold
into an infinite tree of paths. The space's finiteness and a
procedure's termination are separate questions.

### Answer quality and search effort

#### What an objective measures

The word “cost” can refer to different quantities. We will keep
three meanings separate:

| Quantity | Examples | What it measures |
| --- | --- | --- |
| Objective value | Partition imbalance, schedule length | Quality of a candidate |
| Path cost | Sum of road travel costs | Quality of a route or action sequence |
| Search effort | Nodes examined, seconds, peak memory | Resources used by the solver |

Path cost is one possible objective. In our original pathfinding
instance, S→A→G costs 2 regardless of how many other routes the
solver investigated first. In our number partitioning instance,
imbalance zero is optimal regardless of how many item moves or
partial assignments led the solver to discover it. Charging one
unit per exploratory move would define a different optimization
problem.

#### Counting the program's work

A **generated** node has been produced as a candidate for
consideration. An **expanded** node has had its successors
considered. A solver might generate many duplicate states and
expand only a few of those records. Reporting both counts can
expose work hidden by a single headline number.

Let b be the number of children per node in a regular tree, and
let d be its depth, counting transitions from the root. If each
node has exactly b children, the total number of nodes through
depth d, counting the root at depth zero, is

**1 + b + b² + … + bᵈ = (b^(d+1) − 1)/(b − 1), for b>1.**

In a fixed-order coloring search, depth d means that d vertices
have been assigned. Each unconstrained choice has three children.
The leaves count complete assignments; internal nodes count
partial assignments examined along the way. Pruning a partial
assignment can remove an entire subtree of completions. Rejecting
a branch together with its completions is **pruning**.

Consider the simpler binary tree, with b=2. At an illustrative
constant rate of one million nodes per second, exhausting the
tree takes approximately:

| Depth | Total nodes examined | Time |
| ---: | ---: | ---: |
| 20 | 2,097,151 | 2.1 seconds |
| 30 | 2,147,483,647 | 35.8 minutes |
| 40 | 2,199,023,255,551 | 25.5 days |

These counts include partial candidates as well as complete ones.
The assumed processing rate converts a count into an illustrative
time; a real rate depends on the work performed on each record.

[![Illustrative total search nodes versus depth for regular trees with two and four children per node. A one-million-node budget permits depth 18 in the two-child tree and depth 9 in the four-child tree. Both curves cross the budget and continue growing.](figures/search-growth.svg)](figures/search-growth.svg)

*Reducing branching extends the useful depth. Both examples still
reach the same fixed resource limit. The curves are mathematical
illustrations, not measured solver results. Open the figure for a
larger view.*

The figure models successful pruning by reducing a uniform
branching factor from four to two. Below a budget of one million
nodes, the four-child tree reaches depth 9 and the two-child tree
reaches depth 18. That is a substantial gain. Further growth
still exceeds the budget in both cases. Real pruning is irregular
and instance-dependent; these curves are not a prediction of its
effect on every problem.

Depth measures decisions in the chosen search representation. It
need not equal the chosen measure of instance size. In graph
coloring with a fixed vertex order, each decision colors one more
vertex. Other representations can change branching, depth, and
the work done per node.

#### From counts to time and memory

A node count is a machine-independent measure of search work
under a specified counting rule. For a fixed algorithm and
ordering, changing processor speed changes elapsed time without
changing the number of candidates it considers. This makes counts
useful for comparing search policies and understanding growth
beyond one particular machine.

The usual analysis assumes polynomial-time work per node in the
chosen instance-size measure n. If N nodes are examined and all
work charged to each node is bounded by a polynomial p(n), total
time is O(N·p(n)). This must include generating successors and
evaluating estimates; an expensive inner search cannot be hidden
inside a cheap node operation.

Two solvers can examine the same number of nodes while taking
different amounts of time because one copies large states or
computes a more expensive estimate. A method examining fewer
nodes can still be slower. Memory depends on what the solver
retains, which can be much less than all the records it has ever
generated. Node counts help explain behavior; time and peak
memory determine whether a run fits its budget. [Week
8](08-engineering.md) develops these implementation and
measurement issues.

### Evidence and guarantees

#### A feasible answer and a best answer

A feasible answer establishes that the modeled requirements can
be satisfied. An optimal answer additionally has the best
objective value among feasible answers. Finding a coloring,
proving that none exists, and finding a coloring using the fewest
colors require different evidence.

The returned object must support the claimed answer. A coloring
lists vertex colors; a partition identifies its groups; a route
includes its roads. Checking such an answer establishes its
feasibility and objective value. Claiming that no better answer
exists requires further reasoning.

#### Completeness, termination, and failure

A search is **complete** if it eventually examines every state
in its state space. It is **systematic** if it examines each
state at most once. A search with both properties examines
every state exactly once. For traversal from an initial state,
we mean the states reachable from that initial state.

Here, examining a state means selecting it for substantive
search processing after duplicate or stale-record filtering.
Generating and ranking records are counted separately as
work; discarding a duplicate record is not another state
examination. Selecting the same state again through another
path is another examination.

Completeness concerns eventual coverage. In an infinite space,
every particular state might eventually be examined without
the traversal ever finishing. Conversely, a systematic search
can miss states: avoiding repetition does not ensure coverage.

A solver may stop at its first answer. That run need not examine
every state, even if continuing its traversal would do so.
Sound pruning can also establish an answer without examining
the states in excluded branches. We distinguish those answer
guarantees from complete enumeration. A disappointing candidate
or a long run without success establishes neither impossibility
nor optimality.

Guarantees belong to particular algorithms under explicit
assumptions. Path-search guarantees also depend on costs and
goal-test timing. We will develop those details with the
algorithms in [Weeks 3](03-systematic.md) and
[4](04-best-first.md); the [notation reference](notation.md)
collects the conventions. Each guarantee must justify both the
work explored and any alternatives safely discarded.

#### Bounds and an optimality certificate

For minimization, an **incumbent** is the best feasible complete
candidate found so far. Its objective value U is an upper bound
on the optimum C*: C*≤U. A justified lower bound L establishes
L≤C*. Together they give

**L ≤ C* ≤ U.**

In our number partitioning instance, the partition with sums 17
and 13 has imbalance 4 and supplies U=4. Nonnegativity supplies
L=0. Finding the partition with sums 15 and 15 makes U=0, proving
optimality because the bounds meet. A constraint optimization
solver can return a useful feasible answer while still working to
close this gap. A candidate violating the hard constraints
supplies no feasible upper bound.

Before choosing a method, identify the answer wanted, the states
and transitions representing its possibilities, and the resources
available for exploring them. Then ask what structure the model
exposes. Can a constraint rule out a partial assignment? Can a
bound show that a branch cannot improve the incumbent? Can an
inexpensive change improve a complete candidate?

The next chapter develops constraints as a language for
expressing restrictions and deriving their consequences. Later
methods will organize traversal, pruning, and heuristic
repair. Their practical value is how far they extend the range of
instances we can solve, together with the evidence they provide
about the answers returned.

## Further reading

- Russell and Norvig, [*Artificial Intelligence: A Modern
  Approach*](bibliography.md#russell-norvig-2020), 4th US edition
  (2020), chapters 3 and 4. A longer treatment of problem
  formulation, path search, and local optimization.
  **Reading suggestion:** Use chapters 3 and 4 for a second
  explanation of models and search; this course text supplies
  the necessary basics.
- Karp, [“Reducibility Among Combinatorial Problems”](bibliography.md#karp-1972)
  (1972). Develops the reduction framework behind
  NP-completeness. **Reading suggestion:** Consult it for
  the formal theory beyond this chapter's informal treatment.
- Mitchell, [“Complex Systems: Network Thinking”](bibliography.md#mitchell-2006)
  (2006). Discusses emergence and information processing
  through interacting components. **Reading suggestion:**
  Start with §2 for the local-to-global viewpoint used here.
- Khemani, [*Search Methods in Artificial Intelligence*](bibliography.md#khemani-2024)
  (2024). Covers search spaces and a wider range of methods.
  **Reading suggestion:** Its search-space material offers
  another introduction if you have access to the book. The
  publisher TOC informed this book's topic selection;
  access to the book is not required for this course text.
