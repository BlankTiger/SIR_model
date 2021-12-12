import PySimpleGUI as sg


with_vaccinations = False
sg.theme("DarkGrey5")


def create_stretch():
    return sg.Text(
        font="_ 1",
        text="",
        background_color=None,
        pad=(0, 0),
        expand_x=True,
    )


def create_col_for_row(elem):
    return sg.Column([[elem]], pad=(0, 0))


def create_row(col_1, col_2, col_3, row_visible, row_key=""):
    return sg.Column(
        [[col_1, col_2, col_3]],
        pad=(0, 0),
        key=row_key,
        visible=row_visible,
        expand_x=True,
    )


def create_layout(*elements):
    return [[*elements]]


susceptible_text = create_col_for_row(
    sg.Text(text="Susceptible", size=(14, 1))
)
susceptible_value = create_col_for_row(
    sg.InputText(
        "10000", size=(20, 1), justification="right", key="susceptible"
    )
)

infected_text = create_col_for_row(sg.Text(text="Infected", size=(14, 1)))
infected_value = create_col_for_row(
    sg.InputText(
        "10",
        size=(20, 1),
        justification="right",
        key="infected",
    )
)

recovered_text = create_col_for_row(sg.Text(text="Recovered", size=(14, 1)))
recovered_value = create_col_for_row(
    sg.InputText(
        "0",
        size=(20, 1),
        justification="right",
        key="recovered",
    )
)

duration_text = create_col_for_row(sg.Text(text="Duration", size=(14, 1)))
duration_value = create_col_for_row(
    sg.InputText(
        "100",
        size=(20, 1),
        justification="right",
        key="duration",
    )
)

beta_text = create_col_for_row(sg.Text(text="β", size=(14, 1)))
beta_value = create_col_for_row(
    sg.InputText(
        "0.25",
        size=(20, 1),
        justification="right",
        key="beta",
    )
)

recovery_time_text = create_col_for_row(
    sg.Text(text="Recovery time", size=(14, 1))
)
recovery_time_value = create_col_for_row(
    sg.InputText(
        "8",
        size=(20, 1),
        justification="right",
        key="recovery_time",
    )
)

vac_rate_text = create_col_for_row(
    sg.Text(text="Vaccination rate", size=(14, 1))
)
vac_rate_value = create_col_for_row(
    sg.InputText(
        "250",
        size=(20, 1),
        justification="right",
        key="vaccination_rate",
    )
)

vac_eff_text = create_col_for_row(
    sg.Text(text="Vaccination eff", size=(14, 1))
)
vac_eff_value = create_col_for_row(
    sg.InputText(
        "0.9",
        size=(20, 1),
        justification="right",
        key="vaccination_eff",
    )
)

vac_start_text = create_col_for_row(
    sg.Text(text="Vaccination start", size=(14, 1))
)
vac_start_value = create_col_for_row(
    sg.InputText(
        "30",
        size=(20, 1),
        justification="right",
        key="vaccination_start",
    )
)

vac_end_text = create_col_for_row(
    sg.Text(text="Vaccination end", size=(14, 1))
)
vac_end_value = create_col_for_row(
    sg.InputText(
        "50",
        size=(20, 1),
        justification="right",
        key="vaccination_end",
    )
)


with_vaccinations_row = create_row(
    create_stretch(),
    sg.Button("With Vaccinations", key="with_vaccinations"),
    create_stretch(),
    True,
)

susceptible_row = create_row(
    susceptible_text,
    create_stretch(),
    susceptible_value,
    True,
)

infected_row = create_row(
    infected_text,
    create_stretch(),
    infected_value,
    True,
)

recovered_row = create_row(
    recovered_text,
    create_stretch(),
    recovered_value,
    True,
)

duration_row = create_row(
    duration_text,
    create_stretch(),
    duration_value,
    True,
)

beta_row = create_row(
    beta_text,
    create_stretch(),
    beta_value,
    True,
)

recovery_time_row = create_row(
    recovery_time_text,
    create_stretch(),
    recovery_time_value,
    True,
)

vac_rate_row = create_row(
    vac_rate_text,
    create_stretch(),
    vac_rate_value,
    False,
    "vaccination_rate_row",
)

vac_eff_row = create_row(
    vac_eff_text,
    create_stretch(),
    vac_eff_value,
    False,
    "vaccination_eff_row",
)

vac_start_row = create_row(
    vac_start_text,
    create_stretch(),
    vac_start_value,
    False,
    "vaccination_start_row",
)

vac_end_row = create_row(
    vac_end_text,
    create_stretch(),
    vac_end_value,
    False,
    "vaccination_end_row",
)

draw_row = create_row(
    create_stretch(),
    sg.Button("Draw", key="-DRAW-", size=(15, 2)),
    create_stretch(),
    True,
)

column1 = sg.Column(
    [
        [with_vaccinations_row],
        [susceptible_row],
        [infected_row],
        [recovered_row],
        [duration_row],
        [beta_row],
        [recovery_time_row],
        [vac_rate_row],
        [vac_eff_row],
        [vac_start_row],
        [vac_end_row],
        [draw_row],
    ],
    element_justification="c",
    expand_x=True,
)

column2 = sg.Column(
    [
        [
            sg.Canvas(
                key="-CANVAS-",
                size=(1000, 800),
                background_color="white",
                expand_y=True,
                expand_x=True,
            )
        ],
        [
            sg.Canvas(
                key="-TOOLBAR-",
                size=(1000, 30),
                background_color="white",
                expand_x=True,
            )
        ],
    ],
    expand_y=True,
    expand_x=True,
)

layout = create_layout(column1, column2)