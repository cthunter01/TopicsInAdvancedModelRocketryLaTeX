# Audit: ch4-sec4 corrections, round 1

Unit: chapters/ch4-sec4.tex (PDF 610-634, printed pp. 578-602). Items: errata items 2-4 (PDF 664), item 9 (PDF 712),
doubt notes D1, D5, D7, D10 (check), D2 (restyle).
Diff inspected: `git diff HEAD -- chapters/ch4-sec4.tex` (header comment; notes at (134), before (137)-(153), before
(154), at "Equation (200a)", before (166); the three citation replacements; the Table 1 caption and three value cells;
a `\FloatBarrier` before Table 2). No other hunks.

## What was checked

1. **Errata items 2-4 (PDF 664, checked against the sheet's wording).**
   - p.583, line 4 from the bottom: "Again, as in Section 2.4, expressions such as (139) are not equations". The
     unit reads "Again, as in Section~\ref{ch4:sec:2.4}, expressions such as~\eqref{ch4:eq:139} are not equations".
     This matches, and only the number changed (1973: "(175)", PDF 615).
   - p.590, line 3 of 4.3.3: "quiescent prior rotational state specified by equations (154)." The unit reads
     `equations~\eqref{ch4:eq:154}.`, which renders "(154)" (page 6 of the unit PDF). `ch4:eq:154` is the
     `\refstepcounter` group label. This matches.
   - p.591, line 6: "account in equations (160)." The unit reads `equations~\eqref{ch4:eq:160}.`, which renders
     "(160)". This matches.
   - None of the three has a note, as the Decisions say (applied silently).
2. **Item 9 (PDF 712 against the 1973 Table 1, PDF 627), zoomed at 300 dpi.**
   - The source prints: 0.00993 radian = 0.569°, 0.0993 radian = 5.69°, and $k$ = 0.92, 0.921 and
     1.016 × 10^-4 kg/m (without fin cant, with 0.569° cant, with 5.69° cant). The three cells match symbol for
     symbol, including the source's "radian" (1973: "rad").
   - The row labels keep the 1973 $\omega_z$ (the source labels them $\omega_c$, a symbol the chapter's Symbols list
     does not have). The \edcap says so.
   - The \edcap is in the caption (section 9). Its 1973 values match PDF 627: 0.01945 rad = 1.11°, 0.1945 rad = 11.1°,
     0.924 × 10^-4 with 1.11° and 1.288 × 10^-4 with 11.1°, and 0.92 × 10^-4 without cant unchanged.
   - The quoted NOTE matches PDF 712 word for word: "There will be consequential corrections to altitudes attained
     by rockets with canted fins".
   - "Table 2 for nonzero roll rates": Table 2's nonzero rates are 0.325v = ω_cres and 3.25v = 10 ω_cres, which are
     exactly the two canted-fin configurations of Table 1, so the paraphrase holds. The statement that Table 2 is not
     recomputed is in the caption.
   - Conversions check: 0.00993 rad × 57.296 = 0.569°, and 0.0993 rad = 5.69°.
3. **D5 (PDF 613, zoomed).**
   - (134) prints $\alpha^4/4$, and the coefficient of $\alpha^4$ in the series of cos is 1/4! = 1/24.
   - (135) truncates after $\alpha^2$, so the slip is harmless, as the note says.
   - The note is in the sentence that introduces (134), and (134) is unchanged.
4. **D7 (PDF 615, zoomed; Chapter 2 re-derived).**
   - (145) prints $+I_R\omega_y\omega_z$.
   - Chapter 2's (14), second row (the $\alpha_Y$, pitch, equation; Chapter 2's Symbols list: $\alpha_X$ yaw,
     $\alpha_Y$ pitch), is $I_L\ddot\alpha_Y + C_2\dot\alpha_Y + C_1\alpha_Y - I_R\omega_Z\dot\alpha_X = f_y$. Solving
     it for $\Delta\omega_y$ gives $\Delta t[f_y - C_2\omega_y - C_1\alpha_y + I_R\omega_x\omega_z]/I_L$.
   - The first row gives exactly (144): $-I_R\omega_y\omega_z$.
   - (6) of Section 1.4 has $M_Y = I_L\,d\Omega_Y/dt - I_R\Omega_X\omega_Z$, which is consistent.
   - So "$+I_R\omega_x\omega_z$ evidently meant", "(144) agrees with Chapter 2" and the yaw/pitch attributions in
     the note are all correct. The equation is kept as printed.
   - The note is at the colon of the sentence that introduces the (137)-(153) run. It cannot go inside the `align`
     (section 9).
