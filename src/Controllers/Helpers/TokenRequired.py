import jwt
from functools import wraps
from flask import request
from jwt import InvalidSignatureError
from src.Exceptions.TokenInvalidError import TokenInvalidError
from src.Exceptions.TokenMissingError import TokenMissingError
from src.config import Config


def TokenRequired(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            raise TokenMissingError

        try:
            jwt.decode(token, Config.jwtSecret, algorithms=["HS256"])
        except InvalidSignatureError:
            raise TokenInvalidError

        return f(*args, **kwargs)

    return decorator
