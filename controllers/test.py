from bootstrap import firecli


class Test(object):
    def __init__(self, code=1):
        self._code = code

    def hello(self):
        print(firecli.FireCli.config_get('path'))
        print(self._code)

    @staticmethod
    def run():
        return 'Ingesting! Nom nom nom...'
