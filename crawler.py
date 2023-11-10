import requests
from bs4 import BeautifulSoup

# initialize visit stack with starting url
visit_stack = ['https://vm009.rz.uos.de/crawl/']

def visit(url):
    # remove url from visit stack
    visit_stack.remove(url)

    r = requests.get(url)

    # parse html into usable object
    soup = BeautifulSoup(r.content, 'html.parser')

    # find all links
    links = soup.find_all('a')

    # get all the hrefs from the links and extend the visit stack with all links
    visit_stack.extend([link.get('href') for link in links])

    # print the visit stack
    print(visit_stack)

