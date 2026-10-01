# v2 audit: ch4/fig01 (round 1)

Sources checked:
- Scan `figures/ch4/fig01.png`, with 2x and 3x crops of panel (a) and of the lower half of panel (b).
- Redraw `figures/v2/ch4/fig01.pdf` (rebuilt with `make fig F=ch4/fig01`; clean log, 3.40 x 5.88 in): 300 and
  600 dpi renders, a 1600 dpi crop of the dm_e slice and of the C.G. triangle, and `build/v2/png/ch4-fig01-compare.png`.
  I also checked `pdffonts` (all embedded) and looked for opacity operators (none).
- Source `fig01.tex`.
- Inventory row `ch4-fig01`.
- Text: caption and citing text in `chapters/ch4-intro-sec1.tex`:97-153 (Figure 1a, Figure 1b, eqs. (1)-(4)).
- STYLE.md sections 15 and 16; `corrections/v2-figures.md`. The Chapter 3 "Vector lettering" entry is settled:
  Ch4 Fig 1 sets `\vec`.

Checks made:
- **Lettering.** Everything the scan and the inventory list is present:
  - (a): Time = $t$; Rocket mass = $m(t)$; Rocket velocity = $\vec v$; Rocket momentum = $\vec p$; $\vec v$; $\vec E$;
    (a).
  - (b): Time = $t + dt$; Rocket mass = $m(t) - dm_e$; Rocket velocity = $\vec v + d\vec v$; Rocket momentum =
    $\vec p + d\vec p$; $d\vec v$; $\vec v + d\vec v$; $\vec v$ (at the C.G.); $\vec E$; $\vec c + \vec v$; $\vec c$;
    $\vec v$ (at the nozzle); $dm_e$ (on a leader to the slice); (b).
  - The state lists keep the two lettered columns. Vectors use `\vec`, as settled. $dm_e$ has an italic e (STYLE
    s15).
- **Geometry.**
  - The axis is at 60 deg, which I measured as 61 deg on the scan. $\vec E$ comes in at 30 deg below the horizontal
    (scan about 29 deg). The C.G. is at 0.72 L, which I measured as 154/215 px = 0.72 on the scan.
  - At the C.G.: $\vec v$ + $d\vec v$ = $\vec v + d\vec v$, head to tail.
  - At the slice: $\vec c$ runs backwards along the axis, then $\vec v$ (the same length and direction as at the
    C.G.), so $\vec c + \vec v$ closes the triangle. That is eq. (4)'s exhaust velocity relative to the ground, as the
    text says (:150-152).
  - $\vec E$ and $\vec v$ are identical in (a) and (b). Both panels use one rocket placement (the `\rocket` macro).
- **Caption and text.** The engine is thrusting (plume in both panels). (a) is at $t$ and (b) at $t + dt$. The
  velocity has changed by $d\vec v$, and the mass $dm_e$ has been expelled from the nozzle (:120-125). All of this
  holds, except that the expelled mass does not read clearly as a hatched slice (finding 1).
- **House style.**
  - `vec` vectors and a `cg mark`, as in Ch1 Figs 6-8.
  - The `panel` letters (a), (b) are at the lower right of each panel.
  - The callout is the kit `\callout`: a straight leader with a horizontal shoulder.
  - The centre line is `centerline`. Text is in ink. Nothing is filled or transparent, and no kit name is redefined.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | must-fix | The expelled mass $dm_e$ does not read as a hatched slice at final size. The slice is filled with `hatch` (45 deg), which runs only 15 deg off the 60 deg rocket axis. At the 3pt spacing, only two ink2 hairlines fall inside the 3.6 x 2.4 mm slice, and they lie almost parallel to the plume outlines (1600 dpi crop). In the 150 dpi compare, the slice is a faint empty band between the tail line and the aft-face line. The 1973 slice is dark and cross-hatched, and the $dm_e$ leader, the inventory ("hatched propellant slice") and the text (:122-123) all point at it. | `fig01.tex`:54 | Use `\fill[hatch back]` (the kit's 135 deg hatch, 75 deg across the axis). A scratch build puts four lines across the slice, and it reads clearly at 150 dpi. Optionally set `\slab` to 0.8 (line 51). S and the leader follow `\slab`, so nothing else moves by hand. |
| 2 | note | The lower triangle's corner (ct) collects four ends at one point: the head of $\vec c$, the plume tip, the end of the centre line and the tail of the lower $\vec v$. It is still legible at 300 dpi. | `fig01.tex`:68-72 | None needed. If wanted, set `\cl` to 4.0 so the head lands exactly on the plume tip. |
| 3 | note | The C.G. fraction differs from Fig 15: Fig 1 uses 0.72 L and Fig 15 uses 0.62 L. Each follows its own 1973 drawing (Fig 1 scan 0.72; Fig 15 scan about 0.57). The book gives no value. | `fig01.tex`:24 | None. |
| 4 | note | Departures from the 1973 drawing are recorded in the file header, not in `corrections/v2-figures.md`: vectors longer against the rocket, the $\vec v + d\vec v$ label beside its head, $\vec E$ into the C.G. (1973 just below it), $\vec c + \vec v$ at 19 deg (1973 about 35 deg). | `fig01.tex`:1-17 | Orchestrator: optionally add a Chapter 4 Minor line. |

## Verdict: fix

One must-fix (finding 1): a one-word change of the hatch style. Everything else (lettering, vector geometry, caption
and text claims, house style) is correct.
