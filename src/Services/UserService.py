import jwt
from src.Adapters.IDbAdapter import IDbAdapter
from src.Exceptions.AuthorizationError import AuthorizationError
from src.Exceptions.DuplicateUserError import DuplicateUserError
from src.Models.UserModel import UserModel


class UserService:
    config = None

    def __init__(self, config):
        self.config = config
        self.dbAdapter: IDbAdapter = config.dbAdapter

    def register(self, user: UserModel) -> None:
        userExists: bool = self.config.dbAdapter.ifUserExists(user.email)
        if userExists:
            raise DuplicateUserError

        self.config.dbAdapter.putUser(user)
        return

