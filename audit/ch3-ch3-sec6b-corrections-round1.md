# Audit: corrections applied to chapters/ch3-sec6b.tex, round 1

Scope: items 12, 13 and 14 and the check item D26 of corrections/ch3.md, as applied in the working tree
(`git diff HEAD -- chapters/ch3-sec6b.tex`; HEAD = 7e2087d, the faithful 1973 transcription).

## Sources read

| PDF | document | author / date shown |
|---|---|---|
| 664 | 1973 errata sheet ("ERRATA / TOPICS IN ADVANCED MODEL ROCKETRY by Gordon K. Mandell, George J. Caporaso, and William P. Bengen (Cambridge, Massachusetts: The MIT Press, 1973)") | no author or date beyond the book citation; its Chapter 3 entries (pp. 268, 270, 342, 364, 382, 401, 480) do not touch this unit (printed pp. 443-453) |
| 695 | supplement page "-445-" (factor 4) | none |
| 696 | supplement page "-449-" (one line) | none |
| 697-698 | supplement replacement page "-451-" and top of "-452-" | none |
| 476, 477, 478, 479, 480, 481, 482, 483, 484 | 1973 pages (Figure 48; p. 445; pp. 446-447 fin dimensions; Figure 49; p. 449; p. 450; p. 451; p. 452) | - |

Zoomed renders (build/zoom/auditcorr_ch3-sec6b_r1-*): Figure 48 fin region (PDF 476, 400 and 600 dpi), Figure 49b
(PDF 480), supplement Step 3 (PDF 697, confirms 3.03 x 10^4, .00763, .381). Rendered pages build/unit/ch3-sec6b-2..6.png
are newer than the .tex file (09:35:58 against 09:35:51) and were inspected.

## What was checked

1. **Item 12 (PDF 695, p. 445 / PDF 477).** The third member now reads `4\,\frac{22.61}{1.93}`, symbol by symbol as on
   PDF 695 (4, 22.61, 1.93, 46.9; first and second members unchanged). 4 x 22.61/1.93 = 46.86 = 46.9, so the result
   does not change. The \ednote (E1) is in the sentence that introduces the display. It quotes the 1973 display as
   `(S_s/S_m)_CYL = 4 l/d_m = 22.61/1.93 = 46.9`, which matches PDF 477 and HEAD. Only this display changed on the page. Rendered page 2 is correct.
2. **Item 13 (PDF 696, p. 449 / PDF 481).** "From equation (100) we find $B = 1735$. Then, since $R_\ell = 1.27 \times 10^{6}$,"
   matches the supplement's wording and punctuation. Applied silently, as the item says. Rendered page 5 is correct.
3. **Item 14 (PDF 697-698, pp. 451-452 / PDF 483-484).** Extent: PDF 483 runs from the "Step 1" heading to
   $(C_{D_0})_{FB} = .570$, and the top of PDF 484 is "This is a substantial disagreement with the experimental result
   -- almost 36%." The replacement covers exactly that. "And yet the Mercer data should be closer ..." and everything after it on PDF 484 are unchanged
   (compared line by line with HEAD). Every replaced display and sentence was compared with PDF 697-698:
   - Step 1: $(C_f)_B = (C_f)_{\mathrm{LAM.}} = 1.328/\sqrt{31.75\times10^4} = .00236$; $(C_{Df})_b = .00236\times1.055\times59.7 = .149$;
     "This represents a decrease of 0.045, or 23.2%, from the transition-flow calculated value of $(C_{Df})_b$." ("calculated"
     is new in the supplement and is present).
   - Step 2: $C_{Db} = .029/\sqrt{.149} = .075$; "This is an *increase* of 0.009, or 13.6% over the transition-flow calculated
     value." (underline set as \emph).
   - Step 3: $(C_f)_F = 1.328/\sqrt{3.03\times10^4} = .00763$; $(\CDo)_F = 2\times.00763\times1.158\times63/2.92 = .381$; "This is
     an increase of 0.191, or *more than double* the value calculated for 60 meters/second." (the three separately underlined words set as one \emph).
   - "From these calculations we obtain an overall drag coefficient of" and $(\CDo)_{FB} = .149 + .075 + .381 = .605$.
   - Top of p. 452: "This is a substantial disagreement with the experimental result---the calculated value exceeds the
     measured value by more than 44%."
   Arithmetic, redone: 1.328/sqrt(317500) = .002357; .00236 x 1.055 x 59.7 = .1486; .194 - .149 = .045 = 23.2% of .194;
   .029/sqrt(.149) = .0751; .075 - .066 = .009 = 13.6% of .066; 1.328/sqrt(30300) = .007629; 2 x .00763 x 1.158 x 63/2.92
   = .3813; .381 - .190 = .191 (ratio 2.005); .149 + .075 + .381 = .605; .605/.42 = 1.4405 (44.0%). Every supplement
   value is right.
   \ednote E3: placed in the sentence that introduces the first display (section 9). It quotes all six replaced 1973
   displays in full and the four changed sentences. Each quotation was checked against PDF 483-484 and HEAD and is
   accurate. The sentences it calls unchanged (the step headings, "The body skin-friction coefficient is given by",
   "so the forebody drag coefficient is", "The fin skin-friction coefficient is", "Then", "From these calculations ...")
   are unchanged. The one inaccuracy is its causal sentence (see the table).
