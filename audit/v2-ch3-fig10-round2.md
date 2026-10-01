# v2 audit: ch3/fig10 (round 2)

Sources checked: figures/v2/ch3/fig10.tex, fig10.py, fig10-profile.csv, fig10-arrows.csv, fig10.calib.json and
the PDF (rebuilt with `make fig F=ch3/fig10`: 4.39 x 3.11 in, fonts embedded; rendered at 300 and 600 dpi, with
the nose, tail and lower profile zoomed); build/v2/png/ch3-fig10-compare.png beside the scan figures/ch3/fig10.png;
inventory row ch3-fig10; caption and citing text chapters/ch3-sec2b.tex:55-81; Table 1 (chapters/ch3-sec3a.tex);
STYLE.md sections 14 and 16; the round-1 audit and the drafter's fix record. I ran the overlay myself (the lower
profile is mirrored through process substitution).

Round-1 findings:
- Note 1 (axis dash-dot past the nose and tail): taken. The figure now has `centerline=false`, a dash-dot centre
  line from 0.1 to 6.3, and thin solid extensions from -0.51 to 0 and from 6.4 to 6.91 (fig10.tex:92-94). At
  600 dpi the front extension ends exactly on the nose tip and the rear one starts on the base line. This matches
  Figs 1 and 12, Ch1 Figs 6-8 and the 1973 art. The size is unchanged. Resolved, with no regression.
- Note 2 (helpers duplicated in Fig 13): reported in style_suggestions. Resolved.
- Note 3 (exaggeration differs from Fig 12): carried into doubts. Resolved.

Checks:
- Lettering complete and as printed: $V$ in the gap of the dimension on the top row; "Boundary layer" and "Free
  stream" with braces. The Free-stream brace runs on into an arrowhead below the last row.
- Computed profile (Blasius, $u = V f'(5y'/\delta)$, $\delta = 0.65$): spot checks against Table 1 give
  0.6279 / 1.1001 / 1.1591 at y' = 0.219, 0.507, 0.795 (linear interpolation, as an independent check). The CSV has
  0.6283 / 1.1005 / 1.1591 (Hermite), and the lower rows are the same values mirrored.
- Overlay: upper 95% 2.00 px, max 2.24 px; lower 95% 2.00 px, max 3.00 px. Both ok.
- Arrow rows: seven plus the $V$ row above, and eight below. The dashed edge (`guide`) is at $\delta$ below the
  body, as printed.
- Legibility: arrowheads are visible, nothing is clipped, and the width is within 6.5 in.

## Findings
| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | All round-1 notes are resolved. The axis now matches Figs 1 and 12, and the render shows no regression. | fig10.tex:92-94 | None. |

## Verdict: pass (no must-fix)
