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

## Chapter authoring standard — 2026-10-27 Pacific

Paused chapter revision at Bart's request to create the
repository-local search-book-authoring skill. Its editorial
guide captures reader prerequisites, explanation before
notation, example continuity, precise guarantees, and the
existing draft's worked traces and practical cost accounting.
Annotated repairs illustrate those choices without imposing
a fixed chapter template. BRIEF retains topic allocation;
BOOK-NOTES remains the instructor's working feedback.
AGENTS.md routes future chapter work to the skill.

Two independent trials used isolated copies of the skill,
brief, and prior chapters without inherited discussion:

- A 580-word BFS sample restored the Week 1 road instance,
  explained queue records, traced the search, and separated
  minimum transitions from weighted cost. It stated duplicate
  policy, finite/infinite assumptions, and memory costs.
- A review-only trial identified undefined size, unsupported
  runtime/optimality claims, a bound mistaken for a certificate,
  missing example context, and omitted/unintroduced topics.
  It correctly resolved stale AC-3 feedback using BRIEF.

Hash comparisons confirmed supplied trial files and all real
book sources unchanged; only the permitted sample was added
inside its fixture. Temporary fixtures were removed. Skill
frontmatter validation and local-link checks pass. These are
small behavioral trials, not proof of consistent future prose.
The final guide also incorporates Bart's latest distinction
between a general problem and our particular instance.
No book rebuild was needed for these authoring instructions.
No commit or push was requested for this task.

## Follow-up notes and remaining-chapter review — 2026-10-27

Applied the latest instructor notes to Weeks 1–2. Clarified
that NP-completeness does not assume separation from P;
identified specific worked instances when returning to them;
explained linear-time, linear-size Tseitin encoding with
auxiliary variables and satisfiability/projection guarantees;
and distinguished compact representation from easy solving.
Replaced literal underscore subscripts in the first quantified
encoding with rendered subscripts, a separated quantifier,
and a wrapping formula block. Further-reading advice now has
an explicit Reading suggestion label separate from description.
BOOK-NOTES.md was not edited by the agent.

Added a 29-entry bibliography collecting every existing weekly
reading work plus the new Markov/CNF sources. Added concept
citations to Weeks 1–2 and linked the bibliography from the
contents and reading guide. New source checks and access limits
are recorded in verified-sources.md. Updated the authoring
skill/guide to require separate bibliography, point-of-use
citations, and clearly marked reading advice.

Three independent reviewers read all of Weeks 3–10 with the
updated skill, inspected actual validation coverage, checked
suspect claims, and wrote detailed line-anchored reports.
Root read the chapters and reconciled findings in
review-2026-10-27-remaining-chapters.md. There is one definite
technical specification defect: Week 9's solved-game-value
exception can change its exact fixed-horizon function.
Other high-priority work concerns incomplete operational
explanations, missing concrete traces, source support, and
narrow-screen figure legibility. Weeks 3–10 remain unchanged;
review completion is not chapter revision completion.

Independent follow-up review of root's Weeks 1–2/bibliography
changes caught a missing Shannon entry and an ambiguous return
from the two-color triangle to the four-vertex graph. Both
were corrected. NP, Markov, Tseitin/projection, and finite
quantification changes received no technical findings.

Validation: mdBook build; source/link check (19 HTML pages,
628 internal links, no errors); all worked-example checks;
skill frontmatter and local-reference checks. Week 1's 4,026
words give one intentional advisory; Week 2 has 3,196.
Reviewers also reran the algorithm/extension suites and
performed the additional finite calculations documented in
their reports. Those do not prove the untested/general claims.
The browser check now includes the bibliography: 48 views
pass. Formula and bibliography screenshots were manually
inspected at narrow and enlarged text sizes; the former was
compared with its old rendering. Temporary PDF-reading tools
were removed. No commit or push was requested or performed.

## Week 1 outline-based rewrite — 2026-10-28 Pacific

Rewrote Week 1 after Bart accepted both outline levels and
moved Problems, Instances, and Models to the start of Part II.
It remains one weekly chapter with the same title and file:
Part I has examples, growth, and emergence; Part II has models,
states/transitions, records/paths, work accounting, and
criteria for guarantees. Existing examples, all five figures,
and substantial prose were reused. Node counts and the
node-budget figure now follow the explanation of records.
Removed repeated hardware/budget explanation and kept the
formal problem treatment introductory. One Further reading
section serves the chapter, using the shared bibliography.

