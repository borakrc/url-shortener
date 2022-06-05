from flask_restful import Resource

class HelloWorldController(Resource):
    def get(self):
        return {'success': True}
