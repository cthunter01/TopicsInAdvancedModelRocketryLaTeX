# v2 audit: ch4/fig11 (round 1)

Sources checked:
- Scan `figures/ch4/fig11.png`, read at 3x.
- Redraw `figures/v2/ch4/fig11.pdf`:
  - 300 and 600 dpi renders and `build/v2/png/ch4-fig11-compare.png`;
  - a fresh compile in scratch (clean log, pixel-identical);
  - `pdffonts` (all embedded); no opacity operators or soft masks.
- Sources `fig11.tex`, `fig11.py`, `fig11-a/b/c.csv`, `fig11-marks.csv` and `fig11.calib.json`, plus
  `trajectory.py` (B4) and `figures/v2/common/b4.csv`.
- Inventory row `ch4-fig11` (`figures/v2/inventory.csv`:142).
- Text:
  - `chapters/ch4-sec3.tex`:78-131 (eqs. (106)-(115) and (125)-(131), "the first meter or so", .001 s);
  - :139-168 (30 deg, cases, times marked);
  - :185-192 (caption);
  - :276-291.
- `chapters/ch4-sec2b.tex`:169-192 (eqs. (73), (74)) and `chapters/ch4-sec4.tex`:481 (m_f 8.33 g).
- `corrections/v2-figures.md`:69-73 (Fig 11 decision) and STYLE.md sections 15 and 16.

Checks made:
- **Equations.** `fig11.py` implements the book's 2-D method as written:
  - Launch rod, eqs. (125)-(131): $\Delta v = \Delta t[F - mg\cos\theta_o - kv^2]/m$, $\Delta y$ and $\Delta x$
    with $(v + \Delta v/2)\cos\theta_o$ and $\sin\theta_o$, for 1 m of travel. The model is held on the pad while
    $F < mg\cos\theta_o$.
  - Free flight, eqs. (106)-(115): thrust along the velocity, drag $kv\dot y$ and $kv\dot x$, half-step position
    update, $v$ from (112).
  - Coast: the same equations with $F = 0$ at the burnout mass.
  - dt = .001 s, $\theta_o$ = 30 deg, g = 9.8, and the caption's three cases.
  - B4 thrust by (73a)-(73c) from the Fig 4 lettering. Mass by eq. (74) with $c = I_t/m_f$; I checked (74a)-(74c)
    against the integral of (73): $I_t$ = 5.00 N-s.
- **Independent check.**
  - My own implementation (integer step count, mass from the integrated thrust) agrees with `fig11.py` to 0.001 s
    and 0.05 m.
  - Rerunning `fig11.py` in a scratch tree reproduces all four CSVs byte for byte.
  - With float time accumulation, one extra 1 ms step of thrust at burnout moves (b)'s impact to 13.07 s. The
    script's integer stepping is the correct reading.
- **Burnout points against the caption:**
  - (a) (81.5, 131.1) against 82/131;
  - (b) (34.7, 51.2) against 35/51;
  - (c) (15.1, 18.75) against 15/19.
  All three round to the caption.
- **Computed against printed times (owner decision 2026-10-01: computed times marked):**

  | curve | apex (m) | apex time: computed / printed | impact (m) | impact time: computed / printed |
  |---|---|---|---|---|
  | (a) | (338, 418) | 7.07 / 5.60 | 487 | 19.16 / 16.70 |
  | (b) | (207, 194) | 6.02 / 6.20 | 348 | 13.06 / 14.30 |
  | (c) | (39, 33) | 2.72 / 2.80 | 63 | 5.70 / 5.70 |

  The redraw letters exactly the computed values (from `fig11-marks.csv`). Each leader starts at the computed apex
  (where $\dot y$ changes sign) or at the impact.
