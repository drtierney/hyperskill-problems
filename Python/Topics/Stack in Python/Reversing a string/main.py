from collections import deque


n = int(input())
stack = deque()

for _ in range(n):
    stack.append(input())

while stack:
    print(stack.pop())
