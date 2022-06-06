import os
from src.Adapters.FirebaseAdapter import FirebaseAdapter
from src.Adapters.IDbAdapter import IDbAdapter
from src.IConfig import IConfig
from src.Services.IUrlShortenerService import IUrlShortenerService
from src.Services.IUserService import IUserService
from src.Services.UrlShortenerService import UrlShortenerService
from src.Services.UserService import UserService

class Config(IConfig):
    jwtSecret = None
    userService: IUserService = None
    urlShortenerService: IUrlShortenerService = None
    dbAdapter: IDbAdapter = None
    passwordSalt: str = None
    minimumShortUrlLength: int = 4

    @staticmethod
    def initConfig() -> None:
        from dotenv import load_dotenv

        load_dotenv()

        Config.jwtSecret = os.getenv('JWT_SECRET')
        Config.passwordSalt = os.getenv('PASSWORD_HASH_SALT')

        Config.dbAdapter = FirebaseAdapter(Config)
        Config.userService = UserService(Config)
        Config.urlShortenerService = UrlShortenerService(Config)
