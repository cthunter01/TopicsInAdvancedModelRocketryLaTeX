#!/usr/bin/env python3
"""Chapter 2, Figure 26: undamped roll-coupled response to general initial conditions (scan figures/ch2/fig26.png).

The four roll-coupled figures (26-29) use one rocket; this script defines it and the chapter's formulas the others
import (fig27.py, fig28.py, fig29.py).

Units: I_L = C_1 = 1, so time is in units of sqrt(I_L/C_1) and the plots' t axis is unscaled, as printed; angles
are in an arbitrary unit (the printed alpha axes carry no scale), the drawn alpha_Y0 of Figs 26 and 27.
Rocket: I_R omega_Z / I_L = 4/(3 sqrt 5) = 0.596 (then, undamped, the two modes are omega_1 = sqrt(5)/3 and
omega_2 = -3/sqrt(5), in the ratio -5/9, so the motion is periodic, period 5 x 2 pi/omega_1 = 42.2, as the
caption says); C_2/I_L = 0.47 for the damped Figs 27-29. Initial conditions (Figs 26 and 27 alike): alpha_X0 =
0.65, alpha_Y0 = 1, Omega_X0 = Omega_Y0 = 1.55.
These were matched to the scans by one joint fit of the solution to the four 1973 figures' curves (one rocket for
all four, Figs 26 and 27 also sharing their initial conditions, as their alpha_X0 and alpha_Y0 ticks are drawn at
the same heights); the 1973 time windows are 12.5-12.9 units long. Overlay on the scans (calibration
fig26.calib.json ... fig29.calib.json): 95% of the points within 3.2 and 4.5 px (Fig 26, upper and lower), 2.2 and
1.4 (Fig 27), 1.0 and 3.0 (Fig 28), 2.2 and 1.4 px (Fig 29). The straight lines are the true tangents at t = 0
(standing rule 4): they lie on the 1973 slope lines in Figs 27 and 29; Fig 26's are drawn steeper.

Equations: omega_1, omega_2 by eqs. (55), (56a), (56b); D_1, D_2 by (57a), (57b) (both zero here: C_2 = 0);
A_1 sin(phi_1), A_1 cos(phi_1) by the displays before (58a), phi_1 by (58a), phi_2 by (58b), A_1, A_2 by (59a),
(59b); the motion by (60a), (60b) (eq. (51) with D_1 = D_2 = 0). Checked against a direct integration of the
coupled pitch-yaw equations (chapters/ch2-sec3c.tex:11-16).
Writes fig26.csv: t, aX (alpha_X), aY (alpha_Y); fig26-marks.csv: the initial conditions and the curves' extent, for
the tick labels and the tangent lines (the other figures' scripts write the same pair of files).
"""
import pathlib
import numpy as np
from scipy.integrate import solve_ivp

# ---- the rocket of Figs 26-29 (I_L = C_1 = 1) ----------------------------------------------------------------
IL, C1 = 1.0, 1.0
IR_WZ = 4 / (3 * np.sqrt(5))           # I_R omega_Z
C2_DAMPED = 0.47                       # C_2 of Figs 27-29
AX0, AY0, OX0, OY0 = 0.65, 1.0, 1.55, 1.55   # initial conditions of Figs 26 and 27


def modes(C2, IL=IL, IR_wZ=IR_WZ, C1=C1):
    """omega_1, omega_2, D_1, D_2 by eqs. (55)-(57)."""
    F = IR_wZ**2 / (4 * IL**2) + C1 / IL - C2**2 / (4 * IL**2)                          # (55)
    root = np.sqrt(F / 2 + 0.5 * np.sqrt(F**2 + C2**2 * IR_wZ**2 / (4 * IL**4)))
    w1 = -IR_wZ / (2 * IL) + root                                                         # (56a)
    w2 = -IR_wZ / (2 * IL) - root                                                         # (56b)
    D1 = C2 / (2 * IL) * (w1 / (w1 + IR_wZ / (2 * IL)))                                   # (57a)
    D2 = C2 / (2 * IL) * (w2 / (w2 + IR_wZ / (2 * IL)))                                   # (57b)
    return w1, w2, D1, D2


