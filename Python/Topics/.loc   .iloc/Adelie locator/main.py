# put your code here. The data frame is already loaded and stored as penguins_df. 
adelie_df = penguins_df.loc[penguins_df.species == "Adelie", "island"::2]
print(adelie_df)
