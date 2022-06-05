from unittest import TestCase
from Tests.Unit.TestHelpers.MockConfig import getMockConfig
from src.Exceptions.AuthorizationError import AuthorizationError
from src.Models.UserModelFactory import UserModelFactory
from src.Services.UserService import UserService

class TestUserService(TestCase):
    def setUp(self):
        self.mockConfig = getMockConfig()

    def test_login_raises_AuthorizationError_when_credentials_false(self):
        self.mockConfig.dbAdapter.authorizeUser.return_value = False

        service = UserService(self.mockConfig)
        loginAttemptCredentials = UserModelFactory(self.mockConfig)\
            .fromDict({'email': 'mockEmail', 'password': 'MockPassword'})

        self.assertRaises(AuthorizationError, service.login, loginAttemptCredentials)

    def test_login_does_not_raise_AuthorizationError_when_credentials_true(self):
        service = UserService(self.mockConfig)

        loginAttemptCredentials = UserModelFactory(self.mockConfig)\
            .fromDict({'email': 'mockEmail', 'password': 'MockPassword'})

        try:
            service.login(loginAttemptCredentials)
        except AuthorizationError:
            self.fail()

    def test_login_returns_correct_jwt_token(self):
        service = UserService(self.mockConfig)

        loginAttemptCredentials = UserModelFactory(self.mockConfig)\
            .fromDict({'email': 'mockEmail', 'password': 'MockPassword'})

        expectedToken = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Im1vY2tFbWFpbCJ9.v6n4DyY-RF2VcKjZAu19nECG5kwDia6k4EqBZBHGWF8'
        self.assertEqual(expectedToken, service.login(loginAttemptCredentials))
