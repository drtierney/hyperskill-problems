class Task:
    def __init__(self, description, team):
        self.description = description
        self.team = team

    # create the method
    def __add__(self, other):
        new_description = self.description + '\n' + other.description
        new_team = self.team + ', ' + other.team
        return Task(new_description, new_team)
