import re

template = r'are you ready??.?.?'
string = input()
match = re.match(template, string)
print(match.end() if match else 0)
