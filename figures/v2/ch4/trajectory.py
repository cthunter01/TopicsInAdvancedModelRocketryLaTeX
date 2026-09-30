#!/usr/bin/env python3
"""Chapter 4's vertical-flight computations, shared by the redrawn Figures 6, 11 and 16.

Engine B4: the Figure 4 lettering (I_t = 5.0 N-sec, F_m = 13.0 N, F_s = 3.5 N, t_1 = 0.14 sec, t_2 = 0.22 sec,
t_b = 1.20 sec), thrust by the piecewise-linear approximation eqs. (73a)-(73c), propellant mass 8.33 g
(Table 1), mass lost in proportion to the impulse delivered (c = I_t/m_p). g = 9.8 m/sec^2 (Chapter 1).

  interval(m_o, k)            the "second" interval method, eqs. (83)-(87), dt = 0.001 sec (the book's
                              exact solution); the coast uses the same iteration at the burnout mass
  fehskens_malewicki(m_o, k)  eqs. (20), (21) with m = mean of liftoff and burnout mass, F = I_t/t_b
  caporaso_bengen(m_o, k)     eqs. (27), (28), same m and F
Each returns (v_b, y_b, y_max); the approximations add the coast by eq. (67) at the burnout mass.

Run as a script: a regression test against Table 2's "No disturbance" row.
"""
import math

G = 9.8


class Engine:
    def __init__(self, It, tb, Fm, Fs, t1, t2, mp):
        self.It, self.tb, self.Fm, self.Fs, self.t1, self.t2, self.mp = It, tb, Fm, Fs, t1, t2, mp

    def thrust(self, t):
        if t <= self.t1:
            return self.Fm * t / self.t1
        if t <= self.t2:
            return self.Fm - (t - self.t1) / (self.t2 - self.t1) * (self.Fm - self.Fs)
        if t <= self.tb:
            return self.Fs
        return 0.0


B4 = Engine(It=5.0, tb=1.20, Fm=13.0, Fs=3.5, t1=0.14, t2=0.22, mp=0.00833)


def interval(m0, k, eng=B4, dt=0.001):
    c = eng.It / eng.mp
    v = y = t = 0.0
    m = m0
    n = round(eng.tb / dt)
    for _ in range(n):                       # burning: eqs. (83)-(87), mass by the impulse delivered
        f = eng.thrust(t)
        dv = dt * (f - m * G - k * v * v) / m
        y += dt * (v + dv / 2)
        v += dv
        if v < 0 and y <= 0:                 # on the pad until the thrust exceeds the weight
            v = y = 0.0
        m -= f / c * dt
        t += dt
    vb, yb, mb = v, y, m
    while v > 0:                             # coasting: the same iteration without thrust
        dv = dt * (-mb * G - k * v * v) / mb
        y += dt * (v + dv / 2)
        v += dv
        t += dt
    return vb, yb, y, t - eng.tb


def _coast(vb, mb, k):                        # eq. (67)
    return mb / (2 * k) * math.log(k * vb * vb / (mb * G) + 1)


def fehskens_malewicki(m0, k, eng=B4):
    m, mb, F = m0 - eng.mp / 2, m0 - eng.mp, eng.It / eng.tb
    a = eng.tb / m * math.sqrt(k * (F - m * G))
    vb = math.sqrt((F - m * G) / k) * math.tanh(a)          # eq. (20)
    yb = m / k * math.log(math.cosh(a))                      # eq. (21)
    return vb, yb, yb + _coast(vb, mb, k)


def caporaso_bengen(m0, k, eng=B4):
    m, mb, F = m0 - eng.mp / 2, m0 - eng.mp, eng.It / eng.tb
    root = math.sqrt(m * m + k * eng.tb ** 2 * (F - m * G))
    yb = (-m + root) / k                                     # eq. (27)
    vb = (eng.It - m * G * eng.tb) / root                    # eq. (28)
    return vb, yb, yb + _coast(vb, mb, k)


if __name__ == "__main__":
    vb, yb, ymax, tc = interval(0.040, 0.92e-4)
    got = (vb, yb, tc, ymax - yb, ymax)
    want = (111.4, 78.1, 6.46, 265.5, 343.6)    # Table 2, "No disturbance": v_b, y_b, t_c, y_c, y_max
    unit = (0.1, 0.1, 0.01, 0.1, 0.1)            # one unit in the last printed digit (the table's y_c is
    ok = all(abs(g - w) <= u for g, w, u in zip(got, want, unit))   # y_max - y_b of the rounded values)
    print(f"Table 2 regression: computed {tuple(round(g, 3) for g in got)}, printed {want}: "
          f"{'ok' if ok else 'MISMATCH'}")
    raise SystemExit(0 if ok else 1)
