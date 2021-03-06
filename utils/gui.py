import PySimpleGUI as sg


with_vaccinations = False
sg.theme("DarkGrey5")


def create_stretch():
    """Create a stretch element

    Returns:
        sg.Text: stretch element for layout
    """
    return sg.Text(
        font="_ 1", text="", background_color=None, pad=(0, 0), expand_x=True
    )


def create_col_for_row(elem):
    """Create a column for a row

    Args:
        elem (sg.Element): element to be placed in the column

    Returns:
        sg.Column: column for a row
    """
    return sg.Column([[elem]], pad=(0, 0))


def create_row(col_1, col_2, col_3, row_visible, row_key=""):
    """Create a row


    Args:
        col_1 (sg.Column): first column of the row
        col_2 (sg.Column): second column of the row
        col_3 (sg.Column): third column of the row
        row_visible (bool): whether the row is visible or not
        row_key (str): key of the row

    Returns:
        sg.Column: row
    """
    return sg.Column(
        [[create_stretch(), col_1, col_2, col_3, create_stretch()]],
        pad=(0, 0),
        key=row_key,
        visible=row_visible,
        expand_x=True,
    )


def create_layout(*elements):
    """Create a layout


    Args:
        *elements (sg.Element): elements to be placed in the layout

    Returns:
        list: layout
    """
    return [[*elements]]


susceptible_text = create_col_for_row(sg.Text(text="Susceptible", size=(15, 1)))
susceptible_value = create_col_for_row(
    sg.InputText("1000000", size=(20, 1), justification="right", key="susceptible")
)

infectious_text = create_col_for_row(sg.Text(text="Infectious", size=(15, 1)))
infectious_value = create_col_for_row(
    sg.InputText("1", size=(20, 1), justification="right", key="infectious")
)

recovered_text = create_col_for_row(sg.Text(text="Recovered", size=(15, 1)))
recovered_value = create_col_for_row(
    sg.InputText("0", size=(20, 1), justification="right", key="recovered")
)

duration_text = create_col_for_row(sg.Text(text="Duration", size=(15, 1)))
duration_value = create_col_for_row(
    sg.InputText("150", size=(20, 1), justification="right", key="duration")
)

beta_text = create_col_for_row(sg.Text(text="??", size=(15, 1)))
beta_value = create_col_for_row(
    sg.InputText("4e-7", size=(20, 1), justification="right", key="beta")
)

recovery_time_text = create_col_for_row(sg.Text(text="Recovery time", size=(15, 1)))
recovery_time_value = create_col_for_row(
    sg.InputText("5", size=(20, 1), justification="right", key="recovery_time")
)

sw_a_text = create_col_for_row(sg.Text(text="a", size=(15, 1)))
sw_a_value = create_col_for_row(
    sg.InputText("0.01", size=(20, 1), justification="right", key="sw_a")
)

sw_start_text = create_col_for_row(sg.Text(text="Immunity loss start", size=(15, 1)))
sw_start_value = create_col_for_row(
    sg.InputText("30", size=(20, 1), justification="right", key="sw_start")
)


with_multiwave_row = create_row(
    create_stretch(),
    sg.Checkbox("Multiwave on/off", key="with_multiwave", enable_events=True),
    create_stretch(),
    True,
)

sw_a_row = create_row(
    sw_a_text,
    create_stretch(),
    sw_a_value,
    False,
    "sw_a_row",
)

sw_start_row = create_row(
    sw_start_text,
    create_stretch(),
    sw_start_value,
    False,
    "sw_start_row",
)


vac_rate_text = create_col_for_row(sg.Text(text="Vaccination rate", size=(15, 1)))
vac_rate_value = create_col_for_row(
    sg.InputText("20000", size=(20, 1), justification="right", key="vaccination_rate")
)

vac_eff_text = create_col_for_row(sg.Text(text="Vaccination eff", size=(15, 1)))
vac_eff_value = create_col_for_row(
    sg.InputText("0.9", size=(20, 1), justification="right", key="vaccination_eff")
)

vac_start_text = create_col_for_row(sg.Text(text="Vaccination start", size=(15, 1)))
vac_start_value = create_col_for_row(
    sg.InputText("50", size=(20, 1), justification="right", key="vaccination_start")
)

vac_end_text = create_col_for_row(sg.Text(text="Vaccination end", size=(15, 1)))
vac_end_value = create_col_for_row(
    sg.InputText("70", size=(20, 1), justification="right", key="vaccination_end")
)


with_vaccinations_row = create_row(
    create_stretch(),
    sg.Checkbox("Vaccinations on/off", enable_events=True, key="with_vaccinations"),
    create_stretch(),
    True,
)

susceptible_row = create_row(
    susceptible_text, create_stretch(), susceptible_value, True
)

infectious_row = create_row(infectious_text, create_stretch(), infectious_value, True)

recovered_row = create_row(recovered_text, create_stretch(), recovered_value, True)

duration_row = create_row(duration_text, create_stretch(), duration_value, True)

beta_row = create_row(beta_text, create_stretch(), beta_value, True)

recovery_time_row = create_row(
    recovery_time_text, create_stretch(), recovery_time_value, True
)

vac_rate_row = create_row(
    vac_rate_text, create_stretch(), vac_rate_value, False, "vaccination_rate_row"
)

vac_eff_row = create_row(
    vac_eff_text, create_stretch(), vac_eff_value, False, "vaccination_eff_row"
)

vac_start_row = create_row(
    vac_start_text, create_stretch(), vac_start_value, False, "vaccination_start_row"
)

vac_end_row = create_row(
    vac_end_text, create_stretch(), vac_end_value, False, "vaccination_end_row"
)

draw_row = create_row(
    sg.Button("Plot", key="-DRAW-", size=(5, 2), expand_x=True),
    create_stretch(),
    sg.Button("Clear", key="-CLEAR-", size=(5, 2), expand_x=True),
    True,
)


column1 = sg.Column(
    [
        [with_multiwave_row],
        [with_vaccinations_row],
        [susceptible_row],
        [infectious_row],
        [recovered_row],
        [duration_row],
        [beta_row],
        [recovery_time_row],
        [vac_rate_row],
        [vac_eff_row],
        [vac_start_row],
        [vac_end_row],
        [sw_a_row],
        [sw_start_row],
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
                background_color="white",
                expand_y=True,
                expand_x=True,
                size=(1000, 800),
            )
        ],
        [
            sg.Canvas(
                key="-TOOLBAR-",
                background_color="white",
                expand_x=True,
                expand_y=False,
            )
        ],
    ],
    expand_y=True,
    expand_x=True,
)

layout = create_layout(column1, column2)
