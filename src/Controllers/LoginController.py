from flask_restful import Resource
from flask import request
from src.Controllers.Helpers.ExceptionHandler import ExceptionHandler
from src.Models.UserModel import UserModel
from src.Models.UserModelFactory import UserModelFactory
from src.Services.IUserService import IUserService
from src.config import Config

class LoginController(Resource):
    def __init__(self):
        self.userService: IUserService = Config.userService

    @ExceptionHandler
    def post(self):
        rawEmail: str = request.form['email']
        rawPassword: str = request.form['password']
        user: UserModel = UserModelFactory(Config).createInstance(rawEmail, rawPassword)

        jwtToken: str = self.userService.login(user)

        return {'jwtToken': jwtToken}
