import re


# put your regex in the variable template
template = r"(Value|Name|Type)Error"
string = input()
# compare the string and the template
match = re.match(template, string)
print(match.group(1) if match else None)
