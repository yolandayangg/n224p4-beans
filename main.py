# import "packages" from flask
from flask import Flask, render_template
from flask import request

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


@app.route('/walruses/')
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

@app.route('/binary/')
def binary():
    return render_template("binary.html")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True, port=5180)

