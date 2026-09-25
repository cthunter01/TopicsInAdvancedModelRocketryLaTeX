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
| 1 | 664 | p.534 (PDF 566), equation (51) | the last term under the radical needs a right-hand brace after the bracket that follows $v_{n-1}$ (typographical); item 7 also rewrites (51): apply both consistently | ch4-sec2a | applied. Subsumed by the rewritten (51), and the (48)-(51) note (ch4-sec2a.tex:394) says the errata sheet adds the missing brace. |
| 2 | 664 | p.583 (PDF 615), line 4 from the bottom | should read "Again, as in Section 2.4, expressions such as (139) are not equations" | ch4-sec4 | applied silently at ch4-sec4.tex:157, 'expressions such as~\eqref{ch4:eq:139}'. |
| 3 | 664 | p.590 (PDF 622), line 3 of Section 4.3.3 | should read "quiescent prior rotational state specified by equations (154)." | ch4-sec4 | applied silently at ch4-sec4.tex:329, '\eqref{ch4:eq:154}'. |
| 4 | 664 | p.591 (PDF 623), line 6 | should read "account in equations (160)." | ch4-sec4 | applied silently at ch4-sec4.tex:350, '\eqref{ch4:eq:160}'. |
| 5 | 699-702, 666 | p.513 after equation (7) and the top of p.514 (PDF 545-546) | replace the text after (7) with the 1994 text: (7a)-(7d), the over/under-expansion paragraph, the pressure component of thrust, $\vec{c}_{\mathrm{eff}}$, and (8) with its "Where" list; replace the top of p.514 ("in the following discussion ... weight and aerodynamic resistance, or drag."); the rest of p.514 is unchanged. The pressure term is $(P_e - P_a)\vec{A}_e$ (PDF 666) | ch4-intro-sec1 | applied in ch4-intro-sec1.tex after (7), up to the paragraph before Section 1.1. (7a)-(7d) use equation* with \tag and the n7a-n7d labels; (8) keeps ch4:eq:8; the pressure term is (P_e - P_a)\vec{A}_e; the single \ednote is at l.187. Rendered on physical pp. 270-271 (printed 264-265) and matches the source symbol by symbol, emphasis included. |
| 6 | 702 | Symbols list | add $\vec{A}_e$, $\vec{E}_o$, $\vec{F}(t)$, $P_a$, $P_e$, $\vec{c}_{\mathrm{eff}}$ with the meanings given, in the list's order; change the meaning of $F(t)$ to "magnitude of thrust as a function of time" | ch4-symbols | applied in ch4-symbols.tex. Six rows are added, in the list's order; the \edcap is on the \vec{A}_e row (l.14). The F(t) meaning is changed, with an \ednote (E1) at l.27. Rendered on physical pp. 263-264 and correct. |
| 7 | 703-710 | Section 2.2 (PDF 560-570): equations (40), (44)-(53) | the concrete corrections only (interview decision): the rewritten (40), (44) (the truncated drag integral with 0 in place of $y_1$), the corrected (45), (46), (47), the sign-corrected (48) ($+m_2v_1$ under the radical), (49), (50), (51), and the rewritten (52), (53) with the new variables $\hat{t}$, $\hat{y}$ and the limits $v_1$ to $v_2$, $0$ to $t_2$, together with the "upper limit $\hat{t}$" wording the Summary asks for. (58) is confirmed unchanged. The Summary's plans (moving notation and discussion to Section 2.2, the new Sections 2.2.3 and 2.2.4, terminal velocity, the thrust = weight and thrust < weight cases, the coasting-phase treatment) are not applied: one \ednote in Section 2.2 says so and points to the supplement Part, which reproduces the Summary in full | ch4-sec2a | applied in ch4-sec2a.tex. Main note at l.260 on the notation key, plus four key entries. Notes quoting the 1973 forms are at (40) (l.318), (44)-(47) (l.348), (48)-(51) (l.394) and (52)-(53) (l.462). The upper-limit wording change has its note at l.490. The Summary's plans are not carried out, as the Decisions require. Rendered on physical pp. 279-283; (40) and (44)-(53) match the Summary exactly. |
| 8 | 711 | p.548 (PDF 580), Figure 4 | replacement figure and caption (the caption relates $t_1$, $t_2$ of the figure to $t_m$, $t_s$ of equations (73)-(75)); keep the 1973 figure for the supplement Part | ch4-sec2b | applied in ch4-sec2b.tex:212-223. Figure 4 now uses figures/supplement/ch4-fig04-1994.png with the 1994 caption in full, and the \edcap quotes the 1973 caption and states the artwork is unchanged. The 1973 image is owned by 'supplement' in the manifest. Rendered on physical p.289 and correct. |
| 9 | 712 | p.595 (PDF 627), Table 1 | replace the fin cant angles for $\omega_c = \omega_{\mathrm{cres}}$ (0.00993 radian = 0.569 degree) and $\omega_c = 10\omega_{\mathrm{cres}}$ (0.0993 radian = 5.69 degrees) and the $k$ values (0.92, 0.921 and $1.016 \times 10^{-4}$ kg/m); an \edcap or \ednote gives the 1973 values and the source's note that the altitudes of rockets with canted fins change accordingly | ch4-sec4 | applied in ch4-sec4.tex:494-499 (0.00993 radian = 0.569 deg; 0.0993 radian = 5.69 deg; k values 0.92 / 0.921 / 1.016 x 10^-4). The \edcap in the caption (l.461) gives the 1973 values and the source's NOTE. Rendered on physical p.315 and correct. |

