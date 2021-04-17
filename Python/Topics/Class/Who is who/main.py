class Angel:
    color = "white"
    feature = "wings"
    home = "Heaven"


class Demon:
    color = "red"
    feature = "horns"
    home = "Hell"


the_angel = Angel()
print(the_angel.color)
print(the_angel.feature)
print(the_angel.home)

the_demon = Demon()
for attribute in ['color', 'feature', 'home']:
    print(getattr(the_demon, attribute))
