# Review of Weeks 3–5

Review date: 2026-10-27. Review only; no chapter, check,
figure, or skill source was changed by this reviewer.

## Scope and assessment

I read all of `03-systematic.md`, `04-best-first.md`, and
`05-heuristics.md`, including pseudocode, tables, figures,
transitions, and further readings. I read the authoring
skill, its editorial guide and examples, BRIEF.md,
BOOK-NOTES.md, STATUS.md, SUMMARY.md, notation, and Weeks
1–2 as prerequisites. I inspected the actual check
implementations rather than relying on their names or
previous passing reports.

The core algorithms and numerical traces are technically
careful. I found no definite must-fix technical defect in
their stated optimality/completeness arguments. The main
revision need is teaching: some of the hardest sections
explain a general rule and give hypothetical numbers without
an instance from which the reader can reproduce those
numbers. The checks do not resolve that problem.

Severity labels below are:

- **Must fix technical:** a definite false result, unsound
  algorithm, or erroneous numerical example.
- **Substantive teaching:** a material explanatory or
  citation gap under the agreed introductory-book standard.
- **Optional:** a useful refinement or precision improvement.

There are no findings in the first category. This means no
defect found within the reviewed scope, not a general proof
that every implementation of the descriptions is correct.

At review start, the book had no separate bibliography.
The root editor is adding that infrastructure during this
review. The citation findings below concern remaining
point-of-use citations in Weeks 3–5; adding bibliography
entries alone will not resolve them.

## Week 3: Systematic Search

### W3-1: Define the cutoff/failure mechanics completely

**Substantive teaching; definite specification gap.**
Anchors: `src/03-systematic.md:155`, `:159`, `:195`, `:240`.

The chapter correctly distinguishes cutoff from complete
failure, and IDDFS depends on that distinction to stop on
unsolvable finite graphs. However, it never shows how a
depth-limited invocation combines its children's results or
decides whether a boundary node actually has an eligible
continuation. The IDDFS pseudocode calls an undefined
`depth_limited_search`.

A natural implementation returns cutoff immediately at
depth L, even at a leaf. It still finds finite-depth goals,
but can need an extra iteration on finite trees. To obtain
the stronger wording that cutoff means a continuation was
actually excluded, the boundary case must distinguish a
leaf (or a state whose only successors are path cycles)
from a genuine blocked continuation. Likewise, one child
cutoff plus other child failures must yield cutoff overall;
returning failure after the last child fails is unsound for
the outer stopping rule.

Proposed repair: add concise depth-limited pseudocode using
the already taught DFS skeleton. Test goals first, perform
path-local eligibility checks, collect whether any child
returned cutoff, and return complete failure only when no
eligible continuation was excluded. A two-edge chain with
L=1 and a dead leaf at the same boundary makes the two
outcomes tangible. Retain the warning about Boolean visited
sets, which is correct and important.

### W3-2: Give branch-and-bound an actual bound calculation

**Substantive teaching; opportunity, not a false claim.**
Anchors: `src/03-systematic.md:249`, `:254`, `:266`, `:288`.

The proof of pruning is sound, but the example supplies
12, 5, 9, and 10 as hypothetical values without identifying
a graph or candidate problem that produces them. The reader
cannot independently derive the lower bound of 9, see which
subtree it excludes, or reproduce a whole search. This is
the first algorithm in the book that combines an incumbent
with optimistic completion bounds; it deserves a concrete
worked example rather than bookkeeping alone.

Proposed repair: either return to our number partitioning
instance with a justified partial-assignment bound, or make
a named weighted version of the DFS graph. For example,
S→A=3, A→C=4, C→G=5 gives the first route cost 12;
S→B=5, B→G=5 gives cost 10. Add S→D=12, D→G=1 so the
D branch can be visibly pruned after U=10. At B, h(B)=4
is admissible because its actual remaining cost is 5, so
g+h=9 explains the existing number. Show the incumbent,
partial bound, and pruning in a short trace/tree.

The pseudocode should also say what makes a successor
eligible, and display the updated g in its recursive call.
The surrounding finite-tree argument is correct, but a
reader should not have to import an unstated cycle policy
when applying the procedure to a graph.

### W3-3: Point-of-use citations and reading version

**Substantive teaching; definite citation omission.**
Anchors: `src/03-systematic.md:192`, `:214`, `:249`, `:350`.

IDDFS and its repeated-layer analysis have no citation where
they are introduced. Branch-and-bound also has no supporting
source at its introduction. The further-reading list is
separate from that function. Link those passages to relevant
bibliography entries, and add a suitable primary reference
for branch-and-bound if the bibliography's present sources
do not directly support that general method.

