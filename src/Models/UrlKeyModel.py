from src.Models.UrlModel import UrlModel


class UrlKeyModel:
    key: str
    targetUrl: UrlModel

    def __init__(self, key: str, targetUrl: UrlModel):
        self.key: str = key
        self.targetUrl: UrlModel = targetUrl

    def __str__(self) -> str:
        return self.key

    def toJson(self):
        return {'key': self.key, 'targetUrl': self.targetUrl}

    toString = __str__

    def toPath(self):
        return '/' + self.toString()