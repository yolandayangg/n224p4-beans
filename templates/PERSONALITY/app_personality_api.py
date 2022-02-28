"""control dependencies to support CRUD routes and APIs"""
from flask import Blueprint, render_template
from flask_restful import Api, Resource
import requests

from sql import *

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects

app_personality_api = Blueprint('personality_api', __name__,
                         url_prefix='/personality_api',
                         template_folder='templates/personality/',
                         static_folder='static',
                         static_url_path='../../static')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_personality_api)


# Method #2 for CRUD
@app_personality_api.route('/')
def personality_api():
    """obtains all Users from table and loads Admin Form"""
    return render_template("personality_async.html", table=person_all())


""" API routes section """


class PersonAPI:
    # class for create/post
    class _Create(Resource):
        def post(self, name, type, password, phone):
            po = Person(name, type, password, phone)
            person = po.create()
            if person:
                return person.read()
            return {'message': f'Processed {name}, either a format error or {type} is duplicate'}, 210

    # class for read/get
    class _Read(Resource):
        def get(self):
            return person_all()

    # class for delete
    class _ReadID(Resource):
        def get(self, userid):
            po = user_by_id(userid)
            if po is None:
                return {'message': f"{userid} is not found"}, 210
            data = po.read()
            return data

    # class for read/get
    class _ReadILike(Resource):
        def get(self, term):
            return person_ilike(term)

    # class for update/put
    class _Update(Resource):
        def put(self, type, name):
            po = type(type)
            if po is None:
                return {'message': f"{type} is not found"}, 210
            po.update(name)
            return po.read()

        # class for update/put

    class _UpdateName(Resource):
        def put(self, userid, name):
            po = user_by_id(userid)
            if po is not None:
                po.update(name)
            return po.read()

    class _UpdateAll(Resource):
        def put(self, type, name, password, phone):
            po = person_by_type(type)
            if po is None:
                return {'message': f"{type} is not found"}, 210
            po.update(name, password, phone)
            return po.read()

    # class for delete
    class _Delete(Resource):
        def delete(self, userid):
            po = user_by_id(userid)
            if po is None:
                return {'message': f"{userid} is not found"}, 210
            data = po.read()
            po.delete()
            return data

    # building RESTapi resource
    # building RESTapi resource
    api.add_resource(_Create, '/create/<string:name>/<string:type>/<string:password>/<string:phone>')
    api.add_resource(_Read, '/read/')
    api.add_resource(_ReadID, '/read/<int:userid>')
    api.add_resource(_ReadILike, '/read/ilike/<string:term>')
    api.add_resource(_Update, '/update/<string:type>/<string:name>')
    api.add_resource(_UpdateName, '/update/<int:userid>/<string:name>')
    api.add_resource(_UpdateAll, '/update/<string:type>/<string:name>/<string:password>/<string:phone>')
    api.add_resource(_Delete, '/delete/<int:userid>')


""" API testing section """


def api_tester():
    # local host URL for model
    url = 'http://localhost:5222/personality_api'

    # test conditions
    API = 0
    METHOD = 1
    tests = [
        ['/create/Wilma Flintstone/wilma@bedrock.org/123wifli/0001112222', "post"],
        ['/create/Fred Flintstone/fred@bedrock.org/123wifli/0001112222', "post"],
        ['/read/', "get"],
        ['/read/1', "get"],
        ['/read/ilike/John', "get"],
        ['/read/ilike/com', "get"],
        ['/update/wilma@bedrock.org/Wilma S Flintstone/123wsfli/0001112229', "put"],
        ['/update/wilma@bedrock.org/Wilma Slaghoople Flintstone', "put"],
        ['/delete/4', "delete"],
        ['/read/4', "get"],
        ['/delete/5', "delete"],
        ['/read/5', "get"],
        ['/update/1/Thomas Alva Edison', "put"]
    ]

    # loop through each test condition and provide feedback
    for test in tests:
        print()
        print(f"({test[METHOD]}, {url + test[API]})")
        if test[METHOD] == 'get':
            response = requests.get(url + test[API])
        elif test[METHOD] == 'post':
            response = requests.post(url + test[API])
        elif test[METHOD] == 'put':
            response = requests.put(url + test[API])
        elif test[METHOD] == 'delete':
            response = requests.delete(url + test[API])
        else:
            print("unknown RESTapi method")
            continue

        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")


def api_printer():
    print()
    print("Users table")
    for user in users_all():
        print(user)


"""validating api's requires server to be running"""
if __name__ == "__main__":
    api_tester()
    api_printer()