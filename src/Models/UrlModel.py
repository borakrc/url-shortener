class UrlModel:
    value: str

    def __init__(self, value: str):
        self.value = value

    def __str__(self) -> str:
        return self.value

    def toJson(self):
        return self.value

    toString = __str__