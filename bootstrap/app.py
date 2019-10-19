
class App(object):
    def __init__(self):
        pass

    @staticmethod
    def config():
        from helpers import fireconfig
        return fireconfig.FireConfig('./config/config.ini')

    @staticmethod
    def utils():
        from helpers import utils
        return utils.Utils()


# fireConfig Singleton
# config = FireConfig('./config/config.ini')