4. **D26 (PDF 476, 478-480).** Figure 48 labels 3.30 (from the fin's leading edge to the base of the body), 4.19 (span), 1.91 (from the leading edge to the tip
   chord), 2.07 (tip chord) and 0.68 (the height of the trailing-edge chamfer). The figure agrees with itself: 1.91 + 2.07 = 3.98 = 3.30 + 0.68,
   and the text's root chord 3.97 matches to the last digit. Figure 49b shows region III as the in-body strip between the axis and the body surface,
   from the root leading edge down to the body base (the hatching ends at the base, while region II runs on to the
   trailing edge). Its length should therefore be the 3.30 of Figure 48, but the text prints 3.21. No decomposition of the labelled
   dimensions gives 3.21, so this is a real conflict and not a different decomposition of the same fin. The \ednote (E2) is attached to
   "Following Figure 49b, then," (legal placement). Its statements are supported: 1.93/2 = 0.965; 3.30 x 0.965 = 3.18;
   3.98 + 8.68 + 3.18 = 15.84; 4 x 15.84 = 63.4, so still about 63; the only other difference is 1.90 against 1.91.
   It ends with "Neither the errata nor the supplements correct this ...", as required.
5. **Scope.** The diff has four hunks: item 12, the D26 note, item 13 and item 14. Nothing else changed.
6. **Labels.** The unit has no numbered equations, and no labels or \tag were added or removed.
7. **Section 14 notation** in the corrected passages and notes: `(C_f)_{\mathrm{LAM.}}`, `(C_{Df})_b`, `C_{Db}`, `(\CDo)_F`,
   `(\CDo)_{FB}`, `(C_f)_B`, `(C_f)_F`, `\ell`, `d_m`, `\mathrm{CYL}`, leading-dot decimals. All correct.
8. **Renders.** Page 2 (item 12 and E1), page 3 (E2), page 5 (item 13 and E3), page 6 (Steps 1-3, total, the 44% sentence)
   all show the corrected text correctly. In E3 the radical bars of the inline square roots come close to the
   descenders of the line above ("page 451"). This is TeX's normal minimum line spacing and nothing overlaps, so it is not listed.
   (The unresolved "??" references come from the standalone unit build and are expected.)

## Discrepancies

| where | expected (source/1973) | found | severity |
|---|---|---|---|
| ch3-sec6b.tex l. 227-228, \ednote E3 ("The 1973 value of $(C_f)_B$ does not follow from its formula ..., and the figures after it were computed from it.") | Only the Step 1-2 figures and the total depend on $(C_f)_B$. The Step 3 figures do not: the supplement changes them because it recomputes the fin Reynolds number as $3.03\times10^4$ (15 x .0302/1.495e-5 = 30,301). The 1973 display had $3.02\times10^4$, and the unchanged text on PDF 482 (l. 220, "$R_c = 3.02 \times 10^{4}$") still does. The 1973 .00765 and .380 were themselves off by a digit (1.328/sqrt(30200) = .00764; 2 x .00765 x 1.158 x 63/2.92 = .382). Suggested wording: "... and the figures of Steps 1 and 2 and the total were computed from it. In Step 3 the supplement also takes $R_c = 3.03\times10^{4}$ ($15 \times .0302/1.495\times10^{-5}$), where the text above gives $3.02\times10^{4}$." | The note says every later figure was computed from the wrong $(C_f)_B$. The reader is not told why the fin values change, or why the corrected passage uses 3.03 x 10^4 right after the text's 3.02 x 10^4. | note |
