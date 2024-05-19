#!/usr/bin/python3
"""
 starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """route"""
    return "Hello HBNB!"


@app.route("/hbnb/", strict_slashes=False)
def hbnb():
    """route hbnb"""
    return "HBNB!"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """route c"""
    return f"C {text}"


@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """route python"""
    return f"Python {text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
