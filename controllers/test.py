# from ulitilies import telegrambot


class Test(object):
    def __init__(self, code=1):
        self._code = code

    def hello(self):
        print(self._code)

    @staticmethod
    def run():
        return 'Ingesting! Nom nom nom...'
