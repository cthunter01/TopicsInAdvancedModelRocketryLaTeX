# Audit: ch3-sec6a corrections, round 1

Unit: `chapters/ch3-sec6a.tex` (Section 6, 6.1, 6.1.1, 6.1.2; PDF 461-474, book pp. 429-442).
Baseline: git HEAD 7e2087d (the faithful 1973 transcription). Diff inspected: `git diff HEAD -- chapters/ch3-sec6a.tex`
(three hunks: line 62, lines 90-99, lines 336-345). Nothing else in the file changed.

Items for this unit: D18 (note), D19 (note), D5 (silent case fix, per the Decisions of 2026-09-24 in corrections/ch3.md).

## Sources read

- 1973 pages: PDF 463 (p. 431: (159)-(162)), PDF 465 (p. 433: the restated fin equation), PDF 473 (p. 441: (172a)-(172b)),
  plus a 300 dpi crop of (161)-(162) (build/zoom/audit_ch3-sec6a_r1-p463-463.png).
- Errata sheet PDF 664: its Chapter 3 entries are pp. 268, 270, 342, 364, 382, 401, 480. None touches pp. 431, 433 or 441.
  The sheet names the book and its three authors (Mandell, Caporaso, Bengen; MIT Press, 1973). It shows no author of the
  errata and no date.
- Supplement pages PDF 688-698 (read: 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698). They cover pp. 356-357,
  Section 5.2.2 (p. 412), Section 5.3 (pp. 422-424), the Symbols list, and pp. 445, 449 and 451-452. None touches
  pp. 431, 433 or 441, so "Neither the errata nor the supplements correct this" is accurate for D18 and D19. No page shows
  an author, signature or date. The only headings are the section titles, the page numbers -356-, -357-, -445-, -449-,
  -451- and -452-, and the numbers 2 and 3 on the fin-cant pages.

## Checks

1. **D5, (161)** (line 62). The 300 dpi crop shows a clear lowercase b in `(C_f)_b` on PDF 463. (166) and the where-list
   have `(C_f)_B`. The Decisions set the Symbols-list form silently. Found: `(C_f)_B`, no note. Nothing else in (161)
   changed: `(C_{Df})_b` on the left and in (162) is correctly left lowercase. Correct.
2. **D18 note** (E1, lines 90-99). It is placed after "which we repeat here for convenience:", in the sentence that
   introduces the display and outside any math environment. That is legal under section 9. I checked each of its claims:
   - PDF 463 prints (159) without S_F/S_m, and PDF 465 prints the repeated form with `\frac{S_F}{S_m}`. The note's
     statement of the 1973 reading is accurate. Both displays are kept as printed.
   - The text on PDF 463 derives (159) from (108), which ch3-sec3c-sec4a says is "based on fin planform area". (158)
     multiplies (C_Do)_F by S_F/S_m. So with the repeated form, (158) would count the area ratio twice. Correct.
   - "The rest of the chapter uses the repeated form...". ch3-sec6b Step 3 (line 97) uses the repeated form, with
     63/2.92 in the numerics. The totals .279 + .055 + .190 and .194 + .066 + .190 add (C_Do)_F with no further
     factor. So do the p. 451 replacement (PDF 697, .149 + .075 + .381) and (205) in ch3-sec6c,
     `(C_{Df})_b + C_{Db} + (\CDo)_F`, where (C_Do)_F is (180), 16/pi (C_f)_F (c/d_m)(b/d_m)..., which already contains
     S_F/S_m. (163) also divides by S_m. The claim is correct.
   - The closing formula follows the Chapter 2 style.
3. **D19 note** (E2, lines 336-345). It is placed after "is given by", before the subequations. That is legal.
   - 1973 reading: (172a) prints `2(d_m - d_b)\ell_T/d_m^2` before the radical, and (172b) prints `2(1 - d_b/d_m)\ell_T/d_m`.
     The radical and the side condition have (d_m - d_b), and that is correct. The note's statement is accurate, and
     both equations are kept as printed. I checked (172a)-(172b) symbol by symbol against PDF 473.
   - Arithmetic, redone. Frustum lateral area = pi(r_m + r_b) x slant = pi(d_m + d_b)/2 x l_T sqrt(1 + ((d_m - d_b)/2l_T)^2).
     Dividing by pi d_m^2/4 gives 2(d_m + d_b) l_T/d_m^2 x sqrt(...). For 2l_T/(d_m - d_b) >> 1 this is
     2(1 + d_b/d_m) l_T/d_m. Correct.
   - Cylinder, d_b = d_m: printed sign gives 0 and corrected gives 4 l_T/d_m. Correct, but (170) prints 4 l_b/d_m (see table).
   - Pointed cone, d_b = 0: (172a) with either sign gives 2 sqrt(1/4 + (l_T/d_m)^2), which is (171d). (172b) gives
     2 l_T/d_m, which is (171e), not (171d). The note's "both signs give equation (171d)" is true of (172a) only (see table).
4. **Scope.** The whole diff contains only the three item hunks. No other text, math or label changed.
5. **Labels.** No equation was added or renumbered. ch3:eq:158-162 and ch3:eq:172, 172a and 172b are kept.
6. **Section 14 notation** in the changed passages: `(C_f)_B` (italic outer B), `\CDo`, `S_F/S_m`, `\ell_T`, `d_m`, `d_b`
   are all as listed.
7. **Rendering.** The build/unit/ch3-sec6a-*.png files were built after the last edit (tex modified 09:35:29, pdf built
   09:35:30):
   - Page 1: (161) shows (C_f)_B.
   - Page 2: E1 is attached after "convenience:" and the footnote is complete.
   - Page 6: E2 is attached after "is given by", the footnote is complete, and (172a)-(172b) render correctly.
   - The ?? marks are cross-unit references, which the standalone build tolerates.

Observation, outside this unit's diff: in corrections/ch3.md the Status cells of D5, D18 and D19 still read todo/note.
Other units' rows are also not yet updated, so this is presumably done when the checklist is consolidated.

## Discrepancies

| where | expected (source/1973) | found | severity |
|---|---|---|---|
| ch3-sec6a.tex l. 343, D19 note (E2) | (170) prints 4 l_b/d_m. For a boattail of length l_T the value is what (170) gives for a cylinder of that length, e.g. "instead of the $4\ell_T/d_m$ that equation~\eqref{ch3:eq:170} gives for a cylinder of that length" (the wording of the parallel D20 note in ch3-sec6c) | "gives 0 instead of the $4\ell_T/d_m$ of equation~\eqref{ch3:eq:170}" | note |
| ch3-sec6a.tex l. 343-344, D19 note (E2) | with d_b = 0, either sign reduces (172a) to (171d) and (172b) to (171e) (2 l_T/d_m) | "for a pointed cone ($d_b = 0$) both signs give equation~\eqref{ch3:eq:171d}", which is true of (172a) only | note |
