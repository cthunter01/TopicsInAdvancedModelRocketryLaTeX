# Chapter 2 — corrections checklist

Sources: 1973 errata sheet (PDF 664/665); "Correction to original pages 186 through 196 of Chapter 2" (PDF 676-677, 1994);
"Corrections and clarifications to fin normal force curve slope equations on page 195" (PDF 678-679, typed text with handwritten equations);
new Figure 36 (PDF 680); handwritten 1994 corrections to equations (115)-(117) (PDF 681-682, superseded);
"Corrections to pages 251 through 254 and 259" (PDF 683-687, Mandell 15 Feb 2022, adds Figure 52 and Reference 12).
Printed page = PDF page − 30.

Status: todo / applied (with \ednote location) / deferred (reason). Corrections applied 2026-09-24; audits in audit/ch2-*-corrections-round*.md.

| # | Source (PDF) | Original location | Change | Status |
|---|---|---|---|---|
| 1 | 664 | p.108 (PDF 138), last line of the Figure 13 caption | should read "$\alpha_{X0}$ as if encased in very thick glue or tar." (the caption is missing its $\alpha$; typo-level fix, note optional) | applied silently (typographical): Figure 13 caption, ch2-sec3a; the faithful-pass \edcap removed |
| 2 | 664 | p.113 (PDF 143), equation (30) | should read $\alpha_X = A e^{-Dt}\sin(\omega t + \varphi) + M_s/C_1$ | applied: (30) in ch2-sec3a, \ednote on "...is therefore" (merged with D6) |
| 3 | 664 | pp.144-145 (PDF 174-175) | the A, B, C in the last two equations on p.144 and the first two on p.145 should be A′, B′, C′ | applied: primes in the expanded cubic and its three coefficient equations, ch2-sec3c, \ednote on "which, when expanded, becomes" |
| 4 | 676-677 | §4.1, pp.186-196 (PDF 216-226) | replacement paragraphs (unnumbered equations) for the Barrowman-method introduction; global rename "normal force coefficient" → "normal force curve slope" on pp.189-196 including the captions of Figures 34-36, except the paragraph on p.193 | applied: ch2-sec4 Section 4.1; \ednotes on "The equation by which this is accomplished is", at the end of the "Now the normal force curve slope" paragraph, and at the first renamed occurrence (rename range and the p.193 exception); section heading keeps its 1973 wording |
| 5 | 678-679 | from the bottom of p.193 through p.195 (PDF 223-225) | replacement text with the fin normal-force-curve-slope equations (85)-(92) (handwritten in the supplement) | applied: ch2-sec4, (85)-(88) and (89')-(92') (see Decisions), \ednote on "The normal force curve slope of a single fin is given by"; p.188's "three or four" sentence has a note that the 1994 text admits six fins |
| 6 | 680 | p.194 (PDF 224), Figure 36 | replacement figure (fin geometry notation) with typed caption; keep the 1973 figure for the supplement Part | applied: figures/supplement/ch2-fig36-1994.png with the 1994 caption and an \edcap; the 1973 figure (owner "supplement") waits for the supplement Part (M5) |
| 7 | 683-687 | p.251 (PDF 281), equation (115) and its text | replace with the 2022 text and new (115) | applied: ch2-sec6 Section 6.3, \ednote after "...spin in model rockets." (quotes the 1973 (115) and the 1994 A_f/A_r explanation) |
| 8 | 684, 687 | p.252 (PDF 282), below Figure 51 | add Figure 52 "Roll Rates to Avoid to Keep ARc from Exceeding 1.25/Cl" (use the larger copy on PDF 687) | applied: Figure 52 after Figure 51 (ch2:fig:52), figures/supplement/ch2-fig52-2022.png, \edcap in the caption |
| 9 | 685-686 | p.253 and the top of p.254 (PDF 283-284) | replace with the 2022 text and equations (116), (117) | applied: ch2-sec6, \ednote on "where:" (quotes the 1973 (116), (117)); the 2022 $\alpha_0$ carries a note on its second sense |
| 10 | 686 | p.259 (PDF 289), References | add Reference 12 | applied: ch2-refs item 12 (ch2:ref:12) with an \ednote |
| 11 | 681-682 | (handwritten 1994 version of items 7 and 9) | superseded by the 2022 document: not applied; reproduced in the supplement Part with a note | deferred (superseded) |

