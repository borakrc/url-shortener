from unittest import TestCase
from unittest.mock import MagicMock
from Tests.Unit.TestHelpers import MockConfigGenerator
from src.Models.UrlKeyModel import UrlKeyModel
from src.Models.UrlModel import UrlModel
from src.Services.UrlShortenerService import UrlShortenerService

class TestUrlShortenerService(TestCase):
    def setUp(self):
        self.mockConfig = MockConfigGenerator.generate()

    def test_resolveShortUrl_method_calls_dbAdapter_resolveShortUrl_method_once_with_correct_url_key(self):
        mockUrlKey = MagicMock()

        service = UrlShortenerService(self.mockConfig)
        service.resolveShortUrl(mockUrlKey)

        self.mockConfig.dbAdapter.resolveShortUrl.assert_called_once_with(mockUrlKey)


    def test_createShortUrl_method_calls_dbAdapter_putShortUrl_method_once_with_correct_url_key(self):
        mockUrl = MagicMock()

        service = UrlShortenerService(self.mockConfig)
        service.createShortUrl(mockUrl)

        self.mockConfig.dbAdapter.putShortUrl.assert_called_once()

    def test_createShortUrl_method_calls_dbAdapter_resolveShortUrl_method_until_it_returns_falsy_value(self):
        mockUrl = MagicMock()

        service = UrlShortenerService(self.mockConfig)
        service.createShortUrl(mockUrl)

        self.assertEqual(self.mockConfig.dbAdapter.resolveShortUrl.call_count, 3)

    def test_createShortUrl_method_creates_short_url_with_correct_length(self):
        mockUrl = UrlModel("testUrl")

        service = UrlShortenerService(self.mockConfig)
        urlKey: UrlKeyModel = service.createShortUrl(mockUrl)

        self.assertEqual(len(urlKey.toString()), 3)

    def test_createShortUrl_method_creates_same_key_for_same_url(self):
        mockUrl = UrlModel("testUrl")

        service = UrlShortenerService(self.mockConfig)
        urlKey: UrlKeyModel = service.createShortUrl(mockUrl)
        urlKey2: UrlKeyModel = service.createShortUrl(mockUrl)

        self.assertEqual(urlKey.toString(), urlKey2.toString()) # "uGn"

    def test_createShortUrl_method_creates_different_key_for_different_urls(self):
        mockUrl = UrlModel("testUrl")
        mockUrl2 = UrlModel("testUrl2")

        service = UrlShortenerService(self.mockConfig)
        urlKey: UrlKeyModel = service.createShortUrl(mockUrl)
        urlKey2: UrlKeyModel = service.createShortUrl(mockUrl2)

        self.assertNotEqual(urlKey.toString(), urlKey2.toString())
