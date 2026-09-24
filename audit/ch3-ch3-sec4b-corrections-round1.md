# Audit: corrections applied to chapters/ch3-sec4b.tex (round 1)

Unit: `chapters/ch3-sec4b.tex` (4.3-4.4, PDF 408-432, printed pp. 376-400). I audited `git diff HEAD -- chapters/ch3-sec4b.tex`
against HEAD 7e2087d, the faithful transcription. The diff has four hunks: 13 insertions and 8 deletions. The build
audited is `build/unit/ch3-sec4b-01.png` to `-12.png` with `ch3-sec4b.pdf`. It was built at 09:33:51 from the .tex saved
at 09:33:49, so the build is current. I did not rebuild. Rules read: STYLE.md sections 4, 8, 9, 10, 11 and 14, and
corrections/ch3.md, including the "Decisions for the corrections step (2026-09-24)" block.

Items to apply:
- **Item 5** (errata, PDF 664, "Page 382, line 1"): "(from left to right in the diagram) the drag coefficient shows a
  corresponding increase.", with an \ednote that quotes the 1973 line.
- **D8** (PDF 425): set $p_b$ for the typed $P_b$ in the Figure 33 caption, with no note (Decisions).
- **D28** (PDF 423): bring the existing note on "the second term in equation (28)" into the doubt-note style.

## Sources and their authors and dates

- **1973 errata sheet, PDF 664.** It is headed "ERRATA" and gives the book's citation (Mandell, Caporaso and Bengen,
  MIT Press, 1973). It shows no author of the sheet and no date. The entry reads: "Page 382, line 1 should read (from
  left to right in the diagram) the drag coefficient shows a corre-sponding increase." PDF 665 is a second typing of the
  same list, headed "TOPICS IN ADVANCED MODEL ROCKETRY / Errata". It also has no author or date. Its wording is
  identical: "On page 382, line 1 should read: "(from left to right in the diagram) the drag coefficient shows a
  corresponding increase."" Neither sheet has any other entry in pp. 376-400.
- **Chapter 3 supplement pages, PDF 688-698.** I checked each page's head and foot, and the last page of each document
  in full. None shows an author, a signature or a date. They cover:
  - replacement pp. 356-357 (PDF 688-689);
  - Section 5.2.2, p. 412 (PDF 690);
  - Section 5.3, pp. 422-424 (PDF 691-693);
  - the symbol table (PDF 694);
  - pp. 445, 449 and 451-452 (PDF 695-698).

  None touches printed pp. 376-400. PDF 694 has no base-pressure entry.
- **1973 pages read.** PDF 413 (Figure 29 artwork and caption), PDF 414 (printed p. 382), PDF 423 (p. 391), PDF 425
  (Figure 33) and PDF 336 (p. 304, equation (28)).

## What was checked

1. **Item 5, extent and wording.** PDF 414, lines 1-2, read "(from top to bottom in the diagram) the drag coefficient
   shows / a corresponding increase." The errata replacement covers the whole clause, including the second line's "a
   corresponding increase.". The unit now reads "(from left to right in the diagram) the drag coefficient shows a
   corresponding increase." (lines 136-137). This is word for word the errata text. Only "top to bottom" changed; the
   rest of the sentence ("Furthermore, as the ``degree of bluntness'' increases") is kept.
2. **Item 5, the note.** The \ednote comes after "increase." in the prose paragraph, not in a display or a caption, so it
   is legal under section 9. It reads: "Corrected per the 1973 errata sheet; the shapes of Figure 29 stand side by side,
   their drag coefficients rising from left to right. The 1973 text read ``(from top to bottom in the diagram) the drag
   coefficient shows a corresponding increase.''"
   - The quotation matches PDF 414 and git HEAD exactly.
   - The explanation matches PDF 413. The seven nose shapes stand in one row, and the printed values are
     C_Do = -.05, +.01, .20, .20, .34, .90, 1.0. They never fall from left to right, so "rising" is fair; the one tie is
     .20/.20.
   - The Decisions ask for an \ednote on item 5 because it changes the meaning, and the unit has one.
3. **D8.** PDF 425 prints "base pressure" P_b with a capital typewriter P. Equations (121)-(122) and the Symbols list
   (ch3-symbols.tex line 134, `$p_b$ & base pressure`) have $p_b$. STYLE.md section 14 says "Pressure is lowercase p
   (... `p_b` ...)". The caption now has `$p_b$` (line 415), with no \edcap, as the Decisions require for this case
   slip. The "P_b" inside the Figure 33 artwork stays in the image (section 7), which is correct. A grep finds no `P_b`
   left in any ch3 unit.
4. **D28, the 1973 reading and the claim.** PDF 423 reads "base pressures act along the drag axis and the second term in
   equation (28) may be written simply as (121) D_b = -∬_{S_b} p_b dS_b". PDF 336 prints (28) as
   D_p = -∬_{S_b} p cos(n,V) dS_b - ∬_{S_s} p cos(n,V) dS_s. So the base integral is the first term and the foredrag
   integral over S_s is the second, as the note says. On the base, n is parallel to V, so cos(n,V) = 1 and the first
   term reduces to (121). "Restates" is therefore accurate. This claim needs no arithmetic.
5. **D28, the note's style.** It now follows the Chapter 2 doubt-note pattern:
   - what is printed: "The 1973 text reads ``the second term in equation (28)''", an exact quote of PDF 423;
   - what is meant, and why;
   - "Neither the errata nor the supplements correct this; the text is kept as printed."

   That last statement is true: the errata sheets and supplements have no p. 391 entry. The note is in the sentence
   that introduces display (121), outside the display, so it is legal under section 9. The text itself still reads
   "second term", kept as printed, as the Decisions require. The note uses `$S_b$` and `$S_s$`, which are the section 14
   forms.
6. **Scope.** The only other hunk is a header comment (lines 3-4) that lists the corrections applied, as the Chapter 2
   units do. Nothing outside the three items changed. No equations or labels were touched: ch3:eq:121 and ch3:eq:122
   are unchanged, and nothing needed an n-label. No \draftnote remains.
7. **Rendering.**
   - Page 2 shows the corrected clause with E1 and the full note in the footnote area.
   - Page 8 shows "the second term in equation (??)E2" and the E2 note.
   - Page 9 shows the Figure 33 caption with an italic lowercase p_b.

   The "(??)" for ch3:eq:28 is a cross-unit reference (the label is defined in ch3-sec2b.tex). It was already there
   in HEAD, and STYLE.md section 6 tolerates it in a standalone unit build. The log has no overfull boxes and no
   warnings other than the undefined references.

Outside the unit, and not a discrepancy: the Status column of corrections/ch3.md still shows item 5 and D8 as "todo" and
D28 as "\ednote in place (faithful pass)". The step that records the statuses should update them.

## Discrepancies

none

| where | expected (source/1973) | found | severity |
|---|---|---|---|
| none | | | |
