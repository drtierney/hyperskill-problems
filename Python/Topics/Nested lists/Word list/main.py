text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]

n = int(input())
output = []

# [word for line in text for word in line if len(word) <= n]
for line in text:
    for word in line:
        if len(word) <= n:
            output.append(word)

print(output)
