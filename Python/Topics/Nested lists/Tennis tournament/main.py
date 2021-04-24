n = int(input())

matches = [input() for _ in range(n)]

wins = []
for match in matches:
    if "win" in match:
        wins.append(match.split()[0])

print(wins)
print(len(wins))
