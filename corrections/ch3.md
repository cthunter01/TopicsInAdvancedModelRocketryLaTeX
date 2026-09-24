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
| 1 | 664 | p.268 (PDF 298), line 3 of the Symbols list | the symbol of "unit normal vector" should be printed as on the errata sheet (n with a mark above it: read it there) | ch3-symbols | todo |
| 2 | 664 | p.270 (PDF 300), last line of the Symbols list | should read "$\infty$ infinity" | ch3-symbols | todo |
| 3 | 664 | p.342 (PDF 374), line 15 | should read "forces due to rotation of the body, and whether or not heat" | ch3-sec3b | todo |
| 4 | 664 | p.364 (PDF 396), second complete sentence | should read "In accordance with Bernoulli's equation, there is a decrease in static pressure between A and B and a corresponding increase along the downstream surface from B to C." | ch3-sec3c-sec4a | todo |
| 5 | 664 | p.382 (PDF 414), line 1 | should read "(from left to right in the diagram) the drag coefficient shows a corresponding increase." | ch3-sec4b | todo |
| 6 | 664 | p.401 (PDF 433), line 15 | should read "is usually small compared to that due to the mechanism which" | ch3-sec5a | todo |
| 7 | 664 | p.480 (PDF 512), line 8 | should read "nose, on the other hand, is itself rounded at its forward" | ch3-sec7 | todo |
| 8 | 688-689 | p.356 and the top of p.357 (PDF 388-389) | replacement text with equations (97)-(101), (102a), (102b); the word "calculated" is inserted by caret on PDF 688; "remainder of text on page 357 is unchanged" | ch3-sec3b | todo |
| 9 | 690 | Section 5.2.2, p.412 (PDF 444) | remove the second sentence of the second paragraph ("One cannot, however, obtain an expression for C_Di unless he has specific knowledge of the distribution of lift on the fin.") and put the new text with equations (144A), (144B) in its place; add the constant e = 0.863 to the row of two constants at the bottom of p.412 | ch3-sec5a | todo |
| 10 | 691-693 | Section 5.3, from equation (152) on p.422 (PDF 454) to the sentence beginning "Furthermore..." on p.424 (PDF 456) | replacement text with new equations (152)-(156) | ch3-sec5b | todo |
| 11 | 694 | Symbols list | eight entries: $(C_{Di}')_{\mathrm{cant}}$, $(C_{Di})_{\mathrm{twist}}$, $(C_{Di}')_{\mathrm{twist}}$, $\Delta C_{Di}$, $(\Delta C_{Di})_{\mathrm{cant}}$, $(\Delta C_D)_{\mathrm{cant}}$, $e$, $\Delta\alpha$ (compare with the 1973 list: an existing entry is corrected, a missing one added in the book's order) | ch3-symbols | todo |
| 12 | 695 | p.445 (PDF 477), the handwritten equation after "For the cylindrical body we find from (170)" | the third member gets the factor 4: $(S_s/S_m)_{\mathrm{CYL}} = 4\,\ell/d_m = 4\,(22.61/1.93) = 46.9$ | ch3-sec6b | todo |
| 13 | 696 | p.449 (PDF 481), the line after the first handwritten equation | "From equation (100) we find B = 1735; since R_l = 1.27 x 10^6," becomes "From equation (100) we find B = 1735. Then, since R_l = 1.27 x 10^6," | ch3-sec6b | todo |
| 14 | 697-698 | p.451 and the top of p.452 (PDF 483-484) | replacement text: Steps 1-3 and the overall drag coefficient $(C_{Do})_{FB} = .605$; "remainder of text on page 452 is unchanged" | ch3-sec6b | todo |
| F1 | plan | Figure 22 caption vs text | the caption and the text give different values (1740 vs 1700): flag with an \ednote after checking both | (owner of Figure 22) | todo |

Notes
- (144A) and (144B) exist only in the corrected text: `\begin{equation*}\tag{144A}\label{ch3:eq:n144A}` (STYLE.md section 4).
- Doubts noted during the faithful transcription are added below as D-items when the transcription is done.

Doubts (the faithful pass keeps each as printed; the corrections step gives each an \ednote, normalizes it silently as a typing slip, or leaves it, and records which)

| # | Unit | PDF | Doubt | Status |
|---|---|---|---|---|
| D1 | ch3-symbols | 297 | the subscript of the equivalent diameter is typed "eqiv." | fixed silently as a typing slip before transcription (STYLE.md section 14): $d_{\mathrm{equiv.}}$ |
| D2 | ch3-symbols | 298 | the "unit normal vector" n and "unit tangent vector" t are printed without arrows, although the text writes them with arrows (Figure 11 caption) and the list has a separate n (rotation rate) and t (time); errata item 1 marks the n only | todo |
| D3 | ch3-symbols | 300 | the last entry, "infinity", has an empty Symbol cell (errata item 2 supplies it) | covered by item 2 |
| D4 | (owner of (140)) | 436 | $\ell_B$ in (140); elsewhere $\ell_b$ | todo |
| D5 | (owner of (161)) | 463 | $(C_f)_b$ in (161); (166) and the where-list have $(C_f)_B$ | todo |
| D6 | (owner of (182)) | 489 | $\ell_c$ in (182); (184) and (188) have $\ell_s$ (check whether they are the same length) | todo |
| D7 | ch3-sec2b | 334 | typed $P_{\mathrm{tot}}$ in the prose; (22)-(23) and the Symbols list have $p_{\mathrm{tot}}$ | todo |
| D8 | (owner of Figure 33) | 425 | typed $P_b$ in the Figure 33 caption; (121)-(122) have $p_b$ | todo |
