# Continue the State Space Search course book

## Current authoring state — 2026-10-27 Pacific

Manual instructor review and substantive revision are in
progress. Read STATUS.md, BOOK-NOTES.md, and the newest
research/review-log.md entry first. The introduction and
Week 1 were rewritten around the general search philosophy,
NP-hard instances, and solution quality versus search effort.
The authors are ChatGPT and Bart Massey. A closing Epilogue
is reserved for history and authorship discussion. The
early-AI/hardware historical claim is deferred.
Weeks 2–10 remain first drafts awaiting manual review.
The completion statements below describe the first-draft
checkpoint, not completion of all book authoring.

## Campaign completed — 2026-10-22 Pacific

The first instructor-review draft is complete. Start with
STATUS.md and research/final-validation.md for current results.
Open _build/index.html to read the built book. No further
recovery, redrafting, or migration is needed. The instructions
below preserve the historical handoff and its constraints;
their pending-work lists are superseded by the final record.
Future work should follow instructor feedback. Do not add
exercises, commit, or push without new user instructions.

Work in /home/bart/work/search. The book project is book/.
Complete the existing campaign autonomously. Reuse the saved
chapters and verification work; do not restart the book.

## First read

Read applicable AGENTS.md instructions, then:

- book/BRIEF.md
- book/STATUS.md
- book/research/review-log.md
- book/research/recovery-review.md
- book/research/handoff-validation.md
- book/src/SUMMARY.md
- book/src/notation.md

The handoff-validation note is the latest validation checkpoint.
Inspect actual files before relying on older checklists.
The syllabus is front-matter/syllabus.md.

Do not read student submissions or grading records. Do not
recursively inspect prev/ for material. Do not modify the
syllabus or archived course materials. Do not commit or push.

## Goal and accepted editorial decisions

Produce a coherent, technically reviewed first draft of a
ten-week mdBook for Bart Massey's PSU CS 410/510 course.

- mdBook is the only delivery format for this campaign.
- Keep weekly reading short, preferably below ten conventional
  pages. HTML is reflowable, so do not claim exact pagination.
  The original target was roughly 2,500–3,500 words per week;
  recovered chapters are often around 2,100–2,400. Do not pad
  sound, self-contained explanations merely to hit a count.
- Assume undergraduate algorithms, systems, and imperative
  programming experience, but no prior AI course.
- Keep the text language-neutral. Use concise, precise
  imperative pseudocode where it helps, not implementation
  source listings.
- Do not choose or draft exercises or instructor solutions.
- Use worked traces, explicit assumptions, short correctness
  arguments, and original figures.
- Preserve CSP/SAT, systematic and heuristic search, local and
  stochastic search, engineering, and introductory games.
  Planning and scheduling are compact applications.
- Provide light annotated further reading. Core explanations
  should not depend on purchasing a textbook.

The ten chapters are:

1. Models, states, problems, growth, and complexity.
2. Constraints, SAT, backtracking, and propagation.
3. DFS, BFS, depth limits, iterative deepening, branch-and-bound.
4. UCS, greedy best-first, A*, duplicates, and reopening.
5. Heuristic construction, abstraction, IDA*, and RBFS.
6. Local search, repair, neighborhoods, and landscapes.
7. Stochastic optimization, hybrids, and evaluation.
8. Representation, memory, parallelism, planning, scheduling.
9. Minimax, alpha-beta, evaluation, and transpositions.
10. Weighted/anytime and bidirectional search, MCTS, and MAPF.

## Current checkpoint

All ten chapter files are now present in book/src/.

Chapters 01,02,06,07 were saved before the interruptions.
Chapter 08 was completed by the integrating editor, including
a courier planning example, schedule, and original diagram.

The five missing chapters 03,04,05,09,10 have now been restored
from a separately verified recovery archive. Their text was
read back after restoration. The original alpha-beta figure
was restored too. Do not regenerate these chapters.

Recovered files:

- src/03-systematic.md
- src/04-best-first.md
- src/05-heuristics.md
- src/09-adversarial.md
- src/10-frontiers.md
- src/figures/alpha-beta.svg
- research/recovery-review.md

The standalone archive is book/research/recovery-archive.json.
Its files entries have name and text fields. Each name is a
path relative to book/. Before any recovery write, compare an
existing file and preserve newer or differing work. Reject
paths escaping the book directory.

The private backup is also available at:
https://chatgpt.com/space/page_7c387432f1748191a8a9a29e6d4b7451

Use its Exact Markdown archive for recovery, not its readable
preview. The local JSON copy removes any need for Codex to
access that private Page.

## Work to finish

1. Inventory the current project and reconcile this handoff,
   STATUS.md, and the newer recovery review.
2. Build the complete mdBook and run the source/link checks.
3. Review notation, chapter transitions, guarantees, traces,
   references, and reading load across all ten chapters.
4. Inspect rendered pages and all figures, including narrow
   screens and enlarged text. Figures link to full-size SVGs.
5. Reconcile provenance and reference notes. Update the
   reader-facing attribution page if any actual adaptation
   occurs.
6. Update STATUS.md, README.md, and research/review-log.md
   with actual results and remaining issues.
7. Deliver the built book location and a concise review
   summary. Label it a first instructor-review draft.

Some earlier logs are stale and still say chapters are
missing. Do not treat a checklist as evidence against the
files you have actually inspected.

## Build and verification

