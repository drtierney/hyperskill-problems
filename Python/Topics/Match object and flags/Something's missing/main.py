import re


string = input()
template = r'never gonna let you down...'
match = re.match(template, string, flags=re.IGNORECASE)