5. **D1 (PDF 618).**
   - The third row is printed "(156c)".
   - The text cites "equations (154)" on PDF 619 and in 4.3.2, and errata item 3 also has "(154)".
   - The plain (156) follows on PDF 619.
   - The note is in the sentence that introduces the group, as the item requires.
   - The `\tag{156c}` is kept.
6. **D10 (PDF 625, 628-629).**
   - Rows 12, 13 (sinusoidal) and 24-26 (coupled sinusoidal) all give $t_o$ = 0.1 s.
   - The caption (PDF 629) defines $t_o$ as "the time at which the disturbance begins".
   - PDF 625 says both types "arise immediately upon liftoff" and calculations "should therefore be started at
     t = 0", with (166) at $t = 0$.
   - Nothing in 4.3.4 or 4.4 (PDF 625-634) explains a 0.1 s start-up convention. The ranking paragraph on PDF 632
     ("all of which arise at the same time into the flight") does not say which start the table used.
   - So the conflict is genuine, and the note's hedge ("The text does not say which start the tabulated results
     were computed with") is accurate. "All five" is correct. The note sits in the sentence that introduces (166).
7. **D2 (PDF 625).** "Equation (200a)" is still typed literally. The note now has the doubt-note form (1973 reading;
   evident target with reason; "Neither the errata nor the supplements correct this; ..."). (165a) is correct:
   200 - 35 = 165, and it is the $v^2$ law the sentence explains. The chapter's equations end at (166). One claim
   is inaccurate; see the table below.
8. **"Neither the errata nor the supplements correct this".** The errata sheet lists only pp. 534, 583, 590 and 591
   for Chapter 4. PDF 666 and 699-712 cover pp. 513-514, the multistage equations, Figure 4 and Table 1 (p.710 and
   p.699 skimmed). The claim holds for D1, D2, D5, D7 and D10.
9. **Scope.** Nothing else changed apart from the header comment and the `\FloatBarrier` before Table 2. That line
   is a layout consequence of item 9: the \edcap makes Table 1 taller, and without the barrier the float would come
   out after the non-float longtable. `placeins` is loaded in preamble.tex. It leaves page 8 about half empty,
   which is unavoidable because Table 1 fills a page, as it does in the book (p.595). Not a discrepancy.
10. **Labels.** No label was added, removed or renamed. There are no new equations, so no n-labels are needed.
11. **Section 15 notation.** The notes use $t_o$, $\omega_z$, $\omega_{\mathrm{cres}}$, `\dg` and $\times$. The D7
    note quotes Chapter 2's own uppercase forms ($\omega_Z$, $\alpha_X$, $\Omega_X$) when it cites Chapter 2, which
    is appropriate.
12. **Render.** The PNGs (18:32:58 on) are newer than the source (18:32:50). The log has no overfull boxes. The
    "??" marks are cross-chapter references.
    - Page 2: E1 (D5).
    - Page 3: E2 (D7) and "(139)".
    - Page 4: E3 (D1) with the (156c) tag.
    - Page 6: "(154)" and "(160)".
    - Page 7: E4 (D2) and E5 (D10).
    - Page 9: Table 1 with the new values and the \edcap.
    - Page 10: Table 2 unchanged.

## Observation (not a discrepancy)

STYLE.md section 15 ("Stale citations") also says that (175) on PDF 615 is "35 higher" than the equation meant. The
errata sheet corrects it to (139), which is 36 lower (175 - 35 = 140, which is also an assignment statement). That
STYLE sentence is probably where the D2 note's wording came from.

## Discrepancies

| where | expected (source/1973) | found | severity |
|---|---|---|---|
| ch4-sec4.tex l.410-415, \ednote on "Equation (200a)" (D2) | Of the three stale citations the errata sheet corrects, (189)->(154) and (195)->(160) are 35 higher, but (175)->(139) is 36 higher (PDF 664). The note should say only what holds, e.g. "as are the citations (189) and (195), which the errata sheet corrects to (154) and (160)". | "the printed number is 35 higher, as are three citations in this section that the errata sheet corrects" | note |
