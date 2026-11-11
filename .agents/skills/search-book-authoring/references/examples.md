# Annotated teaching examples

These examples calibrate decisions, not exact wording.
They reflect the revised chapters; future instructor feedback
can improve them. Read only the relevant examples for a small
edit. The neighboring chapter context still matters.

## Give notation a concrete referent

An abrupt start:

> Let X₁, …, Xₙ have domains D(X₁), …, D(Xₙ).

A more useful introduction:

> In graph coloring, the choice "which color does A receive?"
> becomes a variable. Red is one possible value. The domain
> is the set of allowed values, initially red, green, and blue.
> We write D(A) for that set.

The notation now names choices the reader understands.
The formal generalization can follow. See the opening of
[Week 2](../../../../src/02-constraints.md).

## Restore context when an example returns

An unsupported return:

> Our partition with imbalance 4 supplies U=4.

A clearer return:

> In our number partitioning instance, the partition with
> sums 17 and 13 has imbalance 4. It supplies the feasible
> upper bound U=4.
> The objective cannot be negative, so L=0 is a lower bound.

This names the problem, restores the objective, and explains
what the numbers mean. It does not require repeating the
whole earlier example. See the bounds discussion in
[Week 1](../../../../src/01-models.md).

## Explain program work before a tree metaphor

An unexplained metaphor:

> The program visits nodes of an exploration tree.

A concrete account:

> The program keeps records for candidates it is considering.
> A record contains the candidate state and information needed
> by the search. Creating another candidate can link its record
> to the record that produced it. Drawing those links gives a
> tree; the program need not construct the entire tree first.

Now a node count has a computational interpretation.
Repeated consideration of one state can still cost work.
Retain the distinction between states and records rather
than replacing every node count with a distinct-state count.

## Ground an indexed formula

Before using p(v,c), say that p(A,red) is the Boolean variable
meaning "A receives red." Let K={red,green,blue}. Then

> ∃c∈K: p(A,c)

abbreviates

> p(A,red) ∨ p(A,green) ∨ p(A,blue).

This demonstrates existence over a finite set of color
names as a propositional disjunction. Explain the matching
conjunction when repeating a rule for every vertex. Let the
expansion establish what the compact notation means rather
than presuming the reader knows the convention.

## Preserve a short argument, not just an outcome

A bare result:

> The partition with sums 15 and 15 is optimal.

An explanatory result:

> In our number partitioning instance, the groups {6,5,4} and {7,8}
> both sum to 15, so the imbalance is zero. No absolute
> difference can be negative; this feasible partition meets
> that lower bound and therefore is optimal.

The extra sentences connect the objective, feasibility,
bound, and guarantee. The point is to include the needed
reasoning, not to demand a formal proof for every arithmetic
observation.

## Separate intention from guarantee

A stronger claim than the heuristic supports:

> Least-constraining-first increases the probability of
> finding the right value.

A useful explanation:

> Least-constraining-first tries the value leaving the most
> flexibility in the remaining domains. It aims to preserve
> opportunities to complete the branch. Its benefit depends
> on the instance and the cost of estimating that flexibility.

The motivation remains clear without introducing an unstated
probability model or promising improvement on every case.
The same discipline preserves the existing draft's care
about weighted keys, lower bounds, sampled outcomes, and
optimality certificates.
