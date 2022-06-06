from abc import ABC, abstractmethod
from src.Adapters.IDbAdapter import IDbAdapter
from src.Services import IUrlShortenerService
from src.Services.IUserService import IUserService

class IConfig(ABC):
    @property
    @abstractmethod
    def jwtSecret(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def passwordSalt(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def minimumShortUrlLength(self) -> int:
        raise NotImplementedError

    @property
    @abstractmethod
    def userService(self) -> IUserService:
        raise NotImplementedError

    @property
    @abstractmethod
    def urlShortenerService(self) -> IUrlShortenerService:
        raise NotImplementedError

    @property
    @abstractmethod
    def dbAdapter(self) -> IDbAdapter:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def initConfig() -> None:
        raise NotImplementedError
