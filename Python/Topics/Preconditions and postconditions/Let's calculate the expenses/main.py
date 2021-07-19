import re

string = input()
# your code here
pattern = r"(?<=\$)\d+"
total = sum(int(i) for i in re.findall(pattern, string))
print(f"This week you have spent:  {total} dollars")
