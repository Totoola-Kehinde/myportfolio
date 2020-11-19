import os
from flask import Flask, render_template, redirect, url_for, request
from views.forms.wisewordform import wisewordForm
from controllers.wisewords import wisewords
from models.wiseword import wiseword
import settings

# Simple App Configurations
app = Flask(__name__)
app.secret_key = settings.secret_key

wisewordcontroller = wisewords()

# Index Page Route
@app.route('/', methods=['GET','POST'])
def index():
    form = wisewordForm()

    # GET Request
    if request.method == 'GET':
        error = None
        if wisewords.error_msg is not None:
            error = wisewords.error_msg
        allwords = wisewordcontroller.read()
        return render_template("index.html", form=form, allwords=allwords, error=error)
    
    # POST Request - When Form is Submitted
    if request.method == 'POST':
        if form.validate_on_submit:
            name = form.name.data
            word = form.wiseword.data
            visible = form.stayanonymous.data

            error = None
            if wisewords.error_msg is not None:
                error = wisewords.error_msg
            allwords = wisewordcontroller.read()

            singlewiseword = wiseword(None, word, visible, name)
            wisewordcontroller.create(singlewiseword)
        return render_template("index.html", form=form, allwords=allwords, error=error)

# Development Mode "Debug=True" to enable debugging
if __name__ == "__main__":
    app.run(debug=True)