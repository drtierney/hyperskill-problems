# your code here. The dataset is already loaded, the variable that contains the DataFrame is called penguins_example
new_row = {
    "species": "Adelie",
    "bill_length_mm": 45.7,
    "bill_depth_mm": 15.5
}

penguins_example = penguins_example.append(new_row, ignore_index=True)

print(penguins_example)
