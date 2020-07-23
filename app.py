import os
from flask import Flask, render_template, redirect, url_for
from views.forms.wisewordform import wisewordForm
import settings

app = Flask(__name__)
app.secret_key = settings.secret_key

@app.route('/')
def index():
    form = wisewordForm()

    return render_template("index.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)