# put your python code here
def edge_length(a, b, c):
    return (a + b + c) * 4


def surface_area(a, b, c):
    return ((a * b) + (b * c) + (a * c)) * 2


def volume(a, b, c):
    return a * b * c


length = int(input())
width = int(input())
height = int(input())

print(edge_length(length, width, height))
print(surface_area(length, width, height))
print(volume(length, width, height))
