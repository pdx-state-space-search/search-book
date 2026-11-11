# Anytime search and inadmissible guidance: source notes

Research date: 2026-11-11 Pacific.

Scope: primary-source research and teaching recommendations for
the ten-week book. Only this note was edited. No chapter,
outline, bibliography, commit, or push was authorized here.

The recommendations apply the repository's
[authoring skill](../.agents/skills/search-book-authoring/SKILL.md).
I read BRIEF.md, BOOK-NOTES.md, STATUS.md, OUTLINE.md, the
relevant chapters, notation, bibliography, and editorial guide.
The latest request to emphasize anytime search and the value of
inadmissible heuristics supersedes any narrower older framing.

## Strongest recommendations

1. Teach a heuristic first as information for choosing work.
   Admissibility is a useful additional property that licenses
   lower-bound reasoning. It is not the definition of useful
   heuristic information.
2. Make the benefit of inadmissible guidance concrete in Week 4,
   then give it a real construction example in Week 5. A warning
   that overestimation removes A*'s first-goal proof is necessary
   but insufficient: readers also need to understand why someone
   would deliberately accept overestimation.
3. Define anytime behavior explicitly in Week 7, as the new
   outline already proposes. A retained answer, the search's
   current candidate, and a quality certificate are different
   objects. More search need not improve the answer at every
   step, and no answer exists before first feasibility unless a
   valid fallback was supplied.
4. Use Hansen and Zhou's separation of ordering and bounding as
   Week 10's central connection. Their general construction
   explicitly permits an arbitrary inadmissible guidance
   heuristic alongside a separate admissible bound. Weighted
   A* is one special case, not the full motivation.
5. Keep a small primary reading set. Hansen–Zhou is already in
   the bibliography. Zilberstein and FF are the most valuable
   additions for the requested teaching changes. LAMA supplies
   a practical anytime application; ARA* and MHA* can remain
   optional connections rather than full new algorithms.

## What the current files already establish

- OUTLINE.md, Week 4, distinguishes promising work from safe
  pruning and separates admissibility from consistency.
  However, its main positive development still moves from
  greedy search to admissible A*. Add a positive account of
  unconstrained estimates alongside the first-goal caveat.
- OUTLINE.md, Week 5, states its purpose as constructing
  justified lower bounds. Its first part has the same narrow
  title. That framing leaves little room for estimating useful
  directions without a lower-bound claim. Broaden the purpose
  before adding examples so this is a planned teaching goal.
- src/04-best-first.md already says priorities need not be
  certificates. Its greedy example usefully shows that even
  admissibility and consistency do not make greedy search
  cost-optimal. The positive case for overestimation currently
  receives only a sentence and a link to Week 10.
- src/05-heuristics.md correctly distinguishes the exact relaxed
  optimum from an arbitrary relaxed solution. This is the best
  entry point for explaining why the latter can still be useful
  guidance. The present language emphasizes what it cannot
  certify without developing what it can accomplish.
- src/07-stochastic.md retains the best feasible candidate but
  does not explicitly define or name anytime behavior in its
  body, despite its title. OUTLINE.md's proposed opening repairs
  this. It should also make the connection to deterministic
  search so readers do not equate anytime with randomized.
- src/10-frontiers.md already has a careful certificate using
  the incumbent and the full eligible frontier. Preserve that
  care. Extend its aggressive-search sentence into a concrete
  illustration with separate guidance and bound values.
- src/bibliography.md contains Hansen–Zhou and Korf's complete
  anytime partitioning paper. It currently lacks Zilberstein,
  FF, LAMA, ARA*, and MHA*. This note does not add entries.

## Six selected primary sources

### 1. Hansen and Zhou: separate guidance from proof

