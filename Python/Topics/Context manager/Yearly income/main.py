# write your code here
with open("salary.txt") as f1, \
     open("salary_year.txt", "w") as f2:
    for line in f1:
        f2.write(f"{int(line.rstrip()) * 12}\n")
