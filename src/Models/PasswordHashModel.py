class PasswordHashModel:
    value: bytes

    def __init__(self, hashedPassword: bytes):
        self.value = hashedPassword

    def __str__(self) -> str:
        return str(self.value)
    toString = __str__

    def toJson(self):
        return self.toString()
