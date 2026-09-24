# Audit: corrections applied to chapters/ch3-sec6b.tex, round 2

Scope: items 12, 13 and 14 and the check item D26 of corrections/ch3.md, as they stand in the working tree
(`git diff HEAD -- chapters/ch3-sec6b.tex`; HEAD = 7e2087d, the faithful 1973 transcription). I re-verified the
round 1 finding and then re-ran every check.

## Sources read

| PDF | document | author / date shown |
|---|---|---|
| 664 | 1973 errata sheet ("ERRATA / TOPICS IN ADVANCED MODEL ROCKETRY by Gordon K. Mandell, George J. Caporaso, and William P. Bengen (Cambridge, Massachusetts: The MIT Press, 1973)") | no author or date beyond the book citation. Its Chapter 3 entries (pp. 268, 270, 342, 364, 382, 401, 480) are all outside this unit (printed pp. 443-453). |
| 695 | supplement page "-445-" (the factor 4) | none |
| 696 | supplement page "-449-" (one line) | none |
| 697-698 | supplement replacement page "-451-" and the top of "-452-" | none |
| 477, 479, 480, 481, 482, 483, 484 | 1973 pages: p. 445; p. 447 (fin areas); Figure 49; pp. 449, 450, 451, 452 | - |
| figures/ch3/fig48.png, fig49.png | Figure 48 (fin labels), Figure 49b (regions I-III) | - |

Zoomed renders (build/zoom/audit_ch3-sec6b_r2-*): the Figure 48 fin (3x), Figure 49b (4x), and the E3 note in
build/unit/ch3-sec6b.pdf at 600 and 1200 dpi. build/unit/ch3-sec6b-*.png (09:43:46-48) are newer than the .tex
file (09:43:44), and I inspected them. I did not rebuild.

## Round 1 finding: re-verified, fixed

The round 1 finding was that E3 said every later figure came from the wrong $(C_f)_B$. E3 now reads: "... the
figures of Steps 1 and 2 and the total were computed from it. In Step 3 the supplement also takes
$R_c = 3.03 \times 10^{4}$ ($15 \times .0302/1.495 \times 10^{-5}$), where the text above gives
$3.02 \times 10^{4}$." Checks:
- 15 x .0302 / 1.495e-5 = 30,301, so 3.03 x 10^4.
- The unchanged text on PDF 482 (unit l. 220) gives $R_c = 3.02 \times 10^{4}$.
- The 1973 Step 3 display (PDF 483) used 3.02 x 10^4.
- Steps 1-2 and the total (.570 = .097 + .093 + .380) depend on $(C_f)_B$. Step 3 does not.

The note is now accurate and complete on this point.

## What was checked

1. **Item 12 (PDF 695 against PDF 477).** The display is now
   `4\,\frac{\ell}{d_m} = 4\,\frac{22.61}{1.93} = 46.9`, symbol by symbol as on PDF 695. The first and second members
   are unchanged. 4 x 22.61/1.93 = 46.86, so 46.9 and the numbers do not change (22.61 = 31.75 - 9.14). E1 sits in
   "For the cylindrical body we find from (170)", outside the align (section 9). Its quotation of the 1973 display
   ($4\,\ell/d_m = 22.61/1.93 = 46.9$) matches PDF 477 and HEAD. Rendered page 2 is correct.
2. **Item 13 (PDF 696 against PDF 481).** The line now reads "From equation (100) we find $B = 1735$. Then, since
   $R_\ell = 1.27 \times 10^{6}$,", word for word and with the same punctuation. It is applied silently, as specified.
   Rendered page 5 is correct.
