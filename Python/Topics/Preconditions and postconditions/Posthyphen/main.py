import re

string = input()
# your code here
pattern = r"(?<=-)(\w*)"
search = re.search(pattern, string)
print(search.group(1))
