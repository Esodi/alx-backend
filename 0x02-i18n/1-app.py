#!/usr/bin/env python3
''' this module institiate babel '''


from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel()


class Config:
    ''' this class configs babel lang '''
    LANGUAGES = ["en", "fr"]
    app.config['BABEL_LANGUAGE_LOCALE'] = LANGUAGES[0]
    app.config['BABEL_TIMEZONE_LOCALE'] = 'UTC'

conf = Config()
babel.init_app(app)

if __name__ == "__main__":
    app.run()
