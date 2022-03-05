import numpy as np
import matplotlib.pyplot as plt
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


def plot_SIR(y, t, beta, gamma, already_plotted=False) -> plt.Figure:
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

    fig, ax = None, None
    plot_num = 0

    if already_plotted:
        try:
            with open(".fig.pkl", "rb") as f:
                fig, plot_num = pkl.load(f)
                plt.subplots_adjust(top=1, bottom=0, left=0, right=1)
                ax = fig.axes[0]
                if plot_num == 4:
                    plot_num = 0
        except (FileNotFoundError, OSError):
            fig = plt.figure()
            plt.subplots_adjust(top=1, bottom=0, left=0, right=1)
            ax = fig.add_subplot(111)
            plt.text(
                0.05,
                0.96,
                "© M. Urban, J. Jodłowska, J. Balbus, K. Kubica",
                fontsize=10,
                transform=plt.gcf().transFigure,
            )
            ax.ticklabel_format(axis="y", useOffset=False, style="Plain")
            ax.set_xlabel("Time [days]")
            ax.set_ylabel("Number of people")

    else:
        fig = plt.figure()
        plt.subplots_adjust(top=1, bottom=0.01, left=0.01, right=1)
        ax = fig.add_subplot(111)
        plt.text(
            0.05,
            0.98,
            "© M. Urban, J. Jodłowska, J. Balbus, K. Kubica",
            fontsize=10,
            transform=plt.gcf().transFigure,
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
    data_to_save = [fig, plot_num + 1]
    pkl.dump(data_to_save, open(".fig.pkl", "wb"))

    return fig
