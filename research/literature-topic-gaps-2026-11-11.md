# Literature-informed teaching gaps

Research review, 2026-11-11. This note proposes priorities;
it does not change the agreed outline or chapter sources.

## Scope and judgment

Question: beyond stronger anytime and inadmissible-heuristic
treatment, which omissions deserve attention in a ten-week
introductory combinatorial state-space search course?

I reviewed BRIEF.md, BOOK-NOTES.md, STATUS.md, OUTLINE.md,
the bibliography, all chapter headings, and the relevant
existing passages. The repository authoring skill and its
editorial guide governed the review. AC-3, exercises, and a
new planning or reinforcement-learning unit remain excluded.

My ranking is:

1. Teach one example of learning from failure.
2. Teach ordinary beam search as selective frontier retention.
3. Make symmetry reduction a worked modeling argument.

The third is an underdeveloped existing idea, not an absent
topic. These choices add three different answers to a central
question: why may a search stop considering an alternative?
A conflict can prove a family impossible; beam pruning can
discard a family without such proof; symmetry can retain an
equivalent representative. That comparison is more valuable
here than extending an algorithm catalog.

The placements and word estimates below are editorial
judgments, not claims from the cited papers. Proposed examples
are original and use the book's conventions. The source
checks were targeted passage checks, not full-paper reviews.

## 1. Learning from failure: a concrete nogood

### Current coverage

Week 2 already teaches decisions, unit propagation, conflict,
and backtracking. Its closing SAT passage mentions learned
clauses and jumping over decisions, but supplies neither a
learned clause nor a trace. The outline explicitly avoids
developing a full clause-learning solver. The bibliography
has DPLL and TABLEAU, but no primary conflict-learning source.

### The missing lesson

Show that a failed branch can produce reusable information
about many branches. A beginner who sees only chronological
backtracking may reasonably think failure merely advances
the enumeration. Explain how a reason for failure can survive
restoration, become a constraint, and cause later propagation.

This is a different use of memory from a reached-state table,
tabu list, incumbent, or cached heuristic. It connects search
to inference without requiring statistical learning or a new
AI subfield. It also gives substance to the book's insistence
that justified deletion differs from promising ordering.

The GRASP report's Section 3 describes extracting a conflict
condition, recording its negation as a clause, and using the
result for further implications and nonchronological
backtracking. It also identifies analysis overhead and clause
storage as costs. This supports a small conceptual treatment;
it does not require importing the report's full machinery.
[Marques Silva and Sakallah, 1996][grasp]

### A small original example

Consider the four clauses:

- ¬a ∨ ¬b ∨ p
- ¬a ∨ ¬b ∨ q
- ¬p ∨ ¬q
- z ∨ r

Decide a=true, then z=true, then b=true, propagating after
each decision. The first two clauses now require p=true and
q=true, which contradicts the third. The z decision did not
cause this conflict. Regardless of z and r, a and b cannot
both be true, so learn ¬a ∨ ¬b.

Undo the decisions after a=true. The learned clause now
forces b=false. Explain that the z decision was undone too;
the solver need not preserve irrelevant assignments to gain
the benefit of skipping their alternatives during this
conflict. A small implication diagram could replace lengthy
resolution notation. The argument that a=true and b=true
force the contradiction justifies the learned clause directly.

An exhaustive check over all 64 assignments found 27 models
of the formula, all satisfying the proposed learned clause.
This verifies the example; the direct implication argument
explains its correctness.

### Placement and cost

Extend Week 2, Part II, “Combining decisions and deductions
in SAT,” by approximately 450–650 words and one short trace.
Retain the introductory DPLL account. Call the example a
first look at conflict learning, not a specification of CDCL.
Leave implication-point selection, restart policy, watched
literals, clause deletion, and industrial heuristics to
further reading. Week 2 is already a pressure point, so this
should replace the current vague practical-solver paragraph
and use its prerequisites rather than start a third SAT unit.

## 2. Beam search: keeping only selected alternatives

### Current coverage

Beam search is absent from the outline, chapter sources, and
bibliography. Greedy best-first search retains alternatives;
IDA* and RBFS recover forgotten work. Local search mainly
changes complete candidates. None supplies the simple case
of deliberately and permanently restricting a constructive
search frontier to its best-ranked members.

### The missing lesson

