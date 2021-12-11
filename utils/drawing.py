from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk,
)
from .plots import plot_SIR, plot_SIR_with_vaccination
from .mathematics import solve_SIR, solve_SIR_with_vaccination
from numpy import linspace


class Toolbar(NavigationToolbar2Tk):
    def __init__(self, *args, **kwargs):
        super(Toolbar, self).__init__(*args, **kwargs)


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


def create_updated_fig_SIR(susceptible, infected, recovered, t_1, beta, gamma):
    t_values = linspace(0, t_1, int(t_1) * 10)
    y_values = solve_SIR(
        [susceptible, infected, recovered], t_values, beta, gamma
    )
    fig = plot_SIR(y_values, t_values, beta, gamma)
    return fig


def create_updated_fig_SIR_with_vaccination(
    susceptible,
    infected,
    recovered,
    t_1,
    beta,
    gamma,
    vaccination_rate,
    eff,
    t_start,
    t_end,
):
    t_values = linspace(0, t_1, int(t_1) * 10)
    y_values = solve_SIR(
        [susceptible, infected, recovered], t_values, beta, gamma
    )
    y_with_vac_values = solve_SIR_with_vaccination(
        [susceptible, infected, recovered],
        t_values,
        beta,
        gamma,
        vaccination_rate,
        eff,
        t_start,
        t_end,
    )
    fig = plot_SIR_with_vaccination(
        y_values, y_with_vac_values, t_values, beta, gamma
    )
    return fig
