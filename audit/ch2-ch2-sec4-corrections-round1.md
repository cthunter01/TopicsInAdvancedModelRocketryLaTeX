# Audit: corrections applied to chapters/ch2-sec4.tex (round 1)

Scope: `git diff HEAD -- chapters/ch2-sec4.tex` (HEAD is the faithful 1973 transcription). Items 4(a)-(c), 5 and 6, plus doubts D15 and D19.
Sources read: 1973 pages p215-p226 and p245; the 1994 supplement p676-p680 (with a 200 dpi zoom of the p678 equations, build/zoom/audit_ch2-sec4_r1-p678-678.png); the 2022 correction p683 and p685 (for the "(90)" citation). Also read STYLE.md sections 4, 7, 9, 10, 11 and 13, and corrections/ch2.md. The unit renders build/unit/ch2-sec4-01..09 and -17.png are newer than the .tex file (05:32:51 against 05:32:38).

## What was checked

1. **Item 4(a) (p676 against 1973 p216-p217).** The replacement starts at "Barrowman's method is based on the concept..." and stops before "Throughout the rest of this treatment", which is the extent the supplement gives in its bracketed instruction. The 1973 display N = C_Na (rho/2) A_r V^2 alpha has been removed, and so have the 1973 where-entries for V and alpha. I compared the new text with the supplement sentence by sentence:
   - the \emph (underline) covers only "normal force coefficient", with C_N outside it;
   - "angle of attack" alpha;
   - N = (rho/2)C_N A_r V^2;
   - the where-list is N, rho, A_r, with "cross-sectional" hyphenated as in the supplement;
   - "[typically 0.2 radian (about 11.5 deg) or less]";
   - C_N = C_Na . alpha;
   - "(C_N = 0, alpha = 0)";
   - C_Na = (dC_N/dalpha)|_{alpha=0};
   - the lift-curve-slope paragraph, with its two underlined terms as \emph and "radians^{-1}".

   All displays are unnumbered. The \ednote sits in "The equation by which this is accomplished is", the sentence that introduces the display. Its quote of the 1973 paragraph, equation and removed where-entries matches p216-p217 and git HEAD.
2. **Item 4(b) (p676-p677 against p217-p218).** The paragraph now matches the supplement word for word. Its note says the 1973 text differs only in "coefficient(s)" at three places, which is true.
3. **Item 4(c).** I counted with a script after removing the notes. Section 4.1 of HEAD, from "Under these conditions" to Section 4.2, has 18 occurrences of "normal force coefficient(s)". The corrected file has 17 renamed and 1 kept, the body-tube paragraph on 1973 p193. I confirmed on the page images that each renamed place is on 1973 pp.190-196 or in the captions of Figures 34-36. Page 189 has only Figures 32 and 33, whose captions do not contain the phrase. These are unchanged, as specified:
   - page 188;
   - the heading on page 185;
   - the A_r entry and the "curve of the normal force coefficient" wording inside the 1994 replacement text (the supplement keeps them);
   - Section 4.7's "like normal force coefficients".

   The single rename \ednote is at the first renamed occurrence, "Under these conditions... analysis:", in the sentence that introduces (79). It states the range, the captions, the exception and the 1973 reading.
