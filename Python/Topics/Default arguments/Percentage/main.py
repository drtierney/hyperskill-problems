def get_percentage(number, round_digits=None):
    if round_digits is None:
        percentage = int(number * 100)
    else:
        percentage = round(number * 100, round_digits)
    return f"{percentage}%"
