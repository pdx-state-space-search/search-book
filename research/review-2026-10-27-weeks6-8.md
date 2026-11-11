# Review of Weeks 6–8

Reviewed 2026-10-27. Review only; no chapter, check, or skill
sources changed by this reviewer.

## Scope and result

Read every section of `src/06-local.md`,
`src/07-stochastic.md`, and `src/08-engineering.md`, including
their further readings, tables, formulas, figure alternatives,
and transitions. Used the repository authoring skill, its
editorial guide and examples, BRIEF.md, BOOK-NOTES.md,
STATUS.md, notation, source records, and relevant material
in Weeks 1–5. The introductory chapters were being revised
concurrently; line anchors below refer to the unchanged
Weeks 6–8 sources inspected during this review.

**No definite must-fix technical error was found in the
stated worked results or qualified guarantees.** This does
not certify every possible implementation of the methods:
these chapters largely specify mechanisms and design choices,
rather than complete executable algorithms. The main needed
repairs are point-of-use source support and a few substantive
teaching gaps. Optional opportunities are labeled separately.

Severity labels:

- **Must fix technical:** an incorrect claim, calculation,
  algorithm, or guarantee. None identified here.
- **Substantive teaching:** a missing explanation or reference
  needed for the agreed self-contained teaching standard.
- **Optional:** a useful improvement to otherwise sound text,
  or a precision issue without an identified false guarantee.

At review start, the book had no separate bibliography.
The root editor is adding that infrastructure during the
same task. The findings below concern the still-absent
point-of-use citations and unsupported source coverage in
Weeks 6–8, not a request to create a duplicate bibliography.

## Week 6: Local Search and Repair

### Substantive teaching: support named methods where used

Anchors: `src/06-local.md:85`, `:130`, `:259`, `:285`,
and the further-reading list at `:336`.

Min-conflicts, WalkSAT, tabu search, and the tour exchange
are introduced without citations at their points of use.
The further-reading list names appropriate sources for the
first three, but makes the reader infer which variant and
claims those sources support. This falls short of the
current bibliography and citation decision even though the
descriptions themselves appear technically sound.

Repair: add short bibliography links at first introduction
of min-conflicts, WalkSAT, and tabu search. If retaining the
tour exchange, name it as the conventional 2-opt move and
provide an appropriate primary source or verified reference
for that particular operation. Do not imply that the short
WalkSAT description reproduces one fully specified original
variant: the current explicit family/variant qualification
at lines 134–136 is good and should remain.

### Substantive teaching: introduce the tour before its delta

Anchors: `src/06-local.md:34`, `:54`, `:259`;
later dependency: `src/07-stochastic.md:162`.

The first tour explanation says only that a complete tour
visits all cities. Neither earlier chapter material nor
this chapter establishes the full traveling-salesperson
task: visit each city exactly once, return to the start,
and minimize the sum of travel costs. At line 259 the reader
must infer the meaning and ordering of a, b, c, d, what
segment is reversed, and why the replacement is still one
tour. Week 7's permutation example supplies part of this
foundation only after the delta formula has used it.

The formula is correct for the intended symmetric 2-opt
operation. This is a prerequisite/representation gap,
not an identified numerical error.

Repair: give the tour rules and cost convention first;
show a small cyclic ordering such as
`a → b → … → c → d → … → a`, with two distinct,
nonadjacent tour edges selected. Show that the new cycle
is `a → c → … → b → d → … → a`. A small before/after
diagram would make the unchanged edges and reversed segment
visible. Then derive the four-edge delta and retain the
asymmetry warning. Alternatively remove this extra example
if coloring and partitioning already carry the intended
lesson; an unexplained additional problem adds reading load.

### Optional: make one repair loop concrete

Anchors: `src/06-local.md:84`, `:101`, `:130`, `:308`.

The coloring and SAT traces are reproducible sequences and
correctly distinguish success from a general guarantee.
However, no complete repair loop specifies initialization,
variable selection, tie handling, move limit, and reporting
failure at the limit. The WalkSAT paragraph deliberately
describes a family, so absence of a particular noise rule
is not an error.

