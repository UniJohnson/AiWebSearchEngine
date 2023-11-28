# myapp.py

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
# Define a route for your main page
def index():
    return render_template('index.html')


@app.route('/search')
def reverse():
    # grab the GET request arguments
    rev = request.args['search']

    # return a search page with the search_results
    search_results = [rev]
    

    return render_template('search.html', search=search_results)

# deliver css
#@app.route('/style.css')
#def style():
#    return app.render_template('style.css')