- **Sensitivity of the times**, all to 2 decimals:
  - dt .0005 s: no change.
  - Thrust and mass at mid-interval: within 0.004 s.
  - dt .01 s: within 0.04 s.
  - Rod length 0.5-2 m (the text says "the first meter or so"): (a) apex 7.06-7.09 s, impact 19.11-19.20 s;
    (b) 5.99-6.05 s and 13.00-13.14 s; (c) 2.69-2.76 s and 5.63-5.80 s.
  - With the shared digitized `b4.csv` (5.09 N-s) instead of (73): times move by at most 0.12 s, and burnout (a)
    becomes 81/130, which no longer matches the caption. So (73) is the right thrust function here, as in Figs 6
    and 16. Rule 5 governs the drawn thrust curves, not this computation.
- **Overlay.** The CSVs carry t, x, y, so I overlaid their x and y columns:
  - (c): 95% within 1.00 px (0.17 mm) of the ink, max 1.0 px. It matches the 1973 curve.
  - (a) and (b), first 3 s: 95% within 1.41 and 1.00 px.
  - (a) and (b), whole curves: 94.4 px (16 mm) and 9.2 px (1.6 mm). This is the approved departure after burnout.
- **Lettering against the inventory.**
  - Titles $x$ (m) and $y$ (m); x ticks 0-600 by 100; y ticks 0-400 by 100. The axis runs to 450 because the
    computed apex is 418 m.
  - Tags a, b, c.
  - Six times, now computed.
- **Caption and text.**
  - The caption's x_b, y_b and 1.20 sec burn hold.
  - Trajectories are continued to impact.
  - No text cites the Fig 11 times; I grepped chapters/ and backmatter/.
  - The printed anomaly (apex of (a) at 5.60 s, earlier than (b)'s 6.20 s although (a) climbs twice as high) is
    gone: 7.07 > 6.02.
- **Legibility.** Every label is at least 1.8 mm from every curve, and the tags clear their curves by 0.6 mm.
- **House rules and family.** The template is identical to Figs 10 and 12-14: 4.2 in axes, 0.007 in/m, s1/s2/s3
  solid, curve tags, ink times on `leader` lines.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The Fig 11 record in corrections/v2-figures.md is stale. It says "the 1973 times are recorded here", but it records only the apex of (a) (418 m at 7.07 s against 368 m at 5.60 s). It names the vertical method, eqs. (83)-(87), rather than eqs. (106)-(115) with (125)-(131). It still ends with the gate question ("Recompute ... or digitize ... **gate**"), although the paragraph opens with DECIDED. | corrections/v2-figures.md:69-73 | Rewrite it as decided. Record all six pairs, computed against printed: (a) 7.07/19.16 against 5.60/16.70; (b) 6.02/13.06 against 6.20/14.30; (c) 2.72/5.70 against 2.80/5.70. Add the computed apex and impact points ((338, 418)/487, (207, 194)/348, (39, 33)/63 m) and the equations (106)-(115), (125)-(131), (73), (74). (This file is outside the figure, so the orchestrator should make the change.) |
| 2 | note | `digitize.py overlay` reads the first two columns, but `fig11-*.csv` lead with t. On the raw CSVs the overlay plots (t, x) and reports meaningless numbers (a 13.4 px, b 8.0 px, c 4.0 px, "MISMATCH"). The correct numbers are in the checks above. | fig11.py (CSV layout) | Optional: say in the fig11.py docstring that the overlay needs columns 2-3 (e.g. `cut -d, -f2,3`), or write x, y first and t last. |
| 3 | note | The second decimal of the computed times depends on the length of the launch rod, which the text leaves loose ("the first meter or so"). Over 0.5-2 m the times move by up to 0.1 s ((c) impact 5.63-5.80 s). The 1 m used is the text's figure. | fig11.py ROD | none |
| 4 | note | The burnout points are not marked, as printed (an editorial option in the inventory; `fig11-marks.csv` already has them). | - | none (owner's option) |

## Verdict

pass (0 must-fix, 1 should-fix, which lies outside the figure's files)
