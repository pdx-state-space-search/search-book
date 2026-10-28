# Notes On State-Space Search Book
Bart Massey 2026-10-27

* In every paragraph, assume that the reader has minimal
  knowledge beyond what they have been told previously here:
  just a basic knowledge of CS.

* When referencing a problem in later text, always name the
  problem. For example, "[In number partitioning, o]ur
  partition with imbalance 4 supplies U=4."

* Don't be parsimonious with diagrams, explanations etc. It's fine to be a little more verbose for clarity.

## Week 1

* The three examples each need a diagram. Refer to the
  problems by their formal names: map coloring, number
  partitioning, and pathfinding. Need to decide early whether we are doing map coloring or graph coloring as an example, and stick with that even in subsequent chapters or change to the other explicitly later.

* Break out a discussion of complexity classes, problems and
  instances in full. Make students understand that a
  collection of problems might form a class, and that a
  problem can be thought of as a set of instances.

* "Growth as a practical limit" starts talking about map coloring again at the beginning, without referencing the previous discussion. Please make sure that things like "color" don't come out of nowhere, in general.

* Avoid "search nodes" as a term: it is confusing. Instead label the y axis of graph 1 as "Total nodes examined".

* Complexity theory uses some measure of "instance size": it is often, but not always, input representation length.

* Avoid technical terms like "schedule makespan" unless they have been or are going to be explained. "schedule length" would be fine here.

* Emphasize the importance of node count as providing a machine-independent measure of cost. Mention the normal assumption of polynomial time per node.

* "partition repair" and "sliding tile puzzles" again come out of nowhere. Omit them, or replace them in the examples if something already discussed is handy. 
## Week 2

* TOC says "Constraints and SAT". Title says "Constraints and Propagation". These kind of small errors are deadly: use all caution when constructing text.

* "Variables, domains and constraints":

  * The formal description kind of comes out of nowhere. Always avoid this: in this case, first explain the role of variables and values in real problems clearly.

  * The constraint graph here needs a diagram

* "A small SAT encoding"

  * CNF needs a reminder explanation. Students won't have seen this for a while.

  * Might as well jump to quantified prop logic right away. This makes
    the sudden appearance of "rU" and "rV" make sense. Again, this will need some explanation.

* "Choosing variables and values"

  * Explicitly use the terminology "most-constrained first" and "least-constraining first" here. Explain that the former causes faster failure when going wrong, and the latter increases the probability of going right.

* Let's save AC-3 until chapter 10. I think it's more than is needed in this introductory chapter, and the explanation is hard.

* Cite Tsang's "Foundations of Constraint Satisfaction" and one of Crawford et al's papers on tableaux and the original WSAT paper in the readings.

