from flask import Flask
import logging
import os

from flask_ask import Ask

app = Flask(__name__)
app.secret_key = 'SUPERSECRET' # you should change this to something equally random
app.config.from_pyfile(os.path.abspath('settings.py'))

app = Flask(__name__)
ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.INFO)

from views import alexa_tivo as alexa_tivo
app.register_blueprint(alexa_tivo)

