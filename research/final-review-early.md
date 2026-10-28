# Final review: notation and Weeks 1–5

Reviewed the current files only. No `prev/` material was read.
Read/write access was verified at the start by reading the
assigned file inventory and creating this note. Chapters were
not edited or regenerated.

## Result

No actionable technical or editorial defects found in the
assigned scope. In particular, no incorrect guarantee,
worked-trace error, or pseudocode defect was established.
The checks below record the substantive review rather than
propose optional rewrites.

## Scope

- `book/src/notation.md`
- `book/src/01-models.md`
- `book/src/02-constraints.md`
- `book/src/03-systematic.md`
- `book/src/04-best-first.md`
- `book/src/05-heuristics.md`

Also compared the SVG sources referenced by these chapters:
`states-and-paths.svg`, `arc-consistency.svg`, `reopening.svg`,
and `manhattan.svg`. Their data match the accompanying prose
and alternative text. This was a source-level comparison,
not a rendered-layout review.

## Guarantees and assumptions checked

- `01-models.md:55–127`: state sufficiency, dominance of a
  cheaper arrival, and the distinction between graph states
  and unfolded path nodes are mutually consistent. Cycle
  elimination is conditioned on relevant history being in
  the state.
- `01-models.md:165–177`: geometric-series counts are correct:
  87,381 through depth 8; 22,369,621 through depth 12;
  approximately 1.47 trillion through depth 20 at b=4.
  The illustrative throughput gives approximately 17 days.
- `01-models.md:208–227` and `notation.md:31–49`: completeness
  is separated from failure termination; infinite-graph cost
  arguments require finite branching and a global positive
  edge-cost lower bound, rather than merely positive edges.
- `01-models.md:249–291`: P, NP, NP-complete, NP-hard, and
  input-size qualifications do not overclaim that membership
  in NP implies hardness or that polynomial time is a runtime
  forecast.
- `02-constraints.md:132–145,259–291`: finite-domain
  backtracking and AC-3 termination are properly separated
  from propagation completeness. Domain restoration is an
  explicit correctness obligation.
- `02-constraints.md:224–237`: the excluded reverse-arc rule
  is correctly conditioned on one relation per pair and its
  transpose. Unsupported X values cannot have supported Y.
- `03-systematic.md:137–146`: the O(b^(d+1)) removal-test BFS
  bound matches the supplied algorithm, which can expand
  non-goal depth-d nodes before removing the first goal.
- `03-systematic.md:177–205`: depth-limited duplicate handling
  and iterative-deepening cache cautions preserve useful
  later arrivals with larger remaining depth budgets.
- `03-systematic.md:247–327`: incumbent feasibility, lower
  bound validity, equality pruning for one optimum, finite
  exhaustion, and the extra infinite-space assumptions are
  all stated. The proof does not promise that depth-first
  search first finds an incumbent on an infinite branch.
- `04-best-first.md:49–97`: immutable path-parent records,
  strict-g improvements, stale-entry rejection before goal
  acceptance, and reopening are compatible. Zero-cost cycles
  do not produce equal-cost reinsertions.
- `04-best-first.md:116–158,195–246`: UCS and A* optimality
  arguments retain an optimal-prefix frontier witness.
  Consistency is used for finalization, whereas admissibility
  with reopening is enough for the A* cost proof. Finite and
  infinite termination conditions are separately addressed.
- `05-heuristics.md:64–142`: maximum combination and additive
  cost partitioning have valid lower-bound arguments. The
  additive pattern-database discussion correctly assigns
  zero cost to moves charged to other groups and rejects
  ordinary BFS for mixed zero/one precomputation costs.
- `05-heuristics.md:163–220`: IDA* checks its threshold before
  accepting goals, resets the shared next threshold once per
  iteration, and uses the minimum exceeded f. Its optimality
  and finite-progress arguments cover inconsistent admissible
  estimates without relying on monotonic f along a path.
- `05-heuristics.md:260–326`: RBFS initializes child values
  with pathmax, backs up revised values, and explicitly exits
  on exhausted infinity-valued branches, including when the
  inherited limit is infinity. Claimed storage is O(bD),
  with heuristic tables excluded explicitly.

## Worked traces checked

- `02-constraints.md:73–94`: two-color triangle SAT encoding
  has the correct six clauses and contradictory implications.
- `02-constraints.md:184–200`: forward checking leaves D
  untouched until C is assigned; the table consistently
  distinguishes an assigned variable from a singleton domain.
- `02-constraints.md:239–257`: AC-3 FIFO queue order, duplicate
  suppression, requeued X→Y, removals, and unique fixed-point
  solution all agree.
- `03-systematic.md:31–35,112–116`: DFS returns S→A→C→G;
  graph BFS returns S→B→G with the stated queue evolution.
- `04-best-first.md:101–109`: UCS improves G from 10 to 2
  before accepting it.
- `04-best-first.md:166–174`: greedy's cost-9 choice versus
  cost 5 is correct, including consistency when h(S)=0.
- `04-best-first.md:253–278`: reopening trace returns cost 5;
  a permanently closed A permits the cost-6 failure described.
- `05-heuristics.md:34–62`: Manhattan distance is 2 and the
  two stated tile moves solve the displayed board.
- `05-heuristics.md:190–207`: IDA* thresholds 2 then 3 are
  correct; A's f=6 and B's goal f=3 determine the next bound.
- `05-heuristics.md:298–304`: RBFS competitor limits 7 then
  9 follow correctly from backed-up child values 4,7 → 9,7.

The chapter transitions progress coherently from model
correctness to propagation, systematic exploration, priorities,
then heuristic construction and memory tradeoffs. No primary
source lookup was needed to resolve an uncertain factual claim.
