class Painting:
    museum = "Louvre"
    paintings = []

    def __init__(self, title, painter, year):
        self.title = title
        self.painter = painter
        self.year = year

        Painting.paintings.append(self)

    def get_info(self):
        print(f'"{self.title}" by {self.painter} ({self.year}) hangs in the {Painting.museum}.')


the_title = input()
the_artist = input()
the_year = int(input())

the_painting = Painting(the_title, the_artist, the_year)
the_painting.get_info()
