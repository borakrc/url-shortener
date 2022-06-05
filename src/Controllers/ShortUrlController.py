from flask_restful import Resource
from flask import request
from src.Controllers.Helpers.ExceptionHandler import ExceptionHandler
from src.Controllers.Helpers.TokenRequired import TokenRequired
from src.config import Config

class ShortUrlController(Resource):
    def __init__(self):
        pass

    @ExceptionHandler
    @TokenRequired
    def put(self):
        longUrl: str = request.form['longUrl']
        Config.urlShortenerService.createShortUrl(longUrl)

        return {'res': 'res'}
