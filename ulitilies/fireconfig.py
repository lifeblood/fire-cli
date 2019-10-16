try:
    import configparser as configparser
except Exception:
    import ConfigParser as configparser


class FireConfig(object):

    def __init__(self):
        self.config_path = './config/config.ini'
        self.config = configparser.ConfigParser()
        self.config.read(self.config_path)

    def config_get(self, config_key):
        return self.config.get('default', config_key)


