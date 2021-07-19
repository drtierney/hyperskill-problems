import re

template = r"[a-zA-Z]"
username = input()
match = re.match(template, username)
if match:
    print("Thank you!")
else:
    print("Oops! The username has to start with a letter.")
