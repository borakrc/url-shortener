from flask import Flask
from flask_restful import Api

from src.Controllers.SignUpController import SignUpController
from src.config import Config

app = Flask(__name__)
Config.initConfig()
api = Api(app)

api.add_resource(SignUpController, '/api/v1/signup')

def serve():
    app.run(debug=True, host='0.0.0.0', port=5001)
