from bootstrap import *


class Test(object):
    def __init__(self, code=1):
        self._code = code

    def hello(self):
        print(config.get('path'))
        # print(app.Cli.config_get('patsh'))
        print(app.get_ip())
        print(app.TelegramBot.run())
        print(self._code)

    @staticmethod
    def run():
        return 'Ingesting! Nom nom nom...'

