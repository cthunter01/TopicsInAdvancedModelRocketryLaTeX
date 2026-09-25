# M5 audit: supplement, "Summary: Corrections and Additions to Altitude Equations" (round 2, part 1)

Scan pages: PDF 703-706 (typescript pages 1-4), figures/pages/p703.png to p706.png.
Render: build/unit/s-ch4-summary-1.png to -4.png carry the content of p703-p706. I also read -5.png, the next page; its content belongs to the part-2 auditor.
Zoomed crops:
- build/zoom/audit_supp-ch4-summary_r2_p1-render1-deflist-1.png (compiled page 1 at 200 dpi, the definition list).
- build/zoom/audit_supp-ch4-summary_r2_p1-p706-tanh-706.png, -p706-arrows-706.png and -p706-lasty2-706.png (the scan's p706 v2/y2 tanh-cosh-sinh displays, the two arrow displays and the last y2 display, at 300 dpi).

## Round 1 item re-verified

- **p703, list of added variables (render p1): FIXED.** The v, y-hat and t-hat definitions now form a hanging-indent list with the "=" signs aligned. The continuation line "point)" starts under "altitude", the text after "=". This matches the typescript, where the continuation lines start under the text after "=".

## Items re-checked on p703-p706

- **Headings (5).**
  - The chapter title, as specified.
  - Second-Stage Burning-Phase Solutions.
  - Extended Caporaso-Bengen Solution.
  - Extended Fehskens-Malewicki Solution.
  - Qualitative Features and Limiting Behavior of Multistage Solutions. Considerations of Terminal Velocity.
- **Text, word by word.**
  - p703: "In hindsight ...", the two bullets, "This formulation ...", "I plan to move ...", the three definitions and "I also plan to move ...".
  - p704: "Rewrite equation (40) on page 531 ...", "This makes the discussion ...", "Rewrite equation (44) on page 532 ...", "This is a correction ... simplifies their algebra.", "Corrected equation (45) ...", "where I have substituted I_t2 ... Corrected equation (46) then becomes", "When F2(t-hat) ... corrected equation (47) becomes", "This equation was actually evaluated ... (t-t1).", and "Rewrite corrected equation (48) on page 533 ...".
  - p705: "This introduces another correction ... Larry Curcio ...", "Rewrite corrected equation (49) as", "Revise the discussion ... Rewrite corrected equation (50) as", "and rewrite corrected equation (51) as", "Rewrite equation (52) as", "and rewrite equation (53) as", "Change discussion of upper limit t ...", "Move the discussion ..." and "Add a Section 2.2.3 which ...".
  - p706: "of approach to terminal velocity ... State that attainment of terminal velocity", "requires the assumption ... (49) ...", "then when v1 = vterm ... in (48) and (49) simplifies them to", "and", "Note that ... [(dv/dt) = 0].", "Show that ... in terms of vterm as", "and", "As v1 approaches vterm ...", "so that", "and v2 approaches v1. Direct substitution ...", and "from which, using the exponential definitions of cosh and sinh, we obtain".
- **Displays (20), symbol by symbol.**
  - p703-p704: rewritten (40).
  - p704: (44), with the evaluation bracket ]^{y2,v2}_{0,v1} and the congruence sign, then (45), (46) and (47), including t2^2/2 and k2 y2^2/2.
  - p705: (48)-(51). The radicals extend over the whole bracket, and the brackets hold t2/2 and tn/2. The subscripts are v_(n-1), I_t2 and I_tn.
  - p705: (52), with limits v1, v2 and 0, t2; (53), with its tanh^-1 bracket evaluated between v1 and v2, = t2.
  - p706: v_term. The constant-thrust v2. y2 = v1 t2 and v2 = v1. The v2 (v_term) tanh[...] form. The y2 = m2/k2 ln[cosh(...) + v1/v_term sinh(...)] form. The two arrow displays. The y2 ln[cosh(k2t2/m2 v1) + sinh(k2t2/m2 v1)] display. All fences were confirmed in zoomed crops.
- **Inline math.**
  - t = t1, t-hat = (t - t1) and y-hat = (y - y1).
  - v1, v2, t2, y2, y1, k and k2.
  - I_t2, F2t2, the inline integral of F2(t-hat) dt-hat, F2(t-hat) and F2.
  - (t - t1), [(t1 + t2) - t1] = t2 and (t-t1).
  - -m2v1, +m2v1, k2v1^2, (F2 - m2g), vterm and [(dv/dt) = 0].
- **Cross-references.** I checked the unit log's undefined-reference sequence against the printed wording.
  - Edcap: sec:2.2, ch4 and sec:2.2.1.
  - "Section 2.2.1 to Section 2.2": sec:2.2.1, then sec:2.2.
  - "from 2.2.1 to 2.2": sec:2.2.1, then sec:2.2.
  - Equations, in order: eq:40, 44, 44, 44, 45, 46, 45, 47, 48, 49, 50, 51, 52, 53, 49, 48 and 49.
  - Every label exists in build/chapters/ch4.aux with the printed number.
  - "Section 2.2.3" is plain text, correctly so.
- **Editorial note.** I re-checked it against build/main.pdf, the compiled Section 2.2.1 (pdftotext).
  - Editor's note E5 says that (40) and (44)-(53) are corrected per the Summary and that the list's last four entries come from it (v, y-hat, t-hat, I_t2).
  - E5 also states that the Summary's plans are not carried out. Editor's note E10 applies the upper-limit change.
  - The edcap's statement is true.

## Discrepancies

none

Wording, paragraphing, bullets, the definition list (now with hanging indents), headings, every display and inline formula, and every reference target agree with the scan on p703-p706.
