from bootstrap import app
from models import *


class Test(object):
    def __init__(self, code=1):
        self._code = code
        self.Bot = TelegramBot(app.config().get('bot_token'))

    def hello(self):
        print(app.config().get('name'))
        print(app.config().get('mysql::host'))
        print(app.config().getint('mysql::port'))
        print(app.config().getboolean('boolean'))
        print(app.config().getfloat('float'))
        print(TelegramBot.run('ss'))
        print(app.config())
        print(app.utils().get_ip())
        args = {
            'url': 'http://google.com',
        }
        print(app.utils().http_get_json(**args))
        print(app.utils().eval('[1, 2, 3]'))
        print(Model.version())

    @staticmethod
    def run():
        return 'Ingesting! Nom nom nom...'
