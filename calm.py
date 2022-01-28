from flask import Blueprint, render_template

app_calm = Blueprint('calm', __name__)

@app_calm.route('/calm1/')
def calm1():
    return render_template("Personal/calm1.html")

@app_calm.route('/calm2/')
def calm2():
    return render_template("Personal/calm2.html")

@app_calm.route('/calm3/')
def calm3():
    return render_template("Personal/calm3.html")

@app_calm.route('/calm4/')
def calm4():
    return render_template("Personal/calm4.html")