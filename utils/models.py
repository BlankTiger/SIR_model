def SIR(t, y, beta, gamma, a, R_prev):
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
    S, I, R = y
    diff_m = a * R_prev
    diff_v = eff * vac_rate
    if S - beta * S * I - diff_v < 0:
        diff_v = S

    _S = -beta * S * I
    _R = gamma * I
    _I = beta * S * I - _R

    dydt = [_S + diff_m - diff_v, _I, _R - diff_m + diff_v]
    return dydt
