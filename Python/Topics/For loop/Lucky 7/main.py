n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(input()))

for i in numbers:
    if i % 7 == 0:
        print(i ** 2)
