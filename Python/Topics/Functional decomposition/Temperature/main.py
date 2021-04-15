def fahrenheit_to_celsius(temps_f):
    temps_c = (temps_f - 32) * 5 / 9
    return round(temps_c, 2)


def celsius_to_fahrenheit(temps_c):
    temps_f = temps_c * 9 / 5 + 32
    return round(temps_f, 2)


def main():
    """Entry point of the program."""
    temperature, unit = input().split()  # read the input
    if unit == "C":
        temp = celsius_to_fahrenheit(int(temperature))
        print(f"{temp} F")
    if unit == "F":
        temp = fahrenheit_to_celsius(int(temperature))
        print(f"{temp} C")
