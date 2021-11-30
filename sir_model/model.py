import matplotlib.pyplot as plt
import numpy as np


def SIR(y, t, a, r):
    """
    Function modeling a SIR model.

    Args:
        t: time
        y: vector of the variables

    Returns:
        dydt: vector of the derivatives of the variables
    """
    S, I, R = y
    dydt = [-r * S * I, r * S * I - a * I, a * I]
    return dydt


def plot_SIR(y, t, a, r, N):
    """
    Function to plot the SIR model.

    Args:
        S: vector of susceptible individuals
        I: vector of infected individuals
        R: vector of recovered individuals
        t: time
        a: rate of recovery
        r: rate of infection
    """
    plt.cla()
    plt.style.use("fivethirtyeight")
    # plt.style.use("dark_background")
    plt.rcParams.update({"font.size": 10})
    np.set_printoptions(suppress=True)
    S, I, R = y[:, 0] * N, y[:, 1] * N, y[:, 2] * N
    figure = plt.figure()
    plt.plot(t, S, label="Susceptible")
    plt.plot(t, I, label="Infected")
    plt.plot(t, R, label="Recovered")
    plt.ticklabel_format(axis="y", useOffset=False, style="Plain")
    plt.xlabel("Time [days]")
    plt.ylabel("Number of people")
    plt.legend()
    plt.tight_layout()
    return figure
