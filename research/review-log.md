# Editorial review log

## Contract and source inspection

- Root: /home/bart/work/search; new work confined to book/.
- Read front-matter/syllabus.md, including outcomes, old weekly
  sequence, prerequisites and bibliography.
- User approved compressing planning/scheduling, omitting exercises,
  language-neutral explanations, figures, and mdBook-only output.
- No student submissions or grading records read or reused.
- The syllabus contains legacy calendar/course administration;
  those details are not imported into the textbook.
- Installed mdBook: 0.5.2. Official configuration documentation
  checked at https://rust-lang.github.io/mdBook/format/configuration/.

## Independent finite algorithm checks

Run: python3 checks/check_algorithms.py

Passed initially:
- 25,792 admissible heuristic / graph cases for A* and weighted A*
  (three weights per case), including inconsistent heuristics and
  zero-cost cycles on finite graphs. Positive-cost subset also
  compared with IDA*. Reference optimum: Floyd–Warshall.
- All 4,096 binary constraint networks with three two-valued
  variables: AC-3 preserves all solutions and reaches the expected
  arc-consistency condition unless a domain is empty.
- All 6,561 depth-three binary game trees with leaf utilities in
  {-1,0,1}: alpha–beta agrees with full minimax.
- 5,184 number-partition move deltas checked directly, plus
  annealing probability and independent-restart arithmetic.

These checks establish finite regression evidence, not general
proofs and not a claim that every sentence in the draft is verified.

## Original figures

Created states-and-paths.svg, arc-consistency.svg, manhattan.svg,
and local-landscape.svg from original geometric layouts.
Rendered a contact sheet using Chromium. Adjusted two labels to
avoid overlap after inspection. All have SVG title/description
metadata and reader-facing alternative text at insertion sites.

## Integration and final review

Pending while chapter drafting continues. See final entries below.

## Recovery integration, 2026-10-22 Pacific

- Completed engineering chapter with original courier planning
  and two-machine scheduling examples and schedule.svg.
- Checked all six existing SVG figures in Chromium contact
  sheet; no overlaps or clipped labels observed.
- Figures in completed chapters link to SVG originals so
  readers can enlarge them independently.
- check_examples.py passed SAT equivalence/unsatisfiability,
  exact AC-3 queue trace, coloring repairs, partition table,
  annealing/restart calculations, real/relaxed courier BFS,
  and enumeration of integer schedules through horizon 7.
- check_extensions.py passed bidirectional Dijkstra on all
  4,096 directed three-state graphs with absent/0/1/3 edges,
  and RBFS on 9,477 positive-cost graph/heuristic cases.
- General algorithm checks rerun successfully without edits.

All are finite regression evidence, not proofs of every claim.

## Final integration and review — 2026-10-22 Pacific

This entry supersedes the historical pending-integration
statements above. The first instructor-review draft campaign
is complete; see final-validation.md for the full record.

- Confirmed all ten chapter files and seven original SVGs.
  Reused saved chapters; no recovery archive was reapplied.
- Independent reviewers read Weeks 1–5 and Weeks 6–10 with
  notation, source-level figure data, guarantees, traces,
  pseudocode, and transitions. Neither found a must-fix
  defect. Detailed notes are final-review-early.md and
  final-review-late.md.
- Root clarified the reachable-goal premise in weighted A*
  and initial distance/bound values in bidirectional search.
  Added the verified edition/year to the AIMA citation.
- Reviewed source/provenance consistency and remaining
  citation metadata. Saved publisher deposited Crossref
  metadata for the SAT and annealing references. Retained
  full-text access limits; no adaptation credits invented.
- Reran all three finite-model suites successfully, with
  the same case counts recorded above. They are regression
  evidence, not general proofs.
- Built mdBook 0.5.2 and passed the source/link check:
  17 HTML pages, 513 internal links, no errors or warnings.
- Expanded the browser tool to all reader-facing pages and
  content screenshots plus a seven-figure sheet. All 42
  page/view combinations pass, including narrow and 200%
  text views, without body overflow or broken images.
- Manually inspected all seven figures at legible size,
  including alpha-beta, their narrow/enlarged-text contexts,
  and representative prose, tables, and pseudocode. No
  label overlap or clipping observed. Narrow inline figure
  labels are small; SVG links support enlargement. Wide
  pseudocode scrolls within its container.
