import requests
from bs4 import BeautifulSoup

import ownIndex

# initialize visit stack with starting url
visit_stack = []
visited = []

# depth first search
def visit(url):
    # add url to visited list, make sure its not visited twice
    if url not in visited:
        visited.append(url)
    
    r = requests.get(url)

    # parse html into usable object
    soup = BeautifulSoup(r.content, 'html.parser')

    # find all links
    links = soup.find_all('a')

    # get all the hrefs from the links and extend the visit stack with all links
    # check against already visited links
    for link in links:
        # if the link is not visited, add it to the visit stack, meaning it will be visited
        # make sure to get the full url

        # get the full url
        # if the link is relative, then we need to add the base url
        if link.get('href').startswith('https'):
            full_url = link.get('href')
        else:
            full_url = url + link.get('href')

        if full_url not in visited:
            # the visit stack appends the full url "https://www.uni-osnabrueck.de/startseite/https://www.twitter.com/uniosnabrueck/", which is wrong
            visit_stack.append(full_url)
    
    # recursively visit all links in the visit stack
    while len(visit_stack) > 0:
        # get the last element from the visit stack
        url_to_be_visited = visit_stack.pop()
        
        print("to visit:" + url_to_be_visited)
        print("visited:" + str(visited))

        # visit the url
        visit(url_to_be_visited)

try:
    visit("https://vm009.rz.uos.de/crawl/")
except:
    print("Crawler stopped as intended.")
    pass

# crawl the visited urls and add them to the index

try:
    for url in visited:
        print("crawling url:" + url)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')

        if soup.title is not None and soup.get_text() is not None:
            ownIndex.add_document(soup.title.string, soup.get_text())
except:
    print("Writing to index stopped as intended.")
    pass

# commit the writer
ownIndex.commit_writer()

print("Everything finished.")