One short min-conflicts loop, or one explicitly labeled
WalkSAT variant, would let a new reader assemble these
design choices into an actual method. Use a finite budget,
preserve the best feasible answer when relevant, and report
budget exhaustion without an unsatisfiability conclusion.
This is an opportunity, not a reason to demand pseudocode
for every local-search family.

### Optional: distinguish a plateau from a necessary barrier

Anchors: `src/06-local.md:164`, `:171`, `:190`, `:197`.

The partition is a non-strict local minimum: moving weight
4 preserves E=4. Consequently, merely displaying an uphill
path does not by itself prove that every path to a better
solution needs an uphill move. The claimed barrier is
nevertheless real in this instance; independent enumeration
confirmed it. The only E≤4 states reachable from the
starting partition are the two obtained by transferring
weight 4 back and forth. Neither has a lower-score neighbor
inside that sublevel set.

Repair opportunity: add that one-sentence plateau argument
when calling the example a barrier. Do not describe the
displayed E=12 intermediate state as a minimum required
barrier height. A transfer path can reach zero with maximum
E=8; the existing text does not claim otherwise.

### Strengths and verified coverage

- The complete/inconsistent assignment distinction at
  lines 19–32 is clear and correct. A zero violated-constraint
  score certifies feasibility only for a correct encoding;
  a positive score does not certify unsatisfiability.
- The weighted-hard/soft warning at lines 41–47 preserves
  the difference between guidance and a feasible answer.
- The neighborhood count n(k−1), local/global definitions,
  and connectivity warning at lines 51–75 are sound. The
  pair-move comparison is appropriately qualified by its
  move count and inspection cost.
- The all-red coloring trace has scores 4, 1, 0. The SAT
  trace has scores 1, 1, 0 and correctly identifies the
  first flip as sideways.
- Every entry of the partition table is correct:
  12, 6, 4, 18, 16. The swap gives sums 15 and 15;
  transferring 8 then 6 gives scores 12 then zero.
- The coloring delta counts edges, not vertices, and the
  stated simple, undirected, loop-free assumptions matter.
  Neighbor-count maintenance costs degree(v) for an accepted
  move; the chapter avoids claiming that all work is O(1).
- Signed partition updates D±2w are correct. The TSP
  symmetry qualification is essential and correct.
- Tabu memory is correctly distinguished from exhaustive
  duplicate detection. Sampled neighbors do not certify
  local optimality; preserving best-so-far is separate from
  moving the current candidate.

### Figures and readings

The landscape SVG is a finite adjacent-state chain, not a
measured continuous energy curve. Its second dot is indeed
a local minimum and fourth dot the global minimum; caption,
alternative, and SVG metadata agree. Desktop and enlarged
text views are legible. At 390 pixels the embedded labels
are small, but the adjacent prose supplies the important
interpretation and the image links to the full original.
A mobile redesign is optional, not a discovered clipping
or semantic defect.

The reading entries are mostly source descriptions rather
than explicit instructions, so there is no major source-
claim/advice confusion. To fulfill the newer reading-guidance
standard, add a distinct **Reading suggestion:** telling the
reader which passage or issue to start with. For example,
keep the description of the Korf paper separate from advice
to compare its retained proof information with local search.

## Week 7: Stochastic Search and Anytime Optimization

### Substantive teaching: define the title's anytime concept

Anchors: `src/07-stochastic.md:1`, `:10`, `:51`, `:178`.

The chapter is titled "Anytime Optimization" but never
defines an anytime algorithm. Earlier material explains
incumbents, and Week 6's Korf annotation uses the term, but
neither supplies a definition on which this title can rely.
The chapter describes the mechanism—retain the best feasible
candidate—but leaves the new concept and its limits implicit.

Repair: define an anytime optimizer as one able to return
its current feasible incumbent when interrupted, potentially
improving that answer with more computation. If the search
begins infeasible and has not found a feasible candidate,
it cannot yet promise such an answer. Explain that monotone
incumbent quality is not convergence to the global optimum,
nor an optimality certificate. Connect this directly to the
existing current-versus-best distinction rather than adding
another detached terminology list.

