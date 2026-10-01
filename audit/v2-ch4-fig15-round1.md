# v2 audit: ch4/fig15 (round 1)

Sources checked:
- Scan `figures/ch4/fig15.png`, with 4x crops of panels (a) and (b).
- Redraw `figures/v2/ch4/fig15.pdf` (rebuilt with `make fig F=ch4/fig15`, identical render; clean log, 5.05 x
  2.66 in): 300 dpi render, 600 dpi crops of both panels, and `build/v2/png/ch4-fig15-compare.png`. I also checked
  `pdffonts` (all embedded) and looked for opacity operators (none).
- Sources `fig15.tex`, `fig15.py`, `fig15.csv`, `fig15-pos.csv` and `fig15.calib.json`.
- Inventory row `ch4-fig15`.
- Text: `chapters/ch4-sec3.tex`:225-252 (the gravity turn and the caption) and :76-118 (eqs. (106)-(115),
  (125)-(131)).
- STYLE.md sections 15 and 16; standing rule 4 in `corrections/v2-figures.md`.

Checks made:
- **Data reproduce.** I reran `fig15.py`'s `track()` in scratch, writing nothing to the repo. It reproduces
  `fig15.csv` exactly. Scale 16.57 px/m; (b) at (379.19, 269.82) px, θ = 74.003 deg, s = 340.3 px, as in
  `fig15-pos.csv`.
- **Equations.**
  - The rod phase is (125) with (126)-(131); free flight is (106)-(115). dt = 0.001 s.
  - F is a constant 7 N and the mass is held at 0.300 kg, k = 0.0045. These are assumed for the schematic and
    stated in the docstring.
- **Attitudes.** On the scan, (a)'s axis is 60.3 deg above the horizontal and (b)'s 16.4 deg, so θ_o ≈ 30 deg and
  θ ≈ 74 deg, as drawn.
- **Overlay (my run).** I split `fig15.csv` into the drawn pieces (s 80-222 and 472-545) and ran
  `digitize.py overlay` (residual 0.00 px):
  - piece 1: mean 4.75 px, 95% 11.29 px (1.91 mm), max 12.08 px;
  - piece 2: mean 10.42 px, 95% 15.67 px (2.65 mm), max 15.81 px.
  - Both are MISMATCH against the 3 px tolerance. The drafter reports the same numbers. The computed track sits
    below the 1973 freehand arc, and 1973 does not draw its arc through either C.G.
- **Force geometry (rule 4).** I checked each vector against the decomposition.
  - (a), with vectors ending at the C.G.: $g$ (100) from above and $g\sin\theta_o$ (50) at -30 deg. This is the
    true normal component g sinθ (cosθ, -sinθ). The dashed closing line from g's tail to g sinθ_o's tail is
    parallel to the axis (the g cosθ component, 86.6).
  - (b), with vectors starting at the C.G.: $g$ (100) and $g\sin\theta$ (96.1) at -74 deg, 16 deg from g. The
    dashed closure runs along the axis (27.6 = g cos 74 deg).
  - Thrust: $F$ (52) along the axis into the tail. $F\cos\theta$ is drawn vertical from F's tail (45.0 in (a), 14.3
    in (b)), and the dashed horizontal $F\sin\theta$ meets the nozzle. The triangles close.
  - θ_o and θ are marked between the vertical and the flight direction at the C.G., where the text defines them
    (:232-233). In (a) the vertical is g's own line; in (b) it is a `guide`.
- **Caption and text.**
  - The gravity component is perpendicular to the velocity in both panels.
  - $g\sin\theta$ (96) > $g\sin\theta_o$ (50): "an even greater component".
  - $F\cos\theta$ (14) < $F\cos\theta_o$ (45): "even less of its thrust is effective".
  - The flight path curves away from the vertical.
  - All hold.
- **Lettering.** Everything the scan and the inventory list is present:
  - (a): $\theta_o$, $g$, $g\sin\theta_o$, $v$, $F$, $F\cos\theta_o$, (a);
  - (b): $F$, $F\cos\theta$, $g$, $g\sin\theta$, $\theta$, $v$, (b).
  - The o subscripts are the letter o (STYLE s15). No vector arrows, as printed.
- **House style.**
  - `vec` vectors and `cg mark`; `guide` for the construction lines and the reference vertical; the path in s1.
  - The house model rocket with its centre line. `panel` letters at the lower right of each position.
  - Text is in ink. Nothing is filled or transparent, and no kit name is redefined.
  - Drawn at 1.25 times the 1973 size, within the 6.5 in text width.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | θ_o and θ use the `\anglemark` default `angle arc`, which puts a head at both ends. Fig 2 in the same family marks the same angle θ (from the vertical to the flight direction) with `angle arc single`, as 1973 prints it there and as STYLE s16 assigns to an angle measured from a reference line. The two figures should read alike. | `fig15.tex`:67, :83 | Add `arc={angle arc single}` to both `\anglemark` options. The head then lands on the flight direction, and the existing trim already stops it at the body outline. The labels can stay outside the arcs. |
| 2 | should-fix | The overlay mismatch is not logged in `corrections/v2-figures.md`, which STYLE s16 requires for any curve over the 3 px tolerance. The figures are 95% 11.3 px (1.9 mm) and 15.7 px (2.7 mm). The log should also record the assumed parameters: Fig 14 (c)'s model with a constant 7 N "F7" thrust and constant mass, the track scaled to the 334 px chord between the 1973 C.G.s, and (b) at 74 deg. The drafter may not edit that file. | `corrections/v2-figures.md` (Chapter 4 Minor) | Orchestrator adds: "Ch4 Fig 15: the flight path is computed by eqs. (125)-(131), (106)-(115) for Fig 14 (c)'s model with a constant 7 N and constant mass (the book gives no F7 curve), scaled so both C.G.s lie on it with tangent axes; 95% 11.3 px and 15.7 px from the 1973 freehand arc, which passes through neither C.G." Also update the inventory row's method/data: the path is computed. |
| 3 | note | In (b), $F\cos\theta$ = 0.28 F is 14.3 units (3.0 mm at final size), of which the 7pt head is 2.5 mm, so it is nearly all arrowhead. It is still recognisable at 150 dpi with its label beside it, and its smallness is the caption's point. | `fig15.tex`:26 | None needed. If wanted, raise `\F` to about 70 in both panels (F cos θ then 19 units, 4 mm). |
| 4 | note | $F\cos\theta$ starts at F's tail, with the dashed $F\sin\theta$ meeting the nozzle. 1973 brings the vertical component into the nozzle from below instead. Both decompositions are valid, and the header gives the reason: in (b) the 1973 form lands on the lower fin. | `fig15.tex`:17-19, :49-53 | None. |
| 5 | note | At the track's scale (16.6 px/m) each rocket is about 7.3 m long, and the track turns from 30 deg to 51.6 deg over (a)'s forward length. So the first visible piece (s = 80) starts 17 px right of and 7 px below (a)'s nose, heading 22 deg further right than the rocket. The 1973 arc also starts beside (a)'s v rather than in line with it. | `fig15.py` (CHORD_PX, s ranges) | None. |

## Verdict: pass

No must-fix. The forces are now resolved consistently, with θ where the text defines it and every printed label
kept. The caption's comparisons between (a) and (b) hold. Finding 1 is a one-option change for family
consistency with Fig 2. Finding 2 is a log entry outside the figure's files.
