#!/usr/bin/env python3
''' this module institiate babel '''


from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel()


class Config:
    ''' this class configs babel lang '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

babel.init_app(app)


@app.route('/', strict_slashes=False)
def index():
    ''' the main function '''
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
