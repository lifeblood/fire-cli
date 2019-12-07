from bootstrap import app
from app.models import *


class Test(object):
    def __init__(self, code=1):
        self._code = code
        self.Bot = TelegramBot(app.config().get('bot_token'))

    def hello(self):
        print(app.config().get('name'))
        print(app.config().get('mysql::host'))
        print(app.config().get_int('mysql::port'))
        print(app.config().get_boolean('boolean'))
        print(app.config().get_float('float'))
        print(TelegramBot.run('fire'))
        print(app.config())
        print(app.utils().get_ip())
        args = {
            'url': 'http://api.plos.org/search?q=',
        }
        # a = app.utils().get_http_json(**args)
        # print(type(a))
        # print(a)
        print(app.utils().get_eval_string('[1, 2, 3]'))
        # print(Model.version())
        c = app.rpclient("127.0.0.1:4242")
        print(c.hello("rpc"))

    @staticmethod
    def run():
        return 'Ingesting! Nom nom nom...'
