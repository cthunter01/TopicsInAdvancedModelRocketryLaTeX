# v2 audit: ch1/fig02 (round 1)

The 1973 Figure 2, shown only in the Errata and Supplement Part beside its 1994 replacement.

Sources checked: figures/ch1/fig02.png (scan, upscaled 2x); figures/v2/ch1/fig02.pdf (rendered 150, 350 and
1200 dpi); figures/v2/ch1/fig02.tex:1-25; figures/v2/inventory.csv row ch1-fig02; 1973 caption
backmatter/supplement/s-ch1.tex:268-283 (figure at :273); text chapters/ch1-sec2a.tex:28-31;
corrections/v2-figures.md; figures/v2/tamrfig.sty (`\plumeshape`, `pic rocket`, `vec`, `thin vec`).

Checked and correct: single upright rocket with a spindle plume as wide as the body; slug $\Delta m_e$ as a grey
(stippled in 1973) band a third of the way down the plume; bold $\vec{F}$ arrow pointing up (+y) between the exit
plane and the slug; bold $\vec{c}$ arrow pointing down (-y) below the slug; axis cross with arrowheads on +y and +x
to the right of the body. All five printed labels present and typeset ($+y$, $+x$, $\vec{F}$, $\Delta m_e$,
$\vec{c}$); the caption's claims ($\Delta m_e$ expelled at $\vec{c}$ in $(-y)$, $\vec{F}$ in $(+y)$) hold. Same
rocket as the 1994 redraw. Moving the $\vec{F}$ and $\vec{c}$ labels from inside the plume to its right is a layout
change, not a loss.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | $\Delta m_e$ (`\footnotesize`, about 15.5pt wide) is wider than the plume at the slug (half-width 0.216-0.221 cm, i.e. about 12.3-12.6pt across between y = -1.2 and -1.8), so the $\Delta$ crosses the left plume outline and the subscript $e$ the right one. In the scan the label sits inside the band. Root cause: the redrawn body is slimmer than the printed one (d/L 0.061 against about 0.08 in the scan), and the plume is as wide as the body. | fig02.tex:7-9 (`\r{0.17}`), 16 | Widen the body and plume toward the printed proportion (e.g. `\r` = 0.22, which gives about 16pt at the slug), or set the label `\scriptsize`. The same fix applies to the 1994 redraw, which shares the rocket. |
| 2 | should-fix | The slug's `wash` fill is drawn after the plume and clipped to the plume path, so it covers the inner half of the plume outline over the slug: the band's sides show as a faint hairline, visibly lighter than the plume outline above and below. | fig02.tex:11-15 (fill at :13 after the pic at :8) | Draw the band before the rocket pic (move lines 11-15 above line 8) or redraw `\plumeshape` over it. |

## Verdict

pass (0 must-fix, 2 should-fix)
