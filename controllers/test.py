from ulitilies import telegrambot


class Test(object):
    def __init__(self, code=1):
        self._code = code

    def hello(self):
        token = '839308438:AAFmLwkNGvrCNDnjfWaRzx6GPuI-JB1suh8'
        t = telegrambot.TelegramBot(token)
        t.send_message('-266910580', 'Hello World')
        print(self._code)

    @staticmethod
    def run():
        return 'Ingesting! Nom nom nom...'
