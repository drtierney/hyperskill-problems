# your code here, the dataset is already loaded. The variable name is df_rock.
df_rock.rename(columns={"0°": "zero_deg",
                      "60°": "sixty_deg",
                      "90°": "ninety_deg",
                      "180°": "straight_angle"}, inplace=True)

print(df_rock.columns)
