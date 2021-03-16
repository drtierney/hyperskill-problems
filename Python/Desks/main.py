# put your python code here
def desk_count(class_n):
    return (class_n // 2) + (class_n % 2)


class_1 = int(input())
class_2 = int(input())
class_3 = int(input())

print(desk_count(class_1) + desk_count(class_2) + desk_count(class_3))
