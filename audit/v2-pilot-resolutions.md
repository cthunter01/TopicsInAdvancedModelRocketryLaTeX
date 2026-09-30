# v2 pilot: how the round-2 should-fix items were resolved (2026-09-30)

All 19 pilot figures (Chapter 1, the 1994 Figure 2 in both forms, and the six style samples) passed round 2
with no open must-fix (audit/v2-*-round2.md). The remaining should-fix items:

| figure | round-2 item | resolution |
|---|---|---|
| ch1/fig03 | (a) outside its axes; (b) at the upper right | (a) inside the plot's upper right; (b) at the lower right of the table panel (STYLE.md section 16) |
| ch1/fig04a, fig04b | shoulder at about 11 N on the spike of the 1973 tracing | smoothing raised (b4-1973.py, s = n x 1.0^2); the steep straight fall is the 1973 drawing's own (overlay: 95% of points within 1 px); kept |
| ch1/fig04b | (d) 0.5 in above (c)'s baseline | (d) anchored on (c)'s baseline |
| ch1/fig09 | the fillet's foot 1 mm above the plate | the fillet runs down to the plate |
| ch1/fig10 | plumes as wide as the body | plumes drawn in the figure from a nozzle 0.6 of the body's radius, bulge 1.25 (the house default unchanged) |
| supplement/ch1-fig02-1994 (both forms) | the white box behind Delta m_e cuts the plume outline | the outline is drawn over the box |
| ch2/fig39 | leaders start inside the C.P./C.G. marks | leaders start at the marks' rims (shorten 2.9pt) |

| supplement/ch1-fig02-1994 | (gate) chapter vs document form | one form: the arrow over $A_e$ only, in Chapter 1 and the supplement Part (owner, 2026-09-30); the -document form and its audit are withdrawn |
