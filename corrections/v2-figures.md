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

## Chapter 2 (workflow wf_6ab5405f-ad9, 2026-09-30): for the Chapter 2 gate

- **C.P. placed by the equations, not where 1973 drew it** (the pilot decision "computed over drawn" applied to
  marks): Fig 34 C.P._CS by eq. (82) at 0.326 L behind Z_1 (drawn 0.589 L; the v1 note's Barrowman formula gives
  0.538 L); Fig 35 C.P._CB by eq. (84) at 0.674 L (drawn 0.417 L; Barrowman 0.462 L); Fig 36 (1994 and 1973)
  C.P._T by eq. (90) at 0.45 s from the root (drawn about 0.39 s; 2.2 mm outboard at final size). Each is a
  one-line change back to the drawn position. **gate**
- **One frame for a family:** Figs 21-23 share one omega_n and H/I_L (zeta = 0.25, 1, 1.7), so the three impulse
  responses compare directly; the 1973 Fig 23 is drawn at its own larger scale. Figs 16-19 and 26-29 likewise
  share one rocket each (the book gives no values for the sketches). **gate** (confirm)
- **Fig 44** (exploded moment balance): the 1973 box is drawn in two projections with the bearing plates detached;
  the redraw shows the box assembled in one projection, the other parts exploded as printed. Two bolt holes for the
  caption's plural. **gate** (confirm)
- **Fig 50 / Fig 43** circled letters: one form for both (the house circled tag; rule 2 keeps the lowercase).
  Settled in the consistency pass.

Chapter 2 gate (user, 2026-09-30): approved as proposed: C.P. marks by the equations (Figs 34, 35, 36), one
frame per sketch family, Fig 44 assembled in one projection, the house circled tag for Figs 43 and 50.

## Chapter 2: questions about the text (v1, outside the figure work)

- **Ch2 Fig 10 caption** (ch2-sec3a.tex:184): "viewed from the negative y axis" cannot show a rotation about X;
  +alpha_X moves the nose towards -Y, which is the viewer's right only when viewed from -X (the art and the redraw
  show that sense). Possible corrections/ch2.md query. **v1**

## Chapter 3 (workflow wf_60d8c862-d5f, 2026-09-30): for the Chapter 3 gate

- **Vector lettering** (Figs 1, 11, 12, 39). The 1973 art letters overbars: $\bar V$, $\bar D$ (Fig 1), $\bar n$,
  $\bar t$, $\bar V$ (Fig 11), $\bar V$ (Fig 12), $\bar U$ (Fig 39). The redraws set $\vec{}$, as the Fig 11 caption,
  the text and the Symbols list do (ch3-symbols.tex:106), as STYLE s14 asks wherever an arrow is drawn, and as the
  approved Ch1 Fig 6 does. Figs 1 and 12 also put heads on the 1973 headless V and D lines, as Ch1 Fig 8 does.
  Standing rule 2 (lettering as printed) points the other way. The alternative is the printed overbars, a one-line
  change per figure. Settled: the book's notation (\vec, as the pilot's Ch1 figures set it) is used throughout the
  redraws, so Ch4 Fig 1 will follow it too. **settled**
- **Fig 9** (fluid element). Drawn in the house orthographic view (STYLE s16). The element is therefore a box
  (dx 1.2, dy 1, dz 0.75), because a cube in this view puts its face centres on the front edge. The u(y) profile
  stands in the same view, and its arrows rise at 28 deg, parallel to the tau arrows. 1973 draws a cube in an
  oblique view with a flat profile and horizontal arrows. Confirm, or draw the profile flat beside the 3D element
  (u and tau are then 28 deg apart). **gate**
- **Fig 12** (drag constituents). The near fin, seen edge-on, is drawn on the axis (the inventory read it as the
  lug). Two parts move from where 1973 draws them. The launch lug goes from under the lower fin root (1973, x about
  5.8-6.4 of 6.4) to just ahead of the fins (x 4.25-4.85), so it does not overlap the root. The fin-tip vortex
  trails from the upper fin's tip; 1973 runs the edge-on fin's vortex along the axis behind the base. The callouts
  are unchanged. Confirm, or put the lug and the vortex where 1973 has them. **gate**