**Optional bibliographic precision:** `:356` labels the
number-partitioning reading 1998, but the linked PDF's title
page says June 27, 1997. The 1998 journal publication is
real and has DOI 10.1016/S0004-3702(98)00086-1. Identify
the linked document as a preprint of that journal article;
do not imply the PDF is the final published version.

### W3-4: Small clarity refinements

**Optional.** Anchors: `src/03-systematic.md:31`, `:107`,
`:211`, `:233`.

- Draw the tiny S/A/B/C/G graph before the DFS/BFS trace.
  All its edges currently appear in one sentence; the
  reader must retain that list while comparing two routes.
- In BFS, change "record state's parent link for child" to
  "record state as child's parent" or equivalent. The
  intended parent direction is clear from the trace, but
  the pseudocode phrase is awkward.
- "Optimal path cost follows only when every action has the
  same positive cost" is a conventional sufficient-condition
  summary phrased as a necessary condition. Uniform zero
  costs also make every returned path optimal; particular
  unequal-cost graphs can happen to align depth and cost.
  Prefer "Equal positive costs give the general minimum-cost
  guarantee". This is wording precision, not evidence that
  the presented IDDFS trace returns a wrong answer.
- Clarify whether O(bd) records already include the active
  path. The subsequent "plus state and path storage" can
  sound like the record bound omits its main stack. Explain
  record count separately from state representation size.

### Week 3 strengths and whole-chapter coverage

Preserve the correct distinctions between state and path,
finite graph and infinite unfolding, generated and expanded
records, and node counts versus explicit-graph complexity.
The goal-test timing qualification for BFS is especially
good: removal-time tests can generate depth d+1 before the
first depth-d goal is removed. The path-local DFS argument,
depth-aware duplicate warning, b=1 IDDFS exception,
incumbent equality rule, and positive-epsilon qualification
for infinite branch-and-bound all withstand review.

I checked every section: opening definitions, DFS, BFS,
depth-limited search, IDDFS, branch-and-bound, the policy
table, transition, and both readings. No numerical error
was found in DFS/BFS orders or the IDDFS layer sums.

## Week 4: Best-First Search

### W4-1: Motivate heuristic estimates before the properties

**Substantive teaching; opportunity, not a technical error.**
Anchors: `src/04-best-first.md:10`, `:24`, `:166`, `:193`.

The opening introduces h*, admissibility, and consistency
in six lines before giving a concrete reason one would
know an optimistic remaining-cost estimate. The first
heuristic example then assigns values to A and B without
explaining how a solver might obtain them. Week 5 teaches
construction properly, but this chapter should let a novice
interpret the estimate before asking them to distinguish
two formal properties of it.

Proposed repair: introduce an explicitly named small route
instance with a simple estimate, such as a lower-cost
relaxed network or geometric distance with a stated cost
model. Explain "remaining," "optimistic," and why g still
matters. Define admissibility next, and move the consistency
inequality to its already substantial later section or
give it a concrete edge check immediately.

This is a sequencing issue; the current formal definitions
and examples are mathematically correct.

### W4-2: Cite algorithm definitions and their variants

**Substantive teaching; definite citation omission.**
Anchors: `src/04-best-first.md:35`, `:49`, `:92`, `:195`,
`:230`, `:282`, `:306`.

UCS/Dijkstra, A*, consistency/reopening, and heuristic
dominance have no point-of-use source links. The general
loop is an explicit modern graph-search variant with lazy
updates, immutable parent entries, strict-g improvement,
and reopenings. Cite sources that support those actual
guarantees rather than allowing the historical A* title
alone to imply coverage of every implementation detail.

The Dechter–Pearl paper is a useful source for the conditions
behind stronger efficiency claims. An author-hosted copy is
available at https://ics.uci.edu/~dechter/publications/r0.pdf
and avoids the ACM access failure encountered in this review.
Adding that access route is optional; the point-of-use
citation requirement remains substantive.

### W4-3: Define expansion finalization and demonstrate stale work

**Optional.** Anchors: `src/04-best-first.md:54`, `:79`,
`:92`, `:238`, `:274`.

The loop and reopening example are good. Add a brief plain
definition of a closed/finalized state at its first use:
the implementation promises not to expand it again. This
helps distinguish it from the already defined reached set.

