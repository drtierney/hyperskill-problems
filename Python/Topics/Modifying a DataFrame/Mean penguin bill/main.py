# your code here. The dataset is already loaded, the variable that contains the DataFrame is called penguins_example
penguins_example["mean_bill"] = (penguins_example.bill_length_mm
                                 + penguins_example.bill_depth_mm) / 2
print(penguins_example)
