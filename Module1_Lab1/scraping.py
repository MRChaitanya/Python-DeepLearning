from bs4 import BeautifulSoup
import requests

URL = 'https://catalog.umkc.edu/course-offerings/graduate/comp-sci/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
# print(page.text)
course_title = soup.findAll('span', {'class': 'title'})
course_overview = soup.findAll('p', {'class': 'courseblockdesc'})
for text in range(len(course_title)):
    print(course_title[text].text)
    print(course_overview[text].text)
    print('\n')
