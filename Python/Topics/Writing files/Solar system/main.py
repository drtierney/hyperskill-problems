# create the planets.txt
file = open("planets.txt", "w")

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

for planet in planets:
    file.write(f"{planet}\n")

file.close()
