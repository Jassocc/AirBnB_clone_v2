#!/usr/bin/python3
"""
starts a web application
"""
from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def states_and_cities():
    """
    display html page with states and cities
    """
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def closup(exception):
    """
    remove session with clsoe
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
