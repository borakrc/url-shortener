class ExceptionBase(Exception):
    def __call__(self, *args):
        return self.__class__(*(self.args + args))
