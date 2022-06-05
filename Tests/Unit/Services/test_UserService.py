from unittest import TestCase

from Tests.Unit.TestHelpers import UserModelGenerator
from Tests.Unit.TestHelpers import MockConfigGenerator
from src.Exceptions.AuthorizationError import AuthorizationError
from src.Exceptions.DuplicateUserError import DuplicateUserError
from src.Services.UserService import UserService

class TestUserService(TestCase):
    def setUp(self):
        self.mockConfig = MockConfigGenerator.generate()
        self.mockUserModel = UserModelGenerator.generate(self.mockConfig)

    def test_login_raises_AuthorizationError_when_credentials_false(self):
        self.mockConfig.dbAdapter.authorizeUser.return_value = False

        service = UserService(self.mockConfig)

        self.assertRaises(AuthorizationError, service.login, self.mockUserModel)

    def test_login_does_not_raise_AuthorizationError_when_credentials_true(self):
        service = UserService(self.mockConfig)

        try:
            service.login(self.mockUserModel)
        except AuthorizationError:
            self.fail()

    def test_login_returns_correct_jwt_token(self):
        service = UserService(self.mockConfig)

        expectedToken = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Im1vY2tFbWFpbCJ9.v6n4DyY-RF2VcKjZAu19nECG5kwDia6k4EqBZBHGWF8'
        self.assertEqual(expectedToken, service.login(self.mockUserModel))


    def test_register_raises_DuplicateUserError_if_user_already_exists(self):
        self.mockConfig.dbAdapter.ifUserExists.return_value = True

        service = UserService(self.mockConfig)

        self.assertRaises(DuplicateUserError, service.register, self.mockUserModel)

    def test_register_does_not_raise_DuplicateUserError_if_user_does_not_exist(self):
        service = UserService(self.mockConfig)

        try:
            service.register(self.mockUserModel)
        except DuplicateUserError:
            self.fail()

    def test_register_calls_dbAdapter_putUser_method_once_if_user_does_not_exist(self):
        service = UserService(self.mockConfig)

        service.register(self.mockUserModel)

        self.mockConfig.dbAdapter.putUser.assert_called_once()

    def test_register_does_not_call_dbAdapter_putUser_method_if_user_already_exist(self):
        self.mockConfig.dbAdapter.ifUserExists.return_value = True

        service = UserService(self.mockConfig)

        try:
            service.register(self.mockUserModel)
        except:
            pass

        self.mockConfig.dbAdapter.putUser.assert_not_called()
