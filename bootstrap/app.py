from firecli import FireCli


class App(object):
    _config_path = './config/config.ini'

    def __init__(self):
        pass

    @classmethod
    def config(cls):
        from helpers import fireconfig
        return fireconfig.FireConfig(cls._config_path)

    @staticmethod
    def utils():
        from helpers import utils
        return utils.Utils()


class Route(FireCli):
    _controller_dir = 'controllers'

    def __init__(self):
        super(Route, self).__init__()

    @classmethod
    def run(cls):
        super(Route, cls).init(cls._controller_dir)
