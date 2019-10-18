from bootstrap import *


class Test(object):
    def __init__(self, code=1):
        self._code = code

    def hello(self):
        print(config.get('path'))
        r = config.get('ansible_url')
        print(r)
        print(app.get_ip())
        print(app.TelegramBot('2'))
        print(app.TelegramBot('2'))
        print(self._code)

    @staticmethod
    def run():
        return 'Ingesting! Nom nom nom...'

