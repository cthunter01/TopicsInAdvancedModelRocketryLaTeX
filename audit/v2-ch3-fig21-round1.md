# v2 audit: ch3/fig21 (round 1)

Sources checked: scan `figures/ch3/fig21.png` (2x of both panels); redraw `figures/v2/ch3/fig21.pdf` (300 and
600 dpi renders, crops of the panel letter and the y titles, `pdffonts`) and
`build/v2/png/ch3-fig21-compare.png`; sources `figures/v2/ch3/fig21.tex`, `fig21.py`, `fig21-a.csv`,
`fig21-b.csv`, `fig21.calib.json` (and `fig14.py`, which it imports); inventory row `ch3-fig21`
(`figures/v2/inventory.csv`:87); `chapters/ch3-sec3b.tex`:640-677 (citing text, caption, eqs. (94)-(96) and
"identical to that of Figure 14, except for a scale factor of two"); `corrections/v2-figures.md` (pilot gate:
Mangler for 21(b)); `STYLE.md` section 16; the approved panels-in-axes examples Ch1 Figs 3 and 4a and Ch2
Figs 20 and 46.

Checks made:
- **Curves.**
  - (a) u/U = f'(2η_2-D) by eq. (96). (b) u/U = f'(2√3 η_3-D) by Mangler's scaling, the same as Fig 20.
  - Both CSVs agree with my own ODE solution of eq. (51) to 1.8e-5.
  - (a) is Fig 14's curve with η halved (Fig 14 ends at η_B 5.79 on its 4.2 in axes; 21(a) ends at η 2.69 =
    η_B 5.38 by the same half-line-width rule on its 1.74 in panel), so the text's "identical ... except for a
    scale factor of two" holds.
  - (b) reaches u/U = 1 at η = 1.55 (printed about 1.5).
- **Overlay** (`digitize.py overlay`, the drafter's per-panel calibration, residual 0.00 px): (a) 201 points, mean
  0.32 px, 95% 1.00 px, max 1.41 px; (b) 201 points, mean 0.68 px, 95% 2.24 px (0.38 mm), max 2.83 px: both ok.
- **Text** (ch3-sec3b.tex:648-651). On the redraw the example's η_k = 1.20 (2-D) gives u/U = f'(2.4) = 0.73, and
  η_k = 0.96 (3-D) gives f'(3.33) = 0.89. Both lie inside the layer (which reaches U at η 2.7 and 1.55), so
  "well within the boundary layer" stays true.
- **Lettering.**
  - y titles $\eta_{\mathrm{2\text{-}D}}$ and $\eta_{\mathrm{3\text{-}D}}$, upright at mid-height.
  - x titles $u/U$ without ∞, as printed (inventory note).
  - y ticks 0-4 step 1 with a gridline every 0.5; x ticks 0, 0.5, 1.0 with a gridline every 0.1, as printed.
  - The panel letters (a), (b), circled at η = 3 in 1973, are set in the house `panel` style at the upper right
    inside each plot's axes, on one baseline. This is the house rule for panel-identifying letters; the text
    cites "Figures 21a and 21b".
- **Style and size.**
  - One frame for both panels (1.74 x 2.7 in axes, the scan's aspect, the same height as Figs 14, 15, 19
    and 20).
  - Curves in s1; the local `profile` style is under a new name, not a kit redefinition.
  - Page 5.10 x 3.38 in; fonts embedded; the panels are aligned on one baseline.
  - The η_3-D title clears panel (a)'s "1.0" tick label; the letters do not touch the curves.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The panel letters add `fill=white, inner sep=1.5pt, xshift=-1pt, yshift=-1pt` to the kit's `panel` style. The approved panels-in-axes figures (Ch1 Figs 3, 4a; Ch2 Figs 20, 46) use the bare style at `(rel axis cs:1,1)`, but they have no grid. Here the knock-out keeps the 0.9 gridline out of "(a)"/"(b)", which is a sensible local choice. The family has only this one gridded panel figure, so nothing is inconsistent yet. | fig21.tex:20-21, 26-27 | None now. Style suggestion for the kit: a `panel on grid` variant (white knock-out), so later gridded panel charts letter their panels the same way. |
| 2 | note | The cone profile (b) comes from outside the book (Mangler's √3 scaling, owner's pilot-gate decision; overlay passes). | fig21.py docstring | None in the figure (About This Edition is a later step). |

## Verdict: pass

No must-fix and no should-fix.