Added a source-supported emergence discussion with an original
C-blue/B-green repair trace (four conflicts to one to zero)
and a separately identified two-vertex synchronous flip cycle.
Added Mitchell's bibliography entry and optional annotated
reading; source-access details are in verified-sources.md.
The pre-rewrite chapter is preserved in
revisions/01-models-before-outline-2026-10-28.md because earlier
uncommitted source revisions also needed preservation.
BOOK-NOTES.md and other chapter sources were left untouched.

Independent review in review-2026-10-28-week1-rewrite.md read
the entire chapter for organization, prerequisites, meaning,
examples, guarantees, and source support. It caught a reversed
road-model example, corrected to treating a closed road as
usable. No other substantive defects were found. Root and
reviewer independently checked the new local choices, 4→1→0
conflict counts, final pictured coloring, and period-two cycle.
The existing example suite passes, including the unchanged
assignment, partition, growth, SAT, and later examples.
New finite traces were checked ad hoc; they are not yet part
of the persistent example suite and do not establish general
repair guarantees.

mdBook builds; the source/link check passes 19 HTML pages and
652 internal links. Week 1 has 4,626 source words, producing
one intentional length advisory. All 48 browser/view checks
pass. Extended screenshot capture to Part headings and
manually inspected the part/section/subsection hierarchy,
new trace, and retained figures in desktop, narrow, and
200% text views. Added heading scroll margins after inspection
showed a Part heading hidden behind the fixed menu on anchor
navigation at enlarged text. The recheck shows it fully.
Wide tables remain horizontally scrollable; figures retain
full-size links, now explicitly advertised in their captions.
Final screenshots: /tmp/search-book-browser-ridlZL/.

Updated the accepted outline, brief, status, README, and
handoff. Other chapter review findings remain pending their
own revision tasks. No commit or push was requested or made.

## DFS pseudocode formatting preview — 2026-10-29 Pacific

Reformatted only Week 3's recursive DFS pseudocode for Bart's
review. The algorithm now uses proportional serif typography,
italic variables, emphasized control words, left-arrow
assignment, numbered statements on separate lines, and a
parameter/result header. Indentation carries control flow;
the steps scroll horizontally when needed at narrow widths.
The semantics remain the same, including path-local cycle
checking, copying a successful path, and restoring the mutable
path before propagating the result. The initial call and path
precondition are explicit. Other pseudocode remains unchanged.

The presentation uses scoped HTML/CSS with a focusable scroll
region and the stable dfs-pseudocode anchor. Added algorithm
blocks to the browser check's teaching-content captures.
mdBook build and the 19-page/652-link check pass. All 48
browser/view checks pass. Manually inspected the DFS block
at desktop, 390px narrow, and 200% text: serif text, arrows,
header, line numbering, and indentation render as intended.
Screenshots: /tmp/search-book-browser-Kbpqgx/.
This is formatting verification, not a new algorithm review.
The broader Week 3 revision and current instructor notes
remain pending. No commit or push was requested or made.

## DFS header refinement — 2026-10-29 Pacific

Applied Bart's header correction to the DFS preview: the
algorithm title is uppercase on its own line, followed by a
function declaration with brief em-dash parameter descriptions.
Parameters wrap together at argument boundaries and align on
separate lines when space is limited. Kept a concise Result
line and moved longer prerequisites to surrounding prose.
The algorithm statements are byte-for-byte unchanged.
Recorded the header convention in the skill, editorial guide,
and brief. Skill validation and mdBook build pass; the link
check has no errors. All 48 browser views pass. Manually
inspected desktop, narrow, and enlarged header layouts:
/tmp/search-book-browser-onJsI3/.
No commit or push was requested or made.

## Whole-draft pseudocode formatting — 2026-10-29 Pacific

Bart accepted the concise task-sentence header, superseding
this log's earlier title/declaration/Result layout. Applied
the accepted convention to all six remaining fenced listings
in Weeks 3–5: BFS, iterative deepening, branch-and-bound,
best-first search, IDA*, and RBFS. IDA*'s driver and recursive
helper now have separate headers. The draft has eight typeset
algorithm blocks including the unchanged DFS preview.

Each block uses the shared proportional typography, italic
variables, left-arrow assignments, emphasized control words,
numbered statements, and explicit indentation. Split inline
condition/actions and extend/recurse/restore sequences onto
separate lines. Moved branch-and-bound's shared initial values
to adjoining prose. Compared all conversions with the prior
listings to preserve their logic, tests, returned values, and
restoration order. This is a presentation pass; the broader
technical/editorial revision findings remain pending.