A width limit is a concrete resource choice students can
understand immediately. Teach one level-synchronous variant:
expand the retained layer, rank its children, keep at most w,
and discard the rest. Explain what happens to the discarded
work and why failure does not establish infeasibility.

The background section of Zhou and Hansen's beam-stack paper
describes this conventional beam search and its lack of
completeness. The paper then adds a recovery mechanism to
restore coverage. Its background is an accessible primary
reading even if beam-stack itself stays optional.
[Zhou and Hansen, 2005][beam]

For this course, the key comparison is permanent discard
versus regeneration. Even an admissible estimate does not
justify width pruning. Thus this addition remains useful
after the requested stronger treatment of inadmissible
heuristics: the lost guarantee comes from the retention rule,
not necessarily the estimator.

### A small original example and boundaries

Let S have successors A and B with costs 1 and 2. A is a
dead end; B reaches goal G at additional cost 1. Use h=0 and
rank by g+h in a width-one level beam. It retains A and
discards B, then fails, although S→B→G exists. The heuristic
is admissible and consistent. Ordinary UCS retains B and
eventually finds G. This isolates the effect of deletion.

Specify whether goals are tested before or after selection,
how ties are resolved, and whether duplicate detection is
within a layer or global. The example has no ties, duplicate
states, or generated goals in its discarded first layer.

Do not identify width-one beam search with the book's greedy
best-first algorithm: their retained alternatives differ.
Do not claim total memory is O(w) without accounting for
children awaiting selection and path reconstruction. A beam
width bounds retained layer size; it does not by itself bound
every piece of solver storage.

### Placement and cost

Add approximately 350–500 words to Week 5's limited-memory
part, preferably as its closing comparison after RBFS.
Use one small tree and a clear loss-of-coverage example.
Leave beam-stack's backtracking details as further reading;
they would duplicate some of the requested anytime expansion.
Do not shorten the already-needed IDA* and RBFS traces just
to fit another named algorithm.

## 3. Symmetry reduction: explain the representative

### Current coverage

Week 8 already has “Canonicalization and equality.” It says
that exchanging identical boxes can create artificial
duplicates, requires preservation of futures, costs and goals,
and warns about reconstructing concrete object identities.
The outline retains this. Accordingly, “add symmetry” would
misdescribe the actual gap.

The gap is a worked example showing why a representative
exists and what is lost when it is chosen. This belongs to
modeling and correctness, not just faster hashing.

### The missing lesson

Use the book's coloring instance: vertices A, B, C, D;
edges AB, AC, BC, CD; three interchangeable color names.
Require A=red. Every proper coloring can be renamed to meet
this requirement, so satisfiability is preserved. The
restriction removes legitimate labeled answers, however:
enumerating every labeled coloring would require a different
account. Fixed color meanings or precolored vertices can
invalidate the argument.

An exhaustive check of the 81 assignments found 12 proper
colorings, four with A=red. The proof is color renaming,
not the count. A second normalization could remove more
symmetry, but one correct reduction is enough here.

Crawford and colleagues describe adding symmetry-breaking
predicates to a theory, including partial symmetry breaking,
so that existing search procedures can exploit symmetry.
Their work supports distinguishing model-level restrictions
from specialized traversal algorithms. The proposal here
needs no group theory or automatic symmetry detector.
[Crawford et al., 1996][symmetry]

### Placement and cost

Expand or replace Week 8's brief canonicalization passage
with about 250–400 words and the coloring example. Explain
both a constraint choosing a representative and a state key
identifying equivalent configurations. They implement related
reasoning at different points in the solver.

This is cheaper than a new structural-search section and
builds on the book's existing restoration, equality, and
model-correctness themes. A short Week 2 forward reference is
optional, not necessary.

## Strong alternatives to defer

### Limited discrepancy search: first alternate

LDS is absent. Its distinct insight is to search according to
the number of departures from a successor-ordering heuristic.
Harvey and Ginsberg explain why chronological backtracking
can spend its budget below one early bad choice; their
increasing-discrepancy procedure eventually covers a finite
binary tree when its limit reaches maximum depth. This is
guidance without a cost-to-go estimate.
[Harvey and Ginsberg, 1995][lds]

It would make an excellent Week 3 bridge from CSP ordering
to iterative deepening, or a Week 5 optional reading. A real
treatment needs approximately 350–500 words and a trace
contrasting “one early discrepancy” with many late changes.
Do not call it already covered by variable/value ordering.

