from abc import ABC, abstractmethod
from src.Models.EmailModel import EmailModel
from src.Models.UrlKeyModel import UrlKeyModel
from src.Models.UrlModel import UrlModel
from src.Models.UserModel import UserModel

class IDbAdapter(ABC):
    @abstractmethod
    def authorizeUser(self, loginAttemptCredentials: UserModel) -> bool:
        raise NotImplementedError

    @abstractmethod
    def getUser(self, email: EmailModel) -> UserModel:
        raise NotImplementedError

    @abstractmethod
    def resolveShortUrl(self, shortUrl: UrlKeyModel) -> UrlModel:
        raise NotImplementedError

    @abstractmethod
    def putShortUrl(self, shortUrl: UrlKeyModel) -> None:
        raise NotImplementedError

    @abstractmethod
    def putUser(self, email: UserModel) -> None:
        raise NotImplementedError

    @abstractmethod
    def ifUserExists(self, email: EmailModel) -> bool:
        raise NotImplementedError
