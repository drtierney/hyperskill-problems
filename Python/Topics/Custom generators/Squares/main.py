#  Posted from EduTools plugin
n = int(input())


def squares(i):
    x = 1
    while x <= i:
        yield x ** 2
        x += 1


# Don't forget to print out the first n numbers one by one here
for y in squares(n):
    print(y)
