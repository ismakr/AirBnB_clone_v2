#!/usr/bin/python3
"""
 starts a Flask web application
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """route"""
    return "Hello HBNB!"


@app.route("/hbnb/", strict_slashes=False)
def hbnb():
    """route hbnb"""
    return "HBNB!"


@app.route("/c/<text>/", strict_slashes=False)
def c_text(text):
    """route c"""
    return f"C {text.replace('_', ' ')}"


@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """route python"""
    return f"Python {text.replace('_', ' ')}"


@app.route("/python/", strict_slashes=False)
def python():
    """route python"""
    return f"Python is cool"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """route python"""
    return f"{str(n)} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """route python"""
    return render_template("templates/5-number.html", nb=n")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