Notes
- Numbering conflict to resolve when applying item 5: the 1994 fin correction's "(90)" vs. the 2022 text (items 7, 9) citing "equation (90)" for $\bar{Y}_T$; decide from the content and record the decision in the \ednote.
- Figure 52 is new: it needs a manifest row (PDF 687), output figures/supplement/ch2-fig52-2022.png, and a figure environment after Figure 51; label ch2:fig:52.

Doubts noted during the faithful transcription (2026-09-24). Each is a reading of the 1973 page, kept as printed.
In the corrections step, give each one an \ednote unless an item above already covers it. Notation follows STYLE.md section 13.

| # | Unit | PDF | Doubt | Status |
|---|---|---|---|---|
| D1 | ch2-symbols | 85-92 | $F(\alpha_X)$ is glossed "function of pitch angle" and $G(\Omega_X)$ "function of pitch angular velocity", but the list defines $\alpha_X$ as the yaw angle; $f_x(t)$ is "pitch forcing function", $f_y(t)$ "yaw forcing function" | applied: \ednote on the $F(\alpha_X)$ row (hbox cell) |
| D2 | ch2-sec2 | 121 | $f_x(t)$ is read as the forcing "about the X-axis" (yaw), against the Symbols list's "pitch forcing function" (see D1) | applied: \ednote in the PDF 121 sentence reading $f_x(t)$, $f_y(t)$ |
| D3 | ch2-sec3a | 125 | the first-derivative formula has the cosine term as $A\omega D e^{-Dt}$; the substituted expression below uses $A\omega$ | \ednote (faithful pass, reworded in the corrections step) |
| D4 | ch2-sec3a | 133 | "substitute $C_2/I_L$ for $D$" although $D = C_2/2I_L$ was just obtained | \ednote (faithful pass, reworded) |
| D5 | ch2-sec3a | 136 | first term of the substituted overdamped expression has bare $A$ instead of $A_1$ | \ednote (faithful pass, reworded) |
| D6 | ch2-sec3a | 143 | equation (30) lacks $+M_s/C_1$ | merged into the item-2 note |
| D7 | ch2-sec3a | 137 | "The constants $A_1$ and $A_2$ in equation (25)" although they appear in (24) | \ednote (faithful pass, reworded) |
| D8 | ch2-sec3b | 158 | the unnumbered zero-angular-velocity display before (43a) has a factor $t$ in both numerators that differentiating (40) does not give ((43a) is unaffected) | applied: \ednote on "Finally, in the case of overdamped motion the applicable equation is" (confirmed by differentiating (40)) |
| D9 | ch2-sec3c | 178 | the expression for $b^2$ lacks the factor $1/2$ before the radical that $a^2$ and the roots (54) carry | applied: \ednote before the $b^2$ display (algebra confirmed) |
| D10 | ch2-sec3d | 204 | the left-hand side $A_r\{[\ldots]^2 + C_2^2\omega_Z^2\}$ has the opposite sign from the preceding line (the book takes magnitudes to reach (68b)) | applied: \ednote on "This can readily be transformed into" (holds above the effective natural frequency; the note says so) |
| D11 | ch2-sec5 | 263 | (113) writes $t_{\mathrm{MAX}}$ in the display while the prose writes $t_{\max}$ | applied silently: (113) uses $t_{\max}$ |
| D12 | ch2-sec6 | 265 | "tested according to the methods of Section 6": the methods are in Section 5 | \ednote (faithful pass), unchanged |
| D13 | ch2-sec6 | 284 | cites Figure 52, which the 1973 book lacks | resolved by items 8 and 9: the 1973 sentence was replaced; the 2022 text cites Figure 52 by \ref |
| D14 | ch2-sec6 | 281-283 | (115) letters the fin span like a capital $S$ (transcribed $s$, the Symbols list's typed form) and the root chord like $C_r$ (transcribed $c_r$, as in (89), (90) and the Symbols list); the p283 prose types $\bar{Y}_t$ while (90), (115) and the Symbols list have $\bar{Y}_T$ (both kept as printed). Items 7 and 9 replace these equations | superseded by items 7 and 9; no note |
| D15 | ch2-sec4 | 221, 223 | (82) and (84) take the C.P. as volume over base area, which drops the $A(0)$ term of Barrowman's frustum formula: right only for a pointed cone (item 4 replaces this text) | applied: \ednote on "valid only for the conical configuration:" (confirmed: Barrowman's frustum formula differs except for a pointed cone) |
| D16 | ch2-sec4 | 225 | the single-fin (85) has $(c_r + c_t)/r_r$ but (86) has $N(c_r + c_t)/(2r_r)$, so (86) with $N = 1$ is half of (85) (item 5 replaces these equations) | covered by the item-5 note |
| D17 | ch2-sec4 | 237, 241 | the prose types the inner radius $R_1$ (as the Symbols list does) while (103b) and (105b) letter $R_i$; both kept as printed | no note (Decisions: notation only) |
| D18 | ch2-sec4 | 242 | the second term of (108a) is the exact integral over the trapezoidal fin only when $r_t = 0$ (the text calls the result a good approximation) | no note (Decisions: the book calls it an approximation) |
| D19 | ch2-sec4 | 245 | "The coupled and decoupled damping ratios, $\zeta$ and $\zeta_c$" lists the symbols in the reverse order | applied: \ednote in Section 4.7 |
| D20 | ch2-sec4 | 229 | a 3 by 36 inch balsa sheet is 696.8 square centimeters; the book says 698 | no note (Decisions: 0.2% arithmetic difference) |

