from flask import *
import os

alexa_tivo  = Blueprint('alexa_tivo', __name__)


@alexa_tivo.route('/')
def index():
    return 'alexa_tivo'


