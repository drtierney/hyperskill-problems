from collections import deque


stack = deque()
n = int(input())
for _ in range(n):
    line = input().split(" ")
    if line[0] == "POP":
        stack.pop()
    if line[0] == "PUSH":
        stack.append(line[1])

while stack:
    print(stack.pop())
