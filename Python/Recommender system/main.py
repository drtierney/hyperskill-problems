age = int(input())

if age <= 16:
    film = "Lion King"
elif 17 <= age <= 25:
    film = "Trainspotting"
elif 26 <= age <= 40:
    film = "Matrix"
elif 41 <= age <= 60:
    film = "Pulp Fiction"
else:
    film = "Breakfast at Tiffany's"

print(film)
