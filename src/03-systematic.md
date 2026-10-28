# Week 3: Systematic Search

Systematic search retains an explicit account of alternatives.
It may explore some choices first because they look promising,
but it does not treat a disappointing guess as proof that the
remaining choices can be forgotten. With appropriate bounds
and duplicate handling, that discipline supports completeness
and sometimes a proof of optimality.

This chapter develops depth-first search, breadth-first
search, depth limits, iterative deepening, and branch-and-bound.
The methods differ in what they retain and which work they
select next. Their guarantees depend on the space being
searched and the objective being optimized.

Let b be an upper bound on branching, d the depth of a
shallowest goal, and m the greatest depth explored in a
bounded search tree. Depth counts transitions, not cost.
We use g for accumulated path cost. The distinction between
states and paths from [Week 1](01-models.md) remains essential:
a finite graph can unfold into an infinite tree of paths.

## Depth-first search

Depth-first search (DFS) pursues one branch until it reaches
a goal, a dead end, or a stated limit. It then backs up to an
ancestor with an unexplored successor. A recursive traversal
and an explicit last-in, first-out stack express this same
selection policy.

Suppose successors are tried in alphabetical order. In a
graph with S→A, S→B, A→C, C→G, and B→G, DFS follows
S, A, C, G and returns the three-edge route before considering
the two-edge route through B. Finding a goal is enough for
reachability. It does not establish that the route is shortest.

A recursive description keeps the current path and considers
one successor at a time:

```text
search(state, path):
    if goal(state): return a copy of path
    for each legal successor child in the chosen order:
        if child is not already on path:
            extend path with child
            result := search(child, path)
            remove child from path
            if result is a solution: return result
    return failure
```

The path-local test rejects cycles on the active route. Its
soundness here relies on memoryless legal futures and on
seeking one reachable goal: a cycle can be removed from a
successful route without changing what remains possible.
If a rule depends on earlier visits, that history belongs
in the state before applying this reasoning.

On a finite search tree, DFS eventually examines every node
unless it stops with a solution. Finite branching alone is
insufficient. An infinite chain below A can keep DFS busy
forever while a goal waits below B. A cycle can cause the
same failure in naive tree search over a finite graph.

For reachability in a finite graph, a global reached set
can prevent repeated expansion. Marking states when generated
avoids pushing several copies of the same state. Any one
arrival suffices for ordinary reachability, so suppressing
later arrivals preserves that task. It does not preserve the
task of enumerating all paths, and it does not by itself
solve minimum-cost search.

The memory difference matters. A tree DFS retaining pending
siblings uses O(bm) search records. Incremental successor
generation can reduce retained records toward the active
path plus generator state. A global reached set instead grows
to O(|V|); parent records add comparable storage. Copying an
entire path into every pending record adds still more memory.
A low-memory claim must identify the representation.

For a bounded tree with b>1, worst-case node count is O(b^m).
For a finite explicit graph, duplicate-aware DFS takes
O(|V|+|E|) time with adjacency lists and constant-time
reached-set operations. These descriptions measure different
inputs: an unfolded tree can contain many routes through
one graph vertex.

## Breadth-first search

Breadth-first search (BFS) examines paths in nondecreasing
depth. A first-in, first-out queue implements this order.
When a depth-k node generates children, they join the queue
behind all remaining depth-k nodes.

For graph reachability, mark states when first generated
and retain a parent link for reconstructing the result.

```text
frontier := queue containing the initial state
reached := set containing the initial state
while frontier is not empty:
    state := remove front of frontier
    if goal(state): return its reconstructed path
    for each successor child:
        if child is not in reached:
            add child to reached
            record state's parent link for child
            append child to frontier
return failure
```

In the earlier graph, removing S leaves [A,B]. Removing A
leaves [B,C]. Removing B discovers G, leaving [C,G].
When C is removed, G is already reached, so C does not enqueue
it again. Removing G returns S→B→G at depth two.
DFS's route through A has depth three.

Why is BFS shallowest-first? Initially only the root is
queued. Inductively, every generated child has depth one more
than its parent, and the FIFO rule leaves all shallower
queued nodes ahead of it. Thus no depth-(k+1) node is removed
before the remaining depth-k nodes. The first goal removed
has minimum depth.

Equal positive transition costs make minimum depth and
minimum path cost the same objective. Unequal costs do not.
A direct edge costing 20 is shallower than a two-edge route
costing 2, but is worse for a minimum-cost task.
[Week 4](04-best-first.md) replaces depth order with cost order.