mdBook build and the 19-page/652-link check pass. All 48
browser views pass. Inspected every new block at desktop,
390px narrow, and 200% text. Headers wrap; long statements
remain on one line in horizontally scrollable bodies.
Screenshots: /tmp/search-book-browser-TVbk1n/.
No fenced or indented listings remain in the draft. No commit
or push was requested or made.

## Grouped chapter outlines — 2026-11-11 Pacific

Reviewed OUTLINE.md for ordering, prerequisite gaps,
coverage, repeated material, and reading load. Independent
reviews cover Weeks 2–4, 5–7, and 8–10 in the three
outline-review-2026-11-11-weeks*.md notes. Root reconciled
those recommendations with the current chapters, instructor
notes, brief, and earlier review findings.

Following Bart's clarification, inserted sections between
chapters and the existing bottom-level topic subsections.
All 54 previous topics remain exactly once. Restored the
existing Week 10 draft's short Guidance and proof synthesis
as one additional peer topic. Added no finer topic level.

Key changes: CSP deductions before ordering heuristics;
landscapes before local repair; restart analysis grouped with
evaluation after the policies; game-value semantics before
alpha-beta and reuse; MAPF grouped with path search. Made
several missing explanatory bridges and example requirements
explicit within existing topics. Flagged the complete versus
systematic vocabulary conflict without changing definitions
in the chapter sources. The outline remains a proposal for
instructor review, not a completed prose rewrite.

Checked exact topic-title coverage, hierarchy, local links,
line lengths, and whitespace. Source and BOOK-NOTES.md hashes
match their pre-review values. No book build or algorithm
suite was needed because only editorial planning documents
changed. No commit or push was requested or made.

## Terminology and literature coverage — 2026-11-11 Pacific

Applied Bart's explicit definitions of complete (eventually
examines every state) and systematic (examines each state at
most once) in Weeks 1–5, the introduction, notation, and
necessary later cross-references. Renamed Week 3 and its
contents entry. Distinguished actual state examination after
record filtering from generation/ranking overhead, continued
traversal from early stopping, and sound pruning from literal
examination. Preserved all pseudocode blocks byte-for-byte.
BOOK-NOTES.md is unchanged.

Independent review in terminology-alignment-2026-11-11.md
identified three wording issues; all were corrected: narrow
examination to selected processing, call a stale record
removed rather than examined, and use literal all-state
coverage in the learned-ordering discussion. No algorithm
behavior changed or new algorithm suite was needed.

Expanded OUTLINE.md with anytime search beginning at
branch-and-bound, a fuller admissibility/useful-overestimate
comparison, and constructions for inadmissible guidance.
Week 7 handles interruption and contracts; Week 10 handles
certificates. These are plans for fuller authoring, not claims
that those new treatments have been written in the chapters.

Primary-source research is recorded in
anytime-inadmissible-sources-2026-11-11.md and
literature-topic-gaps-2026-11-11.md. The latter recommends
beam search, a learned-conflict trace, and worked symmetry;
these remain proposals. Source checks were selected passages,
not full-paper audits. No new source prose was adapted.

mdBook builds; 19 pages and 654 internal links pass. All 48
browser views pass, and the changed Week 3 opening was
visually checked. Week 1 retains its intentional length
advisory. Outline links resolve. Screenshots:
/tmp/search-book-browser-IbH2k3/.
No commit or push was requested or made.

## Four approved outline additions — 2026-11-11 Pacific

Added learning from failure to Week 2, limited discrepancy
search to Week 3, beam search to Week 5, and symmetry reduction
to Week 8. Each is a peer topic at the existing bottom level.
Week 3 now separates bounded exploration from optimization
and anytime answers so the added material has a coherent home.
The new descriptions specify examples, guarantees, and limits;
full chapter prose remains subsequent authoring work.

Recorded Bart's CIRL connection in the outline and brief for
reading choices and the eventual Epilogue. Checked Ginsberg's
Dynamic Backtracking title page and introduction, supplying
a CIRL reading connection distinct from the GRASP reference.
Updated status/handoff approval language. Corrected a stale
complete-SAT label in the outline to match the settled terms.

Validated nine chapter groups, 62 peer topics, section-local
numbering, hierarchy, and local links. No chapter sources or
instructor notes changed; no build was needed for this outline
and editorial-record update. No commit or push was requested.