def denominator(w1, w2, D1, D2):
    """The common denominator 2(D_1 D_2 + omega_1 omega_2) - D_1^2 - D_2^2 - omega_1^2 - omega_2^2."""
    return 2 * (D1 * D2 + w1 * w2) - D1**2 - D2**2 - w1**2 - w2**2


def general(w1, w2, D1, D2, aX0, aY0, OX0, OY0):
    """A_1, A_2, phi_1, phi_2 for general initial conditions, eqs. (58), (59)."""
    den = denominator(w1, w2, D1, D2)
    s1 = (OX0 * (D1 - D2) + OY0 * (w1 - w2) + aX0 * (D1 * D2 + w1 * w2 - D2**2 - w2**2)
          + aY0 * (w1 * D2 - w2 * D1)) / den                                              # A_1 sin phi_1
    c1 = (OX0 * (w2 - w1) + OY0 * (D1 - D2) + aX0 * (w2 * D1 - w1 * D2)
          + aY0 * (w1 * w2 + D1 * D2 - w2**2 - D2**2)) / den                              # A_1 cos phi_1
    p1 = np.arctan(s1 / c1)                                                               # (58a)
    p2 = np.arctan((aX0 - s1) / (aY0 - c1))                                               # (58b)
    A1 = s1 / np.sin(p1)                                                                  # (59a)
    A2 = (aX0 - s1) / np.sin(p2)                                                          # (59b)
    return A1, A2, p1, p2


def motion(t, w1, w2, D1, D2, A1, A2, p1, p2):
    """alpha_X, alpha_Y by eq. (51) (eq. (60) when D_1 = D_2 = 0)."""
    aX = A1 * np.exp(-D1 * t) * np.sin(w1 * t + p1) + A2 * np.exp(-D2 * t) * np.sin(w2 * t + p2)
    aY = A1 * np.exp(-D1 * t) * np.cos(w1 * t + p1) + A2 * np.exp(-D2 * t) * np.cos(w2 * t + p2)
    return aX, aY


def integrate(t, C2, y0, Ms=0.0):
    """Direct integration of the coupled equations (yaw step Ms), for the check."""
    def f(_, y):
        aX, aY, OX, OY = y
        return [OX, OY, (Ms - C2 * OX - C1 * aX - IR_WZ * OY) / IL, (-C2 * OY - C1 * aY + IR_WZ * OX) / IL]
    s = solve_ivp(f, (t[0], t[-1]), y0, t_eval=t, rtol=1e-11, atol=1e-12)
    return s.y[0], s.y[1]


def write(path, t, aX, aY, check, **marks):
    """figNN.csv (the curves, checked against the integration) and figNN-marks.csv (marks = the constants the
    figure letters or draws: initial values, slopes, M_s/C_1, and tend, the curves' extent)."""
    err = max(np.abs(aX - check[0]).max(), np.abs(aY - check[1]).max())
    assert err < 1e-6, f"closed form and integration differ by {err}"
    path.write_text("t,aX,aY\n" + "".join(f"{a:.4f},{b:.5f},{c:.5f}\n" for a, b, c in zip(t, aX, aY)))
    marks = dict(marks, tend=float(t[-1]))
    mpath = path.with_name(path.stem + "-marks.csv")
    mpath.write_text(",".join(marks) + "\n" + ",".join(f"{v:g}" for v in marks.values()) + "\n")
    print(f"{path.name}: {len(t)} points, t 0-{t[-1]:g}; closed form = integration to {err:.1e}; "
          f"{mpath.name}: {marks}")


T_END = 12.8        # the curves' extent (the 1973 window: 12.78 upper, 12.89 lower)

if __name__ == "__main__":
    w1, w2, D1, D2 = modes(0.0)
    A1, A2, p1, p2 = general(w1, w2, D1, D2, AX0, AY0, OX0, OY0)
    t = np.linspace(0, T_END, 513)
    aX, aY = motion(t, w1, w2, D1, D2, A1, A2, p1, p2)
    print(f"omega_1 {w1:.5f}, omega_2 {w2:.5f} (ratio {w2 / w1:.5f}); A_1 {A1:.4f}, A_2 {A2:.4f}")
    write(pathlib.Path(__file__).with_suffix(".csv"), t, aX, aY, integrate(t, 0.0, [AX0, AY0, OX0, OY0]),
          aX0=AX0, aY0=AY0, OX0=OX0, OY0=OY0)
