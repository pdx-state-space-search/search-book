# Independent review of the Week 2 revision

Reviewed 2026-10-27. Read `BOOK-NOTES.md` first. Scope:
`src/01-models.md`, `src/02-constraints.md`, the new SAT
section and reading in `src/06-local.md`,
`src/notation.md`, and the four requested SVGs. No chapter
or figure files edited. No `prev/` content read.

## Must fix

1. **Crawford–Auton page range is off by one.**
   `src/02-constraints.md:387` currently gives pp. 21–26.
   The linked primary AAAI PDF starts at printed page 21
   and ends at printed page 27, including the conclusion,
   references, and figures on the last page. Use 21–27.
   This is also the range given in the references of the
   linked Selman–Kautz–Cohen 1994 paper.

   Source: [AAAI-93 primary PDF](https://cdn.aaai.org/AAAI/1993/AAAI93-004.pdf).

No technical must-fix was found in the grounded SAT
encoding, backtracking account, ordering heuristics,
forward-checking trace, unit propagation, or new local SAT
search section.

## Clarification initially flagged and discussed with root

At initial review, `src/01-models.md:285` still used
"yes-instances" in its NP definition. I reported this
because the review brief asked to avoid yes-instance
language. Root clarified that the main concern is avoiding
the identification of a problem with the language of its
yes-instances, while retaining a brief informal certificate
explanation, and plans to say "a yes answer" instead.
That rephrasing resolves this concern. The actual
problem/instance explanation at lines 175–196 already
uses a collection of parameter instantiations and includes
instances without solutions; it does not identify a problem
with only its positive instances.

## Optional clarity improvements

- **Introduce the word record at the first counted node.**
  Lines 207–212 of Week 1 say each pictured node represents
  a candidate, and explicitly deny the need to build the
  whole tree. The full record definition appears at
  lines 374–384. This meets the intent, but changing the
  first mention to "a candidate record considered by the
  solver" would make the software interpretation explicit
  before the time table and growth figure. This is a small
  improvement, not a missing explanation.

- **Distinguish the two meanings of n in the notation page.**
  The notation table uses n for a node, while Weeks 1 and 2
  explicitly use n for instance size or variable count.
  These are standard context-dependent uses, and each
  local use is explained. A short note in the table could
  prevent a beginner from treating n as a globally fixed
  symbol. No renaming throughout the book is necessary.

- **The k-color edge family could get one grounded example.**
  Week 2 explicitly grounds both two-color edge clauses
  and the general encoding's at-least-one and at-most-one
  clauses. The final edge family is correctly explained
  in words. A single example such as
  `¬p(A,red)∨¬p(B,red)` would finish the pattern for a
  reader who benefits from seeing every schema instantiated.
  The present explanation is already sufficient.

## Requirements that pass

- The example is consistently graph coloring. Map coloring
  is explained as its motivation, with an explicit move
  to graph representation. The four-vertex instance is
  reused correctly in Week 2, and the two-color triangle
  is explicitly introduced as a different instance.
- Week 1 defines n before k^n; Week 2 defines n and k before
  its assignment count. The discussion explicitly warns
  that size can count vertices, variables, items, or input
  bits, and refers formal treatment to an algorithms text.
- Node counts mean work on candidates. Generated and
  expanded counts are distinguished, node processing is
  explained through records, duplicate states are handled
  explicitly, and machine independence is qualified by
  the algorithm, ordering, and counting rule.
- Polynomial work per node is stated and includes successor
  generation and estimate evaluation. The book does not
  claim that merely having k^n candidates proves an
  exponential lower bound.
- Quantifiers in Week 2 range over finite named sets.
  Universal expansion is conjunction; existential expansion
  over colors is disjunction. The text explicitly grounds
  r_U to r_A and treats p(v,c) as indexed propositional
  variable names. There is no QBF detour or accidental
  quantification over truth values.
- The two-color triangle encoding has three Boolean
  variables, six clauses, and no satisfying assignment.
  Its worked red/blue failure is correct.
- The general encoding uses exactly-one color per vertex
  and prohibits shared colors across edges. Both encoding
  directions are explained, so a satisfying assignment
  can be decoded to an actual proper coloring.
- MRV is named most-constrained first and explained as
  fail-first; LCV is named least-constraining first and
  explained as preserving options. The LCV example removes
  one, two, and one neighbor values for red, green, and
  blue, respectively, as claimed.
- The forward-checking table correctly removes red from B
  and C after A=red, leaves only blue at C after B=green,
  and removes blue from D only after C is assigned blue.
  The text distinguishes a singleton domain from automatic
  assignment. Its unsatisfiable two-color triangle trace
  is also correct.
- Unit propagation on `(p∨q)∧(¬p∨r)∧¬q` correctly forces
  q=false, p=true, and r=true. The discussion separates
  branch conflicts from a complete unsatisfiability result.
- No AC-3 mention was found under `src/`; it has been
  removed rather than relocated.
- Tsang and Crawford–Auton are Week 2 readings. The Tsang
  author page confirms the 1993 Academic Press edition.
  The Crawford–Auton paper does describe TABLEAU.
- WalkSAT appears only in Week 6 under `src/`, including
  its reading. The SAT local trace has scores 1, 1, 0;
  flipping p is a valid sideways step and flipping r
  then satisfies every clause. The section accurately
  distinguishes repair over complete assignments from
  systematic search over partial assignments and rejects
  an unsatisfiability inference from a failed timed run.
- The linked 1994 Selman–Kautz–Cohen paper and its
  pp. 337–343 range are correct. The text cautiously says
  the strategies are associated with WalkSAT; it does not
  imply that every variant has identical noise rules.

## Independent numerical checks

Used a temporary Python enumeration, without changing
project source files:

- Enumerated all eight assignments of the two-color
  triangle CNF: zero satisfying assignments.
- Grounded the general encoding on vertices A–D, three
  colors, and AB, AC, BC, CD: 12 Boolean variables and
  28 clauses. Enumerating all 4,096 truth assignments gives
  12 models, matching the 12 proper graph colorings.
- Binary tree totals at depths 20, 30, and 40 agree with
  the table and its rounded elapsed times.
- Four children per node: depth 9 totals 349,525 nodes;
  depth 10 totals 1,398,101.
- Two children per node: depth 18 totals 524,287 nodes;
  depth 19 totals 1,048,575.
  Thus the claimed million-node budget boundaries are
  correct, including the root at depth zero.

## Figure inspection

Rendered all four original SVGs with local Chromium and
visually inspected the resulting screenshot. Labels fit,
no content was clipped, and the figures agree with their
captions and accessible descriptions:

- Graph coloring has exactly AB, AC, BC, CD, with
  A=red, B=green, C=blue, D=red.
- Number partitioning shows sums 17/13 and 15/15 and
  uses each listed weight exactly once per candidate.
- Pathfinding shows directed S→G cost 20 and S→A→G
  with cost 1 on each segment, totaling 2.
- Search growth uses "Total nodes examined", identifies
  the million-node budget, marks the correct last fitting
  integer depths, and states that both curves continue
  beyond the visible range. Its smooth curves are an
  acceptable illustration of the discrete depth counts.

Temporary visual artifact: `/tmp/review-figures.png`.

## Overall assessment

The revised chapter proceeds from concrete choices to CSP
terminology, refreshes Boolean logic before CNF, grounds
its compact formulas, then introduces complete search,
ordering, and propagation. The Week 6 addition has a clear
return link to Week 2 and appears after a concrete local
repair trace, so its complete-assignment interpretation
is already motivated. Apart from the citation range and
the NP wording change already accepted by root, the review
finds the requested revision technically sound and suitable
for its intended introductory audience.

## Integration follow-up

The root corrected the Crawford–Auton range to pp. 21–27.
The final text explains a node as a candidate record before
counting it, distinguishes local n meanings in the notation
reference, and supplies an explicitly grounded red-edge
clause. The four-vertex encoding is now in the reproducible
worked-example suite as well. Final rendered QA and all
checks are recorded in review-log.md.
