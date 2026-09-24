# Audit: corrections applied to chapters/ch2-sec3a.tex (round 1)

Unit: `chapters/ch2-sec3a.tex` (3.-3.1.2, PDF 122-149). Diff audited: `git diff HEAD -- chapters/ch2-sec3a.tex`
(7 hunks). Build audited: `build/unit/ch2-sec3a-{01..16}.png`, `.log` and `.aux`. The build ran at 05:27:15, after the
.tex was saved at 05:27:13, so the build is current. Sources consulted: the errata sheet PDF 664 (the one named in the task), the
second errata sheet PDF 665 (the same entries), and the 1973 pages PDF 125 (D3 and the clipped edge), PDF 133 (D4), PDF 136
(D5; zoomed crop `build/zoom/audit_ch2-sec3a_r1-p136-136.png`), PDF 137 (D7), PDF 138 (Figure 13 caption) and PDF 143
(equation (30)). Also consulted: corrections/ch2.md, STYLE.md sections 4, 7, 9, 10, 11 and 13, and git HEAD.

Items: **1** (Figure 13 caption, applied silently), **2** (equation (30), with D6 merged into its note), and the rewording of
the doubt notes **D3, D4, D5, D7**. The clipped-edge note on PDF 125 was to be kept.

## What was checked

1. **Item 1: extent and content.** The errata entry on PDF 664 is "Page 108, last line of figure caption, should read
   α_xo as if encased in very thick glue or tar". PDF 665 gives the same text for "line 7". PDF 138 prints only a blank
   space and the typed subscript "xo". The caption's last line now reads "angle $\alpha_{X0}$ as if encased in very thick
   glue or tar.", with $\alpha_{X0}$ in the STYLE.md section 13 form. The `\edcap` about the missing alpha is removed, and
   no note replaces it, as the decision in corrections/ch2.md requires. The rest of the caption matches HEAD word for word.
2. **Item 2: equation, symbol by symbol.** The errata on PDF 664 hand-letters (30) as α_x = Ae^{-Dt} sin(ωt+φ) + M_s/C_1,
   with M_s over C_1 as a built-up fraction. PDF 665 gives the same. The unit has
   `\alpha_X = A e^{-Dt}\sin(\omega t + \varphi) + \frac{M_s}{C_1}`: the same terms, the same signs and the same fraction,
   and the notation follows section 13 ($\alpha_X$, $\varphi$). Only the equation body changed. The label `ch2:eq:30`
   is kept, with no tag and no new label. A sympy check with $D$ and $\omega$ from (16) and (17) confirms that the corrected
   (30) satisfies $I_L\ddot\alpha_X + C_2\dot\alpha_X + C_1\alpha_X = M_s$ (residual 0). The 1973 form leaves a residual of $-M_s$.
3. **Item 2: note.** The note quotes the 1973 equation as $\alpha_X = A e^{-Dt}\sin(\omega t + \varphi)$, which matches
   PDF 143 and git HEAD. The note's other claims hold in the unit: $M_s/C_1$ is the particular response (29); the
   initial-condition expression $\alpha_{X0} = A\sin\varphi + M_s/C_1$ contains the term; and (33) and (35) contain it.
   The old D6 note is fully replaced, so only one note sits on (30). The note sits in the sentence that introduces the display
   ("is therefore\ednote{...}"), outside the `equation`, as section 9 requires. Its wording ("Equation~\eqref{...} corrected
   per ...; the 1973 equation read ...") follows the ch1 precedent (ch1-sec2a, equation (2)).
4. **D3 (PDF 125).** The scan prints "+ AωD e^{-Dt} cos(ωt+φ)" in the first derivative, so the note's statement of what
   is printed is accurate. Sympy confirms that differentiating (15) gives $A\omega$, and that the printed second-derivative
   formula $A(D^2-\omega^2)e^{-Dt}\sin - 2A\omega D e^{-Dt}\cos$ is exactly the derivative computed with $A\omega$. The
   substituted expression has $C_2 A\omega e^{-Dt}\cos$. The note's claim that both are computed with $A\omega$ is
   therefore correct. The display is unchanged from HEAD.
5. **Clipped-edge note (PDF 125).** The scan shows ":L" (a fragment of the I and the subscript L) and a sliver before
   "C2 ω cos". The note is accurate and unchanged.
6. **D4 (PDF 133).** The scan reads "If you substitute C2/IL for D in the first equation". The quotation is accurate. In the
   first equation, the $A_2$ coefficient is $C_2 - 2I_L D$, which is 0 for $D = C_2/2I_L$ and $-C_2$ for $D = C_2/I_L$. The $A_1$
   coefficient with $C_2/2I_L$ is $C_1 - C_2^2/4I_L$, which is the next display. With $C_2/I_L$ it is $C_1$. The note's claim
   "only with it do the terms involving $A_2$ sum to zero and the next display follow" is therefore correct.
7. **D5 (PDF 136, zoomed).** The first term is $I_L \frac{A}{\tau_1^2}e^{-t/\tau_1}$ with a bare A and no subscript.
   The second-derivative formula has $A_1/\tau_1^2$, and the other $e^{-t/\tau_1}$ terms have $A_1$. The note is accurate.
8. **D7 (PDF 137).** The scan reads "The constants A1 and A2 in equation (25)". Equation (24) contains $A_1$ and $A_2$, and
   (25) gives $\tau_1$ and $\tau_2$. The note is accurate. The literal "(25)" inside the quotation of the 1973 text follows
   the ch1 precedent (ch1-sec2b: "The 1973 text cited ``equations (19), (20), and (21)''").
9. **"Neither the errata nor the supplements correct this."** The only Chapter 2 entries on the errata sheets
   (PDF 664, 665) are pp. 108, 113 and 144-145. The supplements (PDF 676-687) cover pp. 186-196, 251-254 and 259. D3, D4, D5
   and D7 fall on pp. 95, 103, 106 and 107, so the claim is correct for all four. All four notes follow the chapter's pattern
   for doubt notes (ch2-sec2, ch2-sec3b, ch2-sec3d): what is printed, what is evidently meant and why, then "Neither the
   errata nor the supplements correct this; the ... is kept as printed". The printed text or display is unchanged in each case.
10. **Scope (whole diff).** The diff changes only: two LaTeX comment lines in the header recording the corrections (ch1-sec2a
    has the same kind of comment), the D3, D4, D5 and D7 note texts, the Figure 13 caption, and the (30) note and body. No
    other text, display or label changed.
11. **Labels.** No labels were added, removed or retagged. In the `.aux`, (15)-(36), Figures 10-19 and (30) on page 12
    are all in sequence. The log's only undefined references are `ch2:eq:11` and `ch2:sec:2.4`, both labels in ch2-sec2,
    which is expected.
12. **Rendering.** On page 2, E1 (D3) and E2 (the clipped edge) render in full. On page 6, E3 (D4) renders in full. On
    page 8, E4 (D5) and E5 (D7) render in full. On page 9, the Figure 13 caption ends "the initial yaw angle α_X0 as if
    encased in very thick glue or tar." On page 12, (30) shows the $+M_s/C_1$ fraction, E6 renders in full, and (31a) and
    (31b) follow. The E-numbers run E1-E6 in order. The log reports no overfull boxes, and no layout is broken.

Side observation, not a discrepancy in the unit: rows 1, 2 and D3-D7 in corrections/ch2.md still show their pre-correction
status ("todo" or "\ednote added in the faithful pass"). They need updating when the checklist is closed.

## Discrepancies

none