mdBook 0.5.2 was installed and ran successfully. The project
uses its built-in HTML renderer, local CSS and SVGs, with no
MathJax or external diagram preprocessor.

From /home/bart/work/search/book:

```sh
mdbook build
python3 checks/check_algorithms.py
python3 checks/check_examples.py
python3 checks/check_extensions.py
python3 checks/check_book.py
node checks/check_browser.cjs
```

Run build before the source/generated-link check. Inspect
each script before assuming its name establishes coverage.

Previous successful checks, before the final restoration:

- 25,792 small path-search/heuristic cases for A*, weighted
  A*, and the positive-cost IDA* subset.
- 4,096 binary constraint networks.
- 6,561 small zero-sum game trees, alpha-beta versus minimax.
- 5,184 partition move-delta cases.
- Exact worked-example checks for SAT, AC-3, coloring,
  partitioning, annealing, restarts, courier, and scheduling.
- 4,096 directed graphs for bidirectional Dijkstra.
- 9,477 positive-cost graph/heuristic cases for RBFS.

These are finite regression evidence, not general proofs.
At handoff, the full ten-chapter HTML build passed.
check_book.py passed with 17 HTML pages, 513 checked internal
links, no errors and no warnings. The automated browser
check passed 30 chapter/view combinations (desktop, narrow,
and 200% text), with no overflow or broken images.
See research/handoff-validation.md for the exact checkpoint.

The browser script uses Chromium and node-ws and writes
screenshots to a temporary directory. Existing diagrams were
visually checked; the newly restored alpha-beta figure still
needs final rendered inspection.

## Technical details to protect during review

The recovery-review note records corrections already made.
Do not reintroduce these errors:

- Greedy best-first orders by h, UCS by g, A* by g+h.
- Goal-on-removal BFS can generate depth d+1 before finding
  a goal at depth d; qualify the corresponding bounds.
- Equal positive costs are needed to equate shallowest paths
  with cheapest paths.
- Infinite-space termination needs more than positive costs;
  finite branching and a fixed positive cost floor are a
  useful sufficient condition.
- A* with inconsistent admissible h may need reopening.
  Strict best-g updates and stale-record handling matter.
- Cost-bounded searches can reach deeper than the shallowest
  goal; memory notation must say which depth is measured.
- IDA* checks its f threshold before accepting a goal.
  RBFS explicitly handles an infinite best bound.
- Maximum of admissible heuristics is safe; addition requires
  justified cost partitioning.
- An anytime global lower bound includes the incumbent:
  L=min(U,min eligible frontier(g+h)). Account for pending
  expansion and reopening work.
- Weighted search keys are not admissible certificates.
- Bidirectional stopping requires correct joins and minima.
- Game utilities use a fixed MAX perspective. Transposition
  bounds and horizons must be compatible.
- Fixed-MAX MCTS selects MAX children by Q+bonus and MIN
  children by -Q+bonus, maximizing in both cases. Backups
  retain the same reward perspective.
- Failed/time-limited stochastic runs must remain visible;
  independent seeds are not independent problem instances.

Extend checks where they materially test new claims. Avoid
tests that merely restate the implementation or word counts.

## Licensing and sources

Original text and figures are CC BY-SA 4.0.
No Wikipedia prose, tables, algorithm listings, or figures
have actually been incorporated so far. The previous
Wikipedia outline informed topic coverage only.

Khemani's publisher TOC informed coverage; no textbook prose
or figures were copied. Referenced works retain their own
licenses.

If you actually adapt Wikipedia material, record the article,
exact permanent revision, contributor-history link, license,
destination section, retrieval date, and description of edits
in research/source-log.md and the reader-facing attribution.
Do not invent revision IDs or credit unadapted articles.
Do not copy archived copyrighted textbook material.

Use primary sources for algorithmic claims and verify
bibliographic metadata. Record access limitations honestly;
a search result is not evidence of a full-paper review.

## Permissions and reliability

Saved config inspected on this machine on 2026-10-22:

```toml
default_permissions = "container-local"
approval_policy = { granular = { sandbox_approval = false, rules = false, mcp_elicitations = false, request_permissions = false, skill_approval = false } }

[permissions.container-local.filesystem]
":root" = "write"

[permissions.container-local.network]
enabled = true
```

This is broad configured filesystem/network access, with
approval requests disabled. It is not proof that the OS
sandbox is disabled or that every session uses those defaults.
Launch overrides and managed/session policies can differ.
Do not change permission settings merely because this
handoff contains a snapshot.

The standalone CLI reported version 0.163.0.
A config snapshot is not an independently observed active CLI
session: the visible Codex processes were app/exec servers,
not an interactive CLI with a verified permission display.
This Work session's shell tool failed before command execution
with a bwrap /proc mount permission error; direct Node-runtime
filesystem and child-process operations worked when connected.
Those are observations about different execution routes, not
proof that standalone CLI shell execution is broken.

Before lengthy unattended work, demonstrate read/write and
build access and test one subagent's file access. If an agent
cannot write, request its findings/text directly and integrate
from the parent. Do not leave calls hanging for minutes.

Save small checkpoints directly to disk, read them back,
and keep durable status notes. Agent messages and in-memory
tool state alone are not durable project checkpoints.
Do not regenerate completed text after an interruption.

Routine reversible editorial/build work is already authorized.
Resolve ordinary choices and proceed. Ask only for missing
information that truly blocks the task or actions outside the
authorized scope. Never claim a save, test, build, or review
that did not actually complete.
