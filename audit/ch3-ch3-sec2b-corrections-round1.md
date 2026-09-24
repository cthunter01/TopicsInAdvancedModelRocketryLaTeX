# Audit: corrections applied to chapters/ch3-sec2b.tex (round 1)

Unit: `chapters/ch3-sec2b.tex` (2.2-2.3, PDF 324-340). Diff audited: `git diff HEAD -- chapters/ch3-sec2b.tex`.
It has two hunks, 7 insertions and 4 deletions, against HEAD 7e2087d, the faithful transcription. The build audited is
`build/unit/ch3-sec2b-1.png` to `-8.png` with `ch3-sec2b.pdf`. It was built at 09:33:11 from the .tex saved at
09:33:05, so the build is current. Rules read: STYLE.md sections 4, 6, 8, 9, 10, 11 and 14, and corrections/ch3.md,
including the "Decisions for the corrections step (2026-09-24)" block.

Items to apply:
- **D7** (PDF 334): set $p_{\mathrm{tot}}$ for the typed $P_{\mathrm{tot}}$, with no note (Decisions: a case slip
  for the same quantity).
- **D27** (PDF 333): bring the existing stale-reference note on "(2.20)" and "(2.18)" into the doubt-note style.

## Sources and their authors and dates

- 1973 pages: PDF 333 (printed p. 301) and PDF 334 (printed p. 302), both read in full. I also made a 300 dpi zoom of
  the "P_tot" line on PDF 334: `build/zoom/audit_ch3-sec2b_corr_r1-ptot-334-334.png`.
- 1973 errata sheet, PDF 664: headed "ERRATA" and the book's citation (Mandell, Caporaso and Bengen, MIT Press,
  1973). It shows no author of the sheet and no date. Its Chapter 3 entries are pp. 268, 270, 342, 364, 382, 401 and 480.
  None is for p. 301 or p. 302.
- The Chapter 3 supplement pages, PDF 688-698. All were read. None shows an author or a date.
  - PDF 688-689 are the replacement pp. 356-357.
  - PDF 690 is Section 5.2.2, p. 412.
  - PDF 691-693 are Section 5.3, pp. 422-424.
  - PDF 694 is the eight symbol-table entries. None of them is $p_{\mathrm{tot}}$.
  - PDF 695-698 are pp. 445, 449 and 451-452.
  - None of these pages touches p. 301 or p. 302.

## What was checked

1. **D7, the 1973 reading.** The zoom of PDF 334 shows a capital typewriter "P" (cap height, no descender) with the
   subscript "tot": "the total pressure P_tot is a constant". The hand-lettered (22) prints $p_{\mathrm{tot}}$, and so
   does (23) on PDF 335. The Symbols list has `$p_{\mathrm{tot}}$ & total pressure` (ch3-symbols.tex line 126).
   STYLE.md section 14 says "Pressure is lowercase p (... `p_{\mathrm{tot}}` ...)". So this is a case slip for the
   same quantity. Under the Decisions it is set silently.
2. **D7, as applied.** Line 275 now reads `$p_{\mathrm{tot}}$`: lowercase p and an upright "tot", the same form as
   (22)-(23). There is no \ednote, as the Decisions require. It was the only capital-P pressure in the unit. A grep
   finds no `P_` left in ch3-sec2b.tex.
3. **D27, the 1973 reading.** PDF 333 reads "Comparison of equation (2.20) with equation (2.18) reveals that k is just
   equal to ½ρC_DA_r". The note quotes ``equation (2.20)'' and ``equation (2.18)''. These quotes are accurate. The
   text keeps both references typed literally, as printed, as STYLE.md section 6 requires for a stale reference.
4. **D27, the note's claims.**
   - "Section-prefixed numbers that the chapter uses nowhere else": a grep of all chapters/ch3-*.tex for
     "(N.N)" and "equation N.N" finds only this sentence. The other matches are numbers inside formulas, such as
     .55(8.9) and (1.03)^2. The claim is true of the transcription.
   - "The first is the D = kV^2 just given": (20) is D = kV^2, directly above.
   - "The second defines C_D": (18) is C_D = D/(½ρV^2 A_r).
   - "Together they give k = ½ρC_D A_r": I redid the algebra. From (18), D = ½ρC_D A_r V^2. Comparing this with
     D = kV^2 gives k = ½ρC_D A_r. This is correct.
   - "Neither the errata nor the supplements correct this": confirmed from PDF 664 and PDF 688-698 (see above).
5. **D27, style.** The note follows the Chapter 2 doubt-note pattern, for example ch2-sec3a.tex lines 412-416 (a
   stale-reference note). It gives what is printed ("The 1973 text reads ..."), then what is evidently meant and why,
   and it ends "Neither the errata nor the supplements correct this; the references are kept as printed." The old
   wording ("The typescript's ... are ...; elsewhere the chapter cites ...") is fully replaced, and it now names the
   probable targets with `\eqref`, as section 6 requires.
6. **Placement** (section 9). The note stays in the prose sentence, after "(2.18)", before "reveals". It is not
   inside a display, a caption or a table.
7. **Scope** (the whole diff). There are only the two hunks: the rewritten note text and the one symbol change at
   line 275. Nothing else in the unit changed. The only change in corrections/ch3.md is the added Decisions block.
8. **Labels.** No label was added, removed or retagged, and the unit has no new equations. `\eqref{ch3:eq:20}` and
   `\eqref{ch3:eq:18}` are labels in this unit and resolve in the build. The log's undefined references are all in
   other units (ch2, ch3:eq:12b, ch3:fig:12, ch3:ref:14/15/17, ch3:sec:3-6), which is expected in a unit build.
9. **Notation** (section 14). $p_{\mathrm{tot}}$ matches the list. In the note, `\CD`, $A_r$ and `\tfrac{1}{2}` match
   the prose.
10. **Rendering.** `build/unit/ch3-sec2b-5.png`:
    - The E1 marker follows "equation (2.18)", and the footnote is complete at the foot of the same page. Its
      "(20)" and "(18)" are live references.
    - The Bernoulli sentence shows an italic lowercase $p_{\mathrm{tot}}$ with an upright "tot", identical to (22)
      and (23) below it.
    - Nothing is clipped or overfull.

Side observation, not a discrepancy in the unit: the D7 row in corrections/ch3.md still reads "todo", and the D27
row still reads "\ednote in place (faithful pass, stale reference)". They should read "applied silently
(ch3-sec2b, line 275)" and "applied (\ednote reworded to the doubt-note style, after "(2.18)" on PDF 333)" when the
checklist is updated.

## Discrepancies

none