### Substantive teaching: complete one annealing policy/run

Anchors: `src/07-stochastic.md:22`, `:46`, `:76`, `:90`.

The acceptance rule, temperature scaling, calibration, and
cooling warnings are accurate. Line 78 explicitly explains
that a cooling schedule is incomplete without move counts,
stopping, and restart/reheating rules. The chapter never
then provides one fully specified example satisfying its
own standard. The partitioning illustration computes the
probability of a useful worsening move but does not show
an actual randomized acceptance or a rejected proposal.

Repair: present one compact, explicitly illustrative
budgeted policy: initial partition, proposal distribution,
temperature, proposals per temperature, cooling factor,
stopping budget, and incumbent initialization/update.
Give a short trace with E, Δ, T, the selected uniform draw,
accept/reject, current E, and best E. This supplies the
missing connection between correct scalar formulas and an
implementable stochastic algorithm. There is no need to
claim that this illustrative tuning is recommended generally.

### Substantive teaching: cite methods and convergence

Anchors: `src/07-stochastic.md:17`, `:28`, `:82`, `:149`,
`:187`, `:195`, and `:299`.

Simulated annealing, the Metropolis acceptance rule,
classical convergence, evolutionary search, iterated local
search, and large-neighborhood search have no point-of-use
sources. The three optional readings cover only part of
this territory. In particular, the Kirkpatrick reading is
not a substitute for identifying the theorem behind the
asymptotic-convergence caveat, and neither Metropolis nor
large-neighborhood search has an explicit listed reference.

Repair: link the named methods to verified bibliography
entries. For the convergence sentence, either cite a precise
primary result with its intended meaning or keep the current
caveat and add a source without promising an unexplained
theorem. Hajek's 1988 paper is a suitable verified candidate:
its opening specifies a finite-state model, proposal
conditions, and convergence **in probability to the set of
global minima**, with a logarithmic-cooling condition related
to barrier depth. That is different from a finite-deadline
success guarantee. Do not silently strengthen the text to
almost-sure eventual permanent residence in one optimum.

### Optional: show one full evolutionary generation

Anchors: `src/07-stochastic.md:149`, `:162`, `:178`.

The invalid-permutation crossover example is correct and
useful, and the list of algorithm-defining choices is honest.
Selection, variation, replacement, and elitism still appear
as prose descriptions without one population evolving through
them. A tiny generation using a representation already known
to the reader would clarify where each operation acts.
This is a depth opportunity, not a false claim requiring
an algorithm survey or another large worked problem.

### Optional: sharpen two broad statements

Anchors: `src/07-stochastic.md:223`, `:295`.

"A single successful seed ... does not estimate reliability"
is clearer as "does not establish a reliable success rate".
A single Bernoulli observation technically admits a very
uncertain estimator; the educational point is the weakness
of the evidence. Also qualify "Stochastic search trades
exhaustive coverage" to the heuristic stochastic methods
considered here. Randomness itself does not preclude a
complete search that retains and exhausts alternatives.
Neither sentence currently supports a consequential wrong
formula, so these are optional precision edits.

### Strengths and verified coverage

- The sign of Δ and the acceptance table are correct.
  Improvements and sideways moves are accepted; a higher
  T increases a fixed positive-Δ acceptance probability.
- The symmetric-proposal qualification prevents an
  unwarranted equilibrium-distribution claim. The chapter
  does not need Metropolis–Hastings to use the rule as a
  heuristic policy, and correctly does not claim arbitrary
  proposals preserve the physical stationary law.
- Dollars-to-cents rescaling and T₀=−Δ₀/ln(q) are correct;
  the example gives approximately 17.92568.
- Geometric cooling is not confused with the stronger
  conditions needed for asymptotic convergence.
- The restart model states independence, identical trial
  distribution, positive success probability, and fixed
  duration before using the geometric law. The five-trial
  success probability is 0.67232, not certainty.
- The outcome-dependent-duration formula is correct for
  iid trials with the stated finite conditional expectations.
  Its example is 110 seconds. The cutoff/right-censoring
  distinction is particularly valuable and should remain.
