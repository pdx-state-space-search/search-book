# Week 10: Beyond the Basics

The preceding methods provide a vocabulary for new search
designs: priorities, lower bounds, incumbents, duplicate
dominance, constraints, adversarial values, and measured
resource costs. This chapter uses that vocabulary to study
bounded suboptimal search, anytime certificates, bidirectional
search, Monte Carlo tree search, and multi-agent pathfinding.

These are extensions with different purposes. Some trade
solution quality for a different exploration order.
Others use two search directions, sampled outcomes, or
structured successor generation. Understanding which
information justifies a guarantee remains more useful than
memorizing another algorithm name.

## Weighted A*

A* selects minimum g+h. **Weighted A*** instead selects

**g+w·h, where w≥1.**

Keep g as actual path cost and h as a nonnegative admissible
remaining-cost estimate, zero at goals. Use strict best-g
improvements, skip stale queue entries, and reopen improved
states. Accept a goal only on a nonstale minimum removal.

For finite graphs with nonnegative costs, this version
returns a solution costing at most w times the optimum
when a goal is reachable; otherwise it terminates with failure.
For potentially infinite graphs, finite branching and costs
bounded below by a positive ε provide a useful sufficient
condition for finite progress to a finite-cost goal.

Let C* be optimal cost. Until an optimal route is completed,
correct duplicate handling preserves a frontier prefix n
of that route with no worse than its optimal prefix cost.
Admissibility gives g(n)+h(n)≤C*. Since g(n)≥0 and w≥1,

**g(n)+w·h(n) ≤ w·(g(n)+h(n)) ≤ w·C*.**

When a goal of cost C is selected, its weighted key is C.
It cannot exceed that eligible prefix's key.
Therefore C≤w·C*.

The proof depends on retaining useful improved arrivals.
A permanent closed set is not automatically justified by
the consistency of the original h: multiplying h by w
can destroy consistency for the original edge costs.
Use the stated reopening implementation unless another
argument establishes the needed bound.

Consider two frontier entries with (g,h) values (2,8) and
(8,3). Ordinary A* assigns 10 and 11, preferring the first.
At w=2, the keys are 18 and 14, preferring the second.
Weight changes ordering; it does not change the actual
cost of either path.

This may find an acceptable goal sooner, but faster runtime
is not guaranteed on every instance. A larger weight also
weakens the worst-case solution-quality bound.
Report the weight, returned cost, and measured effort.
An inadmissible h does not inherit this w-factor proof.

## Anytime search and certified gaps

An **anytime optimizer** retains a feasible incumbent of
cost U while continuing to search. For minimization, U
is an upper bound: C*≤U. A lower bound explains how much
improvement could remain.

Suppose the search preserves all unresolved possibilities
through a correctly maintained frontier F. Every entry
has an admissible completion bound g+h. Account for improved
states awaiting reopening, and evaluate certificates between
completed expansion steps so pending child generation is
not silently omitted.

A valid global bound is

**L=min(U, min over eligible frontier entries of g+h).**

Take the minimum over an empty frontier as infinity.
Including U is essential: after finding an optimal
incumbent, all remaining frontier estimates can exceed U.
Their minimum alone would not lower-bound C*.

The certificate is L≤C*≤U. If U=15 and L=12, the optimum
lies between 12 and 15. The incumbent is at most 3 above
optimal, and, since L>0, at most 15/12=1.25 times optimal.
If the frontier minimum later rises to 18, the certificate
uses min(15,18)=15 and proves the incumbent optimal.

If L=0, U/L does not provide a useful finite ratio.
The additive gap U−L still makes sense. With no incumbent,
there is no feasible upper-bound answer to return.

Weighted keys g+w·h are not admissible lower bounds when
w>1. Choose work by that key if desired, but compute a
certificate from g+h or another justified bound.
A weighted queue's front need not minimize unweighted g+h;
maintaining both minima may require another queue or a scan.

An incumbent permits pruning a branch whose valid lower
bound is at least U when only one optimal answer is needed.
At frontier exhaustion, a retained incumbent is optimal
if all discarded branches were soundly handled.
If the search is restarted, certificates must be derived
from the new search's actual coverage, not an old queue
that has been discarded.

