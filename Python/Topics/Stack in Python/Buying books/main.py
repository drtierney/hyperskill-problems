from collections import deque

books = [input().split(" ", 1) for entry in range(int(input()))]
stack = deque()
for book in books:
    if book[0] == "BUY":
        stack.append(book)
    else:
        print(stack.pop()[1])
