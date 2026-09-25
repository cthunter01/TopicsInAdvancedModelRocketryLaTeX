# M5 audit: supplement, "Changes to Text of Chapter 4" (round 1)

Scan pages: PDF 699-702 (figures/pages/p699.png ... p702.png), plus zoomed crops of the scan at 300 and
600 dpi (build/zoom/audit_supp-ch4-thrust_r1-p700a..i-700.png, -p701a..c-701.png, -p702a..b-702.png).
Render: build/unit/s-ch4-thrust-1.png and -2.png, plus 300 dpi crops of build/unit/s-ch4-thrust.pdf
(build/zoom/audit_supp-ch4-thrust_r1-render1a/1b-1.png, -render2a/2b/2c-2.png). The unit was not rebuilt.
No .tex file was opened.

## Items checked

PDF 699 (cover note)
- Heading "CHANGES TO TEXT OF CHAPTER 4" (capitals) set as the unnumbered chapter title
  "Changes to Text of Chapter 4", as specified.
- The paragraph, word by word: "The equation for rocket thrust that originally appeared in *Topics in
  Advanced Model Rocketry* was restricted to the case where the rocket's exhaust expands through the
  divergent section of the nozzle until it crosses the nozzle exit plane at a pressure equal to the
  ambient atmospheric pressure. This condition is called "optimal expansion" or "correct expansion"
  and many model rocket motors closely approach it. Some readers were, however, dissatisfied with the
  restriction so I wrote these changes to the text of Chapter 4 to include cases where the exhaust
  pressure is greater or less than the ambient pressure." Italic book title matches. "Chapter 4"
  shows "??" (a chapter reference; the log names ch4, expected in the standalone build).
- Signature "Gordon Mandell" / "June 1994" on two lines, flush left. Matches.

PDF 700
- "[Change text after equation 7 on page 513 to the following:]" centred, "equation 7" without
  parentheses as printed. Matches.
- Paragraph "If the nozzle ... That is,": every word; underlined *exit plane*, *ambient*, *thrust* set
  in italics; inline term −c⃗(dm_e/dt) with the arrow over c only. Matches.
- (7a) F(t) = −c⃗(dm_e/dt): F without an arrow in the scan (zoomed at 600 dpi), none in the render;
  arrow over c. Tag (7a). Matches.
- "If the exhaust gas pressure ... is *not* equal to the ambient pressure, the thrust will be". Matches.
- (7b) F⃗(t) = −c⃗(dm_e/dt) + [arrow over (P_e − P_a)A_e]: the pressure-term arrow runs from the opening
  parenthesis to the subscript e in both scan and render; arrows over F and c only. Tag (7b). Matches.
- "Where A⃗_e = area of nozzle exit plane / P_e = exhaust gas pressure at nozzle exit plane /
  and P_a = ambient pressure": words, subscripts, arrow over A. Matches.
- Paragraph "Most practical rocket motors ... reduction in thrust.": every word, the quoted
  "overexpands"/"underexpands", P_e and P_a inline with correct subscripts. Matches.
- Paragraph "Equation (7) above includes the term ...": both inline pressure terms carry the full-length
  arrow over (P_e − P_a)A_e in scan and render; E⃗ (twice) and F⃗(t) with short arrows; "(7b)" plain;
  "(7)" renders "(??)" (reference to ch4:eq:7, expected standalone). Quoted "pressure component of
  thrust" (period after the closing quote, as printed), "effective", "equivalent". The line that looks
  like underlining under "it as part" is the arrow of the next typed line's pressure term. Checked.
  Inline c_eff: see the table.
- (7c) c_eff = c⃗ − [arrow over (P_e − P_a)A_e]/(dm_e/dt): the pressure-term arrow ends at A_e, before the
  slash, in both. Short arrow over the lone c. Tag (7c). c_eff arrow: see the table.
- "and to write the equation for thrust in the form". Matches.
- (7d) F⃗(t) = −c_eff(dm_e/dt): the minus sign is outside the arrow (zoomed at 600 dpi). Tag (7d).
  c_eff arrow: see the table.
- Last lines "Since the effective exhaust velocity is directed *backward* along the longitudinal axis
  of the rocket it is vectorially *negative* with". Matches.

PDF 701
- "respect to v⃗. And since ... expressed as the *positive* mass-flow rate dm_e/dt, equivalent to ṁ as
  used by professional rocket engineers, the thrust is a *positive* force tending to *increase* v⃗ --
  which, as practical rocketeers, we already know from experience. We can then write the vector
  differential equation of motion as": every word, the emphasis, ṁ with its dot, the "--" as an em
  dash. Matches.
- (8) m(t)(dv⃗/dt) = F⃗(t) + E⃗_o: arrows over v, F, E; subscript o. Tag (8). Matches.
- "Where E⃗_o = vector sum of all externally-applied forces *other than* the pressure component of
  thrust". Matches.
- "Both the engine thrust and the externally-applied forces other than the pressure component of thrust
  will be referred to as *flight forces* as per the notation of Chapter 1," (ends with a comma, as
  printed; "1" renders "??", a ch1 reference). Matches.
- "[End of text on page 513]" and "[Change text at the top of page 514 to the following:]", centred. Match.
- "in the following discussion. The externally-applied flight forces whose vector sum is here
  represented by E_o will be resolved into two components: *weight* and aerodynamic resistance, or
  *drag*." E_o has no arrow in the scan and none in the render; paragraph not indented, as a
  continuation. Matches.
- "[The rest of the text on page 514 is unchanged.]" centred. Matches.
- Page number "2" not transcribed (correct).

PDF 702
- "The table of symbols for Chapter 4 will need to have the following symbols added:" ("4" renders
  "??", a ch4 reference). Matches.
- Symbol list, six rows in printed order, every word: A⃗_e "nozzle exit plane area written as a vector
  whose direction is forward along the vehicle centerline"; E⃗_o "vector sum of all externally-applied
  forces other than pressure component of thrust" (no "the", as printed); F⃗(t) "thrust as a function
  of time"; P_a "ambient pressure"; P_e "pressure of exhaust gas at nozzle exit plane"; c_eff
  "effective exhaust velocity, *also* called equivalent exhaust velocity" (underlined *also*). Match,
  except the c_eff arrow (table).
- "The meaning of F(t) will need to be changed to" / "F(t) magnitude of thrust as a function of time",
  F without an arrow in both. Matches.
- Booktabs rules around the two lists (the typescript has none): accepted convention.
- Page number "3" not transcribed (correct).

General
- No figures, photos, tables with captions or editorial notes in these pages; the render has none.
- Arrows over A_e and E_o: the typewriter arrows sit over the capital (and in the PDF 702 list reach
  partly over the subscript); the render's \vec over the capital is the project's vector form. Not a
  discrepancy.
- The unit log has only the expected undefined references (ch4, ch4:eq:7, ch1, ch4) and no overfull boxes.

## Discrepancies

| where | scan reading | compiled reading | severity |
|---|---|---|---|
| PDF 700 inline "velocity c_eff as", (7c) left side, (7d); PDF 702 symbols list | a long arrow over the whole of c_eff (letter and subscript) in all four places, clearly longer than the short arrow over the lone c in (7c) | arrow over the c only, subscript outside (\vec{c}_{\mathrm{eff}}) | math |

Note on the item above: the vector meant is the same, and the project's STYLE section 15 sets the arrow
"over the letter only", so this may be accepted as the intended form. It is reported because the arrow
extent is on the checklist and the scan draws it over the whole symbol every time, while the render
reproduces the long arrow of the pressure term. To match the scan, set it as
\overrightarrow{c_{\mathrm{eff}}}.
