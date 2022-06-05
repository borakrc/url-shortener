from unittest.mock import MagicMock

def generate() -> MagicMock:
    mockConfig = MagicMock()
    mockConfig.dbAdapter = MagicMock()
    mockConfig.dbAdapter.authorizeUser.return_value = True
    mockConfig.dbAdapter.ifUserExists.return_value = False
    mockConfig.passwordSalt = "mockSalt"
    mockConfig.jwtSecret = "mockSecret"
    return mockConfig
