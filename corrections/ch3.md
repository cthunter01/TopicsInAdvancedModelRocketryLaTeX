# Chapter 3 — corrections checklist

Sources: the 1973 errata sheet (PDF 664; PDF 665 is a second typing of the same list); the supplement pages for
Chapter 3, PDF 688-698 (authors and dates as the pages give them; the corrections step records them): replacement page 356 and top
of page 357 (PDF 688-689); "Corrections and additions to Section 5.2.2 of Chapter 3" (PDF 690); "Corrections to drag
due to fin cant in Chapter 3, Section 5.3" (PDF 691-693); "Corrections and additions to symbol table of Chapter 3"
(PDF 694); corrections to pages 445 (PDF 695), 449 (PDF 696), 451 and the top of 452 (PDF 697-698).
Printed page = PDF page - 30 up to PDF 321, and PDF page - 32 from PDF 324 on (PDF 322-323 are unnumbered figure pages).

Status: todo / applied (with \ednote location) / deferred (reason)

| # | Source (PDF) | Original location | Change | Unit | Status |
|---|---|---|---|---|---|
| 1 | 664 | p.268 (PDF 298), line 3 of the Symbols list | the symbol of "unit normal vector" should be printed as on the errata sheet (n with a mark above it: read it there) | ch3-symbols | applied silently, $\vec{n}$ unit normal vector, ch3-symbols.tex:133 |
| 2 | 664 | p.270 (PDF 300), last line of the Symbols list | should read "$\infty$ infinity" | ch3-symbols | applied silently, $\infty$ infinity, ch3-symbols.tex:187 (closes D3) |
| 3 | 664 | p.342 (PDF 374), line 15 | should read "forces due to rotation of the body, and whether or not heat" | ch3-sec3b | in place (faithful pass), ch3-sec3b.tex:352 |
| 4 | 664 | p.364 (PDF 396), second complete sentence | should read "In accordance with Bernoulli's equation, there is a decrease in static pressure between A and B and a corresponding increase along the downstream surface from B to C." | ch3-sec3c-sec4a | applied, \ednote after 'from B to C.', ch3-sec3c-sec4a.tex:189 |
| 5 | 664 | p.382 (PDF 414), line 1 | should read "(from left to right in the diagram) the drag coefficient shows a corresponding increase." | ch3-sec4b | applied, \ednote after 'increase.', ch3-sec4b.tex:138 |
| 6 | 664 | p.401 (PDF 433), line 15 | should read "is usually small compared to that due to the mechanism which" | ch3-sec5a | in place (faithful pass), ch3-sec5a.tex:32 |
| 7 | 664 | p.480 (PDF 512), line 8 | should read "nose, on the other hand, is itself rounded at its forward" | ch3-sec7 | in place (faithful pass), ch3-sec7.tex:176 |
| 8 | 688-689 | p.356 and the top of p.357 (PDF 388-389) | replacement text with equations (97)-(101), (102a), (102b); the word "calculated" is inserted by caret on PDF 688; "remainder of text on page 357 is unchanged" | ch3-sec3b | applied, the text follows the supplement including the caret-inserted 'calculated'; (102a)-(102b) with R_crit; labels ch3:eq:97-102b kept; \ednote at the end of the first sentence, ch3-sec3b.tex:719; rendered p.183 (PDF p.188) matches the supplement symbol by symbol |
| 9 | 690 | Section 5.2.2, p.412 (PDF 444) | remove the second sentence of the second paragraph ("One cannot, however, obtain an expression for C_Di unless he has specific knowledge of the distribution of lift on the fin.") and put the new text with equations (144A), (144B) in its place; add the constant e = 0.863 to the row of two constants at the bottom of p.412 | ch3-sec5a | applied, (144A)/(144B) as equation* with \tag and labels n144A/n144B (ch3-sec5a.tex:289, 309); constants row 18.6 / 0.123 / e = 0.863 (line 317); \ednote on 'is given by' (line 280); rendered pp.209-210 (PDF 214-215) match |
| 10 | 691-693 | Section 5.3, from equation (152) on p.422 (PDF 454) to the sentence beginning "Furthermore..." on p.424 (PDF 456) | replacement text with new equations (152)-(156) | ch3-sec5b | applied, (152)-(154) with the 1973 labels, the new (155)/(156) as (155')/(156') with labels n155/n156 (ch3-sec5b.tex:331, 342; see gap on Decisions); \ednote on 'determined by', line 243; rendered pp.216-218 (PDF 221-223) match |
| 11 | 694 | Symbols list | eight entries: $(C_{Di}')_{\mathrm{cant}}$, $(C_{Di})_{\mathrm{twist}}$, $(C_{Di}')_{\mathrm{twist}}$, $\Delta C_{Di}$, $(\Delta C_{Di})_{\mathrm{cant}}$, $(\Delta C_D)_{\mathrm{cant}}$, $e$, $\Delta\alpha$ (compare with the 1973 list: an existing entry is corrected, a missing one added in the book's order) | ch3-symbols | applied, the (C_Di')_cant meaning corrected with an \ednote (ch3-symbols.tex:35); seven entries added in the book's order, one \ednote on the Delta C_Di row (line 33); e after d_r, Delta alpha after alpha-bar; rendered pp.138-142 match |
| 12 | 695 | p.445 (PDF 477), the handwritten equation after "For the cylindrical body we find from (170)" | the third member gets the factor 4: $(S_s/S_m)_{\mathrm{CYL}} = 4\,\ell/d_m = 4\,(22.61/1.93) = 46.9$ | ch3-sec6b | applied, factor 4 in the third member, ch3-sec6b.tex:67, \ednote line 63; rendered p.229 (PDF 234) matches |
| 13 | 696 | p.449 (PDF 481), the line after the first handwritten equation | "From equation (100) we find B = 1735; since R_l = 1.27 x 10^6," becomes "From equation (100) we find B = 1735. Then, since R_l = 1.27 x 10^6," | ch3-sec6b | applied silently (punctuation and connective only, no change of content), ch3-sec6b.tex:178 |
| 14 | 697-698 | p.451 and the top of p.452 (PDF 483-484) | replacement text: Steps 1-3 and the overall drag coefficient $(C_{Do})_{FB} = .605$; "remainder of text on page 452 is unchanged" | ch3-sec6b | applied, Steps 1-3, (CDo)_FB = .605 and 'more than 44%'; \ednote on 'The body skin-friction coefficient is given by', ch3-sec6b.tex:225; rendered pp.232-233 (PDF 237-238) match |
| F1 | plan | Figure 22 caption (PDF 390) vs the text and tabulation (PDF 389) | the caption gives B = 1740, the text and tabulation about 1700 (the formula gives about 1742): flag with an \ednote | ch3-sec3c-sec4a | applied, \edcap in the Figure 22 caption, ch3-sec3c-sec4a.tex:30 (B = 1742.6, so 1743, verified) |

