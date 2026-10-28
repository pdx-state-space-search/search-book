# Recovery review and pending integration

Historical checkpoint. The recovery and pending tasks below
were completed; see final-validation.md for the final review.

2026-10-22 Pacific. This note concerns the recovered first draft.

## State on disk

Root read back complete chapters 01,02,06,07 and partial 08.
Root completed 08 and added schedule.svg before disconnection.
Algorithm checks, worked-example checks and extension checks passed.
Six then-existing SVGs were visually inspected in Chromium.
Figures in completed chapters link to full-size SVG originals.

## New reviewed text

Recovered chapters 03,04,05,09,10 are original explanations,
approximately 2,100–2,400 words each by the source-check counter.
They contain no exercises, implementation-language listings,
unconfigured LaTeX or unresolved placeholders.
They use the accepted chapter sequence and existing notation.

Root corrected these draft problems before checkpointing:
- Systematic search can use heuristic ordering; coverage is the
  relevant distinction.
- Goal-on-removal BFS can generate the next layer; distinguish its
  O(b^(d+1)) bound from goal-on-generation O(b^d).
- The DFS example route has three edges; the BFS route has two.
- IDDFS's constant-factor regular-tree comparison assumes b>1;
  a chain gives quadratic regeneration.
- Removed an unverified/misattributed Korf thesis reference.
- Replaced mutable predecessor ambiguity with immutable path
  entries in the best-first pseudocode.
- Corrected chapter-order transitions and removed raw LaTeX and
  redundant ASCII puzzle boards.
- Memory depth D means maximum depth actually reached; it need
  not be the shallowest solution depth.
- Initialized the IDA* path and copied a successful path before
  restoration; retained RBFS infinity-exhaustion handling.
- Made MAX a fixed player throughout game search; qualified
  transposition-table horizon compatibility and fingerprint risk.
- Corrected weighted-A* arithmetic: (g,h)=(2,8),(8,3) gives
  ordinary keys10,11 and weight-two keys18,14.
- Anytime lower bound is min(U,min eligible frontier(g+h)),
  including the incumbent and pending/reopened work.
- At MIN, fixed-MAX UCT explores by maximizing -Q+bonus,
  not by minimizing Q+bonus.
- Made the bidirectional joining and stopping assumptions explicit.

An independent agent checked supplied excerpts for AC-3,
coloring deltas, partition neighbors, annealing/restart math,
finite-domain backtracking, the courier relaxation, and the
schedule. It found no substantive error. Its wording caveats
(singleton AC-3 domains; absolute-imbalance E) were already
explicit. It did not review the full chapters or SAT encoding.
SAT equivalence and the AC-3 trace were separately enumerated
by root in check_examples.py.

## Primary reference checks

Metadata/relevance checked through publisher or author pages:
- Dijkstra1959, DOI10.1007/BF01386390.
- Korf1985 iterative deepening, author bibliography and cited DOI
  10.1016/0004-3702(85)90084-0.
- Dechter/Pearl1985, DOI10.1145/3828.3830.
- Korf/Felner2002, DOI10.1016/S0004-3702(01)00092-3.
- Korf1993 RBFS, DOI10.1016/0004-3702(93)90045-D.
- Shannon1950, DOI10.1080/14786445008521796.
- Knuth/Moore1975, DOI10.1016/0004-3702(75)90019-3.
- Hansen/Zhou2007, DOI10.1613/jair.2096; author-hosted arXiv
  record1110.2737 confirms journal year despite2011 posting.
- Kocsis/Szepesvari2006, DOI10.1007/11871842_29, Springer.
- Okumura LaCAM2023, AAAI proceedings26377.
- Okumura LaCAM*2023, IJCAI proceedings2023/28. Publisher
  abstract explicitly conditions eventual optimality on
  accumulated transition costs.

Hart/Nilsson/Raphael1968 DOI10.1109/TSSC.1968.300136 is a
bibliographic citation. IEEE automated access reached a
robot-verification page; retain this access limitation rather
than claiming a full primary-paper review.
No cited paper was comprehensively audited in this campaign.
The new chapter arguments and examples were written independently;
no source prose, tables, pseudocode listings, or figures adapted.
No actual Wikipedia adaptation requires a revision attribution.

## Pending after reconnect

Read exact JSON archive on the recovery Page and write files at
their paths relative to /home/bart/work/search/book.
Its src/figures/alpha-beta.svg is an original new figure.
Do not overwrite saved chapters1,2,6,7,8 with stale copies.

Run mdbook build and checks/check_book.py.
Run checks/check_browser.cjs and visually inspect new figure
and representative pages, including narrow and large-text views.
Extend worked-example checks for new traces if needed.
Update STATUS, README and source/review logs from actual results.
No completed full-book build or browser check is claimed yet.
Do not commit or push.