4. **Item 5 (p678-p679, 200 dpi zoom, against p223 and p225).**
   - **Extent.** The replacement begins at "The normal force curve slope of a single fin is given by" and ends after (92'). "The longitudinal position of the C.P. of any one fin" continues unchanged.
   - **Equations, symbol by symbol.** Each one matches the supplement:
     - (85): the 1973 form, with \AR, (c_r+c_t)/r_r, s/r_r and \cos\Gamma_c;
     - (86): \AR = 4s/(c_r+c_t);
     - (87): \ell = s/\cos\Gamma_c;
     - the substitution line;
     - (88): 2(s/r_r)^2/[1+\sqrt{1+(2\ell/(c_r+c_t))^2}];
     - (89'): (N/2)(\CNa)_1;
     - tau = (s+r_t)/r_t;
     - (90'): 1+1/tau;
     - (91'): 1+1/(2tau);
     - (92'): K_{T(B)}(\CNa)_T.
   - **Derivation.** I derived (88) from (85)-(87) myself.
   - **Prose.** It matches the supplement sentence by sentence, including "three, four, or six", "is altered by", "not exactly equal to the value predicted by" and "and its value for six-finned configurations is".
   - **Labels and citations.**
     - The labels are ch2:eq:85 to ch2:eq:88, numbered automatically, and ch2:eq:n89 to ch2:eq:n92 with \tag{89$'$} to \tag{92$'$}.
     - The 1973 labels ch2:eq:89 to ch2:eq:92 are kept, and the rendered numbers run (88), (89')-(92'), (89)-(92).
     - The text's citations are \eqref's: (86)/(87) and (85) twice, and (89') twice.
     - No other unit cites ch2:eq:85 to 88. The only outside citation is ch2-sec6's \eqref{ch2:eq:90}, which is the unchanged 1973 (90).
   - **The \ednote.**
     - It sits in the sentence that introduces (85).
     - It quotes the 1973 (85)-(88) and all the replaced 1973 prose exactly as in git HEAD and p223/p225.
     - It explains the (89')-(92') marking and the 2022 citation of (90), which I checked on p685: "Ybar_t is given by equation (90)".
     - It mentions six fins.
     - I verified its mathematics:
       - 1973 (86) = (N/2) x 1973 (85);
       - with the 1994 \AR, (88) and (89') give N(s/r_r)^2/[1+\sqrt{1+(2\ell/(c_r+c_t))^2}];
       - with the 1973 \AR = 2s/(c_r+c_t), the 1973 (86) gives (N/2)(s/r_r)^2/[1+\sqrt{1+(\ell/(c_r+c_t))^2}];
       - so the 1973 value is half as much at small aspect ratio, and the two agree in the large-aspect-ratio limit.
   - **Wording that departs from the task.** The task text asked the note to say the 1994 text "removes the factor-of-two difference between the 1973 (85) and (86)". The note instead says the 1994 text *keeps* the N/2 factor, now written out in (89'), and that the doubled \AR makes the total twice the 1973 value for fins of small aspect ratio. That is mathematically correct: (89') with N = 1 is still half of (88). The task's phrasing would have been inaccurate, so this is not a discrepancy. D16 is covered by the same note.
5. **Item 6 (p680 against p224).**
   - The figure uses figures/supplement/ch2-fig36-1994.png, with the width/height/keepaspectratio form. Its manifest row sup-ch2-fig36-1994 exists and is owned by ch2-sec4. \label{ch2:fig:36} is kept.
   - The typed caption is transcribed in full and verbatim: "tip of the rocket's nose", "and the fin leading edge.", the \ell sentence, and "aspect ratio" as \emph, with ``wing'' and span 2s.
   - The \edcap says the figure and caption are replaced per the June 1994 supplement. It gives the 1973 \AR = 2s/(c_r+c_t), says the 1973 drawing did not mark \ell (true on p224), quotes the 1973 caption exactly as in HEAD and p224, and says the 1973 figure is reproduced in the supplement Part.
6. **D15 (p221, p223).**
   - **Derivation.** Slender-body theory gives the C.P. from the forward end as (L A(L) - V)/(A(L) - A(0)). For a frustum with r_1 forward and r_2 aft, this is (L/3)[1 + r_2/(r_1+r_2)] = (L/3)[1 + (1 - r_1/r_2)/(1 - (r_1/r_2)^2)]. That is Barrowman's form with d_F/d_R, valid for a shoulder and for a boattail alike.
   - **The printed equations.** (82) as printed is L - V/(pi r_2^2) = L[2/3 - (1/3)x(x+1)] with x = r_1/r_2. (84) as printed is V/(pi r_1^2) = (L/3)[1 + y(y+1)] with y = r_2/r_1. Both are the volume-over-base rule, with the A(0) term missing.
   - **Numerical comparison.**

     | case | book | Barrowman |
     |---|---|---|
     | x = 0 (pointed cone) | 2L/3 | 2L/3 (they agree) |
     | x = 1/2 | 0.4167L | 0.5556L |
     | x -> 1 | 0 | L/2 |
     | boattail, y = 0 (pointed cone) | L/3 | L/3 (they agree) |
     | boattail, y -> 1 | L | L/2 |

     Setting the two equal gives x = 0 or y = 0 as the only root in the admissible range. The doubt is therefore confirmed.
   - **The note.** It is neutral. It gives Barrowman's form in the notation of Figures 34 and 35 (r_1 at the forward end, which I checked on p222), and every number in it checks out. It sits in the sentence that introduces (82). It is somewhat longer than "short", but it contains nothing incorrect.
7. **D19 (p245).** The printed sentence is "The coupled and decoupled damping ratios, zeta and zeta_c,". The Symbols list has zeta "damping ratio" and zeta_c "coupled damping ratio". (20) defines zeta with I_L and (70) defines zeta_c with I_L + I_R. The note is accurate and is placed in the sentence.
8. **Scope.**
   - The whole diff has 11 hunks, and each belongs to item 4, 5 or 6, D15 or D19. Nothing else in the file changed, and HEAD had no notes to merge.
   - D17, D18 and D20 have no note, as decided.
   - Nothing in figures/ was touched in this unit.
9. **Renders (pages 1-9 and 17).**
   - The corrected passages are typeset correctly.
   - The numbers run in sequence.
   - The notes run E1 to E6: 4(a), 4(b), 4(c), D15, item 5, D19.
   - The only ?? marks are for other units' labels: ch2:sec:3, ch2:sec:5, ch2:sec:2.2, ch2:eq:20 and ch2:eq:70. That is expected.
   - The log's only box warning is a 2.5 pt overfull \vbox while the D15 footnote splits across pages 4-5. Nothing visible results from it.

## Observations (not discrepancies)

- The corrected text now says "N must be three, four, or six" (1994, before (89')), while the unchanged 1973 page 188 still says "the number of fins must be either three or four". The supplement does not touch p188, and the task says p188 stays unchanged, so this follows the sources.
- The E1 note says the 1994 where-list keeps "the entries for N, rho and A_r given here". The A_r entry differs from 1973 only by the hyphen in "cross-sectional" (1973 prints "cross sectional"), which is a typographic variant.
- The 1994 Figure 36 crop carries a small scanner mark above the drawing. It is present on p680 itself, and figures/ is outside this unit's remit.

## Discrepancies

| where | expected (source/1973) | found | severity |
|---|---|---|---|
| none | | | |
