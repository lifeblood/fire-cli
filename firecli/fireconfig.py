import io
try:
    import configparser as configparser
except Exception:
    import ConfigParser as configparser


class FireConfig(object):

    def __init__(self, config_path='./config/config.ini'):
        self._config_path = config_path

    def _cfg(self):
        cfg = configparser.ConfigParser()
        with io.open(self._config_path, mode="r", encoding="utf-8") as f:
            try:
                cfg.read_file(f)
            except AttributeError:
                cfg.readfp(f)
        return cfg

    def get(self, config_key, section='default'):
        return self._cfg().has_option(section, config_key) and self._cfg().get(section, config_key) or None

