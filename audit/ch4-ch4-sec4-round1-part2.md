# Audit ch4-sec4, round 1, part 2 (scan PDF 622-633)

## 1. Pages and items checked

Scan pages: PDF 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633. I read each page separately and zoomed at 300 dpi on the displays of 622, 624 and 625, on Table 1 (627) and on all four Table 2 pages (628-631). I also zoomed at 200 dpi on the prose of 623 and 625 to check for underlining.
Render pages: build/unit/ch4-sec4-05.png to ch4-sec4-11.png. My content is on render pages 6-11; page 5 is the page before it.

Items checked:
- **Headings (3):** 4.3.3 Impulse Response; 4.3.4 Response to Sinusoidal Forcing; 4.4 The Effect of Dynamic Oscillations on the Altitude Performance of a Typical Model Rocket.
- **Numbered equations (16):** (160a), (160b), (160c) with the brace "t = t_o"; (161); (162a), (162b); (163a), (163b) with the connective "and" set as a prose line; (164a), (164b); (165a), (165b); (166a), (166b) with the brace "t = 0". Every symbol, subscript, fraction, brace extent, condition and number matches. The sequence runs on from (159) with no offset.
- **Inline math:** M_x, M_y, t_o (3 times), H_x, H_y (twice), f_x(t), f_y(t), A_f, ω_f, A_o, ω_o, t = 0, α, C_1, v^2, I_R, ω_z, I_R ω_z, I_L. All match.
- **Citations:**
  - Literal, with no note: (189) on PDF 622 and (195) on PDF 623.
  - Literal, with an \ednote: (200a) on PDF 625. The note's statement, "No equation carries the number (200a); equation (165a) is evidently meant", is correct.
  - Shown as "??" in the standalone build, as expected: Chapter 2 (5 times), Sections 3.1.4 and 3.2.4 of Chapter 2, Figure 37 of Chapter 3 (text and both captions), and Section 5.3 of Chapter 3.
  - Linked: Section 4.3.1, Section 4.2, Table 1 and Table 2.
- **Lists:** the lettered list (a)-(b) on PDF 623-624 and the ranked list (a)-(d) on PDF 632.
- **Prose:** every sentence on PDF 622-626 and 632-633, compared by eye and by a word-level diff against the OCR layer. The only differences are OCR noise. Emphasis matches: complete, steady-state, starting transients (625); strength (632); angular momentum, angle of attack, reduced, persist, longer time, and "causes the model to act as if it had a larger longitudinal moment of inertia than its actual value of" (633). No other underlining appears on these pages; I checked 622-626 by zoom. Paragraph indents and non-indents after displays all match. "multi-/staged" is rejoined as "multistaged", the chapter's usual spelling.
- **Table 1 (PDF 627):** the caption, the 2 header cells, 20 rows × 2 cells (the k row has 3 lines) and the table number.
- **Table 2 (PDF 628-631):** the caption (typed on PDF 629, set above), 10 header cells, and 26 rows × 10 cells = 260 cells. Rows 1-17 and 18-26 of the left half were matched to the right half by position, and every cell matches. The survey's readings of Tables 1 and 2 are confirmed.
- **Survey briefing (build/ch4-notes/ch4-sec4.md):** its list of numbered items, headings, emphasis and table data for PDF 622-633 is confirmed. I found no difference from the survey.

## 2. Discrepancies

none

## Observations (not counted as discrepancies)

- **Footnote placement (layout only):** the text of footnote E1 is printed at the bottom of render page 9, two pages after its mark on render page 7 ("Equation (200a)^E1"). Render page 8 is the Table 1 float page. This is a page-break effect of the standalone build.
- **Table 2, row 1, t_o cell:** the typescript's placeholder "----" is set as an em dash "—". I treat this as the typographic equivalent of the typed dash.
