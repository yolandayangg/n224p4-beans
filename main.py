
# import "packages" from flask
from flask import render_template
from __init__ import app
from templates.CRUD.app_crud import app_crud
from flask import request

# create a Flask instance
# app = Flask(__name__)
app.register_blueprint(app_crud)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render volunteering.html
@app.route('/volunteering/')
def kangaroos():
    return render_template("Personal/volunteering.html")


@app.route('/signup/')
def walruses():
    return render_template("Personal/signup.html")


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

@app.route('/jeopardy/')
def jeopardy():
    return render_template("Personal/jeopardy.html")

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

@app.route('/Natalie/')
def Natalie():
    return render_template("aboutme/Natalie.html")

@app.route('/nayana/')
def nayana():
    return render_template("aboutme/nayana.html")

@app.route('/Shruti/')
def Shruti():
    return render_template("aboutme/Shruti.html")

@app.route('/yolanda/')
def yolanda():
    return render_template("aboutme/yolanda.html")

@app.route('/mahima/')
def mahima():
    return render_template("aboutme/mahima.html")

@app.route('/calm1/')
def calm1():
    return render_template("Personal/calm1.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)









