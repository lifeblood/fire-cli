try:
    import configparser as configparser
except Exception:
    import ConfigParser as configparser


class FireConfig(object):

    def __init__(self, config_path):
        self._config_path = config_path
        self.config = configparser.ConfigParser()
        self.config.read(self._config_path)

    def config_get(self, config_key):
        return self.config.get('default', config_key)