- The four-city crossover indeed produces (A,B,A,B).
- Exact repair of a restricted minimization problem cannot
  worsen its optimum if the old feasible answer remains
  permitted. The text correctly limits that guarantee to
  the neighborhood and preserves the original candidate
  under an unsuccessful time-limited repair.
- Experimental sections correctly expose unsuccessful runs,
  distinguish seeds from sampled instances, separate tuning
  from final evaluation, and avoid treating equal iteration
  counts as equal computational budgets.
- The ten-run example correctly shows why successful-runtime
  averages alone conceal reliability differences. The text
  does not present these hypothetical ten runs as reliable
  population estimates or as a universal algorithm ranking.
- Quantiles, paired-instance comparisons, and the warning
  about pairing seed labels are appropriately qualified.

### Rendering and readings

The acceptance table renders correctly at desktop, narrow
width, and enlarged text. There are no chapter figures and
no pseudocode to audit for a hidden mismatch between its
loop and its guarantee; the absence of a complete annealing
policy is the teaching finding above.

The three reading annotations describe their sources and
do not explicitly issue conflicting instructions. Add
distinct reading suggestions and a concrete starting point
when revising. Keep Johnson et al.'s experimental study
separate from this book's own instructions on reporting;
do not imply every modern evaluation recommendation is a
claim established in that one paper.

## Week 8: Engineering Search

### Substantive teaching: encode completion deadlines

Anchor: `src/08-engineering.md:325`.

The scheduling model and the optimum-seven proof are correct.
The paragraph that proposes a CSP representation only says
that horizon H restricts start-time domains, then speaks of
proving that no schedule finishes by H. A beginning reader
does not yet see the actual finite domains or how a completion
deadline differs from an allowed latest start. Merely using
start domains 0..H would allow tasks to finish after H.

Repair: for this integer example, state that a task of
duration pᵢ can start in {0,…,H−pᵢ}, with machine domain
{1,2}; explain an empty start domain. Show one precedence
constraint, such as s_C≥s_A+3, and state that tasks assigned
to one machine must have disjoint execution intervals.
Use half-open intervals to permit one task to start exactly
when another ends. This makes the proposed encoding
concrete without adding a general scheduling chapter.
This is an underspecified teaching example, not an actual
incorrect start-domain formula already printed in the book.

### Substantive teaching: cite the named models and protocols

Anchors: `src/08-engineering.md:198`, `:216`, `:243`,
`:272`, and `:348`.

Work stealing, hash-distributed search, the positive-fact
action model, and delete relaxation have no source links
at their introduction. The readings support HDA* and
heuristic planning but are not tied to the relevant claims.

Repair: link the owner-based scheme and global termination
caveat to the HDA* bibliography entry. The author's paper
explicitly supports the ownership, in-flight-message, and
exact-state-comparison distinctions taught here. Cite an
appropriate primary planning/action-model source at the
model's introduction and the verified planning reading where
its relaxation discussion is used. If naming the action
language STRIPS, verify its primary source and state that
the chapter teaches a restricted positive-fact model rather
than introducing all language variants. Add a work-stealing
source if retaining that named systems concept.

### Optional: clarify the scope of shared-queue ordering

Anchor: `src/08-engineering.md:209`.

"A single shared priority queue preserves a global selection
order" can be read as preserving the serial best-first
expansion sequence. It preserves priority order among
currently enqueued records, not a serial sequence when
expansions run concurrently.

For example, workers can remove records of priorities 1
and 5 while the priority-1 worker is still computing a
child of priority 2. A serial algorithm would have queued
and selected that child before priority 5. The shared
queue itself has behaved correctly throughout.

Repair: add "among currently queued records" and connect
the in-progress expansion to the later termination caveat.
The later paragraph already accounts for work undergoing
expansion, so this is an ambiguity repair rather than an
identified false optimality guarantee.

### Optional: state the probability model for fingerprints

Anchor: `src/08-engineering.md:52`.

