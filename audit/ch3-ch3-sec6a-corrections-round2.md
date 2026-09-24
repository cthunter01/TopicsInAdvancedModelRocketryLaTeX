# Audit: ch3-sec6a corrections, round 2

Unit: `chapters/ch3-sec6a.tex` (Sections 6, 6.1, 6.1.1 and 6.1.2; PDF 461-474, book pp. 429-442).
Baseline: git HEAD 7e2087d (the faithful 1973 transcription). I inspected the whole of `git diff HEAD -- chapters/ch3-sec6a.tex`.
It has three hunks: (161) at line 62, E1 at lines 90-99 and E2 at lines 336-347. Nothing else in the file changed.

Items: D5 (silent case fix, as the Decisions of 2026-09-24 in corrections/ch3.md direct), D18 (note) and D19 (note).

## Sources read (this round)

- 1973 pages: PDF 463 (p. 431: (158)-(162)), PDF 465 (p. 433: the repeated fin equation), PDF 470 (p. 438: (169)-(170)),
  PDF 471 (p. 439: (171a)-(171e)) and PDF 473 (p. 441: (172a)-(172b), (173)).
- Errata: PDF 664 and PDF 665 (a second typing of the same list). Their Chapter 3 entries are pp. 268, 270, 342, 364, 382, 401 and 480.
  None touches pp. 431, 433 or 441. Both sheets name the book, its three authors (Mandell, Caporaso, Bengen) and "The MIT Press, 1973".
  Neither shows who wrote the errata or a date.
- Supplement pages, PDF 688-698, all read:
  - 688-689: replacement p. 356 and the top of p. 357.
  - 690: Section 5.2.2, (144A)-(144B) and e = 0.863.
  - 691-693: Section 5.3, new (152)-(156).
  - 694: the eight Symbols-list entries.
  - 695: p. 445 (the factor 4).
  - 696: p. 449.
  - 697-698: p. 451 and the top of p. 452.

  None touches pp. 431, 433 or 441. No page shows an author, signature or date. The only headings are the section titles, the
  page numbers -356-, -357-, -445-, -449-, -451- and -452-, and the numbers 2 and 3 on the fin-cant pages. PDF 692 converts
  (C_Di)_twist from fin area to S_m by multiplying by S_F/S_m. PDF 697 computes (C_Do)_F with 63/2.92 and adds it to the body
  terms with no further factor (.149 + .075 + .381 = .605). Both agree with the reasoning of E1.

## Round-1 findings

1. **E2, l. 343 (the cylinder value).** Fixed. It now reads "gives 0 instead of the $4\ell_T/d_m$ that equation~\eqref{ch3:eq:170}
   gives for a cylinder of that length". (170) on PDF 470 prints 4 l_b/d_m, so the value for a cylinder of length l_T is 4 l_T/d_m.
   The wording matches the D20 note in ch3-sec6c.
2. **E2, l. 344-346 (the pointed cone).** Fixed. It now reads "for a pointed cone ($d_b = 0$) either sign reduces (172a) to (171d)
   and (172b) to (171e)". Redone: with d_b = 0, (172a) = 2(l_T/d_m) sqrt(1 + d_m^2/4l_T^2) = 2 sqrt(1/4 + (l_T/d_m)^2), which is
   (171d) with l = l_T. (172b) = 2 l_T/d_m, which is (171e), and its side condition 2l_T/d_m >> 1 is the same. Correct.

## Checks

1. **D5, (161), l. 62.** PDF 463 prints a lowercase b in (C_f)_b. The capital B of (C_Do)_B in (160) on the same page is
   clearly different, and round 1 confirmed the reading at 300 dpi. (166), the where-list (l. 213), (174) and the Symbols
   list (`$(C_f)_B$ & skin friction coefficient of body`) all have (C_f)_B. The line now reads `(C_f)_B`, with no note, as the
   Decisions direct. `(C_{Df})_b` on the left of (161) and inside (162) is correctly left lowercase. Nothing else in (161)-(162)
   changed.
