# Version 2 figures: doubts, mismatches and decisions

Found while surveying the 147 line figures (inventory `figures/v2/inventory.csv`, 2026-09-30) and while redrawing
them. Each item says what the 1973 artwork shows, what the book's text, captions or equations say, and what the
redraw does. Status: **gate** (the user decides at the chapter's gate), **rule** (a standing rule below settles
it; confirm at the gate), **minor** (logged only, no note in the book: see the no-notes rule for minor numeric
slips), **v1** (a question about the text, not the figure).

## Standing rules (proposed at the pilot gate)

1. **The text is right about line styles.** Where a caption or sentence names a line style the 1973 art does not
   use, the redraw uses the named style, so the book stays self-consistent: Ch2 Fig 11 envelope ("dotted",
   printed dashed); Ch3 Fig 27 control surface ("dotted line", printed dashed); Ch3 Fig 39 ("dotted", printed
   dashed); Ch3 Fig 54 wake lines ("dotted" and "wavy", printed dashed and straight). **rule**
2. **Lettering stays as printed** where the figure and the text use different symbols for the same thing (the
   v1 text is not touched): Ch2 Fig 20 $T_1$, $M_{s1}$ (text $t_1$, $M_s t_1$); Ch2 Fig 30 $\varphi_c$ (eq. (73a)
   $\varphi$); Ch2 Figs 36-41 $\bar Z_{T(B)}$ (eqs. (89), (92), (97) $\bar Z_T$); Ch2 Fig 42 $r_o$, $r_i$
   (eq. (105b) $R_o$, $R_i$); Ch2 Figs 43, 50 circled lowercase panel letters (text "43A", "Rocket A-F"); Ch2
   Fig 6 lowercase $f$ and no origin label O. **rule**
3. **Non-logarithmic "log" grids.** Ch3 Figs 22, 26, 51, 52 and 55 are drawn on paper whose intermediate lines
   are not at log positions (the "2" line at about 0.43 of each decade instead of 0.30). Redraws use true log
   axes; computed curves are computed; a digitized curve is read against the drawn gridlines (piecewise
   calibration between them), not against a log fit. **rule**
4. **Geometry drawn correctly.** A schematic whose 1973 geometry contradicts its own labels is drawn
   consistently, same labels: Ch4 Fig 2 (x axis drawn oblique to y), Ch4 Fig 15(b) ($g\sin\theta$ and $\theta$
   inconsistent with the drawing), Ch2 Figs 12, 13, 26 (the "Slope = $\Omega_{x0}$" line is not tangent to the
   curve; the redraw makes it tangent), Ch2 Fig 48 (the scale bar is about 6% longer than the drawing's scale;
   the redraw is drawn to its dimensions with a true scale bar). **rule**
5. **One engine, one curve.** The B4 thrust curve is traced slightly differently in Ch1 Figs 4, 5 and Ch4 Fig 4;
   the redraws share one digitized B4 curve (`figures/v2/common/b4.csv`, from the 1994 Ch4 Fig 4). **Exception:**
   Ch1 Fig 4 is a worked example whose lettered results (the rectangle areas of (b), the 49.7 squares of (c), the
   weights of (d)) were read off its own tracing, which falls from the spike more slowly: its four panels use
   that tracing (`b4-1973.csv`, from panel (a); area 5.19 N-sec), on which the rectangles fit (audit round 1).
   **rule**

## Pilot gate decisions (user, 2026-09-30)

- Formulas from outside the book that the book relies on (the 1962 US Standard Atmosphere for Ch3 Figs 2, 7, 8;
  Lamb's prolate spheroid for Ch3 Fig 35; slender-body theory for Ch3 Fig 40; Mangler's scaling for Ch3 Figs 20,
  21(b)): **compute from the formulas** (checked against the scan by overlay; named in About This Edition).
- Computed curves that differ visibly from the 1973 art (Ch2 Figs 25, 49; Ch3 Fig 22; Ch4 Fig 6 and the like):
  **use the computed curves**.
