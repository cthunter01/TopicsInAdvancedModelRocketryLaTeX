# Audit ch4-sec2a, round 1, part 1 (scan PDF 552-560)

Auditor compared the scan page images with the compiled unit (build/unit/ch4-sec2a-1.png to -5.png, plus
zoomed crops of build/unit/ch4-sec2a.pdf). No .tex file was opened.

## 1. Pages and items checked

- Scan pages: figures/pages/p552.png to p560.png, one Read each. Zoomed crops of p554 ((19a), (19b), (20),
  (21), "in equations"), p556 ((24)-(27)), p557 ((28), (29), the unnumbered v display and inline fraction),
  p558 ((32)-(34)), p559 ((36)-(37)) are in build/zoom/audit_ch4-sec2a_r1_p1-*.
- Render pages: build/unit/ch4-sec2a-1.png to -4.png (content of PDF 552-560), and -5.png (the page after).
- Headings (6): 2. The Non-Oscillating Rocket: Solutions for Vehicles Launched Vertically; 2.1 The
  Specialized Differential Equation for the Vertical Case; 2.1.1 Fehskens-Malewicki Solution; 2.1.2
  Caporaso-Bengen Solution; 2.1.3 Caporaso-Riccati Solution; 2.2 Extension of the Solutions to Multistaged
  Vehicles. All correct in wording and number.
- Numbered equations (23): (18), (19a), (19b), (20)-(39). Each was checked symbol by symbol against the scan:
  signs, exponents, subscripts, dots (u-dot, u-double-dot), brackets, radical extents, fraction bars, the
  integral limits (both t_b in (25)), the evaluation bar with y_b,v_b over 0,0 in (23), the equation number
  and its place in the sequence. The (19a)/(19b) pair is a subequations group: "equations (19)" on p556
  resolves to the group label (ch4:eq:19 is in the .aux).
- Unnumbered displays (2): v = (m/k)(u-dot/u) (p557); A_1H - A_2H = 0 (p559). Both correct.
- Inline formulas: about 40, including the inline fractions (m/k)(u-dot/u) on p557 and p558, v(dy/dt), kyv,
  ky_bv_b, v = v_b, y = y_b, t = 0, t = t_b, v_y, F(t), m(t), mg, t_b, I_t, A_1, A_2, e, H. All correct.
- Lists (1): the assumptions list (a)-(c) on p553. Correct.
- Tables, figures, captions: none on these pages.
- Prose: checked sentence by sentence. Wording, paragraph breaks (indented paragraphs vs. text that
  resumes after a display) and emphasis (idealized; separation of variables; argument; truncated;
  velocity; burnout altitude does; linear; will; initial conditions; burnout velocity; burnout altitude;
  Fehskens-Malewicki; Caporaso-Bengen; Caporaso-Riccati) all match the scan.
- Cross-references to the previous unit: the undefined-reference lines in build/unit/ch4-sec2a.log give
  the order 16, 17, 16, 17, 16, 17, 17, 16 for the "??" on render page 1. This matches the scan: "(16) and
  (17)" three times, then "equation (17) becomes identically zero and equation (16)".
- Silent slip fixes observed (intended, not discrepancies): "in equations (20) and (21)" at the start of a
  sentence on p554 (the lowercase i is clear in the zoom) is set "In"; "methematics" (p558) is set
  "mathematics".
- Survey briefing verified for PDF 552-560. The equation pages are right: (18) p553; (19a), (19b), (20),
  (21) p554; (22), (23) p555; (24)-(27) p556; (28)-(31) p557; (32)-(34) p558; (35)-(39) p559. There is no
  numbered display on p560. The unnumbered displays on p557 and p559, the two inline hand fractions, the
  underlined phrases and the survey's equation remarks (both upper limits t_b in (25); the long fraction bar
  in (27); script ln in (21) and (39)) all agree with the scan.

## 2. Discrepancies

none