- **Fig 28** (half-body). Computed from the axisymmetric Rankine half-body (a point source in a uniform stream).
  This is an outside formula the pilot gate did not name; the caption appeals to potential theory. The body and
  streamlines match the 1973 art within 1-3 px, but the drawn pressures do not:
  - (a) The computed $C_p$ minimum is $-1/3$ at 0.79 R behind the nose; the drawn one is about $-0.39$ near 1.1 R.
    The computed curve also recovers faster: $-0.01$ against $-0.06$ at 6.7 R (overlay 95% 9 px, 1.5 mm).
  - (b) Both lobes share one scale, so the suction lobes reach 1.33 R from the axis against about 1.6 R printed
    (about 40% lower).

  The proposal is to keep the computed curves and name the Rankine half-body in About This Edition (Fig 27 uses
  the same body). The alternative is to digitize the printed curve and lobes (a change to one file). **gate**
- **Fig 37(b)** (trial rocket at angle of attack). The C.G. pivot (an unlabelled cg mark) stays where 1973 draws
  it: 20.3 cm from the tip (0.61 $\ell_b$). The book gives no C.G. for this rocket. Two estimates from the book's
  own numbers place it further aft:
  - Ch4 Table 1's static margin (2.06 cm) with the C.P. from Ch2 eqs. (88)-(92) (27.5 cm, $C_{N\alpha}$ = 15.0)
    puts it at 25.4 cm (0.77 $\ell_b$), about 8 mm further aft at the panel's size.
  - Ch4 Table 1's own $C_1 = 396v^2$ implies $C_{N\alpha} \approx 9.4$, which gives about 23.3 cm.

  So the book does not fix the position, and the drawn one is kept (one line, `\def\cg{25.4}`, would place it by
  the Ch2 equations). **minor**
- **Fig 46** ($S_s/S_m$ against fineness ratio). The redraw plots the exact eqs. (171a) (ellipsoid) and (171d)
  (cone). The 1973 art draws the straight lines $\pi\ell/d_m$ and $2\ell/d_m$, which the caption calls
  "approximate and ... terminated at the lower limit" (ch3-sec6a.tex:281-285). The exact curves lie above them by
  0.21 and 0.16 at $\ell/d_m$ = 1.5, and by 0.07 and 0.04 at 5-6 (at most 0.6 mm). With the exact curves the
  caption fits only the ogive line, which is (171c) in both versions. The alternative is `\exactfalse` (one line):
  it draws the printed lines, and the caption and the figure agree again. The ellipsoid line is then
  $\pi\ell/d_m$, not (171b) as printed (see the v1 question below). **gate**

