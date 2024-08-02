#!/usr/bin/env python3
''' this is the module containing gettext '''


from flask import Flask, render_template
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index():
    home_title = gettext("Welcome to Holberton")
    home_header = gettext("Hello world!")
    return render_template('3-index.html')
