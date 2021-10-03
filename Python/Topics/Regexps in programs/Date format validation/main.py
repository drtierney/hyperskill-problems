import re

string = input()
# your code here
date_pattern = r"^([0-1][0-9]/){2}[\d]{4}$"
print(bool(re.match(date_pattern, string)))
