# Audit: corrections applied to chapters/ch3-sec5b.tex (round 1)

Scope: `git diff HEAD -- chapters/ch3-sec5b.tex` (HEAD = 7e2087d, the faithful 1973 transcription). Checked against
the errata sheet (PDF 664), the supplement "Corrections to drag due to fin cant in Chapter 3, Section 5.3"
(PDF 691-693), the 1973 pages PDF 449, 450 (Table 4), 454, 455 and 456, and the Chapter 2 pages PDF 281 and 283
(the 1973 (115)-(117)) for D25. Also checked against STYLE.md sections 4, 8, 9, 10, 11 and 14, the Decisions in
corrections/ch3.md, and the rendered pages build/unit/ch3-sec5b-1.png to -7.png. Those pages were built at
09:39:28, after the last edit to the .tex at 09:39:26. I did not rebuild.

## Authors and dates shown by the sources

- Errata sheet (PDF 664): headed "ERRATA / TOPICS IN ADVANCED MODEL ROCKETRY by Gordon K. Mandell, George J.
  Caporaso, and William P. Bengen (Cambridge, Massachusetts: The MIT Press, 1973)". It names the book's authors
  but gives no author for the sheet and no date. None of its Chapter 3 entries (pp. 268, 270, 342, 364, 382, 401,
  480) falls in this unit (printed pp. 414-429).
- Supplement PDF 691-693: the title is in capitals. It opens with "[Replace text starting with equation (152) on page
  422 of the original book, with the following:]" and closes with "[Continue with the sentence beginning with
  "Furthermore...." on page 424 of the original book.]". Pages 2 and 3 carry page numbers only. No page has an
  author, signature or date. The note names the document by its title only, which is correct.

## What was checked

1. **Item 10, extent.** The 1973 text replaced runs from (152) on PDF 454 through "...by which rotation is induced
   are considerable." on PDF 456. That covers (152), the 0.1-radian sentence, (153), the root/tip sentence, the
   alpha-bar display, the "6.24 alpha^2" sentence, (154) and the closing paragraph. All of it is gone. The
   sentence before (152), "canting the fins ... determined by", is unchanged. So is "Furthermore, ..." and
   everything after it, including 5.4 with the 1973 (155) and (156). No 1973 text is left behind and none that the
   supplement keeps was removed.
2. **Item 10, prose, sentence by sentence against PDF 691-693.** All match the supplement:
   - the 0.05093 radian (2.918 deg) sentence;
   - "fins affixed to the rotating rocket", with *less* emphasized;
   - "varies with the radius";
   - the arctan sentence, with 15 deg (= 0.262 radian) and 0.268;
   - "small angle approximation";
   - "without significant loss of accuracy";
   - the new paragraph "For the simple, rectangular fins ... largest component of the induced drag, and to
     determine the fin-body interference drag, due to fin cant", with *average* emphasized;
   - "Remembering that the fins ... to the fin tip.";
   - the 0.05093 / -0.00857 sentence;
   - the roll damping sentence, which cites equation (115) of Chapter 2 and (152) above as linked refs;
   - "two diametrically opposed fins ... 6.51 alpha^2";
   - the twist paragraph, with *aerodynamic twist* emphasized and "Hoerner~(\ref{ch3:ref:9})", the unit's own form
     (line 12);
   - "For Delta alpha given in radians";
   - "This coefficient is based on the fin area ... all four canted fins:";
   - "From equation (147), ... 4 canted fins as";
   - "The total drag increase ... is then";
   - "which, for our trial rocket, becomes";
   - "The average effective angle ... at the fin tip:";
   - "Then";
   - the closing paragraph with 0.75, 2.46%, 9.84%, the triple-spin sentence with 22.14%, and "may be
     considerable".

   Paragraph breaks follow the supplement's indents.
