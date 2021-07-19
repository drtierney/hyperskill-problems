import re

string = input()
# your code here
pattern = r"(?<=<li>)(.*?)(?=</li>)"
entries = re.findall(pattern, string)
for entry in entries:
    print(entry)