With finite branching and a goal at finite depth, BFS is
complete: only finitely many nodes precede the goal's layer.
It may run forever without a goal in an infinite graph.
On a finite graph with a reached set, it terminates whether
or not a solution exists.

Goal-test timing changes the precise tree-space estimate.
The pseudocode tests on removal. Before the first goal at
depth d is removed, other depth-d nodes can generate children
at depth d+1. Its worst-case generated count and frontier
storage are therefore O(b^(d+1)), for b>1. The familiar
O(b^d) estimate applies to a version that tests for a goal
on generation and stops before expanding the goal layer.
Both conventions return a shallowest goal in ordinary BFS.
For explicit finite graphs the standard bounds remain
O(|V|+|E|) time and O(|V|) additional memory.

The practical difficulty is the frontier. DFS retains
alternatives along one path; BFS can retain nearly an entire
layer. A shallowest-route guarantee can become unusable if
the queue exhausts memory first.

## Depth-limited search

Depth-limited DFS refuses to expand a path beyond a specified
limit L. Test for a goal before applying the expansion cutoff,
so goals exactly at depth L remain eligible.

A useful result type distinguishes three outcomes:

- A solution was found.
- Complete failure: every eligible continuation was exhausted.
- Cutoff: some potentially useful continuation was excluded
  by the depth limit.

Cutoff does not establish that no solution exists. It says
that this limit did not settle the question. For example,
a search with L=2 cuts off the A→C→G route before G,
although another route may still find G through B.

For finite branching, the bounded traversal is finite.
It finds a goal at depth at most L if one exists and all
soundly eligible paths through that depth are considered.
For b>1 its tree work is O(b^L), with O(bL) retained records
in a version that stores pending siblings.

A global Boolean visited set is dangerous in a depth-limited
search. Imagine reaching X first at depth L, where no further
expansion is allowed. A later arrival at depth one may have
enough remaining depth to reach a goal through X. Discarding
that arrival because X was already seen loses the solution.
Use path-local cycle checking, or a depth-aware rule that
retains and acts on a better remaining-depth budget.

This is another example of dominance. An arrival is redundant
only when retained information covers its useful futures.
State equality alone does not establish that a shallower
arrival under a depth limit is redundant.

## Iterative deepening

Iterative deepening depth-first search, or IDDFS, runs
depth-limited DFS with limits 0, 1, 2, and so on.

```text
for limit := 0, 1, 2, ...:
    result := depth_limited_search(initial, limit)
    if result is a solution: return result
    if result is complete failure: return failure
```

Do not carry an ordinary visited set from one iteration to
the next. The larger limit makes previously excluded
continuations eligible. Caches require a separate proof
that their depth and path information supports safe reuse.

Every bounded iteration finishes with finite branching.
If a goal exists at finite depth d, the depth-d iteration
finds a goal after all shallower limits have failed.
Consequently IDDFS is complete for such goals and returns
a shallowest one. As with BFS, optimal path cost follows
only when every action has the same positive cost.

What does repeating the upper levels cost? In a regular
tree searched through depth d, the root is visited d+1
times, each depth-one node d times, and each depth-i node
d−i+1 times. The total is

**(d+1) + d·b + (d−1)·b² + … + b^d.**

For fixed b>1 this is O(b^d). Compared with one complete
traversal of the same layers, the ratio approaches b/(b−1).
For b=2 the limiting ratio is two; for b=10 it is about
1.11. This is a regular-tree calculation, not a promise
about every instance or every stopping point.

A chain behaves differently. With b=1, repeated limits
perform 1+2+…+(d+1) visits, giving quadratic work rather
than a constant-factor overhead over a single traversal.
The usual explanation that the deepest level dominates
depends on branching growth.

IDDFS uses O(bd) retained search records in the pending-sibling
implementation, plus state and path storage. Incremental
successor generation may use less. A global duplicate table
can again dominate this bound. IDDFS is particularly useful
when solution depth is unknown, costs are uniform, and a BFS
frontier would be too large.

If there is no solution in an infinite space, iterations can
continue forever. If a finite graph uses path-local cycle
checking, only finitely many simple paths exist; a sufficiently
large limit can exhaust them and return complete failure.
The cycle policy determines whether that failure certificate
will eventually be available.

## Branch-and-bound

