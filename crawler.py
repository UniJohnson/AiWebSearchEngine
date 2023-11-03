import requests
from bs4 import BeautifulSoup


r = requests.get('https://www.uos.de')

# parse html into usable object
soup = BeautifulSoup(r.content, 'html.parser')

# find all links
links = soup.find_all('a')

# print all links
for link in links:
    print(link.get('href'))