from abc import ABC, abstractmethod
from src.IConfig import IConfig
from src.Models.UserModel import UserModel

class IUserService(ABC):
    @property
    @abstractmethod
    def config(self) -> IConfig:
        raise NotImplementedError

    @abstractmethod
    def __init__(self, config: IConfig):
        raise NotImplementedError

    @abstractmethod
    def login(self, loginAttemptCredentials: UserModel) -> str:
        raise NotImplementedError

    @abstractmethod
    def register(self, user: UserModel) -> None:
        raise NotImplementedError
