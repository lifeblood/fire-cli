import io
try:
    import configparser as configparser
except ImportError:
    import ConfigParser as configparser


class FireConfig(object):

    def __init__(self, config_path='./config/config.ini'):
        self._config_path = config_path
        self._default_section = 'default'
        self._splitter = '::'
        self._string = 'string'
        self._int = 'int'
        self._float = 'float'
        self._boolean = 'boolean'

    def _cfg(self):
        cfg = configparser.ConfigParser()
        with io.open(self._config_path, mode="r", encoding="utf-8") as f:
            try:
                cfg.read_file(f)
            except AttributeError:
                cfg.readfp(f)
        return cfg

    def _split_key(self, config_key):
        str_list = config_key.split(self._splitter)
        if len(str_list) == 1:
            str_list.insert(0, self._default_section)
        return str_list

    def _get_config(self, get_type, config_key):
        dictionary = {
            self._string: self._cfg().get,
            self._int: self._cfg().getint,
            self._float: self._cfg().getfloat,
            self._boolean: self._cfg().getboolean
        }
        config = self._split_key(config_key)
        try:
            data = dictionary.get(get_type)(config[0], config[1])
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            data = e
        return data

    def get(self, config_key):
        return self._get_config(self._string, config_key)

    def get_int(self, config_key):
        return self._get_config(self._int, config_key)

    def get_float(self, config_key):
        return self._get_config(self._float, config_key)

    def get_boolean(self, config_key):
        return self._get_config(self._boolean, config_key)
