# M5 audit: supplement, "Changes to Text of Chapter 4" (round 2)

Scan pages: PDF 699-702 (figures/pages/p699.png ... p702.png), plus zoomed crops of the scan at 600 and
1200 dpi (build/zoom/audit_supp-ch4-thrust_r2-p700a..f-700.png, -p701a..c-701.png, -p702a-702.png).
Render: build/unit/s-ch4-thrust-1.png and -2.png (built 19:22, after the round-1 fix), plus 300 dpi crops
of build/unit/s-ch4-thrust.pdf (build/zoom/audit_supp-ch4-thrust_r2-render1a/1b-1.png,
-render2a/2b-2.png). The unit was not rebuilt. No .tex file was opened.

## Round-1 item re-checked

- c_eff arrow (PDF 700 inline "velocity c_eff as", (7c) left side, (7d); PDF 702 symbols list): the
  scan draws one long arrow over the whole of c_eff (letter and subscript) in all four places, longer
  than the short arrow over the lone c in (7c). The render now draws a long arrow over c and "eff" in
  all four places (inline, (7c), (7d), symbols list), and the lone c in (7c) keeps its short \vec
  arrow. **Fixed.**
- (7d): the minus sign stays outside the long arrow in the scan (600 dpi: the arrow starts at the c) and
  in the render. Matches.

## Everything else re-checked

PDF 699 (cover note)
- Heading "CHANGES TO TEXT OF CHAPTER 4" set as the unnumbered chapter title "Changes to Text of
  Chapter 4", as specified.
- The paragraph, word by word ("The equation for rocket thrust ... than the ambient pressure."),
  including the italic *Topics in Advanced Model Rocketry*, "rocket's", the quoted "optimal
  expansion" and "correct expansion". "Chapter 4" renders "Chapter ??" (a ch4 reference, expected in
  the standalone build). Matches.
- Signature "Gordon Mandell" / "June 1994", two lines, flush left. Matches.

PDF 700
- "[Change text after equation 7 on page 513 to the following:]" centred, "equation 7" without
  parentheses, as printed. Matches.
- "If the nozzle ... That is,": every word; *exit plane*, *ambient*, *thrust* in italics; the
  quotes "optimum expansion" and "correct expansion", (comma after the closing quote, as printed);
  inline −c⃗(dm_e/dt). Matches.
- (7a) F(t) = −c⃗(dm_e/dt): no arrow over F (600 dpi), arrow over c. Tag (7a). Matches.
- "If the exhaust gas pressure ... is *not* equal to the ambient pressure, the thrust will be". Matches.
- (7b) F⃗(t) = −c⃗(dm_e/dt) + [long arrow over (P_e − P_a)A_e]: arrows over F and c only; the
  pressure-term arrow spans the opening parenthesis to A_e. Tag (7b). Matches.
- "Where A⃗_e = area of nozzle exit plane / P_e = exhaust gas pressure at nozzle exit plane / and P_a =
  ambient pressure": words, subscripts, the arrow over A (600 dpi). Matches.
- "Most practical rocket motors ... a reduction in thrust.": every word, "convergent/divergent", the
  quoted "overexpands" and "underexpands", P_e and P_a with correct subscripts. Matches.
- "Equation (7) above includes the term [arrow (P_e − P_a)A_e] as one component of E⃗, the vector sum
  of all externally-applied forces. It is more convenient for calculation purposes, however, to extract
  it from E⃗ and write it as part of the thrust F⃗(t) as in equation (7b) above. Indeed, [arrow
  (P_e − P_a)A_e] is part of the thrust measured in a static test stand and is referred to as the
  "pressure component of thrust". It is then possible to define an "effective" or "equivalent" exhaust
  velocity c_eff as": every word and symbol. Zoomed at 1200 dpi: the stroke that looks like an underline
  under "more" is the arrow over the E of "from E" on the next line (the E carries an arrow, and the
  render has E⃗ there); the stroke under "purposes," is the arrow over F of the next line; the stroke
  under "it as part" is the arrow of the next line's pressure term. "(7)" renders "(??)" (ch4:eq:7,
  expected standalone); "(7b)" plain. Matches.
- (7c) c_eff⃗ = c⃗ − [arrow (P_e − P_a)A_e]/(dm_e/dt): the pressure-term arrow ends at A_e before the
  slash in both. Tag (7c). Matches.
- "and to write the equation for thrust in the form". Matches.
- (7d) F⃗(t) = −c_eff⃗(dm_e/dt). Tag (7d). Matches.
- "Since the effective exhaust velocity is directed *backward* along the longitudinal axis of the rocket
  it is vectorially *negative* with". Matches.

PDF 701
- "respect to v⃗. And since the rate of mass expulsion has been expressed as the *positive* mass-flow
  rate dm_e/dt, equivalent to ṁ as used by professional rocket engineers, the thrust is a *positive*
  force tending to *increase* v⃗ -- which, as practical rocketeers, we already know from experience.
  We can then write the vector differential equation of motion as": every word, emphasis, ṁ with its
  dot, "--" as an em dash. The mark under the end of "rocket" is the arrow over the v of the next line
  (600 dpi). Matches.
- (8) m(t)(dv⃗/dt) = F⃗(t) + E⃗_o: arrows over v, F and E; subscript o. Tag (8). Matches.
- "Where E⃗_o = vector sum of all externally-applied forces *other than* the pressure component of
  thrust". Matches.
- "Both the engine thrust and the externally-applied forces other than the pressure component of thrust
  will be referred to as *flight forces* as per the notation of Chapter 1," (trailing comma as printed;
  "1" renders "??", a ch1 reference). Matches.
- "[End of text on page 513]" and "[Change text at the top of page 514 to the following:]", centred.
  Match.
- "in the following discussion. The externally-applied flight forces whose vector sum is here
  represented by E_o will be resolved into two components: *weight* and aerodynamic resistance, or
  *drag*.": E_o without an arrow in scan (600 dpi) and render; not indented (continuation). Matches.
- "[The rest of the text on page 514 is unchanged.]" centred. Matches.
- Page number "2" not transcribed (correct).

PDF 702
- "The table of symbols for Chapter 4 will need to have the following symbols added:" ("4" renders
  "??", a ch4 reference). Matches.
- Symbol list, six rows in printed order: A⃗_e "nozzle exit plane area written as a vector whose
  direction is forward along the vehicle centerline"; E⃗_o "vector sum of all externally-applied forces
  other than pressure component of thrust" (no "the", as printed); F⃗(t) "thrust as a function of
  time"; P_a "ambient pressure"; P_e "pressure of exhaust gas at nozzle exit plane"; c_eff (long arrow)
  "effective exhaust velocity, *also* called equivalent exhaust velocity". Match.
- "The meaning of F(t) will need to be changed to" / "F(t) magnitude of thrust as a function of time",
  F without an arrow in both. Matches.
- Booktabs rules around the two lists (none in the typescript): accepted convention.
- Page number "3" not transcribed (correct).

General
- No figures, photos, captioned tables or editorial notes on these pages; the render has none.
- Arrows over A_e and E_o over the capital only (\vec): project vector form, as in round 1.
- Paragraph indentation and the compact "Where" lists differ from the block-style typescript: layout
  of the edition, not a discrepancy.
- The unit log has only the expected undefined references (ch4, ch4:eq:7, ch1, ch4).

## Discrepancies

none
