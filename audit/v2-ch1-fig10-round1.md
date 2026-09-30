# v2 audit: ch1/fig10 (round 1)

Sources checked: figures/ch1/fig10.png (scan; each panel's tail region upscaled 4x); figures/v2/ch1/fig10.pdf
(rendered 300 and 400 dpi, each panel cropped); figures/v2/ch1/fig10.tex:1-67; figures/v2/inventory.csv row
ch1-fig10; caption chapters/ch1-sec3.tex:106-119 and citing text ch1-sec3.tex:97-101;
corrections/v2-figures.md; figures/v2/tamrfig.sty (`\pic{rocket}`, `\plumeshape`, `cg mark`, `cp mark`,
`panel`); STYLE.md section 16.

Checked and correct:
- **Common to all panels.** Six copies of one upright model rocket in a 3 x 2 arrangement, (a)-(c) above and
  (d)-(f) below. Each has the C.G. mark (quartered circle) at 0.36L and the C.P. mark (circle with dot) at 0.22L
  above the tail, so C.G. is above C.P. in every panel. The disturbing force is drawn as a heavy arrow. Panel
  letters (a)-(f) are present, and there is no other text, as printed.
- **(a).** Horizontal wind: small arrows pointing left beside the rocket, and a bold arrow pointing left with
  its tip at the C.P.
- **(b).** One fin's root is drawn canted across the body (a single slanted line, so one canted fin, as the
  caption's spin sentence needs). The bold arrow points left into the right fin.
- **(c).** Torsionally vibrating fins: deflected fin outlines plus crossing lines inside the body, and bold
  arrows from both sides pointing inward.
- **(d).** A skewed plume, a thin inclined thrust line that passes 0.14 cm left of the C.G. (so it has a moment
  arm, as printed), and a bold arrow at the tail pointing left.
- **(e).** A launch lug on the body at the C.G. level, a rod line beside the tail ending in a short cross-bar,
  and a bold arrow at the tail pointing left.
- **(f).**
  - The upper stage has no plume.
  - The lower stage is displaced 0.2 cm to the right and rotated 20 deg clockwise, with its fins. Its axis
    and fin line tilt the same way as printed.
  - Blast lines radiate from the joint.
  - A bold arrow pointing left has its tip at the upper stage's base.
  - "The lower stage has been blown to the right ... the base of the upper stage is pushed to the left" holds.
- **Aerodynamic/mechanical split.** (a)-(c) show aerodynamic sources (wind, fins) and (d)-(f) mechanical
  ones (engine, rod, staging), as the caption divides them.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | must-fix | In (d) the plume is skewed the wrong way. `rotate=-8, ..., rotate=-90` turns the plume 98 deg clockwise from +x, so it points down and to the LEFT: its point is at (-0.17, -1.19). The thin thrust line runs from upper left to lower RIGHT, (-0.28, 2.4) to (0.2, -1.3), 7.4 deg from vertical. The two cross under the tail and are 0.35 cm apart at the plume's point. In the scan the plume lies along the inclined line, both running down to the right. A plume deflected down-left would push the tail to the right, contradicting the bold arrow at the tail, which points left (and the scan). | fig10.tex:40 | `rotate=8` instead of `rotate=-8` (net -82 deg): the plume then points down-right along the thrust line. Check that the line still runs down the plume's middle. |
| 2 | should-fix | In (b) the canted-fin line starts at (-0.07, 0.85), inside the C.P. mark (centre y = 0.79, rim 0.70-0.88). Because it is drawn after the mark, it crosses the lower left of the C.P. symbol. In the scan the slanted line begins just below the C.P. mark. | fig10.tex:24 | Start the line below the mark on the same slant, e.g. `(-0.04,0.66) -- (0.07,-0.02)`. |
| 3 | should-fix | In (d) the scan continues the rocket's axis below the tail as a thin straight line as far as the thrust line reaches (about 0.37L). The misalignment is shown as the angle between that axis and the inclined thrust line. The redraw keeps only the pic's dash-dot stub (0.08L = 0.29 cm, inside the plume), so the inclined line has no reference below the tail. | fig10.tex:39-41 | Add `\draw[thin line] (0,0) -- (0,-1.3);` in (d). |
| 4 | note | (a) has 11 wind arrows (y = -1.0 to 3.5 step 0.45) where the print has 9. The arrow at y = 0.80 lies under the bold arrow (y = 0.79) and shows only as a grey tail beyond it; the print also hides one there. The lowest arrow (y = -1.0) nearly touches "(a)" (about 1 mm clear). | fig10.tex:18-20 | Optional: 9 arrows (e.g. `{-0.8,-0.25,...,3.6}`), skipping the one behind the bold arrow, and keep about 2 mm clear of the letter. |
| 5 | note | In (e) the rod is at x = r + 0.1 = 0.27, 0.03 cm outside the lug's outer face (lug from 0.17 to 0.24), so it is not quite in line with the lug it has just left. In the print the rod is in line with the lug. | fig10.tex:48-50 | Optional: rod at x = r + 0.035 (the lug's centre line), with its cross-bar centred on it. |
| 6 | note | The panel letters sit at the lower right, as printed, while STYLE.md section 16 places panel letters "at the upper right of the panel" (same as Figs 1 and 9). | fig10.tex:20-64 | Settle one convention for the drawings at the gate. |

## Verdict

fix (1 must-fix, 2 should-fix)
