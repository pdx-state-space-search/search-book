# State-Space Search

A ten-week mdBook draft for Bart Massey's PSU CS 410/510
course, by ChatGPT and Bart Massey. All ten chapters have a
first draft; instructor review and substantive revision are
in progress. The introduction
and Week 1 were rewritten from feedback on 2026-10-27.

## Read or build

From any directory:

```text
mdbook build /home/bart/work/search/book
mdbook serve /home/bart/work/search/book --open
```

Open [_build/index.html](_build/index.html) to read the book.
Only mdBook HTML is produced.
The source is in src/, with its reading order in src/SUMMARY.md.
The installed tool used for the first build is mdBook 0.5.2.
No additional preprocessors, JavaScript packages, network fonts,
or MathJax are needed to read the book offline.

## Editorial contract

See BRIEF.md for the accepted scope and chapter allocation.
There are no exercises or programming-language source listings
in the student-facing text. Short language-neutral pseudocode
is used where it makes an algorithm precise. Planning and
scheduling are compressed applications in the engineering week.

The initial weekly target was approximately 2,500–3,500 words,
including a few short reading recommendations. The revised
Week 1 contains about 3,300 words; the other weekly chapters
contain about 2,100–2,500. Further changes follow instructional
needs rather than a fixed word count. Reflowable HTML
has no fixed page count; page length is not forced by small type
or by hiding necessary explanations. Figures have descriptive
alternatives and can be enlarged with the rest of the page.

## Verification

```text
mdbook build /home/bart/work/search/book
python3 /home/bart/work/search/book/checks/check_algorithms.py
python3 /home/bart/work/search/book/checks/check_examples.py
python3 /home/bart/work/search/book/checks/check_extensions.py
python3 /home/bart/work/search/book/checks/check_book.py
node /home/bart/work/search/book/checks/check_browser.cjs
```

The Python checks use the standard library. The browser check
uses Chromium and the system node-ws package; its screenshots
are written to a temporary directory. It checks all ten chapters
and the introduction, reference pages, and Epilogue at desktop
and narrow widths and with 200% text. It also captures page
content and a
sheet of all teaching figures for manual inspection. The new
growth figure can be regenerated with
`python3 checks/render_growth.py` (requires matplotlib).
Algorithm checks explore finite models independently of the
prose. They are regression evidence, not a substitute for the
mathematical arguments.

The first-draft validation on 2026-10-22 passed the build,
all Python checks, and 42 browser/view checks. Seven original
figures and representative rendered prose, tables, and
pseudocode were inspected then. See STATUS.md and
research/review-log.md for current revision checks;
research/final-validation.md preserves that earlier checkpoint.
See those records for results, review scope, and limitations.
Per-workstream research
notes retain source metadata and claim checks. The validation
scripts are editorial tools outside the student-facing src/ tree.

## License and provenance

Original contributions are under CC BY-SA 4.0. See LICENSE.md,
src/attribution.md and research/source-log.md. No Wikipedia
article passages or figures are incorporated in this draft;
the previous Wikipedia outline informs broad coverage only.
Khemani's table of contents informs coverage without reproducing
book prose or figures. References keep their original licenses.

No original syllabus, archive, student submission, or grading
record is modified by this campaign.
