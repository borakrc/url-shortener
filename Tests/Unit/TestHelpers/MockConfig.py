from unittest.mock import MagicMock

def getMockConfig() -> MagicMock:
    mockConfig = MagicMock()
    mockConfig.dbAdapter = MagicMock()
    mockConfig.dbAdapter.authorizeUser.return_value = True
    mockConfig.passwordSalt = "mockSalt"
    mockConfig.jwtSecret = "mockSecret"
    return mockConfig
