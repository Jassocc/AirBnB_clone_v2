#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask, abort, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    display Hello HBNB
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    display HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Display c and following text
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    """
    display python and text, default = is cool
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    display number with given num
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    display a HTML page
    """
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """
    display number as odd or even
    """
    return render_template("6-number_odd_or_even.html",
                           number=n, odd_even='odd' if n % 2 != 0 else "even")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
