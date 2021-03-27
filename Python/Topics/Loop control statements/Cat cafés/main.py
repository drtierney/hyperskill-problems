cafes = []
cats = []
while True:
    line = input().split(" ")
    if line[0] == "MEOW":
        break
    cafes.append(line[0])
    cats.append(int(line[1]))

print(cafes[cats.index(max(cats))])
