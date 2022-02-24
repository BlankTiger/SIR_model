import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
from .mathematics import find_max_and_argmax
import pickle as pkl

colors = [
    "#FFD700",
    "#ED572D",
    "#DC2F02",
    "#6A040F",
    "#CD34B5",
    "#3AFC98",
    "#02A14E",
    "#21aF56",
    "#0000FF",
    "#1E1E9C",
    "#0466C8",
    "#002855",
]

line_styles = ["-", "--", "-.", ":"]


def plot_SIR(y, t, beta, gamma, already_plotted=False):
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
    fig, ax = plt.subplots()
    plot_num = 0

    if already_plotted:
        fig_data = pkl.load(open(".fig.pkl", "rb"))
        for item in fig_data:
            if isinstance(item, plt.Figure):
                fig = item
                ax = fig.axes[0]
            else:
                if int(item) == 4:
                    item = 0
                plot_num = int(item)
    else:
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

    line_colors = [colors[plot_num], colors[plot_num + 4], colors[plot_num + 8]]
    line_style = line_styles[plot_num]

    fig.set_figwidth(10)
    fig.set_figheight(8)

    ax.plot(t, S, line_style, color=line_colors[0], label="Susceptible")
    ax.plot(t, I, line_style, color=line_colors[1], label="Infectious")
    ax.plot(t, R, line_style, color=line_colors[2], label="Recovered")
    ax.plot(0, 0, color="none", label=r_0_text)
    ax.plot(0, 0, color="none", label=max_infectious_text)
    ax.plot(0, 0, color="none", label=r_tmax_text)

    ax.legend(handlelength=4, framealpha=1)
    plt.tight_layout()
    data_to_save = [ax.figure, plot_num + 1]
    pkl.dump(data_to_save, open(".fig.pkl", "wb"))

    return fig


def plot_SIR_with_vaccination(y, t, beta, gamma, already_plotted=False):
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

    fig, ax = plt.subplots()
    plot_num = 0

    if already_plotted:
        fig_data = pkl.load(open(".fig.pkl", "rb"))
        for item in fig_data:
            if isinstance(item, plt.Figure):
                fig = item
                ax = fig.axes[0]
            else:
                if int(item) == 4:
                    item = 0
                plot_num = int(item)
    else:
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

    line_colors = [colors[plot_num], colors[plot_num + 4], colors[plot_num + 8]]
    line_style = line_styles[plot_num]

    fig.set_figwidth(10)
    fig.set_figheight(8)

    ax.plot(t, S, line_style, color=line_colors[0], label="Susceptible")
    ax.plot(t, I, line_style, color=line_colors[1], label="Infectious")
    ax.plot(t, R, line_style, color=line_colors[2], label="Recovered")
    ax.plot(0, 0, color="none", label=r_0_text)
    ax.plot(0, 0, color="none", label=max_infectious_text)
    ax.plot(0, 0, color="none", label=r_tmax_text)

    ax.legend(handlelength=4, framealpha=1)
    plt.tight_layout()
    data_to_save = [ax.figure, plot_num + 1]
    pkl.dump(data_to_save, open(".fig.pkl", "wb"))

    return fig
