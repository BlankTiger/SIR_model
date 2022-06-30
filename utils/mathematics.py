import numpy as np
import utils
from dataclasses import dataclass


@dataclass
class solution:
    t: np.ndarray
    y: np.ndarray


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
        if with_multiwave is True and t >= t_3:
            args["R_prev"] = R[t - t_3]

            k1 = np.array(f(t, prev_y, **args))
            k2 = np.array(f(t + dt2, prev_y + dt2 * k1, **args))
            k3 = np.array(f(t + dt2, prev_y + dt2 * k2, **args))
            k4 = np.array(f(t + dt, prev_y + dt * k3, **args))
            new_y = np.maximum(prev_y + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4), 0)
            S[t + 1] = new_y[0]
            I[t + 1] = new_y[1]
            R[t + 1] = new_y[2]

        else:
            k1 = np.array(f(t, prev_y, **args))
            k2 = np.array(f(t + dt2, prev_y + dt2 * k1, **args))
            k3 = np.array(f(t + dt2, prev_y + dt2 * k2, **args))
            k4 = np.array(f(t + dt, prev_y + dt * k3, **args))
            new_y = np.maximum(prev_y + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4), 0)
            S[t + 1] = new_y[0]
            I[t + 1] = new_y[1]
            R[t + 1] = new_y[2]

    sol = solution(np.array(time_points), np.array([S, I, R]))
    return sol


def solve_SIR_with_vaccination(time_range, y0, t_1, t_2, with_multiwave, t_3, **args):
    f = utils.models.SIR_with_vaccination
    dt = 0.05
    time_points = np.arange(time_range[0], time_range[1], dt)
    (S, I, R) = (np.zeros(shape=(len(time_points))) for _ in range(3))
    S[0] = y0[0]
    I[0] = y0[1]
    R[0] = y0[2]

    population = np.sum(y0)

    args["R_prev"] = 0
    args["population"] = population
    vac_rate = args["vac_rate"]
    for t in range(len(time_points) - 1):
        curr_t = time_points[t]

        dt2 = dt / 2
        prev_y = np.array([S[t], I[t], R[t]])

        if t_1 <= curr_t < t_2 + 1:
            args["vac_rate"] = vac_rate
        else:
            args["vac_rate"] = 0

        if with_multiwave and curr_t >= t_3:
            args["R_prev"] = R[t - t_3]

            k1 = np.array(f(curr_t, prev_y, **args))
            k2 = np.array(f(curr_t + dt2, prev_y + dt2 * k1, **args))
            k3 = np.array(f(curr_t + dt2, prev_y + dt2 * k2, **args))
            k4 = np.array(f(curr_t + dt, prev_y + dt * k3, **args))
            S[t + 1], I[t + 1], R[t + 1] = np.maximum(
                prev_y + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4), 0
            )
            if S[t + 1] >= population:
                S[t + 1] = population
            elif I[t + 1] >= population:
                I[t + 1] = population
            elif R[t + 1] >= population:
                R[t + 1] = population

        else:
            k1 = np.array(f(curr_t, prev_y, **args))
            k2 = np.array(f(curr_t + dt2, prev_y + dt2 * k1, **args))
            k3 = np.array(f(curr_t + dt2, prev_y + dt2 * k2, **args))
            k4 = np.array(f(curr_t + dt, prev_y + dt * k3, **args))
            S[t + 1], I[t + 1], R[t + 1] = np.maximum(
                prev_y + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4), 0
            )
            if S[t + 1] >= population:
                S[t + 1] = population
            elif I[t + 1] >= population:
                I[t + 1] = population
            elif R[t + 1] >= population:
                R[t + 1] = population

    return solution(np.array(time_points), np.array([S, I, R]))


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
