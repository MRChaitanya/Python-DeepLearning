from bs4 import BeautifulSoup
import requests

URL = 'https://catalog.umkc.edu/course-offerings/graduate/comp-sci/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

x = soup.find_all('title')
print(x)

y = soup.findAll('span')
print(y)

z = soup.findAll('p')
print(z)

for link in soup.findAll('a'):
    print(link.get('href'))

