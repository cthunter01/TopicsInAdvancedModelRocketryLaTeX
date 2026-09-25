# M5 audit: supplement, "Summary: Corrections and Additions to Altitude Equations" (round 1, part 1)

Scan pages: PDF 703-706 (typescript pages 1-4), figures/pages/p703.png to p706.png.
Render: build/unit/s-ch4-summary-1.png to -4.png (content of p703-p706), plus -5.png (next page; that content is the part-2 auditor's).
Zoomed crops: build/zoom/audit_supp-ch4-summary_r1_p1-*.png (display of (40); (44); "At t-hat = 0 v = v1 but y-hat = 0"; (49), (50), (51), (53); p706 "then when v1 = vterm ... and v2 = v1", the two v_term displays and the last y2 display).

## Items checked

- **Headings (5).** Chapter title (SUMMARY / CORRECTIONS AND ADDITIONS TO ALTITUDE EQUATIONS FOR 2-STAGE AND MULTISTAGE ROCKETS, as specified); Second-Stage Burning-Phase Solutions; Extended Caporaso-Bengen Solution; Extended Fehskens-Malewicki Solution; Qualitative Features and Limiting Behavior of Multistage Solutions. Considerations of Terminal Velocity.
- **Text (37 blocks), word by word.**
  - p703: the "In hindsight" paragraph, the two bullets, "This formulation ...", "I plan to move ...", the three variable definitions (v, y-hat, t-hat), "I also plan to move ...", "Rewrite equation (40) on page 531 ...".
  - p704: "This makes the discussion ...", "Rewrite equation (44) ...", "This is a correction ...", "Corrected equation (45) ...", "where I have substituted I_t2 ...", "When F2(t-hat) ...", "This equation was actually evaluated ...", "Rewrite corrected equation (48) on page 533 ...".
  - p705: "This introduces another correction ... Larry Curcio ...", "Rewrite corrected equation (49) as", "Revise the discussion ... Rewrite corrected equation (50) as", "and rewrite corrected equation (51) as", "Rewrite equation (52) as", "and rewrite equation (53) as", "Change discussion of upper limit ...", "Move the discussion ...", "Add a Section 2.2.3 ...".
  - p706: "requires the assumption ...", "then when v1 = vterm ... in (48) and (49) ...", "and", "Note that ... [(dv/dt) = 0].", "Show that ...", "and", "As v1 approaches vterm ...", "so that", "and v2 approaches v1 ...", "from which, using the exponential definitions ...".
- **Displays (20), symbol by symbol.**
  - p703: rewritten (40).
  - p704: (44) with its evaluation bracket ]^{y2,v2}_{0,v1} and the congruence sign; (45), (46) and (47).
  - p705: (48) to (53), including the radical extents, the t2/2 and tn/2 brackets, the v_{(n-1)} subscripts, I_tn, tanh^-1 and the limits v1 and v2.
  - p706: v_term; the constant-thrust v2; y2 = v1t2; v2 = v1; the v2 tanh form; the y2 ln[cosh + (v1/vterm) sinh] form; the arrow display; the v2 arrow display; the y2 ln[cosh(...v1) + sinh(...v1)] display.
  - Hats, subscripts, superscripts, signs and fences all agree with the scan.
- **Inline math.** t = t1, t-hat = (t - t1), y-hat = (y - y1), v1, v2, t2, y2, k, k2, I_t2, F2t2, the inline integral of F2(t-hat) dt-hat, [(t1 + t2) - t1] = t2, -m2v1, +m2v1, y1, k2v1^2, (F2 - m2g), vterm, [(dv/dt) = 0].
- **Cross-references (23).** The unit log's undefined references on render pages 1-3 were checked in order against the printed wording.
  - Edcap: ch4:sec:2.2, ch4, ch4:sec:2.2.1.
  - "Section 2.2.1 to Section 2.2" and "from 2.2.1 to 2.2": sec:2.2.1 then sec:2.2, twice.
  - Equations: eq:40; eq:44 three times; eq:45, 46, 45, 47, 48, 49, 50, 51, 52, 53, 49, 48, 49.
  - All match the printed numbers, and all these labels exist in build/chapters/ch4.aux (2.2, 2.2.1, 40-53, 4).
  - "Section 2.2.3" is plain text, correctly so: it is a proposed section and has no label.
- **Editorial note (1).** It was checked against the compiled chapter 4 in build/main.pdf (pdftotext, logical pages 273-277, not the .tex).
  - Section 2.2.1 applies the rewrites of (40) and (44)-(53). The notation list gains v, y-hat, t-hat and I_t2. Editor's note E10 applies the change of the upper limit t to t-hat.
  - Editor's note E5 in Section 2.2.1 states that the Summary's plans are not carried out.
  - The edcap's statement is true.

## Discrepancies

| where | scan reading | compiled reading | severity |
|---|---|---|---|
| p703, list of added variables (render p1) | Hanging-indent definition list: the continuation lines "engine" and "(not the total altitude above the launch point)" align under the text after "=" | No hanging indent: "point)" wraps back to the item's left edge under "y-hat" | layout |

No other discrepancies on p703-p706. Wording, paragraphing, bullets, headings, every display and inline formula, and the reference targets all agree with the scan. The paragraph flow after displays is ambiguous in the typescript (for example "Note that the extended Caporaso-Bengen ..." after "and v2 = v1": the gap is typed-display spacing, not a clear blank line), so it is not reported.
