import os
from flask import Flask, render_template, redirect, url_for, request
from views.forms.wisewordform import wisewordForm
from controllers.wisewords import wisewords
from models.wiseword import wiseword
import settings

app = Flask(__name__)
app.secret_key = settings.secret_key

wisewordcontroller = wisewords()

@app.route('/', methods=['GET','POST'])
def index():
    form = wisewordForm()
    if request.method == 'GET':
        allwords = wisewordcontroller.read()
        return render_template("index.html", form=form, allwords=allwords)
    if request.method == 'POST':
        if form.validate_on_submit:
            name = form.name.data
            word = form.wiseword.data
            visible = form.stayanonymous.data

            singlewiseword = wiseword(None, word, visible, name)
            wisewordcontroller.create(singlewiseword)
        return render_template("index.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)