2. **D18, E1 (l. 90-99).** It is placed after "which we repeat here for convenience:" and before `equation*`, outside any math
   environment, which section 9 allows. Its claims:
   - PDF 463 prints (159) with no S_F/S_m, and PDF 465 prints the repeated form with S_F/S_m. The note states this accurately.
     Both displays are kept as printed.
   - (159) is "derived in Section 3.6, equation (108)". The text before (108) (ch3-sec3c-sec4a l. 115) calls it the fin drag
     coefficient "based on fin planform area". (158) multiplies (C_Do)_F by S_F/S_m, so with the repeated form the area ratio
     would count twice. This is correct.
   - "The rest of the chapter uses the repeated form...":
     - ch3-sec6b Step 3 (l. 97) uses the repeated form, and its totals (.279 + .055 + .190, .194 + .066 + .190) add (C_Do)_F with no factor.
     - The p. 451 replacement (PDF 697) does the same.
     - (205) is `(C_{Df})_b + C_{Db} + (\CDo)_F`, where (201) = (16/pi)(C_f)_F(c/d_m)(b/d_m)(1 + 2t/c) is the repeated form with
       (190) S_F/S_m = (8/pi)(c/d_m)(b/d_m).
     - (178) lists S_F/S_m among the arguments of (C_Do)_F.
     - (163) also has /S_m.

     The claim is correct.
   - Closing sentence: "Neither the errata nor the supplements correct this; the equations are kept as printed." Both halves
     are accurate (see above).
3. **D19, E2 (l. 336-347).** It is placed after "is given by", before the subequations, which is legal.
   - 1973 reading, checked symbol by symbol against PDF 473:
     (172a) = `2(d_m - d_b) l_T / d_m^2 sqrt(1 + ((d_m - d_b)/2l_T)^2)` and (172b) `≅ 2(1 - d_b/d_m) l_T/d_m`, for
     2l_T/(d_m - d_b) >> 1. The note's description ("a minus sign in the leading factor: (d_m - d_b) before the radical in (172a),
     (1 - d_b/d_m) in (172b)") is accurate. The (d_m - d_b) inside the radical and in the side condition is correct and is not
     called into question. Both equations are kept as printed.
   - Arithmetic, redone:
     - The lateral area of the frustum is pi(r_m + r_b) x slant = [pi(d_m + d_b)/2] x l_T sqrt(1 + ((d_m - d_b)/2l_T)^2).
     - Divided by pi d_m^2/4, this gives 2(d_m + d_b) l_T/d_m^2 x sqrt(...).
     - In the limit of (172b) it gives 2(1 + d_b/d_m) l_T/d_m.
     - For a cylinder (d_b = d_m), the printed sign gives 0 in both equations and the corrected sign gives 4 l_T/d_m, as (170) does.
     - For a pointed cone, see finding 2 above.

     Every statement in the note is correct.
   - Consistency: the parallel D20 note in ch3-sec6c (l. 76-84) agrees in its facts and wording. (172a)-(172b) are not used
     elsewhere in the chapter (grep of ch3-sec6b, ch3-sec7, ch3-sec8). The GCR carry-over belongs to D20.
4. **Scope.** The diff contains only the three item hunks. No other prose, math, label or comment changed.
5. **Labels.** No equation was added, removed or renumbered. ch3:eq:158-163, ch3:eq:172, ch3:eq:172a and ch3:eq:172b are kept.
   The labels the notes cite (ch3:eq:108, 158, 159, 170, 171d, 171e, 172a, 172b, 205 and ch3:sec:6.2) exist in the chapter's units.
6. **Section 14 notation** in the changed passages: `(C_f)_B` (italic outer capital), `(C_{Df})_b`, `\CDo`, `S_F/S_m`, `S_m`,
   `\ell_T`, `d_m` and `d_b` are all as listed. The notes' "in~\eqref{...}" without the word "equation" follows existing
   Chapter 2 editorial notes (ch2-sec4).
7. **Rendering.** build/unit/ch3-sec6a.pdf and the PNGs were built at 09:39:30-34, after the last edit to the .tex at 09:39:28.
   The log has no overfull or underfull boxes. Its only warnings are cross-unit undefined references, which the standalone
   build tolerates.
   - Page 1: (161) shows (C_f)_B, and (162) shows (C_Df)_b.
   - Page 2: the E1 mark follows "convenience:" and the footnote is complete.
   - Page 6: the E2 mark follows "is given by". The footnote is complete and shows the round-1 fixes. (172a)-(172b) render as printed.

Observation, outside this unit's diff: in corrections/ch3.md the Status cells of D5, D18 and D19 still read todo/note.
No unit's row has been updated yet, so this is presumably done when the checklist is consolidated.

## Discrepancies

none
