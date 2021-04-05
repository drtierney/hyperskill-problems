# read test.txt
file = open("test.txt")

for line in file:
    print(line[0])

file.close()
