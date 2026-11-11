---
name: search-book-authoring
description: >-
  Draft, revise, or review chapters of this repository's
  State-Space Search course book for consistent teaching style
  and technical precision. Not for build-only or Git maintenance.
---

# Search Book Authoring

Teach a programmer encountering search for the first time.
Help the reader understand what a method does, why it helps,
and what its answer establishes. Preserve the book's worked
examples, technical care, and practical emphasis while making
its explanations easier to follow.

This is a repository-local skill. Project paths below are
relative to the book repository root; the skill folder is
`.agents/skills/search-book-authoring/`.

## Establish the requested work

Distinguish drafting, revision, and review-only requests.
A request for reactions or a plan is not permission to edit
chapters. Work only on the requested scope and necessary
integration. Preserve Bart's wording in BOOK-NOTES.md unless
he asks to edit it. Commits and pushes need their own user
authorization; using this skill supplies neither.

Read the current request, applicable project instructions,
[BRIEF.md](../../../BRIEF.md), and the relevant feedback in
[BOOK-NOTES.md](../../../BOOK-NOTES.md). Use
[STATUS.md](../../../STATUS.md) for the revision state,
[src/SUMMARY.md](../../../src/SUMMARY.md) for order, and
[src/notation.md](../../../src/notation.md) for conventions.
Inspect the target and the relevant adjoining material.
Consult the relevant entries in the
[bibliography](../../../src/bibliography.md) when checking
or adding citations.

Resolve feedback by the latest explicit decision, not by
assuming every old note is still current. For example,
BOOK-NOTES.md proposed postponing AC-3, but the subsequent
resolved decision in BRIEF.md omits it. Treat existing prose
as material to assess, not an unquestioned authority.
If an unresolved conflict materially changes the assignment,
clarify it before doing dependent work.

## Outline before drafting

Always begin a chapter with a two-level outline, developed
one level at a time. First establish only the top-level
sections: the chapter's purpose, their order, and the job
each section does. For an existing draft, reconstruct its
current organization before proposing improvements.

Resolve that structure before expanding it into second-level
subsections. Resolve the second level before writing prose.
In an outline discussion, present only the requested level;
do not preempt the next pass with subsections or a rewrite.
An existing agreed outline can support small corrections
without restarting the whole outlining process.

If a chapter has two distinct teaching purposes, consider
splitting it at a conceptual boundary. A week may contain
more than one reading chapter without extending the course.
Propose the split before changing files, numbering, or links.

## Teach before compressing

For drafting, substantive revision, and editorial review, read the
[editorial guide](references/editorial-guide.md). For tone
calibration or choosing how to repair an abrupt explanation,
consult the [annotated examples](references/examples.md).
These are teaching patterns, not a compulsory chapter outline.

Identify what the reader already knows and what this section
must add. Build from a named concrete problem to its choices,
notation, method, trace, and justification as appropriate.
Do not require an unfamiliar concept to explain another one.
When returning to an example, identify the problem and its
specific instance, restoring the context needed for the next
step. Distinguish claims about that instance from general
claims about the problem.

Keep enough explanation to make the chapter self-contained
within the book. Length targets guide reading load; they do
not justify unexplained notation or missing reasoning.
Do not pad sound material to reach a target either. Respect
current topic allocation rather than moving omitted material
to another week automatically.

## Preserve technical meaning

Separate feasibility, objective quality, path cost, and
computational effort. Define size parameters and counting
rules. Give guarantees for the actual stated method under
its assumptions, including relevant duplicate handling,
goal tests, termination, and randomness. State a heuristic's
intention without turning it into a universal guarantee.

Use concise language-neutral imperative pseudocode when it
adds precision. Typeset it like an algorithms textbook, using
← for assignment and one statement per line. Begin with a
brief task sentence: the operation's name in capitals, its
inputs in context, and its result or effect. Let surrounding
prose supply the details. Use proportional text and
mathematical typography rather than typewriter-style code
blocks; see the editorial guide's pseudocode conventions.
A trace and a short argument should explain its important
behavior. Keep implementation-language listings and validation
code outside the student-facing chapters.

Use original figures where they make choices, relationships,
changes, or growth easier to understand. Keep notation,
values, labels, and alternative text consistent with the prose.
Keep a book-wide bibliography separate from suggested
readings. Cite sources for named concepts and substantive
borrowed claims where they enter the explanation. In reading
recommendations, distinguish source description from advice
to the reader. Use the project's source/adaptation ledger;
do not invent provenance or claim full-paper review from
metadata access.

## Review and finish

Use the editorial guide's review questions. For substantial
new technical material, obtain an independent review when
it adds useful confidence. Check examples and changed claims
with meaningful finite calculations where appropriate;
these supplement the argument rather than prove it.

Use the existing tools instead of duplicating them:

- `mdbook build`, then `python3 checks/check_book.py` for
  source, title, and generated-link checks.
- Relevant example/algorithm checks in `checks/` when their
  covered claims change. Inspect their coverage; a filename
  does not establish what was tested.
- `node checks/check_browser.cjs` and manual screenshots for
  changed diagrams, formulas, or layout. Inspect affected
  content at desktop/narrow widths and enlarged text.

A prose-only skill or workflow edit does not require a full
book rebuild. Do not repeat unchanged suites without a new
concern. Interpret length advisories against the accepted
scope; do not cut a needed explanation merely to silence one.

For chapter edits, reconcile affected titles, links, notation,
readings, and transitions. Update the durable revision/source
records when warranted. Report what changed, relevant checks,
and remaining teaching decisions. A checked first draft is a
review milestone, not a finished textbook. Do not resume other
chapter work just because this task has ended.

## Maintain the standard

When later feedback changes the teaching style, update the
guide's reusable principle and add an example only if it
clarifies a new decision. Keep topic allocation in BRIEF.md
and case-specific verification in the research records.
Do not turn a one-off correction into a universal rule.