Notes
- (144A) and (144B) exist only in the corrected text: `\begin{equation*}\tag{144A}\label{ch3:eq:n144A}` (STYLE.md section 4).
- Doubts noted during the faithful transcription are added below as D-items when the transcription is done.

Doubts (the faithful pass keeps each as printed; the corrections step gives each an \ednote, normalizes it silently as a typing slip, or leaves it, and records which)

| # | Unit | PDF | Doubt | Status |
|---|---|---|---|---|
| D1 | ch3-symbols | 297 | the subscript of the equivalent diameter is typed "eqiv." | fixed silently as a typing slip before transcription (STYLE.md section 14): $d_{\mathrm{equiv.}}$ |
| D2 | ch3-symbols | 298 | the "unit normal vector" n and "unit tangent vector" t are printed without arrows, although the text writes them with arrows (Figure 11 caption) and the list has a separate n (rotation rate) and t (time); errata item 1 marks the n only | note in a longtable-safe \multicolumn cell, ch3-symbols.tex:148 |
| D3 | ch3-symbols | 300 | the last entry, "infinity", has an empty Symbol cell (errata item 2 supplies it) | covered by item 2 |
| D4 | ch3-sec5a | 436 | $\ell_B$ in (140); elsewhere $\ell_b$ | applied silently, \ell_b in (140), ch3-sec5a.tex:122 |
| D5 | ch3-sec6a | 463 | $(C_f)_b$ in (161); (166) and the where-list have $(C_f)_B$ | applied silently, (C_f)_B in (161), ch3-sec6a.tex:62 |
| D6 | ch3-sec6c | 489 | $\ell_c$ in (182); (184) and (188) have $\ell_s$ (check whether they are the same length) | checked; l_c is the cylinder length l_s of (184) and (188); set silently, ch3-sec6c.tex:74 |
| D7 | ch3-sec2b | 334 | typed $P_{\mathrm{tot}}$ in the prose; (22)-(23) and the Symbols list have $p_{\mathrm{tot}}$ | applied silently, p_tot, ch3-sec2b.tex:275 |
| D8 | ch3-sec4b | 425 | typed $P_b$ in the Figure 33 caption; (121)-(122) have $p_b$ | applied silently, p_b in the Figure 33 caption, ch3-sec4b.tex:415 |
| D9 | ch3-intro-sec2a | 314-315 | E is taken as the sea-level pressure for "isothermal" changes, so (5) gives c = sqrt(101325/1.225) = 288 m/s, not the 340 m/s used on PDF 316 and in Figure 4 (sound is adiabatic: E = gamma p; Newton's isothermal error) | note, ch3-intro-sec2a.tex:315 (288 and 340.3 m/s verified) |
| D10 | ch3-intro-sec2a | 315 | c^2 = E/rho_o is credited to "a calculus problem known as Laplace's equation"; the problem is the wave equation | note, ch3-intro-sec2a.tex:346 |
| D11 | ch3-sec3a | 358-359 | the coefficients 3.10 in (55a)-(55b) and 3.22 x 10^-2 in (57) do not follow from (54) and (56) with the stated U = 60 m/s and nu = 1.495 x 10^-5 (they imply nu = 2.31 x 10^-5); the delta values and the 0.322 m/s that follow use the printed coefficients | note, ch3-sec3a.tex:486 (2.50e-3, 2.59e-2 and nu = 2.31e-5 verified) |
| D12 | ch3-sec3a | 361 | the last member of (60) drops the factor mu that the middle member carries; (61) restores it | note, ch3-sec3a.tex:577 |
| D13 | ch3-sec3a | 349 | the Plate 2 caption gives "a Reynolds number R_l of 3", implausibly low for the flow shown (the words are in a different, smaller type, as if patched) | \edcap in the Plate 2 caption, ch3-sec3a.tex:196 (checked on the scan) |
| D14 | ch3-sec3b | 367 | the integrand of (69) is printed with "- uU_inf" where Table 2 and (70) require "+ uU_inf" | note, ch3-sec3b.tex:172 (verified against Table 2 and (70)) |
| D15 | ch3-sec3c-sec4a | 392 | (Delta C_f)_turb = 5.93 x 10^-5 and (C_f')_turb = .0045593 were suspected not to follow from (105) (the transcriber's figures 6.15 x 10^-5 and .00459 were themselves miscomputed) | checked, not confirmed: (105) gives 5.91e-5 (the printed 5.93e-5 is .016/270, R_l^{2/5} rounded) and the printed .0045593 is .0045 + .0000593; last-digit rounding of the D35 kind, no note (reason also in the ch3-sec3c-sec4a.tex header) |
| D16 | ch3-sec5a | 436 | (139) ends in alpha where alpha C_L gives alpha^2, as (142) and the PDF 441 display have it | note, ch3-sec5a.tex:104 |
| D17 | ch3-sec5b | 449 | Delta C_Di = 8.38 alpha^2 is said to be "larger than the sum" of C_DB(alpha) and C_Di'; it is larger than each, not than their sum (Table 4 at 10 degrees: .255 against .304) | note, ch3-sec5b.tex:53 (.304 against .255 verified on PDF 449 and Table 4) |
| D18 | ch3-sec6a | 463, 465 | (159) has no factor S_F/S_m, while its restatement on PDF 465 adds it; with that form (158) counts the area ratio twice | note, ch3-sec6a.tex:90 |
| D19 | ch3-sec6a | 473 | (172a)-(172b) print the frustum factor (d_m - d_b) and (1 - d_b/d_m); the lateral area of a frustum gives (d_m + d_b) and (1 + d_b/d_m) (with the printed sign a cylinder gives 0 instead of (170)) | note, ch3-sec6a.tex:336 |
| D20 | ch3-sec6c | 489-491 | the same frustum sign in (183a)-(183b), carried into (184) and (199) | note, ch3-sec6c.tex:76 (1.2 against 10.8 verified) |
| D21 | ch3-sec6c | 493 | the coefficient 82.8 in (C_Df)_b = 82.8(C_f)_B does not follow from (199) with the GCR-x values (59.8 as printed, 69.9 with the corrected sign); Table 6 is computed with 82.8 | checked, confirmed; note, ch3-sec6c.tex:251 (59.8, 69.9 and 78.5 verified on PDF 493) |
| D22 | ch3-sec6c | 492 | the fin side conditions of (204a)-(204b) are printed with R_l and R_crit, but fin transition depends on R_c = (c/l_b) R_l: R_l < (l_b/c) R_crit, i.e. the 5.14 x 10^6 used on PDF 493 | note, ch3-sec6c.tex:188 (5.14e6 verified) |
| D23 | ch3-sec6c | 494 | R = 10^4 is said to correspond to "about 0.6 meter/second" for a 30 cm rocket; nu R/l = 0.50 m/s, as the book's own U = 4.975 x 10^-5 R_l (PDF 499) also gives | note, ch3-sec6c.tex:345 (0.50 m/s verified on PDF 494) |
| D24 | ch3-sec6c | 491-494 | C_DI is computed in (202) and on PDF 493 but left out of (205) and the PDF 494 total | checked, not confirmed: C_DI in (194) is the friction drag of the buried fin area S_F - S_E, which (CDo)_F in (201) already covers by using the gross area S_F (Section 6.1.1, PDF 465); leaving it out of (205), the PDF 494 total and Table 6 is the method, not an omission; no note |
| D25 | ch3-sec5b | 452 (ch3-sec5b.tex, before (152)) | the derivation of (152) cites Chapter 2's (90) and (115)-(117), which this edition prints in Mandell's 2022 form; item 10 replaces (152) onward but not this sentence | note, ch3-sec5b.tex:233 (0.32726, 0.1691 and 0.0505 verified by recomputing Chapter 2's (90) and (115)-(117)) |
| D26 | ch3-sec6b | 478-479 | the fin dimensions in the text (root chord 3.97, region I 1.90 x 4.19, region III 3.21 x 0.965) do not all match the labels of Figure 48 (1.91, 3.30, 4.19, 0.68, 2.07) | checked, confirmed for region III (3.21 against the 3.30 of Figure 48); note, ch3-sec6b.tex:123 (3.18 and 15.84 verified) |
| D27 | ch3-sec2b | 333 | "Comparison of equation (2.20) with equation (2.18)" uses section-prefixed numbers that exist nowhere else (it means (20) and (18)) | existing note restyled, ch3-sec2b.tex:242 |
| D28 | ch3-sec4b | 423 | base drag is called "the second term in equation (28)", but the S_b integral is the first term of (28) as printed | existing note restyled, ch3-sec4b.tex:367 |
| D29 | several | 362, 372, 399, 406, 409, 522 | silent typographical fixes: "occuring" (362), "drag one one side" (372), "Prandl" (399; "Prandtl" on 404), "as a subcritical" for "at" (406), "R_a = A_2/A_1." before (112) (409), "Where" after (222) (522) | fixed silently in the faithful pass |
| D30 | ch3-sec3b / ch3-sec3c-sec4a | 389-390 | B = 1700 in the text and the tabulation, 1740 in the Figure 22 caption (the formula gives about 1742) | item F1 |
| D31 | ch3-sec3b | 388-389 | (97)-(102b) as printed in 1973 (e.g. (102a)-(102b) with R_l where R_crit is meant) | item 8 |
| D32 | ch3-sec5b | 455 | 6.24 alpha^2 for the 6.51 alpha^2 of (145), the 12.5 of (154), 6.34%, and (C_Di')_c for (C_Di')_cant | item 10 (replaced text) |
| D33 | ch3-sec6b | 477, 483-484 | the missing factor 4 in (S_s/S_m)_CYL; (C_f)_B = .00154 for .00236 and the figures that follow it | items 12 and 14 |
| D34 | ch3-sec4b / ch3-sec3c-sec4a | 396, 414 | the pressure increase/decrease reversed (396) and "from top to bottom" (414) | items 4 and 5 |
| D35 | several | various | last-digit arithmetic and rounding, recorded without notes because they do not change any conclusion: 25.6% for 25.8% (311); 1.205e6 for 1.204e6 (331); 4.02e4 and 12.06e4 for 4.01e4 and 12.04e4 (358, 362); "water roughly 75 times as viscous as air" (321); "50% to 100%" for 38%-120% (340); 8.86 for 8.89 and 5.42/6.51 for 5.44/6.50 (441, 445); 8.38 for 8.37, 12.95 cm^2, 18.52 for 18.56, 2.48e-5 for 2.49e-5 and last-digit cells of Table 4 (449-457); "a about 0.05" (474); 2.7 for 2.67, .279 for .280, 8.68 for 8.67, .190 for .191 (477-479); Mercer 0.42 against 0.43, 3.175e5 and 3.02e4 (482); 4.25 and 17,900 (493); Table 6 row 1e4 (495); 4.975e-5 (499); 30-300 m/s against 24.9 and 256 (497); Figure 51 caption 5e6 for 5.14e6 (496); 3.33e-13 (500); Table 7 cells and the "<10%" claim (501-504); Table 8 cells (515); 0.28/67% and 0.21 against Figure 31 (420); "From equation (113)" (411) | no note |
| D36 | several | various | notation kept as printed, no note: tau in (27) vs tau_o in (33); (p_s)_stag vs the list's p_s(stag.); D_forebody,friction vs D_forebody; C_D(alpha) vs the list's C_Dalpha; (C_f)_LAM.; std without a period in (213); \vec{U} in (222); l_n and l_t in the Figure 50 artwork; the arrowed n of (109) vs the typed n; References 4 and 6 punctuation | no note |

Decisions for the corrections step (2026-09-24)
- Errata items 1 and 2 (the n of "unit normal vector" as the errata sheet prints it, and the missing infinity sign)
  are typographical: apply them silently. Items 4 and 5 change the meaning: each gets an \ednote.
- Item 8 keeps the 1973 labels ch3:eq:97 to ch3:eq:102b. Item 9's (144A) and (144B) exist only in the corrected text:
  `\begin{equation*}\tag{144A}\label{ch3:eq:n144A}`. Item 10 replaces the 1973 (152)-(154), which keep their labels;
  its two further equations are numbered (155) and (156) in the supplement, numbers the unchanged 1973 equations of
  Section 5.4 keep, so they are shown as (155') and (156') with labels ch3:eq:n155 and ch3:eq:n156 (the Chapter 2
  (89')-(92') decision), and the item-10 \ednote says so. Item 13 (punctuation and a connective only) is applied silently. Replaced
  passages get one \ednote each. The note quotes every replaced 1973 equation in full and quotes the replaced prose
  when it is a paragraph or less. For longer passages it quotes the sentences whose content changes (Chapter 2
  practice). The 1973 text is in git (commit 7e2087d).
- D4, D5, D7 and D8 are case slips for the same quantity: set the Symbols-list form silently (as for Chapter 2's
  D11). For D6, check whether l_c in (182) is the length l_s; if so, set l_s silently, otherwise keep it as printed.
- D-items marked "note" get a short \ednote in the Chapter 2 style: what is printed, what is evidently meant and
  why, and "Neither the errata nor the supplements correct this; the ... is kept as printed." Items marked "check"
  are verified first (by derivation or recomputation), then noted if confirmed or left as printed with the reason
  recorded. D27 and D28 already have notes: bring their wording into the same style. D2 (the unit tangent t without
  an arrow) gets a note on its row, in the longtable-safe form of STYLE.md section 9.
- F1: an \edcap in the Figure 22 caption. The caption gives B = 1740, while the text and the tabulation give 1700,
  and (100) with (102a)-(102b) gives about 1742.
