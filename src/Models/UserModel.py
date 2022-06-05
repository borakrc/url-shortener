from __future__ import annotations
from src.Models import EmailModel
from src.Models.PasswordHashModel import PasswordHashModel

class UserModel:
    email: EmailModel
    hashedPassword: PasswordHashModel

    def __init__(self, email: EmailModel, hashedPassword: PasswordHashModel):
        self.email = email
        self.hashedPassword = hashedPassword

    def toJson(self) -> dict:
        return {
            'email': self.email.toString(),
            'password': self.hashedPassword.toString(),
        }

    def compareCredentials(self, target: UserModel) -> bool:
        passwordMatch: bool = self.hashedPassword.toString() == target.hashedPassword.toString()
        emailMatch: bool = self.email.toString() == target.email.toString()

        return passwordMatch and emailMatch
