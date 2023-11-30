# myapp.py

from flask import Flask, render_template, request

from whoosh.qparser import QueryParser
from whoosh.index import open_dir

read_index = open_dir("indexdir")

def search_index(search_term):
    print("searching index")
    with read_index.searcher() as searcher:
        # find entries with the words 'first' AND 'last'
        query = QueryParser("content", read_index.schema).parse(search_term)
        results = searcher.search(query)
        
        result_array = []

        # print all results
        for r in results:
            
            title = r['title']
            content = r['content']
            url = r['url']

            # clean up line breaks
            title = title.replace("\n", "")
            title = title.replace("\r", "")
            title = title.replace("\t", "")
            content = content.replace("\n", "")
            content = content.replace("\r", "")
            content = content.replace("\t", "")
            url = url.replace("\n", "")
            url = url.replace("\r", "")
            url = url.replace("\t", "")
            # clean up white spaces
            title = title.strip()
            content = content.strip()
            url = url.strip()
            
            # store an object with title, content and url
            result_array.append({'title': title, 'content': content, 'url': url})

    return result_array


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

    # get data from index
    #indexing_result = ownIndex.get_data_from_index(searchRequest)
   
    result = search_index(searchRequest)
    print("from function search")
    print(result)

    return render_template('search.html', search=result, query=searchRequest)
