# Week 3: Complete and Systematic Search

A complete search eventually examines every state; a systematic
search examines each state at most once. These are separate
properties. Here the space consists of states reachable from
the initial state, and examination means processing a state
after duplicate filtering, as defined in [Week 1](01-models.md).

When comparing coverage, we consider traversal continued after
finding an answer, including exploration of a goal state's
successors unless goals are terminal in the model. The solver
listings instead stop when they have the requested answer.
Such an early stop need not complete the traversal. Likewise,
sound pruning can prove a result while leaving states unexamined.

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
one successor at a time. Begin with the initial state and a
path containing only that state. The path is mutable and
contains no repeated states. The problem supplies the goal
test and legal successors in the chosen order. A successful
result is a copy of the path; each call restores the supplied
path before returning.

<figure class="algorithm" id="dfs-pseudocode"
        aria-labelledby="dfs-algorithm">
<figcaption id="dfs-algorithm">
<strong>SEARCH</strong> from <var>state</var>, reached by
<var>path</var>; returning a solution path or <em>failure</em>.
</figcaption>
<div class="algorithm-body" tabindex="0"
     role="region" aria-label="Depth-first search steps">
<ol class="algorithm-steps">
<li><span class="algorithm-statement"><strong>if</strong> <span class="algorithm-procedure">Goal</span>(<var>state</var>) <strong>then</strong></span></li>
<li><span class="algorithm-statement" style="--indent: 1"><strong>return</strong> a copy of <var>path</var></span></li>
<li><span class="algorithm-statement"><strong>for each</strong> legal successor <var>child</var> in the chosen order <strong>do</strong></span></li>
<li><span class="algorithm-statement" style="--indent: 1"><strong>if</strong> <var>child</var> ∉ <var>path</var> <strong>then</strong></span></li>
<li><span class="algorithm-statement" style="--indent: 2">Append <var>child</var> to <var>path</var></span></li>
<li><span class="algorithm-statement" style="--indent: 2"><var>result</var> ← <span class="algorithm-procedure">Search</span>(<var>child</var>, <var>path</var>)</span></li>
<li><span class="algorithm-statement" style="--indent: 2">Remove the last state from <var>path</var></span></li>
<li><span class="algorithm-statement" style="--indent: 2"><strong>if</strong> <var>result</var> is a solution <strong>then</strong></span></li>
<li><span class="algorithm-statement" style="--indent: 3"><strong>return</strong> <var>result</var></span></li>
<li><span class="algorithm-statement"><strong>return</strong> <em>failure</em></span></li>
</ol>
</div>
</figure>

The path-local test rejects cycles on the active route. Its
soundness here relies on memoryless legal futures and on
seeking one reachable goal: a cycle can be removed from a
successful route without changing what remains possible.
If a rule depends on earlier visits, that history belongs
in the state before applying this reasoning.

On a finite graph, DFS with path-local cycle checking examines
every reachable state if continued to exhaustion. It is then
complete, but need not be systematic: different paths can lead
to another examination of the same state. On a finite search
tree, DFS eventually examines every node unless it stops with
a solution. Finite branching alone is
insufficient. An infinite chain below A can keep DFS busy
forever while a goal waits below B. A cycle can cause the
same failure in naive tree search over a finite graph.

For reachability in a finite graph, a global reached set
can prevent repeated expansion. Marking states when generated
avoids pushing several copies of the same state. This makes
the traversal systematic, and continuing it through the finite
reachable graph makes it complete as well. Any one
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

<figure class="algorithm" id="bfs-pseudocode"
        aria-labelledby="bfs-algorithm">
<figcaption id="bfs-algorithm">
<strong>BREADTH-FIRST SEARCH</strong> from the initial state;
returning a solution path or <em>failure</em>.
</figcaption>
<div class="algorithm-body" tabindex="0"
     role="region" aria-label="Breadth-first search steps">
<ol class="algorithm-steps">
<li><span class="algorithm-statement"><var>frontier</var> ← queue containing the initial state</span></li>
<li><span class="algorithm-statement"><var>reached</var> ← set containing the initial state</span></li>
<li><span class="algorithm-statement"><strong>while</strong> <var>frontier</var> is not empty <strong>do</strong></span></li>
<li><span class="algorithm-statement" style="--indent: 1"><var>state</var> ← remove front of <var>frontier</var></span></li>
<li><span class="algorithm-statement" style="--indent: 1"><strong>if</strong> <span class="algorithm-procedure">Goal</span>(<var>state</var>) <strong>then</strong></span></li>
<li><span class="algorithm-statement" style="--indent: 2"><strong>return</strong> its reconstructed path</span></li>
<li><span class="algorithm-statement" style="--indent: 1"><strong>for each</strong> successor <var>child</var> <strong>do</strong></span></li>
<li><span class="algorithm-statement" style="--indent: 2"><strong>if</strong> <var>child</var> ∉ <var>reached</var> <strong>then</strong></span></li>
<li><span class="algorithm-statement" style="--indent: 3">Add <var>child</var> to <var>reached</var></span></li>
<li><span class="algorithm-statement" style="--indent: 3">Record <var>state</var>'s parent link for <var>child</var></span></li>
<li><span class="algorithm-statement" style="--indent: 3">Append <var>child</var> to <var>frontier</var></span></li>
<li><span class="algorithm-statement"><strong>return</strong> <em>failure</em></span></li>
</ol>
</div>
</figure>

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

