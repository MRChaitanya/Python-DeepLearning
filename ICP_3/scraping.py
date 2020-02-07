from bs4 import BeautifulSoup
import requests

URL = 'https://en.wikipedia.org/wiki/Deep_learning'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

x = soup.find_all('title')
print(x)

y = soup.find_all('a')
print(y)

for link in soup.findAll('a'):
    print(link.get('href'))
