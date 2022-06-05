from src.Adapters.IDbAdapter import IDbAdapter
from src.Exceptions.UrlNotFoundError import UrlNotFoundError
from src.Models import UrlKeyModel
from src.Models.UrlKeyFactory import UrlKeyFactory
from src.Models.UrlModel import UrlModel


class UrlShortenerService:
    config = None

    def __init__(self, config):
        self.config = config
        self.dbAdapter: IDbAdapter = config.dbAdapter

    def createShortUrl(self, longUrl: UrlModel) -> UrlKeyModel:
        counter = 0
        longUrlInDb: UrlModel = None
        while longUrlInDb or counter == 0:
            shortUrl: UrlKeyModel = UrlKeyFactory().fromLongUrl(longUrl, self.config.minimumShortUrlLength + counter)
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

