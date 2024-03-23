#!/usr/bin/python3
"""
A script that start a Flask Web application
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """web display"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """display HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def variable(text):
    """displays about C"""
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<adj>", strict_slashes=False)
def python(adj="is cool"):
    """display about python"""
    adj = adj.replace("_", " ")
    return f"Python {adj}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
