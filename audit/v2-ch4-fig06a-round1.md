# v2 audit: ch4/fig06a (round 1)

Sources checked: scan `figures/ch4/fig06a.png` (2x upscale; column-by-column reading of the printed curves
with the piecewise `xgrid`/`ygrid` calibration); redraw `figures/v2/ch4/fig06a.pdf` (350 and 700 dpi renders,
crop of the k labels) and `build/v2/png/ch4-fig06a.png`; `figures/v2/ch4/fig06a.tex` lines 1-30, `fig06.py`,
`trajectory.py` (run: Table 2 regression ok, 111.407 / 78.058 / 6.461 / 265.561 / 343.618), `fig06a.csv`
(40 rows), `fig06a.calib.json`; `digitize.py overlay` of all four curves; inventory row `ch4-fig06a`
(`figures/v2/inventory.csv`:129); `chapters/ch4-sec2a.tex`:20-30 (average mass), :55-64 (eqs. (20), (21)),
:118-128 (eqs. (27), (28)); `chapters/ch4-sec2b.tex`:56-58 (eq. (67)), :101-110 (eqs. (68), (69)), :169-192
(eqs. (73), (74)), :281-287 (eqs. (83)-(87)), :308-330 (method and accuracy claims), :343-372 (collective caption
and key table, B4 $k_{\min} = .00005$, $k_{\max} = .002$), :400-406 (caption); `chapters/ch4-sec3.tex`:147-148,
:189 ($m_o = .021$ kg, the engine alone); `corrections/v2-figures.md`; `STYLE.md` section 16.

Checks made:
- **Formulas.** `trajectory.py` implements the book's equations as written:
  - Eqs. (83)-(87) exactly: $\Delta v = \Delta t[F - mg - kv^2]/m$, $\Delta y = \Delta t(v + \Delta v/2)$, dt = 0.001 s.
  - Thrust by eq. (73) (B4 from the Fig 4 lettering). $I_t$ by eq. (75) is 13(0.22)/2 + 3.5(1.02) = 5.00 N-s.
  - Mass lost at $F/c$ with $c = I_t/m_p$, which is eq. (74) with the exhaust velocity implied by Table 1's 8.33 g.
  - FM is eqs. (20)/(21) and CB is eqs. (27)/(28). Both use $m = m_o - m_p/2$ (the average of liftoff and burnout
    mass, ch4-sec2a.tex:25-26) and $F = I_t/t_b$.
  - The error is $100(\text{approx} - \text{exact})/\text{exact}$.
- **Independent check.** I integrated with RK4 (24,000 steps), the analytic mass function (74), and no pad
  clamp. The v_b errors (FM k_min / CB k_min / FM k_max / CB k_max) agree with the CSV within 0.04 point:
  - $m_o$ = 0.022: 2.69 / -4.40 / 8.98 / 7.51
  - $m_o$ = 0.04: 0.76 / -2.12 / 9.12 / 3.85
  - $m_o$ = 0.06: 0.28 / -0.99 / 7.98 / -0.24
  - $m_o$ = 0.10: -0.02 / -0.43 / 4.89 / -2.65
  The data are therefore the book's method correctly evaluated.
- **Lettering.**
  - y title "Percent error in $v_b$"; y ticks -15 to 15 in steps of 5; x title $m_o$ (kg); x ticks 0.02-0.10
    with minor ticks at 0.01 steps.
  - $k_{\max}$ and $k_{\min}$ (notation as in the text, ch4-sec2b.tex:348-351), each with two leaders.
  - Legend at lower right: solid "Fehskens-Malewicki", dashed "Caporaso-Bengen".
  - Thin zero line.
  - Each leader ends exactly on its curve: (0.060, 7.975) FM k_max, (0.046, 2.440) CB k_max, (0.030, 1.453)
    FM k_min, (0.030, -3.280) CB k_min, all matching the CSV.
- **Caption and text.** The panel shows the burnout-velocity error for B4 at the key table's two k values, as the
  caption and the collective caption say. The panel letter is supplied by `\figurepanel{a}` in the chapter.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The $k_{\min}$ callout is crowded onto the curves. (a) The label at (0.037, -1.35) almost touches the dashed CB $k_{\min}$ curve: the subscript "min" is within about 0.3 mm of it near $m_o$ = 0.040. (b) Its lower leader (south-west anchor to (0.030, -3.28)) runs along the dashed CB $k_{\min}$ curve for its whole length, so at final size it merges with the curve instead of pointing to it. (c) Its upper leader starts at the label's north-west corner, which sits on the zero line (y about 0), so it reads as a stub rising from the zero line. The 1973 art puts $k_{\min}$ at the left, about $m_o$ 0.022-0.028 and y about -1.5, in the open space between the zero line and CB $k_{\min}$, with two clearly angled leaders. | fig06a.tex:25-27 | Move the label to about (0.026, -1.7). Draw its leaders from its north and south anchors to FM $k_{\min}$ near 0.031 (1.37) and to CB $k_{\min}$ near 0.033 (-2.86), so that each meets its curve at a clear angle. |
| 2 | should-fix | The curves begin at $m_o$ = 0.022, about 1.3 mm right of the y axis. The printed curves begin at about 0.021 (6 px right of the axis on the scan, 0.001 kg), which is the engine-alone mass the chapter uses (ch4-sec3.tex:147-148, :189; Fig 11 case (a) $m_o$ = .021). At 0.021 the errors are 2.96 / -4.44 / 8.95 / 7.63, closer to the printed endpoints (about 3.0 / -4.2 / 9.2 / 8). | fig06.py:45-46 | Start the sampling at 0.021 (e.g. 0.021, then 0.022 + 0.002 i, or a 1 g step) and regenerate fig06a/b/c.csv. |
| 3 | should-fix | The overlay fails for all four curves, not only the k_min pair that is known. `digitize.py overlay` gives 95th percentiles of FM k_max 4.0 px, CB k_max 5.0 px, FM k_min 4.0 px and CB k_min 5.8 px, against a tolerance of 3 px. The k_max curves are also low: FM k_max prints 9.19 / 8.33 / 5.54 at 0.022 / 0.06 / 0.098 against 8.98 / 7.98 / 5.02 computed, and CB k_max prints about -2.0 against -2.64 at 0.098. So all four computed curves lie 0.2-0.6 point below the print. Part of this, 0.1-0.2, may be registration, since the printed zero line reads 0.05-0.2 above the tick-calibrated 0. STYLE section 16 requires a failed overlay to be written into `corrections/v2-figures.md`, which has no Ch4 Fig 6 entry; only the inventory's notes mention the offset. | corrections/v2-figures.md | Add a Ch4 Fig 6(a) entry (and 6(b)/(c) when they are audited): "computed by the book's method (verified independently), all curves 0.2-0.6 point below the print, cause unexplained". The data need no change. |
| 4 | note | The 1973 x axis is not linear: the printed tick spacing falls from 59.3 to 52.5 px per 0.01 kg. The calibration handles this piecewise (`xgrid`), and the redraw's linear axis is correct. | fig06a.calib.json | none |
| 5 | note | The known offset of the k_min curves below the print (up to about 0.6 point) was confirmed: FM k_min prints about 0.69 at 0.098 against 0.03 computed. It is not raised as a new problem. | - | none |

## Verdict

pass (0 must-fix, 3 should-fix)
