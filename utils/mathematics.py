import numpy as np
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


def solve_SIR_with_vaccination(time_range, y0, t_1, t_2, with_multiwave, t_3, **args):
    f = utils.models.SIR_with_vaccination
    dt = 1
    time_points = np.arange(time_range[0], time_range[1], dt)
    (S, I, R) = (np.zeros(shape=(len(time_points))) for _ in range(3))
    S[0] = y0[0]
    I[0] = y0[1]
    R[0] = y0[2]

    args["R_prev"] = 0
    vac_rate = args["vac_rate"]
    for t in range(len(time_points) - 1):

        dt2 = dt / 2
        prev_y = np.array([S[t], I[t], R[t]])

        if not t_1 < t < t_2:
            args["vac_rate"] = 0
        else:
            args["vac_rate"] = vac_rate

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


def heaviside_analytical(t, tau):
    """Analytical version of the Heaviside function.

    Args:
        t (float): Time.
        tau (float): Time of the peak.

    Returns:
        float: The value of the Heaviside function at time t.
    """
    return 1 / (1 + np.exp(-5 * (t - tau)))


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
