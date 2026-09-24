# Chapter 2 — corrections checklist

Sources: 1973 errata sheet (PDF 664/665); "Correction to original pages 186 through 196 of Chapter 2" (PDF 676-677, 1994);
"Corrections and clarifications to fin normal force curve slope equations on page 195" (PDF 678-679, typed text with handwritten equations);
new Figure 36 (PDF 680); handwritten 1994 corrections to equations (115)-(117) (PDF 681-682, superseded);
"Corrections to pages 251 through 254 and 259" (PDF 683-687, Mandell 15 Feb 2022, adds Figure 52 and Reference 12).
Printed page = PDF page − 30.

Status: todo / applied (with \ednote location) / deferred (reason)

| # | Source (PDF) | Original location | Change | Status |
|---|---|---|---|---|
| 1 | 664 | p.108 (PDF 138), last line of the Figure 13 caption | should read "$\alpha_{X0}$ as if encased in very thick glue or tar." (the caption is missing its $\alpha$; typo-level fix, note optional) | todo |
| 2 | 664 | p.113 (PDF 143), equation (30) | should read $\alpha_X = A e^{-Dt}\sin(\omega t + \varphi) + M_s/C_1$ | todo |
| 3 | 664 | pp.144-145 (PDF 174-175) | the A, B, C in the last two equations on p.144 and the first two on p.145 should be A′, B′, C′ | todo |
| 4 | 676-677 | §4.1, pp.186-196 (PDF 216-226) | replacement paragraphs (unnumbered equations) for the Barrowman-method introduction; global rename "normal force coefficient" → "normal force curve slope" on pp.189-196 including the captions of Figures 34-36, except the paragraph on p.193 | todo |
| 5 | 678-679 | from the bottom of p.193 through p.195 (PDF 223-225) | replacement text with the fin normal-force-curve-slope equations (85)-(92) (handwritten in the supplement) | todo |
| 6 | 680 | p.194 (PDF 224), Figure 36 | replacement figure (fin geometry notation) with typed caption; keep the 1973 figure for the supplement Part | todo |
| 7 | 683-687 | p.251 (PDF 281), equation (115) and its text | replace with the 2022 text and new (115) | todo |
| 8 | 684, 687 | p.252 (PDF 282), below Figure 51 | add Figure 52 "Roll Rates to Avoid to Keep ARc from Exceeding 1.25/Cl" (use the larger copy on PDF 687) | todo |
| 9 | 685-686 | p.253 and the top of p.254 (PDF 283-284) | replace with the 2022 text and equations (116), (117) | todo |
| 10 | 686 | p.259 (PDF 289), References | add Reference 12 | todo |
| 11 | 681-682 | (handwritten 1994 version of items 7 and 9) | superseded by the 2022 document: not applied; reproduced in the supplement Part with a note | deferred (superseded) |

Notes
- Numbering conflict to resolve when applying item 5: the 1994 fin correction's "(90)" vs. the 2022 text (items 7, 9) citing "equation (90)" for $\bar{Y}_T$; decide from the content and record the decision in the \ednote.
- Figure 52 is new: it needs a manifest row (PDF 687), output figures/supplement/ch2-fig52-2022.png, and a figure environment after Figure 51; label ch2:fig:52.

Doubts noted during the faithful transcription (2026-09-24). Each is a reading of the 1973 page, kept as printed.
In the corrections step, give each one an \ednote unless an item above already covers it. Notation follows STYLE.md section 13.

