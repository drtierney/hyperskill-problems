import re

template = r'... Jude'
string = input()
match = re.match(template, string)
if match:
    print(match.group())
else:
    print(None)
