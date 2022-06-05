from src.Models.EmailModel import EmailModel
from src.Models.PasswordHashFactory import PasswordHashFactory
from src.Models.PasswordHashModel import PasswordHashModel
from src.Models.UserModel import UserModel


class UserModelFactory:
    def __init__(self, config):
        self.config = config

    def createInstance(self, email: str, rawPassword: str) -> UserModel:
        emailObject: EmailModel = EmailModel(email)
        passwordObject: PasswordHashModel = PasswordHashFactory(self.config).fromRawPassword(rawPassword)
        user: UserModel = UserModel(emailObject, passwordObject)
        return user

    def fromDict(self, userDict) -> UserModel:
        emailObject: EmailModel = EmailModel(userDict['email'])
        passwordObject: PasswordHashModel = PasswordHashFactory(self.config).fromHashedPassword(userDict['password'])
        user: UserModel = UserModel(emailObject, passwordObject)
        return user


