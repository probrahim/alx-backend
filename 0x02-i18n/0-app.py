from flask import render_template
from flask import Flask
i  # !/usr/bin/env python3
"""
flask application
"""


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index() -> str:
    """template html de base"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
