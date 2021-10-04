# the following line reads the list from the input, do not modify it, please
passwords = input().split()

# your code below
for password in sorted(passwords, key=len):
    print(password, len(password))
