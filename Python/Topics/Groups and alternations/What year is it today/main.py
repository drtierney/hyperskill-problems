import re


# put your regex in the variable template
template = r"(\d{1,2})[/.](\d{1,2})[/.](\d{4})"
re.escape(template)
string = input()
# compare the string and the template
match = re.match(template, string)
if match:
    print(match.group(3))
else:
    print(None)
