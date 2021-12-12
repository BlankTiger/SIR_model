import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
from .mathematics import find_max_and_argmax

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
    max_x, max_y = find_max_and_argmax(t, I)
    figure = plt.figure()
    dpi = figure.get_dpi()
    figure.set_figwidth(1000 / dpi)
    figure.set_figheight(800 / dpi)
    plt.plot(t, S, color=colors[0], label="Susceptible")
    plt.plot(t, I, color=colors[4], label="Infected")
    plt.plot(t, R, color=colors[6], label="Recovered")
    gamma_text = (
        "$γ = \\frac{1}{\\mathtt{recovery\\;time}} = "
        + str(round(gamma, 3))
        + "$"
    )
    r_0_text = "$R_0 = \\frac{β}{γ}=" + str(round(beta / gamma, 3)) + "$"
    max_infected_text = (
        "$I_{\\mathrm{max}}(t) = "
        + str(int(round(max_y, 0)))
        + "\\;\\mathrm{at}\\;\\mathtt{t="
        + str(int(round(max_x, 0)))
        + "}$"
    )
    additional_text = (gamma_text, r_0_text, max_infected_text)
    plt.ticklabel_format(axis="y", useOffset=False, style="Plain")
    plt.xlabel("Time [days]")
    plt.ylabel("Number of people")
    handles, labels = plt.gca().get_legend_handles_labels()
    for text in additional_text:
        handles.append(mpatches.Patch(color="none", label=text))
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
    max_x, max_y = find_max_and_argmax(t, I)
    max_x_v, max_y_v = find_max_and_argmax(t, I_v)
    figure = plt.figure()
    dpi = figure.get_dpi()
    figure.set_figwidth(1000 / dpi)
    figure.set_figheight(800 / dpi)
    plt.plot(t, S, color=colors[0], label="Susceptible")
    plt.plot(t, I, color=colors[4], label="Infected")
    plt.plot(t, R, color=colors[6], label="Recovered")
    plt.plot(t, S_v, "--", color=colors[1], label="Susceptible (v)")
    plt.plot(t, I_v, "--", color=colors[5], label="Infected (v)")
    plt.plot(t, R_v, "--", color=colors[7], label="Recovered (v)")
    gamma_text = (
        "$γ = \\frac{1}{\\mathtt{recovery\\;time}} = "
        + str(round(gamma, 3))
        + "$"
    )
    r_0_text = "$R_0 = \\frac{β}{γ}=" + str(round(beta / gamma, 3)) + "$"
    max_infected_text = (
        "$I_{\\mathrm{max}}(t) = "
        + str(int(round(max_y, 0)))
        + "\\;\\mathrm{at}\\;\\mathtt{t="
        + str(int(round(max_x, 0)))
        + "}$"
    )
    max_infected_v_text = (
        "$I_{v,\\mathrm{max}}(t) = "
        + str(int(round(max_y_v, 0)))
        + "\\;\\mathrm{at}\\;\\mathtt{t="
        + str(int(round(max_x_v, 0)))
        + "}$"
    )
    additional_text = (
        gamma_text,
        r_0_text,
        max_infected_text,
        max_infected_v_text,
    )
    plt.ticklabel_format(axis="y", useOffset=False, style="Plain")
    plt.xlabel("Time [days]")
    plt.ylabel("Number of people")
    handles, labels = plt.gca().get_legend_handles_labels()
    for text in additional_text:
        handles.append(mpatches.Patch(color="none", label=text))
    plt.legend(handles=handles, handlelength=3)
    plt.tight_layout()
    return figure
