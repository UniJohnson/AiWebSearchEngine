
# better crawler than Johnsons

import requests
from bs4 import BeautifulSoup

visit_stack = []
already_visited = []

def visit(url):
    

    # get the HTML and spice it up with beautiful soup
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')

    links = soup.find_all('a')
   
    # go through all links and add them to the visit stack
    for link in links:
        content = link.get('href')

        # make sure it is a string not of type none
        if isinstance(content, str):
            # relative links
            if content.startswith('/'):
                visit_stack.append(url + content)
            # full links
            elif content.startswith('https'):
                visit_stack.append(content)
    
    # recursive call till 1000 entries
    # gets exceeded by a few    
    while len(visit_stack) < 1000:
        temp = visit_stack.pop()
        already_visited.append(temp)
        visit(temp)


visit("https://www.factorio.com/")



# TESTING
# Print out all links in Stack

print(len(already_visited))
#print out the stack
for page in list(already_visited):
    print(already_visited.pop())

print(len(already_visited))



