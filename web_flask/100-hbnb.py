#!/usr/bin/python3
"""
display html of airbnb
"""
from flask import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """
    display hbnb site
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template("100-hbnb.html", states=states, amenities=amenities,
                           places=places)


@app.teardown_appcontext
def closeup(exception):
    """
    remove sql session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