With finite branching, continued BFS is complete: every
reachable state lies at a finite depth, and only finitely many
records precede its layer. The reached set makes it systematic.
The goal-stopping version therefore finds a goal at finite
depth if one exists, though that successful run need not examine
all states. On a finite graph it can also exhaust the reachable
space and report failure; an infinite traversal need not finish.

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

<figure class="algorithm" id="iddfs-pseudocode"
        aria-labelledby="iddfs-algorithm">
<figcaption id="iddfs-algorithm">
<strong>ITERATIVE DEEPENING</strong> from <var>initial</var>;
returning a solution path or <em>failure</em>.
</figcaption>
<div class="algorithm-body" tabindex="0"
     role="region" aria-label="Iterative deepening steps">
<ol class="algorithm-steps">
<li><span class="algorithm-statement"><strong>for</strong> <var>limit</var> <strong>in</strong> 0, 1, 2, … <strong>do</strong></span></li>
<li><span class="algorithm-statement" style="--indent: 1"><var>result</var> ← <span class="algorithm-procedure">Depth-limited-search</span>(<var>initial</var>, <var>limit</var>)</span></li>
<li><span class="algorithm-statement" style="--indent: 1"><strong>if</strong> <var>result</var> is a solution <strong>then</strong></span></li>
<li><span class="algorithm-statement" style="--indent: 2"><strong>return</strong> <var>result</var></span></li>
<li><span class="algorithm-statement" style="--indent: 1"><strong>if</strong> <var>result</var> is complete failure <strong>then</strong></span></li>
<li><span class="algorithm-statement" style="--indent: 2"><strong>return</strong> <em>failure</em></span></li>
</ol>
</div>
</figure>

Do not carry an ordinary visited set from one iteration to
the next. The larger limit makes previously excluded
continuations eligible. Caches require a separate proof
that their depth and path information supports safe reuse.

Every bounded iteration finishes with finite branching.
If a goal exists at finite depth d, the depth-d iteration
finds a goal after all shallower limits have failed.
It therefore returns a shallowest goal. Continued traversal
with path-local cycle checking is complete: every reachable
state has a finite-depth path that some iteration examines.
IDDFS is not systematic, since successive iterations examine
the initial state and other states again. As with BFS, optimal
path cost follows only when every action has the same positive
cost.

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

Branch-and-bound adds objective bounds to an exploration policy.
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
discard an optimal branch; the pruning bound must be justified.
A separate estimate may guide successor order without being a
lower bound. Its usefulness for ordering is a different question.

Initially, *incumbent* is *none* and *U* is ∞. The recursive
procedure below shares these values across calls.

<figure class="algorithm" id="branch-and-bound-pseudocode"
        aria-labelledby="branch-and-bound-algorithm">
<figcaption id="branch-and-bound-algorithm">
<strong>EXPLORE</strong> <var>path</var> of cost <var>g</var>;
updating the incumbent and its cost <var>U</var>.
</figcaption>
<div class="algorithm-body" tabindex="0"
     role="region" aria-label="Branch-and-bound steps">
<ol class="algorithm-steps">
<li><span class="algorithm-statement"><var>state</var> ← last state on <var>path</var></span></li>
<li><span class="algorithm-statement"><strong>if</strong> <span class="algorithm-procedure">Goal</span>(<var>state</var>) <strong>then</strong></span></li>
<li><span class="algorithm-statement" style="--indent: 1"><strong>if</strong> <var>g</var> &lt; <var>U</var> <strong>then</strong></span></li>
<li><span class="algorithm-statement" style="--indent: 2">Retain a copy of <var>path</var> as <var>incumbent</var></span></li>
<li><span class="algorithm-statement" style="--indent: 2"><var>U</var> ← <var>g</var></span></li>
<li><span class="algorithm-statement" style="--indent: 1"><strong>return</strong></span></li>
<li><span class="algorithm-statement"><strong>if</strong> <span class="algorithm-procedure">Lower-bound</span>(<var>path</var>, <var>g</var>) ≥ <var>U</var> <strong>then</strong></span></li>
<li><span class="algorithm-statement" style="--indent: 1"><strong>return</strong></span></li>
<li><span class="algorithm-statement"><strong>for each</strong> eligible successor <var>child</var> <strong>do</strong></span></li>
<li><span class="algorithm-statement" style="--indent: 1">Extend <var>path</var> to <var>child</var></span></li>
<li><span class="algorithm-statement" style="--indent: 1">Explore the extended <var>path</var> with its accumulated cost</span></li>
<li><span class="algorithm-statement" style="--indent: 1">Restore <var>path</var></span></li>
</ol>
</div>
</figure>

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
finite exhaustive traversal establishes failure. When pruning
leaves states unexamined, the search is not complete over the
original space. Its optimality argument justifies excluding
those states instead of claiming to have examined them.

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
  continued search and an eventual optimality proof.
