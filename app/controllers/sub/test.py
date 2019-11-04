from bootstrap import app
from app.models import *


class Test(object):
    def __init__(self, code=1):
        self._code = code
        self.Bot = TelegramBot(app.config().get('bot_token'))

    def hello(self):
        print(app.config().get('name'))
        print(app.config().get('cnname'))
        print(TelegramBot.run('ss'))
        print(app.config())
        print(app.utils().get_ip())
        print(app.utils())
        print(app.utils())
        print(self._code)

    @staticmethod
    def run():
        return 'Ingesting! Nom nom nom...'