I rank it below beam search for this outline because beam
fills the more basic missing retention policy. If the
instructor wants stronger emphasis on constructive assignment
search, LDS is a reasonable substitute for the third
recommendation's expanded symmetry treatment. I would not
automatically add both algorithms to the required reading.

### Incremental replanning: further reading

The book discusses improved arrivals within a run and
transposition reuse, but not repairing search results after
the graph itself changes. D* Lite applies incremental
heuristic search to repeated navigation problems and reuses
earlier search information as edge costs change.
[Koenig and Likhachev, 2002][dlite]

This is a real omitted problem setting, not the same as
incremental objective evaluation in Week 6. For a general
combinatorial introduction it is less central than the three
recommendations above. Add a short Week 8 or Week 10 reading
annotation if desired. A proper algorithm treatment brings
additional labels, consistency conditions, queue rules, and
repair invariants; it should replace another substantial
topic rather than be squeezed into the closing survey.

## Tempting recommendations that overstate the gaps

**Dominance is already present.** Week 3 explains depth-budget
dominance; Week 4's improved arrivals embody cost dominance;
Week 9 distinguishes reusable bounds and hints. Make those
instances explicitly share the idea “retained work covers
this alternative's useful futures.” A new generic dominance
algorithm would add terminology before it adds teaching value.

**Decomposition is partly present.** Week 10's conflict-based
MAPF example separates individual path searches and resolves
their coupling; Week 7 solves restricted subproblems inside
a heuristic outer search. Neither is the general theory of
independent constraint components or tree decomposition.
That broader idea is missing, but a full structural-CSP unit
would compete with the already dense Week 2. Keep the current
examples' independence and coupling assumptions explicit.
Do not imply that large-neighborhood search automatically
discovers independent factors or proves a global optimum.

**Memory-bounded search is not a gap.** IDA*, RBFS, memory
accounting, and pattern-database storage are already assigned.
The beam proposal fills a guarantee tradeoff within that
coverage rather than adding memory as a new subject.

**Modern SAT is not wholly absent.** The current bridge is
correct but too abstract to teach its mechanism. One learned
clause is the recommended increment; a CDCL implementation
chapter would exceed this review's scope.

## Verified primary sources and access limits

1. João P. Marques Silva and Karem A. Sakallah,
   *GRASP—A New Search Algorithm for Satisfiability*,
   University of Michigan CSE-TR-292-96, April 10, 1996.
   [Institutional PDF][grasp]. Checked the report identity
   and Section 3's conflict clauses, backtracking, and costs.

2. Rong Zhou and Eric A. Hansen,
   *Beam-Stack Search: Integrating Backtracking with Beam
   Search*, ICAPS 2005. [Conference PDF][beam]. Checked the
   introduction and background definition of ordinary beam
   search. The recommended required material is that basic
   policy; beam-stack is a possible reading connection.

3. James Crawford, Matthew Ginsberg, Eugene Luks, and
   Amitabha Roy, *Symmetry-Breaking Predicates for Search
   Problems*, KR 1996, pp. 148–159.
   [Institutional PDF][symmetry]. Verified the reachable
   14-page scan, institutional abstract, and conference
   proceedings listing. The PDF has no extractable text in
   the web tool; do not claim a full-paper reading. The
   university metadata page has an erroneous “Dec 1969”
   field; the conference record establishes 1996.

4. William D. Harvey and Matthew L. Ginsberg,
   *Limited Discrepancy Search*, IJCAI 1995.
   [Proceedings page][lds] and
   [conference PDF](https://ijcai.org/proceedings/1995/0080.pdf).
   Checked Sections 2.2 and 3, including the finite-tree
   coverage condition and repeated work across iterations.

5. Sven Koenig and Maxim Likhachev, “D* Lite,” AAAI 2002,
   pp. 476–483. [Conference PDF][dlite]. Checked the abstract,
   navigation motivation, and the description of LPA*'s
   retained g and rhs values. The recommendation is a reading
   direction, not a verified implementation specification.

[grasp]: https://www.eecs.umich.edu/techreports/cse/1996/CSE-TR-292-96.pdf
[beam]: https://cdn.aaai.org/ICAPS/2005/ICAPS05-010.pdf
[symmetry]: https://www.cs.uoregon.edu/Reports/TR-1996-012.pdf
[lds]: https://ijcai.org/proceedings/1995/80
[dlite]: https://cdn.aaai.org/AAAI/2002/AAAI02-072.pdf
