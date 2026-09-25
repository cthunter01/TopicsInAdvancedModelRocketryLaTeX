# M5 audit: supplement, "Summary: Corrections and Additions to Altitude Equations for 2-Stage and Multistage Rockets" (round 1, part 2)

Scan pages: PDF 707-710 (figures/pages/p707.png ... p710.png; typescript pages 5-8), plus zoomed 300 dpi
crops of the scan (build/zoom/audit_supp-ch4-summary_r1_p2-p707a..e-707.png, -p708a..c-708.png,
-p709a..d-709.png, -p710a..d-710.png) for every handwritten display and the unclear typed glyphs.
Render: build/unit/s-ch4-summary-4.png ... -7.png (content of PDF 707-710 runs from the display at the
foot of render page 4 to the end of render page 7), plus render page 3 as the neighbouring page; text
of build/unit/s-ch4-summary.pdf (pdftotext) used for a word-by-word cross-check. The unit was not
rebuilt. No .tex file was opened.

Boundary: PDF 706 ends "from which, using the exponential definitions of cosh and sinh, we obtain";
PDF 707 starts with the display y2 = (m2/k2) ln[e^((k2t2/m2) v1)]. The render has the sentence and then
the display at the foot of page 4, with nothing lost or duplicated.

## Items checked

PDF 707 (typescript page 5)
- Display y2 = (m2/k2) ln[ e^{( (k2 t2/m2) v1 )} ]: square brackets, parenthesized exponent, v1 outside
  the fraction. Matches.
- "from which" / y2 = v1t2. Matches.
- "The extended Fehskens-Malewicki solution therefore also predicts terminal velocity exactly, despite
  the singularity in the inverse hyperbolic tangent at (v1/vterm) = 1." Matches.
- Paragraph "Describe the case of the low-thrust sustainer ... acceptably accurate results.", word by
  word, including "√2·(vterm)" (radical over 2 only, centred dot, parenthesized vterm) and inline dv/dt.
  Matches.
- Paragraph "Note that the extended Fehskens-Malewicki velocity equation (state equation numbers)
  derived on the assumption ... greater than 1. Explain that the integral". The placeholder
  "(state equation numbers)" kept as printed. Matches.
- Display ∫_{v1}^{v2} m2 dv / (F2 − m2g − k2v^2). Matches.
- "of the extended Fehsksns-Malewicki velocity equation has a different functional form when the
  quantity": the typing slip "Fehsksns" (confirmed in the zoom) is set as "Fehskens" (slip fixed
  silently, allowed). Matches otherwise.
- Display F2 − m2g − k2v^2; "is less than zero. In such cases the integral is". Matches.
- Display m2/√(k2(F2 − m2g)) coth^{-1}[ v √(k2/(F2 − m2g)) ]_{v1}^{v2}: plain v inside the bracket
  (zoomed), limits v1 below and v2 above the closing bracket. Matches.
- "from which the velocity is obtained as" / v2 = √((F2 − m2g)/k2) coth[ (t2/m2)√(k2(F2 − m2g)) +
  coth^{-1}( v1 √(k2/(F2 − m2g)) ) ]. Radical extents, bracket and parentheses match.
- "The altitude increment gained during the second-stage burn can also be determined from this
  equation, by integrating it from t̂ = 0 to t̂ = t2:" with hats on both t. Matches.

PDF 708 (typescript page 6)
- Display y2 = (m2/k2) ln{ sinh[ (t2/m2)√(k2(F2 − m2g)) + coth^{-1}( v1 √(k2/(F2 − m2g)) ) ] /
  sinh[ coth^{-1}( v1 √(k2/(F2 − m2g)) ) ] }: curly braces, square brackets, parentheses. Matches.
- "and through the use of the well-known identity" / sinh(A + B) = sinh(A)cosh(B) + cosh(A)sinh(B).
  Matches.
- "where A and B represent any two quantities, the altitude equation may be cast into the simpler
  form" / y2 = (m2/k2) ln[ v1 √(k2/(F2 − m2g)) sinh( (t2/m2)√(k2(F2 − m2g)) ) + cosh( (t2/m2)√(k2(F2 −
  m2g)) ) ]. Matches.
- "which is identical to equation (58) on page 536 of the original text -- the same result obtained
  for v1 less than vterm. This is expected, since the altitude equation does not have a singularity
  at v1 = vterm as the velocity equation does." The "(58)" shows "(??)" (a chapter reference in the
  standalone build, expected); "on page 536" kept as printed; "--" set as an em dash. Matches.
- "Add the generalization of extended Fehskens-Malewicki solution to rockets of three or more stages
  here." Matches.
- Underlined subheading "Upper Stages With Very Low Thrust" set as an unnumbered section heading.
  Matches.
- Paragraph "Add a section 2.2.4 which discusses ... phase of flight." (lower-case "section" as
  printed). Matches.
