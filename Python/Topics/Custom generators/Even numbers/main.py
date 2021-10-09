n = int(input())


def even():
    for i in range(n):
        yield i * 2


# Don't forget to print out the first n numbers one by one here
my_generator = even()
for _ in range(n):
    print(next(my_generator))
