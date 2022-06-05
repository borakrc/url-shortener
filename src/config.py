import os

from src.Adapters.FirebaseAdapter import FirebaseAdapter
from src.Adapters.IDbAdapter import IDbAdapter
from src.Services.UrlShortenerService import UrlShortenerService
from src.Services.UserService import UserService


class Config:
    jwtSecret = None
    userService: UserService = None
    urlShortenerService: UrlShortenerService = None
    dbAdapter: IDbAdapter = None
    passwordSalt: str = None

    @staticmethod
    def initConfig():
        from dotenv import load_dotenv

        load_dotenv()

        Config.jwtSecret = os.getenv('JWT_SECRET')
        Config.passwordSalt = os.getenv('PASSWORD_HASH_SALT')

        Config.dbAdapter = FirebaseAdapter(Config)
        Config.userService = UserService(Config)
