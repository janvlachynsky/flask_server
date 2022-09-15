from tokenize import String
from turtle import lt
from numpy import datetime_as_string
from flask import (
    Flask,
    render_template,
    flash,
    redirect,
    url_for,
    session,
    request,
    logging,
)

from forms import AddEletricityEntryForm
from database import Database
from datetime import datetime


from passlib.hash import sha256_crypt

import os


app = Flask(__name__)

# CSRF protection
SECRET_KEY = os.urandom(32)
app.config["SECRET_KEY"] = SECRET_KEY


@app.route("/")
def index():
    return render_template("index.html")


# @app.route('/<string:name>')
# def index_hello(name):
#     return render_template('index.html', name=name)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/energy")
def energy():

    db = Database()
    energy_data = db.getEletricityEntries()

    return render_template("energy.html", energy_data=energy_data)


@app.route("/energy/add_entry", methods=["GET", "POST"])
def add_entry():
    date = datetime.now()
    form = AddEletricityEntryForm()

    if form.validate_on_submit():

        submit_new_entry(
            request.form["lowTariff"], request.form["highTariff"], request.form["date"]
        )
    else:
        print("valid???", form.highTariff.errors)
        print("form not valid")
    # TODO: add energy entry
    return render_template(
        "energy_add_entry.html", date=date, form=form, last_form=request.form
    )


@app.route("/submit_new_entry", methods=["GET", "POST"])
def submit_new_entry(lowTariff, highTariff, date):
    print(lowTariff, highTariff, date)
    pass


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
