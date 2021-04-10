def select_dates(potential_dates):
    names = []
    for pd in potential_dates:
        if pd.get("age") > 30 \
                and "art" in pd.get("hobbies") \
                and pd.get("city") == "Berlin":
            names.append(pd["name"])
    return ", ".join(names)
