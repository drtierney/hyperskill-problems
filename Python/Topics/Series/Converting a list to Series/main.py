import pandas as pd


def create_series(foods, calories):
    return pd.Series(index=foods, data=calories, name="Calorie content")
