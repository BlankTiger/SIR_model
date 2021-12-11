import numpy as np
from scipy.integrate import odeint
from .models import SIR, SIR_with_vaccination


def heaviside_analytical(t, tau):
    return 1 / (1 + np.exp(-20 * (t - tau)))


def solve_SIR(y0, t_values, beta, gamma):
    return odeint(SIR, y0, t_values, args=(beta, gamma))


def solve_SIR_with_vaccination(
    y0, t_values, beta, gamma, vac_rate, eff, t_start, t_end
):
    return odeint(
        SIR_with_vaccination,
        y0,
        t_values,
        args=(beta, gamma, vac_rate, eff, t_start, t_end),
    )
