import pandas as pd

df = pd.DataFrame({'a': [1, 4], 'b': [2, 5]})

# your code here
df["c"] = [3, 6]

new_row = {"a": 7,
           "b": 8,
           "c": 9}

df = df.append(new_row, ignore_index=True)
