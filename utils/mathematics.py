import numpy as np
from scipy.integrate import solve_ivp
import utils


class solution:
    def __init__(self, t, y):
        self.t = t
        self.y = y


def solve_SIR(time_range, y0, with_multiwave, t_3, **args):
    f = utils.models.SIR
    dt = 1
    time_points = np.arange(time_range[0], time_range[1], dt)
    (S, I, R) = (np.zeros(shape=(len(time_points))) for _ in range(3))
    S[0] = y0[0]
    I[0] = y0[1]
    R[0] = y0[2]

    args["R_prev"] = 0
    for t in range(len(time_points) - 1):

        dt2 = dt / 2
        prev_y = np.array([S[t], I[t], R[t]])
        if with_multiwave is True and t > t_3:
            args["R_prev"] = R[t - t_3]

            k1 = np.array(f(t, prev_y, **args))
            k2 = np.array(f(t + dt2, prev_y + dt2 * k1, **args))
            k3 = np.array(f(t + dt2, prev_y + dt2 * k2, **args))
            k4 = np.array(f(t + dt, prev_y + dt * k3, **args))
            new_y = prev_y + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
            S[t + 1] = new_y[0]
            I[t + 1] = new_y[1]
            R[t + 1] = new_y[2]

        else:
            k1 = np.array(f(t, prev_y, **args))
            k2 = np.array(f(t + dt2, prev_y + dt2 * k1, **args))
            k3 = np.array(f(t + dt2, prev_y + dt2 * k2, **args))
            k4 = np.array(f(t + dt, prev_y + dt * k3, **args))
            new_y = prev_y + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
            S[t + 1] = new_y[0]
            I[t + 1] = new_y[1]
            R[t + 1] = new_y[2]

    sol = solution(np.array(time_points), np.array([S, I, R]))
    return sol


# def solve_SIR(t_range, y0, beta, gamma, with_multiwave, a, t_3, R_prev, t_values):
#     """Solves the SIR model using the scipy.integrate.solve_ivp function.

#     Args:
#         t_range (tuple): The time range of the simulation.
#         y0 (tuple): The initial conditions.
#         beta (float): The infection rate.
#         gamma (float): The recovery rate.
#         t_values (list): The time values at which to calculate the solution.
#         with_multiwave (bool): indicates if recovered people lose immunity
#         a (float): proportion of recovered people who lose immunity
#         t_3 (int): time of the start of immunity loss

#     Returns:
#         tuple: The solution of the SIR model.
#     """
#     SIR = utils.models.SIR
#     return solve_ivp(
#         SIR,
#         t_range,
#         y0,
#         t_eval=t_values,
#         method="DOP853",
#         args=(beta, gamma, with_multiwave, a, t_3, R_prev),
#     )


def heaviside_analytical(t, tau):
    """Analytical version of the Heaviside function.

    Args:
        t (float): Time.
        tau (float): Time of the peak.

    Returns:
        float: The value of the Heaviside function at time t.
    """
    return 1 / (1 + np.exp(-5 * (t - tau)))


def solve_SIR_with_vaccination(
    t_range,
    y0,
    beta,
    gamma,
    vac_rate,
    eff,
    t_start,
    t_end,
    with_multiwave,
    a,
    t_3,
    t_values,
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
        with_multiwave (bool): indicates if recovered people lose immunity
        a (float): proportion of recovered people who lose immunity
        t_3 (int): time of the start of immunity loss

    Returns:
        tuple: The solution of the SIR model with vaccinations.
    """
    SIR_with_vaccination = utils.models.SIR_with_vaccination
    return solve_ivp(
        SIR_with_vaccination,
        t_range,
        y0,
        t_eval=t_values,
        method="DOP853",
        args=(beta, gamma, vac_rate, eff, t_start, t_end, with_multiwave, a, t_3),
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
