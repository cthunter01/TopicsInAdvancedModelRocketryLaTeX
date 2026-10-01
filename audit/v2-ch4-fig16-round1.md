# v2 audit: ch4/fig16 (round 1)

Sources checked:
- Scan `figures/ch4/fig16.png`, with 3x crops of the top, the lower left and the right of the overlay.
- Redraw `figures/v2/ch4/fig16.pdf`: 300 and 600 dpi renders, with crops of the engine-mass label, the k labels,
  the lower end of the Bengen line and the callout; `build/v2/png/ch4-fig16-compare.png`; `pdffonts`; a scan for
  opacity operators; the build log.
- Sources `fig16.tex`, `fig16.py`, `fig16.csv`, `fig16-bengen.csv` and `fig16.calib.json`, plus `trajectory.py`.
- Inventory row `ch4-fig16`.
- Text: `chapters/ch4-sec5.tex`:15-86 (Bengen's maxima, "Figure 19" with its ednote, how such charts are made),
  :140-150 (use as a Malewicki chart) and :159-171 (caption); `chapters/ch4-sec2a.tex`:55-64 (eqs. (20), (21));
  `chapters/ch4-sec2b.tex`:56-57 (eq. (67)); `chapters/ch4-sec3.tex`:145-148, 185-191 (m_o = .021 kg, the engine
  alone); `chapters/ch4-sec4.tex`:481 (propellant 8.33 g).
- `corrections/v2-figures.md` and STYLE.md sections 15 and 16.

Checks made:
- **Data reproduce.** Rerunning `fig16.py` in a scratch copy reproduces `fig16.csv` and `fig16-bengen.csv`
  byte for byte.
- **Equations.**
  - `trajectory.fehskens_malewicki` is eq. (20) for v_b and eq. (21) for y_b, with the mean of the liftoff and
    burnout masses and F = I_t/t_b. The coast is eq. (67) at m_b.
  - The B4 data are I_t 5.0 and t_b 1.20 (Fig 4 lettering) and m_p .00833 kg (Table 1), with g = 9.8.
  - Recomputed at every 7th row, the CSV matches to 0.005 m.
- **Values.**
  - k = .0001: 341.7, 353.3, 328.4, 233.8, 151.4 and 98.3 m at m_o = .0213, .03, .04, .06, .08 and .10, as the
    inventory's FM column gives.
  - Maxima: (.0250, 536.8), (.0282, 354.0), (.0316, 233.4), (.0348, 154.2), (.0373, 102.4) and (.0378, 68.6) for
    k = .00005 to .0016.
  - The top of the Bengen line is k = .0000321 at 700 m, m_o .0231.
- **Which method the 1973 chart used.** I overlaid all three computable variants on the scan with the drafter's
  calibration (residual 0.00 px):

  | variant | six curves, 95% to ink | Bengen line |
  |---------|------------------------|-------------|
  | Fehskens-Malewicki (the redraw) | 1.00-1.41 px (0.17-0.24 mm) | 3.63 px (0.61 mm), max 5.0 |
  | interval method (83)-(87), dt 0.001 | 2.00-3.16 px | 5.08 px |
  | Caporaso-Bengen (27), (28), (67) | 4.0-13.0 px | not run |

  - The engine-alone line at .021 is 95% 2.0 px from the drawn one.
  - So the 1973 curves are the FM solution itself.
  - The text says charts are made "using the methods of Section 2 except in very high-performance cases, where
    numerical interval methods must be used" (ch4-sec5.tex:82-84), and that Section 2 gives "closed-form,
    algebraic solutions" (:70-72). The drafter's choice is right on both counts.
- **Lettering.**
  - $y_{\max}$ (m), with the upright max of STYLE s15, and $m_o$ (kg).
  - y ticks 0-700 step 100. x ticks 0, 0.02, ..., 0.10 (house leading zero; printed .02 ...).
  - Grid every .01 kg and every 100 m, as printed.
  - The six k labels .00005, .0001, .0002, .0004, .0008 and .0016, keeping the leading dot as printed (precedent:
    Ch2 Fig 33 ".466L", Ch3 Fig 34 ".029"). They sit right of the Bengen line just above each maximum, and .00005
    sits on its falling branch, as printed.
  - "Line of Bengen's maxima" with a straight `\callout` leader. Its point (0.02375, 640) lies on the computed
    line (interpolated m_o .023752 at 640 m).
  - "$m_o$ of engine alone" set along the guide. The 1973 short slanted leader stroke is dropped because the label
    sits beside the line.
- **Caption and text.**
  - The k values are noted on the curves.
  - The Bengen line lies right of the engine-mass line everywhere (m_o >= .0231 against .021).
  - The optimum mass falls as k falls (ch4-sec5.tex:28-31).
  - The curves start at the loaded engine's mass (:84-86).
  - All of these hold.
- **Style.**
  - Six curves are more than the r1-r5 ramp, so they are one colour (s1) with a label on each, as STYLE s16 says.
  - The Bengen locus is `series2` (s2 dashed).
  - The engine-mass reference is `guide`.
  - The k labels and the callout sit in white knock-outs where the 1973 art breaks the grid. They are drawn
    after the curves, and I checked at 600 dpi that none of them covers a curve. The closest gaps are about 1 mm:
    ".00005" to its own curve, and ".0004", ".0008" to the Bengen line.
  - The engine label is drawn before the curves, so the curve starts at .021 paint over it.
  - Text is in ink, and there is no local redefinition of kit names: `callout label/.append style` is local to the
    picture.
  - `\pgfplotsinvokeforeach` is used as the pitfalls section asks.
  - Page 4.52 x 5.75 in. Fonts embedded, no transparency operators, clean log.
  - Legible at final size (tick labels \footnotesize, labels \small).

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The computed line of Bengen's maxima is 95% 3.63 px (0.61 mm; max 5.0 px) from the printed one, over the 3 px tolerance. Its lower end stops at m_o = .0378 kg on the .0016 curve, where the printed line, ruled by eye across flat maxima, runs on to about .040 kg. Two other facts are also unrecorded: Fig 16 uses FM (eqs. (20), (21), (67)), not the interval method that the owner's Fig 11 decision uses; and the evidence that the 1973 curves are FM. None of this is in `corrections/v2-figures.md` yet, and STYLE s16 says an overlay mismatch goes there. The drafter may not edit that file. | `corrections/v2-figures.md` (Chapter 4) | The orchestrator adds a Chapter 4 Minor entry. Suggested text: "Ch4 Fig 16: computed by Fehskens-Malewicki (20), (21) with the coast (67), as Section 5.1 says such charts are made (ch4-sec5.tex:82-84). The 1973 curves are this solution: 95% within 1.0-1.4 px, against 2.0-3.2 px for the interval method and 4-13 px for Caporaso-Bengen. The Bengen line is the locus of the computed maxima (k .000032 at 700 m to .0016): 95% 3.6 px, lower end .0378 kg against about .040 drawn." |
| 2 | note | The `fig16.py` docstring and the tex header say the interval method is "one line away" (METHOD = "interval"). The CSVs would follow that switch, but the hard-coded label and callout positions would not. With the interval method the .0016 maximum moves to .0407 kg, so the end of the Bengen line would run through the ".0016" label (box from .0384 kg, 72 m). The ".0008" (.0390) and ".0004" (.0360) labels would also sit on the line. | `fig16.tex`:33-39; `fig16.py` docstring | None for the redraw as it stands. If the method is ever switched, move the six labels. Optionally soften "one line away" in the comments. |
| 3 | note | The lowest ~15 m of the computed Bengen line turns vertical: the m_o of the maximum peaks at .0379 kg near k = .0013 and falls back to .0378 at .0016. This is a true property of the FM locus and is less than 0.1 mm at final size. | `fig16-bengen.csv` last rows | None. |
| 4 | note | The Bengen line is s2 dashed where the 1973 line is long-dash-short-dash. The caption names no line style, so the kit's second-series style is consistent. | `fig16.tex`:30 | None. |

## Verdict: pass
