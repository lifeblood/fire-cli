import io
try:
    import configparser as configparser
except Exception:
    import ConfigParser as configparser


class FireConfig(object):

    def __init__(self, config_path='./config/config.ini'):
        self._config_path = config_path
        self._default_section = 'default'
        self._splitter = '::'

    def _cfg(self):
        cfg = configparser.ConfigParser()
        with io.open(self._config_path, mode="r", encoding="utf-8") as f:
            try:
                cfg.read_file(f)
            except AttributeError:
                cfg.readfp(f)
        return cfg

    def _split_init_key(self, config_key):
        str_list = config_key.split(self._splitter)
        if len(str_list) == 1:
            str_list.insert(0, self._default_section)
        return str_list

    def get(self, config_key):
        data = self._split_init_key(config_key)
        section = "".join(data[0:1])
        key = "".join(data[-1:2])
        return self._cfg().has_option(section, key) and self._cfg().get(section, key) or None

    def getint(self, config_key):
        data = self._split_init_key(config_key)
        section = "".join(data[0:1])
        key = "".join(data[-1:2])
        return self._cfg().has_option(section, key) and self._cfg().getint(section, key) or None

