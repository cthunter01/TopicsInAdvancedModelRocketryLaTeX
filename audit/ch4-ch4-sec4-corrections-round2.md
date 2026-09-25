# Audit: ch4-sec4 corrections, round 2

Unit: chapters/ch4-sec4.tex (PDF 610-634, printed pp. 578-602). The items are errata items 2-4 (PDF 664), item 9
(PDF 712), the doubt notes D1, D5 and D7, the check item D10, and the D2 restyle. This round re-verifies the whole
diff, with extra attention to the one round-1 finding (the D2 note's "three citations ... 35 higher").

Diff inspected: `git diff HEAD -- chapters/ch4-sec4.tex` (56 insertions, 14 deletions). It has these hunks and no
others:
- the header comment;
- the notes at (134), before (137)-(153), before (154), at "Equation (200a)", and before (166);
- the three citation replacements;
- the Table 1 caption and its three value cells;
- `\FloatBarrier` before Table 2.

## Round-1 finding

- **D2 note (l.410-415).** The note now reads: "... and the printed number is 35 higher, as are the citations (189)
  and (195) in this section, which the errata sheet corrects to (154) and (160)."
  - Checked against PDF 664 and PDF 622-623: 189 - 154 = 35, 195 - 160 = 35 and 200 - 165 = 35. Every part of the
    sentence holds.
  - (175) -> (139), which differs by 36, is no longer included in the claim.
  - The rest of the note also holds:
    - The 1973 reading "Equation (200a)" matches PDF 625.
    - The chapter has no (200a); its equations end at (166b).
    - (165a) $A_f = A_o v^{2}$ is the law "just given", and its $v^{2}$ proportionality is what the sentence explains.
    - It closes with "Neither the errata nor the supplements correct this; the reference is kept as printed." This
      is the same doubt-note form as the D3 note in ch4-sec5.
  - Rendered as E4 on page 7. **Fixed.**

## What was checked

1. **Errata items 2-4.** Checked against the sheet (PDF 664) and the 1973 pages.
   - **p.583 (PDF 615).** Line 4 from the bottom reads "Again, as in Section 2.4, expressions such as (175) are not
     equations". The unit has `expressions such as~\eqref{ch4:eq:139} are not equations`, which renders "(139)"
     (page 3). This matches the errata wording.
   - **p.590 (PDF 622).** Line 3 of 4.3.3 now reads `equations~\eqref{ch4:eq:154}.`, which renders "(154)" (page 6).
     `ch4:eq:154` is the `\refstepcounter` group label.
   - **p.591 (PDF 623).** Line 6 now reads `equations~\eqref{ch4:eq:160}.`, which renders "(160)" (page 6).
   - All three are silent, as the Decisions require. Only the number changed in each sentence.
2. **Item 9 (PDF 712 against the 1973 Table 1, PDF 627).**
   - The new cells match the source symbol for symbol, including its "radian":
     - 0.00993 radian = 0.569°;
     - 0.0993 radian = 5.69°;
     - $k$ = 0.92 / 0.921 / 1.016 × 10^-4 kg/m, without fin cant / with 0.569° cant / with 5.69° cant.
   - The conversions hold: 0.00993 × 57.2958 = 0.569, and 0.0993 × 57.2958 = 5.69.
   - The \edcap is in the caption, as section 9 allows. Everything it states matches the pages:
     - The 1973 values match PDF 627: 0.01945 rad = 1.11°, 0.1945 rad = 11.1°, 0.924 and 1.288 × 10^-4 kg/m, and
       0.92 unchanged.
     - The supplement's ω_c labels are reported, and the table keeps its ω_z.
     - The quoted NOTE is verbatim.
     - "Table 2 for nonzero roll rates" is right: Table 2's roll rates 0.325v and 3.25v are ω_cres and 10 ω_cres of
       Table 1. The not-recomputed statement is present.
   - Nothing else in Chapter 4's text cites the old cant angles or k values (grep of chapters/ch4-*.tex).
   - Table 2 is unchanged.
3. **D5 (PDF 613).**
   - (134) prints $\alpha^4/4$ as its third term. The series term is $\alpha^4/4! = \alpha^4/24$.
   - (135) truncates after $\alpha^2$, so the slip is harmless.
   - The note is in the sentence that introduces (134), and (134) is kept as printed.
4. **D7 (PDF 615, zoomed at 300 dpi; Chapter 2 re-derived).**
   - (145) prints $+I_R\omega_y\omega_z$.
   - Chapter 2's (14), second row (the $\alpha_Y$ row, pitch per the Chapter 2 Symbols list), solved for the
     angular acceleration gives $[f_y - C_2\omega_Y - C_1\alpha_Y + I_R\omega_Z\omega_X]/I_L$. So $+I_R\omega_x\omega_z$
     is meant.
   - The first row gives exactly (144)'s $-I_R\omega_y\omega_z$.
   - (6) has $M_Y = I_L\,d\Omega_Y/dt - I_R\Omega_X\omega_Z$, which is consistent.
   - The labels `ch2:eq:14`, `ch2:eq:6` and `ch2:sec:1.4` exist.
   - Chapter 4's own usage agrees with the note's yaw/pitch naming: (132) calls $\alpha_x$, $\alpha_y$ the yaw and
     pitch angles, and (162) puts $f_x$ about the yaw axis.
   - The note sits at the colon before the `align`.
5. **D1 (PDF 618).**
   - The third row is printed "(156c)". The text cites "equations (154)", and a separate (156) follows on PDF 619.
   - The note is in the introducing sentence ("For values of t less than t_o, therefore,"), and `\tag{156c}` is kept.
6. **D10 (PDF 625, 628-629).**
   - Rows 12-13 (sinusoidal) and 24-26 (coupled sinusoidal) all give $t_o$ = 0.1, which makes five cases.
   - The caption (PDF 629) defines $t_o$ as "the time at which the disturbance begins".
   - PDF 625 says the forcing arises "immediately upon liftoff" and that calculations start at $t = 0$.
   - No start-up convention is explained anywhere in 4.3.4-4.4. The ranking paragraph ("all of which arise at the
     same time into the flight") does not state the start time used.
   - The conflict is genuine and the note's hedge is accurate. It sits in the sentence that introduces (166).
7. **"Neither the errata nor the supplements correct this".** The errata cover only pp. 534, 583, 590 and 591 of
   Chapter 4. PDF 666 and 699-712 cover pp. 513-514, the multistage equations, Figure 4 and Table 1. So the phrase
   holds for D1, D2, D5, D7 and D10.
8. **Scope.** There are no changes outside the items, apart from the header comment and the `\FloatBarrier`.
   - The `\FloatBarrier` keeps Table 1 (a float) ahead of the non-float Table 2 longtable, as in the book. Round 1
     accepted it as a layout consequence of the taller captioned table.
   - `placeins` is loaded in preamble.tex.
9. **Labels.** The sequence of `\label`/`\tag` in the working file is identical to HEAD. No equations were added, so
   no n-labels are needed.
10. **Section 15 notation in the notes and caption.** The notes use:
    - `t_o`, `\omega_z`, `\omega_{\mathrm{cres}}`, `\dg`, `\times`, and "kg/m" as text;
    - Chapter 2's uppercase forms only where they quote Chapter 2.
11. **Render.** The build/unit PNGs (18:40:28 on) are newer than the source (18:40:16). The log has no overfull
    boxes. Every undefined reference points outside the unit (other chapters or other ch4 units).
    - Page 2: E1 (D5).
    - Page 3: E2 (D7) and "(139)".
    - Page 4: E3 (D1) with the (156c) tag.
    - Page 6: "(154)" and "(160)".
    - Page 7: E4 (D2, revised) and E5 (D10).
    - Page 9: Table 1 with the new values and the \edcap, all correct.

## Observation (not a discrepancy of this unit)

The round-1 observation still applies. STYLE.md section 15 ("Stale citations") describes (175) on PDF 615 as 35 higher
than the equation meant, but the errata's target (139) is 36 lower. This is outside the unit and changes nothing in it.

## Discrepancies

none
