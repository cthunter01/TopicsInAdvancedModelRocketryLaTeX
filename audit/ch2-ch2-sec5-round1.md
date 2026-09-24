# Audit: ch2-sec5 (5. Experimental Determination of the Dynamic Parameters), round 1

## Scope checked

Scan pages read: figures/pages/p245.png through p265.png (21 pages, one Read per page).
The unit's text actually spans PDF p246 (book -216-, heading "5.") through PDF p264
(book -234-, last sentence "Equation (114) determines C_2 in units of dyne-centimeter-seconds.");
"6. Model Rocket Design" begins on PDF p264, one page later than the task statement said.
p245 and p265 were read only to confirm the boundaries and contain no text of this unit.

Render pages read: build/unit/ch2-sec5-1.png through ch2-sec5-9.png (all 9).

Zooms rendered (STYLE.md section 4) for glyph checks: build/zoom/sec5-p251-Ts-251.png
(typed subscripts I_s, T_s), sec5-p249-eq110-249.png, sec5-p252-eq111-252.png
(eqs 111 and 112), sec5-p263-eq113-263.png.

Items compared, symbol by symbol / sentence by sentence:

| item | count | result |
|---|---|---|
| headings (5., 5.1, 5.2, 5.3) with numbers | 4 | match |
| numbered displays (110)-(114), sequence and placement | 5 | match, no offset |
| unnumbered displays | 0 | - |
| "where" list rows after (110) (M, R, L) | 3 | match |
| inline formulas / symbols (I_s, T_s, T_L, T_R, I_L, I_R, C_1, C_2, alpha_0, alpha_1, t_max, D, ln(alpha_0/alpha_1), degree values, equation citations) | 43 | match |
| figure captions 43-47, word by word | 5 | match |
| prose paragraphs (1 intro + 9 in 5.1 + 11 in 5.2 + 6 in 5.3), plus 3 unindented continuations after displays | 27 (+3) | match: wording, order, paragraph breaks, emphasis, quotes |
| emphasis (reference standard; period of torsional oscillation; period; cycle; and back again; ten; design; record; overshoot; and) | 10 | all set italic |
| pasted-in correction "15 meters" (p252) | 1 | present |

Notes (not discrepancies, per the task's intended-change list): cross-unit references to
Figure 7, Sections 2.2, 4.7, 3.1.1, 3.1.2 and equations (32), (16) render as "??"; "--"
rendered as em dash; underlining as italics; Figure 46(a) data table remains inside the
image; t_max is lowercase in prose and "MAX" in eq. (113) exactly as in the typescript.

## Discrepancies

| where | scan reading | compiled reading | severity |
|---|---|---|---|

none
