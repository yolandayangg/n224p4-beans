# import "packages" from flask
from flask import Flask, render_template
from flask import request
from image import image_data
from pathlib import Path



# create a Flask instance
app = Flask(__name__)


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
    return render_template("Minilabs/gabriel.html", name="World")

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
                    return render_template("Minilabs/binary.html", bits=int(bits), imgCloudOn="static/assets/bulb_on.gif", imgCloudOff="static/assets/bulb_off.png")
            if request.form["change_picture"] == "clouds":
                if len(bits) !=0:
                    return render_template("Minilabs/binary.html", bits=int(bits), imgCloudOn="static/assets/cloud.png", imgCloudOff="static/assets/lightning cloud.png")
        except:
            return render_template("Minilabs/binary.html", bits=8, imageCloudOn="/static/assets/bulb_on.gif", imageCloudOff="static/assets/bulb_off.png")
    return render_template("Minilabs/binary.html", bits=8, imageCloudOn="/static/assets/bulb_on.gif", imageCloudOff="/static/assets/bulb_off.png")


@app.route('/aboutme/')
def aboutme():
    return render_template("Minilabs/aboutme.html")

@app.route('/RGB/')
def RGB():
    path = Path(app.root_path) / "static" / "assets"
    return render_template('Minilabs/RGB.html', images=image_data(path))


@app.route('/colorcode/')
def colorcode():
    return render_template('Minilabs/colorcode.html')

@app.route('/logicgate/')
def logicgate():
    return render_template('Minilabs/logicgate.html')


@app.route('/minilabs/')
def minilabs():
    return render_template("minilabs.html")


@app.route('/wha_quiz/')
def wha_quiz():
    return render_template("Personal/wha_quiz.html")




if __name__ == "__main__":
    app.run(debug=True, port=5180)

