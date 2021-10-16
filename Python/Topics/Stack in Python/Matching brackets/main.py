from collections import deque
brackets = deque()
code = input()
try:
    for i in code:
        if i == "(":
            brackets.append(i)
        elif i == ")":
            brackets.pop()

    if not len(brackets):
        print("OK")
    else:
        print("ERROR")
except IndexError:
    print("ERROR")
