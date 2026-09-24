# Audit: ch3-sec5b, round 1

Unit: 5.2.3 Fin-Body Interference Drag at Angle of Attack (PDF 446) through the end of 5.4 (top of PDF 461,
"... applicable to the calculation of its drag coefficient."), stopping before heading "6.".

## 1. What was checked

Scan pages: PDF 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461 (16 pages, one Read each).
Zoomed 300 dpi crops of the scan (build/zoom/audit_ch3-sec5b_r1-p447a, p449a, p449b, p451a, p451b, p452a, p454a,
p454b, p455a, p455b, p455c, p457a, p457b, p457c, p458a, p458b) covered every hand-lettered display and the
equation-bearing prose lines. Render: build/unit/ch3-sec5b-1..7.png, plus a 250 dpi rasterization of
build/unit/ch3-sec5b.pdf (build/zoom/audit_ch3-sec5b_r1-unit-*.png, crops u1a, u1b, u2a, u4a, u4b, u4c, u5a, u6a, u6b)
for the primes, bars, subscripts and radicals.

Items checked:

- Headings: 4 (5.2.3, 5.2.4, 5.3, 5.4). The number and wording of each match.
- Numbered equations: 12, (146) to (157). Each was checked symbol by symbol and each number is in sequence. The standalone
  build numbers them 146-157 with no offset.
- Unnumbered displays: 5 display lines holding 6 formulas: S_m = pi r^2 = 3.33 cm.^2 with dC_L/dalpha = 1/.32 = 3.12
  (PDF 449); u/U = 0.0172 (454); alpha-bar = (.0828 + .0405)/2 = .0617 (455); k_adm <= 2.48 x 10^-5 meter = 2.48 x 10^-3 cm.
  (457); C_f = 7.63 x 10^-3 (458).
- Where-list on PDF 447: 4 items. The two typed word fractions, with the semicolon after the bar, match. So do the dC_L/dalpha
  item ("at alpha = 0; and") and the S_e item.
- Inline formulas: about 75. Among them are Delta C_Di, d/b = .289, K_B(F) = 0.44, K_F(B) = 1.25, S_e = 12.95 cm.^2,
  C_DB(alpha), C_Di', C_D(alpha), alpha^2, alpha^3, alpha = 5 deg, epsilon (x4), 2epsilon/(rho S_m), 0.201 radian,
  11.5 deg, omega_Z, U = 6000 cm./sec., theta, 5.73 deg, alpha(r), alpha-bar, 6.24alpha^2, (C_Di')_c = .0475, the two
  C_Do, k_adm (x8), 1 x 10^6, C_fx, 2tau_o/(rho U_inf^2), nu = 1.495 x 10^-5 meter^2/second, the micron conversion,
  l_b/k (x2), l_b, k = 0.02 cm., 4.5 x 10^-3, k/delta, delta, 5 x 10^5, R and C_f.
- Captions: 5. Figures 40, 41 and 42, and Tables 4 and 5, all match word for word. Cross-unit targets appear as "??".
- Table 4, one float with two stacked sub-tables: 8 header cells, including the formula lines 1.94alpha^2 + 8.86alpha^3,
  6.51alpha^2, 8.38alpha^2 and 16.83alpha^2 + 8.9alpha^3, and 88 data cells (11 rows x 4 columns x 2). All match.
- Table 5: 2 header cells ("Approximate grain size k / in microns") and 30 data cells (15 rows x 2 columns). All match.
- Prose: 31 paragraph blocks, compared sentence by sentence for wording, emphasis and paragraph breaks. The
  emphasis checked is "sum", "roll", "less", "average", "admissible height", "poorly-sprayed", "eight times" and
  "any two". The author's caret insertions "drag coefficient" on PDF 449 appear twice and are both transcribed.
- Survey briefing (build/ch3-notes/ch3-sec5b.md): the equation pages, figure and table pages, headings and table
  contents it lists for this unit all agree with the scan.

Intended, not reported: the "semi-/empirical" line-end hyphen on PDF 458 is rejoined as "semiempirical", as the
author spells it throughout this unit. The typed C_Do is set as \CDo and the typed C_DB(alpha) as C_{D_B}(alpha).
omega_Z has an uppercase Z. References to other units and chapters appear as "??" in the standalone build. Tables
are set with booktabs rules and the caption above.

## 2. Discrepancies

none
