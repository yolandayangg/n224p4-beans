from flask import Blueprint, render_template

app_yolanda = Blueprint('yolanda', __name__)

@app_yolanda.route
def yolanda():
    return render_template("aboutme/yolanda.html")
