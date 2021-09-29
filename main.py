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
    return render_template("volunteering.html")


@app.route('/signup/')
def walruses():
    return render_template("signup.html")


@app.route('/outreach/')
def hawkers():
    return render_template("outreach.html")


@app.route('/Mahima/', methods=['GET', 'POST'])
def stub():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Mahima.html", name=name)
    # starting and empty input default
    return render_template("Mahima.html", name="World")

@app.route('/grayGreet/', methods=['GET', 'POST'])
def grayGreet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("grayGreet.html", name=name)
    # starting and empty input default
    return render_template("grayGreet.html", name="World")

@app.route('/Nayana2', methods=['GET', 'POST'])
def greet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Nayana2.html", name=name)
    # starting and empty input default
    return render_template("Nayana2.html", name="World")

@app.route('/gabriel', methods=['GET', 'POST'])
def gabriel():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("gabriel.html", name=name)
    # starting and empty input default
    return render_template("gabriel.html", name="World")

@app.route('/binary/')
def binary():
    if request.form:
        bits = request.form.get("bits")
        if len(bits) !=0:
            return render_template("binary.html", int(bits))
        #
    return render_template("binary.html", bits= 8)

@app.route('/aboutme/')
def aboutme():
    return render_template("aboutme.html")

@app.route('/RGB/')
def RGB():
    path = Path(app.root_path) / "static" / "assets"
    return render_template('RGB.html', images=image_data(path))




@app.route('/minilabs/')
def minilabs():
    return render_template("minilabs.html")




if __name__ == "__main__":
    app.run(debug=True, port=5180)

