import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

colors = [
    "#ffd700",
    "#ffb14e",
    "#fa8775",
    "#ea5f94",
    "#cd34b5",
    "#9d02d7",
    "#0000ff",
    "#000000",
    "#000000",
    "#000000",
]


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
    plt.plot(t, S, color=colors[0], label="Susceptible")
    plt.plot(t, I, color=colors[4], label="Infected")
    plt.plot(t, R, color=colors[6], label="Recovered")
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
    plt.plot(t, S, color=colors[0], label="Susceptible")
    plt.plot(t, I, color=colors[4], label="Infected")
    plt.plot(t, R, color=colors[6], label="Recovered")
    plt.plot(t, S_v, "--", color=colors[1], label="Susceptible (vaccinated)")
    plt.plot(t, I_v, "--", color=colors[5], label="Infected (vaccinated)")
    plt.plot(t, R_v, "--", color=colors[7], label="Recovered (vaccinated)")
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
