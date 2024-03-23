#!/usr/bin/python3
"""
A script that start a Flask Web application
"""
from flask import Flask
from flask import render_template

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


@app.route("/number/<int:n>", strict_slashes=False)
def num(n):
    """displays about a number"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_page(n):
    """Displaying a HTML page only if n is integer"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def even_or_odd(n):
    """Diaplays if a number is even or odd"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
