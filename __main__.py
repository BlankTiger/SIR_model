import PySimpleGUI as sg
import numpy as np
from scipy.integrate import odeint
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sir_model.model import SIR, plot_SIR

#################
# Default values and initial plot
#################
r = 0.56
a = 0.05

S0 = 1000000
I0 = 10
R0 = 0
N = S0 + I0 + R0
S0 /= N
I0 /= N
R0 /= N
y0 = [S0, I0, R0]

t_0 = 0
t_1 = 100
t_values = np.linspace(t_0, t_1, 100)

# Solve the ODEs
y_values = odeint(SIR, y0, t_values, args=(a, r))

# Plot the solution
fig = plot_SIR(y_values, t_values, a, r, N)

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
                f"{int(S0*N)}",
                size=(20, 1),
                justification="right",
                key="susceptible",
            ),
        ],
        [
            sg.Text("Infected", size=(10, 1)),
            sg.Stretch(),
            sg.InputText(
                f"{int(I0*N)}",
                size=(20, 1),
                justification="right",
                key="infected",
            ),
        ],
        [
            sg.Text("Recovered", size=(10, 1)),
            sg.Stretch(),
            sg.InputText(
                f"{int(R0*N)}",
                size=(20, 1),
                justification="right",
                key="recovered",
            ),
        ],
        [
            sg.Text("Start time", size=(10, 1)),
            sg.Stretch(),
            sg.InputText(
                f"{t_0}", size=(20, 1), justification="right", key="start_time"
            ),
        ],
        [
            sg.Text("Stop time", size=(10, 1)),
            sg.Stretch(),
            sg.InputText(
                f"{t_1}", size=(20, 1), justification="right", key="stop_time"
            ),
        ],
        [
            sg.Text("a", size=(10, 1)),
            sg.Stretch(),
            sg.InputText(f"{a}", size=(20, 1), justification="right", key="a"),
        ],
        [
            sg.Text("r", size=(10, 1)),
            sg.Stretch(),
            sg.InputText(f"{r}", size=(20, 1), justification="right", key="r"),
        ],
        [sg.Button("Draw", key="-DRAW-", size=(15, 2))],
    ],
    element_justification="c",
    expand_x=True,
)

column2 = sg.Column(
    [[sg.Canvas(key="-CANVAS-", size=(800, 500), background_color="white")]],
    element_justification="right",
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
    grab_anywhere=True,
)
window["-CANVAS-"].expand(True, True)


#################
# Drawing functions
#################
def draw_fig(canvas, fig):
    figure_canvas_agg = FigureCanvasTkAgg(fig, canvas)
    figure_canvas_agg.draw()
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
    return figure_canvas_agg


def create_updated_fig(susceptible, infected, recovered, a, r, t_0, t_1):
    N = susceptible + infected + recovered
    susceptible /= N
    infected /= N
    recovered /= N
    t_values = np.linspace(t_0, t_1, int(t_1 - t_0) * 100)
    y_values = odeint(
        SIR, [susceptible, infected, recovered], t_values, args=(a, r)
    )
    fig = plot_SIR(y_values, t_values, a, r, N)
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
fig_agg = draw_fig(window["-CANVAS-"].TKCanvas, fig)


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
            and validate_positive_float_input(values["a"])
            and validate_positive_float_input(values["r"])
            and validate_positive_float_input(values["start_time"])
            and validate_positive_float_input(values["stop_time"])
        ):
            susceptible = float(values["susceptible"])
            infected = float(values["infected"])
            recovered = float(values["recovered"])

            if susceptible + infected + recovered > 0 and float(
                values["start_time"]
            ) < float(values["stop_time"]):
                t_0 = float(values["start_time"])
                t_1 = float(values["stop_time"])
                a = float(values["a"])
                r = float(values["r"])
                fig = create_updated_fig(
                    susceptible, infected, recovered, a, r, t_0, t_1
                )
                fig_agg = update_canvas(window["-CANVAS-"].TKCanvas, fig)
            else:
                sg.popup_error("Invalid input")
        else:
            sg.popup_error("Invalid input", title="Error")
