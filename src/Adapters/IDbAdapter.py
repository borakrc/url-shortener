from abc import ABC, abstractmethod
from src.Models.EmailModel import EmailModel
from src.Models.UserModel import UserModel

class IDbAdapter(ABC):
    @abstractmethod
    def getUser(self, email: EmailModel) -> UserModel:
        raise NotImplementedError

    @abstractmethod
    def putUser(self, email: UserModel) -> None:
        raise NotImplementedError

    @abstractmethod
    def ifUserExists(self, email: EmailModel) -> bool:
        raise NotImplementedError
