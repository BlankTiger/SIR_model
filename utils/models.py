import utils


def SIR(t, y, beta, gamma, a, R_prev):
    """Function modeling a SIR model.

    Args:
        y: vector of the variables
        t: time
        beta: infection rate
        gamma: recovery rate
        with_multiwave: indicates if recovered people lose immunity
        a: proportion of recovered people who lose immunity
        t_3: time of the start of immunity loss

    Returns:
        dydt: vector of the derivatives of the variables
    """
    S, I, R = y
    _S = -beta * S * I
    _R = gamma * I
    _I = beta * S * I - _R
    diff = a * R_prev
    if R - diff < 0:
        diff = 0
    dydt = [_S + diff, _I, _R - diff]
    return dydt


def SIR_with_vaccination(t, y, beta, gamma, eff, vac_rate, a, R_prev):
    """Function modeling a SIR model with vaccination.

    Args:
        y: vector of the variables
        t: time
        beta: infection rate
        gamma: recovery rate
        vac_rate: vaccination rate
        eff: efficacy of the vaccine
        t_1: time of the start of the vaccine
        t_2: time of the end of the vaccine
        with_multiwave: indicates if recovered people lose immunity
        a: proportion of recovered people who lose immunity
        t_3: time of the start of immunity loss

    Returns:
        dydt: vector of the derivatives of the variables
    """
    S, I, R = y
    diff_m = a * R_prev
    diff_v = eff * vac_rate
    if S - beta * S * I - diff_v < 0:
        diff_v = 0
    if R - diff_m < 0:
        diff_m = 0

    _S = -beta * S * I
    _R = gamma * I
    _I = beta * S * I - _R

    dydt = [_S + diff_m - diff_v, _I, _R - diff_m + diff_v]
    return dydt
    # if with_multiwave:
    #     if S - vac_rate * eff * hev(t, t_1) * (1 - hev(t, t_2)) <= 0 and t < t_2:
    #         dydt = [-S, beta * S * I - gamma * I, S + gamma * I]
    #     elif S - beta * S * I - vac_rate * eff * hev(t, t_1) * (1 - hev(t, t_2)) <= 0:
    #         dydt = [
    #             -beta * S * I + hev(t, t_3) * a * R,
    #             beta * S * I - gamma * I,
    #             gamma * I - hev(t, t_3) * a * R,
    #         ]
    #     else:
    #         dydt = [
    #             -beta * S * I
    #             + hev(t, t_3) * a * R
    #             - vac_rate * eff * hev(t, t_1) * (1 - hev(t, t_2)),
    #             beta * S * I - gamma * I,
    #             gamma * I
    #             - hev(t, t_3) * a * R
    #             + vac_rate * eff * hev(t, t_1) * (1 - hev(t, t_2)),
    #         ]
    #     return dydt

    # elif S - vac_rate * eff * hev(t, t_1) * (1 - hev(t, t_2)) <= 0 and t < t_2:
    #     dydt = [-S, beta * S * I - gamma * I, S + gamma * I]
    # elif S - beta * S * I - vac_rate * eff * hev(t, t_1) * (1 - hev(t, t_2)) <= 0:
    #     dydt = [-beta * S * I, beta * S * I - gamma * I, gamma * I]
    # else:
    #     dydt = [
    #         -beta * S * I - vac_rate * eff * hev(t, t_1) * (1 - hev(t, t_2)),
    #         beta * S * I - gamma * I,
    #         gamma * I + vac_rate * eff * hev(t, t_1) * (1 - hev(t, t_2)),
    #     ]
    # return dydt
