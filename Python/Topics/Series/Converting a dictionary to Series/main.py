import pandas as pd

def create_series(capitals):
    return pd.Series(capitals, name="Capitals of the world")
