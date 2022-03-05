import platform
import PySimpleGUI as sg
import os
import importlib

from utils.drawing import (
    create_updated_fig_SIR,
    create_updated_fig_SIR_with_vaccination,
    delete_figure_agg,
    draw_fig,
)
from utils.icon import icon
from utils.gui import layout
from utils.mathematics import solve_SIR
from utils.plots import plot_SIR
from utils.validation import (
    validate_positive_float_input,
    validate_positive_int_input,
    validate_pos_float_under_one,
)

if platform.system() == "Windows":
    import ctypes

    if platform.release() == "7":
        ctypes.windll.user32.SetProcessDPIAware()
    elif float(platform.release()) >= 8:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)

if "_PYIBoot_SPLASH" in os.environ and importlib.util.find_spec("pyi_splash"):
    import pyi_splash

    pyi_splash.close()

if __name__ == "__main__":
    icon = icon
else:
    icon = "icon.ico"


def set_scale(scale):
    root = sg.tk.Tk()
    root.tk.call("tk", "scaling", scale)
    root.destroy()


# Default values and initial plot
beta = 4e-7
gamma = 0.2
y0 = [1e6, 1, 0]

# Solve the ODEs
sol = solve_SIR((0, 150), y0, beta=beta, gamma=gamma, with_multiwave=False, a=0, t_3=30)

# Plot the solution
fig = plot_SIR(sol, sol.t, beta, gamma)
del plot_SIR
set_scale(fig.dpi / 75)

# GUI
sg.theme("DarkGrey5")
with_vaccinations = False
with_multiwave = False
already_plotted = True


window = sg.Window(
    title="SIR model",
    layout=layout,
    element_justification="c",
    icon=icon,
    resizable=True,
    finalize=True,
)

# Insert initial figure into canvas
fig_agg = draw_fig(window["-CANVAS-"].TKCanvas, fig, window["-TOOLBAR-"].TKCanvas)


# Main loop
while True:
    event, values = window.read()
    if event in (None, "Exit"):
        try:
            os.remove(".fig.pkl")
        except (FileNotFoundError, OSError):
            pass
        window.close()
        break
    if event == "with_vaccinations":
        with_vaccinations = not with_vaccinations
        window["vaccination_rate_row"].update(visible=with_vaccinations)
        window["vaccination_eff_row"].update(visible=with_vaccinations)
        window["vaccination_start_row"].update(visible=with_vaccinations)
        window["vaccination_end_row"].update(visible=with_vaccinations)
        window.visibility_changed()
        window.refresh()
    if event == "with_multiwave":
        with_multiwave = not with_multiwave
        window["sw_a_row"].update(visible=with_multiwave)
        window["sw_start_row"].update(visible=with_multiwave)
        window.visibility_changed()
        window.refresh()
    if event == "-CLEAR-":
        delete_figure_agg(fig_agg)
        try:
            os.remove(".fig.pkl")
        except (FileNotFoundError, OSError):
            pass
        already_plotted = False

    if event == "-DRAW-" and with_vaccinations:
        delete_figure_agg(fig_agg)
        try:
            validate_positive_float_input(values["susceptible"], "susceptible")
            validate_positive_float_input(values["infectious"], "infectious")
            validate_positive_float_input(values["recovered"], "recovered")
            validate_positive_float_input(values["beta"], "beta")
            validate_positive_int_input(values["recovery_time"], "recovery time")
            validate_positive_int_input(values["duration"], "duration")
            validate_pos_float_under_one(values["sw_a"], "a")
            validate_positive_int_input(values["sw_start"], "immunity loss start")
            validate_positive_float_input(
                values["vaccination_rate"], "vaccination rate"
            )
            validate_pos_float_under_one(values["vaccination_eff"], "vaccination eff")
            validate_positive_int_input(
                values["vaccination_start"], "vaccination start"
            )
            validate_positive_int_input(values["vaccination_end"], "vaccination end")

            S = int(float(values["susceptible"]))
            I = int(float(values["infectious"]))
            R = int(float(values["recovered"]))

            t_1 = int(values["duration"])
            beta = float(values["beta"])
            gamma = 1 / int(values["recovery_time"])

            sw_a = float(values["sw_a"])
            sw_start = int(values["sw_start"])

            vac_rate = int(float(values["vaccination_rate"]))
            vac_eff = float(values["vaccination_eff"])
            vac_start = int(values["vaccination_start"])
            vac_end = int(values["vaccination_end"])

            if already_plotted:
                figure = create_updated_fig_SIR_with_vaccination(
                    S,
                    I,
                    R,
                    t_1,
                    beta,
                    gamma,
                    vac_eff,
                    vac_rate,
                    vac_start,
                    vac_end,
                    with_multiwave,
                    sw_a,
                    sw_start,
                    already_plotted,
                )
                fig_agg = draw_fig(
                    window["-CANVAS-"].TKCanvas, figure, window["-TOOLBAR-"].TKCanvas
                )
            else:
                figure = create_updated_fig_SIR_with_vaccination(
                    S,
                    I,
                    R,
                    t_1,
                    beta,
                    gamma,
                    vac_eff,
                    vac_rate,
                    vac_start,
                    vac_end,
                    with_multiwave,
                    sw_a,
                    sw_start,
                )
                fig_agg = draw_fig(
                    window["-CANVAS-"].TKCanvas, figure, window["-TOOLBAR-"].TKCanvas
                )
                already_plotted = True
        except ValueError as e:
            sg.popup_error(
                "Invalid input:\n" + str(e), title="Invalid parameters", icon=icon
            )
    elif event == "-DRAW-":
        delete_figure_agg(fig_agg)
        try:
            validate_positive_float_input(values["susceptible"], "susceptible")
            validate_positive_float_input(values["infectious"], "infectious")
            validate_positive_float_input(values["recovered"], "recovered")
            validate_positive_float_input(values["beta"], "beta")
            validate_positive_int_input(values["recovery_time"], "recovery time")
            validate_positive_int_input(values["duration"], "duration")
            validate_pos_float_under_one(values["sw_a"], "a")
            validate_positive_int_input(values["sw_start"], "immunity loss start")

            susceptible = int(float(values["susceptible"]))
            infectious = int(float(values["infectious"]))
            recovered = int(float(values["recovered"]))

            t_1 = int(values["duration"])
            beta = float(values["beta"])
            gamma = 1 / int(values["recovery_time"])

            sw_a = float(values["sw_a"])
            sw_start = int(values["sw_start"])

            if already_plotted:
                figure = create_updated_fig_SIR(
                    susceptible,
                    infectious,
                    recovered,
                    t_1,
                    beta,
                    gamma,
                    with_multiwave,
                    sw_a,
                    sw_start,
                    already_plotted,
                )
                fig_agg = draw_fig(
                    window["-CANVAS-"].TKCanvas, figure, window["-TOOLBAR-"].TKCanvas
                )
            else:
                figure = create_updated_fig_SIR(
                    susceptible,
                    infectious,
                    recovered,
                    t_1,
                    beta,
                    gamma,
                    with_multiwave,
                    sw_a,
                    sw_start,
                )
                fig_agg = draw_fig(
                    window["-CANVAS-"].TKCanvas, figure, window["-TOOLBAR-"].TKCanvas
                )
                already_plotted = True
        except ValueError as e:
            sg.popup_error(
                "Invalid input:\n" + str(e), title="Invalid parameters", icon=icon
            )