| # | Unit | PDF | Doubt | Status |
|---|---|---|---|---|
| D1 | ch2-symbols | 85-92 | $F(\alpha_X)$ is glossed "function of pitch angle" and $G(\Omega_X)$ "function of pitch angular velocity", but the list defines $\alpha_X$ as the yaw angle; $f_x(t)$ is "pitch forcing function", $f_y(t)$ "yaw forcing function" | todo |
| D2 | ch2-sec2 | 121 | $f_x(t)$ is read as the forcing "about the X-axis" (yaw), against the Symbols list's "pitch forcing function" (see D1) | todo |
| D3 | ch2-sec3a | 125 | the first-derivative formula has the cosine term as $A\omega D e^{-Dt}$; the substituted expression below uses $A\omega$ | \ednote added in the faithful pass ("The cosine term of the first-derivative formula ...") |
| D4 | ch2-sec3a | 133 | "substitute $C_2/I_L$ for $D$" although $D = C_2/2I_L$ was just obtained | \ednote added ("Printed $C_2/I_L$ ...") |
| D5 | ch2-sec3a | 136 | first term of the substituted overdamped expression has bare $A$ instead of $A_1$ | \ednote added ("The first term ...") |
| D6 | ch2-sec3a | 143 | equation (30) lacks $+M_s/C_1$ | \ednote added ("Equation (30) ..."); errata item 2 covers the same fix: merge that note into the item-2 note |
| D7 | ch2-sec3a | 137 | "The constants $A_1$ and $A_2$ in equation (25)" although they appear in (24) | \ednote added after the \eqref ("... appear in equation (24) ...") |
| D8 | ch2-sec3b | 158 | the unnumbered zero-angular-velocity display before (43a) has a factor $t$ in both numerators that differentiating (40) does not give ((43a) is unaffected) | todo |
| D9 | ch2-sec3c | 178 | the expression for $b^2$ lacks the factor $1/2$ before the radical that $a^2$ and the roots (54) carry | todo |
| D10 | ch2-sec3d | 204 | the left-hand side $A_r\{[\ldots]^2 + C_2^2\omega_Z^2\}$ has the opposite sign from the preceding line (the book takes magnitudes to reach (68b)) | todo |
| D11 | ch2-sec5 | 263 | (113) writes $t_{\mathrm{MAX}}$ in the display while the prose writes $t_{\max}$ | todo |
| D12 | ch2-sec6 | 265 | "tested according to the methods of Section 6": the methods are in Section 5 | \ednote added |
| D13 | ch2-sec6 | 284 | cites Figure 52, which the 1973 book lacks | \ednote added; item 8 above adds the figure: then make it Figure~\ref{ch2:fig:52} and reword the note |
| D14 | ch2-sec6 | 281-283 | (115) letters the fin span like a capital $S$ (transcribed $s$, the Symbols list's typed form) and the root chord like $C_r$ (transcribed $c_r$, as in (89), (90) and the Symbols list); the p283 prose types $\bar{Y}_t$ while (90), (115) and the Symbols list have $\bar{Y}_T$ (both kept as printed). Items 7 and 9 replace these equations | todo |
| D15 | ch2-sec4 | 221, 223 | (82) and (84) take the C.P. as volume over base area, which drops the $A(0)$ term of Barrowman's frustum formula: right only for a pointed cone (item 4 replaces this text) | todo |
| D16 | ch2-sec4 | 225 | the single-fin (85) has $(c_r + c_t)/r_r$ but (86) has $N(c_r + c_t)/(2r_r)$, so (86) with $N = 1$ is half of (85) (item 5 replaces these equations) | todo |
| D17 | ch2-sec4 | 237, 241 | the prose types the inner radius $R_1$ (as the Symbols list does) while (103b) and (105b) letter $R_i$; both kept as printed | todo |
| D18 | ch2-sec4 | 242 | the second term of (108a) is the exact integral over the trapezoidal fin only when $r_t = 0$ (the text calls the result a good approximation) | todo |
| D19 | ch2-sec4 | 245 | "The coupled and decoupled damping ratios, $\zeta$ and $\zeta_c$" lists the symbols in the reverse order | todo |
| D20 | ch2-sec4 | 229 | a 3 by 36 inch balsa sheet is 696.8 square centimeters; the book says 698 | todo |

Fixed silently in the faithful pass as typographical slips (STYLE.md section 3), recorded here because they touch displays or sentence ends:
PDF 183 (ch2-sec3c), the second row of the right-hand bracket lacks the closing parenthesis of $(D_2^2 + \omega_2^2 - D_1D_2 - \omega_1\omega_2)$; PDF 200 (ch2-sec3d), the last sentence of 3.2.3 lacks its full stop.
Editorial notes are identified above by their opening words, not by number: the E-numbers shift whenever a note is added.
