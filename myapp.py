# myapp.py

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
# Define a route for your main page
def index():
    return render_template('index.html')


@app.route('/reverse')
def reverse():
    # grab the GET request arguments
    rev = request.args['rev']

    #  return the reverse.html and pass the rev argument
    return render_template('reverse.html', rev=rev[::-1])

# deliver css
#@app.route('/style.css')
#def style():
#    return app.render_template('style.css')