# Week 7: Stochastic Search and Anytime Optimization

Randomness can change which neighbors a search examines,
which starting candidates it tries, and which worsening moves
it accepts. These changes let a method revisit decisions that
strict descent would never reconsider. Their value depends on
the problem and computational budget, so the method and its
experimental evaluation need equally careful descriptions.

A randomized optimizer can be useful without a finite-time
optimality guarantee. To understand its results, separate the
rule that generates a trajectory, the best candidate retained
along that trajectory, and the evidence from repeated runs.

## Simulated annealing

**Simulated annealing** sometimes accepts a move that worsens
an objective. The physical analogy is a material heated to
explore configurations and cooled to favor low energy. In an
optimizer, energy is an objective E to minimize.

Let x be the current candidate and y a proposed neighbor.
Define Δ=E(y)−E(x). Accept improvements and equal-score moves.
For a worsening move, Δ>0, accept with probability

**P(accept)=exp(−Δ/T), where T>0.**

This is the Metropolis acceptance rule. The standard physical
interpretation assumes an appropriate symmetric proposal rule;
we can use the rule as search guidance without claiming that
an arbitrary proposal mechanism has the same equilibrium law.
The proposal policy and acceptance rule together define the
algorithm.

At temperature T=2, a worsening change of Δ=4 is accepted
with probability exp(−2)≈0.1353. At T=4 its probability is
exp(−1)≈0.3679. Raising temperature makes this same worsening
step more likely, though it does not guarantee that the next
proposal will take it.

| Worsening change Δ | T=1 | T=2 | T=4 |
| --- | ---: | ---: | ---: |
| 1 | 0.3679 | 0.6065 | 0.7788 |
| 4 | 0.0183 | 0.1353 | 0.3679 |

Draw a uniform random number in [0,1) and accept when it is
less than the probability. There is no need to wait for a
fixed quota of worsening moves: each proposal receives its
own randomized decision.

The current candidate can become worse. Keep the best feasible
candidate separately if an answer must be available at any
time. Updating that record only on improvement makes its
objective nonincreasing even when the current trajectory
moves uphill.

## Temperature is tied to objective scale

Suppose an objective measured in dollars is converted to
cents. Every Δ is multiplied by 100. Leaving T unchanged
would radically change acceptance probabilities. Multiplying
T by the same factor preserves Δ/T and therefore preserves
the acceptance decision probabilities.

One practical calibration uses a representative worsening
change Δ₀ and a desired initial acceptance probability q,
with 0<q<1. Solving q=exp(−Δ₀/T₀) gives

**T₀=−Δ₀/ln(q).**

For Δ₀=4 and q=0.8, T₀≈17.93. Sampling move deltas can help
choose such a scale. It remains a tuning choice: a sample
near the initial candidate may not describe deltas near a
later local optimum.

A geometric cooling schedule uses Tₖ₊₁=αTₖ, where 0<α<1.
Taking α=0.95 lowers temperature five percent per schedule
step. A schedule is incomplete without specifying how many
moves occur at each temperature, when to stop, and whether
reheating or restarts are allowed.

Slow cooling spends more computation exploring before strong
preference for downhill moves emerges. Fast cooling approaches
greedy descent sooner. Classical asymptotic convergence results
require conditions on the finite state space, connectivity,
proposal mechanism, and sufficiently slow cooling. They do not
justify a claim that a practical geometric schedule finds a
global optimum within a given deadline.

The partitioning barrier from [Week 6](06-local.md) gives a
concrete use for uphill moves. The candidate with sums 17 and
13 has E=4. Transferring weight 8 gives E=12, a worsening
change of 8. At T=4 it is accepted with probability exp(−2).
Transferring weight 6 back then reaches E=0. Annealing gives
the first step a chance; it does not promise that the useful
second proposal will follow.

## Restarts and expected time

A simple restart model makes its assumptions explicit. Let
independent trials start from the same distribution, each
succeeding with probability p>0. Suppose every trial consumes
exactly t time units, including a successful trial.

