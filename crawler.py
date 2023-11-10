import requests
from bs4 import BeautifulSoup

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
        full_url = url + link.get('href')

        if full_url not in visited:
            visit_stack.append(full_url)
    
    # recursively visit all links in the visit stack
    while len(visit_stack) > 0:
        # get the last element from the visit stack
        url_to_be_visited = visit_stack.pop()
        
        print("to visit:" + url_to_be_visited)
        print("visited:" + str(visited))


        # visit the url
        visit(url_to_be_visited)

        
    

visit("https://www.uni-osnabrueck.de/startseite/")
# problem, if href is twitter.com, then url+href appends a lot.
# maybe we can fix this with whooshh.

for page in visited:
    print(page)