Neither worked example actually removes and skips a stale
entry, because it stops at an earlier goal. A tiny queue
snapshot with a stale non-goal record would make lazy
updates more concrete, but is not necessary for correctness.
Keep the explicit immutable parent-entry explanation; it
avoids a real source of mismatched path/cost reporting.

### Week 4 strengths and whole-chapter coverage

The common queue loop is coherent for all three priorities.
Strict improvement suppresses zero-cost duplicate cycling;
the finite-graph termination claims are valid with finite
graphs and nonnegative costs. Positive costs alone are
correctly distinguished from a uniform positive lower bound
on infinite graphs. UCS's first-generated-goal counterexample
is correct. The greedy example's h values are admissible
and, with h(S)=0, consistent; it still returns cost 9 instead
of 5. This appropriately disproves any optimality inference
from those properties for greedy search.

The A* prefix argument includes its real obligation:
retain better arrivals and reopen when needed. In the figure
instance h is admissible and inconsistent on B→A (also on
S→A, which need not be listed). The five removed entries
and both path costs are correct. The heuristic-dominance
section avoids an unjustified universal runtime claim.

I checked the whole chapter: priorities/ties, arrival loop,
reconstruction, UCS proof/complexity, greedy example and
termination, A* proof, consistency, reopening figure/trace,
strength/memory discussion, transition, and all readings.

## Week 5: Heuristics and Limited Memory

### W5-1: Work one abstraction through actual states and values

**Substantive teaching; opportunity, not a false claim.**
Anchors: `src/05-heuristics.md:81`, `:99`, `:108`, `:120`,
`:137`.

The cost-partition proof is sound, but the pattern-database
section never shows a concrete projection, abstract move,
table entry, or summed lookup. It also introduces "state
ranking" without an example. A reader can repeat the rule
without yet being able to construct even one entry.

Proposed repair: reuse the illustrated board and retain tile
5 plus the blank in one abstract state, and tile 8 plus the
blank in another. Show the 5-up/8-left solution: component
costs are (1,0) and (0,1), so each lookup is 1 and their
sum is 2. Background-tile swaps must be shown as zero-cost
abstract moves, explaining immediately why FIFO BFS is
insufficient for the resulting 0/1 graph. State ranking can
be one sentence explaining how a position tuple becomes an
array index, or deferred as an engineering detail.

If a stronger-than-Manhattan example is desired, an
independently checked candidate is board
2,1,3 / 4,5,6 / 8,7,blank with the usual goal. Manhattan
is 4; a database for tiles {1,2} plus blank has value 4,
and one for {7,8} plus blank also has value 4 when only
selected-tile moves cost one. Their safe sum is 8. Each
database has 504 abstract configurations. The real optimum
is 22. This is evidence for a proposed example, not a
recommendation to add all these numbers without explaining
their derivation. The simpler existing-board demonstration
may teach the accounting better.

### W5-2: Turn RBFS's hypothetical bounds into a reproducible trace

**Substantive teaching; definite absence of worked instance.**
Anchors: `src/05-heuristics.md:253`, `:260`, `:276`, `:298`,
`:319`.

The RBFS example starts with hypothetical F values 4 and 7,
then stipulates a returned 9. There is no underlying graph
or subtree explaining why 9 is returned, what was forgotten,
or how regeneration inherits that bound. This is the most
subtle algorithm introduced so far, and the present example
does not illuminate its central operation.

Proposed repair: supply a small named tree with edge costs
and h values. Trace a descent, limit violation, backed-up
minimum, branch switch, and one regeneration. Draw retained
siblings separately from discarded descendants, and show
why `max(F(parent),g+h)` preserves a valid lower bound after
the old subtree is regenerated. Specify tie handling for
that trace and call the root with limit infinity.

Also replace "appropriate finite-search conditions" with
an explicit guarantee paragraph: admissible nonnegative h,
zero at goals, finite branching, and costs bounded below
by epsilon>0 suffice to find an optimal finite-cost goal;
a finite graph with path-local cycle exclusion also permits
nonnegative costs. In a finite exhausted simple-path tree
it reports failure. The current qualifications point in the
right direction, but "preserve the possibility of an optimal
route" does not plainly tell the reader what a returned
answer establishes or when termination is promised.

This is not a report of an incorrect RBFS implementation.
The pseudocode's explicit infinity exhaustion test is
correct and worth retaining.

### W5-3: Point-of-use citations and reading guidance

**Substantive teaching; definite citation omission.**
Anchors: `src/05-heuristics.md:17`, `:43`, `:81`, `:101`,
`:152`, `:253`, `:347`.

