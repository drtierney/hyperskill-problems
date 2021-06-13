args = sys.argv

# further code of the script "add_four_numbers.py"
total = 0
for arg in args[1:]:
    total += int(arg)
print(total)
