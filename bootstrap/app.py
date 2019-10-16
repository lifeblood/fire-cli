from ulitilies import *


class Cli(object):
    def __init__(self):
        pass

    @staticmethod
    def fire_config():
        return fireconfig.FireConfig('./config/config.ini')

    @classmethod
    def config_get(cls, key):
        config = cls.fire_config()
        return config.config_get(key)
