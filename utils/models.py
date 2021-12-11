from .mathematics import heaviside_analytical as hev


def SIR(y, t, beta, gamma):
    """
    Function modeling a SIR model.

    Args:
        y: vector of the variables
        t: time
        beta: infection rate
        gamma: recovery rate

    Returns:
        dydt: vector of the derivatives of the variables
    """
    S, I, R = y
    N = S + I + R
    dydt = [-beta * S * I / N, beta * S * I / N - gamma * I, gamma * I]
    return dydt


def SIR_with_vaccination(y, t, beta, gamma, vac_rate, eff, t_1, t_2):
    """
    Function modeling a SIR model with vaccination.

    Args:
        y: vector of the variables
        t: time
        beta: infection rate
        gamma: recovery rate
        vac_rate: vaccination rate
        eff: efficacy of the vaccine
        t_1: time of the start of the vaccine
        t_2: time of the end of the vaccine

    Returns:
        dydt: vector of the derivatives of the variables
    """
    S, I, R = y
    N = S + I + R
    if vac_rate * eff * (t_2 - t_1) > S:
        t_2 = t_1 + S / vac_rate / eff
    dydt = [
        -beta * S * I / N - vac_rate * eff * hev(t, t_1) * (1 - hev(t, t_2)),
        beta * S * I / N - gamma * I,
        gamma * I + vac_rate * eff * hev(t, t_1) * (1 - hev(t, t_2)),
    ]
    return dydt
