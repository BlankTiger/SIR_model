import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
from .mathematics import find_max_and_argmax
import pickle as pkl

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


def plot_SIR(y, t, beta, gamma, fig=None):
    plt.style.use("fivethirtyeight")
    plt.rcParams.update({"font.size": 10})
    np.set_printoptions(suppress=True)

    S, I, R = y.y[0, :], y.y[1, :], y.y[2, :]
    max_x, max_y = find_max_and_argmax(t, I)
    r_0_text = "$R_0 = " + str(round(beta * S[0] / gamma, 3)) + "$"
    max_infectious_text = (
        "$I_{\\mathrm{max}}(t) = "
        + str(int(round(max_y, 0)))
        + "\\;\\mathrm{at}\\;\\mathtt{t="
        + str(int(round(max_x, 0)))
        + "}$"
    )
    r_tmax_text = (
        "$R\\left({t_\\mathrm{max}}\\right) = " + str(int(round(R[-1], 0))) + "$"
    )
    additional_text = (r_0_text, max_infectious_text, r_tmax_text)

    if fig is None:
        fig, ax = plt.subplots()
        ax.text(
            -0.05 * max(t),
            max(S) * 1.05,
            "© M. Urban, J. Jodłowska, J. Balbus, K. Kubica",
            ha="left",
            va="top",
        )
        ax.ticklabel_format(axis="y", useOffset=False, style="Plain")
        ax.set_xlabel("Time [days]")
        ax.set_ylabel("Number of people")

    ax = fig.axes[0]
    fig.set_figwidth(8)
    fig.set_figheight(8)

    ax.plot(t, S, color=colors[0], label="Susceptible")
    ax.plot(t, I, color=colors[4], label="Infectious")
    ax.plot(t, R, color=colors[6], label="Recovered")

    handles, _ = ax.get_legend_handles_labels()
    for text in additional_text:
        handles.append(mpatches.Patch(color="none", label=text))

    plt.legend(handles=handles, framealpha=1)
    plt.tight_layout()
    pkl.dump(ax.figure, open(".fig.pkl", "wb"))
    return fig


def plot_SIR_with_vaccination(y, t, beta, gamma, fig=None):
    plt.style.use("fivethirtyeight")
    plt.rcParams.update({"font.size": 10})
    np.set_printoptions(suppress=True)

    S, I, R = y.y[0, :], y.y[1, :], y.y[2, :]
    max_x, max_y = find_max_and_argmax(t, I)
    max_infectious_text = (
        "$I_{\\mathrm{max}}(t) = "
        + str(int(round(max_y, 0)))
        + "\\;\\mathrm{at}\\;\\mathtt{t="
        + str(int(round(max_x, 0)))
        + "}$"
    )
    r_tmax_text = (
        "$R\\left({t_\\mathrm{max}}\\right) = " + str(int(round(R[-1], 0))) + "$"
    )
    additional_text = (r_tmax_text, max_infectious_text, "")

    if fig is None:
        fig, ax = plt.subplots()
        plt.text(
            -0.05 * max(t),
            max(S) * 1.05,
            "© M. Urban, J. Jodłowska, J. Balbus, K. Kubica",
            ha="left",
            va="top",
        )
        ax.ticklabel_format(axis="y", useOffset=False, style="Plain")
        ax.set_xlabel("Time [days]")
        ax.set_ylabel("Number of people")

    ax = fig.axes[0]
    fig.set_figwidth(8)
    fig.set_figheight(8)

    ax.plot(t, S, color=colors[1], label="Susceptible")
    ax.plot(t, I, color=colors[5], label="Infectious")
    ax.plot(t, R, color=colors[7], label="Recovered")

    handles, _ = ax.get_legend_handles_labels()
    for text in additional_text:
        handles.append(mpatches.Patch(color="none", label=text))

    plt.legend(handles=handles, handlelength=3, framealpha=1)
    plt.tight_layout()
    pkl.dump(ax.figure, open(".fig.pkl", "wb"))
    return fig
