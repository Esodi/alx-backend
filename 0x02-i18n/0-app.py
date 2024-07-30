#!/usr/bin/python3
''' flask using module '''

from flask import render_template, Flask


app = Flask(__name__)


@app.route('/', strict_slashes = False)
def index():
    ''' the index function '''
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
