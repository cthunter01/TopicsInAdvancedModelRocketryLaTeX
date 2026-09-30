# v2 audit: ch1/fig09 (round 1)

Sources checked: figures/ch1/fig09.png (scan; rocket, pad, vector diagram and path tip upscaled 4-6x);
figures/v2/ch1/fig09.pdf (rendered 300 and 600 dpi) and build/v2/png/ch1-fig09-compare.png;
figures/v2/ch1/fig09.tex:1-37; figures/v2/inventory.csv row ch1-fig09; caption chapters/ch1-sec3.tex:50-58 and
citing text ch1-sec3.tex:41-45; corrections/v2-figures.md (minor item: C.P. and C.G. not drawn);
figures/v2/tamrfig.sty (`vec`, `guide`, `\pic{rocket}`, `\plumeshape`, `panel`); STYLE.md section 16.

Checked and correct:
- **Wind direction.**
  - The wind blows from the right in both panels. (a) has five arrows pointing left and (b) has seven.
  - "Wind" is set rotated 90 deg beside each column of arrows.
- **Vectors of (a).**
  - $\vec{V}$ is vertical from the origin, labelled at its left near the tip.
  - $\vec{U}$ is horizontal, pointing left, drawn with its head at the common origin (tail at the right),
    i.e. in the wind's direction, as printed. It is labelled right of its tail.
  - The diagonal from the origin to the far corner is up and to the right, which is $\vec{V} + (-\vec{U})$
    for $\vec{U}$ pointing left. It is labelled $\vec{V} + (-\vec{U})$, as the caption writes it.
  - Dashed lines complete the rectangle.
  - The origin sits just above the rocket's nose, as printed.
- **Launcher of (a).** The rocket is nose up, just clear of the rod's top (gap 0.2 cm), on a base plate with
  a hub.
- **Path of (b).**
  - It starts almost vertical (83 deg) and turns to 50 deg, i.e. into the wind (to the right, against wind
    blowing left), as the caption's "flies into the wind" requires.
  - A small rocket at its end points along the path's end tangent (50 deg; nose at the end + 0.9 cm along 50
    deg).
- **Legibility.** All arrowheads are visible, and no label touches a line.
- **Panel letters.** (a) and (b) are present.
- **Omissions already logged.** C.P. and C.G. are not drawn, as printed; this is the minor item in
  corrections/v2-figures.md.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | must-fix | The exhaust plume of the rocket in (a) is missing. In the scan a spindle-shaped plume hangs below the fins, about half the rocket's length, pointed at the bottom, between the tail and the rod's top. It shows the rocket leaving the launcher under thrust. The redraw's pic has `plume` at its default 0, so the rocket is drawn without it. The inventory's panel description omits it too. | fig09.tex:15-16 (pic keys), 13 (rod top at 5.1) | Add `plume=0.8` (about half the 1.6 length, as printed: 27 px of plume under a 50 px rocket) to the pic keys, and lower the rod's top to about 4.3 so that a gap stays open between the plume's point and the rod. |
| 2 | should-fix | The rod's "fillet brace" does not read as a brace. It is a thin S-curve from the hub's top right corner running up beside the rod to (0.02, 0.8), nearly parallel to it and not joined to it, so at final size it looks like a loose wire. In the scan the brace is a concave fillet (a quarter-round gusset). It leaves the rod about 0.15 of the pad's width above the plate and sweeps out to the plate's top about the same distance to the right of the rod. | fig09.tex:14 | Draw a concave fillet from the rod to the plate's top, e.g. `\draw[outline] (0,0.5) .. controls (0,0.3) and (0.1,0.18) .. (0.3,0.18);` (the hub box of line 12 then sits inside the fillet's foot). |
| 3 | note | The vector rectangle's proportions differ from the print: $\lvert\vec{U}\rvert/\lvert\vec{V}\rvert$ = 1.5/2.2 = 0.68 against about 0.51 printed (100 x 51 px), so the diagonal leans 34 deg from vertical against 27 deg. The figure is schematic and the text gives no magnitudes, so the meaning is unchanged. | fig09.tex:18-22 | Optional: U = 1.1 (tail at x = 1.1) to keep the printed lean. |
| 4 | note | "$\vec{V} + (-\vec{U})$" sits wholly outside the rectangle, 0.12 cm right of the dashed right side and about 0.8 cm from the diagonal it names. In the print the label starts inside the rectangle, next to the diagonal, and straddles the dashed line. Since the diagonal is the only unlabelled heavy vector the association still holds. | fig09.tex:23 | Optional: move the label in to start just right of the diagonal (e.g. `at (0.95,8.3)` with a white knock-out over the dashed line), or add a short leader. |
| 5 | note | The panel letters sit at the lower right, as printed, while STYLE.md section 16 places panel letters "at the upper right of the panel". Figs 1 and 10 follow the same lower-right placement. | fig09.tex:26, 34 | Decide one convention for the drawings (the gate), then apply it to Figs 1, 9 and 10 together. |

## Verdict

fix (1 must-fix, 1 should-fix)
