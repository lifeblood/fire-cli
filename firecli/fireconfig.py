try:
    import configparser as configparser
except Exception:
    import ConfigParser as configparser


class FireConfig(object):

    def __init__(self, config_path='./config/config.ini'):
        self._config_path = config_path
        self._config = configparser.ConfigParser()
        self._config.read(self._config_path)

    def get(self, config_key, section='default'):
        return self._config.has_option(section, config_key) and self._config.get(section, config_key) or None