Notes
- Equations that exist only in the corrected text ((7a)-(7d)) take `\begin{equation*}\tag{7a}\label{ch4:eq:n7a}`
  (STYLE.md section 4). Where the corrected text gives a 1973 number to a different equation, follow the Chapter 2
  and 3 practice (keep the 1973 labels; mark a colliding new number with a prime and say so in the note).
- Minor arithmetic slips get no notes (user decision, 2026-09-24): record them below as "minor, no note".
- Doubts noted during the faithful transcription are added below as D-items when the transcription is done.

Doubts (from the prep survey; the faithful pass keeps each as printed)

| # | Unit | PDF | Doubt | Status |
|---|---|---|---|---|
| D1 | ch4-sec4 | 618 | the third member of the (154) brace group is printed "(156c)"; it is evidently (154c) (the text cites "equations (154)" and a separate (156) follows on PDF 619) | note at ch4-sec4.tex:223. Checked on the scan. |
| D2 | ch4-sec4 | 625 | "Equation (200a)" cites a number 35 higher than the equation meant, (165a), as do the three citations errata items 2-4 correct | note restyled at ch4-sec4.tex:410. It is accurate: (189) and (195) are 35 higher than their targets. |
| D3 | ch4-sec5 | 635 | "the sample plot presented in Figure 19": Chapter 4 has no Figure 19; Figure 16 is meant | note restyled at ch4-sec5.tex:25. Figure 16 is the chapter's only plot of altitude against liftoff mass; Figures 5-9 plot errors. |
| D4 | ch4-sec2b | 587 | the legend line "Figures 5.5 - 5.9:" uses a numbering the chapter has nowhere else (the text and captions say Figures 5 through 9) | note at ch4-sec2b.tex:336. Checked on the scan. |
| D5 | ch4-sec4 | 613 | (134) prints the series of cos(alpha) with alpha^4/4 where alpha^4/24 is meant (harmless after the truncation to (135)) | note at ch4-sec4.tex:83. Checked on the scan; 1/4! = 1/24. |
| D6 | ch4-sec2a | 556 | (25): the inner and outer upper limits are both printed t_b, despite the prose about dummy variables | confirmed. Both upper limits are printed t_b. Note at ch4-sec2a.tex:103; its mathematics is correct (I_t t_b, and Ft_b^2 against the Ft_b^2/2 of (26)). |
| D7 | ch4-sec4 | 615 | (145) prints the gyroscopic term $+I_R\omega_y\omega_z$; the Euler equations of Chapter 2 ((14) and the equations of Section 1.4) give $I_R\omega_x\omega_z$ in the pitch equation ((144) agrees with Chapter 2) | note at ch4-sec4.tex:125. The scan shows +I_R omega_y omega_z. Chapter 2's (14) row 2 gives I_L d(omega_y)/dt = ... + I_R omega_z omega_x, so the sign is right and the subscript should be x; the note is accurate. |
| D8 | ch4-sec5 | 642 | "Section 5 of Chapter 2" is cited for working out $C_1$, $C_2$, $I_L$ and $I_R$ of a design on paper; that is Section 4 (Analytical Determination), Section 5 being the experimental one | note at ch4-sec5.tex:176, with the reference typed literally as 'Section~5'. Chapter 2 Section 4 is the Analytical Determination and Section 5 the Experimental one. |
| D9 | ch4-intro-sec1 | 552 | the text says (9), (10), (14) and (15) are substituted into (12)-(13), but $F_p$ of (10) appears in neither (12)-(13) nor (16)-(17): the thrust component normal to the axis is dropped without comment | note at ch4-intro-sec1.tex:380. F_p appears in neither (12)-(13) nor (16)-(17); verified. |
| D10 | ch4-sec4 | 625, 628-629 | Table 2 gives $t_o = 0.1$ s for the sinusoidal and coupled-sinusoidal rows (12, 13, 24-26), while PDF 625 says such perturbations arise immediately upon liftoff and (166) starts at $t = 0$ | confirmed. Table 2 rows 12, 13 and 24-26 have t_o = 0.1. Note at ch4-sec4.tex:423. |
| D11 | ch4-sec2a | 565-567 | the radicands of (48)-(51) print $-m_2v_1$ ($-m_nv_{n-1}$) where $+$ is correct; (50) prints $k_ny_{n-1}v_{n-1}$ where $k_n(y_1 + \ldots + y_{n-1})v_{n-1}$ generalizes (46); (53) is printed as an expression without "= $t_2$"; (44) keeps $y_1v_1$ at the lower limit | resolved by item 7. The corrected (44) and (48)-(53) remove every y_1 term, fix the sign, and give (53) its '= t_2'. |
| D12 | ch4-intro-sec1 | 546 | "whose vector sum is here represented by E" prints E without an arrow | resolved by item 5. The replaced top of p.514 prints E_o without an arrow, and the item-5 note records the 1973 plain E. |
| D13 | ch4-sec2a | 568-569 | the parenthesis opened after the first cosh of (58) and (60) is never closed | fixed silently. \Bigr) added in (58) (ch4-sec2a.tex:519) and (60) (l.536); both render closed. |
| D14 | several | 554, 558, 564, 601, 640, 646 | silent typographical fixes: "in equations (20)" at a sentence start (554), "methematics" (558), "mass. we obtain" (564), "use A Malewicki chart" (640), "Chicago.," in Reference 4 (646) in the faithful pass; "0.453 Kg" (601) to be set "kg" silently in the corrections step | fixed silently. '0.453 kg' at ch4-sec3.tex:153; the faithful-pass fixes (the capital 'In equations (20)', 'mathematics', 'use a Malewicki chart', 'Chicago,') are present. |
| D15 | several | various | minor, recorded without notes: $F_2(t)$ in (40) not in the Symbols list; $k_1$ undefined (564); the overlap of (158) and (159) at $t = t_1$ (620); Table 2 row 25 $\alpha_{\max} = 0.220$ above the 0.2 rad limit; last-digit rounding in Table 2's percent reductions and in the PDF 587 key table; "slightly more than doubled" (601); "identical specific impulse" (644); Reference 1's "Phoenix" | no notes, as decided; none were added. |

