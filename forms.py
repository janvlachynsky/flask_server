from flask_wtf import FlaskForm
from wtforms import (
    Form,
    StringField,
    TextAreaField,
    PasswordField,
    validators,
    IntegerField,
    DateField,
)
from wtforms.validators import InputRequired, Length


class AddEletricityEntryForm(FlaskForm):
    lowTariff = StringField("lowTariff", validators=[validators.Length(min=1, max=9)])
    highTariff = StringField(
        "highTariff", validators=[validators.Length(min=1, max=10)]
    )
    date = DateField("date")
    note = StringField("note", validators=[validators.Length(max=200)])
