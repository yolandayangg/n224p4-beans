from flask import Blueprint, render_template

app_facts = Blueprint('facts', __name__)

@app_facts.route('/fact1/')
def fact1():
    return render_template("Personal/fact1.html")

@app_facts.route('/fact2/')
def fact2():
    return render_template("Personal/fact2.html")

@app_facts.route('/fact3/')
def fact3():
    return render_template("Personal/fact3.html")