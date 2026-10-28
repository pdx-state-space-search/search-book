# Final review: Weeks 6–10 and notation

Reviewed 2026-10-22. Read-only chapter review; no chapter
edits, regeneration, commits, or pushes. Read/write access
was demonstrated at the start by listing all six source files
and creating this note. No `prev/` content was accessed.

## Scope and outcome

Read these files completely with line numbers:

- `book/src/06-local.md` (317 lines).
- `book/src/07-stochastic.md` (313 lines).
- `book/src/08-engineering.md` (361 lines).
- `book/src/09-adversarial.md` (338 lines).
- `book/src/10-frontiers.md` (330 lines).
- `book/src/notation.md` (95 lines).

Also read the source of the three directly relevant SVGs:
`local-landscape.svg`, `alpha-beta.svg`, and `schedule.svg`.
Their labels, topology, numerical values, and accessible
text agree with the chapter traces. This was a source check,
not a rendered layout review.

**Must-fix technical or editorial errors: none found.**
The following are optional teaching improvements, not claims
that the current text or stated guarantees are wrong.

## Optional teaching improvements

1. **Make bidirectional initialization explicit.**
   `10-frontiers.md:140–163` gives a useful four-step
   implementation discipline and an explicit empty-queue
   rule, but does not give initial labels or an initial
   incumbent. A short sentence could set forward(s)=0,
   backward(t)=0, all other labels and mu to infinity, and
   handle s=t as a zero-cost solution before expansion.
   This makes the prose closer to executable pseudocode and
   prevents an implementer from overlooking the shared
   initial vertex. The present general joining rule can
   already cover it; this is not a counterexample to that
   rule.

2. **Say that expectations require cardinal utility.**
   `09-adversarial.md:302–311` correctly says that the utility
   scale determines the meaning of an expectation. An
   additional sentence could explain that arbitrary monotone
   rescaling preserves deterministic minimax choices but need
   not preserve choices involving chance. This is a useful
   conceptual bridge from deterministic minimax to
   expectiminimax. No extra topic or formal derivation is
   necessary.

3. **Name the sampling estimate in MCTS explicitly.**
   `10-frontiers.md:189–223` correctly defines Q as a sampled
   MAX reward and carefully avoids claiming it is a minimax
   certificate. A sentence before the UCT formula could say
   that Q summarizes returns under the changing selection
   and rollout policies, rather than samples from a fixed
   optimal opponent. This would reinforce why it differs
   from Week 9's exact backed-up V. The existing caveats at
   lines 218–237 already imply this distinction.

4. **Clarify solvability in the weighted-A* guarantee.**
   `10-frontiers.md:28–32` says the finite-graph algorithm
   returns a bounded-cost solution. It is naturally read
   conditional on a reachable goal, as the proof immediately
   assumes an optimal route. Adding “when a goal is
   reachable” would make that premise explicit and parallel
   the infinite-graph sentence's finite-cost-goal premise.
   Unreachable finite instances terminate with failure under
   the stated duplicate discipline; they cannot return a
   solution. This is a small statement-of-assumptions polish,
   not a problem with the quality-bound proof.

## Technical checks by chapter

### Week 6

- Lines 19–47 correctly distinguish complete assignments,
  feasibility, penalty guidance, and valid returned answers.
- Lines 79–105: the coloring trace has exactly four initial
  conflicts; recoloring C removes three; recoloring A green
  removes the remaining AB conflict without creating AC.
- Lines 116–144: all five transfer outcomes are correct.
  The starting assignment is a non-strict local minimum;
  swapping 8 and 6 attains equal sums of 15. The explicitly
  given two-transfer path has objective sequence 4,12,0.
- Lines 187–226: the coloring delta uses edge conflicts and
  the partition delta retains the essential sign. Both
  bookkeeping explanations match their formulas.
- Lines 228–234 correctly restrict the short 2-opt delta to
  symmetric tours and include reversal costs otherwise.
- Lines 268–296 correctly distinguish sampled neighborhoods
  from an exhaustive local-optimality certificate.

### Week 7

- Lines 22–49: the acceptance formula, tie behavior,
  symmetric-proposal qualification, and probability table
  are consistent. Numerical calibration gives T0=17.93.
- Lines 76–96 avoid extending asymptotic cooling results to
  an arbitrary practical geometric schedule or deadline.
- Lines 100–145 state the restart independence/distribution
  assumptions. Both t/p and ((1-p)/p)F+S are correct under
  their respective models. Five trials with p=.2 succeed
  with probability .67232, rather than certainty.
- Lines 162–167 correctly demonstrate ordinary crossover's
  failure to preserve permutation validity.
- Lines 201–213 correctly restrict nonworsening exact repair
  to a neighborhood containing the old feasible candidate.
- Lines 228–290 handle failed/censored runs, seed versus
  instance replication, tuning, and cost-unit fairness
  without overstating empirical guarantees.

### Week 8

- Lines 39–64 correctly separate symmetry preservation,
  reconstructibility, exact equality, fingerprints, and
  stable hash-table keys.
- Lines 81–99 clearly distinguish depth-first trailing from
  storage/reconstruction obligations in best-first search.
