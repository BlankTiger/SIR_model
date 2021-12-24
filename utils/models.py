def SIR(t, y, beta, gamma):
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
    dydt = [-beta * S * I, beta * S * I - gamma * I, gamma * I]
    return dydt


def SIR_with_vaccination(t, y, beta, gamma, vac_rate, eff, t_1, t_2):
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
    from .mathematics import heaviside_analytical as hev

    S, I, R = y
    dydt = []
    if S - vac_rate * eff * hev(t, t_1) * (1 - hev(t, t_2)) <= 0 and t < t_2:
        dydt = [-S, beta * S * I - gamma * I, S + gamma * I]
    elif (
        S - beta * S * I - vac_rate * eff * hev(t, t_1) * (1 - hev(t, t_2))
        <= 0
    ):
        dydt = [
            -beta * S * I,
            beta * S * I - gamma * I,
            gamma * I,
        ]
    else:
        dydt = [
            -beta * S * I - vac_rate * eff * hev(t, t_1) * (1 - hev(t, t_2)),
            beta * S * I - gamma * I,
            gamma * I + vac_rate * eff * hev(t, t_1) * (1 - hev(t, t_2)),
        ]
    return dydt
