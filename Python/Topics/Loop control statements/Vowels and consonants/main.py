from string import ascii_letters


line = input()
for letter in line:
    if letter not in ascii_letters:
        break
    print("vowel" if letter in "aeiou" else "consonant")
