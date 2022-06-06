from src.Adapters.IDbAdapter import IDbAdapter
from src.Exceptions.UrlNotFoundError import UrlNotFoundError
from src.Models import UrlKeyModel
from src.Models.UrlKeyFactory import UrlKeyFactory
from src.Models.UrlModel import UrlModel
from src.Services.IUrlShortenerService import IUrlShortenerService


class UrlShortenerService(IUrlShortenerService):
    dbAdapter: IDbAdapter = None
    minimumShortUrlLength: int = None

    def __init__(self, dbAdapter: IDbAdapter, minimumShortUrlLength: int):
        self.dbAdapter: IDbAdapter = dbAdapter
        self.minimumShortUrlLength: int = minimumShortUrlLength

    def createShortUrl(self, longUrl: UrlModel) -> UrlKeyModel:
        counter = 0
        longUrlInDb: UrlModel = None
        shortUrl: UrlKeyModel = None
        while longUrlInDb or counter == 0:
            shortUrl = UrlKeyFactory().fromLongUrl(longUrl, self.minimumShortUrlLength + counter)
            try:
                longUrlInDb = self.dbAdapter.resolveShortUrl(shortUrl)
            except UrlNotFoundError:
                longUrlInDb = None
            counter += 1

        self.dbAdapter.putShortUrl(shortUrl)
        return shortUrl

    def resolveShortUrl(self, shortUrl: UrlKeyModel) -> UrlModel:
        longUrlInDb = self.dbAdapter.resolveShortUrl(shortUrl)
        return longUrlInDb

