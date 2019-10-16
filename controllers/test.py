from bootstrap import app


class Test(object):
    def __init__(self, code=1):
        self._code = code

    def hello(self):
        print(app.Cli.config_get('path'))
        print(self._code)

    @staticmethod
    def run():
        return 'Ingesting! Nom nom nom...'
