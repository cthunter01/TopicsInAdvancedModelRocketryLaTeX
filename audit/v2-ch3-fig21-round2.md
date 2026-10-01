# v2 audit: ch3/fig21 (round 2)

Sources checked: scan `figures/ch3/fig21.png`; redraw `figures/v2/ch3/fig21.pdf` (300 dpi render, 600 dpi crop
of both panel letters, `pdftotext -bbox`, `pdffonts`, `pdfinfo`); sources `figures/v2/ch3/fig21.tex`,
`fig21.py`, `fig21-a.csv`, `fig21-b.csv`, `fig21.calib.json` (and `fig14.py`); inventory row `ch3-fig21`
(`figures/v2/inventory.csv`:87); `chapters/ch3-sec3b.tex`:640-677 (citing text, caption, eqs. (94)-(96));
`corrections/v2-figures.md` (pilot gate: Mangler for 21(b)); `STYLE.md` section 16; the panel letters of the
approved Ch1 Figs 3, 4a, 5 and Ch2 Fig 20, and of Ch3 Fig 26 (another family); the round-1 audit and fix
records.

Checks made:
- **Round-1 items.** There were none needing action. Note 1 (the local white knock-out on the panel letters)
  was kept, and the kit suggestion "panel on grid" was passed on in style_suggestions. That handling is correct.
- **Regression.**
  - `fig21.tex` and `fig21.py` are unchanged since round 1.
  - The current source compiles cleanly in my scratch directory. Its 300 dpi render is pixel-identical to the
    PDF in the tree and to the round-1 auditor's render.
- **Data.**
  - I re-ran `fig21.py` in a scratch copy. Both CSVs are byte-identical.
  - Against my own ODE solution, (a) f'(2η) agrees to 1.4e-5 and (b) f'(2√3 η) to 1.7e-5.
  - The curves end at η = 2.692 and 1.554 (u/U = 0.996, half a line width from the border).
- **Text** (ch3-sec3b.tex:648-651, 675-677).
  - η_k = 1.20 (2-D) gives u/U = 0.73, and η_k = 0.96 (3-D) gives 0.89. The u = 0.99U edges are at η 2.5 and
    1.44, so "well within the boundary layer" holds.
  - (a) is Fig 14's curve with η halved, as the text says.
- **Overlays** (`digitize.py overlay`, per-panel calibration, residual 0.00 px): (a) mean 0.32 px, 95% 1.00 px,
  max 1.41 px; (b) mean 0.68 px, 95% 2.24 px (0.38 mm), max 2.83 px: both ok.
- **Lettering.**
  - η_{2-D} and η_{3-D} upright.
  - u/U without ∞, as printed.
  - y ticks 0-4 (minor grid 0.5); x ticks 0, 0.5, 1.0 (minor grid 0.1).
  - Panel letters (a), (b) at the upper right inside the axes.
- **Baseline.** The letters' baselines differ by 0.24 pt, because the node anchor is north and "b" is taller
  than "(". The approved Ch2 Fig 20 and Ch1 Fig 4a show the same 0.24 pt, so this is house behaviour and
  invisible at final size.
- **Size.** Page 5.10 x 3.38 in; fonts embedded. Panel (b)'s η_{3-D} title clears (a)'s "1.0" by about 0.37 in.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Ch3 Fig 26 (another family) now hand-rolls the same knock-out on panel letters in gridded axes (`fill=white, inner sep=1.5pt`), but at `(rel axis cs:0.985,0.975)` and `(0.985,0.96)`. Fig 21 uses `(rel axis cs:1,1)` with `xshift=-1pt, yshift=-1pt`. Two figures now need it, so by STYLE §16 ("define a helper once in tamrfig.sty when a second figure needs it") the round-1 kit suggestion is due. Fig 21 is consistent within itself, so the figure needs no change now. | fig21.tex:20-21, 26-27; fig26.tex:22, 28 | Orchestrator: add a kit `panel on grid` style (panel + fill=white, inner sep=1.5pt, a fixed inset from the axes corner), and switch Figs 21 and 26 to it in one pass. |
| 2 | note | No other round-1 items. Curves, overlays and lettering are re-verified and unchanged. | fig21.* | None. |

## Verdict: pass

No must-fix and no should-fix.
