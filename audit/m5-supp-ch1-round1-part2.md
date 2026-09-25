# M5 audit: supplement, Chapter 1 documents (round 1, part 2)

Scan pages: PDF 672, 673, 674, 675 (figures/pages/p672.png to p675.png), plus PDF 44 for the
1973 Figure 2 caption. Render: build/unit/s-ch1-4.png to s-ch1-8.png (page 4 carries the end of
PDF 671 and all of PDF 672; page 5 = PDF 673; page 6 = PDF 674; page 7 = the editorial line and
the 1973 Figure 2; page 8 = PDF 675). Page 3 was not needed: page 4 opens with PDF 671 text
belonging to the other auditor.

Zooms (300 dpi scan, 250 dpi render): build/zoom/audit_supp-ch1_r1_p2-p674cap-674.png,
-p675eq-675.png, -p675eq22-675.png, -p672num-672.png, -r5-5.png, -r6-6.png.

## Items checked

PDF 672 (render p. 4)
- Continuation "I_sp a given type of propellant ... infinite exit plane area.": every word and
  the inline math (P_e = P_a = 0) match.
- The paragraph "Model rocket engines using pressed blackpowder ...": the numbers 48 to 103, 175
  and 240 were zoomed and match, as do "high-performance, ammonium perchlorate/polyurethane" and
  the paragraph break.
- The paragraph "The specific impulse delivered ...": "equation (7)", "c_eff = c", "equation
  (2a)", "engine's thrust-time curve" and the rest of the wording match. The references resolve
  to ch1:eq:7 and ch1:eq:n2a. Both labels exist in chapters/*.tex, so the "??" is only the
  standalone build.
- Bracketed instructions "[End of Section 2.1]" and "[Section 2.2 and remainder of Chapter 1 are
  unchanged]" are centred and in the right order. The references go to ch1:sec:2.1, ch1:sec:2.2
  and ch1, and all three labels exist.

PDF 673 (render p. 5)
- Lead sentence "The table of symbols for Chapter 1 will need to have the following symbols
  added:" matches; its reference goes to ch1.
- All five entries match in order, symbol and wording. The arrow of \vec{A}_e sits over the A
  alone, as in the scan. The symbols are A_e, P_a, P_e and c_eff, and the underlined "also" is set
  as \emph. Booktabs rules stand in for the typescript's layout, which is intended.

PDF 674 (render p. 6)
- The figure image (the 1994 Figure 2) is present and complete: three rockets, the +y/+x axes,
  P_a, A_e, P_e, F, Δm_e, c and the equation labels along the bottom edge.
- Caption checked word by word:
  - "Figure 2:" is bold as printed, and "Origin of Rocket Thrust." keeps the printed capitals.
  - Δt, Δm_e, \vec c, (-y), dt, dm_e, dm_e/dt and ṁ match. The "--" dashes are set as em dashes.
  - "-c⃗(dm_e/dt)", (+y) and P_e match.
  - The emphasis matches: "nozzle exit plane", "ambient" and "thrust" are underlined in the scan
    and italic in the render.
  - "\vec A_e" matches, and the long arrow covers the whole of "(P_e - P_a)A_e". The zoom settles
    what looks like an underline under "the nozzle" on the line above: it ends in an arrowhead and
    spans exactly "(Pe - Pa)Ae", so it is that overarrow and not emphasis. The render is correct.
  - "greater than P_a", "less than P_a" and "rocket's thrust F⃗:" match.
- Displayed equation "F⃗ = -c⃗(dm_e/dt) + overarrow{(P_e - P_a)A_e}" matches symbol by symbol,
  including the arrow extents.
- The "NOTE:" paragraph matches word for word, with NOTE underlined in the scan and italic in the
  render, and the colon upright.

Editorial line and the 1973 figure (render p. 7)
- "[Editor's note: The 1973 Figure 2, which this figure replaces:]" is true: PDF 44 carries the
  1973 figure, and PDF 674 replaces it.
- figures/ch1/fig02.png matches the drawing on PDF 44.
- The 1973 caption was checked against PDF 44 word by word:
  - "Figure 2: Origin of rocket thrust." has the lower-case "rocket thrust" and no bold, as
    printed.
  - Δt, Δm_e, \vec c, (-y), "In the limit", dm_e, the "mass flow rate" dashes, dm_e/dt and ṁ
    match.
  - "The thrust F⃗ is given by the equation F⃗ = -c⃗(dm_e/dt) and thus acts in the (+y)
    direction." matches.

PDF 675 (render p. 8)
- The heading "CORRECTION TO ORIGINAL PAGE 40 OF CHAPTER 1" becomes the \chapter "Correction to
  Original Page 40 of Chapter 1" with the label supp:ch1-page40 (checked in the .aux), and it
  appears in the TOC.
- Paragraph 1 matches, including "James Barrowman", "Chapter 2" (reference to ch2),
  "\emph{normal force}", "(i.e., one perpendicular to the model's centerline)" and "given by".
- The equations were checked symbol by symbol from zooms:
  - (20) N = (1/2)ρ C_N A_r v^2
  - (21) C_N = C_{Nα}·α
  - (22) N = (1/2)ρ C_{Nα} A_r v^2 α
- The printed numbers (20), (21) and (22) are kept. The .aux has no equation labels, only
  supp:ch1 and supp:ch1-page40, so the equations are \tag without \label as required.
- In (22) the typewriter's final α sits low, near subscript height. It is the multiplier α (as in
  (21) and as the sense requires), and the render's baseline α is correct. This is not a
  discrepancy.
- The paragraph "where C_N is the normal force coefficient ..." matches, including "Chapter 2",
  "not too large C_N is very nearly directly proportional to α" and "with α".
- The paragraph "where C_Nα is the slope ... normal force curve slope. Then" matches, with the
  emphasis in place.
- The paragraph "The component of force N sin α ... drag, ... N cos α is a side force ... shown in
  Figure 7." matches, with the emphasis on drag and side force. The reference goes to ch1:fig:7,
  and that label exists.
- "[All subsequent equation numbers must be increased by 2]" matches. The red caret "a" in the
  scan ("incre^sed") is transcribed as "increased", which is correct.

All labels used in these pages exist in chapters/*.tex: ch1, ch2, ch1:eq:7, ch1:eq:n2a,
ch1:sec:2.1, ch1:sec:2.2 and ch1:fig:7.

## Discrepancies

none