The number N of trials through the first success has

**P(N=k)=(1−p)^(k−1)p, for k=1,2,…**

The expected trial count is E[N]=1/p, and expected total time
is t/p. With p=0.2 and t=30 seconds, that is five trials and
150 seconds on average. The probability of succeeding within
five trials is only 1−0.8⁵=0.67232. An expected time is not
a deadline by which success is certain.

After m independent trials, success probability is
1−(1−p)^m. This can help interpret repeated failures when p
is known. In experiments p is usually estimated, and the
estimate itself has uncertainty. A success rate measured on
one instance need not describe another instance.

When successful and failed trials have different durations,
let F be expected duration conditional on failure and S be
expected duration conditional on success. Independent,
identically distributed trials then give

**E[time]=((1−p)/p)F+S.**

There are on average (1−p)/p failures before one success.
For p=0.2, F=20, S=30 seconds, expected time is 4×20+30=110
seconds. Replacing this with t/p would ignore the differing
trial durations.

For a cutoff policy, every unsuccessful trial may be stopped
after τ seconds. Those are failures of the capped trial, even
if an uncapped run would eventually succeed. The capped policy
has its own p, F, and S. When analyzing the uncapped runtime
distribution, those same timeouts are right-censored: we know
only that success took longer than τ.

Restarts can avoid wasting a whole budget on a long unlucky
run. Restarting too quickly can also repeatedly throw away
useful progress. Compare restart cutoffs using observed
success probability and duration, rather than assuming that
more restarts are always better. Correlated starts or shared
persistent state also break the independent-trial model.

## Populations and evolutionary search

An evolutionary method maintains a population of candidates.
Selection favors some candidates as parents, mutation changes
individual candidates, and crossover combines parts of
parents. These operations need a representation in which
variation corresponds to meaningful changes in the problem.

For minimization, selection can use objective ranks rather
than converting every score to an arbitrary positive fitness.
The stronger the preference for top-ranked candidates, the
faster poor candidates may disappear. Strong selection can
also eliminate diversity before different useful regions have
been explored.

Representations constrain variation. A tour is a permutation
of cities. Swapping two cities preserves that property.
Ordinary one-point crossover need not: combining the first
half of (A,B,C,D) with the second half of (C,D,A,B) produces
(A,B,A,B), with repeated cities and missing cities. A
permutation-aware operator or an explicit repair is needed.

Crossover is useful when parts of good candidates can be
combined productively. Strong dependencies can make the
combination worse than either parent. Mutation provides new
variation but, at excessive strength, can erase the structure
selection was preserving. Population size, parent selection,
replacement policy, mutation, crossover, repair, and stopping
budget are parts of the algorithm, not minor details hidden
behind the word "evolutionary."

An elitist policy retains the best feasible candidate seen.
This protects output quality while allowing population members
to vary. It does not guarantee that the population explores
all useful regions. Applying local improvement to offspring
can make candidates better while making the population more
similar; the value of diversity still needs attention.

## Hybrids and restricted exact search

**Iterated local search** alternates local improvement,
perturbation, and another local improvement. A perturbation
tries to leave the current basin without discarding all useful
structure. Too small a perturbation can return to the same
local minimum; a large one can behave like a random restart.
An acceptance rule decides which resulting local minimum
becomes the next starting point.

**Large-neighborhood search** can unassign part of a candidate
and repair it while fixing the rest. A constraint solver or
branch-and-bound search may solve this restricted subproblem
exactly. This allows coordinated changes that would require
many poor single-variable moves.

Suppose a schedule is feasible and we free three tasks while
fixing all others. If the old assignments remain permitted,
the restricted neighborhood contains the old schedule.
Solving that restricted minimization problem optimally cannot
return a worse objective. This is a guarantee about that
neighborhood, not about all possible schedules.

