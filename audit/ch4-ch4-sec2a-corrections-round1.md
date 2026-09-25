# Audit: ch4-sec2a corrections, round 1

Unit: chapters/ch4-sec2a.tex (Sections 2.1-2.2, PDF 552-570, printed pp. 520-538).
Items for this unit: item 7 (the multistage Summary, PDF 703-710, concrete fixes only; subsumes errata item 1, PDF 664),
D6 (PDF 556, check), D13 (PDF 568-569, silent).
Read: STYLE.md sections 4, 7-11 and 15; corrections/ch4.md; `git diff HEAD -- chapters/ch4-sec2a.tex`.
Source pages read: p664 (errata), p699, p702, p703-p710 (Summary), and the 1973 pages p556, p562-p569.
Zoomed renders: build/zoom/audit_ch4-sec2a_r1-p704a, -p704b, -p705a to -p705e, -p556, -p568, -p569.

## What was checked

1. **Equations against the Summary, symbol by symbol** (PDF 703-705, 300 dpi crops):
   - (40): all four integrals run from 0 to t_2 in d\hat{t}. The terms are m_2 dv/d\hat{t}, F_2(\hat{t}), m_2g and
     k_2v^2. Matches.
   - (44): `\int_0^{t_2} k_2v (d\hat{y}/d\hat{t}) d\hat{t} = k_2\hat{y}v]_{0,v_1}^{y_2,v_2} - k_2\int_0^{t_2}\hat{y}
     (dv/d\hat{t}) d\hat{t} \cong k_2y_2v_2`. The evaluation bar and its limits are as printed, in the (23) style, and
     "≅" is `\cong`. Matches.
   - (45): `m_2v_2 - m_2v_1 = I_{t2} - m_2gt_2 - k_2y_2v_2`. Matches.
   - (46): `(I_{t2} - m_2gt_2 + m_2v_1)/(m_2 + k_2y_2)`. Matches.
   - (47): `\frac{t_2^2}{2}(F_2 - m_2g) - k_2\frac{y_2^2}{2}`. Matches.
   - (48) and (49): the radicand is `m_2^2 + 2k_2t_2[\tfrac{t_2}{2}(F_2 - m_2g) + m_2v_1]`. The numerator of (48) is -m_2
     and that of (49) is `I_{t2} - m_2gt_2 + m_2v_1`. Matches.
   - (50) and (51): the same in n. The Summary letters v_{(n-1)}; it is set as `v_{n-1}`, the section 15 stage-index form
     and the 1973 form. That is typographic, not a discrepancy.
   - (52): the right side is `\int_0^{t_2} d\hat{t}`. Matches.
   - (53): the 1973 bracket form is kept, followed by `= t_2`. Matches.
   - Extent: every rewritten equation replaces its 1973 form in place. (41)-(43) and (54)-(60) are unchanged, as they
     should be: the Summary gives no text for them, and on PDF 708 it confirms (58).
2. **Mathematics redone.**
   - Solving the corrected (47) as a quadratic in y_2 gives exactly the corrected (48), with +m_2v_1.
   - Solving the 1973 (47) gives +m_2v_1 as well. The 1973 minus sign is therefore an error, as the note says.
   - m_2 + k_2y_2 equals the radical, so (46) with (48) gives (49).
   - With v_1 = 0, (48) and (49) reduce to (27) and (28), which is what note E5's parenthesis claims.
   - Integrating the running form of (45) from 0 to t_2 gives (47) when the thrust is constant.
3. **Notation key** (PDF 562 and 703-704). The v, \hat{y} and \hat{t} entries are word for word from PDF 703, and I_{t2}
   is from PDF 704. They are appended after t_1, where the 1973 list ends.
4. **Upper-limit paragraph** (PDF 567 and 705). All three uses of t in the 1973 sentence become \hat{t}, and the range
   becomes "greater than or equal to 0 and less than or equal to t_2", as the Summary asks. The rest of the paragraph is
   unchanged. (56) and the sentence before (57), with "t = t_1 to t = t_1 + t_2", are kept, and note E7 says so.
5. **Notes: 1973 quotations against the scans and git HEAD.**
   - E3 quotes (40) (PDF 563) correctly.
   - E4 quotes (44)-(47) (PDF 564) correctly.
   - E5 quotes (48)-(51) (PDF 565-566) correctly: R_2 and R_n as printed, and the k_ny_{n-1}v_{n-1} numerator of (50).
     Its statement that (51) lacks the right-hand brace after the bracket that follows v_{n-1} matches both PDF 566 and
     the errata entry for p.534, so errata item 1 is mentioned in the (51) quotation.
   - E6 quotes (52)-(53) (PDF 567) correctly, and (53) is indeed printed without a right-hand side.
   - E7 quotes the 1973 upper-limit sentence verbatim.