- Reconciled STATUS, README, the handoff, and source notes.
  Weekly word counts are about 2,100–2,500; no padding added.

Instructor review of teaching choices and pacing remains.
Optional cardinal-utility and sampling-policy explanations
from the late review can be considered at that stage; the
current text already qualifies both issues. No exercises,
commits, pushes, or changes outside book/ were made.

## Instructor revision — 2026-10-27 Pacific

Bart's BOOK-NOTES.md covers the introduction and Week 1.
The follow-up discussion authorized their rewrite and
explicitly deferred the historical claim about early AI,
hardware optimism, and NP-completeness. That claim and the
related historical quotations were not incorporated.

Changes:

- Expanded the introduction's account of the purpose and
  philosophy of search. Made authorship explicit: written
  by ChatGPT, with guidance and review by Bart Massey.
  Reconciled book.toml, attribution, and license credit.
- Rewrote Week 1 around exploring possibilities, with small
  coloring, partitioning, and routing examples. Partial
  assignments and complete candidate repair now enter before
  the action-sequence model.
- Connected state-space growth, the practical resource knee,
  NP-hard families, and solvable instances. Distinguished
  search depth from encoded input size and retained the
  qualifications on complexity claims.
- Separated objective value, path cost, and search effort.
  Generalized the notation reference's C*, U, and bound
  explanation accordingly. Kept path-specific g, h, and c.
- Added original search-growth.svg with a one-million-node
  budget and uniform branching factors four and two.
  checks/render_growth.py regenerates it with matplotlib.
- Preserved the prior introduction and Week 1 in revisions/.
  Left BOOK-NOTES.md and Weeks 2–10 unchanged.
- Corrected the status records to distinguish a complete
  first draft from ongoing book authoring and revision.

Independent review in review-2026-10-27-week1.md found no
must-fix issue in the prose or mathematics. Root adopted
its local-search cycling wording and objective-value
notation suggestions. The suggested generality caveat
about easy problem families was not added, following Bart's
explicit preference to keep NP-hard problems central.

Validation completed so far:

- mdbook build succeeds.
- check_book.py passes: 17 pages, 521 internal links, no
  errors or warnings; revised Week 1 has 3,309 source words.
- check_examples.py passes, including new finite coloring
  and partition checks, integer-layer node totals, rounded
  times, and both figure budget thresholds.
- The existing general algorithm and extension suites were
  not rerun: their code and relevant later algorithms did
  not change. Their earlier results remain historical.

Rendered review caught a clipped vertical axis label in the
first growth figure. The plot margin and SVG bounding box
were corrected before the final browser run. Chromium's
initial startup exceeded the old five-second allowance;
the script now allows thirty seconds and preserves startup
diagnostics. A separate retry encountered a concurrent
rebuild by the existing mdBook server; the final run was
started after the source tree stabilized.

Final rendered result: all 42 browser/view combinations pass,
with no document overflow or broken images. The final report
is browser-latest.json; screenshots are temporary under
/tmp/search-book-browser-iVzjzl and can be regenerated.

Root visually inspected the new figure in desktop, narrow,
and 200% text contexts, plus the revised introduction and
Week 1 openings. Centered images in course.css after the
200% view exposed overlap between the growth axis label and
the previous-chapter navigation arrow. The final image has
complete labels clear of those controls. Also spot-checked
the existing reopening figure at 200% text after centering.
Narrow figures link to full-size SVGs and the wide growth
table scrolls inside its own container.

The revised introduction and Week 1 are ready for Bart's
next read. Weeks 2–10 remain first drafts awaiting manual
review and resulting revisions. No exercises, commits,
pushes, or changes to BOOK-NOTES.md were made.

## Joint authorship and reserved Epilogue — 2026-10-27

At Bart's direction, the authors are now ChatGPT and Bart
Massey. Their names appear together under the opening book
title and in mdBook metadata. Removed the interstitial
role-based credit and the contribution narrative from the
attribution page. Updated reuse credit, README, brief,
status, and handoff to agree with the joint credit. This
supersedes the earlier role-based attribution decision.

Added an unnumbered closing Epilogue after the reference
material, with a reserved History and authorship section.
No history or contribution discussion was drafted there yet.

