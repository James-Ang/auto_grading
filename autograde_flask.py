from flask import Flask, request
from flask_restful import Resource, Api
from autograde_lib import select_grade
import pandas as pd
import json

app = Flask(__name__)
api = Api(app)

#%% Endpoint '/' - to test connection
class index(Resource):
    def get(self):
        return request.url

#%% Endpoint '/recomm_grade'
class recomm_grade(Resource):

    def post(self):
        data_json = request.get_json()

        selected_grade = select_grade(data_json)
        #retJSON = "OK" #selected_grade

        retJSON = {
            "selected_grade": selected_grade
                    }

        return retJSON

api.add_resource(index, '/')
api.add_resource(recomm_grade, '/recomm_grade')

if __name__ == '__main__':
    app.run(debug=True)
