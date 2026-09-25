# Audit: ch4-symbols corrections, round 1

Unit: chapters/ch4-symbols.tex (Chapter 4 Symbols list, PDF 531-536, printed pp. 499-504).
Item for this unit: corrections/ch4.md item 6. Source: Mandell's "Changes to text of Chapter 4", page numbered "3"
(PDF 702). The cover note on PDF 699 is signed "Gordon Mandell, June 1994". PDF 700 is unnumbered, and PDF 701 and 702 are
numbered 2 and 3.

## What was checked

1. **Item applied as specified.** PDF 702 was compared entry by entry with the working tree.
   - Symbols: `$\vec{A}_e$`, `$\vec{E}_o$`, `$\vec{F}(t)$`, `$P_a$`, `$P_e$` and `$\vec{c}_{\mathrm{eff}}$`. These are
     the forms corrections/ch4.md and STYLE.md section 15 give (arrow over the letter only; o is the letter o;
     "eff" is an upright word subscript). They are the same forms the corrected ch4-intro-sec1.tex uses at (7b)-(7d)
     and (8) (checked with grep).
   - Meanings, word for word:
     - "nozzle exit plane area written as a vector whose direction is forward along the vehicle centerline": matches.
     - "vector sum of all externally-applied forces other than pressure component of thrust": matches, including the
       source's hyphen. The 1973 E-vector entry keeps its own "externally applied" unchanged.
     - "thrust as a function of time": matches.
     - "ambient pressure": matches.
     - "pressure of exhaust gas at nozzle exit plane": matches.
     - "effective exhaust velocity, \emph{also} called equivalent exhaust velocity": matches. The underlined "also"
       is `\emph`, the same as the 1973 "mass; \emph{also} average mass".
   - F(t) now reads "magnitude of thrust as a function of time", as PDF 702 gives it.
   - Order. The 1973 list (PDF 531-532) sets the capitals first (A, B ... M_y) and then the lowercase letters
     (a-vector, c ...). The new rows are placed as follows:
     - `\vec{A}_e` goes between "A, B" and `A_f`, since e comes before f. The 1973 A-subscripts run f, r, o, 1, 2,
       so no strictly alphabetical slot exists, and this placement is the natural one.
     - `\vec{E}_o` goes after `\vec{E}`.
     - `\vec{F}(t)` goes after `F(t)`: the vector follows its scalar, as with the 1973 pair F and F-vector.
     - `P_a` and `P_e` go after `M_y`, the last capital.
     - `\vec{c}_{\mathrm{eff}}` goes after `\vec{c}`.
   - Nothing was added that the source does not give. The Summary's new variables (t-hat, y-hat, I_t2) are not
     added to the Symbols list. That is correct: the Decisions put their definitions in the Section 2.2.1 key.
2. **Notes.**
   - The \vec{A}_e row, the first added row, carries one `\edcap`. It names all six symbols as added per Mandell's
     June 1994 supplement ("Changes to text of Chapter 4", p. 3) and says they are not in the 1973 list. The claim
     is true: PDF 531-532 show none of them.
   - The \vec{A}_e meaning wraps to two lines, so an hbox cell is not possible. STYLE.md section 9 allows `\edcap` in
     a table row.
   - The F(t) row is a one-line `\multicolumn{1}{l@{}}` cell with an `\ednote`, the pattern of chapters/ch1-symbols.tex.
     It quotes the 1973 entry as "thrust as a function of time", which is correct (PDF 531 and git HEAD line 20).
     Its statement that the supplement adds the vector \vec{F}(t) as a separate entry is correct.
   - "p. 3" is the page number printed on PDF 702.
   - Observation, not a discrepancy: the `\edcap` sentence "They are introduced in the corrected text after
     equation (7)" is true of the corrected text: all six first appear in (7b)-(8) and their "Where" lists. But
     \vec{F}(t) was already defined in the 1973 text too ("The thrust can be denoted by the single symbol F(t)", PDF 545,
     and the 1973 (8)); only its Symbols-list entry is new. The note never says otherwise, so no change is required.
     An optional precision would be "(\vec{F}(t) already appears in the 1973 equation (8))".
3. **Doubt notes.** No doubt item (D1-D15) belongs to this unit, and no doubt note was added. No arithmetic is involved.
4. **Scope.**
   - `git diff HEAD -- chapters/ch4-symbols.tex` shows three kinds of change: the header comment, which describes the
     corrections step accurately; six inserted rows; and the one changed F(t) row.
   - No other row changed. The 1973 entries around the insertions (A, B; A_f; E; F; F-vector; F_m ... M_y;
     a-vector; c; c-vector; d()/dt) are byte-identical to HEAD.
   - The longtable spec, head, foot and `\addtocounter{table}{-1}` are untouched.
5. **Labels.** No label added or changed. `\label{ch4:sec:symbols}` is kept. No equations.
6. **Section 15 notation.** Every new symbol follows section 15 (see 1).
7. **Render.**
   - build/unit/ch4-symbols.pdf and the PNGs (18:28:19-20) are newer than the edit (18:28:10).
   - build/unit/ch4-symbols-1.png shows the six new rows in place, with the bracketed "[Editor's note: ...]" after
     "centerline".
   - The F(t) row shows its E1 marker, and the footnote E1 at the foot of page 1 has its full text. The footnote is
     not lost from the longtable cell.
   - The `\eqref{ch4:eq:7}` prints "(??)" in the standalone unit build because the label is in ch4-intro-sec1.tex.
     The log shows it as the only undefined reference. It resolves in the chapter build.
   - Pages 2-4 continue the longtable normally, with repeated heads and the closing rule on page 4.

## Discrepancies

none

| where | expected (source/1973) | found | severity |
|---|---|---|---|