Fixed silently in the faithful pass as typographical slips (STYLE.md section 3), recorded here because they touch displays or sentence ends:
PDF 183 (ch2-sec3c), the second row of the right-hand bracket lacks the closing parenthesis of $(D_2^2 + \omega_2^2 - D_1D_2 - \omega_1\omega_2)$; PDF 200 (ch2-sec3d), the last sentence of 3.2.3 lacks its full stop.
Editorial notes are identified above by their opening words, not by number: the E-numbers shift whenever a note is added.

Decisions for the corrections step (2026-09-24)
- Equation numbers in the 1994 fin correction (item 5). Mandell numbers the eight replacement equations (85)-(92), but the 1973 text that follows keeps its own (89)-(92) ($\bar{Z}_T$, $\bar{Y}_T$, the total $\CNa$, the total $\bar{Z}$), and his 2022 correction still cites "equation (90)" for $\bar{Y}_T$ and keeps (115)-(117). This edition keeps every 1973 number from (89) on. The first four 1994 equations take (85)-(88), labels ch2:eq:85-88. The other four display as (89')-(92'), with labels ch2:eq:n89-n92 and \tag{89$'$} and so on. The \ednote on the block says so. So no renumber map is needed.
- Item 1 is a typographical omission: apply it silently (drop the \edcap that explains the missing alpha). Items 2 and 3 change equations: each gets an \ednote. For item 2, merge it with the existing D6 note.
- D11: in (113), set t_{\max} like the prose, silently (the same quantity; only the lettering's case differs). D16 is covered by item 5's note. D14 is superseded by items 7 and 9. D17, D18 and D20 get no note: D17 is notation only, D18 is a result the book calls an approximation, and D20 is a 0.2% arithmetic difference. D15 gets an \ednote only if a derivation confirms it.
- Replacement passages: the \ednote quotes every replaced 1973 equation in full. It quotes replaced 1973 prose in full when that prose is one paragraph or less. For longer passages it quotes the sentences whose content changes and says which passages are only reworded. The 1973 text is in git (the commit "ch2: faithful transcription").
