import re 

pets = input()
# your code here
pattern = r"(dog|cat|parrot|hamster)"
print(re.findall(pattern, pets, flags=re.IGNORECASE))
