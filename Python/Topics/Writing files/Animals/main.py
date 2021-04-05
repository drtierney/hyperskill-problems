# read animals.txt
# and write animals_new.txt
file1 = open("animals.txt")
file2 = open("animals_new.txt", "w")

for line in file1:
    file2.write(line.replace("\n", " "))

file1.close()
file2.close()