Chapter 3 gate (user, 2026-10-01): Figs 9, 12 and 28 kept as redrawn (house 3D view; lug ahead of the fins and the
tip vortex from the upper fin; Rankine half-body pressures computed); Fig 46 keeps the EXACT curves of (171a) and
(171d) (the caption's "approximate" then holds for the ogive line (171c) only; caption kept as printed). Eq. (171b)
corrected in the text (corrections/ch3.md D37).

## Chapter 3: questions about the text (v1, outside the figure work)

- **Ch3 eq. (171b)** (ch3-sec6a.tex:267) prints $(1 + \pi\,\ell/d_m)$ for $\ell/d_m \gg 1$. Confirmed wrong (the
  open question in "Questions about the text" above). The asymptote of eq. (171a) (ch3-sec6a.tex:263-265) is
  $\pi\,\ell/d_m$: $\sin^{-1}e \approx \pi/2 - d_m/2\ell$, which cancels the 1. That is also the line the 1973
  Fig 46 draws. As printed, (171b) lies 0.80, 0.89 and 0.94 above (171a) at $\ell/d_m$ = 1.5, 3 and 6 ((171a)
  gives 4.917, 9.540 and 18.911; checked numerically). The owner decided (2026-10-01) to correct it in the text:
  (171b) now reads $\pi\ell/d_m$, with a note quoting the 1973 form (corrections/ch3.md D37). **applied**

## Chapter 3 minor (logged only)

- Ch3, chapter-wide (consistency pass):
  - Velocity profiles are in one family style: profile in s1 at 1pt, arrows in s1 at 0.5pt with small heads, base
    lines and walls in ink (Figs 6, 9, 10, 13, 16-18, 23, 25, 33).
  - Labelled free-stream velocities are `vec`.
  - Boundary-layer edges are a dashed `guide`, since the house dash-dot is a centre line. 1973 dash-dots them in
    Figs 13 and 17 and dashes them in Figs 10 and 25.
  - Hatched walls are about 2 mm deep.
  - The 1973 round-bar break is redrawn as `\breakline` (Figs 27, 29, 33, 44, 49).
  - Callout leaders are straight and headless.
  - Circled panel letters become the house `(a)` (Figs 18, 21, 47, 49, 54).
  - The Fig 4 y title is upright like those of Figs 2, 3, 7 and 8; 1973 rotates it.
  - Heads are added to velocity and flow lines printed without them, in the sense the drawing implies (Figs 1, 12,
    29, 30, 37).
- Ch3 Fig 1: the C.P. is placed by Barrowman for three fins at 0.813 L, where 1973 draws it. Four fins, as in
  Fig 12, would put it at 0.836 L, 1.8 mm aft. The loosely drawn 1973 fins become the house model's symmetric fins.
- Ch3 Fig 3: the unit "(°K)" is kept as printed; the text writes "288° Kelvin" (ch3-intro-sec2a.tex:238).
- Ch3 Fig 4: eq. (213) with the text's 340 m/sec reproduces the print. The 1962 standard's 340.29 m/sec (the
  credit's source) would raise the curve 0.29 m/sec.
- Ch3 Fig 7: the lettered $\mu_o$ = 1.78943e-5 is what Sutherland's formula gives at 288.16 K, or the English-unit
  table value converted; at 288.15 K it gives 1.78938e-5 (0.003%). Kept; the plotted ratio does not depend on it.
- Ch3 Fig 9: where the lower tau arrow runs inside the element it is drawn hidden; 1973 draws it solid through the
  front face.
- Ch3 Fig 10: the house model rocket of Figs 1, 10 and 12 is used, with fin span 1.5 d against 1973's 1.84 d.
- Ch3 Fig 11: the far half of the base rim is drawn as the true ellipse; the 1973 dashed half lies inside it. The
  body is a paraboloid of fineness 2.5 fitted to the outline (the book names neither the shape nor the fineness).
- Ch3 Fig 12: alpha is the true arc about the point where V meets the axis (1973 draws a short straight double
  arrow ahead of the nose). Not reproduced: a small V-shaped mark in the turbulent layer and two specks.
  Transition is shown by a tick.
- Ch3 Fig 13: the edge and the profiles share one $\delta(x)$, eq. (54). The 1973 edge flattens down the plate, so
  it is not a $\sqrt{x}$ curve (overlay 95% 8.95 px, 1.52 mm; max 20.8 px). The 1973 profiles are not drawn to that
  edge (profile 1 about twice its thickness), so the computed profile 1 is much thinner than printed (95% 1.5 mm).
- Ch3 Fig 15: the 1973 curve lies up to 0.04 left of eq. (46) for eta 1.2-3.2 (eta 1.4: 0.13 vs 0.158; 1.8: 0.215
  vs 0.253; 2.2: 0.34 vs 0.359; 3.2: 0.607 vs 0.617), overlay 95% 4.12 px (0.70 mm); the computed curve is kept.
  The dashed asymptote and the end of the dimension are at Table 1's 0.8604, under the lettered 0.865 (see the
  Figs 14, 15 entry).
- Ch3 Fig 16: the tangent is drawn true (rule 4): phi = 22.5 deg against about 21 deg in 1973. The vertex moves
  about 1.8 mm.
- Ch3 Fig 17: computed for the turbulent layer the caption names, which the 1973 art does not draw:
  - The edges follow eq. (80) as near-straight wedges, up to 16 px (2.7 mm) from the laminar-looking 1973 edges
    (about $x^{0.4}$).
  - The wake at B B$_1$ is a Gaussian defect with the momentum thickness of the 1/7-law profile at O (eqs. (73),
    (76)). Its dip reaches 0.77 $U_\infty$; 1973 draws about 0.35-0.37 $U_\infty$, which would need about three
    times the momentum deficit.
  - The corner letters A, A$_1$, B, B$_1$ and O stay italic, not curve tags, because Table 2 uses them as segment
    names.
- Ch3 Fig 18: (a) is a Falkner-Skan profile (eqs. (38)-(39), beta = -0.198, f''(0) = 0.02 to keep it attached and
  distinct from Fig 25's c). Its point of inflection is placed by the equation, about 4 mm below and left of the
  1973 circle (1973: y/delta about 0.55, u/U 0.6).
- Ch3 Fig 23:
  - S stays where 1973 puts it, 137 deg from A. Laminar separation on a cylinder is nearer 80 deg (Fig 24's
    subcritical curve), but the text gives no angle.
  - The hatched band is bounded by the fitted dividing streamline: 0.42a thick at B against 0.31a printed (about
    1.3 mm), with thinner lobes.
  - The innermost streamlines are up to 1.4 mm nearer the axis at the left edge than the freehand ones.
- Ch3 Fig 24: a $C_p$ ordinate title is added (the 1973 axis has none). The $R_d = 3\times10^5$ label moves from
  the right end, where the computed theory curve now runs, to above its curve's knee.
- Ch3 Fig 25:
  - Profiles a-e are Falkner-Skan (eqs. (38)-(39)). d and e use the reversed-flow lower branch, past the point
    where the text says the approximations hold: minima -0.08 and -0.12 $U_\infty$ against about -0.13 and -0.26
    drawn, so d is up to 1.4 mm off.
  - The streamlines are stream-function contours (freehand in 1973; 95% 7.2 px, max 15.7 px).
  - The u = 0 line is up to 1.9 mm from the drawn dash-dot.
- Ch3 Fig 27: the tube walls are hatched sections (1973: heavy solid lines); plain heavy outlines are a one-line
  change.
- Ch3 Fig 29: U is drawn as a vector pointing up, towards the nose-down bodies (the 1973 line has no head). The
  cone half-angles measure 22 deg (#4) and 39 deg (#5), which do not match Fig 31's "60°"/"45°" cones; left as
  drawn.
- Ch3 Fig 30: the inset flow lines get heads, and the y title $C_{Do}$ is kept as printed (the caption says "drag
  coefficient").
- Ch3 Fig 31: the "Hemisphere" icon is a true hemisphere (1973's flattened end protrudes about 0.4 d). The cones are
  as printed, "60°" with a 30 deg half-angle: the labels read as the angle between the surface and the base.
- Ch3 Fig 32: the y title $C_D$ is kept as printed (the text says pressure drag coefficient).
- Ch3 Fig 33: the solid-shaft break becomes `\breakline`, and the leaning base line of the velocity profile is drawn
  normal to the axis.
- Ch3 Fig 34: the inset moves 0.04 left and 0.015 down, and its leader is straight (1973 runs it out through the
  frame and back).
- Ch3 Fig 37: the flow-direction line has a head (as in Fig 38). The body is drawn at the lettered 2.06; 1973 draws
  1.93 at its own scale.
- Ch3 Fig 38:
  - The C.P. is at c/4 by Ch2 eq. (89) for the rectangular fin, under the Ch2 C.P. decision (1973: about 0.36 c).
    L, F, $D_i$, the flow line and the alpha vertex move 0.11 c forward with it.
  - alpha_i keeps the 1973 proportions (12.1 deg) so the schematic stays legible. The trial fin's eq. (144A) gives
    about 4.6 deg at alpha = 12 deg, with $D_i$ shorter than its arrowhead.
  - F is kept as lettered (the text says normal force N, ch3-sec5a.tex:261).
- Ch3 Fig 39:
  - (a) Square slab tips (1973: curled), and vortices 5 chords long (1973: about 6).
  - (b) The columns are set at an even pitch (shifts up to 1.2 mm).
  - (b) Section 2's end radius is 4.5 px against the measured 6, so it stays distinct from section 3.
  - (b) Tip 3's trailing-edge step is read as the extended trailing edge, which makes y the core's inboard offset
    there.
- Ch3 Fig 40: at d/b = .289 the computed $K_{B(F)}$ = 0.419 and $K_{F(B)}$ = 1.242, against the text's 0.44 and
  1.25 (ch3-sec5b.tex:38-40, eq. (147)) and the 1973 art's about 0.43 and 1.25. The 1973 $K_{B(F)}$ is drawn about
  0.03 low over d/b 0.6-0.95. The text keeps its readings. About This Edition should name slender-body theory
  (NACA Report 1307) as the source; the credit reads "After U.S.A.F. Stability and Control Datcom"
  (figure-credits.tex:231).
- Ch3 Fig 41: the fit is forced through $C_D$ = 0.75 with zero slope at 0 deg (the unconstrained fit starts at
  0.754, 0.6 px higher).
- Ch3 Fig 42: the drawn curve leaves $C_D$ = 0.20 at u/U = 0 with a slope of about 0.04, although drag should be
  even in the spin rate. Kept as drawn (measured data).
- Ch3 Fig 43: $\ell_n$ and $\ell_t$ are kept as lettered (the equations use $\ell_N$, $\ell_T$; rule 2, as D36 does
  for Fig 50).
- Ch3 Fig 44: the swept fin is a true parallelogram, within 3 px (1973's LE and TE drop 38 and 43 px). The ruled
  cell grid becomes booktabs rules, as in Fig 45; Fig 47 keeps thin cell rules, as Ch2 Fig 43 does.
- Ch3 Fig 46: the printed cone line is ruled about 1.5% steep (3.1 at 1.5 and 12.2 at 6, against 3.0 and 12.0), and
  both variants replace it. The ogive is (171c) in both, since the book gives no exact formula. The exact
  tangent-ogive area is 4.26 at 1.5 against 4.00, and 2.69 $\ell/d_m$ at 4.74, so the worked example's 2.7
  (ch3-sec6b.tex:69) holds.
- Ch3 Fig 47:
  - The plane inclinations are chosen (beta 48, 68.2 and 76 deg), since the book gives none.
  - Each nose is its section's half revolved exactly, so the (b) nose is blunter than 1973's (l/d 1.54 against
    about 2.3 by eye). The 1973 top and bottom drawings disagree, and a hyperbolic nose on this cone cannot exceed
    about 1.75.
  - The (b) and (c) planes face a different way from (a).
  - The cut-away piece is dashed in ink2 and the hidden edges in black; 1973 dashes both alike.
- Ch3 Fig 48: the fins are drawn to their lettering, which the 1973 fins do not follow (root LE to base 3.48 for
  3.30, sweep 1.81 for 1.91, tip chord 2.29 for 2.07, span 4.02 for 4.19; shifts up to 0.7 mm). The edge-on strip
  runs to the TE, 0.68 past the base, as the dimensions require.
- Ch3 Fig 49: drawn to the text's fin dimensions, as 1973 is, so it differs from Fig 48's lettering by 0.09 cm in
  root length (D26).
- Ch3 Fig 50: the drawing keeps the scan's proportions, not GCR-x (boattail $\ell_t$ 1.4 against GCR-x's 3);
  Fig 51's inset uses GCR-x.
- Ch3 Fig 51: the region 2/3 boundary is at the caption's 5e6 (D35), so the fin curves' kinks at 5.14e6 sit
  0.55 mm right of it. The inset follows the text's GCR-x; the 1973 inset is up to about 15% off.
- Ch3 Fig 52: above about 0.5 N the 1973 curves drift right of eq. (210) and Table 7 (0.6 N at about 2.25e6 drawn,
  near 2.0e6 computed; up to 1.7 mm). The computed curves are kept.
- Ch3 Fig 53: the digitized (a) is within 0.03 of Table 8's experimental column. The ogive ends at 1.25 as drawn,
  where Table 8 and the text give 1.27 (M 1.8-2.0). The "flat" 1.0 line, ruled straight on a leaning grid, is set
  to exactly 1.0.
- Ch3 Fig 54: "wavy lines delineate the wakes" is read as covering both the shear layers from the base corners to
  the neck and the far wake. Straight shear layers, as printed, are a one-line change.
- Ch3 Fig 55: eq. (230) with g = 9.8; the computed curves are kept, as for Ch2 Fig 25 and Ch3 Fig 22. Above k/m of
  about 0.04 the 1973 curves run long. At k/m = 0.094 they are drawn at 1.75, 3.74 and 6.31 s against 1.66, 3.17
  and 5.62 s computed (10, 25, 50 m). The 100 m curve meets t = 10 s at about 0.068 drawn, 0.084 computed. Below
  0.02 they agree within 0.03 s, so the 1973 tops look hand-faired.

### Style suggestions worth adopting

- Move the Chapter 3 profile styles (`profile`, `profile arrow`, `profile stroke`) into tamrfig.sty. Ten figures
  carry identical local copies (Figs 6, 9, 10, 13, 16-18, 23, 25, 33). Rename Fig 21's unrelated pgfplots
  `profile`.
- Add a hatched-wall helper `\wall[<side>]{<from>}{<to>}` with the settled 2 mm band (Figs 6, 13, 16-18, 25).
- Provide one CSV-path macro for TikZ drawings, covering a polyline, a mirrored edge and arrow rows. It would replace
  the local `\csvline`, `\csvarrows`, `\csvedge`, `\segments` and `\csvpath` of Figs 10, 12, 13, 25 and 39 and Ch2
  Fig 33. Add its pitfall to STYLE s16: with anchor=origin, zero must lie inside the hidden axis's limits.
- Flow-figure styles: `streamline` with a mid-line head, `wake` (the wavy snake), the long-dash-dot `dividing
  line`, and `eddy` (an arrow cased in white over hatching). Figs 12, 23, 25, 28, 33 and 54 each define their own.
- `\angleout`, the angular `\dimout` (Figs 16, 33 and 38 draw it by hand; Ch4 Fig 15(b) may need it). Also a
  `\dimout` with its label between the extension lines (Figs 43, 48, 50), and one placement for diameter labels
  (Figs 43, 45, 48, 50).
- Plot styles: `upright ylabel`, with the unit on a second line (Ch3 Figs 2-4, 7, 8, 40-42, 53, 55); `panel on grid`
  and a `curve label` knock-out (Ch1 Fig 4(c), Ch3 Figs 21, 24, 26); `inset blank` (Figs 51, 53); and one
  `tamr Rl axis` for the 1e4-1e7 log axis of Figs 22, 26, 51, 52, 55, at least 5 in wide so that the labelled 2-8
  ticks stay clear.
- Legends and labels: set the kit legend to fill opacity=1 (the flat-art rule; Fig 52 fixes it locally). Settle
  one legend and curve-label size: `\small` in Ch3, `\footnotesize` in the kit default, Ch2 Figs 24, 25, 30, 31 and
  Ch4 Fig 6(a).
- Series colours: state which four of r1-r5 a four-curve ordered family takes (r2-r5 in Fig 55). Add a rule, or an
  s4, for four unordered series (Fig 51).
- `\breakpath`, a path form of `\breakline` that reads the break amplitude. Document an amplitude of about 0.36 for
  a full-width tube (Figs 44, 49).
- Shared code: `figures/v2/common/blasius.py` (Figs 15, 19-21 import fig14.py) and a shared helper for digitized
  curves (Figs 30, 32).
- digitize.py:
  - a piecewise-bilinear "mesh" calibration from gridline crossings, for keystoned or leaning scans (Figs 26, 34-36,
    40, 53);
  - gridline masking in `overlay` (on dense grids, distance to ink says little: Figs 40, 51, 52, 55);
  - masking every ruling run of at least min_len in `trace` (Fig 41);
  - an overlay mode for drawings that renders the redraw at the scan's dpi, aligns by cross-correlation and
    reports ink-to-ink distances (Figs 33, 37; Ch2 Fig 48).
- 3D and rocket kit: a shorter-period phantom for small drawings (Fig 47 and Ch2 Fig 41 render short phantom
  segments solid); `hidden vec` (Fig 9); an axis-extension key on `\pic{rocket}` (Ch1 Figs 6-8, Ch3 Figs 1, 12);
  fins on a conical boattail in `\rocketfins` (Figs 50, 51).

## Minor (logged only)

- Ch2 Fig 4: the angular-velocity components only, no resultant (as printed); house vectors replace the 1973
  cone-and-ball heads (as in the approved Fig 3).
- Ch2 Fig 5: which line is fixed is not stated; the redraw takes the up-right line as the fixed horizontal
  (guide) and the lower one as the line on the wheel, turned through alpha in the sense of rotation.
- Ch2 Fig 7/9: the true M_c is flat from 0.30 rad (Fig 7) and from 0.287 rad (1973 Fig 9, about 1.5% lower); the
  redraws share the Fig 7 data. Fig 9's printed linear approximations are about 2% steeper than the lettered C_1,
  C_2 (the lower ends at about 1.9e6 against 1.875e6 at 150 rad/sec); computed from the lettering.
- Ch2 Fig 10: the 1973 sinusoid fits A = 1.73 alpha_X0 although its ticks letter A = 2.83 alpha_X0; the lettered
  ratio is kept (points b and f move 1.4 and 0.7 mm). Its Slope = Omega_X0 line is drawn as the true tangent.
- Ch2 Figs 11-14: computed curves within about 1 mm of the 1973 art (the envelope of Fig 11 lies up to 1 mm above
  the drawn one; Fig 14's divergence turns up more steeply in the art); Figs 12, 13, 26 tangents drawn true.
- Ch2 Figs 17, 19, 22: Fig 17's undershoot at 2 pi/omega (eq. (30)), drawn at 2.16; Fig 19 paired with Fig 18's
  C_1/I_L; Fig 22's t_m mark on the computed peak (the 1973 mark is 4 px off its own curve).
- Ch2 Fig 31: the zeta_c = .2 peak is 2.55/C_1 by eqs. (73b)/(75), drawn about 2.4/C_1 (as Fig 25).
- Ch2 Fig 33: the tangent ogive's C.P. by the text's rule is 0.460 L at the drawn fineness 2.4; the printed
  .466 L (the slender limit, 7/15) is drawn.
- Ch2 Fig 48: the end view's left fin, drawn about 2.7 cm too long in 1973, has the 5.08 span of the others.
- Ch2 Fig 49 (text): eq. (50) at zeta = 0.3 gives 1.7471, printed 1.746 (minor; corrections/ch2.md only).
- Ch2 Fig 52 (2022): tick labels 0, 0.5, ... (the values of the chart's 0.000, 0.500 ...); the spreadsheet's
  point markers are not drawn; omega_z kept lowercase as printed (rule 2).


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
- **Ch3 eq. (171b)** (ch3-sec6a.tex): corrected by the editor at the owner's direction, 2026-10-01 (see the Chapter 3
  section). **applied**
