class Template(object):
    def __init__(self, code=1):
        self.code = code
        self._code = code

    @staticmethod
    def run():
        return 'ingesting! nom nom nom...'

    @classmethod
    def class_method(cls):
        print(cls.run())

    def public_method(self):
        print(self._code)

    def __private_method(self):
        print(self._code)