Decisions for the corrections step (2026-09-24)
- Errata items 2-4 replace stale equation numbers with the right ones. They are typographical: apply them silently,
  as \eqref's to (139), (154) and (160). Stale citations that no source corrects keep their faithful-pass notes
  ((200a), D2; "Figure 19", D3) or get one ("Section 5 of Chapter 2", D8).
- Item 5 (the June 1994 thrust text): (7a)-(7d) exist only in the corrected text and are `equation*` with \tag and the
  labels ch4:eq:n7a to ch4:eq:n7d. The rewritten (8) keeps ch4:eq:8. The pressure term is $(P_e - P_a)\vec{A}_e$ (PDF 666).
  One \ednote quotes the 1973 text from after (7) to the top of p.514, including the 1973 (8).
- Item 7 (the multistage Summary). Apply its equation rewrites: (40), (44)-(53). Keep the 1973 labels; the corrected
  (45)-(53) replace their 1973 forms in place. The rewritten equations use the Summary's new variables $\hat{t} = t - t_1$
  and $\hat{y} = y - y_1$ and the total impulse $I_{t2}$. Add their definitions, in the Summary's words, to the notation
  key of Section 2.2.1; the Summary would move the key to Section 2.2, a plan that is not carried out. Also apply the
  Summary's one concrete wording change: the upper limit $t$ becomes $\hat{t}$ in the discussion of (53)-(55).
  Instructions without supplied text ("revise the discussion of limiting behavior", "move the discussion ...", the new
  Sections 2.2.3-2.2.4, the terminal-velocity, thrust = weight and thrust < weight cases, the coasting-phase
  treatment) are not carried out. The 1973 discussion around (41)-(43), which the Summary calls unnecessary after the
  rewrite, is kept. One \ednote at the start of Section 2.2.1 says what the Summary corrects and why: the truncated drag
  integral should have 0 where it has $y_1$, and the sign of $m_2v_1$ in (48)-(51) is wrong. The note also says which
  Summary items are not applied and that the supplement Part reproduces the Summary in full. Each rewritten equation's
  1973 form is quoted, in the same note or in short notes at (44) and (48). Errata item 1 (the brace of (51)) is
  subsumed by the rewritten (51); mention it in the (51) note.
- Item 8: include figures/supplement/ch4-fig04-1994.png (manifest row sup-ch4-fig04-1994, already cropped). Transcribe
  the 1994 caption in full, with an \edcap that quotes the 1973 caption and says whether the artwork changed.
- Item 9: replace the three Table 1 values. An \edcap in the table caption gives the 1973 values and the source's note
  that the altitudes of rockets with canted fins change accordingly (the Table 2 figures are not recomputed).
- Doubts: notes for D1, D4, D5, D7, D8, D9; checks D6 and D10 (note only if confirmed); D13 and "0.453 Kg" fixed
  silently; D15 no notes. Restyle the faithful-pass notes for D2 and D3 to the doubt-note style.