Eric A. Hansen and Rong Zhou. “Anytime Heuristic Search.”
*Journal of Artificial Intelligence Research* 28, 267–297,
2007. [DOI](https://doi.org/10.1613/jair.2096),
[full paper](https://arxiv.org/pdf/1110.2737),
[record](https://arxiv.org/abs/1110.2737).
The arXiv posting is 2011; the journal article is 2007.

Selected passages, paraphrased:

- Section 1, p.268, allows an initial interval before a first
  answer exists when describing anytime search.
- Section 2.3, p.270, gives three changes: use inadmissible
  guidance, continue after finding a solution, and use separate
  admissible bounds with the incumbent for pruning and proof.
  The text says this is “not limited to weighted heuristic
  search.”
- Sections 2.3.1–2.3.2, pp.272–273, distinguish convergence from
  the changing upper/lower bounds. The stated termination proof
  is for weighted guidance under its explicit assumptions.

Teaching use: the strongest anchor for Week 10 and for avoiding
the false dichotomy between aggressive guidance and correctness.

Access: full 31-page PDF available; selected sections reviewed,
not every proof or experiment. The book's incumbent-capped
global bound is more explicit about the already-optimal case.

### 2. Zilberstein: what anytime means

Shlomo Zilberstein. “Using Anytime Algorithms in Intelligent
Systems.” *AI Magazine* 17(3), 73–83, Fall 1996.
[DOI](https://doi.org/10.1609/aimag.v17i3.1232),
[author PDF](http://anytime.cs.umass.edu/shlomo/papers/Zaimag96.pdf).

Selected passages, paraphrased:

- “Desired Properties,” p.74, distinguishes output quality from
  computation time and lists desirable properties. Retaining
  the best recognized result can make reported quality monotone
  even when the generating process is not.
- “Interruptible and Contract Algorithms,” p.77, calls both
  types anytime algorithms. An interruptible method can provide
  a result when stopped; a contract method needs the allocation
  beforehand and may provide nothing useful if stopped early.
- Performance profiles describe quality versus computation;
  empirical profiles and per-run certificates are different.

Teaching use: Week 7 needs a declared convention, preferably
“interruptible anytime optimization” for its retained-incumbent
interface, plus a brief contract distinction. Do not turn all
listed desirable properties into mandatory axioms.

Access: AAAI's article page blocked automated access; HTTPS on
the author host failed. The exact HTTP URL above returned the
complete 11-page PDF, inspected in memory. Printed pages
73–83 were verified; relevant sections were read.

### 3. Hoffmann and Nebel: useful relaxed plans without bounds

Jörg Hoffmann and Bernhard Nebel. “The FF Planning System:
Fast Plan Generation Through Heuristic Search.”
*Journal of Artificial Intelligence Research* 14, 253–302,
2001. [DOI](https://doi.org/10.1613/jair.855),
[full paper](https://arxiv.org/pdf/1106.0675),
[author page](https://fai.cs.uni-saarland.de/hoffmann/ff.html).
The arXiv posting is 2011, not the publication year.

Selected passages, paraphrased:

- Section 4, p.257, motivates extracting a relaxed plan cheaply
  rather than solving the relaxed optimization problem exactly.
- The same page gives a shared-precondition example: additive
  estimates total four although a three-action solution exists.
- Section 4.2, p.262, footnote 2, explicitly warns that the
  extracted relaxed solution need not be optimal, even with
  optimal action linearizations at individual layers.
- The abstract and evaluation describe successful practical
  planning with this guidance and additional search machinery.

Teaching use: Week 5's distinction between a relaxed optimum
and a relaxed answer becomes a positive design choice. The
latter can be informative while failing to supply a bound.
Do not attribute FF's whole performance to inadmissibility.

Access: complete 50-page paper available; targeted sections
reviewed. DOI metadata verified through the arXiv record;
direct DOI access failed in the web tool.

### 4. Richter and Westphal: finite-budget planning in practice

Silvia Richter and Matthias Westphal. “The LAMA Planner:
Guiding Cost-Based Anytime Planning with Landmarks.”
*Journal of Artificial Intelligence Research* 39, 127–177,
2010. [DOI](https://doi.org/10.1613/jair.2972),
[full paper](https://arxiv.org/pdf/1401.3839).
The arXiv posting is 2014; use 2010 for the journal article.

Selected passages, paraphrased:

- Section 3.3, pp.135–137, describes a greedy first search,
  followed by restarted weighted searches with declining
  weights, preserving the best plan across searches.
- Section 7, p.153, compares first and final solutions under a
  30-minute limit. Quality is actual plan cost regardless of
  whether the guiding heuristic incorporates costs.
- The abstract reports that cost awareness did not uniformly
  help; some domains benefited from ignoring costs in guidance.

Teaching use: a concrete application for Weeks 7–8 and a reminder
that guidance may estimate distance or ease of finding a plan
instead of precisely estimating its objective cost. Its
empirical results do not establish a universal winner or a
weighted-A* approximation bound for arbitrary guidance.

Access: full 51-page journal PDF and publisher metadata were
available; selected search and evaluation sections reviewed.

### 5. Likhachev, Gordon, and Thrun: bounded anytime search

Maxim Likhachev, Geoffrey J. Gordon, and Sebastian Thrun.
“ARA*: Anytime A* with Provable Bounds on Sub-Optimality.”
*Advances in Neural Information Processing Systems* 16.
[Official record](https://papers.nips.cc/paper_files/paper/2003/hash/ee8fe9093fbbb687bef15a38facc44d2-Abstract.html),
[paper](https://papers.nips.cc/paper_files/paper/2003/file/ee8fe9093fbbb687bef15a38facc44d2-Paper.pdf).
The official archive and BibTeX use 2003; author bibliographies
also cite the published proceedings as 2004. State the
convention consistently if adding it.

Selected passages, paraphrased:

- Sections 2.1–2.3 start with a consistent base heuristic,
  reduce its inflation factor, and reuse search work.
- Figure 3, PDF p.4, includes OPEN and INCONS in its quality
  calculation. Deferred improvements remain relevant to proof
  even when absent from the immediate expansion queue.

Teaching use: an optional Week 10 example of controlled
suboptimality and reuse. It supports the existing requirement
to account for pending improvements. Its particular algorithm
and assumptions matter; arbitrary reuse is not automatically
valid, and decreasing a weight alone is not a certificate.

Access: complete eight-page official paper and BibTeX read;
selected algorithm sections reviewed. No comprehensive theorem
or experiment audit was performed.

### 6. Aine et al.: arbitrary guidance with an anchor

Sandip Aine, Siddharth Swaminathan, Venkatraman Narayanan,
Victor Hwang, and Maxim Likhachev. “Multi-Heuristic A*.”
*The International Journal of Robotics Research* 35(1–3),
224–243, 2016.
[DOI](https://doi.org/10.1177/0278364915594029),
[author-hosted published PDF](https://www.cs.cmu.edu/~venkatrn/papers/ijrr16.pdf).
Published online August 21, 2015; the paginated issue is 2016.

Selected passages, paraphrased:

- Abstract and Section 3 combine one consistent anchor
  heuristic with multiple heuristics that may be arbitrarily
  inadmissible and inconsistent.
- Theorem 3, p.228, gives the independent-search variant's
  bound C≤w₁w₂C*. The scheduling and stopping rules constrain
  the aggressive searches using the anchor.
- Theorem 10, p.232, states the corresponding shared-search
  bound. These are claims about the specified algorithms.

Teaching use: a compact optional Week 10 example showing that
poorly bounded guidance can coexist with a guarantee. Learned
predictions can motivate this design pattern, but this paper
is not evidence that any particular learned model works well.

Access: publisher metadata and complete published PDF available;
selected definitions and theorem statements reviewed. An older
author draft is dated 2015 and has different pagination.

## Teaching distinctions to make explicit

The following is editorial synthesis and original explanation,
not copied source prose.

### Accuracy, optimism, consistency, and usefulness

Treat these as separate questions:

| Question | Meaning |
| --- | --- |
| Accuracy | How close is an estimate to its stated target? |
| Admissibility | Is it always at most the optimal remaining cost? |
| Consistency | Does it obey the edge-wise inequality? |
| Ordering value | Does the induced priority find useful answers? |
| Computational value | Does its benefit justify its time/memory? |

“Optimistic” is an intuition for a one-sided inequality, not
a claim of small error or an average statistical tendency.
An estimate can be admissible and extremely inaccurate.
Conversely, a numerically accurate estimate can overestimate
slightly and therefore be inadmissible. A heuristic called
inadmissible need only violate the bound somewhere; it need
not overestimate at every state.

Consistency is neither accuracy nor smoothness in a loose
statistical sense. Under the book's zero-at-goals convention,
the edge inequality implies admissibility along finite goal
paths. An admissible heuristic can still be inconsistent,
which is why reopening has a separate role.

Use an original tiny example before discussing learned models.
Suppose A and B are frontier states reached at equal cost 1.
Their only continuations are A→G costing 4 and B→G costing 10.
Consider these estimates:

| State | True remaining cost | Bound h | Estimate q |
| --- | ---: | ---: | ---: |
| A | 4 | 4 | 5 |
| B | 10 | 0 | 11 |
| G | 0 | 0 | 0 |

Here h is admissible but favors B under greedy ordering.
The estimate q overestimates at A and B but ranks their
continuations correctly. On A and B, h's mean absolute error
is 5 and q's is 1. Set h(start)=0 if a full graph is needed;
with the stated edges, h can also be consistent.

The example separates the properties; it is not evidence that
inadmissibility is generally faster. Exact A* with h still
returns the optimal cost 5. Greedy ordering by h can return
11, while greedy ordering by q returns 5 on this instance.

In practical design, relaxed-plan extraction, hand-built
penalties, estimates of remaining steps, and learned
predictions can all carry useful ordering information.
Their success must be measured for the target task and budget.
It is especially important to say what they estimate: solution
cost, number of remaining actions, and computational effort
are different targets.

### Anytime behavior is an output discipline

Week 7 should introduce an incumbent before the annealing
formula. State that the ongoing search may inspect infeasible
or worsening candidates while the returned record changes only
when a better feasible solution is found. This works for both
randomized and deterministic methods.

For minimization, retain U(t), the best feasible objective
found by time t. Once defined, U(t) is nonincreasing. It can
remain flat for a long interval. Neither an improvement rate
nor eventual optimality follows merely from maintaining it.

Distinguish four interfaces:

1. A one-shot solver returns one answer when it finishes.
2. An interruptible anytime solver retains an answer once
   feasibility has been reached and can report it on request.
3. A contract solver requires a time allocation in advance
   and need not have a useful earlier answer.
4. A certified anytime solver also reports a justified bound
   on how far the incumbent may be from optimal.

These categories can overlap; for example, an interruptible
solver can also accept a planned deadline. Running with a fixed
cutoff does not by itself make a solver a contract algorithm.
Conversely, merely terminating a search process at an arbitrary
time does not make its internal partial state a valid answer.

Do not promise hard real-time responsiveness. The reporting
points and longest uninterrupted expansion or repair operation
affect response latency. For the introductory text, stating
that answers and certificates are read between completed search
steps is sufficient.

Evaluation should include time to first feasible answer,
best feasible objective at several budgets, and time to a
quality target. Report failures to reach feasibility or the
target. A quality-versus-time curve usefully exposes behavior
that final runtimes alone conceal.

### Combining aggressive guidance with admissible bounds

Use distinct notation when both roles coexist, for example
q(s) for an unrestricted estimate and h_L(s) for a justified
remaining-cost lower bound. Choose expansions using q, g+q,
or another explicitly stated priority. Use g+h_L for sound
objective pruning and certificate calculations.

The current Week 10 formula should remain:

**L = min(U, min over eligible frontier entries of g+h_L).**

It requires retained coverage of all potentially improving
solutions, correct better-arrival handling, and consideration
of work awaiting completion or reopening. With L>0, U/L bounds
the multiplicative gap; U−L gives an additive bound. The
minimum key in an aggressively ordered queue need not be L.

An early heuristic run can instead supply a feasible U to a
separate branch-and-bound run. An aggressive estimate cannot
silently replace that second run's lower bound. Learning a
useful ordering, identifying a feasible incumbent, and safely
pruning a branch each require different evidence.

On finite spaces, complete coverage and sound pruning can
allow eventual proof despite inaccurate ordering. On infinite
spaces, a priority can indefinitely postpone required work;
do not extend weighted-search termination proofs to arbitrary
unrestricted guidance without new progress assumptions.

For weighted A*, emphasize that w scales a known admissible
base estimate. The usual C≤wC* conclusion is not a theorem
about every formula of the form g+wq. Also prefer “may cease
to be admissible/consistent” when scaling by w>1: a zero or
sufficiently weak heuristic can remain admissible after scaling.

## Suggested placement within the existing ten weeks

These are outline suggestions, not an attempted rewrite.

- Week 4, Part I: introduce guidance through useful ordering
  before formal properties. In Part II or the transition to
  Part III, use the small paired-estimate example. End by
  asking separately what first-goal stopping proves.
- Week 5, Part I: broaden the heading to construction and
  assessment of heuristics. Keep relaxed optima and pattern
  databases, but add relaxed solutions as cheap informative
  estimates. Mention FF briefly and defer planning machinery
  to Week 8. This should be an actual subsection job, not a
  parenthetical caveat after the admissibility proof.
- Week 7, opening: make interruptible anytime behavior explicit,
  contrast current and retained best, distinguish contract
  budgets, and show a simple improvement curve. Reuse this
  interface in the annealing trace and evaluation section.
- Week 8, planning application: revisit FF or LAMA after the
  planning model is introduced. It connects the Week 5 design
  choice to a real solver and Week 7's finite-budget evaluation.
- Week 10, Part I: organize around bounded-suboptimal answers
  and improving answers/certificates. Explain unrestricted
  guidance plus separate bounds before optional named variants.
  Use MHA* and ARA* only as short reading connections unless
  the instructor explicitly expands the chapter's scope.

No source prose, algorithms, or figures were adapted. The
six sources were checked selectively for these claims, not
comprehensively audited. No build or algorithm test suite was
needed because only this research note changed.
