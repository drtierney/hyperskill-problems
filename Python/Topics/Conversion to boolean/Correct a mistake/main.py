def compare(numerator, denominator):
    return bool(denominator and numerator / denominator == 0.5)


a = int(input())
b = int(input())

print(compare(a, b))
