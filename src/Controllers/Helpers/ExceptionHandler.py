from functools import wraps
from flask import jsonify, make_response
from werkzeug.utils import redirect
from src.Exceptions.AuthorizationError import AuthorizationError
from src.Exceptions.DuplicateUserError import DuplicateUserError
from src.Exceptions.EmptyUserInformationError import EmptyUserInformationError
from src.Exceptions.RedirectError import RedirectError
from src.Exceptions.TokenInvalidError import TokenInvalidError
from src.Exceptions.TokenMissingError import TokenMissingError
from src.Exceptions.UrlNotFoundError import UrlNotFoundError


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
        except UrlNotFoundError:
            return make_response(jsonify({'message': 'Url could not be found.'}), 404)
        except TokenInvalidError:
            return make_response(jsonify({'message': 'Token is invalid.'}), 401)
        except TokenMissingError:
            return make_response(jsonify({'message': 'Token is missing.'}), 401)
        except RedirectError as e:
            return redirect(e.redirectUrl, code=302)

    return decorator
