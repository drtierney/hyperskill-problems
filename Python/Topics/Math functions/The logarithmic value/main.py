import math

a = int(input())
b = int(input())

print(round(math.log(a) if b <= 1 else math.log(a, b), 2))
