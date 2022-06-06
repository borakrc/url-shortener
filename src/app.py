from flask import Flask
from flask_restful import Api

from src.Controllers.HelloWorldController import HelloWorldController
from src.Controllers.LoginController import LoginController
from src.Controllers.ShortUrlController import ShortUrlController
from src.Controllers.ShortUrlResolveController import ShortUrlResolveController
from src.Controllers.SignUpController import SignUpController
from src.Config import Config

app = Flask(__name__)
Config.initConfig()
api = Api(app)

api.add_resource(HelloWorldController, '/')
api.add_resource(SignUpController, '/api/v1/signup')
api.add_resource(LoginController, '/api/v1/login')
api.add_resource(ShortUrlController, '/api/v1/shortenUrl')
api.add_resource(ShortUrlResolveController, '/<path:path>')

def serve():
    app.run(debug=True, host='0.0.0.0', port=5001)