The exact-key comparison rule is correct. Calling a stored
fingerprint a "probabilistic correctness tradeoff" is a useful
warning but does not by itself define a probability. For
a fixed deterministic hash on a fixed input, a collision
either happens or does not; quantifying risk needs a
random-hash or input-distribution assumption.

Repair opportunity: state that any claimed collision
probability depends on the fingerprint construction and
randomness assumptions. No quantitative collision claim
or guarantee is currently made, so this is optional.

### Strengths and verified coverage

- Representation costs are tied to actual hot operations,
  not an unsupported universal rule that packed data wins.
- Canonicalization requires preservation of future actions,
  costs, goals, and reconstructible concrete answers.
- Hash collisions are distinguished from equality; mutating
  stored keys is correctly identified as a correctness risk.
- Copy cost bC, persistent sharing tradeoffs, trails and
  restoration obligations, and best-first snapshot needs
  are well explained. The trail memory claim concerns
  active-path data rather than pretending that a large
  global reached set costs nothing.
- The bitset/locality/vectorization discussion is cautious
  about workload, sparsity, latency, and end-to-end timing.
- Memory arithmetic is correct: 28,000,000 bytes for records,
  7,200,000 for queue entries, 35,200,000 total; rounded MiB
  values are 26.7, 6.9, and 33.6. Exclusions, slack, and
  potential shared-key double counting are explicit.
- The throughput counterexample is correct: 10 seconds
  versus approximately 13.3 seconds despite fewer expansions.
- Parallel branch ownership, imbalance, restart independence,
  distributed duplicates, in-flight messages, and seed-only
  reproducibility are treated carefully. No claim that more
  workers necessarily reduce time or work is made.
- The courier has a real optimum of four actions and
  relaxed optimum of three. The real lower-bound argument
  identifies four distinct necessary actions. Dropping
  deletes preserves each real positive-fact plan; the
  three-action relaxed plan exploits persistent AtA.
- The delete-relaxation argument correctly limits itself
  to the stated positive preconditions/goals and correctly
  warns that finding one relaxed plan gives the wrong bound
  direction for automatic admissibility.
- For the schedule, the chain bound is 7, the workload
  bound 5.5, and the shown schedule achieves 7. Taking
  maximum rather than sum is justified. Integer starts
  suffice for this example; no broad claim with release
  dates or setup costs is smuggled into the model.
- The final distinction among feasible answers, justified
  lower bounds, and failed heuristic runs is sound.

### Figures and readings

The schedule SVG, task table, caption/alternative, and
optimality argument agree: A 0–3 and C 3–7 on machine 1;
B 0–2 and D 2–4 on machine 2. Idle 4–7 is harmless.
No clipping or navigation collision was visible in inspected
desktop, narrow, or enlarged views. As with the landscape,
mobile SVG text is small and opening the linked original
is useful; this is not evidence of a false diagram.

The HDA* entry correctly distinguishes its 2013 journal
version from the linked 2012 arXiv submission. The arXiv
record confirms the title, authors, journal reference,
and DOI. The reading annotations are descriptions; add
separate starting-point advice if intended. The transition
to adversarial search/sampling is consistent with Weeks 9–10
and does not presume planning will become a full later unit.

## Independent checks and source evidence

### Finite verification performed

Ran `python3 checks/check_examples.py`; that script passed.
Inspected its implementation before interpreting
that result. For this scope it checks the displayed coloring
and SAT traces, partition neighbor table, selected annealing
and restart arithmetic, BFS optima for real/relaxed courier,
integer scheduling instances through horizon 7, and a range
for the modeled memory total. It is not a local-search,
annealing, evolutionary, or parallel solver implementation.

Inspected `checks/check_algorithms.py`'s local-math checks:
5,184 partition delta cases over four small weights and
all sign assignments; one acceptance value; a truncated
geometric-series expectation check. It does not test
general annealing convergence, WalkSAT selection, tabu
behavior, population evolution, or concurrency.
`checks/check_extensions.py` concerns other chapters.
The source/link check is structural and does not establish
whether citations support claims or whether methods are
pedagogically self-contained.

Additional independent calculations, run without adding
book/check files:

