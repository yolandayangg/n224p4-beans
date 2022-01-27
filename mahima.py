
from flask import Blueprint, render_template

app_mahima = Blueprint('mahima', __name__)

@app_mahima.route('/mahima/')
def mahima():
    return render_template("aboutme/mahima.html")