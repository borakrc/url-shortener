import jwt
from src.Adapters.IDbAdapter import IDbAdapter
from src.Exceptions.AuthorizationError import AuthorizationError
from src.Exceptions.DuplicateUserError import DuplicateUserError
from src.IConfig import IConfig
from src.Models.UserModel import UserModel
from src.Services.IUserService import IUserService


class UserService(IUserService):
    config: IConfig = None

    def __init__(self, config: IConfig):
        self.config = config
        self.dbAdapter: IDbAdapter = config.dbAdapter

    def login(self, loginAttemptCredentials: UserModel) -> str:
        if not self.dbAdapter.authorizeUser(loginAttemptCredentials):
            raise AuthorizationError

        jwtSecret = self._getJwtSecret()
        encoded_jwt = jwt.encode({"email": loginAttemptCredentials.email.toString()}, jwtSecret, algorithm="HS256")

        return encoded_jwt

    def _getJwtSecret(self) -> str:
        return self.config.jwtSecret

    def register(self, user: UserModel) -> None:
        userExists: bool = self.dbAdapter.ifUserExists(user.email)
        if userExists:
            raise DuplicateUserError

        self.dbAdapter.putUser(user)
        return

