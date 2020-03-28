import logging

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, audio, statement, question, session

NUMBERS = {
    1: "uno",
    2: "dos",
    3: "tres",
    4: "cuatro",
    5: "cinco",
    6: "seis",
    7: "siete",
    8: "ocho",
    9: "nueve",
    10: "diez",
    11: "once",
    12: "doce",
    13: "trece",
    14: "catorce",
    15: "quince",
    16: "dieciseis",
    17: "diecisiete",
    18: "dieciocho",
    19: "diecinueve",
    20: "veinte",
}

app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch
def new_game():
    welcome_msg = render_template("welcome")
    return question(welcome_msg)


@ask.intent("OneshotTakeoffIntent", convert={"seconds": int})
def answer(seconds):
    seconds = seconds or 10
    count = range(1, seconds + 1)
    words = reversed(list(map(lambda num: NUMBERS[num], count)))

    speech = render_template("takeoff", words=words)
    stream_url = 'https://freesound.org/data/previews/93/93078_1386366-lq.mp3'
    return audio(speech).play(stream_url)


if __name__ == "__main__":
    app.run(debug=True)
