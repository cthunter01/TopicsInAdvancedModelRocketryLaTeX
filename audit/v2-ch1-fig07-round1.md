# v2 audit: ch1/fig07 (round 1)

Sources checked: figures/ch1/fig07.png (scan, upscaled 2x); figures/v2/ch1/fig07.pdf (rendered 350 and 1200 dpi);
figures/v2/ch1/fig07.tex:1-26; figures/v2/inventory.csv row ch1-fig07; caption chapters/ch1-sec2b.tex:259-268;
text ch1-sec2b.tex:253-257 and backmatter/supplement/s-ch1.tex:302-305 (page-40 correction); ch1-sec2b.tex:270-276
(eqs. (21), (22), $S \equiv N\cos\alpha$); corrections/v2-figures.md; figures/v2/tamrfig.sty (`cg mark`,
`cp mark`, `vec`, `centerline`).

Geometry verified from the source (axis 27 deg, $\alpha$ = 33 deg, N = 2.4):
- $\vec{V}$ from the C.G. (0.62L) at 60 deg.
- $\vec{N}$ from the C.P. (0.75L, aft of the C.G.) at -63 deg: perpendicular to the axis.
- $\vec{S}$ from the C.P. at -30 deg, length N cos 33 deg = 2.013: perpendicular to $\vec{V}$.
- $\vec{D}_1$ from the tip of $\vec{S}$ to the tip of $\vec{N}$: N(cos -63, sin -63) - 2.013(cos -30, sin -30)
  = 1.307 along 240 deg = N sin 33 deg, antiparallel to $\vec{V}$ (parallel, pointing back: drag).
- $\vec{N} = \vec{S} + \vec{D}_1$ exactly; the $\alpha$ arc (radius 1.0 about the C.P.) spans $\vec{N}$ to
  $\vec{S}$, which is $\alpha$ because $\vec{N} \perp$ axis and $\vec{S} \perp \vec{V}$.

All the caption's claims hold (forces through the C.P.; $\vec{N} \perp$ axis; $\vec{S} \perp \vec{V}$;
$\vec{D}_1 \parallel \vec{V}$; no wind). All printed labels present and typeset: $\vec{V}$, $\vec{N}$,
$\vec{S} = \vec{N}\cos\alpha$, $\vec{D}_1 = \vec{N}\sin\alpha$ (numeral 1), $\alpha$. C.G. quartered circle and
C.P. circle-with-dot as the house style specifies. Same rocket, attitude and stations as Figs 6 and 8. No label
touches a line (the $\vec{S}$ label clears the $\vec{S}$ shaft by about 1.6 mm and the body by more).

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The thin solid axis line runs the full length, from 7.3 behind the nose to 0.9 ahead of it, underneath the dash-dot centre line, so inside the body the dash gaps are filled and the centre line reads as solid. The scan has dash-dot inside the body and the thin solid line only beyond the nose tip and the tail. | fig07.tex:9, 11 | Draw the solid axis only outside the body: `\draw[thin line] (0,0) -- (27:0.9); \draw[thin line] (207:6.4) -- (207:7.3);`. |
| 2 | note | The heads of $\vec{N}$ and $\vec{D}_1$ meet at the same point (the tip of $\vec{N}$), as printed; both heads remain distinct. | fig07.tex:18, 20 | None. |

## Verdict

pass (0 must-fix, 1 should-fix)
