# Week 2: Constraints and SAT

A timetable chooses a time and room for each class. A
configuration chooses compatible components. Graph coloring
chooses a color for each vertex. In each case, we have named
choices, possible values for those choices, and rules about
which combinations are permitted. We can describe the rules
before choosing a particular way to search for an answer.

This chapter develops that description as a constraint
satisfaction problem, then shows how Boolean formulas can
express the same kind of task. We will combine choices with
simple deductions: try an assignment, work out its immediate
consequences, and undo it if those consequences contradict
the requirements. This supplies the book's main foundation
for SAT; [Week 6](06-local.md#sat-as-local-search) returns to
SAT using local search.

## Variables, values, and constraints

Start with the graph coloring instance from Week 1: vertices
A, B, C, D; edges AB, AC, BC, CD; and colors red, green,
blue. The choice "which color does A receive?" becomes a
**variable**. Red is one possible **value** for that variable.
Its **domain** is the set of allowed values, initially
{red, green, blue}. We use the vertex name A for its color
variable too; the surrounding description tells us which
role the name has.

A **constraint** restricts combinations of values. Edge AB
requires A≠B: the variables for A and B must receive
different colors. We may assign A=red and B=green together,
but not A=red and B=red. C and D have the same kind of
inequality constraint, while A and D can share a color
because there is no edge AD.

A **constraint satisfaction problem**, or CSP, consists of
variables, their domains, and constraints. A solution is a
complete assignment satisfying every constraint. Here we
consider finite sets of variables with finite domains.
The notation X₁, …, Xₙ names n variables, and D(X) denotes
the domain of variable X. The notation packages choices
we can already describe in words.

For a timetable, a variable might choose one class's room
and time, with values such as (Room 10, Monday at 9).
Constraints can prohibit two classes using the same room
at the same time. A useful model makes the choices and the
rules explicit enough that the solver can check them.

A constraint on a group of variables specifies permitted
combinations of their values. A **unary** constraint concerns
one variable, a **binary** constraint a pair, and a
**higher-arity** constraint three or more variables. The
color inequalities above are binary. A timetable's room
capacity restriction can limit one class's choices; a rule
limiting total simultaneous resource use may concern many
classes together.

For binary CSPs, the **constraint graph** has one vertex per
variable and an edge between variables sharing a constraint.
For graph coloring, this is the graph being colored:

[![The constraint graph for color variables A, B, C, and D has edges AB, AC, BC, and CD. The pictured colors are one satisfying assignment.](figures/graph-coloring.svg)](figures/graph-coloring.svg)

*Each vertex represents a color choice, and each edge an
inequality. The colors show the feasible assignment from
Week 1. C participates in three constraints; D in only one.*

A **partial assignment** gives values to some variables.
It is locally consistent if it violates no constraint whose
variables have all been assigned. This is a weak condition:
it does not say that we can complete the assignment. For
example, assigning one vertex of a two-color triangle
violates no edge yet, although the triangle has no proper
two-coloring.

A **current domain** contains values still considered
possible under the current branch and its deductions. It
can be smaller than the original domain. An empty current
domain establishes failure of that branch. Values removed
because of a choice must be restored when the solver undoes
that choice, unless another active reason still excludes them.

Some constraints concern a whole collection. An
**all-different** constraint requires every variable in a
group to have a distinct value. Three variables choosing
from {1,2} cannot all differ, although any two can differ.
A specialized check can recognize that shortage directly.
Equivalent descriptions of the valid assignments need not
make the same deductions equally easy.

## Propositional formulas and CNF

A **Boolean variable** takes the value true or false.
A propositional formula combines Boolean variables using
logical connectives. We write ¬ for "not," ∨ for "or,"
and ∧ for "and." A **truth assignment** chooses true or
false for each Boolean variable. A formula is satisfied
when it evaluates to true under that assignment.

For example, p∨q holds when at least one of p and q is true.
The disjunction includes the possibility that both are true.
The formula ¬p holds when p is false. The conjunction
(p∨q)∧¬p requires both parts to hold, so it forces p=false
and q=true. Parentheses specify how the parts are grouped.

A **literal** is a Boolean variable or its negation: p and
¬p are literals. A **clause** is a disjunction of literals,
such as p∨¬q∨r. It holds when at least one listed literal
is true. A one-literal clause such as ¬q is allowed.
A formula is in **conjunctive normal form**, or CNF, when
it is a conjunction of clauses. For example,

**(p∨q) ∧ (¬p∨r) ∧ ¬q**

has three clauses: p∨q, ¬p∨r, and ¬q. All three must hold.
Boolean satisfiability, or **SAT**, asks whether a formula
has any satisfying truth assignment. A solver either finds
one or establishes that none exists. We will use CNF so
that each clause states one explicit requirement.

## Encoding graph coloring as SAT

Return to graph coloring, now with a triangle A, B, C and
only red and blue available. Introduce Boolean variables
r_A, r_B, and r_C. The statement r_A means "vertex A is red."
True means red; false means blue. This interpretation works
because there are exactly two color choices.

For edge AB, the clause r_A∨r_B rules out both endpoints
being blue. The clause ¬r_A∨¬r_B rules out both being red.
Together the two clauses express different endpoint colors:

**(r_A ∨ r_B) ∧ (¬r_A ∨ ¬r_B).**

We need the same pair of clauses for every edge. In a
compact formula, let U and V stand for vertex names and
let E be the finite edge set {AB, BC, CA}:

**∀ edge UV∈E: (r_U ∨ r_V) ∧ (¬r_U ∨ ¬r_V).**

The symbol ∀ means "for every." Here it abbreviates a
finite conjunction: write the body once for AB, once for
BC, and once for CA, and join those copies with ∧. This
**grounded expansion** substitutes actual vertex names for
U and V. The indexed name r_U becomes r_A when U=A;
it names a Boolean variable, rather than adding another
unknown color or another kind of truth value.

| Edge | Clauses produced by expansion |
| --- | --- |
| AB | (r_A ∨ r_B), (¬r_A ∨ ¬r_B) |
| BC | (r_B ∨ r_C), (¬r_B ∨ ¬r_C) |
| CA | (r_C ∨ r_A), (¬r_C ∨ ¬r_A) |

The expanded CNF has three Boolean variables and six
clauses. With r_A=true, r_B=false, r_C=true, the first
two edges are satisfied but CA is violated. In fact there
is no satisfying assignment: making A red forces B blue
and C red, contradicting CA. Making A blue gives the
symmetric failure. The formula and this graph coloring
instance have exactly the same solutions: none.

### More than two colors

For a general graph, let V be its finite vertex set, E its
edge set, and K its finite set of allowed colors. Use one
Boolean variable p(v,c) for every vertex v and color c.
For example, p(A,red) means "A receives red." Parentheses
are part of our naming convention: this denotes a Boolean
variable for a particular vertex/color pair.

We require at least one color for each vertex:

**∀v∈V: ∃c∈K: p(v,c).**

The symbol ∃ means "there exists." Over a finite set of
color names it abbreviates a disjunction. With
K={red,green,blue}, the rule for A expands to

**p(A,red) ∨ p(A,green) ∨ p(A,blue).**

The outer ∀ repeats this clause for each vertex and joins
the clauses with ∧. Both quantifiers are shorthand over
explicit finite index sets. After expansion, the result is
an ordinary propositional formula for a SAT solver.

At least one color is insufficient: it would permit A to
receive red and green simultaneously. To require at most
one, add a clause ¬p(v,c)∨¬p(v,d) for every vertex v and
every unordered pair of distinct colors c,d. For A and our
three colors, these are

**(¬p(A,red)∨¬p(A,green)) ∧
(¬p(A,red)∨¬p(A,blue)) ∧
(¬p(A,green)∨¬p(A,blue)).**

Finally, adjacent vertices must not share a color. For each
edge uv and each color c, add ¬p(u,c)∨¬p(v,c). These three
families of clauses require exactly one color per vertex
and different colors across every edge.

For example, edge AB produces ¬p(A,red)∨¬p(B,red) for red.
Both variables cannot be true, so the endpoints cannot
both be red. Repeat for green, blue, and the other edges.

An encoding needs both directions of reasoning. Every proper
graph coloring makes these clauses true by setting exactly
its selected vertex/color variables true. Conversely, every
satisfying assignment selects exactly one color per vertex,
and the edge clauses ensure a proper coloring. Missing an
at-most-one or edge constraint can admit invalid answers;
adding an unintended restriction can exclude valid ones.

SAT is an NP-complete decision problem. Many useful
instances still admit practical solutions, as discussed in
Week 1. Encoding an application as SAT lets us use an
existing solver. A specialized CSP solver may instead work
directly with the original variables and constraints.
We should judge either approach by the correctness of its
model and the effort needed on relevant instances.

## Backtracking search

A straightforward CSP solver chooses an unassigned variable,
tries a value, and continues recursively. If the choice
violates a constraint or deductions produce an empty domain,
it rejects that branch. If every value for the selected
variable fails, it returns to an earlier choice. This is
**backtracking**.

Here n denotes the number of variables and k an upper bound
on each domain's size. There are at most kⁿ complete
assignments. With 20 variables and four values each,
4²⁰=1,099,511,627,776. If the first two choices violate a
constraint, there is no reason to extend them through the
remaining eighteen variables. Rejecting partial assignments
is the source of much of backtracking's practical power.

For finite domains, backtracking is complete if it eventually
tries every relevant value, restores branch state correctly,
and prunes only branches with no solution. Ordering rules
change which branches are reached first. Sound deductions
can remove branches that need never be reached. These
contribute to performance in different ways.

A failed branch must leave no residue in its siblings.
In graph coloring, suppose A=red caused red to be removed
from B's current domain. Undoing A=red must restore that
removal unless another active reason still excludes red.
Copying domains for each branch makes this conceptually
simple. A **trail** instead records changes so they can be
undone in reverse order. Either method must restore exactly
the information belonging to the abandoned choice.

## Choosing variables and values

**Most-constrained first** chooses an unassigned variable
with the fewest currently available values. This is also
called **minimum remaining values**, or MRV. Its fail-first
purpose is to discover a wrong branch quickly: confront a
tight choice before doing work on easy choices that may
later have to be undone. A zero-size domain means failure;
a one-value domain may force a choice without branching.

**Degree ordering** can break MRV ties by choosing the
variable with the most unassigned neighbors. In our graph
coloring instance, C interacts with A, B, and D; D interacts
only with C. Degree is a rough measure of influence, since
constraints differ in restrictiveness.

After selecting a variable, **least-constraining first**
tries a value leaving the most flexibility for other
variables. This is the **least-constraining value**, or LCV,
rule. Its purpose is to improve the chance that the current
branch can be completed successfully.

For example, in graph coloring suppose A borders B and C,
with B's current domain {red,green} and C's {blue,green}.
Choosing A red removes one neighbor value, as does choosing
A blue. Choosing A green removes two. LCV prefers red or
blue in this local calculation. It tries to preserve useful
options rather than consume them early.

These intuitions complement each other: choose the variable
most likely to expose a failure, then try its value least
likely to cause one. They are heuristics, not guarantees
about every instance. Computing their scores also takes
work, so both ordering effects and overhead matter.

## Forward checking

After assigning a variable, **forward checking** removes
values in neighboring unassigned variables that conflict
with the new assignment. If a domain empties, backtrack
immediately.

Return to our graph coloring instance with edges AB, AC,
BC, CD and three colors. Assigning A=red removes red from
B and C. D is unaffected because AD is not an edge.
Assigning B=green then removes green from C, leaving
C={blue}.

| Stage | B domain | C domain | D domain |
| --- | --- | --- | --- |
| Initially | red, green, blue | red, green, blue | red, green, blue |
| A=red | green, blue | green, blue | red, green, blue |
| B=green | green (assigned) | blue | red, green, blue |
| C=blue | green (assigned) | blue (assigned) | red, green |

Choosing D=red or D=green completes a valid graph coloring.
The trace distinguishes assigning C from noticing its
singleton domain. Automatically assigning such forced
variables is another possible policy; we should state
whether the solver does that.

Forward checking processes consequences of the latest
assignment on neighboring unassigned variables. It need
not recognize a contradiction before any assignment is
made. In the two-color triangle from the SAT encoding,
all initial domains are nonempty. Assigning A=red leaves
both B and C with only blue. Assigning B=blue then empties
C's domain. Trying A=blue gives the symmetric failure.
Exhausting both choices proves that this instance has no
proper two-coloring.

A **sound** deduction never removes a value that occurs in
a solution of the current branch. A **complete** solver
finds a solution whenever one exists under its stated
assumptions. Forward checking supplies sound deductions;
finite exhaustive backtracking supplies the remaining
coverage. A single deduction phase need not settle the
whole instance.

## Propagation and complete search in SAT

SAT's corresponding basic deduction is **unit propagation**.
Under a partial truth assignment, a clause is unit when
exactly one literal remains unassigned and all others are
false. That literal must be made true. An all-false clause
establishes a conflict, while a clause containing a true
literal is already satisfied.

Return to the CNF example (p∨q)∧(¬p∨r)∧¬q. The clause ¬q
forces q=false. Then p∨q forces p=true, and ¬p∨r forces
r=true. The resulting assignment satisfies every clause.
Each choice follows from a requirement; there was no need
to guess in this particular instance.

On another formula, unit propagation may stop while some
clauses remain unresolved. A complete SAT search can choose
an unassigned Boolean variable, try a truth value, propagate
again, and backtrack on conflict. Trying both truth values
as needed gives a systematic search over the finite
assignments. If every clause is satisfied while variables
remain unassigned, any completion preserves satisfaction;
the solver can fill in those variables to return a complete
truth assignment.

A contradiction under one decision rules out that branch,
not necessarily the formula. Only when all relevant branches
have been excluded is unsatisfiability established. This is
the same distinction between local consequences and complete
coverage that we saw in graph coloring.

Practical SAT solvers also analyze conflicts to learn
clauses and sometimes return past several decisions at once.
A learned clause must be justified by the formula; it cannot
merely prohibit an inconvenient candidate. The TABLEAU
solver in the Crawford–Auton reading gives a concrete
connection between branching, unit propagation, and measured
SAT difficulty. We need these underlying ideas here without
trying to cover an industrial solver's full design.

The next chapter develops systematic exploration more
explicitly. The question remains how to account for the
choices still available while using deductions to avoid
unnecessary work.

## Further reading

- Tsang, [*Foundations of Constraint Satisfaction*](https://www.bracil.net/edward/FCS.html)
  (Academic Press, 1993). A broad treatment of CSP models,
  inference, and search. Start with the introductory
  formulations and the overview of solving methods; the
  book provides deeper material beyond this course.
- Crawford and Auton,
  [“Experimental Results on the Crossover Point in
  Satisfiability Problems”](https://cdn.aaai.org/AAAI/1993/AAAI93-004.pdf)
  (AAAI-93, pp. 21–27). Describes TABLEAU and experiments
  relating random SAT instances' constraints to difficulty.
  Distinguish that measured crossover from the fixed-budget
  growth illustration in Week 1.
- Davis, Logemann, and Loveland,
  [“A Machine Program for Theorem-Proving”](https://doi.org/10.1145/368273.368557)
  (1962). An early systematic SAT procedure underlying the
  decision, propagation, and backtracking connection.
