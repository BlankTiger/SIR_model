import numpy as np
from scipy.integrate import solve_ivp
from .models import SIR, SIR_with_vaccination


def heaviside_analytical(t, tau):
    """Analytical version of the Heaviside function.

    Args:
        t (float): Time.
        tau (float): Time of the peak.

    Returns:
        float: The value of the Heaviside function at time t.
    """
    return 1 / (1 + np.exp(-5 * (t - tau)))


def solve_SIR(t_range, y0, beta, gamma, t_values):
    """Solves the SIR model using the scipy.integrate.solve_ivp function.

    Args:
        t_range (tuple): The time range of the simulation.
        y0 (tuple): The initial conditions.
        beta (float): The infection rate.
        gamma (float): The recovery rate.
        t_values (list): The time values at which to calculate the solution.

    Returns:
        tuple: The solution of the SIR model.
    """
    return solve_ivp(SIR, t_range, y0, t_eval=t_values, args=(beta, gamma))


def solve_SIR_with_vaccination(
    t_range, y0, beta, gamma, vac_rate, eff, t_start, t_end, t_values
):
    """Solves the SIR model with vaccinations using the
    scipy.integrate.solve_ivp function.

    Args:
        t_range (tuple): The time range of the simulation.
        y0 (tuple): The initial conditions.
        beta (float): The infection rate.
        gamma (float): The recovery rate.
        vac_rate (int): The vaccination rate.
        eff (float): The efficacy of the vaccination.
        t_start (int): The start time of the vaccination.
        t_end (int): The end time of the vaccination.
        t_values (list): The time values at which to calculate the solution.

    Returns:
        tuple: The solution of the SIR model with vaccinations.
    """
    return solve_ivp(
        SIR_with_vaccination,
        t_range,
        y0,
        t_eval=t_values,
        args=(beta, gamma, vac_rate, eff, t_start, t_end),
    )


def find_max_and_argmax(x, y):
    """Finds the maximum and its index in a function y = f(x).

    Args:
        x (list): The x values.
        y (list): The y values.

    Returns:
        tuple: The maximum value and its index.
    """
    max_y = np.max(y)
    max_x = x[np.argmax(y)]
    return max_x, max_y