6. **Notes: statements about the Summary**, checked against PDF 703-710:
   - E2 gives the zero-for-y_1 quotation, the physical-intuition argument, the Larry Curcio attribution ("marked xerox
     copy of page 533"), I_{t2} in place of F_2t_2, and "= t_2".
   - E2 lists the plans that are not carried out: moving the notation and the two-stage physics discussion to 2.2;
     revising the limiting-behavior discussion; moving the generalization; the new 2.2.3 with terminal velocity; the new
     2.2.4 with thrust equal to or less than weight; the coasting phase. It also says the discussion of (41)-(43) and of
     k_2 "made unnecessary" is kept (PDF 704, top). All accurate.
   - E4: "introduces the constant average thrust F_2 only at (47)" matches PDF 704.
   - E5: the Summary indeed does not define I_{tn}, and it gives no text for the limiting-behavior revision.
   - Placement follows section 9. Every note sits in the prose that introduces a display or list, or after a sentence;
     none is inside a display, caption or longtable.
7. **Prose kept where it contradicts** (as the item asks). Three passages are stated in the notes:
   - "constant average thrust" before (45) is in E4;
   - "y_1 ... treated as constants" before (48) and the "let y_1 and v_1 both be zero" check after (49) are in E5;
   - the 1973 (43) limits, which (44) no longer follows from, are in E3 and E4.
   No other 1973 prose in the unit names y_1 terms or F_2t_2. The later passages (the t_2^2 term dominating (48), the
   limit of (49) at long burn times, and the closing instructions) remain valid for the corrected equations.
8. **D6.** The 300 dpi crop of PDF 556 confirms both upper limits of (25) are t_b. The note's mathematics is right:
   - The inner t_b makes the first term I_tt_b, which does not depend on the thrust's form. The text says the burnout
     altitude does depend on it.
   - A constant F would give Ft_b^2, where (26) has Ft_b^2/2.
   - The running (dummy) time is meant, and integrating the running form of (24) confirms it.
   - No errata or supplement entry covers (25) (PDF 664, 699-712).
   The note is in the introducing sentence and follows the doubt-note style used in Chapters 2 and 3.
9. **D13.** `\Bigr)` now closes the first cosh of (58) and (60), silently, with no other change. The crops of PDF 568-569
   confirm the 1973 parenthesis is never closed.
10. **Scope.** The whole diff contains only the following, and nothing outside the items changed:
    - the header comment;
    - D6;
    - item 7: the notes E2-E7, the four list entries, (40), (44)-(53) and the upper-limit sentence;
    - D13.
    The `\begingroup\small` and `split` wrappers of the 1973 (50)-(51) were removed because the corrected one-line forms
    fit, as section 15 requires ("keep a one-line display on one line if it fits"). The Summary also prints (51) on one
    line.
11. **Labels.** ch4:eq:40 and ch4:eq:44 to ch4:eq:53 are kept on the corrected equations. No new equations, so no
    n-labels and no `\tag`.
12. **Section 15 notation.** The corrected passages use:
    - `\hat{t}`, `\hat{y}`, `d\hat{t}` and `F_2(\hat{t})`;
    - `I_{t2}` and `I_{tn}`, with a capital I and an italic t;
    - `\cong`, `\tfrac{t_2}{2}` and `\tfrac{t_n}{2}`;
    - side-set integral limits;
    - lowercase v and y, and `v_{n-1}`.
13. **Render.** build/unit/ch4-sec2a.pdf and its PNGs (18:35:21-18:35:35) are newer than the edit (18:35:15), and the
    log has no overfull boxes. The only undefined references are the cross-unit ch4:eq:16/17 and ch4:sec:2.5. Pages
    02, 05-09 were checked. (25) and E1 render correctly. The key and E2 are on p.5. (40), (44) and E3-E4 are on p.6.
    (45)-(49) and E5 are on p.7. (50)-(53) and E6 are on p.8. The upper-limit paragraph, E7 and the closed parentheses
    of (58) and (60) are on p.9. All render correctly.

Observation (not a discrepancy of this unit): corrections/ch4.md still shows item 1, item 7, D6 and D13 as "todo" or
"check". The status column is bookkeeping outside this unit's diff.

## Discrepancies

none

| where | expected (source/1973) | found | severity |
|---|---|---|---|
