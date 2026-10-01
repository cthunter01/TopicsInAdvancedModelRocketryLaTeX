# v2 audit: ch2/fig51 (round 1)

Sources checked: scan `figures/ch2/fig51.png` (fin regions zoomed 7x; row profiles across the canted-fin
body); redraw `figures/v2/ch2/fig51.tex` / `.pdf` (4.24 x 2.71 in, fonts embedded), rendered at 400 dpi and at
90.7 dpi (one scan pixel = one redraw unit) for an overlay; `build/v2/png/ch2-fig51{,-compare}.png`; inventory
row `ch2-fig51`; caption `chapters/ch2-sec6.tex:445-449`; citing text ch2-sec6.tex:363-366 and
`backmatter/supplement/s-ch2-2022.tex:28-30`; STYLE.md section 16.

Checks:
- **Lettering.** "Airfoiled fins", "Canted fins" and "Spinnerons" are present, centred under their rockets on
  one baseline (\small). These are the three techniques the text names "as illustrated in Figure 51".
- **Fin details.**
  - Airfoiled: the edge-on fin shows a flat-bottomed section, leading edge up (the rocket flies nose up),
    flat side to the right, as printed. Its thickness is 12% of the root chord (0.38 units, about 3.8 scan
    px), which matches the scan's.
  - Canted: the edge-on fin slants 13.4 deg (+-0.38 over the root chord). On the scan it runs -3.5 to +3.5 px
    across the axis. The two side-fin root lines run 0.92R to 0.6R (left) and 0.6R to 0.92R (right). On the
    scan they measure about 1.0R to 0.6R and 0.6R to 0.97R (row profiles, rows 196-226).
  - Spinnerons: each side fin has a tab below its square trailing edge, foreshortened to 0.85 cos 33 deg =
    0.71 with its inner edge cut back, as printed. The tabs of the edge-on fin and of the fin behind it are
    bent opposite ways, forming the printed inverted V below the tail. This is the correct projection: all
    four tabs turn in one sense, so the front and rear tabs appear mirrored in the image plane, and the side
    fins' tabs, which rotate about a horizontal hinge, appear foreshortened.
- **Overlay (my own check).** Each rocket aligned separately: redraw to scan 100% within 3 px (mean
  0.05-0.17 px), and scan to redraw 99.9-100%. This confirms the drafter's figures. The rockets are set
  closer together than printed (160 against about 203 scan px between axes). That is a layout choice and
  changes nothing.
- **Legibility.** The edge-on details are clear at 400 dpi and at final size: the airfoil is about 1.1 mm
  thick and the spinneron tabs are distinct. Nothing is clipped or overlapping.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The side-fin root lines of the canted rocket keep the 1973 schematic slant (0.92R to 0.6R). For a flat fin canted 13.4 deg at the limb, the true root curve would bow only from about 0.92R at its ends to R at mid-chord, almost on the body outline. The printed exaggeration is the visible cue that the fins are canted. There is no lettering for it to contradict, so standing rule 4 does not apply. | fig51.tex:40-41 | None. Keep as printed. |
| 2 | note | The edge-on fins are drawn at the outline weight (0.6pt). Fig 48 draws its edge-on fin at 0.4pt. This is a minor difference within the family. | fig51.tex:23 vs fig48.tex:61 | Optional: settle one weight for edge-on fins. |

## Verdict: pass (no must-fix)