- Standing rules 1-5 (with the Ch1 Fig 4 exception to rule 5): **approved**.
- Ch1 Fig 2 (1994): **the arrow only over $A_e$**, in Chapter 1 and in the supplement Part alike (one form of the
  drawing; the 1994 drawing's long arrow over the whole pressure term is not kept). The typed text of the
  supplement Part, which reproduces the 1994 document, is unchanged.

## Decisions for the gates

- **Formulas from outside the book** (pilot gate; ch3-fig02 is a pilot sample). Ch3 Figs 2, 7, 8 are reproduced
  exactly by the 1962 US Standard Atmosphere formulas, which the book uses but does not print; Ch3 Fig 35 by
  Lamb's prolate-spheroid result, Fig 40 by slender-body theory, Figs 20 and 21(b) by Mangler's $\sqrt3$
  scaling of the flat-plate profile. Proposal: compute them from the cited source when the overlay against the
  scan passes (95% of points within 0.5 mm), and say so in "About This Edition"; otherwise digitize. **gate**
- **Ch1 Fig 2 (1994).** The artwork's arrow spans the whole pressure term; the chapter caption writes
  $(P_e - P_a)\vec{A}_e$ under Mandell's 1994 vector-notation rule (arrow over $A_e$ only). Decided at the pilot
  gate: the redraw follows the rule, in both places.
- **Ch2 Fig 25** (pilot sample). Computed from eq. (48b), the tails beyond $\beta \approx 1.6$ lie up to
  $0.1/C_1$ below the 1973 curves (at $\beta = 1.95$: computed 0.36, 0.34, 0.29, 0.25, 0.21, 0.12 against drawn
  0.46, 0.42, 0.35, 0.29, 0.24, 0.16, in units of $1/C_1$, for $\zeta = 0$ to 2); $\zeta = 2$ is drawn low near
  $\beta = 0.5$. Ch2 Fig 31 is the same plot. **gate** (pilot)
- **Ch2 Fig 49.** The drawn curve reaches $8/C_1$ at $\zeta \approx 0.052$ where eq. (50), which the text uses,
  gives about $9.6/C_1$; computed from eq. (50). **gate**
- **Ch2 Figs 34, 35.** The drawn C.P. marks (about 0.59L and 0.42L) match neither eqs. (82)/(84) nor the formula
  in the v1 editor's note. Keep as drawn (illustrative) or place by the equations. **gate**
- **Ch3 Fig 22** (pilot sample). Caption $B = 1740$, text 1700, formula 1742.6 (v1 already notes the caption and
  text); curve C starts on curve A only with about 1742; curve A is drawn about 0.1 decade high. Computed on
  true log axes with the formula. **gate** (pilot)
- **Ch4 Fig 11.** The book's own method (eqs. (83)-(87), 0.001 s steps, B4 from Fig 4 and Table 1) matches all
  three captioned burnout points and the whole of curve (c), but for curves (a) and (b) the printed apex, impact
  point and times differ badly after burnout (curve (a): computed apex 418 m at 7.07 s, printed 368 m at 5.60 s).
  Recompute (and the printed times then disagree with the drawing) or digitize the printed curves. **gate**
- **Ch4 Fig 6** (pilot sample 6(a)). Computed with the book's own method (`figures/v2/ch4/trajectory.py`: the
  interval method (83)-(87) with the mass by eq. (74), which reproduces Table 2's "No disturbance" row; the
  approximations (20), (21), (27), (28), (67)), the curves keep the printed shapes but sit up to about 1
  percentage point from them: the overlay on the scan puts 95% of the points 4-6 px (0.7-1.0 mm) from the ink
  for all four curves, the k_min pair about 0.6 point low throughout. The book does not state the twenty liftoff
  masses, the percent-error formula (100 (approx - exact)/exact reproduces the shapes) or its 360/65 program's
  details; no single variant tried (g, a mass linear in time, thrust at the interval's end, dt) closes the gap
  at both ends. Keep the computed curves (the proposal) or trace the printed ones. **gate** (pilot)
- **Ch4 Figs 5, 7-10, 12-14** (engines B14, D4, F100, F7): the book does not give their thrust curves,
  propellant masses (and, for Fig 8, the transonic drag model), so these are digitized; Ch4 Figs 6, 11 and 16
  (B4) are computable. **rule** (compute-else-digitize)

## Minor (logged only)

- Ch1 Fig 4(b): the lettered areas are not listed left to right and sum to 5.20 N-sec against the engine's 5.0;
  kept as printed.
- Ch1 Fig 9: the caption relies on the C.P. and C.G., which are not drawn; kept as printed.
- Ch1 Fig 4(c): the curve (the figure's own tracing, 5.19 N-sec) encloses about 52 of the 0.1 N-sec squares,
  against the lettered count of 49.7 (4.97 N-sec); the book's count is kept.
- Ch2 Fig 36 (1973): eq. (89) needs $x_t$, which the figure does not mark; kept as printed.
- Ch2 Fig 7: the curve must flatten to zero slope near 0.3 rad, which ch2-sec5.tex:252-255 relies on; the
  digitized curve keeps it.
- Ch3 Figs 14, 15: printed 1.73 and 0.865 against Table 1's 1.7208 and 0.8604; curves computed from Table 1,
  printed values kept.
- Ch3 Fig 34: the caption mentions experimental data; only the fitted curve is drawn; kept.
- Ch4 Fig 4 (1973 and 1994): the dashed approximation's descending leg bends; computed as the straight lines
  of eqs. (73a)-(73c).
- Ch2 Fig 52 (2022) is eq. (73b) with $\mathit{AR}_c = 1.25/C_1$ (not eqs. (115)-(117)); computed.

## Questions about the text (v1, outside the figure work)

- **Ch4 Section 2.5** (ch4-sec2b.tex:322-330) says the approximations' maximum error is less than the 10%
  total-impulse scatter; several panels of Figs 5-9 show errors of 12-15% and more. No note in v1. **v1**
- **Ch3 eq. (171b)** (ch3-sec6a.tex:267) prints $1 + \pi\,\ell/d_m$, but Fig 46 plots the ellipsoid line as
  $\pi\,\ell/d_m$, which is the asymptote of eq. (171a); the "1 +" may be a 1973 error. Not in corrections/ch3.md;
  to verify at the Chapter 3 prep. **v1**
