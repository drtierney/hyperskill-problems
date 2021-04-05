# read sums.txt
file = open("sums.txt")

for line in file:
    numbers = line.split(" ")
    print(int(numbers[0]) + int(numbers[1]))

file.close()
