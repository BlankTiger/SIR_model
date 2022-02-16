__requires__ = ["matplotlib==3.4.1", "PySimpleGUI==4.55.1"]
import platform

from numpy import linspace
import pkg_resources
import PySimpleGUI as sg

from utils.drawing import (
    create_updated_fig_SIR,
    create_updated_fig_SIR_with_vaccination,
    delete_figure_agg,
    draw_fig,
)
from utils.gui import layout
from utils.mathematics import solve_SIR
from utils.plots import plot_SIR
from utils.validation import (
    validate_positive_float_input,
    validate_positive_int_input,
)

if platform.system() == "Windows":
    import ctypes

    if platform.release() == "7":
        ctypes.windll.user32.SetProcessDPIAware()
    elif float(platform.release()) >= 8:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)


# Default values and initial plot
beta = 25e-6
gamma = 0.125

S0 = 10000
I0 = 10
R0 = 0
y0 = [S0, I0, R0]

t_1 = 100
t_values = linspace(0, t_1, 100)

# Solve the ODEs
y_values = solve_SIR((0, t_1), y0, beta, gamma, False, 0, 0, t_values=t_values)

# Plot the solution
fig = plot_SIR(y_values, t_values, beta, gamma)

# GUI
sg.theme("DarkGrey5")
with_vaccinations = False
with_multiwave = False


window = sg.Window(
    title="SIR model",
    layout=layout,
    element_justification="c",
    resizable=True,
    finalize=True,
)
# this scaling is not needed in newer versions of python I think
# window.TKroot.tk.call("tk", "scaling", 3)


# Insert initial figure into canvas
fig_agg = draw_fig(window["-CANVAS-"].TKCanvas, fig, window["-TOOLBAR-"].TKCanvas)


# Main loop
while True:
    event, values = window.read()
    if event in (None, "Exit"):
        break
    if event == "with_vaccinations":
        with_vaccinations = not with_vaccinations
        window["vaccination_rate_row"].update(visible=with_vaccinations)
        window["vaccination_eff_row"].update(visible=with_vaccinations)
        window["vaccination_start_row"].update(visible=with_vaccinations)
        window["vaccination_end_row"].update(visible=with_vaccinations)
        window.visibility_changed()
    if event == "with_multiwave":
        with_multiwave = not with_multiwave
        window["sw_a_row"].update(visible=with_multiwave)
        window["sw_start_row"].update(visible=with_multiwave)
        window.visibility_changed()
    if event == "-DRAW-" and with_vaccinations:
        delete_figure_agg(fig_agg)
        if (
            validate_positive_int_input(values["susceptible"])
            and validate_positive_int_input(values["infectious"])
            and validate_positive_int_input(values["recovered"])
            and validate_positive_float_input(values["beta"])
            and validate_positive_float_input(values["recovery_time"])
            and validate_positive_float_input(values["duration"])
            and validate_positive_float_input(values["sw_a"])
            and validate_positive_int_input(values["sw_start"])
            and validate_positive_int_input(values["vaccination_rate"])
            and validate_positive_float_input(values["vaccination_eff"])
            and validate_positive_int_input(values["vaccination_start"])
            and validate_positive_int_input(values["vaccination_end"])
        ):
            susceptible = float(values["susceptible"])
            infectious = float(values["infectious"])
            recovered = float(values["recovered"])

            t_1 = float(values["duration"])
            beta = float(values["beta"])
            gamma = 1 / float(values["recovery_time"])

            sw_a = float(values["sw_a"])
            sw_start = int(values["sw_start"])

            vaccination_rate = int(values["vaccination_rate"])
            vaccination_eff = float(values["vaccination_eff"])
            vaccination_start = int(values["vaccination_start"])
            vaccination_end = int(values["vaccination_end"])

            fig = create_updated_fig_SIR_with_vaccination(
                susceptible,
                infectious,
                recovered,
                t_1,
                beta,
                gamma,
                vaccination_rate,
                vaccination_eff,
                vaccination_start,
                vaccination_end,
                with_multiwave,
                sw_a,
                sw_start,
            )
            fig_agg = draw_fig(
                window["-CANVAS-"].TKCanvas, fig, window["-TOOLBAR-"].TKCanvas
            )
        else:
            sg.popup_error("Invalid input", title="Error")
    elif event == "-DRAW-":
        delete_figure_agg(fig_agg)
        if (
            validate_positive_int_input(values["susceptible"])
            and validate_positive_int_input(values["infectious"])
            and validate_positive_int_input(values["recovered"])
            and validate_positive_float_input(values["beta"])
            and validate_positive_float_input(values["recovery_time"])
            and validate_positive_float_input(values["duration"])
            and validate_positive_float_input(values["sw_a"])
            and validate_positive_int_input(values["sw_start"])
        ):
            susceptible = float(values["susceptible"])
            infectious = float(values["infectious"])
            recovered = float(values["recovered"])

            t_1 = float(values["duration"])
            beta = float(values["beta"])
            gamma = 1 / float(values["recovery_time"])

            sw_a = float(values["sw_a"])
            sw_start = int(values["sw_start"])

            fig = create_updated_fig_SIR(
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
                window["-CANVAS-"].TKCanvas, fig, window["-TOOLBAR-"].TKCanvas
            )
        else:
            sg.popup_error("Invalid input", title="Error")