3. **Item 14 (PDF 697-698 against PDF 483-484).**
   - **Extent.** PDF 483 runs from "Step 1:" to $(C_{D_0})_{FB} = .570$. The top of PDF 484 is "This is a
     substantial disagreement with the experimental result -- almost 36%." The replacement covers exactly this.
     From "And yet the Mercer data should be closer ..." to the end of the unit, the text matches HEAD.
   - **Step 1.** $(C_f)_B = (C_f)_{\mathrm{LAM.}} = 1.328/\sqrt{31.75\times10^4} = .00236$ and
     $(C_{Df})_b = .00236\times1.055\times59.7 = .149$. The sentence reads "This represents a decrease of 0.045, or
     23.2%, from the transition-flow calculated value of $(C_{Df})_b$.", with the new word "calculated" present.
   - **Step 2.** $C_{Db} = .029/\sqrt{.149} = .075$. The sentence reads "This is an *increase* of 0.009, or 13.6%
     over the transition-flow calculated value."
   - **Step 3.** $(C_f)_F = 1.328/\sqrt{3.03\times10^4} = .00763$ and
     $(\CDo)_F = 2\times.00763\times1.158\times63/2.92 = .381$. The sentence reads "This is an increase of 0.191, or
     *more than double* the value calculated for 60 meters/second." "Then" is a prose line, as in HEAD (section 4).
   - **Total.** "From these calculations we obtain an overall drag coefficient of" (new paragraph, as on PDF 697),
     then $(\CDo)_{FB} = .149 + .075 + .381 = .605$.
   - **Top of p. 452.** "This is a substantial disagreement with the experimental result---the calculated value
     exceeds the measured value by more than 44%." It opens the paragraph, and the unchanged "And yet ..." follows
     it.
   - **Arithmetic, redone.**

     | quantity | computed | printed |
     |---|---|---|
     | 1.328/sqrt(317,500) | .0023568 | .00236 |
     | .00236 x 1.055 x 59.7 | .14864 | .149 |
     | (.194 - .149)/.194 | .045, 23.2% | 0.045, 23.2% |
     | .029/sqrt(.149) | .07513 | .075 |
     | (.075 - .066)/.066 | .009, 13.6% | 0.009, 13.6% |
     | 1.328/sqrt(30,300) | .0076292 | .00763 |
     | 2 x .00763 x 1.158 x 63/2.92 | .38126 | .381 |
     | .381 - .190 | .191 (ratio 2.005, "more than double") | 0.191 |
     | .149 + .075 + .381 | .605 | .605 |
     | .605/.42 | 1.4405 (44.0%, "more than 44%") | more than 44% |
     | 1973: .570/.42 | 1.357 ("almost 36%") | almost 36% |

   - **E3.** It is placed in "The body skin-friction coefficient is given by", before the first display (section 9).
     It quotes all six replaced 1973 displays in full and the four changed sentences. I checked each quotation
     against PDF 483-484 and HEAD, and each is exact. The sentences it calls unchanged are unchanged: the step
     headings, "The body skin-friction coefficient is given by", "so the forebody drag coefficient is", "The fin
     skin-friction coefficient is", "Then" and "From these calculations ...". Its explanatory statements are
     supported (see the round 1 section above).
4. **D26 (PDF 476, 479, 480; fig48.png, fig49.png).**
   - **Figure 48 labels.** 3.30 is the distance from the root leading edge to the body base. 4.19 is the span.
     1.91 runs from the root leading edge to the tip chord. 2.07 is the tip chord. 0.68 is the height of the
     trailing-edge chamfer above the body (drawn at about 45 degrees).
   - **Figure 48 is consistent with itself.** 1.91 + 2.07 = 3.98 = 3.30 + 0.68. The drawn proportions match the
     labels: the 3.30 extent is about 0.83 of the root chord, and 3.30/3.98 = 0.83.
   - **Region III in Figure 49b** is the in-body strip between the axis and the body surface. It runs from the root
     leading edge to the body base.
   - **The conflict is genuine.** No combination of Figure 48's labels gives the text's 3.21: 3.30, or
     3.97 - 0.68 = 3.29. So this is not a different decomposition of the same fin.
   - **Figure 49b, for information.** This unlabeled schematic is drawn nearer 3.2: region III is about 0.81 of the
     root chord there. Being unlabeled, it does not outweigh Figure 48's dimensioned drawing, and the note correctly
     cites only Figure 48.
   - **E2's figures check out.** 1.93/2 = 0.965; 3.30 x 0.965 = 3.18; 3.98 + 8.68 + 3.18 = 15.84;
     4 x 15.84 = 63.4, which is about 63. The only other label difference is 1.90 for 1.91 (4.19 and 2.07 agree).
   - **Form and placement.** E2 ends with "Neither the errata nor the supplements correct this; the dimension is
     kept as printed." It sits in "Following Figure 49b, then,", outside the align.
5. **Scope.** The diff has four hunks: item 12 with E1, the D26 note E2, item 13, and item 14 with E3. Nothing else
   in the unit changed. The only new cross-reference is `\ref{ch3:fig:48}` inside E2.
6. **Labels.** The unit has no numbered equations. No `\label` or `\tag` was added or removed; I compared the
   label, tag and ref lists of HEAD and the working tree. No new equations need n-labels.
7. **Section 14 notation** in the corrected passages and the notes: `(C_f)_{\mathrm{LAM.}}`, `(C_f)_B`, `(C_f)_F`,
   `(C_{Df})_b`, `C_{Db}`, `(\CDo)_F`, `(\CDo)_{FB}`, `R_c`, `\ell`, `d_m`, `\mathrm{CYL}`, leading-dot decimals and
   `\times 10^{4}`. All are correct.
8. **Renders.** Page 2 shows item 12 and E1; page 3 shows E2; page 5 shows item 13 and E3; page 6 shows Steps 1-3,
   the total and the 44% sentence. All are correct. The build log has no errors and no overfull boxes. The "??"
   references are expected in a standalone unit build.
   - **Cosmetic, not listed.** In E3 the radical bar of $\sqrt{31.75\times10^4}$ (second line) sits just below the
     descenders of "page" in the first line. At 150 dpi it looks like an underline under "for page 451". At
     1200 dpi there is a clear gap, so nothing overlaps: this is TeX's normal minimum line spacing. If wanted,
     `\sqrt{\smash[b]{...}}` or writing the square root as a power 1/2 would avoid it.

## Discrepancies

none
