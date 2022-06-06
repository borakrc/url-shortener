from unittest.mock import MagicMock
from src.Models.UrlModel import UrlModel

def generate() -> MagicMock:
    mockConfig = MagicMock()
    mockConfig.dbAdapter = MagicMock()
    mockConfig.dbAdapter.authorizeUser.return_value = True
    mockConfig.dbAdapter.ifUserExists.return_value = False
    mockConfig.dbAdapter.resolveShortUrl.side_effect = [UrlModel("mockValue1"), UrlModel("mockValue2"), None, UrlModel("mockValue1"), UrlModel("mockValue2"), None]
    mockConfig.passwordSalt = "mockSalt"
    mockConfig.minimumShortUrlLength = 1
    mockConfig.jwtSecret = "mockSecret"
    return mockConfig
