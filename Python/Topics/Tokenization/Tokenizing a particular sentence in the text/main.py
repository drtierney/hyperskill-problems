from nltk.tokenize import sent_tokenize
from nltk.tokenize import regexp_tokenize


text = input()
index = int(input())
sentences = sent_tokenize(text)

print(regexp_tokenize(sentences[index], "[A-z']+"))
