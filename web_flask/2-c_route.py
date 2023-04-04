#!/usr/bin/python3
''' starts a Flask web application'''
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def index_2():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def index_3(text):
    return "C {}".format(text).replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
