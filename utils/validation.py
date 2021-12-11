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
