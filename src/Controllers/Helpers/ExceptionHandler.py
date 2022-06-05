from functools import wraps
from flask import jsonify, make_response
from src.Exceptions.AuthorizationError import AuthorizationError
from src.Exceptions.DuplicateUserError import DuplicateUserError
from src.Exceptions.EmptyUserInformationError import EmptyUserInformationError


def ExceptionHandler(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        try:
            return make_response(jsonify(f(*args, **kwargs)), 200)
        except AuthorizationError:
            return make_response(jsonify({'message': 'Incorrect credentials.'}), 401)
        except DuplicateUserError:
            return make_response(jsonify({'message': 'User already exists.'}), 409)
        except EmptyUserInformationError:
            return make_response(jsonify({'message': 'User could not be found.'}), 404)

    return decorator
