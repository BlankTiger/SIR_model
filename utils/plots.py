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
    """Plot SIR model

    Args:
        y (scipy.integrate._ivp.ivp.OdeResult): solution of the ODE
        t (array): time array
        beta (float): infection rate
        gamma (float): recovery rate

    Returns:
        figure: figure object
    """
    plt.gcf()
    plt.style.use("fivethirtyeight")
    plt.rcParams.update({"font.size": 12})
    np.set_printoptions(suppress=True)
    S, I, R = y.y[0, :], y.y[1, :], y.y[2, :]
    max_x, max_y = find_max_and_argmax(t, I)
    figure = plt.figure()
    plt.text(
        0,
        max(S) * 1.05,
        "© M. Urban, J. Jodłowska, J. Balbus, K. Kubica",
        ha="left",
        va="top",
    )
    dpi = figure.get_dpi()
    figure.set_figwidth(1000 / dpi)
    figure.set_figheight(800 / dpi)
    plt.plot(t, S, color=colors[0], label="Susceptible")
    plt.plot(t, I, color=colors[4], label="Infectious")
    plt.plot(t, R, color=colors[6], label="Recovered")
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
    plt.ticklabel_format(axis="y", useOffset=False, style="Plain")
    plt.xlabel("Time [days]")
    plt.ylabel("Number of people")
    handles, _ = plt.gca().get_legend_handles_labels()
    for text in additional_text:
        handles.append(mpatches.Patch(color="none", label=text))
    plt.legend(handles=handles, framealpha=1)
    plt.tight_layout()
    return figure


def plot_SIR_with_vaccination(y, y_v, t, beta, gamma):
    """Plot SIR model with vaccination

    Args:
        y (scipy.integrate._ivp.ivp.OdeResult): solution of the ODE
        y_v (scipy.integrate._ivp.ivp.OdeResult): solution of the ODE with
            vaccination
        t (array): time array
        beta (float): infection rate
        gamma (float): recovery rate

    Returns:
        figure: figure object
    """
    plt.gcf()
    plt.style.use("fivethirtyeight")
    plt.rcParams.update({"font.size": 12})
    np.set_printoptions(suppress=True)
    S, I, R = y.y[0, :], y.y[1, :], y.y[2, :]
    S_v, I_v, R_v = y_v.y[0, :], y_v.y[1, :], y_v.y[2, :]
    max_x, max_y = find_max_and_argmax(t, I)
    max_x_v, max_y_v = find_max_and_argmax(t, I_v)
    figure = plt.figure()
    plt.text(
        0,
        max(S) * 1.05,
        "© M. Urban, J. Jodłowska, J. Balbus, K. Kubica",
        ha="left",
        va="top",
    )
    dpi = figure.get_dpi()
    figure.set_figwidth(1000 / dpi)
    figure.set_figheight(800 / dpi)
    plt.plot(t, S, color=colors[0], label="Susceptible")
    plt.plot(t, I, color=colors[4], label="Infectious")
    plt.plot(t, R, color=colors[6], label="Recovered")
    plt.plot(t, S_v, "--", color=colors[1], label="Susceptible (v)")
    plt.plot(t, I_v, "--", color=colors[5], label="Infectious (v)")
    plt.plot(t, R_v, "--", color=colors[7], label="Recovered (v)")
    r_0_text = "$R_0 = " + str(round(beta * S[0] / gamma, 3)) + "$"
    max_infectious_text = (
        "$I_{\\mathrm{max}}(t) = "
        + str(int(round(max_y, 0)))
        + "\\;\\mathrm{at}\\;\\mathtt{t="
        + str(int(round(max_x, 0)))
        + "}$"
    )
    max_infectious_v_text = (
        "$I_{v,\\mathrm{max}}(t) = "
        + str(int(round(max_y_v, 0)))
        + "\\;\\mathrm{at}\\;\\mathtt{t="
        + str(int(round(max_x_v, 0)))
        + "}$"
    )
    r_tmax_text = (
        "$R\\left({t_\\mathrm{max}}\\right) = " + str(int(round(R[-1], 0))) + "$"
    )
    r_tmax_v_text = (
        "$R_v\\left({t_\\mathrm{max}}\\right) = " + str(int(round(R_v[-1], 0))) + "$"
    )
    additional_text = (r_0_text, max_infectious_text, r_tmax_text, "")
    plt.ticklabel_format(axis="y", useOffset=False, style="Plain")
    plt.xlabel("Time [days]")
    plt.ylabel("Number of people")
    handles, _ = plt.gca().get_legend_handles_labels()
    for text in additional_text:
        handles.append(mpatches.Patch(color="none", label=text))
    # move elements of index 3, 4, 5 to the end of the list
    for _ in range(3, 6):
        handles.append(handles.pop(3))
    handles.append(mpatches.Patch(color="none", label=max_infectious_v_text))
    handles.append(mpatches.Patch(color="none", label=r_tmax_v_text))
    plt.legend(handles=handles, handlelength=3, framealpha=1)
    plt.tight_layout()
    return figure
