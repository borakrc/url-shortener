from flask_restful import Resource
from src.Controllers.Helpers.ExceptionHandler import ExceptionHandler
from src.Exceptions.RedirectError import RedirectError
from src.Models.UrlKeyModel import UrlKeyModel
from src.Models.UrlModel import UrlModel
from src.config import Config

class ShortUrlResolveController(Resource):
    def __init__(self):
        pass

    @ExceptionHandler
    def get(self, path: str):
        shortUrl = UrlKeyModel(path, None)
        longUrl: UrlModel = Config.urlShortenerService.resolveShortUrl(shortUrl)
        raise RedirectError(longUrl.toString())
