import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches


def plot_SIR(y, t, beta, gamma):
    """ """
    plt.gcf()
    plt.style.use("fivethirtyeight")
    plt.rcParams.update({"font.size": 13})
    np.set_printoptions(suppress=True)
    S, I, R = y[:, 0], y[:, 1], y[:, 2]
    figure = plt.figure()
    dpi = figure.get_dpi()
    figure.set_figwidth(768 / dpi)
    figure.set_figheight(576 / dpi)
    plt.plot(t, S, label="Susceptible")
    plt.plot(t, I, label="Infected")
    plt.plot(t, R, label="Recovered")
    gamma_text = (
        "$γ = \\frac{1}{\\mathtt{recovery\\;time}} = "
        + str(round(gamma, 3))
        + "$"
    )
    r_0_text = "$R_0 = \\frac{β}{γ}=" + str(round(beta / gamma, 3)) + "$"
    plt.ticklabel_format(axis="y", useOffset=False, style="Plain")
    plt.xlabel("Time [days]")
    plt.ylabel("Number of people")
    handles, labels = plt.gca().get_legend_handles_labels()
    handles.append(mpatches.Patch(color="none", label=gamma_text))
    handles.append(mpatches.Patch(color="none", label=r_0_text))
    plt.legend(handles=handles)
    plt.tight_layout()
    return figure


def plot_SIR_with_vaccination(y, y_v, t, beta, gamma):
    plt.gcf()
    plt.style.use("fivethirtyeight")
    plt.rcParams.update({"font.size": 12})
    np.set_printoptions(suppress=True)
    S, I, R = y[:, 0], y[:, 1], y[:, 2]
    S_v, I_v, R_v = y_v[:, 0], y_v[:, 1], y_v[:, 2]
    figure = plt.figure()
    dpi = figure.get_dpi()
    figure.set_figwidth(768 / dpi)
    figure.set_figheight(576 / dpi)
    plt.plot(t, S, label="Susceptible")
    plt.plot(t, I, label="Infected")
    plt.plot(t, R, label="Recovered")
    plt.plot(t, S_v, "--", color="blue", label="Susceptible (vaccinated)")
    plt.plot(t, I_v, "--", color="orange", label="Infected (vaccinated)")
    plt.plot(t, R_v, "--", color="yellow", label="Recovered (vaccinated)")
    gamma_text = (
        "$γ = \\frac{1}{\\mathtt{recovery\\;time}} = "
        + str(round(gamma, 3))
        + "$"
    )
    r_0_text = "$R_0 = \\frac{β}{γ}=" + str(round(beta / gamma, 3)) + "$"
    plt.ticklabel_format(axis="y", useOffset=False, style="Plain")
    plt.xlabel("Time [days]")
    plt.ylabel("Number of people")
    handles, labels = plt.gca().get_legend_handles_labels()
    handles.append(mpatches.Patch(color="none", label=gamma_text))
    handles.append(mpatches.Patch(color="none", label=r_0_text))
    plt.legend(handles=handles)
    plt.tight_layout()
    return figure
