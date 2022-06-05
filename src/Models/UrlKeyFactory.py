import random
import string
from src.Models.UrlKeyModel import UrlKeyModel
from src.Models.UrlModel import UrlModel


class UrlKeyFactory:
    def __init__(self):
        pass

    def fromLongUrl(self, longUrl: UrlModel, length: int) -> UrlKeyModel:
        characterOptions = string.ascii_letters + string.digits
        random.seed(longUrl.toString())
        key: str = ''.join(random.choice(characterOptions) for i in range(length))
        return UrlKeyModel(key, longUrl)
