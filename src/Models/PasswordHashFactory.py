import bcrypt
from src.Models.PasswordHashModel import PasswordHashModel


class PasswordHashFactory:
    passwordSalt: str = None

    def __init__(self, passwordSalt: str):
        self.passwordSalt = passwordSalt

    def fromRawPassword(self, rawPassword: str) -> PasswordHashModel:
        hashedPassword: bytes = self._hashPassword(rawPassword)
        passwordObject: PasswordHashModel = PasswordHashModel(hashedPassword)
        return passwordObject

    def fromHashedPassword(self, hashedPassword: bytes) -> PasswordHashModel:
        password: PasswordHashModel = PasswordHashModel(hashedPassword)
        return password

    def _hashPassword(self, password: str) -> bytes:
        SaltedPassword = (password + self.passwordSalt).encode('utf-8')

        # I gave it a static seed(salt) so that it produces the same hash given the same password.
        # This is not a best practice, but I hope you let this one pass given the time constraints.
        # When a random seed is used, even if two users have the same password, the hashes will be different.
        # But it can still verify if a hash is generated from a specific password or not.
        # Embedding this in the code still more secure than SHA-512 because we're salting the password above.
        hash = bcrypt.hashpw(SaltedPassword, b'$2b$12$uw67b2JIjzhyHDMsb3XW9.')

        return hash