Build and source/link check pass: 18 HTML pages, 548 internal
links, no errors or warnings. Browser coverage now includes
the Epilogue. No chapter algorithms or examples changed.

All 45 browser/view checks pass after the joint-authorship
and Epilogue changes. Visually inspected the opening title
and author block and the closing Epilogue. It appears as an
unnumbered final section. Current screenshots are temporary
under /tmp/search-book-browser-PPcaFl; browser-latest.json
records the run.

## Review through Week 2 — 2026-10-27 Pacific

Applied the updated BOOK-NOTES.md and Bart's clarifications.
The notes themselves are preserved unchanged by the agent.

- Added original diagrams for graph coloring, number
  partitioning, and pathfinding. Reused the coloring graph
  explicitly as its CSP constraint graph. Related map
  coloring to graph coloring once, then used graph terms.
- Explained problems as collections of parameter
  instantiations, instances as particular parameter choices,
  and classes as collections of problems with a stated
  property. Deferred full formal descriptions to an
  algorithms textbook; did not identify the problem with
  its yes-instance language.
- Made n's meaning explicit, introduced nodes through
  candidate records, and emphasized machine-independent
  counts with the stated polynomial-per-node assumption.
  Changed the growth axis to Total nodes examined.
  Removed unintroduced makespan and tile-puzzle examples
  from Week 1 and named problems at example re-entry.
- Rewrote Week 2 with concrete variables/values first,
  a CNF refresher, named Boolean variables, finite quantified
  shorthand, explicit grounded expansions, and the two
  directions of encoding correctness.
- Removed AC-3 and its unused figure from the current book,
  rather than moving them to Week 10. Retained forward
  checking, soundness versus completeness, and unit
  propagation within complete SAT search. Active checks
  now test forward checking rather than the retired AC-3
  implementation; older evidence stays in historical notes.
- Named most-constrained-first/MRV and least-constraining-
  first/LCV, with their fail-first and preserve-flexibility
  motivations qualified as heuristic intentions.
- Added Tsang and Crawford–Auton readings to Week 2 and a
  short WalkSAT treatment/reading to Week 6. Chapter 2
  remains the main SAT foundation; local SAT repair returns
  in Week 6. The earlier historical-hardware claim is still
  omitted.
- Aligned all weekly contents labels with chapter titles
  and added a regression check for their agreement.

Independent review in review-2026-10-27-chapter2.md checked
conceptual clarity, grounding, examples, figures, and counts.
Root corrected the Crawford–Auton page range to 21–27 and
adopted the clarity suggestions for node records, local n
meanings, and one explicitly grounded edge/color clause.

Completed validation:

- mdBook build passes; source/link check passes 18 pages and
  558 internal links with no errors. Week 1 has 3,880 words,
  generating one advisory length warning. The longer chapter
  is intentional under the accepted clarity-first scope.
  Week 2 has 2,810 words; Week 6 has 2,503.
- Algorithm suite: 25,792 path/heuristic cases; 110,592 binary
  CSP/partial-assignment cases for forward-check preservation;
  6,561 game trees; 5,184 partition deltas. All pass.
- Worked examples: 8,768 grounded SAT assignments, exact
  forward-check domains, unit/repair SAT example, coloring,
  partitioning, stochastic, courier, and schedule cases pass.
  The named four-vertex, three-color graph gives 12 Boolean
  variables, 28 clauses, and 12 models/colorings.
- Extension checks pass: 4,096 bidirectional graphs and
  9,477 RBFS graph/heuristic cases.
- All 45 browser/view checks pass: desktop, 390px narrow,
  and 200% text for fifteen reader-facing pages. Ten SVG
  figures render with no broken images. Added screenshots
  of quantified formulas and a navigation-overlap check.
- Visually inspected all three new introductory diagrams,
  graph-as-constraint-graph use, and grounded formulas in
  narrow/enlarged views. Corrected one missing subpath
  arrowhead by drawing the pathfinding edges separately.
  Reserved desktop content gutters after enlarged-text
  inspection exposed navigation arrows over formula text.
  Final screenshots: /tmp/search-book-browser-HSwMBU;
  browser-latest.json records the reproducible run.

Finite checks are regression evidence, not general proofs.
Weeks 1–2 are ready for Bart's next read. Other weeks remain
first drafts awaiting full manual review. The user authorized
committing this revision and all current notes; no push is
requested or performed.
