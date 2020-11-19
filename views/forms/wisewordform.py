from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import data_required

class wisewordForm(FlaskForm):
    name = StringField("Your name", [data_required()])
    wiseword = TextAreaField("Wise words / Legendary Experience", [data_required()])
    stayanonymous =  BooleanField("Stay Anonymous?")
    submit = SubmitField("Submit!")