An early aggressive search can supply U to a separate
proof-oriented search. Alternatively, one algorithm can
improve the incumbent and bound together.
The interface is a feasible answer and a justified gap,
not merely a stream of increasingly plausible candidates.

## Bidirectional shortest-path search

For a known start s and goal t, search forward from s and
backward from t. In a directed graph, backward expansion
uses reversed edges with the original edge costs.
Each direction can use Dijkstra's nonnegative-cost rule.

Initialize the forward label at s and the backward label
at t to zero; other labels and the joined-route bound μ
start at infinity. If s=t, return the zero-cost path.

A joined route supplies an upper bound μ. A shared
discovered vertex v gives an actual route costing
g_forward(v)+g_backward(v). Joining across an original edge
u→v can similarly combine a forward prefix, that edge,
and a backward suffix.

The first discovered meeting need not be optimal.
Consider s→a costing 1 and a→t costing 100, versus
s→b costing 50 and b→t costing 50.
After forward expansion of s, both prefixes are known.
If backward expansion of t considers predecessor a first,
the first joined candidate costs 101.
Considering b establishes a better candidate of 100.
Stopping at the first meeting even interrupts a necessary
comparison within this tiny example.

A standard bidirectional Dijkstra discipline is:

1. Maintain correct distance labels and queues in each
   direction, removing stale minima.
2. Expand a minimum-distance entry in the selected direction
   and perform the usual nonnegative-cost relaxations.
3. Update μ whenever discovered information joins the two
   directions into an actual complete route, including
   relevant crossing edges.
4. Stop when the valid queue minima satisfy m_f+m_b≥μ.

The stopping proof needs the joining discipline, not just
the formula. If a potentially cheaper path already crosses
the settled regions, its relevant join must have been
considered in μ. Otherwise it has an unresolved gap whose
forward prefix and backward suffix cost at least m_f and
m_b. Such a route cannot improve μ once their sum reaches μ.

An empty queue also needs explicit handling.
If one direction has exhausted its reachable region and
no join exists, there is no s-to-t path. If a joined route
exists, the algorithm's exhaustion and join invariant
settle its cost without pretending infinity is an ordinary
queue entry.

Two directions can reduce work greatly in roughly symmetric
spaces, but reverse successor generation may be hard.
The goal might describe many acceptable states rather than
one known endpoint. Two frontiers also consume memory,
and heuristic bidirectional search needs more careful
bounds than substituting two A* queues into this rule.

## Monte Carlo tree search

Minimax evaluates an adversarial tree using terminal values
or a horizon evaluator. **Monte Carlo tree search**, MCTS,
instead allocates repeated samples among actions.
A typical iteration has four stages:

1. Select a path through currently stored tree nodes.
2. Expand an untried action when appropriate.
3. Estimate its continuation through a rollout or value model.
4. Back up the result and update visit counts.

A rollout can play legal moves to a terminal state using a
simple policy. Its result might be +1 for a MAX win, 0 for
a draw, and −1 for a loss. Keep the fixed MAX perspective
from [Week 9](09-adversarial.md).

Let Q_i be the mean sampled MAX reward for child i, N_i its
visit count, and N the parent's count. A common exploration
bonus has the form

**B_i=c·sqrt(ln(N)/N_i), with c>0.**

Try unvisited actions before using this expression.
The division is undefined at N_i=0.
The parameter c has meaning relative to reward scale.

For a MAX node, select a child maximizing Q_i+B_i.
For a MIN node, select one maximizing −Q_i+B_i.
Equivalently, MIN minimizes Q_i−B_i.
The exploration bonus must encourage poorly sampled actions
at either player's node. Simply minimizing Q_i+B_i at MIN
would instead penalize a large uncertainty bonus.

Under this convention, backup adds the same MAX-perspective
reward to every visited node's accumulated reward and
increments each visit count. Do not also negate the reward
on alternate levels. Other perspective conventions work,
but their selection and backup rules must match.

For example, let N=16 and c=0.5. A child with N_i=4 has
bonus about 0.416; one with N_i=1 has bonus about 0.833.
At a MAX node, means 0.5 and 0.25 give selection scores
about 0.916 and 1.083. The less-tested action receives
another sample despite its lower observed mean.

