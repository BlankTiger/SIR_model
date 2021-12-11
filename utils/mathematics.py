import numpy as np


def heaviside_analytical(t, tau):
    return 1 / (1 + np.exp(-40 * (t - tau)))
