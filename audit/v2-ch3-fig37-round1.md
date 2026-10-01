# v2 audit: ch3/fig37 (round 1)

Sources checked: figures/v2/ch3/fig37.tex and .pdf (built 22:12, after the .tex; log clean; 373.2 x 221.7 pt =
5.18 in wide, fonts embedded), render at 400 dpi and at the scan's 14.74 px/cm (overlay on the scan, stations
aligned on the nose-tip line); figures/ch3/fig37.png (zoomed 4x, including the small mark of (b)); inventory
row ch3-fig37; caption and citing text chapters/ch3-sec5a.tex:46-47, 200-236, 332, ch3-sec5b.tex:38-39, 86-101,
ch4-sec4.tex:451-519 (Table 1); STYLE.md sections 14 and 16; tamrfig.sty (\rocketoutline, \rocketfins, \dimout,
\dimline, edge fin, cg mark, angle arc); approved Ch2 fig48.tex (dimensioned rocket).

Numbers checked against the text: l_b/d = 33/2.06 = 16.0 (sec5a:221); nose-body joint at 8.9 = x_1 (sec5a:224);
x_o = 0.51 x 33 = 16.83 (the text's 16.8, eq. (140)); r = 1.03 (sec5a:234); span b = 2.06 + 2 x 2.54 = 7.14
(sec5a:332, sec5b:38). All lettering present and correct: $x$ (arrow aft from the nose-tip station), "Tangent
ogive" (straight leader), 8.9, 33.0, 2.06, $x_o = .51\ell_b$ (letter-o subscript, script ell, leading-dot
decimal as printed), 2.54 (chord, label outside the stubs), 2.54 (span, reading up its line as printed), $\alpha$,
"Flow / direction", panel letters (a), (b) in the house panel style.

## Findings
| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Geometry is drawn to the lettered dimensions and sits on the scan: in the overlay the nose-body joint, the x_o leader, the fin leading and trailing edges and both ends of 33.0 coincide with the 1973 stations; the fins are drawn to the true 2.54 span (the 1973 fins are about 2.37) and the body to 2.06 (1973 about 1.93-2.04). | fig37.tex:21-50 | none |
| 2 | note | The mark in (b) is the house `cg mark`. Zoomed, the 1973 mark (scan about (270,307)) is a small circle with two opposite quadrants dark, so it is the C.G. symbol; the redraw's quartered mark matches it. Its position (20.3 from the tip, 0.61 l_b) is as drawn: the book gives no C.G. for this rocket (Ch4 Table 1 gives only the 1-calibre margin). Flow line and axis cross at it, as in 1973. | fig37.tex:54-65 | none |
| 3 | note | The flow-direction line has an arrowhead the 1973 line lacks. It shows the same direction and matches Fig 38's flow arrow. | fig37.tex:56-57 | none (already stated in the header comment) |
| 4 | note | alpha = 10 deg (the scan's axis slope measures 9.5 deg); the double-headed `angle arc` sits ahead of the nose between the flow line and the axis, as in Fig 38. | fig37.tex:66-67 | none |
| 5 | note | Panel letter (b) is at x = 35.45 in (a)'s units and (a) is at 38.2, so (b) sits about 9.5 mm left of (a). Each is at the lower right of its own panel, which is the house rule. Fig 39 in this family puts both letters on one right edge. | fig37.tex:47, 68 | optional: `\node[panel, anchor=base east] at (43.7,-6) {(b)};` puts (b) under (a) |

No overlaps or clipping at final size. The stubs and labels of 2.54 / 2.54 at the tail have at least 1.4 mm
clearance. Arrowheads are visible. Line styles follow the kit: `centerline`, `extension`, `dim stub`, `leader`,
`thin vec`, `edge fin`, `outline`.

## Verdict: pass (no must-fix)
