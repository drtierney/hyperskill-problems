import pandas as pd


def concatenate_data(keyboard_instruments, string_instruments):
    return pd.concat([keyboard_instruments, string_instruments], ignore_index=True)
