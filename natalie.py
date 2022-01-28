
from flask import Blueprint, render_template

app_natalie = Blueprint('natalie', __name__)

@app_natalie.route('/natalie/')
def natalie():
    return render_template("aboutme/natalie.html")