- Lines 142–162: the byte arithmetic is correct; the modeled
  total is 35,200,000 bytes or 33.6 MiB. Assumptions and
  excluded allocator costs are explicit.
- Lines 209–239 acknowledge in-flight expansions/messages,
  ownership, and distributed optimality/termination. No
  false “first goal wins” or empty-local-queues claim.
- Lines 243–292: the courier has real optimum four and
  delete-relaxed optimum three. Positive preconditions/goals
  justify the relaxation. A found relaxed plan is correctly
  identified as an upper bound on the relaxed optimum,
  rather than automatically admissible for the real one.
- Lines 296–337: total task work is 11, the chain bound is
  seven, and the illustrated feasible schedule reaches seven.
  The proof does not incorrectly add overlapping bounds.

### Week 9

- Lines 8–43 explicitly fix the game class, utility
  perspective, finite-tree premise, history dependence, and
  transposition-state requirements.
- Lines 65–140: minimax and alpha-beta agree on North=3;
  South's first reply proves only South<=2. The SVG labels
  this as a bound, not an exact interior value.
- Lines 87–91 distinguish active traversal records from
  materialized siblings and table/state storage.
- Lines 128–158 correctly qualify equality pruning and
  separate ordering hints from pruning arguments.
- Lines 169–209 distinguish truncated-tree values, static
  evaluation, terminal range, and full-game guarantees.
- Lines 221–243 correctly retain the completed iteration
  under interruption and avoid monotonic-quality claims.
- Lines 247–298 correctly distinguish exact/lower/upper
  table entries, matching-horizon semantics, and deliberate
  practical reuse of deeper results. Original-window
  fail-low/fail-high classification is correctly stated.
- Lines 302–322 correctly distinguish random outcomes from
  adversarial choices and avoid transferring deterministic
  alpha-beta pruning unchanged to partial expectations.

### Week 10

- Lines 23–50 give sufficient weighted-A* implementation
  assumptions: actual g, nonnegative admissible h, goal-zero
  h, strict improvements, stale-entry handling, reopening,
  and minimum-removal goal testing. The frontier-prefix
  w-factor inequality is correct. The warning about wh
  losing consistency is correct and conservatively worded.
- Lines 71–109 correctly require unresolved-work coverage,
  account for reopening/pending generation, include the
  incumbent in L=min(U,min(g+h)), and separate weighted
  priority from an admissible certificate. Both gap examples
  are correct; empty-frontier semantics are explicit.
- Lines 119–170 correctly reverse directed edges with their
  original costs, reject first-meeting termination, update
  joined-route incumbents, and condition m_f+m_b>=mu on the
  joining discipline. The 101-versus-100 example works.
- Lines 189–216: fixed-MAX means, MAX's Q+B, MIN's -Q+B,
  and same-sign reward backup are mutually consistent.
  Numerical bonuses round to .416 and .833.
- Lines 247–287 correctly make MAPF collisions, waiting,
  arrival, and objective conventions explicit. CBS is an
  illustration rather than an unsupported optimality claim.
  The LaCAM and LaCAM* descriptions match primary sources.

### Notation and transitions

- `notation.md:33–49` correctly distinguishes strictly
  positive edge costs from a uniform positive lower bound,
  and admissibility from consistency/reopening requirements.
- `notation.md:64–76` matches the later exact-state,
  history-sensitive, and stale-entry discussions.
- `notation.md:80–95` consistently supports minimization,
  fixed-player game utility, seed/instance distinctions,
  censoring, and exact mathematical sentinels.
- Week 6's ending leads directly into Week 7's randomness
  and repeated-run evaluation. Week 7's end supplies the
  evaluation discipline referenced by Week 8.
- Week 8's ending accurately previews adversarial choices
  and sampling; Week 9's ending establishes the fixed-MAX
  convention explicitly reused by Week 10. No transition
  promises an omitted prerequisite or contradicts the next
  chapter.
- There are no executable pseudocode blocks in these six
  files. Reviewed formula/recurrence and numbered algorithm
  descriptions in their place; no code-regeneration needed.

## Verification and source checks

A small, temporary Python invocation independently checked
partition-transfer arithmetic, annealing calibration, restart
probability, memory totals, and UCT bonuses. All assertions
passed. It did not add a project test or source artifact.

Primary publication pages checked on 2026-10-22:

- [AAAI LaCAM paper](https://ojs.aaai.org/index.php/AAAI/article/view/26377):
  the abstract calls LaCAM complete and describes its
  two-level constraints/configuration search; confirms 2023.
- [IJCAI LaCAM* paper](https://www.ijcai.org/proceedings/2023/28):
  the abstract explicitly makes eventual optimality
  conditional on accumulated transition costs; confirms 2023.
- [HDA* paper and journal metadata](https://arxiv.org/abs/1201.3204):
  confirms authors, hash-distributed A*, and Artificial
  Intelligence 195 (2013), pages 222–248. The chapter's
  “journal version, 2013” correctly distinguishes it from
  the arXiv submission/revision dates in 2012.

This was a correctness/editorial review, not a full link
checker or a comprehensive audit of every further-reading
paper's contents.