This exploration rule is often called UCT.
Its confidence-inspired expression does not turn every
finite search into a calibrated statistical guarantee.
Tree policies change as search learns, descendants can
be sampled unevenly, and rollout outcomes can be biased
relative to optimal play.

At the final decision, the exploration bonus is generally
not the value to maximize. A common choice is the most
visited root action; another is a suitably supported mean.
Specify the recommendation rule separately from the rule
used to allocate samples.

MCTS can miss rare decisive replies under a small budget.
Random rollouts may almost never execute an important tactic.
A learned value model can replace or shorten rollouts,
but its errors become part of the search behavior.
Report budget, policy, perspective, reward scale, and
empirical reliability rather than treating a sampled mean
as a minimax certificate.

## Many agents sharing one graph

**Multi-agent pathfinding**, MAPF, seeks compatible paths for
several agents. Individually shortest routes can collide
at a shared vertex or a narrow passage.
A joint state records one location per agent, making the
configuration space grow rapidly with team size.

A common discrete-time model allows each agent to move
to a neighbor or wait. Collision rules are part of the
instance definition. Two agents may be forbidden from
occupying one vertex simultaneously and from swapping
the endpoints of an edge in one step. Arrival behavior
also matters: does an agent remain at its goal?

The objective must be specified too.
**Makespan** measures when the last agent finishes.
**Sum of costs** adds agents' path costs under the stated
waiting and arrival convention. A plan that improves one
objective can worsen the other.

Conflict-Based Search illustrates a structured alternative
to blindly enumerating every joint action. It proposes
individual paths, finds a conflict, and branches on
constraints excluding one participant or the other from
that conflict. Individual replanning supplies paths
respecting the accumulated constraints.
The conflict tree can still be large; decomposition does
not remove combinatorial difficulty.

Keisuke Okumura's LaCAM work offers a more recent connection
between configuration search and constraint-driven successor
generation. Its 2023 AAAI paper guarantees finding a feasible
plan when one exists under its stated assumptions, using lazy
constraint addition to organize the generation
of joint configurations. The useful design idea is to avoid
materializing all joint moves eagerly.

The 2023 IJCAI follow-up, LaCAM*, develops an anytime
extension with eventual optimality under its stated
accumulated-transition-cost model. Eventual optimality
does not supply a deadline by which the optimum must appear.
The distinction between an early feasible plan and a
completed optimality argument remains essential.

These papers are examples of current research directions,
not a claim that one planner wins on every MAPF instance.
Their model, objective, solution-finding conditions, benchmark
distribution, and resource budget determine how to interpret
reported results.

## Guidance and proof in new methods

Learned models can suggest promising successors, conflicts,
or moves. If guidance only changes ordering inside an
otherwise complete search, completeness can survive when
every state in the stated space is eventually examined.
Permanent learned pruning or replacing an admissible bound
with an unchecked prediction needs a new argument.

The same questions apply without machine learning.
Does a new data structure preserve duplicate identity?
Does a parallel termination rule account for in-flight work?
Does a faster priority supply a valid bound, or only a
preference? Does an exact inner solver make the outer
method complete, or only solve one neighborhood?

The methods in this chapter can be combined, but their
guarantees do not combine automatically.
A weighted search can supply an incumbent to a certifying
search. An anytime MAPF method can use ordering guidance.
A game search can use sampled evaluations.
State the model, retained information, and stopping rule
before inheriting any promise from a familiar name.

## Further reading

- Hansen and Zhou,
  [“Anytime Heuristic Search”](https://doi.org/10.1613/jair.2096)
  (2007). Develops heuristic search that improves answers
  while maintaining information about solution quality.
- Kocsis and Szepesvári,
  [“Bandit Based Monte-Carlo Planning”](https://doi.org/10.1007/11871842_29)
  (2006). Introduces UCT and its combination of sampling
  with exploration-guided tree search.
- Okumura, [“LaCAM: Search-Based Algorithm for Quick
  Multi-Agent Pathfinding”](https://ojs.aaai.org/index.php/AAAI/article/view/26377)
  (2023). A concrete example of constraints organizing
  successor generation in a large joint space.
- Okumura, [“Improving LaCAM for Scalable Eventually
  Optimal Multi-Agent Pathfinding”](https://www.ijcai.org/proceedings/2023/28)
  (2023). Connects early feasibility, continued search,
  and eventual optimality in the same application family.
