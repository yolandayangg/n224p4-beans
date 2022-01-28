from flask import Blueprint, render_template, app

app_aboutme = Blueprint('aboutme', __name__)

@app_aboutme.route('/nayana/')
def nayana():
    return render_template("aboutme/nayana.html")

@app_aboutme.route('/Shruti/')
def Shruti():
    return render_template("aboutme/Shruti.html")

@app_aboutme.route('/Mahima/')
def Mahima():
    return render_template("aboutme/Mahima.html")