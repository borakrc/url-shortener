from flask import Flask
from flask_restful import Api

from src.Controllers.HelloWorldController import HelloWorldController

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorldController, '/')

def serve():
    app.run(debug=True, host='0.0.0.0', port=5001)
