# #!Scripts/python
# activate_this_file = "Scripts/activate_this.py"
# exec(
#   compile(open(activate_this_file, "rb").read(), activate_this_file, "exec"),
#   dict(__file__=activate_this_file),
# )
__requires__ = ["matplotlib==3.4.1", "PySimpleGUI==4.55.1"]
import pkg_resources
import PySimpleGUI as sg
import numpy as np
from scipy.integrate import odeint
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk,
)
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.patches as mpatches
import platform


if platform.system() == "Windows":
    import ctypes

    if platform.release() == "7":
        ctypes.windll.user32.SetProcessDPIAware()
    elif platform.release() == "8" or platform.release() == "10":
        ctypes.windll.shcore.SetProcessDpiAwareness(1)


matplotlib.use("TkAgg")


def SIR(y, t, beta, gamma):
    """
    Function modeling a SIR model.

    Args:
        t: time
        y: vector of the variables

    Returns:
        dydt: vector of the derivatives of the variables
    """
    S, I, R = y
    N = S + I + R
    dydt = [-beta * S * I / N, beta * S * I / N - gamma * I, gamma * I]
    return dydt


def plot_SIR(y, t, beta, gamma, N):
    """
    Function to plot the SIR model.

    Args:
        S: vector of susceptible individuals
        I: vector of infected individuals
        R: vector of recovered individuals
        t: time
        a: rate of recovery
        r: rate of infection
    """
    plt.gcf()
    plt.style.use("fivethirtyeight")
    # plt.style.use("dark_background")
    plt.rcParams.update({"font.size": 10})
    np.set_printoptions(suppress=True)
    S, I, R = y[:, 0], y[:, 1], y[:, 2]
    figure = plt.figure()
    figure.set_dpi(110)
    figure.set_figwidth(768 / 110)
    figure.set_figheight(576 / 110)
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


#################
# Default values and initial plot
#################
beta = 0.5
gamma = 0.05

S0 = 1000000
I0 = 10
R0 = 0
y0 = [S0, I0, R0]

t_1 = 100
t_values = np.linspace(0, t_1, 100)

# Solve the ODEs
y_values = odeint(SIR, y0, t_values, args=(beta, gamma))

# Plot the solution
fig = plot_SIR(y_values, t_values, beta, gamma, S0 + I0 + R0)
#################
# GUI
#################
sg.theme("DarkGrey5")

column1 = sg.Column(
    [
        [
            sg.Text("Susceptible", size=(10, 1)),
            sg.Stretch(),
            sg.InputText(
                f"{int(S0)}",
                size=(20, 1),
                justification="right",
                key="susceptible",
            ),
        ],
        [
            sg.Text("Infected", size=(10, 1)),
            sg.Stretch(),
            sg.InputText(
                f"{int(I0)}",
                size=(20, 1),
                justification="right",
                key="infected",
            ),
        ],
        [
            sg.Text("Recovered", size=(10, 1)),
            sg.Stretch(),
            sg.InputText(
                f"{int(R0)}",
                size=(20, 1),
                justification="right",
                key="recovered",
            ),
        ],
        [
            sg.Text("Duration", size=(10, 1)),
            sg.Stretch(),
            sg.InputText(
                f"{t_1}", size=(20, 1), justification="right", key="duration"
            ),
        ],
        [
            sg.Text("β", size=(10, 1)),
            sg.Stretch(),
            sg.InputText(
                f"{beta}",
                size=(20, 1),
                justification="right",
                key="beta",
            ),
        ],
        [
            sg.Text("Recovery time", size=(13, 1)),
            sg.Stretch(),
            sg.InputText(
                f"{round(1/gamma, 3)}",
                size=(20, 1),
                justification="right",
                key="recovery_time",
            ),
        ],
        [sg.Button("Draw", key="-DRAW-", size=(15, 2))],
    ],
    element_justification="c",
    expand_x=True,
)

column2 = sg.Column(
    [
        [
            sg.Canvas(
                key="-CANVAS-",
                size=(768, 576),
                background_color="white",
                expand_y=True,
                expand_x=True,
            )
        ],
        [
            sg.Canvas(
                key="-TOOLBAR-",
                size=(768, 30),
                background_color="white",
                expand_x=True,
            )
        ],
    ],
    expand_y=True,
    expand_x=True,
)

window = sg.Window(
    title="SIR model",
    layout=[
        [
            column1,
            column2,
        ],
    ],
    element_justification="c",
    resizable=True,
    finalize=True,
)
window.TKroot.tk.call("tk", "scaling", 3)


class Toolbar(NavigationToolbar2Tk):
    def __init__(self, *args, **kwargs):
        super(Toolbar, self).__init__(*args, **kwargs)


#################
# Drawing functions
#################
def draw_fig(canvas, fig, canvas_toolbar):
    if canvas.children:
        for child in canvas.winfo_children():
            child.destroy()
    if canvas_toolbar.children:
        for child in canvas_toolbar.winfo_children():
            child.destroy()
    figure_canvas_agg = FigureCanvasTkAgg(fig, canvas)
    figure_canvas_agg.draw()
    toolbar = Toolbar(figure_canvas_agg, canvas_toolbar)
    toolbar.update()
    figure_canvas_agg.get_tk_widget().pack(
        side="top", fill="both", expand=True
    )
    return figure_canvas_agg


def update_canvas(canvas, fig):
    figure_canvas_agg = draw_fig(canvas, fig)
    return figure_canvas_agg


def delete_figure_agg(figure_canvas_agg):
    for item in figure_canvas_agg.get_tk_widget().find_all():
        figure_canvas_agg.get_tk_widget().delete(item)
    figure_canvas_agg.get_tk_widget().pack_forget()


def create_updated_fig(susceptible, infected, recovered, beta, gamma, t_1):
    N = susceptible + infected + recovered
    t_values = np.linspace(0, t_1, int(t_1) * 100)
    y_values = odeint(
        SIR, [susceptible, infected, recovered], t_values, args=(beta, gamma)
    )
    fig = plot_SIR(y_values, t_values, beta, gamma, N)
    return fig


#################
# Validation functions
#################
def validate_positive_int_input(value):
    try:
        value = int(value)
        if value < 0:
            raise ValueError
        return True
    except ValueError:
        return False


def validate_positive_float_input(value):
    try:
        value = float(value)
        if value < 0:
            raise ValueError
        return True
    except ValueError:
        return False


# Insert initial figure into canvas
fig_agg = draw_fig(
    window["-CANVAS-"].TKCanvas, fig, window["-TOOLBAR-"].TKCanvas
)


#################
# Main loop
#################
while True:
    event, values = window.read()
    if event in (None, "Exit"):
        break
    if event == "-DRAW-":
        delete_figure_agg(fig_agg)
        if (
            validate_positive_int_input(values["susceptible"])
            and validate_positive_int_input(values["infected"])
            and validate_positive_int_input(values["recovered"])
            and validate_positive_float_input(values["beta"])
            and validate_positive_float_input(values["recovery_time"])
            and validate_positive_float_input(values["duration"])
        ):
            susceptible = float(values["susceptible"])
            infected = float(values["infected"])
            recovered = float(values["recovered"])

            t_1 = float(values["duration"])
            beta = float(values["beta"])
            gamma = 1 / float(values["recovery_time"])
            fig = create_updated_fig(
                susceptible, infected, recovered, beta, gamma, t_1
            )
            fig_agg = draw_fig(
                window["-CANVAS-"].TKCanvas, fig, window["-TOOLBAR-"].TKCanvas
            )
        else:
            sg.popup_error("Invalid input", title="Error")
