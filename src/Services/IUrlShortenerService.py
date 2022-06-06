from abc import ABC, abstractmethod
from src.IConfig import IConfig
from src.Models.UrlKeyModel import UrlKeyModel
from src.Models.UrlModel import UrlModel


class IUrlShortenerService(ABC):
    @property
    @abstractmethod
    def config(self) -> IConfig:
        raise NotImplementedError

    @abstractmethod
    def __init__(self, config: IConfig):
        raise NotImplementedError

    @abstractmethod
    def createShortUrl(self, longUrl: UrlModel) -> UrlKeyModel:
        raise NotImplementedError

    @abstractmethod
    def resolveShortUrl(self, shortUrl: UrlKeyModel) -> UrlModel:
        raise NotImplementedError
