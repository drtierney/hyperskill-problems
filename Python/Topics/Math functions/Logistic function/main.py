import math

x = int(input())
result = 1 / (1 + math.exp(-x))

print(round(result, 2))