- Enumerated all 64 simple graphs on four vertices, all
  81 three-color assignments, and every recoloring: all
  41,472 edge-conflict deltas matched full rescoring.
- Enumerated the partition's transfer graph. Only two
  E≤4 states are reachable from the given candidate;
  no zero partition is reachable without worsening.
  A minimax-path calculation gives minimum peak E=8.
  One such path transfers weights 4, 6, 8, 4 and has
  successive energies 4, 8, 8, 0. This supplements,
  rather than contradicts, the chapter's simpler path.
- Checked the asymmetry caveat with tours ABCDEA and
  ACBDEA. Set all directed edges to cost 1 except C→B
  with cost 9. The displayed external-edge-only formula
  gives zero, while full rescoring gives +8. Thus the
  chapter correctly requires symmetry for that formula.
- Recomputed every acceptance-table entry, the 17.92568
  temperature calibration, and each MiB conversion.
- Checked the restart expectation independently by the
  renewal identity T=(1−p)(F+T)+pS, which gives the
  printed ((1−p)/p)F+S under the stated iid assumptions.

### Rendering evidence

Ran the existing browser check against the built draft:
45 page/view checks, zero reported overflow, broken images,
or wide-navigation overlap failures. It produced screenshots
in `/tmp/search-book-browser-wFTQ6E`.
Manually inspected the Week 6 landscape at narrow and
200% text sizes and Week 8 schedule at desktop/narrow
sizes. Inspected SVG source metadata and geometry as well.
The browser check checks page geometry and image loading;
it does not detect tiny labels, semantic inconsistencies,
or missing explanations automatically. Its built snapshot
preceded concurrent root-editor bibliography integration;
it is not a final check of those later changes.

### Primary-source passages consulted

These were selected-passage and metadata checks, not full
audits or permission to import source prose or figures.

- [Selman et al.](https://cdn.aaai.org/AAAI/1994/AAAI94-051.pdf):
  inspected metadata and local-SAT/annealing/noise passages.
  It supports the chapter's distinction among complete
  assignments, flips, randomized escape, and bounded runs.
  Its different specific policies reinforce the need to
  label a chosen variant rather than treating a family
  description as complete pseudocode.
- [Metropolis et al.](https://bayes.wustl.edu/Manual/Metropolis.pdf):
  inspected the acceptance prescription and equal forward/
  reverse proposal argument on printed pp. 1088–1089.
  This supports the existing acceptance rule and symmetric-
  proposal caveat. DOI: 10.1063/1.1699114.
- [Hajek, 1988](https://web.mit.edu/6.435/www/Hajek88.pdf):
  inspected the abstract and opening finite-state/proposal
  assumptions. It supports the distinction between a
  specified asymptotic convergence result and a practical
  geometric schedule's finite-budget behavior.
  DOI: 10.1287/moor.13.2.311.
- [Kishimoto et al.](https://arxiv.org/abs/1201.3204), and its
  [author manuscript](https://arxiv.org/pdf/1201.3204):
  verified journal metadata and inspected state ownership,
  termination/in-flight messages, and exact-state versus
  fingerprint comparisons, especially manuscript pp. 12–14.
  These directly support Week 8's relevant distinctions.
- The Bonet–Geffner DOI could not be opened through the
  browser tool during this pass. Existing repository notes
  record prior publisher metadata/abstract checking; this
  review does not claim a new full-text verification.
  Other further-reading metadata were read in the existing
  source records rather than independently re-audited in full.

## Limits and priorities for the next authoring pass

First connect named concepts and borrowed claims to the
new bibliography, including sources not already present
in optional readings. Next define anytime behavior and
complete one annealing policy/run. Then decide whether
to teach the tour example fully or omit it, and make the
scheduling deadline encoding concrete. Preserve the strong
bound directions, finite-budget qualifications, and honest
experimental accounting throughout.

This review did not run empirical stochastic benchmarks,
test a parallel implementation, prove an annealing theorem,
or inspect every line of every linked reading. No student
submissions or archive material were accessed. No commits
or pushes were made. Passing finite checks and finding no
definite technical defect leave the substantive teaching
and source-support findings above open for revision.
