import re

string = input()
# your code here
capitalized_pattern = r'[A-Z]\w+'
digit_pattern = r'\d+'

capitalized_words = ", ".join(re.findall(capitalized_pattern, string))
digits = ", ".join(re.findall(digit_pattern, string))

print(f"Capitalized words: {capitalized_words}")
print(f"Digits: {digits}")