Relaxation, Manhattan heuristic, cost partitioning, pattern
databases, IDA*, and RBFS need citations where introduced.
The existing three sources can support much of this, but
the mapping from source to claim must be explicit. Verify
whether the cited source covers the particular abstraction
and pathmax RBFS variant before attaching it to a broad
paragraph. The author/publisher abstracts support the
general descriptions of the three papers, not every detail
of this chapter's pseudocode.

The Week 3–5 further-reading annotations are descriptions;
none currently contains a direct instruction conflated
with a source claim. Thus there is no definite violation
like the mixed description/advice in older Week 2 text.
An optional improvement is to add a clearly marked
**Reading suggestion:** for an accessible section or first
pass, especially for Dechter–Pearl and the RBFS paper.
Do not turn the present lack of advice into an alleged
misattribution.

### W5-4: Explain a strict relaxation gap

**Optional.** Anchors: `src/05-heuristics.md:28`, `:50`,
`:54`, `:55`.

The warning that an arbitrary relaxed solution is an upper
bound on the relaxed optimum is excellent. Add a tiny
numeric illustration if students struggle: a relaxed
optimum of 2, a found relaxed route of cost 9, and an
original optimum of 5 show why the found 9 is unsafe as h.
Likewise, the Manhattan board has estimate equal to actual
cost, so it does not exhibit the omitted interactions.
One second board or brief explained detour would make the
optimism tangible, but the current admissibility argument
is already sufficient.

### Week 5 strengths and whole-chapter coverage

The chapter explains tile-puzzle rules before using the
example and correctly excludes the blank from Manhattan.
Its two-move solution and consistency argument are correct.
The maximum-versus-sum distinction and per-action accounting
are sound. Additive tables explicitly charge background
moves zero and warn against ordinary BFS precomputation.
Total-memory accounting correctly includes the databases.

IDA* is especially strong: bound-before-goal testing, copying
the successful path, minimum-exceeded threshold updates,
the optimal-prefix proof, finite-progress assumptions,
finite graph/nonnegative-cost exception, path-local cycle
policy, and actual-depth memory parameter D all agree.
The example uses thresholds 2 then 3 and returns cost 3.
RBFS handles exhausted infinity branches explicitly and
states its O(bD) retained-record assumption carefully.

I checked every section: relaxation, tile example/figure,
combination proof, abstraction/cost assignment/construction,
IDA* pseudocode/trace/proof, retention/memory, RBFS
pseudocode/summary/complexity, final comparison, transition,
and all three readings.

## Independent verification and check coverage

### Checks read

- `checks/check_algorithms.py`: Floyd–Warshall comparison
  for three-vertex UCS/A*/weighted A* with integer
  nonnegative costs and bounded integer admissible h;
  IDA* only when all present edges have positive cost;
  the explicit reopening and first-generated-goal cases.
  This file does not check DFS/BFS/DLS/IDDFS/B&B or PDBs.
- `checks/check_extensions.py`: 4,096 three-vertex directed
  cost graphs for bidirectional search, plus 9,477 RBFS
  graph/heuristic cases with positive costs. It omits
  zero-cost RBFS despite the chapter's finite-graph nuance.
  Its RBFS code matches the chapter's pathmax/exhaustion
  logic; its tie handling uses sorted record tuples.
- `checks/check_examples.py`: many checks for other weeks,
  but no independent Week 3 trace/B&B/IDDFS check and no
  Manhattan/PDB example check. Passing its complete output
  therefore does not establish those claims.
- `checks/check_browser.cjs`: detects page overflow, broken
  images, missing titles, and navigation overlap at desktop,
  narrow, and 200% text sizes; saves screenshots of figures,
  code blocks, and tables. It does not judge label legibility
  or whether a diagram explains the intended concept.

### Additional finite calculations performed

Executed ad hoc Python without adding a check file:

- Independently enumerated the reachable 8-puzzle component
  by BFS from the goal: 181,440 states. Manhattan never
  exceeded true distance. Checked consistency across all
  483,840 directed legal transitions. The illustrated board
  has Manhattan 2 and actual distance 2.
- Reproduced the IDA* example with two goal states and
  alphabetical A-before-B order: bound 2 excludes f values
  6 and 3; bound 3 returns S→B→G_B at cost 3.
- Checked regular-tree IDDFS ratios at depth 20: for b=2,
  1.9999899864; for b=10, 1.1111111111. The asymptotic
  ratios and b=1 exception are correct.
