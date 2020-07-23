from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, BooleanField
from wtforms.validators import data_required

class wisewordForm(FlaskForm):
    name = StringField("Input Your name Jigga!", [data_required()])
    wiseword = TextField("Wise words from wise men!", [data_required()])
    stayanonymous =  BooleanField("Stay Anonymous?")
    submit = SubmitField("Submit!")