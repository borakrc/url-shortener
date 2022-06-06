from src.Models.EmailModel import EmailModel
from src.Models.PasswordHashFactory import PasswordHashFactory
from src.Models.PasswordHashModel import PasswordHashModel
from src.Models.UserModel import UserModel


class UserModelFactory:
    passwordSalt: str = None

    def __init__(self, passwordSalt):
        self.passwordSalt = passwordSalt

    def createInstance(self, email: str, rawPassword: str) -> UserModel:
        emailObject: EmailModel = EmailModel(email)
        passwordObject: PasswordHashModel = PasswordHashFactory(self.passwordSalt).fromRawPassword(rawPassword)
        user: UserModel = UserModel(emailObject, passwordObject)
        return user

    def fromDict(self, userDict) -> UserModel:
        emailObject: EmailModel = EmailModel(userDict['email'])
        passwordObject: PasswordHashModel = PasswordHashFactory(self.passwordSalt).fromHashedPassword(userDict['password'])
        user: UserModel = UserModel(emailObject, passwordObject)
        return user


