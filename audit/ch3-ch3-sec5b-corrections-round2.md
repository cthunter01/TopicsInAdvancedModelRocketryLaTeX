# Audit: corrections applied to chapters/ch3-sec5b.tex (round 2)

Scope: `git diff HEAD -- chapters/ch3-sec5b.tex` (HEAD = 7e2087d, the faithful 1973 transcription), read in full
together with the current file (lines 1-80 and 200-400). Checked against:
- the errata sheet (PDF 664);
- the supplement "Corrections to drag due to fin cant in Chapter 3, Section 5.3" (PDF 691-693), with a 300 dpi
  zoom of the small-angle lines on PDF 691 (build/zoom/audit_ch3-sec5b_r2-p691-691.png);
- the 1973 pages PDF 449, 454, 455 and 456;
- Chapter 2 as now printed (chapters/ch2-sec6.tex, Section 6.3, and its notes quoting the 1973 (115)-(117);
  chapters/ch2-sec4.tex (90), unchanged since fe208b8);
- STYLE.md sections 3, 4, 8, 9, 10, 11 and 14, and corrections/ch3.md;
- the rendered pages build/unit/ch3-sec5b-2.png and -4.png to -7.png. They were built at 09:49:07, after the last
  edit to the .tex at 09:49:05. I did not rebuild.

## Authors and dates shown by the sources

- **Errata sheet (PDF 664).** It is headed "ERRATA / TOPICS IN ADVANCED MODEL ROCKETRY by Gordon K. Mandell,
  George J. Caporaso, and William P. Bengen (Cambridge, Massachusetts: The MIT Press, 1973)". The sheet itself
  has no author and no date. Its Chapter 3 entries (pp. 268, 270, 342, 364, 382, 401, 480) are all outside this
  unit (printed pp. 414-429).
- **Supplement (PDF 691-693).** It gives a title only, with the bracketed instructions "[Replace text starting
  with equation (152) on page 422 of the original book, with the following:]" and "[Continue with the sentence
  beginning with "Furthermore...." on page 424 of the original book.]". Pages 2 and 3 carry page numbers only.
  There is no author, signature or date. E3 names the document by its title, which is correct.

## Round 1 findings: re-verified

1. **E2 (the D25 note), first sentence: fixed.** The overstatement "Bengen evaluated these equations in their
   1973 form" is gone. The note now says that .1672 follows from the 1973 form of (115), with k_r computed as in
   the corrected (116), and that these give 0.169 U theta. It adds that with the 1973 (116), which prints (tau+1),
   the 1973 (115) gives 0.0505 U theta. I recomputed each value for s = c_r = c_t = 2.54, r_t = 1.03, lambda = 1:
   - tau = 3.4660, Ybar_T = 2.30 from (90), k_d = 1.12920;
   - k_r = 0.93633 with (tau^2+1), and 0.27951 with the 1973 (tau+1);
   - the corrected (115) gives 0.327260 U theta, which is the supplement's 0.327259;
   - the 1973 (115) with the corrected k_r gives 0.1691 with A_r = pi r_t^2, or 0.1689 with A_r = 3.33;
   - the 1973 (115) with the 1973 k_r gives 0.0505.

   The note's structural claim is also right: the 1973 (115) has 12 A_r/(s c_r) where the corrected one has
   6(1+lambda). (90) and (117) are unchanged, as the note says (ch2-sec4.tex, and the Chapter 2 note on (117)).
   On whether the replaced (152) is consistent with either form, the note gives what the arithmetic supports:
   (152) is the corrected form, and the 1973 forms give 0.169 or 0.0505.

   Remark, not a discrepancy: "follows from" allows for a gap of about 1% (.1672 against 0.169). The note prints
   both numbers, and every other combination of forms is far off (0.0505, 0.0977, 0.327). So the identification
   is sound.
2. **The small-angle approximation (l.280-283): fixed.** It now runs on in the text line, as on PDF 691:
   "For arctan(...) <= about 15 deg (= 0.262 radian), or (...) <= about 0.268, arctan(...) ≅ omega_Z r/U. That
   is, ...". The rendered page 5 is correct.

   Remark: the zoom shows no period after the final omega_Z r/U on PDF 691 (the formula ends the typed line,
   and a blank line and "That is," follow). The transcription adds the period that the inline setting needs.
   This is an obvious completion of punctuation (STYLE.md section 3), and it changes no wording.

## What else was checked

