# Final source and provenance review

Reviewed 2026-10-22. Scope: source-log, verified-sources,
license-notes, recovery-review, attribution, reading-guide,
README, and Further reading sections in chapters 01–10. This is a
metadata and consistency review, not a full audit of cited books
or papers. The `prev/` archive was not inspected.

## Findings

- No material mismatch was found between the source ledger, license
  notes, reader-facing attribution, reading guide, README, and the
  ten chapter reading lists. They consistently say that chapter
  prose/examples and figures are original, that Khemani and the
  earlier Wikipedia outline informed topic coverage, and that no
  Wikipedia prose, tables, pseudocode, or images were adapted.
  The stated CC BY-SA 4.0 scope is limited to this book's original
  contributions; third-party references and mdBook dependencies
  retain their own terms.
- There are no missing Wikipedia adaptation records given the
  documented no-adaptation status. The attribution instructions
  for any future use capture article/revision, history, license,
  location, changes, and nearby credit. This conclusion is based on
  the supplied provenance declarations and repository text review;
  it is not an independent forensic comparison against Wikipedia.
- The stale status is in `recovery-review.md`: its “Pending after
  reconnect” checklist still says to recover the archive,
  run the book/check/browser workflow, and update
  status/readme/review logs. The current tree already contains
  chapters 01–10, including complete chapter 08, and the README
  describes a built HTML book. This recovery note should be marked
  historical or have its pending checklist reconciled with current
  state. Its earlier first-draft wording is otherwise explicitly
  scoped to the recovery checkpoint.
- The reading lists give useful titles and years, but citation
  completeness is uneven. DOI-linked papers are resolvable; many
  omit venue, volume, and pages in the student-facing entry. The
  Russell/Norvig entry does not name an edition or year;
  Dechter and Khemani already include years. Fuller venue
  metadata for papers, including the Korf instructor-hosted
  PDF citation, would be an optional enhancement. Consider
  an edition for Russell/Norvig and an author/publisher
  landing page for the Korf item. These are enhancements, not
  bibliographic contradictions found in the material reviewed.
- The source notes correctly qualify their level of review as
  metadata/relevance checks rather than comprehensive paper review.
  In particular, the Hart/Nilsson/Raphael access limitation and
  the statement that no cited paper was comprehensively audited
  are retained. No claim of full-text review should be inferred.

## Spot checks and limitations

The citation list was compared against the chapter sections and
`verified-sources.md`/`recovery-review.md`; author names, years,
titles and supplied DOI identifiers appear internally consistent
for the items explicitly recorded as checked. Spot-checking
publisher/author records confirmed, among other items, Karp's 1972
chapter in *Complexity of Computer Computations*, pp. 85–103, and
Korf's 1998 *Artificial Intelligence* paper, vol. 106(2), pp.
181–203. The prose entries omit some of that useful bibliographic
context, as noted above. The web checks did not expand to every
Further reading item, and this note does not verify every link's
current availability or inspect the full text of every cited work.

No chapter text was changed as part of this review.

## Publisher/author metadata follow-up (2026-10-22)

Checked the four remaining citation records against their official
publisher or author pages. These checks verify citation metadata,
not the full papers' arguments.

- **Russell and Norvig, *Artificial Intelligence: A Modern
  Approach*.** The existing chapter link points to the authors'
  AIMA site, which identifies itself as the US fourth edition.
  The authors' [editions page](https://aima.eecs.berkeley.edu/translations.html)
  gives “Fourth Edition (2020),” Stuart Russell and Peter Norvig,
  Pearson, 2020, ISBN 978-0134610993. Pearson's official
  [catalog page](https://www.pearson.com/en-us/subject-catalog/p/artificial-intelligence-a-modern-approach/P200000003500/9780134610993)
  likewise identifies the fourth edition. The chapter's current
  short citation (“Russell and Norvig,” linked site, chapter 3)
  omits edition/year; metadata is now confirmed.
- **Dechter, *Constraint Processing*.** The existing ScienceDirect
  link is the publisher's book record. It lists Rina Dechter,
  2003, Morgan Kaufmann, ISBN 978-1-55860-890-0, DOI
  10.1016/B978-1-55860-890-0.X5000-2. Its chapter-level contents
  and selected preview are available, while full access may require
  purchase or institutional access. The cited year was already
  present; no year correction is needed.
- **Davis, Logemann, and Loveland, “A Machine Program for
  Theorem-Proving.”** Official ACM DOI page:
  https://dl.acm.org/doi/10.1145/368273.368557 . It returned HTTP
  403 in this check, so I could not read ACM's record directly.
  DOI/title lookup in bibliographic records identifies *Communications
  of the ACM*, 5(7), July 1962, pp. 394–397, DOI
  10.1145/368273.368557, authors Martin Davis, George Logemann,
  and Donald W. Loveland. The chapter citation gives title, all
  three surnames, DOI, and year; it omits journal/volume/pages.
  Metadata was cross-checked via [CiNii Research](https://cir.nii.ac.jp/crid/1361699994219727872)
  and [DBLP](https://dblp.org/rec/journals/cacm/DavisLL62.html),
  so those fields are not represented as directly verified on ACM.
  Full-text access was not established.
- **Kirkpatrick, Gelatt, and Vecchi, “Optimization by Simulated
  Annealing.”** The official Science DOI record
  (https://doi.org/10.1126/science.220.4598.671) identifies S.
  Kirkpatrick, C. D. Gelatt Jr., and M. P. Vecchi; *Science*,
  220(4598), 671–680; 13 May 1983; DOI
  10.1126/science.220.4598.671. The Science page itself returned
  HTTP 403 when opened, but its DOI search result exposed the
  publisher metadata. Full article access is restricted to access
  options; no full-text review is claimed. The chapter's existing
  title, authors, year, and DOI are consistent; venue/volume/issue/
  pages could be added for completeness.
