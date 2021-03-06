from flask import Flask, render_template, flash, redirect, url_for, session, logging

from database import Database

from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/<string:name>')
# def index_hello(name):
#     return render_template('index.html', name=name)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/energy')
def energy():

    db = Database()
    energy_data = db.getEletricityEntries()

    return render_template('energy.html', energy_data=energy_data)



class RegisterForm(Form):
    name = StringField('Name', [validators])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
