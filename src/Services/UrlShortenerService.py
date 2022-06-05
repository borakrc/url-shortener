from src.Adapters.IDbAdapter import IDbAdapter


class UrlShortenerService:
    config = None

    def __init__(self, config):
        self.config = config
        self.dbAdapter: IDbAdapter = config.dbAdapter

    def createShortUrl(self, longUrl) -> str:
        pass
