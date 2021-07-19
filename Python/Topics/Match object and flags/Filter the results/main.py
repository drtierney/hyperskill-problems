import re


# put your regex in the variable template
template = r"Scaramouch."
string = input()
match = re.match(template, string)
if match:
    print("Match")
else:
    print("No match")