- Paragraph "Note that the functional forms ... velocity and altitude increment equations change when
  the thrust becomes equal to the weight (F2 − m2g = 0). Derive and present the Fehskens-Malewicki
  solution for the case where thrust = weight:" with the underlined "and" in italics and no
  "extended" before "Fehskens-Malewicki solution", as printed. Matches.
- v2 = v1 / (1 + (k2/m2) v1 t2); "and"; y2 = (m2/k2) ln(1 + (k2/m2) v1 t2). Matches.
- 'Note that the "terminal velocity" has now become zero ... suddenly shut down.' Matches.
- "Present the generalization of the extended Fehskens-Malewicki equations to rockets of three or more
  stages." Matches.
- "Derive and present the extended Caporaso-Bengen solution for the case where thrust = weight:".
  Matches.

PDF 709 (typescript page 7)
- v2 = v1 / √(1 + (2k2/m2) v1 t2); "and"; y2 = (m2/k2)( √(1 + (2k2/m2) v1 t2) − 1 ) with the −1 outside
  the radical (zoomed). Matches.
- Paragraph "Note that the Caporaso-Bengen solution was originally derived ... if its recovery device
  did not deploy:", word by word, including "1.25 times", inline dv/dt, "vfterm/√2" and "vfterm".
  Matches.
- Display vfterm = √(m2 g/k2). Matches.
- "Present the generalization of the extended Caporaso-Bengen equations to rockets of three or more
  stages." Matches.
- Paragraph 'Note that the functional forms ... change again when the rocket's thrust is less than its
  weight (the case of "boosted coasting"). Derive and present the extended Fehskens-Malewicki solution
  for the case where thrust is less than weight:'. Matches.
- v2 = √((m2g − F2)/k2) tan[ tan^{-1}( v1 √(k2/(m2g − F2)) ) − (t2/m2)√(k2(m2g − F2)) ]. Matches.
- "and" / y2 = (m2/(2k2)) ln[ (v1^2 + (m2g − F2)/k2) / (v2^2 + (m2g − F2)/k2) ]: v1 squared above, v2
  squared below (zoomed). Matches.
- "Derive the present the extended Fehskens-Malewicki solution for the maximum altitude increment and
  boosted coasting time:": the slip "Derive the present" is set as "Derive and present" (slip fixed
  silently, allowed). Matches otherwise.
- t_BC = m2/√(k2(m2g − F2)) tan^{-1}( v1 √(k2/(m2g − F2)) ); "and"; y_BC = (m2/(2k2)) ln( k2v1^2/(m2g −
  F2) + 1 ). The small-capital subscript "BC" is set as upright BC. Matches.

PDF 710 (typescript page 8)
- "Present the generalization of the extended Fehskens-Malewicki equations to rockets of three or more
  stages." Matches.
- "Derive and present the extended Caporaso-Bengen solution for the case where thrust is less than
  weight:". Matches.
- v2 = [m2v1 − (m2g − F2)t2] / √( m2^2 + 2k2t2[ m2v1 − (t2/2)(m2g − F2) ] ); "and"; y2 = [ −m2 +
  √( m2^2 + 2k2t2[ m2v1 − (t2/2)(m2g − F2) ] ) ] / k2. Radical extents, brackets and signs match.
- "Derive the present the extended Caporaso-Bengen solution for the maximum altitude increment and the
  boosted coasting time:": slip fixed silently to "Derive and present"; "and the boosted" kept.
  Matches.
- t_BC = m2v1/(m2g − F2); "and"; y_BC = (m2/k2)( √( k2v1^2/(m2g − F2) + 1 ) − 1 ) with +1 inside and −1
  outside the radical (zoomed). Matches.
- Paragraph 'Note that the Caporaso-Bengen solution for this case predicts the same "boosted" coasting
  time ... only if v1 is not greater than vfterm/√2.' Matches.
- Underlined subheading "Solutions for a Non-Oscillating Rocket in the Coasting Phase" set as an
  unnumbered section heading. Matches.
- "Add a treatment of the extended Caporaso-Bengen solution for the maximum altitude increment and
  coasting time:" / t_c = v_b/g; "and"; y_c = (m_b/k)( √( k v_b^2/(m_b g) + 1 ) − 1 ). Matches.
- "Note that acceptable accuracy can be obtained from the Caporaso-Bengen equations for this case only
  if vb is not greater than vfterm/√2." End of the document; the render ends there too. Matches.

Also checked: paragraph breaks (each blank-line-separated typescript paragraph is a separate paragraph
in the render; text after a display continues unindented, consistently); every connective "and" /
"from which" between displays is a short prose line; no page numbers, running heads or page markers
from the typescript appear in the text.

Typing slips fixed silently in the render (allowed, reported here): "Fehsksns-Malewicki" (PDF 707) as
"Fehskens-Malewicki"; "Derive the present" (PDF 709 and PDF 710) as "Derive and present".

## Discrepancies

none
