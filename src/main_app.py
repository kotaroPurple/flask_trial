
from flask import render_template

from core.app import app


# top page
@app.route("/")
def index():
    return render_template("1_index.html")


@app.route("/sub_index")
def sub_index():
    return render_template("2_sub_index.html")


if __name__ == '__main__':
    app.run(debug=True)
