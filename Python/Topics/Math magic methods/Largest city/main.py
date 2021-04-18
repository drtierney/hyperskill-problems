class City:
    # define methods here
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __gt__(self, other):
        return self.population > other.population
