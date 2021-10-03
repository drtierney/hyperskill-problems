from nltk.tokenize import regexp_tokenize


text = input()
index = int(input())
words = regexp_tokenize(text, "[A-z]+")

print(words[index])
