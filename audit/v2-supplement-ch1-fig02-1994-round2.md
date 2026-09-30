# v2 audit: supplement/ch1-fig02-1994 (round 2)

The June 1994 Figure 2 in its chapter form (Chapter 1, `ch1:fig:2`). The document form has a report of its own.

Sources checked: figures/supplement/ch1-fig02-1994.png (scan); figures/v2/supplement/ch1-fig02-1994.pdf (current,
rendered 150, 300 and 1200 dpi); figures/v2/supplement/ch1-fig02-1994.tex:1-65; audit/v2-supplement-ch1-fig02-1994-round1.md;
inventory row sup-ch1-fig02-1994; chapter caption chapters/ch1-sec2a.tex:48-73; corrections/v2-figures.md ("Ch1
Fig 2 (1994)"); figures/v2/tamrfig.sty (`\plumeshapeb`, `vec`, `thin vec`).

| round-1 # | severity | status | evidence |
|---|---|---|---|
| 1 | should-fix | resolved | The side exit arrows now sit at x = ±0.13 (ch1-fig02-1994.tex:39-40) with 3.5 x 2.4pt heads. The centre arrow (:41) is 1.1pt with a 4.5 x 3.4pt head. The side heads start 0.088 cm from the axis and the centre head ends at 0.060 cm, a gap of about 0.8pt. At 1200 dpi they read as three distinct arrows (thin, bold, thin), as in the 1994 art. |
| 2 | should-fix | resolved | The stations are computed per index (ch1-fig02-1994.tex:31-32: `\i` = 0..15; d = 0.3-1.2 step 0.3, then 1.55 + 0.35(i-4)), so the last pair is at d = 5.40, 0.2 cm above the fin trailing edge (5.6). At 1200 dpi the arrows continue across the fin root to the tail region, as printed. |
| 3 | should-fix | not resolved (in part) | The label now fits: the plume bulges to 1.8 r (`plume bulge=1.8`, :13; the agreed plume parameter). At 1200 dpi the $\Delta m_e$ ink clears the outlines by 0.7pt (left) and 1.1pt (right). But the node's white box (`fill=white`, :22) is still drawn after the plume outline (:21) and is as wide as the plume interior, so it erases both plume outlines over 8.5pt (3.0 mm) of height at the label: the plume has two open gaps beside $\Delta m_e$. In the 1994 art the outlines run unbroken past the label's white patch (scan, checked at 5x). Fix: draw the node before the outline (swap :21 and :22), or clip the white box to `\plumeshapeb{1.8}{\r}{\P}`. |
| 4 | note | resolved | $\vec{A}_e$ and $P_e$ now clear the wider plume's outlines by several points. |
| 5 | note | accepted: note, no action required | `-\vec{c}\,(dm_e/dt)` still has the thin space (:57); invisible to most readers. |
| 6 | note | accepted: note, no action required | 16 pressure arrows a side (after finding 2) against 14 printed; the count carries no meaning. |

## New findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The bold exit-plane arrow is a local 1.1pt arrow rather than `vec` (1.3pt, 7 x 4.6pt head). That is a reasonable compromise: it is a pressure arrow, and a `vec` head would again merge the three arrows. The force vectors ($\vec{c}$, $\vec{F}$) are `vec`. | ch1-fig02-1994.tex:41 | None. |

Checked again: three identical rockets with plumes as wide as the body at the exit plane (caption NOTE); hatched
slug, $\vec{c}$ down, axis cross on the left; $P_a$, the inward arrows on nose, body and fins, the down arrow on the
nose tip, $\vec{A}_e$ and $P_e$ in the centre; $\vec{F}$ up on the right. The equation row is
$-\vec{c}\,(dm_e/dt) + (P_e - P_a)\vec{A}_e = \vec{F}$, with the arrow over $A_e$ only (the pilot decision).

## Verdict

pass (0 must-fix, 1 should-fix open: round-1 #3, the white box cutting the plume outlines)
