from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk,
)
import utils.plots as plot
import utils.mathematics as mat


class Toolbar(NavigationToolbar2Tk):
    def __init__(self, *args, **kwargs):
        super(Toolbar, self).__init__(*args, **kwargs)


def draw_fig(canvas, fig, canvas_toolbar):
    """Draws the figure on the figure_canvas_agg

    Args:
        canvas (tk.Canvas): The canvas on which the figure is drawn
        fig (matplotlib.figure): The figure to be drawn
        canvas_toolbar (Toolbar): The toolbar of the canvas

    Returns:
        figure_canvas_agg (FigureCanvasTkAgg): The figure canvas
    """
    if canvas.children:
        for child in canvas.winfo_children():
            child.destroy()
    if canvas_toolbar.children:
        for child in canvas_toolbar.winfo_children():
            child.destroy()
    figure_canvas_agg = FigureCanvasTkAgg(fig, canvas)
    toolbar = Toolbar(figure_canvas_agg, canvas_toolbar)
    toolbar.update()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=True)
    return figure_canvas_agg


def update_canvas(canvas, fig):
    """Updates the figure_canvas_agg with the new figure

    Args:
        canvas (tk.Canvas): The canvas on which the figure is drawn
        fig (matplotlib.figure): The figure to be drawn

    Returns:
        figure_canvas_agg (FigureCanvasTkAgg): The figure canvas
    """
    figure_canvas_agg = draw_fig(canvas, fig)
    return figure_canvas_agg


def delete_figure_agg(figure_canvas_agg):
    """Deletes the figure_canvas_agg content

    Args:
        figure_canvas_agg (FigureCanvasTkAgg): The figure_canvas_agg from which
            the content is deleted
    """
    for item in figure_canvas_agg.get_tk_widget().find_all():
        figure_canvas_agg.get_tk_widget().delete(item)
    figure_canvas_agg.get_tk_widget().pack_forget()


def create_updated_fig_SIR(
    susceptible,
    infectious,
    recovered,
    t_1,
    beta,
    gamma,
    with_multiwave,
    a,
    t_3,
    already_plotted=False,
):
    """Creates a new figure with the updated SIR values

    Args:
        susceptible (int): The susceptible population
        infectious (int): The infectious population
        recovered (int): The recovered population
        t_1 (float): The time of the simulation
        beta (float): The infection rate
        gamma (float): The recovery rate
        with_multiwave (bool): indicates if recovered people lose immunity
        a (float): proportion of recovered people who lose immunity
        t_3 (int): time of the start of immunity loss

    Returns:
        fig (matplotlib.figure): The figure with the updated SIR values
    """
    sol = mat.solve_SIR(
        (0, t_1),
        [susceptible, infectious, recovered],
        with_multiwave,
        t_3,
        beta=beta,
        gamma=gamma,
        a=a,
    )
    fig = plot.plot_SIR(sol, sol.t, beta, gamma, already_plotted)
    return fig


def create_updated_fig_SIR_with_vaccination(
    susceptible,
    infectious,
    recovered,
    t_1,
    beta,
    gamma,
    eff,
    vac_rate,
    t_start,
    t_end,
    with_multiwave,
    a,
    t_3,
    already_plotted=False,
):
    y0 = [susceptible, infectious, recovered]

    sol_v = mat.solve_SIR_with_vaccination(
        [0, t_1],
        y0,
        t_start,
        t_end,
        with_multiwave,
        t_3,
        beta=beta,
        gamma=gamma,
        eff=eff,
        vac_rate=vac_rate,
        a=a,
    )
    fig = plot.plot_SIR(sol_v, sol_v.t, beta, gamma, already_plotted)
    return fig
