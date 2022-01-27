from flask import Blueprint, render_template

app_Natalie = Blueprint('Natalie', __name__)

@app_Natalie.route('/Natalie/')
def Natalie():
    return render_template("aboutme/Natalie.html")