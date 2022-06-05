from src.Exceptions.ExceptionBase import ExceptionBase

class RedirectError(ExceptionBase):
    redirectUrl: str = None

    def __init__(self, url: str, *args: object):
        super().__init__(args)
        self.redirectUrl = url
