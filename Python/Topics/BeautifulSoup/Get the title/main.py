import requests

from bs4 import BeautifulSoup

url = input()

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

print(soup.find("h1").text)
