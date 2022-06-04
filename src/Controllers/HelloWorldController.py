from flask_restful import Resource

from flask import request, make_response, jsonify

class HelloWorldController(Resource):
    def __init__(self):
        pass

    def get(self):
        return make_response(jsonify({'message':'hello, world! (from controller)'}), 200)
