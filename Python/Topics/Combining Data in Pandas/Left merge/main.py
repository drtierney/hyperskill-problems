import pandas as pd


def merge_data(user_info, emails):
    return user_info.merge(emails, how="left")
