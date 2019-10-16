from ulitilies import *


class FireCli(object):
    def __init__(self):
        pass

    @staticmethod
    def fire_config():
        return fireconfig.FireConfig()

    @classmethod
    def config_get(cls, key):
        config = cls.fire_config()
        return config.config_get(key)
