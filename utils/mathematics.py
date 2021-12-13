import numpy as np
from scipy.integrate import solve_ivp
from .models import SIR, SIR_with_vaccination


def heaviside_analytical(t, tau):
    return 1 / (1 + np.exp(-5 * (t - tau)))


def solve_SIR(t_range, y0, beta, gamma, t_values):
    return solve_ivp(SIR, t_range, y0, t_eval=t_values, args=(beta, gamma))


def solve_SIR_with_vaccination(
    t_range, y0, beta, gamma, vac_rate, eff, t_start, t_end, t_values
):
    return solve_ivp(
        SIR_with_vaccination,
        t_range,
        y0,
        t_eval=t_values,
        args=(beta, gamma, vac_rate, eff, t_start, t_end),
    )


def find_max_and_argmax(x, y):
    max_y = np.max(y)
    max_x = x[np.argmax(y)]
    return max_x, max_y