- Extended existing IDA*/RBFS checks to 3,321 finite
  three-vertex graph/admissible-heuristic cases with edge
  choices absent/0/1. Both matched independently computed
  Floyd–Warshall optima, including unreachable goals.
  These calculations use the existing implementations;
  they supplement, rather than independently replace,
  the reviewed proof and pseudocode comparison.
- Built the two proposed 504-state pattern tables by
  zero/one queue search and checked the values reported
  under W5-1. Independently BFS-checked the concrete
  board's true optimum of 22.

An initial attempt to import `check_extensions.py` lacked
its `checks` module search path and stopped before checking
anything. Rerunning with `PYTHONPATH=checks` succeeded;
the evidence above refers to the successful run.

### Rendering inspected

Ran the existing browser script against the existing built
book: 45 views passed, with no automated failures. Report:
`/tmp/weeks3-5-browser-review.json`. Screenshots:
`/tmp/search-book-browser-M3qhGM/`.

Manually inspected the reopening and Manhattan figures in
their chapters at desktop, narrow width, and 200% text;
also inspected narrow Week 3 IDDFS pseudocode and desktop/
narrow RBFS pseudocode. Labels, arrows, values, and prose
agree; no clipping/overlap was found. Pseudocode scrolls
horizontally in narrow view rather than breaking the page.

**Optional figure-accessibility refinement:** at 390 pixels
the 880-pixel SVGs scale labels to roughly 7–8 CSS pixels.
Their desktop and enlarged-text appearances remain clear,
but enlarging text alone does not enlarge SVG labels.
Clickable full-size originals and detailed alternative
text already mitigate this. Consider a visible "Open
full-size figure" cue or a narrow-layout treatment before
claiming the figures are comfortably legible inline on a
phone. This is not an automated overflow failure.

Week 3 has no figure, so its important graph/policy
comparisons received source and rendered-code/table review,
not a nonexistent figure review. No new build was necessary
for this read-only review; the screenshot run used the
existing build, whose target chapter text matched the
reviewed unchanged source. Root's concurrent bibliography
work is outside these screenshots.

## Primary-source access and limits

The following primary pages/passages were checked on the
review date. This was metadata/abstract and selected-passage
verification, not a claim of full-paper review:

- [Korf 1985 publisher page](https://www.sciencedirect.com/science/article/abs/pii/0004370285900840):
  title, author, year, journal details, and abstract agree
  with the reading description. The DOI resolver failed
  in the browsing tool; the publisher page was reachable.
- [Korf's IJCAI 1985 IDA* paper](https://ijcai.org/proceedings/1985/208):
  selected algorithm passage corroborates the initial h
  threshold and minimum-exceeded-f update. It explicitly
  distinguishes its tree analysis from duplicate-rich
  graphs. This is an additional accessible primary reading,
  not the identical journal article cited in the book.
- [Dijkstra publisher page](https://link.springer.com/article/10.1007/BF01386390):
  author/title/year/pages verified; subscription preview
  did not permit review of the full algorithm paper.
- [Dechter–Pearl author-hosted paper](https://ics.uci.edu/~dechter/publications/r0.pdf):
  title and selected abstract/introduction checked. The
  original ACM DOI returned 403. The paper's distinction
  between admissibility and stronger efficiency conditions
  is consistent with the chapter's cautious description.
- Hart–Nilsson–Raphael's supplied IEEE DOI reached a
  JavaScript/robot-verification page. No full-paper support
  claim is made from that access failure.
- [Korf–Felner 2002 publisher page](https://www.sciencedirect.com/science/article/pii/S0004370201000923):
  author/title/year and abstract support the broad additive
  pattern-database description. No full-paper review.
- [Korf 1993 publisher page](https://www.sciencedirect.com/science/article/pii/000437029390045D):
  title/year and abstract confirm RBFS and the linear-space
  best-first subject. Its experimental constant-factor
  time observation should not be promoted to a universal
  guarantee; this chapter correctly does not do so.
- [Korf 1998 publisher page](https://www.sciencedirect.com/science/article/pii/S0004370298000861)
  and the [linked manuscript](https://web.cecs.pdx.edu/bart/cs510cs/papers/korf-ckk.pdf):
  metadata/abstract and manuscript title-page date checked;
  they explain the 1997-preprint/1998-publication distinction.

Finite tests do not establish the infinite-space claims,
general PDB abstraction correctness, arbitrary state-size
memory bounds, or worst-case RBFS regeneration behavior.
Those were reviewed by their stated assumptions and short
arguments. The most important follow-up is a teaching pass
on W3-1/W3-2 and W5-1/W5-2 plus point-of-use citations,
while retaining the existing careful qualifications.