Branch-and-bound adds optimization to systematic exploration.
Maintain an **incumbent**, a complete feasible solution of
cost U. Since the true optimum C* cannot exceed a known
feasible cost, C*≤U.

For a partial path n, let L(n) lower-bound the cost of every
complete solution extending it. If L(n)≥U, that branch cannot
strictly improve the incumbent. It can be pruned when finding
one optimal answer is enough. To enumerate all optimal ties,
equality requires different treatment.

For nonnegative additive edge costs, accumulated path cost
g(n) is already a lower bound. An admissible remaining-cost
estimate h(n) strengthens it to L(n)=g(n)+h(n).
An estimate that sometimes overstates remaining cost can
discard an optimal branch; optimism is a correctness condition.

```text
incumbent := none
U := infinity

explore(path, g):
    state := last state on path
    if goal(state):
        if g < U:
            retain a copy of path as incumbent
            U := g
        return
    if lower_bound(path, g) >= U: return
    for each eligible successor child:
        extend path, explore it, and restore path
```

The bound applies to this path's possible completions.
A general CSP optimization model may use a bound on the
partial assignment's eventual objective instead of a path
cost. In either setting, the bound must match the objective
and retained information.

Suppose the first complete route costs 12. Install U=12.
Another partial route has accumulated cost 5 and a justified
total lower bound of 9. It remains eligible: it might finish
at cost 10. A branch with total lower bound 12 can be pruned.
When the cost-10 route is found, update U=10 and prune future
branches with bounds at least 10.

Calling a candidate promising supplies no upper bound.
Only a complete feasible answer supplies U. Likewise,
inventing a bound of 13 for the branch that actually finishes
at 10 would make the pruning unsound.

The finite-tree correctness argument is direct. Each pruned
branch cannot improve the current feasible incumbent. Since
later incumbents only improve, that discarded branch cannot
hide a solution better than the final incumbent either.
Every unpruned branch is eventually explored. At exhaustion,
no cheaper solution remains. If there is no solution,
finite exhaustive traversal establishes failure.

Depth-first branch-and-bound can use little search memory
and often obtains an incumbent early. Best-bound order
instead selects the smallest L from a frontier, retaining
more alternatives. Ordering affects effort and early answers;
the pruning argument depends on valid bounds and sufficient
coverage, not on one mandatory ordering.

Infinite spaces need care. Before any incumbent is found,
ordinary DFS can follow an infinite branch and miss a goal.
After a finite incumbent exists, finite branching and a fixed
positive lower edge-cost bound ε imply that any improving
path has depth below U/ε. With nonnegative h, all paths whose
bounds remain below U lie inside that finite-depth region.
Exhaustive bounded exploration can then establish optimality.

Zero-cost paths in an infinite space break that argument:
arbitrarily long paths can remain under the same bound.
Negative edges also invalidate g as a lower bound and can
create cycles with no finite optimum. A different cost model
requires a different proof.

## Choosing an exploration policy

| Need | Starting method | Main qualification |
| --- | --- | --- |
| Any reachable goal, little retained work | DFS | Bound or control infinite branches and cycles |
| Fewest transitions | BFS | A complete layer can consume much memory |
| Known depth budget | Depth-limited DFS | Cutoff is not failure |
| Unknown depth, uniform costs, limited memory | IDDFS | Regeneration costs depend on branching |
| Minimum objective with feasible candidates | Branch-and-bound | Bounds must be sound and coverage sufficient |

These choices express resource and guarantee tradeoffs.
A reached set changes memory use. A depth limit changes
what a repeated arrival can still accomplish. An incumbent
changes which branches can improve the answer. Treat each
detail as part of the algorithm.

The next chapter orders alternatives by path cost and
heuristic estimates. It retains the same obligation:
explain why a discarded arrival or pruned branch cannot
change the required answer.

## Further reading

- Korf, [“Depth-First Iterative-Deepening: An Optimal
  Admissible Tree Search”](https://doi.org/10.1016/0004-3702(85)90084-0)
  (1985). Develops iterative deepening and its search-cost
  analysis; the cost-bounded form returns in Week 5.
- Korf, [“A Complete Anytime Algorithm for Number
  Partitioning”](https://web.cecs.pdx.edu/bart/cs510cs/papers/korf-ckk.pdf)
  (1998). Connects strong early heuristic answers with
  complete exploration and an eventual optimality proof.
