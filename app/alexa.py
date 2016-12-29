import logging
import tivo
from flask import current_app
from flask_ask import Ask, statement, question, session

tivo_address = current_app.config['TIVO_ADDRESS']


@ask.launch
def tivo_control():
    welcome_msg = render_template('welcome')
    return question(welcome_msg) \
     .reprompt("I didn't get that. What would you like to do?")


@ask.intent("PauseIntent")
def pause_tivo():
    t = tivo.Tivo(tivo_address)
    t.connect()
    t.send_code('PAUSE')
    t.close()
    paused = render_template('pause')
    return statement(paused)


@ask.intent("PlayIntent")
def play_tivo():
    t = tivo.Tivo(tivo_address)
    t.connect()
    t.send_code('PLAY')
    t.close()
    play = render_template('play')
    return statement(play)


@ask.intent("GuideIntent")
def open_tivo_guide():
    t = tivo.Tivo(tivo_address)
    t.connect()
    t.send_code('GUIDE')
    t.close()
    guide = render_template('guide')
    return statement(guide)

@ask.intent("LiveTVIntent")
def tv_mode():
    t = tivo.Tivo(tivo_address)
    t.connect()
    t.send_code('LIVETV')
    t.close()
    livetv = render_template('livetv')
    return statement(livetv)

@ask.intent("InfoIntent")
def info():
    t = tivo.Tivo(tivo_address)
    t.connect()
    t.send_code('INFO')
    t.close()
    info = render_template('info')
    return statement(info)

