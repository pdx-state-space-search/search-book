# Introduction and Week 1 review

Reviewed 2026-10-27 against BOOK-NOTES.md and the requested
scope. Read the introduction, Week 1, notation, attribution,
book metadata, license, Week 2 opening and closing sections,
and search-growth SVG source. Compared the earlier Week 1
opening. No chapter files were changed. No prev/ access.

## Must-fix findings

None found in the prose or mathematical examples.
Figure rendering and visual QA remain with the root agent.

## Assessment

- The rewrite meets the requested conceptual change. Partial
  assignments, complete candidate repair, constrained
  optimization, and routes all receive concrete explanations.
  Transition cost is a special case of candidate quality;
  solver effort is explicitly separate.
- The course philosophy centers tractable instances of
  NP-hard families, without claiming exponential lower bounds
  from NP-hardness or candidate counts. The input-length versus
  search-depth distinction is especially helpful.
- The growth explanation treats the knee as crossing a fixed
  resource budget, rather than asserting a discontinuity in
  the mathematical growth curve. Pruning is explicitly an
  illustrative reduction in uniform branching, with a clear
  warning about irregular real instances.
- Recomputed 3^20, the three binary-tree counts and times,
  and the budget thresholds. All agree with the text.
  For the figure, totals are 349,525 and 1,398,101 at b=4,
  depths 9 and 10; 524,287 and 1,048,575 at b=2, depths 18
  and 19. Twenty binary levels require a factor 1,048,576,
  supporting the approximate millionfold-speedup statement.
- The coloring assignment and both partition sums are correct.
  Nonnegativity establishes the stated optimality certificate.
  The incumbent/lower-bound discussion correctly requires
  feasibility and a minimization objective.
- Completeness and termination on failure are distinguished.
  Duplicate dominance is qualified by equivalent continuations.
  These statements support later chapters without making
  unjustified algorithm guarantees.
- Week 2 smoothly specializes the general Week 1 discussion.
  Reusing the same four-region graph and coloring reinforces
  the connection. The ending points naturally toward systematic
  exploration after propagation.
- ChatGPT authorship with Bart's guidance and review is explicit
  and consistent across introduction, attribution, metadata,
  and license. No deferred early-AI or historical-hardware
  narrative was introduced. The hardware paragraph is an
  arithmetic scaling example, not a historical claim.

## Optional refinements

1. Week 1, after the NP-hardness emphasis or route example:
   one sentence could say that search also applies to families
   with efficient general algorithms, while this course's
   motivating difficulty is NP-hard families. This would head
   off the inference that ordinary nonnegative shortest-path
   problems are NP-hard. Current wording is a course stance,
   not an incorrect formal claim, so this is not a blocker.
2. Week 1, lines 335-338: "Local improvement can cycle" could
   become "Local search can cycle". Strictly improving a
   fixed objective cannot cycle; sideways or worsening moves
   can. The surrounding intended point is sound, but the more
   general term avoids that small ambiguity.
3. Notation: C*, U, and L are described using "cost" whereas
   Week 1 deliberately uses objective value. "Optimal objective
   value" and "objective value of a feasible incumbent" would
   reinforce the broadened framing. Path-specific c, g, and h
   can retain their current meanings.
4. For figure QA, inspect the left vertical axis label at normal
   reading width. Its SVG text anchor lies near the canvas edge
   (x about 2.43 pt before rotation). This is a visual check,
   not a confirmed clipping defect. The SVG title, description,
   curve formulas, and integer-depth claims are consistent.