3. **Item 10, extent.** The 1973 text replaced runs from (152) on PDF 454 through "...by which rotation is
   induced are considerable." on PDF 456. None of it is left behind. Three things are unchanged:
   - the sentence before (152) ("According to equations (90), (115), (116), and (117) of Chapter 2, canting the
     fins ... determined by");
   - "Furthermore, ..." and everything after it, re-wrapped only;
   - Section 5.4 with its 1973 (155) and (156).
4. **Item 10, prose, sentence by sentence against PDF 691-693.** Every sentence matches. That includes:
   - *less*, *average* and *aerodynamic twist* emphasized, as underlined in the supplement;
   - "Hoerner~(\ref{ch3:ref:9})", the unit's own form (l.12), with Reference 9 = Hoerner, *Fluid-Dynamic Drag*;
   - the roll damping sentence, with equation~\eqref{ch2:eq:115} of Chapter~\ref{ch2} and (152) as links;
   - "two diametrically opposed fins ... 6.51 alpha^2";
   - "From equation (147), ... 4 canted fins as";
   - the closing paragraph with 0.75, 2.46%, 9.84%, the triple-spin sentence with 22.14%, and "may be
     considerable".

   Paragraph breaks follow the supplement's indents: new paragraphs at "For the simple", "The linear variation",
   "From equation (147)" and "The total drag increase". There are run-ons after the displays at "without
   significant", "which, for", "The average effective", "Then" and "If the rocket's". "Then", which the
   typescript prints beside the display, is a prose line (STYLE.md section 4).
5. **Item 10, equations symbol by symbol.** All match the supplement:
   - (152) omega_Z = 0.327259 U theta;
   - alpha(r) = theta - arctan(omega_Z r/U), unnumbered;
   - (153) alpha(r) = theta - omega_Z r/U, with "radian" after `\qquad`;
   - alpha-bar = (0.05093 - 0.00857)/2 = 0.02118 radian;
   - (154) (C_Di')_cant = 13.02 alpha-bar^2;
   - (C_Di)_twist = (4 x 10^-5)(Delta alpha)^2, "for Delta alpha given in degrees";
   - (C_Di)_twist = 0.1313 (Delta alpha)^2;
   - the three-line align: 4(3.57 x 2.54)/(pi(1.03)^2), then 10.8828 (C_Di)_twist, then (155′) 1.43 (Delta
     alpha)^2;
   - (Delta C_Di)_cant = 2(8.38 alpha-bar^2) = 16.76 alpha-bar^2;
   - (156′) (Delta C_D)_cant = (C_Di')_cant + (C_Di')_twist + (Delta C_Di)_cant;
   - (13.02 + 16.76) alpha-bar^2 + 1.43 (Delta alpha)^2;
   - Delta alpha = 0.05093 - (-0.00857) = 0.0595 radian;
   - 0.018433.

   The intermediate displays are unnumbered.
6. **The supplement's arithmetic, redone.**
   - 100/(0.327259 x 6000) = 0.050928 rad, which is 2.9180 deg.
   - The tip is at r = 1.03 + 2.54 = 3.57, which gives -0.008572.
   - tan 15 deg = 0.2679 and 15 deg = 0.2618 rad.
   - 4e-5 (180/pi)^2 = 0.13131.
   - S_F/S_m = 10.8827, and 0.1313 x 10.8827 = 1.4289.
   - 2 x 6.51 = 13.02 and 2 x 8.38 = 16.76.
   - The total recomputes to 0.018422 against the printed 0.018433. The percentages recompute to 2.456%, 9.82%
     and 22.11%; the supplement's 9.84 and 22.14 are 4 x 2.46 and 9 x 2.46.

   These are last-digit differences with no effect on the conclusion. Under the D35 policy no note is needed, and
   none was added.
7. **E3 (the item 10 note).**
   - Placement: after "determined by", in the sentence that introduces (152), outside any display (section 9).
   - Quotes: the 1973 (152), (153), the alpha-bar display and (154) with ≅ 12.5 match PDF 454-455. So do the four
     quoted sentence groups: the 0.1-radian sentence, the root/tip pair, the 6.24 alpha^2 sentence and the whole
     closing paragraph through "are considerable". The quoted "(C_Di')_c" is as printed.
   - Its list of what is new, and of what is only reworded, is accurate.
   - The (155′)/(156′) explanation is correct. The 1973 (155) and (156) of Section 5.4 keep ch3:eq:155 and
     ch3:eq:156, and the aux shows both on page 7 with distinct anchors.
8. **E1 (D17).**
   - (144) + (145) = 8.45 alpha^2 + 8.86 alpha^3, which exceeds 8.38 alpha^2 for every alpha > 0.
   - 8.38 alpha^2 exceeds 1.94 alpha^2 + 8.86 alpha^3 below 41.6 deg, and exceeds 6.51 alpha^2 always. So it is
     larger than either term over Table 4's 0.5-10 deg.
   - At 10 deg: 0.1062 + 0.1983 = 0.3045 against 0.2553. This matches the table's .106, .198 and .255.
   - The sentence on PDF 449 is kept as printed, with *sum* emphasized. The note uses the Chapter 2 closing
     formula.
9. **Nothing outside the items changed.** The diff has exactly three hunks, for E1, E2 and item 10.
10. **Labels.**
    - ch3:eq:152-154 stay on numbered `equation`s.
    - The new (155′) is `\tag` in `align*`, labelled ch3:eq:n155 (anchor AMS.6).
    - The new (156′) is `equation*` + `\tag`, labelled ch3:eq:n156 (anchor AMS.7).
    - This follows STYLE.md section 4 and the Chapter 2 (89′)-(92′) precedent.
11. **Section 14 notation.** It is used throughout:
    - `\omega_Z`, `\theta`, `\arctan`, `\cong`, `\bar{\alpha}`, `\Delta\alpha`;
    - `(C_{Di}')_{\mathrm{cant}}`, `(C_{Di})_{\mathrm{twist}}`, `(C_{Di}')_{\mathrm{twist}}`,
      `(\Delta C_{Di})_{\mathrm{cant}}`, `(\Delta\CD)_{\mathrm{cant}}`, `S_F/S_m`, `\CDo`;
    - `\dg`, `\times`, `\un{radian}` on numbers in displays, and `\qquad\text{...}` for words at the right.
12. **Rendered pages.**
    - Page 2 shows E1.
    - Pages 4-5 show E2 (split across the two footnote areas) and E3.
    - Pages 5-7 show (152), the α(r) display, the inline approximation, (153), (154), (155′), (156′) and the
      closing paragraph, all correctly.
    - The only warning is the expected undefined cross-unit references: ch2 equations and section, ch3:ref:9,
      (144), (145) and others.

Remark outside this unit, for the orchestrator: corrections/ch3.md still lists item 10, D17 and D25 as
todo/note. Its Decisions line "Item 10 keeps the labels ch3:eq:152 to ch3:eq:156" should record that 155-156 are
(155′)/(156′) with n-labels.

## Discrepancies

none
