#!/usr/bin/env python
# http://flask.pocoo.org/docs/0.10/quickstart/
# http://jinja.pocoo.org/docs/dev/templates/

from flask import (Flask, request, render_template)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('twitter.html')

@app.route('/poop', methods=['POST'])
def hello_world():
    if request.form:
        username = request.form['username']
        return render_template('twitter.html', username=username)
    else:
        return "ERROR"

if __name__ == '__main__':
    app.run(debug=True)
