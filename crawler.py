import requests
from bs4 import BeautifulSoup


r = requests.get('https://www.uos.de')

# parse html into usable object
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())