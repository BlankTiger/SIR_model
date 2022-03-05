def validate_positive_int_input(value, param=None):
    if param:
        msg = f"Please make sure that '{param}' is a positive, whole number."
    else:
        msg = "Please make sure that all entered values are valid."
    try:
        value = int(value)
    except ValueError:
        raise ValueError(msg)
    if value < 0:
        raise ValueError(msg)
    return True


def validate_positive_float_input(value, param=None):
    if param:
        msg = f"Please make sure that '{param}'is a positive number."
    else:
        msg = "Please make sure that all entered values are valid."
    try:
        value = float(value)
    except ValueError:
        raise ValueError(msg)
    if value < 0:
        raise ValueError(msg)
    return True


def validate_pos_float_under_one(value, param=None):
    if param:
        msg = (
            f"Please make sure that '{param}' is a positive number less or equal to 1."
        )
    else:
        msg = "Please make sure that all entered values are valid."
    try:
        value = float(value)
    except ValueError:
        raise ValueError(msg)
    if value < 0 or value > 1:
        raise ValueError(msg)
    return True
