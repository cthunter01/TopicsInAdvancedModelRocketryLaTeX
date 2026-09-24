# Chapter 4 — corrections checklist

Sources: the 1973 errata sheet (PDF 664; PDF 665 is a second typing of the same list); Mandell's "Changes to text
of Chapter 4" (PDF 699-702, cover note signed "Gordon Mandell, June 1994") and his note "Vector notation for pressure
term of rocket thrust" (PDF 666, 1 June 1994: in Chapters 1 and 4 the pressure term is $(P_e - P_a)\vec{A}_e$, arrow
over $A_e$ only); "Summary: Corrections and additions to altitude equations for 2-stage and multistage rockets"
(PDF 703-710, no author or date shown); the replacement Figure 4 (PDF 711); "Corrections to rocket characteristics in
Table I of Chapter 4, on page 595 of original book" (PDF 712). Printed page = PDF page - 32 throughout Chapter 4.

Status: todo / applied (with \ednote location) / deferred (reason)

| # | Source (PDF) | Original location | Change | Unit | Status |
|---|---|---|---|---|---|
| 1 | 664 | p.534 (PDF 566), equation (51) | the last term under the radical needs a right-hand brace after the bracket that follows $v_{n-1}$ (typographical); item 7 also rewrites (51): apply both consistently | ch4-sec2a | todo |
| 2 | 664 | p.583 (PDF 615), line 4 from the bottom | should read "Again, as in Section 2.4, expressions such as (139) are not equations" | ch4-sec4 | todo |
| 3 | 664 | p.590 (PDF 622), line 3 of Section 4.3.3 | should read "quiescent prior rotational state specified by equations (154)." | ch4-sec4 | todo |
| 4 | 664 | p.591 (PDF 623), line 6 | should read "account in equations (160)." | ch4-sec4 | todo |
| 5 | 699-702, 666 | p.513 after equation (7) and the top of p.514 (PDF 545-546) | replace the text after (7) with the 1994 text: (7a)-(7d), the over/under-expansion paragraph, the pressure component of thrust, $\vec{c}_{\mathrm{eff}}$, and (8) with its "Where" list; replace the top of p.514 ("in the following discussion ... weight and aerodynamic resistance, or drag."); the rest of p.514 is unchanged. The pressure term is $(P_e - P_a)\vec{A}_e$ (PDF 666) | ch4-intro-sec1 | todo |
| 6 | 702 | Symbols list | add $\vec{A}_e$, $\vec{E}_o$, $\vec{F}(t)$, $P_a$, $P_e$, $\vec{c}_{\mathrm{eff}}$ with the meanings given, in the list's order; change the meaning of $F(t)$ to "magnitude of thrust as a function of time" | ch4-symbols | todo |
| 7 | 703-710 | Section 2.2 (PDF 560-570): equations (40), (44)-(53) | the concrete corrections only (interview decision): the rewritten (40), (44) (the truncated drag integral with 0 in place of $y_1$), the corrected (45), (46), (47), the sign-corrected (48) ($+m_2v_1$ under the radical), (49), (50), (51), and the rewritten (52), (53) with the new variables $\hat{t}$, $\hat{y}$ and the limits $v_1$ to $v_2$, $0$ to $t_2$, together with the "upper limit $\hat{t}$" wording the Summary asks for. (58) is confirmed unchanged. The Summary's plans (moving notation and discussion to Section 2.2, the new Sections 2.2.3 and 2.2.4, terminal velocity, the thrust = weight and thrust < weight cases, the coasting-phase treatment) are not applied: one \ednote in Section 2.2 says so and points to the supplement Part, which reproduces the Summary in full | ch4-sec2a | todo |
| 8 | 711 | p.548 (PDF 580), Figure 4 | replacement figure and caption (the caption relates $t_1$, $t_2$ of the figure to $t_m$, $t_s$ of equations (73)-(75)); keep the 1973 figure for the supplement Part | ch4-sec2b | todo |
| 9 | 712 | p.595 (PDF 627), Table 1 | replace the fin cant angles for $\omega_c = \omega_{\mathrm{cres}}$ (0.00993 radian = 0.569 degree) and $\omega_c = 10\omega_{\mathrm{cres}}$ (0.0993 radian = 5.69 degrees) and the $k$ values (0.92, 0.921 and $1.016 \times 10^{-4}$ kg/m); an \edcap or \ednote gives the 1973 values and the source's note that the altitudes of rockets with canted fins change accordingly | ch4-sec4 | todo |

Notes
- Equations that exist only in the corrected text ((7a)-(7d)) take `\begin{equation*}\tag{7a}\label{ch4:eq:n7a}`
  (STYLE.md section 4). Where the corrected text gives a 1973 number to a different equation, follow the Chapter 2
  and 3 practice (keep the 1973 labels; mark a colliding new number with a prime and say so in the note).
- Minor arithmetic slips get no notes (user decision, 2026-09-24): record them below as "minor, no note".
- Doubts noted during the faithful transcription are added below as D-items when the transcription is done.

Doubts (from the prep survey; the faithful pass keeps each as printed)

| # | Unit | PDF | Doubt | Status |
|---|---|---|---|---|
| D1 | ch4-sec4 | 618 | the third member of the (154) brace group is printed "(156c)"; it is evidently (154c) (the text cites "equations (154)" and a separate (156) follows on PDF 619) | todo (note) |
| D2 | ch4-sec4 | 625 | "Equation (200a)" cites a number 35 higher than the equation meant, (165a), as do the three citations errata items 2-4 correct | \ednote in the faithful pass (stale reference) |
| D3 | ch4-sec5 | 635 | "the sample plot presented in Figure 19": Chapter 4 has no Figure 19; Figure 16 is meant | \ednote in the faithful pass (stale reference) |
| D4 | ch4-sec2b | 587 | the legend line "Figures 5.5 - 5.9:" uses a numbering the chapter has nowhere else (the text and captions say Figures 5 through 9) | todo |
| D5 | ch4-sec4 | 613 | (134) prints the series of cos(alpha) with alpha^4/4 where alpha^4/24 is meant (harmless after the truncation to (135)) | todo |
| D6 | ch4-sec2a | 556 | (25): the inner and outer upper limits are both printed t_b, despite the prose about dummy variables | todo (check) |
