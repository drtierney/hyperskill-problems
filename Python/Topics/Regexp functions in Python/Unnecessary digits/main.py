import re       
names = input()
# your code here
result = re.split(r"\d+", names)
print(result)
