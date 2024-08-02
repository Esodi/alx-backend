#!/usr/bin/env python3
''' this module contain get_locale method '''


from flask import Flask, request, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    ''' function itself '''
    return request.accept_languages.best_match(['en', 'fr'])


@app.route('/', strict_slashes=False)
def index():
    ''' index function '''
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
