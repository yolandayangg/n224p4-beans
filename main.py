
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

@app.route('/search/')
def search():
    return render_template("CRUD/templates/search.html")

@app.route('/calm1/')
def calm1():
    return render_template("Personal/calm1.html")

@app.route('/calm2/')
def calm2():
    return render_template("Personal/calm2.html")

@app.route('/calm4/')
def calm4():
    return render_template("Personal/calm4.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)









