from flask import Blueprint, render_template

app_other = Blueprint('other', __name__)



@app_other.route('/quiz/')
def quiz():
    return render_template("Personal/quiz.html")

@app_other.route('/food/')
def food():
    return render_template("Personal/food.html")