3. **Item 10, equations symbol by symbol.** All match:
   - (152) omega_Z = 0.327259 U theta;
   - the unnumbered alpha(r) = theta - arctan(omega_Z r/U);
   - the approximation arctan(omega_Z r/U) ≅ omega_Z r/U (`\cong`);
   - (153) alpha(r) = theta - omega_Z r/U, with "radian" after `\qquad`;
   - alpha-bar = (0.05093 - 0.00857)/2 = 0.02118 radian;
   - (154) (C_Di')_cant = 13.02 alpha-bar^2;
   - (C_Di)_twist = (4 x 10^-5)(Delta alpha)^2, "for Delta alpha given in degrees";
   - (C_Di)_twist = 0.1313 (Delta alpha)^2;
   - the three-line align with the factor 4(3.57 x 2.54)/(pi(1.03)^2), then 10.8828 (C_Di)_twist, then (155)
     1.43 (Delta alpha)^2;
   - (Delta C_Di)_cant = 2(8.38 alpha-bar^2) = 16.76 alpha-bar^2;
   - (156) (Delta C_D)_cant = (C_Di')_cant + (C_Di')_twist + (Delta C_Di)_cant;
   - the trial-rocket form (13.02 + 16.76) alpha-bar^2 + 1.43 (Delta alpha)^2;
   - Delta alpha = 0.05093 - (-0.00857) = 0.0595 radian;
   - the final evaluation = 0.018433.

   Intermediate displays are unnumbered, as the task asks.
4. **The supplement's arithmetic, redone.**
   - 100/(0.327259 x 6000) = 0.050928, which is 2.918 deg.
   - The tip is at r = 3.57 cm, so 0.05093 - 0.0595 = -0.00857.
   - The average is 0.02118.
   - tan 15 deg = 0.268 and 15 deg = 0.2618 rad.
   - 2 x 6.51 = 13.02.
   - 4e-5 x (180/pi)^2 = 0.13131.
   - 4 x 3.57 x 2.54 / (pi x 1.0609) = 10.8827, and 0.1313 x 10.8828 = 1.429.
   - 2 x 8.38 = 16.76.
   - The final value recomputes to 0.018422 against the printed 0.018433. The percentages recompute to 2.456%,
     9.82-9.83% and 22.11-22.12%, against 2.46, 9.84 and 22.14 (the supplement multiplies the rounded 2.46 by 4
     and by 9). These are last-digit differences that change no conclusion. Under the D35 policy they need no
     note, and none was added.
5. **Item 10 note (E3).**
   - Placement: after "determined by", in the sentence that introduces (152), outside any display (section 9).
   - Equations quoted: the 1973 (152) .1672 U theta, (153), the alpha-bar display (.0828 + .0405)/2 = .0617, and
     (154) with ≅ 12.5. All match PDF 454-455 and HEAD.
   - Sentences quoted: the 0.1-radian sentence, the root/tip sentence (with *average*), the "6.24 alpha^2"
     sentence, and the whole closing paragraph through "are considerable". All match PDF 454-456 verbatim.
   - The note also says that (145) gives 6.51 alpha^2, which ch3-sec5a.tex line 335 confirms (D32).
   - It names the supplement by title.
   - Its list of what is new and what is only reworded is accurate. The remaining changes ("with the radius",
     "radian" in (153)) are trivial.
6. **Numbering of the supplement's (155) and (156).** The 1973 (155) k_adm and (156) 7nu/(U sqrt C_fx) of 5.4 are
   unchanged and keep ch3:eq:155 and ch3:eq:156 (inventory/ch3.csv rows 160-161, PDF 457). The supplement's
   (155) and (156) are therefore shown as (155′) and (156′). They are labelled ch3:eq:n155 (`\tag` inside
   `align*`) and ch3:eq:n156 (`equation*` + `\tag`). This follows Chapter 2's (89′)-(92′) precedent and
   STYLE.md section 4, and the note explains it. The 1973 labels ch3:eq:152-154 are kept on numbered equations.
   The task's wording "keep the labels ch3:eq:152 to ch3:eq:156" cannot hold for 155-156 without taking the
   5.4 labels. The choice made is sound.
   - Remark: when the checklist is updated, the Decisions line in corrections/ch3.md ("Item 10 keeps the labels
     ch3:eq:152 to ch3:eq:156") should record the (155′)/(156′) decision.
7. **D25 note (E2).**
   - Placement: after "of Chapter~\ref{ch2}," in the unchanged sentence. The sentence text is unchanged.
   - Scan check: PDF 281 confirms that the 1973 (115) is 12 theta V A_r Ybar_T k_r / {s c_r k_d [...]}. PDF 283
     confirms that the 1973 (116) has ((tau+1)/(tau-1))^2 in its second term, and that (117) matches the
     corrected one. Equation (90) is the 1973 equation, unchanged in ch2-sec4.tex.
   - Recomputation for the trial rocket (s = c_r = c_t = 2.54, r_t = 1.03, lambda = 1, tau = 3.466,
     Ybar_T = 2.30, k_d = 1.1292):
     - corrected k_r = 0.93633; k_r with the 1973 (tau+1) = 0.27951;
     - corrected (115) with corrected k_r: 0.327260 U theta, which is the supplement's (152);
     - 1973 (115) with corrected k_r: 0.1691 (A_r = pi r_t^2) or 0.1689 (A_r = 3.33);
     - 1973 (115) with the 1973 k_r: 0.0505.
   - Every number in the note is correct, and so is "12A_r/(s c_r) where the corrected one has 6(1 + lambda)".
     Its opening sentence overstates, however (see the table).
8. **D17 note (E1).**
   - Placement: at the end of the sentence on PDF 449, in prose.
   - (144) + (145) = 1.94 + 6.51 = 8.45 alpha^2 + 8.86 alpha^3, which exceeds 8.38 alpha^2 for every alpha > 0.
   - 8.38 alpha^2 exceeds 1.94 alpha^2 + 8.86 alpha^3 for alpha < 0.727 rad (41.6 deg), so it is larger than each
     term over Table 4's range of 0.5-10 deg.
   - Table 4 at 10 deg (PDF 450) gives .106 and .198 (sum .304) against .255. This matches the scan and my
     recomputation (0.1062, 0.1983, 0.2553).
   - The closing formula follows the Chapter 2 style.
9. **Nothing outside the items changed.** The diff has exactly three hunks: E1, E2 and the item 10 block. The
   "Furthermore" sentence is only re-wrapped.
10. **Section 14 notation.** It is used throughout the corrected passage:
    - `\omega_Z`, `\theta`, `\arctan`, `\cong`, `\bar{\alpha}`, `\Delta\alpha`;
    - `(C_{Di}')_{\mathrm{cant}}`, `(C_{Di})_{\mathrm{twist}}`, `(C_{Di}')_{\mathrm{twist}}`,
      `(\Delta C_{Di})_{\mathrm{cant}}`, `(\Delta\CD)_{\mathrm{cant}}` (the same output as the Symbols list's
      `(\Delta C_D)_{\mathrm{cant}}`), `S_F/S_m`, `\CDo`;
    - `\dg`, `\times`, `\un{radian}` on numbers, and `\qquad\text{...}` for "radian" and "for ... in degrees".
11. **Rendered pages.** Page 2 shows E1. Pages 4-7 show E2, E3, (152)-(154), (155′) and (156′), and the closing
    paragraph, all correctly. The 48 undefined references are all cross-unit or cross-chapter (ch2:eq:90 and
    115-117, ch2:sec:6.3, ch3:ref:9, ch3:eq:144 and 145, and others), as expected in a standalone unit build.
    The log has no overfull boxes. Figure 42 floats to the top of page 5, between the E2 sentence and "canting
    the fins"; this is ordinary float placement.

## Discrepancies

| where | expected (source/1973) | found | severity |
|---|---|---|---|
| ch3-sec5b.tex l.233, E2 (D25 note), first sentence | a claim the arithmetic supports: Bengen's .1672 agrees with the 1973 equation (115) (0.169 U theta), but only with k_r from the (tau^2 + 1) form; the 1973 (116) as printed, with (tau + 1), gives 0.0505 U theta. So he did not use (116) in its printed 1973 form (e.g. "Bengen's .1672 follows from the 1973 form of equation (115), with k_r computed as in the corrected equation (116)") | "Bengen evaluated these equations in their 1973 form." The note's own last clause shows this is not true of (116) as printed. The numbers that follow are all correct | note |
| ch3-sec5b.tex l.279-283 (small-angle approximation) | PDF 691: "…≤ about 0.268, arctan(ω_Z r/U) ≅ ω_Z r/U" runs on in the text line (the line starts at the text margin, not indented like the α(r) display above it); "That is, …" follows | set as a separate `equation*` display after "about 0.268,". The two other stacked-fraction expressions of the same sentence stay inline. This is a minor judgement call: a display is defensible for readability, but it is not the supplement's layout | layout |
