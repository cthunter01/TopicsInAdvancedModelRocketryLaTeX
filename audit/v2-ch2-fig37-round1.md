# v2 audit: ch2/fig37 (round 1)

Sources checked: scan `figures/ch2/fig37.png` (3x upscale; pixel scan of the extension lines and of the joint
lines crossing the body); redraw `figures/v2/ch2/fig37.pdf` (400 dpi render, 2x crop of the C.G./C.G.$_B$
region) and `build/v2/png/ch2-fig37-compare.png`; build log `build/v2/ch2/fig37.log` (no warnings);
`pdfinfo`/`pdffonts` (334.4 x 170.2 pt = 4.64 in wide, all fonts embedded); source `figures/v2/ch2/fig37.tex`
lines 1-38; inventory row `ch2-fig37`; `chapters/ch2-sec4.tex`:478-484 (citing text), :512-521 (caption),
:523-546 (eqs. (93), (94)); `corrections/v2-figures.md` (standing rule 2); STYLE.md sections 13 and 16; the
approved `figures/v2/ch2/fig39.tex`.

Checks made:
- **Outline and scale.** The stations, fins, centre line and unit are identical to the approved Fig 39.
- **Point stations** (1973 Fig 37 measured from the nose tip and mapped station by station onto the Fig 39
  outline; the 1973 joints are at 55 / 110 / 147 / 295 / 332 and the tail at 482 scan px), against the redraw:
  - C.G.$_n$ 40.3 / 40;
  - C.G.$_S$ 131.7 / 131;
  - C.G. 281.2 / 283;
  - C.G.$_B$ 303.2 / 304;
  - C.G.$_T$ 420.2 / 420.
  - The overall C.G. is just forward of the main-tube/boattail joint and C.G.$_B$ is on the boattail, as
    printed.
  - The overall C.G. agrees with Figs 38 and 39 (283).
- **Caption.** The two constant-diameter tubes forward of the boattail are drawn with no C.G. of their own. The
  tail section (tube, engine, fins) has the single mark C.G.$_T$. Both points of the caption hold.
- **Datum and sense.** The datum rises from the nose tip, with $W = 0$ above it. The arrow is marked $+W$ and
  points aft. This matches ch2-sec4.tex:479-484 (moments about the nose tip, coordinate renamed from $Z$ to
  $W$).
- **Dimension lines.** They are stacked longest on top ($\bar W_T$, $\bar W_B$, $\bar W$, $\bar W_S$,
  $\bar W_n$), as printed. Each ends on the extension line of its own mark.
- **Lettering.**
  - All 12 labels are present: $W = 0$, $+W$, $\bar W_T$, $\bar W_B$, $\bar W$, $\bar W_S$, $\bar W_n$,
    C.G.$_n$, C.G.$_S$, C.G., C.G.$_B$, C.G.$_T$.
  - The printed capitals S, B, T and lowercase n are kept. On the scan the n is clearly lowercase and S, B, T
    are cap height.
- **Marks.** All five points use the quartered `cg mark`, as printed.
- **Legibility.**
  - Nothing is clipped and no label meets a line.
  - The C.G.$_T$ label clears the fin tip.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The figure keeps its printed subscripts $\bar W_S$, $\bar W_B$, $\bar W_T$ (C.G.$_S$, C.G.$_B$, C.G.$_T$). Eq. (94) has $\bar W_s$, $\bar W_b$, and $\bar W_t$ for the *body tube*. The figure's T is the whole tail unit (caption), so it is not eq. (94)'s $t$. This is a rule-2 case (lettering kept), but rule 2's list in `corrections/v2-figures.md` does not name Fig 37. | fig37.tex:22, 30-35 | For the lead: add Fig 37 to the standing rule 2 list. No change to the figure. |
| 2 | note | The C.G.$_T$ leader runs at 45 degrees, (420,0) to (486,-66). The other leaders in the family run at about 61 degrees (36 across per 66 down). The shallower slope moves the label clear of the lower fin tip; the leader crosses the lower fin and leaves it through the trailing edge at y = -56, as the 1973 leader and Fig 39's C.P.$_{T(B)}$ leader do. | fig37.tex:35 | none (acceptable as is) |
| 3 | note | The overall C.G. mark (283, radius about 4.6 units) comes within about 0.1 mm of the main-tube/boattail joint line at 289. It stays legible at 400 dpi. The same spacing is in the approved Fig 39 and in Fig 38; the 1973 drawing leaves a visible gap. | fig37.tex:29 | Optional, family-wide only (Figs 37, 38, 39 together): a C.G. at about 280 would clear the joint. Do not change Fig 37 alone. |

## Verdict: pass (0 must-fix, 0 should-fix)
