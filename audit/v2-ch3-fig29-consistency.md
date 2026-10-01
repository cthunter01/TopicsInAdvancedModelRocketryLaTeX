# v2 consistency check: ch3/fig29

Issue 1 (break symbol): Fig 29 was the only figure that kept the 1973 round-bar break (a hatched lobe and an open
lobe) at the top of its seven bodies. The house rule is that a broken-off tube takes `\breakline`, as in Figs 27,
33, 39, 44 and 49 and Ch2 Fig 36.

Issue 2 (velocity-arrow weight) does not apply. Fig 29's $U$ was already `vec`, and it still is (fig29.tex:53).

Sources checked:
- figures/v2/ch3/fig29.tex:1-60 and figures/v2/ch3/fig29.pdf. The PDF is newer than the .tex (23:12:49 against
  23:12:48). It measures 356.875 x 156.211 pt = 4.96 x 2.17 in, the same as round 1, and all fonts are embedded.
  I rendered it at 300 dpi, and the tube tops at 1200 dpi.
- The scan figures/ch3/fig29.png.
- The round-1 audit, and inventory row ch3-fig29 (figures/v2/inventory.csv:95).
- `\breakline` and `break amplitude` in tamrfig.sty:120-121 and 156-162, and STYLE.md s.16 (line 403).
- The breaks in fig49.tex:20 and 38 (rendered at 300 dpi), fig27.tex:30, fig33.tex:42-43 and fig39.tex:91.
- The fixer's 300 dpi before and after renders (scratch u07-base-drag/polish/), compared pixel by pixel with my
  render.

## Checks

- **The issue is resolved.**
  - `\body` (fig29.tex:23-26) now draws three things:
    - the centre line, from y = 12 to 205;
    - the open outline, from (x+R, yc) down round the nose and back up to (x-R, yc);
    - `\breakline[break amplitude=0.5]{(x-R,yc)}{(x+R,yc)}` across the tube end.

    The hatched ellipse, the lobe arc and the lobe half-height `\e` are gone. No local style or macro is defined.
  - The 300 and 1200 dpi renders show the same zigzag on all seven bodies, with clean round-capped corners where
    it meets the walls.
  - The zigzag has the same form and sense as Fig 49's tube top: a small rise, a deep notch, a tall peak, a
    small notch, then flat to the right wall.
  - Peak height:
    - Fig 29: 0.5 x 0.5 x 38 units x 0.02286 cm = 0.217 cm. On the 1200 dpi render I measure 103 px, which is
      0.218 cm.
    - Fig 49: 0.5 x 0.36 x 1.93 x 0.65 cm = 0.226 cm.

    So the two breaks have the same absolute size, as the fixer reports.
  - The centre lines run through the break and on past the tube end (yc = 41 to y = 12), as the suggestion asked
    and as the scan shows.
- **Nothing else changed.**
  - The fixer's after-render matches my render exactly (0 differing pixels).
  - Against the before-render, the differences are at the tops: rows 52-111 at 300 dpi, which is the break band.
  - The only other differences are on bodies 6 and 7, along their side walls and flat faces. They are 1-px
    anti-aliasing shifts (a 2.5-px line rendered as 3 px), with no change of position.
  - The geometry in the .tex is as round 1 describes:
    - R = 19, with the seven centres 88-534.4;
    - the half ellipsoid is 30 long;
    - the hemisphere;
    - corner radius 3.8;
    - cones of 22 and 39 deg, with joint lines;
    - the flat face;
    - the hidden cavity (±13.3, depth 38);
    - `vec` $U$ pointing up.
- **Against the scan, everything else is as before.**
  - The value row reads $\CDo =$ $-.05$, $+.01$, .20, .20, .34, .90 and 1.0, on one baseline.
  - $U$ is under its arrow.
  - The order is #1-#7.
  - The break symbol is now the house zigzag rather than the scan's round-bar break, by design (house rule).
- **Header.** fig29.tex:2-4 records the substitution ("the house break line for a cut-off tube, \breakline, as
  Figs 27, 33, 49; the 1973 art shows the round-bar break, a hatched lobe and an open lobe").

## Findings

| # | severity | finding | where | suggested fix |
|---|---|---|---|---|
| 1 | note | The inventory notes still describe the 1973 break ("broken off at the top (hatched elliptical cut section)"). I found no entry in corrections/v2-figures.md recording the round-bar to `\breakline` substitution for any Chapter 3 figure: a grep for "break", "zigzag" and "lobe" finds nothing. So the fixer's "as was done for Fig 33" refers to fig33.tex's header comment, not to the corrections file. | inventory.csv:95; corrections/v2-figures.md | Orchestrator: one line in corrections/v2-figures.md covering Figs 27, 29, 33 and 49 (the 1973 round-bar break redrawn as `\breakline`). |
| 2 | note | The break amplitude varies across Chapter 3: 0.32 (Fig 33), 0.36 (Figs 44, 49), 0.4 (Fig 27), 0.5 (Fig 29) and 0.6 (Fig 39). Fig 29's is chosen so that its absolute peak height matches Fig 49's, which reads uniformly. | fig29.tex:26 | None for this figure; see the fixer's style suggestion. |
| 3 | note | Round 1's optional note stands. The cavity is 0.70 d wide; the scan's is about 0.76 d. The fix did not touch it, and it is not a regression. | fig29.tex:51 | Optional, as before. |

## Verdict: pass (issue 1 resolved; issue 2 not applicable; no regression)
