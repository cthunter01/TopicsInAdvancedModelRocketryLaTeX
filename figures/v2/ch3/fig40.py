#!/usr/bin/env python3
"""Chapter 3, Figure 40: the fin-body interference factors K_F(B) and K_B(F) against d/b.

The book prints no formula (ch3-sec5b.tex defines both factors in words and reads them off this figure, which is
after the USAF Stability and Control Datcom). The Datcom's curves are the slender-body results of Pitts, Nielsen
and Kaattari (NACA Report 1307, 1957), which the owner decided to compute (corrections/v2-figures.md, pilot gate).
With tau = d/b (body radius over the semispan of the fin-body combination, a/s = d/b):

  K_F(B) = (2/pi) [ (1 + tau^4) ( (1/2) arctan( (1/2)(1/tau - tau) ) + pi/4 )
                    - tau^2 ( (1/tau - tau) + 2 arctan tau ) ] / (1 - tau)^2      (NACA 1307, K_W(B))
  K_B(F) = (1 + tau)^2 - K_F(B)                                                    (NACA 1307, K_B(W))

the second because slender-body theory gives the whole combination (1 + tau)^2 times the lift of the fins alone
(the exposed panels joined). Ends: K_F(B) = 1, K_B(F) = 0 at tau = 0; both 2 at tau = 1 (the 0/0 limit). At the
trial rocket's d/b = .289 they give K_F(B) = 1.242 and K_B(F) = 0.419 (the text reads 1.25 and 0.44 off the 1973
art). Checked against the scan with tools/v2/digitize.py overlay (fig40.calib.json). Writes fig40.csv (tau, KFB, KBF).
"""
import math
import pathlib


def k_fb(t):
    if t <= 0.0:
        return 1.0
    if t >= 1.0:
        return 2.0
    a = (1.0 + t ** 4) * (0.5 * math.atan(0.5 * (1.0 / t - t)) + math.pi / 4.0)
    b = t ** 2 * ((1.0 / t - t) + 2.0 * math.atan(t))
    return (2.0 / math.pi) * (a - b) / (1.0 - t) ** 2


out = pathlib.Path(__file__).with_suffix(".csv")
rows = ["tau,KFB,KBF"]
for i in range(0, 201):
    t = i / 200.0
    kf = k_fb(t)
    rows.append(f"{t:.3f},{kf:.5f},{(1.0 + t) ** 2 - kf:.5f}")
out.write_text("\n".join(rows) + "\n")
print(f"{out.name}: {len(rows) - 1} points; at d/b = .289: K_F(B) = {k_fb(0.289):.3f}, "
      f"K_B(F) = {(1.289) ** 2 - k_fb(0.289):.3f}; at 0.5: {k_fb(0.5):.3f}, {2.25 - k_fb(0.5):.3f}")
