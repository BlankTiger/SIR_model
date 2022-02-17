import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib
import matplotlib.font_manager as fm
import numpy as np
from utils.mathematics import find_max_and_argmax
import platform


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


def prepare_data_for_plots():
    from utils.mathematics import solve_SIR, solve_SIR_with_vaccination

    basic_SIR_data = solve_SIR(
        (0, 150), [1e6, 1, 0], 4e-7, 0.2, False, 0, 0, t_values=np.linspace(0, 150, 150)
    )
    basic_SIR_data_2 = solve_SIR(
        (0, 150),
        [1e6, 1, 0],
        2.8571e-7,
        0.1429,
        False,
        0,
        0,
        t_values=np.linspace(0, 150, 150),
    )
    vaccination_comparison_data_50_71 = solve_SIR_with_vaccination(
        (0, 150),
        [1e6, 1, 0],
        4e-7,
        0.2,
        2e4,
        0.9,
        50,
        71,
        False,
        0,
        0,
        t_values=np.linspace(0, 150, 150),
    )

    vaccination_comparison_data_50_91 = solve_SIR_with_vaccination(
        (0, 150),
        [1e6, 1, 0],
        4e-7,
        0.2,
        1e4,
        0.9,
        50,
        91,
        False,
        0,
        0,
        t_values=np.linspace(0, 150, 150),
    )
    multiwave_comparison_data_30 = solve_SIR(
        (0, 400),
        [1e6, 1, 0],
        4e-7,
        0.2,
        True,
        0.01,
        30,
        t_values=np.linspace(0, 150, 150),
    )
    multiwave_comparison_data_60 = solve_SIR(
        (0, 400),
        [1e6, 1, 0],
        4e-7,
        0.2,
        True,
        0.01,
        60,
        t_values=np.linspace(0, 150, 150),
    )
    return (
        basic_SIR_data.y,
        basic_SIR_data_2.y,
        vaccination_comparison_data_50_71.y,
        vaccination_comparison_data_50_91.y,
        multiwave_comparison_data_30.y,
        multiwave_comparison_data_60.y,
    )


