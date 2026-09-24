# Audit: ch2-sec6 (6. Model Rocket Design), round 1, part 1

## Scope checked

Scan pages read: figures/pages/p264.png through p276.png (13 pages, one Read per page).
On p264 only the part from the heading "6. Model Rocket Design" down was checked (the paragraph
above it, ending "Equation (114) determines C_2 ...", belongs to Section 5). p276 ends mid-sentence
("... excessive aerodynamic drag which can actually cause the"); the rest is part 2's.

Render pages read: build/unit/ch2-sec6-01.png through ch2-sec6-08.png (my content is on 01-07;
08 read as the seam page after it).

Zooms rendered (STYLE.md section 4): build/zoom/audit_ch2-sec6_r1_p1-p270a-270.png (the five-line
display on p270), audit_ch2-sec6_r1_p1-p270b-270.png (the DTV-1 parameter list),
audit_ch2-sec6_r1_p1-p270c-270.png and audit_ch2-sec6_r1_p1-p270d-270.png (the digit in
"I_R = 178"; 178 also agrees with I_R/I_L = .0195 and I_L = 9100).

Items compared, symbol by symbol / sentence by sentence:

| item | count | result |
|---|---|---|
| headings with numbers (6., 6.1, 6.2) | 3 | match |
| numbered equations | 0 | none on these pages, as surveyed |
| unnumbered display (p270: omega_n = .00845V, zeta = .0682, I_R omega_Z / I_L = .0195 omega_Z, omega_nc = .00838V, zeta_c = .0675) | 1 display, 5 lines | match (omega_n, omega_nc per STYLE 13) |
| DTV-1 parameter list (C_1 = 0.65V^2 ..., C_2 = 10.5V ..., I_L = 9100 ..., I_R = 178 ...) | 4 lines | match |
| inline formulas (V twice, omega_Z, I_R omega_Z / I_L, 10%, I_L, C_1, alpha_0, alpha_1 in Plate 1 caption) | 9 | match |
| captions: Figure 48, Plate 1, Figure 49, Figure 50, word by word | 4 | match |
| prose paragraphs (6.: 1; 6.1: 3 plus the unindented "where V ..." continuation; 6.2: 6, the last partial) | 10 (+1) | match: wording, order, paragraph breaks, quotes, dashes |
| lettered/numbered items ((a), (b) on p264; (1), (2), (3) on p270-271) | 5 | match in wording |
| emphasis (design; coupled x2; Decreasing; natural; actual; ballistically; ratio; increase; time; disturbances; not; coupled x2 in Fig. 49 caption) | 14 | all italic |
| author's footnote (asterisk, p275) | 1 | match, placed after "off-optimum" before the period |
| editorial note E1 ("Section 6" on p265) | 1 | statement true: the scan reads "Section 6" |

Notes (not discrepancies): cross-unit references (Section 3, Section 5.3, Figure 44) render as
"??"; "--" rendered as em dash; the author's asterisk footnote is marked with LaTeX's numeral
"1"; the text's "Rocket A", "rocket B", "illustration C" are kept as printed although the artwork
letters its panels (a)-(f); items (1)-(3) are typed as run-in numbered paragraphs (first line
indented, continuation at the margin) and are set in the render as a hanging-indent list like
(a)/(b), which keeps the item structure and wording; figure positions differ from the book.

## Discrepancies

| where | scan reading | compiled reading | severity |
|---|---|---|---|

none
