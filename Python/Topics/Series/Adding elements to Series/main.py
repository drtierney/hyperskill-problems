import pandas as pd


def add_records(olympics):
    olympics[2021] = "Tokyo"
    olympics[2024] = "Paris"
    olympics[2028] = "Los Angeles"
    return olympics
