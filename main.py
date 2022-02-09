# import "packages" from flask
from flask import Flask, render_template
from flask import request
import json
import requests
from __init__ import app
import requests, random


from templates.CRUD.app_crud_api import app_crud_api
app.register_blueprint(app_crud_api)

# create a Flask instance
# app = Flask(__name__)
from templates.CRUD.app_crud import app_crud
app.register_blueprint(app_crud)

from facts import app_facts
from calm import app_calm


app.register_blueprint(app_facts)
app.register_blueprint(app_calm)


from other import app_other
app.register_blueprint(app_other)

from aboutme import app_aboutme
app.register_blueprint(app_aboutme)

# connects default URL to render index.html

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/signup/')
def signup():
    return render_template("Personal/signup.html")

@app.route('/music/')
def music():
    return render_template("Personal/music.html")


@app.route('/outreach/')
def hawkers():
    return render_template("Personal/outreach.html")


@app.route('/Mahima/', methods=['GET', 'POST'])
def stub():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Minilabs/Mahima.html", name=name)
    # starting and empty input default
    return render_template("Minilabs/Mahima.html", name="World")

@app.route('/grayGreet/', methods=['GET', 'POST'])
def grayGreet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Minilabs/grayGreet.html", name=name)
    # starting and empty input default
    return render_template("Minilabs/grayGreet.html", name="World")

@app.route('/Nayana2', methods=['GET', 'POST'])
def greet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Minilabs/Nayana2.html", name=name)
    # starting and empty input default
    return render_template("Minilabs/Nayana2.html", name="World")

@app.route('/gabriel', methods=['GET', 'POST'])
def gabriel():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Minilabs/gabriel.html", name=name)
    # starting and empty input default

    return render_template("Minilabs/gabriel.html", name="World",)

@app.route('/platformer')
def platformer():
    return render_template("Personal/platformer.html")



@app.route('/binary/')
def binary():
    if request.form:
        try:
            bits = request.form.get("bits")
            if request.form["change_picture"] == "lightbulbs":
                if len(bits) !=0:
                    return render_template("Minilabs/binary.html", bits=int(bits), imgBulbOn="static/assets/bulb_on.gif", imgCloudOff="static/assets/bulb_off.png", name="New")
            if request.form["change_picture"] == "clouds":
                if len(bits) !=0:
                    return render_template("Minilabs/binary.html", bits=int(bits), imgBulbOn="static/assets/cloud.png", imgCloudOff="static/assets/lightning cloud.png", name="New")
            if request.form:
                bits = request.form.get("bits")
                if len(bits) !=0:
                    return render_template("Minilabs/binary.html", bits=int(bits))
        except:
            return render_template("Minilabs/binary.html", bits=8, imageBulbOn="/static/assets/bulb_on.gif", imageCloudOff="static/assets/bulb_off.png")
    return render_template("Minilabs/binary.html", bits=8, imageBulbOn="/static/assets/bulb_on.gif", imageCloudOff="/static/assets/bulb_off.png")


@app.route('/aboutme/')
def aboutme():
    return render_template("Minilabs/aboutme.html")



@app.route('/colorcode/')
def colorcode():
    return render_template('Minilabs/colorcode.html')

@app.route('/logicgate/')
def logicgate():
    return render_template('Minilabs/logicgate.html')


@app.route('/minilabs/')
def minilabs():
    return render_template("minilabs.html")



@app.route('/random/')
def random():
    return render_template("Minilabs/random.html")

@app.route('/grayProject/')
def grayProject():
    return render_template("Personal/grayProject.html")

@app.route('/wha_quiz/')
def wha_quiz():
    return render_template("Personal/wha_quiz.html")


@app.route('/clothing/')
def clothing():

    if request.form:
        return render_template("Personal/clothing.html")

    return render_template("Personal/clothing.html")


@app.route('/jeopardy/')
def jeopardy():
    return render_template("Personal/jeopardy.html")




@app.route('/search/')
def search():
    return render_template("CRUD/templates/search.html")

@app.route('/calm2/')
def calm2():
    return render_template("Personal/calm2.html")

@app.route('/calm1/')
def calm1():
    return render_template("Personal/calm1.html")

@app.route('/calm3/')
def calm3():
    return render_template("Personal/calm3.html")

@app.route('/calm4/')
def calm4():
    return render_template("Personal/calm4.html")

@app.route('/game/')
def game():
    return render_template("Personal/faq.html")

@app.route('/poe/')
def poe():
    return render_template("Personal/poe.py")

@app.route('/smiley/')
def smiley():
    return render_template("Personal/smiley.html")

@app.route('/compatability/')
def compatability():
    return render_template("Personal/compatability.html")

@app.route('/faq/')
def faq():
    return render_template("Personal/faq.html")

@app.route('/celeb/')
def celeb():
    return render_template("Personal/celeb.html")

@app.route('/RelaxingGames', methods=['GET', 'POST'])
def RelaxingGames():
    url = "https://free-to-play-games-database.p.rapidapi.com/api/games"

    querystring = {"sort-by":"alphabetical"}

    headers = {
        'x-rapidapi-host': "free-to-play-games-database.p.rapidapi.com",
        'x-rapidapi-key': "810c60410fmshe6c6bf953125c9ep188957jsn0e6dd57091ec"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    output = json.loads(response.text)

    return render_template("Personal/RelaxingGames.html", Games=output)

if __name__ == "__main__":
    app.run(debug=True, port=8000)











