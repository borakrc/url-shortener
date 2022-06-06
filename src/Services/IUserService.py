from abc import ABC, abstractmethod

from src.Adapters.IDbAdapter import IDbAdapter
from src.Models.UserModel import UserModel

class IUserService(ABC):
    @property
    @abstractmethod
    def dbAdapter(self) -> IDbAdapter:
        raise NotImplementedError

    @property
    @abstractmethod
    def jwtSecret(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def __init__(self, dbAdapter: IDbAdapter, jwtSecret: str):
        raise NotImplementedError

    @abstractmethod
    def login(self, loginAttemptCredentials: UserModel) -> str:
        raise NotImplementedError

    @abstractmethod
    def register(self, user: UserModel) -> None:
        raise NotImplementedError
