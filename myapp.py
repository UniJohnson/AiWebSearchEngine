# myapp.py

from flask import Flask, render_template, request

from whoosh.qparser import QueryParser
from whoosh.index import open_dir

read_index = open_dir("indexdir")

def search_index(search_term):
    print("searching index")
    with read_index.searcher() as searcher:
        # find entries with the words 'first' AND 'last'
        query = QueryParser("content", read_index.schema).parse("*")
        results = searcher.search(query)
        
        # print all results
        for r in results:
            print(r)

    return results


app = Flask(__name__)

print("started flask")

@app.route('/')
# Define a route for your main page
def index():
    return render_template('index.html')


@app.route('/search')
def search():
    # grab the GET request arguments
    searchRequest = request.args['search']

    # return a search page with the search_results
    search_results = []

    # get data from index
    #indexing_result = ownIndex.get_data_from_index(searchRequest)
   
    result = search_index(searchRequest)
    print("from function search")
    print(result)

    # add the results to the search_results list
    for r in result:
       # turn the r object into a string
       print(result)
       
       # access the title from the whoosh.searching.Hit
       #print(r["title"])
       

    return render_template('search.html', search=search_results)

# deliver css
#@app.route('/style.css')
#def style():
#    return app.render_template('style.css')