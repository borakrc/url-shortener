from abc import ABC, abstractmethod
from src.Adapters.IDbAdapter import IDbAdapter
from src.Models.UrlKeyModel import UrlKeyModel
from src.Models.UrlModel import UrlModel


class IUrlShortenerService(ABC):
    @property
    @abstractmethod
    def dbAdapter(self) -> IDbAdapter:
        raise NotImplementedError

    @property
    @abstractmethod
    def minimumShortUrlLength(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def __init__(self, dbAdapter: IDbAdapter, minimumShortUrlLength: int):
        raise NotImplementedError

    @abstractmethod
    def createShortUrl(self, longUrl: UrlModel) -> UrlKeyModel:
        raise NotImplementedError

    @abstractmethod
    def resolveShortUrl(self, shortUrl: UrlKeyModel) -> UrlModel:
        raise NotImplementedError
