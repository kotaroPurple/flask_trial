
from flask import render_template

from core.app import app
from core.models import Customer


# top page
@app.route("/")
def index():
    customers = Customer.query.all()
    return render_template("1_index.html", customers=customers)


@app.route("/sub_index")
def sub_index():
    return render_template("2_sub_index.html")


if __name__ == '__main__':
    app.run(debug=True)
