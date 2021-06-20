import pandas as pd


grades_2019 = pd.DataFrame({'Subject': ['Physics', 'Geometry', 'Chemistry'], 'Average': ['68', '78', '75']})
grades_2020 = pd.DataFrame({'Subject': ['Physics', 'Geometry', 'Chemistry'], 'Average': ['72', '80', '75']})
grades_union = pd.concat([grades_2019, grades_2020], keys=["Year 2019", "Year 2020"])
