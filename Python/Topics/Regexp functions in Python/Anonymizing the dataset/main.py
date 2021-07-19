import re

string = input()
# your code
pattern = r"@\w+"
string = re.sub(pattern, "<AUTHOR>", string, count=1)
string = re.sub(pattern, "<HANDLE>", string)

print(string)
