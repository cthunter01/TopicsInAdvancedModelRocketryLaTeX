# v2 audit: ch2/fig41 (round 1)

Sources checked: scan `figures/ch2/fig41.png` (3x upscale; 8x crop of the nose, shoulder and payload; 6x crop of
the casing, fins, $R_o$/$R_i$ and $L_{ch}$, both with pixel rulers); redraw `figures/v2/ch2/fig41.pdf` (400 dpi
render; 1.5x crops of the left and right ends; 4x crop of the phantom, centre-line and hidden patterns) and
`build/v2/png/ch2-fig41-compare.png`; build log `build/v2/ch2/fig41.log` (no warnings); `pdfinfo`/`pdffonts`
(364.7 x 138.6 pt = 5.07 in wide, all fonts embedded); source `figures/v2/ch2/fig41.tex`; inventory row
`ch2-fig41`; `chapters/ch2-sec4.tex`:698-768 (eqs. (102), (103a), (103b), the point-mass text, citing sentence and
caption); STYLE.md sections 13 and 16; `corrections/v2-figures.md` (standing rule 2); the approved
`figures/v2/ch2/fig39.tex`.

Checks made:
- **Stations** (scan pixels from the nose tip at scan x = 32, against the redraw):
  - nose base 57 / 59;
  - shoulder end 77 / 77;
  - payload 112-125 / 113-127;
  - complete-rocket C.G. 323 / 324;
  - casing 414-516 / 414-517;
  - fin root leading edge 450 / 451, tip leading edge 489 / 489.5, trailing edge 516 / 517;
  - span 51 / 50;
  - casing radii: scan about 11.5 and 7, redraw $R_o$ = 11, $R_i$ = 7.25.
- **C.G. marks.** C.G.$_{cs}$ (120) and C.G.$_{ch}$ (465.5) are at the midpoints of their cylinders, as eq. (103)
  defines ("location of cylinder's C.G. (midpoint)"). C.G.$_n$ (49.5; scan 49) is inside the nose just ahead of
  its base, as printed.
- **Line styles.** As the family note asks:
  - The body tube and fins are phantom lines (long dash, two short dashes). At 4x they are clearly distinct
    from the dash-dot centre line.
  - The nose, shoulder, payload and casing are solid `outline`.
  - The casing bore is in hidden (dashed) lines.
- **Dimensions.**
  - $\bar W_n$, $\bar W_{cs}$, $\bar W$ and $\bar W_{ch}$ all run from the nose-tip datum, longest on top, as
    printed.
  - $R$ runs from the centre line to the payload's own surface, with the arrows outside.
  - $L_{cs}$ has its arrows outside and its label to the left, as printed.
  - $R_o$ and $R_i$ run from the centre line to the casing's outer wall and bore, arrows outside, labels
    rotated.
  - $L_{ch}$ spans the casing. Its aft extension starts below the phantom fin tip (-66 < -63.25).
- **Lettering.** All 15 inventory items are present. The cs/ch subscripts, $L_{cs}$, $L_{ch}$ and $R_i$ are kept
  as printed (rule 2; eq. (103) has $\bar W_c$ and $L$, and the prose's "$R_1$" is a 1973 slip the figure does
  not share). The subscripts are italic (STYLE.md 13).
- **Caption.** The point-mass nosecone, the solid-cylinder NAR payload and the hollow-cylinder engine casing are
  all shown and named.
- **Legibility.**
  - Nothing is clipped. Width is within 6.5 in.
  - The C.G.$_{cs}$ leader crosses the top of the right $L_{cs}$ extension line at about (127, -15.6), as it
    does in 1973. It passes 7 units clear of the $L_{cs}$ arrow tail.
  - The $R$ arrowhead overlaps the phantom tube line 2.25 units above its tip. In the 400 dpi crop it still
    lands clearly on the payload's top.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The shoulder and payload are drawn at radius 11, inside the phantom tube (13.25). In 1973 they nearly coincide with the tube lines. The redraw is physically consistent (they fit inside the tube), and $R$ measures the payload's own radius, which eq. (103a) needs. | fig41.tex:31-34 | None. |
| 2 | note | `phantom`, `hidden`, `dim arrow` and `\dimoutv` are local helpers. Fig 42 defines `hidden` and `dim arrow` identically. | fig41.tex:12-18 | Style suggestion: add `phantom`, `hidden` and an outside-arrow dimension helper to `tamrfig.sty`, since Ch2 Figs 41-42 (and likely later notation figures) share them. |

## Verdict: pass

No must-fix or should-fix items. Stations, dimensions, line styles and lettering match the scan, the inventory,
eqs. (102)-(103) and the caption.
