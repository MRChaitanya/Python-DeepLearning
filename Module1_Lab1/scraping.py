from bs4 import BeautifulSoup
import requests

URL = 'https://catalog.umkc.edu/course-offerings/graduate/comp-sci/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

x = soup.find_all('title')
print(x)

y = soup.findAll('a')
print(y)

for link in soup.findAll('a'):
    print(link.get('href'))
