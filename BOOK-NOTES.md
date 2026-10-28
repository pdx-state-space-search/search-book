# Notes On State-Space Search Book
Bart Massey 2026-10-27

* The introduction should start with a fuller explanation of the goals and philosophy of state-space search. One or two paragraphs.

* The authorship should be made clear. This book was written by ChatGPT, with guidance and review by Bart Massey. I don't want to claim more than I did.

## Week 1

* The intro to this chapter implies that planning is the only reason to use state-space search. Mention should be made of constraint satisfaction, optimization under constraint, and other common uses of state-space search.

* In fact, the whole philosophy of this chapter ignores these things. It needs to be rewritten to talk about state exploration in language that doesn't make planning/pathfinding the only goal.

* The first section of this chapter should discuss the general philosophy of state-space search before diving into the technicalities: most students will have small familiarity with the whole discipline. Small examples would be really helpful. This will make this a larger chapter, which is ok.

* The connection between state-space search and NP-hard problems should be discussed in the context of state-space growth. Emphasize the sharp knee experienced in state-space solvers, and the relation to problem size. I generally take an overall philosophy that "State-space search is a technique used to solve tractable instances of NP-hard problems." I often draw a graph showing state-space growth with depth, to emphasize that even in a pruned space instance sizes will suddenly grow from "modest" to "intractable".

* I don't *think* transition cost is a general enough lens for this chapter? We often just count search cost in nodes searched or seconds: even many optimization problems don't care about finding optimal paths, just optimal nodes.