The outer policy chooses which tasks to free. It can omit a
region essential to global improvement. Therefore an exact
repair component does not make the whole hybrid complete or
globally optimal. A time-limited repair may also fail to solve
its subproblem to optimality; retaining the original candidate
preserves an available feasible answer.

These methods connect local search to the complete methods
from earlier weeks. A heuristic outer search can identify
promising regions, while a complete inner search reasons
precisely within one region. Describe both levels when stating
what an experiment or correctness argument establishes.

## Evaluating stochastic methods

A single successful seed demonstrates a possible trajectory.
It does not estimate reliability. Compare methods over a
stated set of instances, with multiple runs on each instance
and a stated stopping budget.

For solution quality at a deadline, record the best feasible
objective found by that deadline and whether feasibility was
reached at all. For time to a target, record the target,
reached-target runtimes, and runs that did not reach it before
the cutoff. A timeout is not an observation that the method
would have succeeded exactly at the cutoff.

Consider two hypothetical methods, each run ten times on one
instance with a 60-second cutoff. Method A succeeds twice,
in one second each. Method B succeeds nine times, in five
seconds each. Averaging successful runtimes alone gives A
one second and B five seconds, obscuring the large difference
in success rate. The appropriate choice depends on the task,
but the report must expose both speed and reliability.

Compare algorithms on the same instances. Instance difficulty
can dominate the differences being studied. Report per-instance
or grouped results when the collection is heterogeneous;
a single pooled mean can hide complementary strengths and
failures.

Multiple seeds for one instance are repeated observations
about that instance. They do not create many independent
instances. A claim about a population of problems needs an
instance sample or a justified benchmark collection, not
merely thousands of seeds on one puzzle.

Fair budgets require a meaningful cost unit. One method's
"iteration" may evaluate one move; another's may inspect an
entire neighborhood or call a complete solver. Wall-clock
time compares actual implementations on specified hardware.
Objective-evaluation and expansion counts help explain work,
but may omit queue, copying, communication, or repair costs.
Report both time and useful work counts where practical.

Keep parameter tuning separate from final evaluation when
possible. Selecting a schedule, population size, or restart
cutoff after seeing all benchmark results adapts the method
to those benchmarks. Record the configurations tried and the
selection procedure rather than presenting the best observed
configuration as if it had been fixed in advance.

## A compact experimental record

A useful report gives enough information to reconstruct the
question and the comparison:

- Instances or their generator, and how the collection was
  selected.
- Algorithm variants, parameters, random seeds, and any
  persistent state shared across runs.
- Objective, feasibility definition, target, and stopping
  budget.
- Hardware and software details relevant to runtime.
- Success rates and quality distributions, including failures
  and censored runtimes.

Medians and quantiles can reveal broad variation that a mean
hides. Uncertainty summaries should match the sampled units.
Paired per-instance comparisons can reduce the noise caused
by differing instance difficulty, but pairing seed labels
alone does not ensure equivalent random events in different
algorithms.

Learning why a method succeeds is often more useful than
announcing a universal winner. A strong result can establish
an advantage on the tested instances and budgets while leaving
other problem families unresolved. Stochastic search trades
exhaustive coverage for a useful distribution of outcomes;
evaluation makes that distribution visible.

## Further reading

- Kirkpatrick, Gelatt, and Vecchi,
  [“Optimization by Simulated Annealing”](https://doi.org/10.1126/science.220.4598.671)
  (1983). The classic connection between temperature-guided
  exploration and combinatorial optimization.
- Lourenço, Martin, and Stützle,
  [“Iterated Local Search”](https://doi.org/10.1007/0-306-48056-5_11)
  (2003). A fuller treatment of perturbation, local improvement,
  and acceptance as distinct design choices.
- Johnson, Aragon, McGeoch, and Schevon,
  [“Optimization by Simulated Annealing: An Experimental
  Evaluation; Part I, Graph Partitioning”](https://doi.org/10.1287/opre.37.6.865)
  (1989). An empirical study useful for thinking about what
  algorithm comparisons must specify and measure.
