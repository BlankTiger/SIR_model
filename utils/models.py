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


def SIR_with_vaccination(t, y, beta, gamma, eff, vac_rate, a, R_prev, population):
    S, I, R = y
    diff_m = a * R_prev
    diff_v = eff * vac_rate

    _S = -beta * S * I + diff_m - diff_v
    _I = beta * S * I - gamma * I
    _R = gamma * I - diff_m + diff_v

    if R >= population:
        _R = population - R

    return [_S, _I, _R]
