import re

password = input()
# your code here
pattern = r'^[\w]{6,15}$'
match = re.match(pattern, password, flags=re.ASCII)
print("Thank you!" if match else "Error!")
