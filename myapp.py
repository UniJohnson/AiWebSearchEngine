# myapp.py

from flask import Flask, render_template, request

import ownIndex

app = Flask(__name__)

@app.route('/')
# Define a route for your main page
def index():
    return render_template('index.html')


@app.route('/search')
def reverse():
    # grab the GET request arguments
    searchRequest = request.args['search']

    # return a search page with the search_results
    search_results = []

    indexing_result = ownIndex.get_data_from_index(searchRequest)
    print("results:" + str(indexing_result))
    print("index:" + str(ownIndex.print_index()))

    search_results.append(indexing_result)

    return render_template('search.html', search=search_results)

# deliver css
#@app.route('/style.css')
#def style():
#    return app.render_template('style.css')