def plot_basic_SIR(basic_SIR_data):
    plt.style.use("fivethirtyeight")
    plt.rcParams.update({"font.size": 16})

    np.set_printoptions(suppress=True)
    S, I, R = basic_SIR_data[0, :], basic_SIR_data[1, :], basic_SIR_data[2, :]
    t = np.linspace(0, 150, 150)
    beta = 4e-7
    gamma = 0.2
    max_x, max_y = find_max_and_argmax(t, I)
    figure = plt.figure(facecolor="white")
    # figure.patch.set_alpha(0)
    axes = plt.axes()
    axes.set_facecolor("#ffffff")
    axes.tick_params(color="black", labelcolor="black")
    for spine in axes.spines.values():
        spine.set_edgecolor("#ffffff")
    plt.text(
        max(t),
        max(S) * 1.05,
        "© M. Urban, J. Jodłowska, J. Balbus, K. Kubica",
        ha="right",
        va="top",
    )
    figure.set_figwidth(12)
    figure.set_figheight(8)
    plt.plot(t, S, color=colors[0], label="Susceptible")
    plt.plot(t, I, color=colors[4], label="Infectious")
    plt.plot(t, R, color=colors[6], label="Recovered")
    r_0_text = "$R_0 = " + str(round(beta * S[0] / gamma, 3)) + "$"
    max_infectious_text = (
        "$I_{\\mathrm{max}}(t) = "
        + str(int(round(max_y, 0)))
        + "\\;\\mathrm{at}\\;t="
        + str(int(round(max_x, 0)))
        + "$"
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
    plt.legend(handles=handles, framealpha=1, loc="center left")
    plt.tight_layout()
    plt.savefig(
        "C:/Users/work/Desktop/optymalizacja-figures/fig_1.tif",
        facecolor="white",
        dpi=300,
    )
    plt.savefig(
        "C:/Users/work/Desktop/optymalizacja-figures/fig_1.pdf", facecolor="white"
    )
    plt.show()


def plot_SIR_with_vaccination_comparison(y_v_1, y_v_2):
    plt.style.use("fivethirtyeight")
    plt.rcParams.update({"font.size": 16})

    np.set_printoptions(suppress=True)
    S_v_1, I_v_1, R_v_1 = y_v_1[0, :], y_v_1[1, :], y_v_1[2, :]
    S_v_2, I_v_2, R_v_2 = y_v_2[0, :], y_v_2[1, :], y_v_2[2, :]
    t = np.linspace(0, 150, 150)
    beta = 4e-7
    gamma = 0.2
    max_x_v_1, max_y_v_1 = find_max_and_argmax(t, I_v_1)
    max_x_v_2, max_y_v_2 = find_max_and_argmax(t, I_v_2)
    figure = plt.figure(facecolor="white")
    axes = plt.axes()
    axes.set_facecolor("#ffffff")
    # axes.tick_params(color="#ffffff", labelcolor="#ffffff")
    for spine in axes.spines.values():
        spine.set_edgecolor("#ffffff")
    plt.text(
        max(t),
        max(S_v_1) * 1.05,
        "© M. Urban, J. Jodłowska, J. Balbus, K. Kubica",
        ha="right",
        va="top",
    )
    figure.set_figwidth(12)
    figure.set_figheight(8)
    plt.plot(t, S_v_1, "o", color=colors[0], label="Susceptible (50-71)")
    plt.plot(t, I_v_1, "o", color=colors[4], label="Infectious (50-71)")
    plt.plot(t, R_v_1, "o", color=colors[6], label="Recovered (50-71)")
    plt.plot(t, S_v_2, "--", color=colors[1], label="Susceptible (50-91)")
    plt.plot(t, I_v_2, "--", color=colors[5], label="Infectious (50-91)")
    plt.plot(t, R_v_2, "--", color=colors[7], label="Recovered (50-91)")
    r_0_text = "$R_0 = " + str(round(beta * S_v_1[0] / gamma, 3)) + "$"
    max_infectious_v_1_text = (
        "$I_{\\mathrm{max}}(t) = "
        + str(int(round(max_y_v_1, 0)))
        + "\\;\\mathrm{at}\\;t="
        + str(int(round(max_x_v_1, 0)))
        + "$"
    )
    max_infectious_v_2_text = (
        "$I_{\\mathrm{max}}(t) = "
        + str(int(round(max_y_v_2, 0)))
        + "\\;\\mathrm{at}\\;t="
        + str(int(round(max_x_v_2, 0)))
        + "$"
    )
    r_tmax_v_1_text = (
        "$R\\left({t_\\mathrm{max}}\\right) = " + str(int(round(R_v_1[-1], 0))) + "$"
    )
    r_tmax_v_2_text = (
        "$R\\left({t_\\mathrm{max}}\\right) = " + str(int(round(R_v_2[-1], 0))) + "$"
    )
    additional_text = (r_0_text, max_infectious_v_1_text, r_tmax_v_1_text, "")
    plt.ticklabel_format(axis="y", useOffset=False, style="Plain")
    plt.xlabel("Time [days]")
    plt.ylabel("Number of people")
    handles, _ = plt.gca().get_legend_handles_labels()
    for text in additional_text:
        handles.append(mpatches.Patch(color="none", label=text))
    # move elements of index 3, 4, 5 to the end of the list
    for _ in range(3, 6):
        handles.append(handles.pop(3))
    handles.append(mpatches.Patch(color="none", label=max_infectious_v_2_text))
    handles.append(mpatches.Patch(color="none", label=r_tmax_v_2_text))
    plt.legend(handles=handles, handlelength=3, framealpha=1, numpoints=3)
    plt.tight_layout()
    plt.savefig(
        "C:/Users/work/Desktop/optymalizacja-figures/fig_2.tif",
        facecolor="white",
        dpi=300,
    )
    plt.savefig(
        "C:/Users/work/Desktop/optymalizacja-figures/fig_2.pdf", facecolor="white"
    )
    plt.show()


def plot_SIR_with_multiwave_comparison():
    figure = plt.figure(facecolor="#ffffff")
    figure.patch.set_facecolor("#ffffff")
    axes = plt.axes()
    axes.set_facecolor("#ffffff")
    # axes.tick_params(color="#ffffff", labelcolor="#ffffff")
    for spine in axes.spines.values():
        spine.set_edgecolor("#ffffff")
    plt.show()


def plot_basic_SIR_param_comp(basic_SIR_data_1, basic_SIR_data_2):
    plt.style.use("fivethirtyeight")
    plt.rcParams.update({"font.size": 16})

    np.set_printoptions(suppress=True)
    S_1, I_1, R_1 = (
        basic_SIR_data_1[0, :],
        basic_SIR_data_1[1, :],
        basic_SIR_data_1[2, :],
    )
    S_2, I_2, R_2 = (
        basic_SIR_data_2[0, :],
        basic_SIR_data_2[1, :],
        basic_SIR_data_2[2, :],
    )
    t = np.linspace(0, 150, 150)
    max_x, max_y = find_max_and_argmax(t, I_1)
    max_x_2, max_y_2 = find_max_and_argmax(t, I_2)
    figure = plt.figure(facecolor="white")
    # figure.patch.set_alpha(0)
    axes = plt.axes()
    axes.set_facecolor("#ffffff")
    axes.tick_params(color="black", labelcolor="black")
    for spine in axes.spines.values():
        spine.set_edgecolor("#ffffff")
    plt.text(
        max(t),
        max(S_1) * 1.05,
        "© M. Urban, J. Jodłowska, J. Balbus, K. Kubica",
        ha="right",
        va="top",
    )
    figure.set_figwidth(12)
    figure.set_figheight(8)
    plt.plot(t, S_1, color=colors[0], label="Susceptible (5 days)")
    plt.plot(t, I_1, color=colors[4], label="Infectious (5 days)")
    plt.plot(t, R_1, color=colors[6], label="Recovered (5 days)")
    max_infectious_text = (
        "$I_{\\mathrm{max}}(t) = "
        + str(int(round(max_y, 0)))
        + "\\;\\mathrm{at}\\;t="
        + str(int(round(max_x, 0)))
        + "$"
    )
    r_tmax_text = (
        "$R\\left({t_\\mathrm{max}}\\right) = " + str(int(round(R_1[-1], 0))) + "$"
    )
    plt.plot(t, S_2, "--", color=colors[1], label="Susceptible (7 days)")
    plt.plot(t, I_2, "--", color=colors[5], label="Infectious (7 days)")
    plt.plot(t, R_2, "--", color=colors[7], label="Recovered (7 days)")
    max_infectious_2_text = (
        "$I_{\\mathrm{max}}(t) = "
        + str(int(round(max_y_2, 0)))
        + "\\;\\mathrm{at}\\;t="
        + str(int(round(max_x_2, 0)))
        + "$"
    )
    r_tmax_2_text = (
        "$R\\left({t_\\mathrm{max}}\\right) = " + str(int(round(R_2[-1], 0))) + "$"
    )
    additional_text = (max_infectious_text, r_tmax_text, "")
    plt.ticklabel_format(axis="y", useOffset=False, style="Plain")
    plt.xlabel("Time [days]")
    plt.ylabel("Number of people")
    handles, _ = plt.gca().get_legend_handles_labels()
    for text in additional_text:
        handles.append(mpatches.Patch(color="none", label=text))

    for _ in range(3, 6):
        handles.append(handles.pop(3))

    handles.append(mpatches.Patch(color="none", label=max_infectious_2_text))
    handles.append(mpatches.Patch(color="none", label=r_tmax_2_text))

    plt.legend(handles=handles, framealpha=1, loc="center left")
    plt.tight_layout()
    plt.savefig(
        "C:/Users/work/Desktop/optymalizacja-figures/fig_4.tif",
        facecolor="white",
        dpi=300,
    )
    plt.savefig(
        "C:/Users/work/Desktop/optymalizacja-figures/fig_4.pdf", facecolor="white"
    )
    plt.show()


if __name__ == "__main__":
    if platform.system() == "Windows":
        import ctypes

        if platform.release() == "7":
            ctypes.windll.user32.SetProcessDPIAware()
        elif float(platform.release()) >= 8:
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
    # path_1 = "C:\\Users\\work\\Desktop\\Noto_Sans\\NotoSans-Bold.ttf"
    # path = path_1
    # fe = fm.FontEntry(
    #     fname=path,
    #     name="NotoSans-Bold",
    # )
    # fe = fm.FontEntry(
    #     fname=path,
    #     name="lmroman10",
    # )
    # fm.fontManager.ttflist.insert(0, fe)
    # plt.rcParams["font.family"] = fe.name
    # plt.rcParams.update(
    #     {
    #         "text.usetex": True,
    #         "font.family": "serif",
    #         "font.serif": ["NotoSans-Regular"],
    #     }
    # )
    # matplotlib.rcParams[
    #     "text.latex.preamble"
    # ] = r"""\usepackage{siunitx}
    #     \usepackage[MeX]{polski}
    #     \usepackage[utf8]{inputenc}
    #     \usepackage[english,polish]{babel}
    #     \sisetup{detect-all}"""
    (
        basic_SIR_data,
        basic_SIR_data_2,
        vaccination_comparison_data_50_71,
        vaccination_comparison_data_50_91,
        _,
        _,
    ) = prepare_data_for_plots()
    plot_basic_SIR(basic_SIR_data)
    plot_SIR_with_vaccination_comparison(
        vaccination_comparison_data_50_71, vaccination_comparison_data_50_91
    )
    # plot_SIR_with_multiwave_comparison()
    plot_basic_SIR_param_comp(basic_SIR_data, basic_SIR_data_2)
