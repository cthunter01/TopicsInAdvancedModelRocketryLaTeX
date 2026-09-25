# M5 audit: supplement, Chapter 3 documents (round 1, part 2)

Scan pages: PDF 694-698 (figures/pages/p694.png ... p698.png).
Render pages: build/unit/s-ch3-5.png, s-ch3-6.png, s-ch3-7.png, plus s-ch3-4.png as the preceding neighbour
(there is no page after 7). No rebuild was run. The comparison used images only. No .tex file was opened.
Zoomed crops: build/zoom/audit_supp-ch3_r1_p2-*.png (scan 695, 696, 697; render page 7).

## Items checked

**PDF 694, "Corrections and Additions to Symbol Table of Chapter 3"** (render p. 5)
- Heading wording (printed in capitals, set as a title-case \chapter).
- Column heads Symbol / Meaning. They are underlined in the scan and bold in the render, following the
  STYLE.md section 8 symbols-list template.
- All 8 rows, symbol by symbol: (C_Di')_cant, (C_Di)_twist, (C_Di')_twist, ΔC_Di, (ΔC_Di)_cant, (ΔC_D)_cant,
  e, Δα. The typewriter prints the prime after the "Di" subscript. The render uses C_{Di}', which matches the
  STYLE.md section 14 prime rule. The "cant" and "twist" subscripts are upright.
- Every meaning cell word for word, including the quoted "lift" and "based on fin area in side view" /
  "based on maximum frontal cross-sectional area".
- Row order matches the scan.

**PDF 695, page -445-** (render p. 6)
- The centred "-445-" line.
- Bracketed instruction "[NO CHANGE UNTIL THE HANDWRITTEN EQUATION FOLLOWING THE LINE "For the cylindrical
  body we find from (170)". THIS LINE PRESENTLY READS:". In the standalone build (170) shows as "??". Its
  label ch3:eq:170 resolves to 170 in build/chapters/ch3.aux.
- The "presently reads" display: (S_s/S_m)_CYL = 4 ℓ/d_m = 22.61/1.93 = 46.9. It correctly has no factor 4
  on 22.61/1.93.
- "CHANGE THE LINE TO READ AS FOLLOWS:]".
- The corrected display: (S_s/S_m)_CYL = 4 ℓ/d_m = 4 (22.61/1.93) = 46.9. Checked the brackets, the extent
  of the CYL subscript, the script ℓ and the fraction bars.
- "[REMAINDER OF TEXT ON PAGE 445 IS UNCHANGED]".

**PDF 696, page -449-** (render p. 6)
- The centred "-449-" line.
- "[NO CHANGE UNTIL THE LINE IMMEDIATELY FOLLOWING THE FIRST HANDWRITTEN EQUATION. THIS LINE PRESENTLY READS:".
- The quoted line "From equation (100) we find B = 1735; since R_ℓ = 1.27 x 10^6,". In the standalone build
  (100) shows as "??". Its label ch3:eq:100 resolves to 100. The line is centred and indented as in the scan.
- "CHANGE THE LINE TO READ AS FOLLOWS:]".
- The replacement line "From equation (100) we find B = 1735. Then, since R_ℓ = 1.27 x 10^6,", set flush left.
- "[REMAINDER OF TEXT ON PAGE 449 IS UNCHANGED]".

**PDF 697, page -451-** (render pp. 6-7)
- The centred "-451-" line.
- "Step 1: forebody drag coefficient (C_Df)_b". "The body skin-friction coefficient is given by".
- (C_f)_B = (C_f)_LAM. = 1.328/√(31.75 × 10^4) = .00236. Checked the uppercase B, the "LAM." with its period,
  and the radical covering the whole of 31.75 × 10^4. The handwritten "1,328" is a decimal point.
- "so the forebody drag coefficient is". (C_Df)_b = .00236 × 1.055 × 59.7 = .149.
- "This represents a decrease of 0.045, or 23.2%, from the transition-flow calculated value of (C_Df)_b."
  A zoom of the render confirms the glyph is %, not ‰.
- "Step 2: base drag coefficient C_Db". C_Db = .029/√.149 = .075.
- "This is an \emph{increase} of 0.009, or 13.6% over the transition-flow calculated value." There is no comma
  after 13.6%, as printed.
- "Step 3: fin drag coefficient (C_Do)_F", set as (C_{D_0})_F. "The fin skin-friction coefficient is".
- (C_f)_F = 1.328/√(3.03 × 10^4) = .00763.
- "Then" (C_Do)_F = 2 × .00763 × 1.158 × 63/2.92 = .381. "Then" is a prose line before the display
  (STYLE.md section 4).
- "This is an increase of 0.191, or \emph{more than double} the value calculated for 60 meters/second."
- The indented paragraph "From these calculations we obtain an overall drag coefficient of", then
  (C_Do)_FB = .149 + .075 + .381 = .605.

**PDF 698, page -452-** (render p. 7)
- The centred "-452-" line.
- The indented paragraph "This is a substantial disagreement with the experimental result---the calculated
  value exceeds the measured value by more than 44%."
- "[REMAINDER OF TEXT ON PAGE 452 IS UNCHANGED]".

**Headings and labels** (from build/unit/s-ch3.aux)
- supp:ch3-symbols: "Corrections and Additions to Symbol Table of Chapter 3".
- supp:ch3-445: "[Corrections to Pages 445, 449, 451 and 452]". This is a bracketed descriptive title for an
  untitled document.
- The pages carry no author, date or signature, and none appears in the render.

## Discrepancies

| where | scan reading | compiled reading | severity |
|---|---|---|---|

none
