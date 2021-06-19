import pandas as pd


my_dict = {'A': {1: 1, 
                 2: 4, 
                 3: 6},
           'B': {1: 2, 
                 2: 7,
                 3: 10},
           'C': {1: 3, 
                 2: 11, 
                 3: 16}}

my_df = pd.DataFrame(my_dict)

# print column C of my_df
print(my_df["C"])
