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
            'string': self._cfg().get,
            'int': self._cfg().getint,
            'float': self._cfg().getfloat,
            'boolean': self._cfg().getboolean
        }
        config = self._split_key(config_key)
        try:
            data = dictionary.get(get_type)(config[0], config[1])
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            data = e
        return data

    def get(self, config_key):
        return self._get_config('string', config_key)

    def getint(self, config_key):
        return self._get_config('int', config_key)

    def getfloat(self, config_key):
        return self._get_config('float', config_key)

    def getboolean(self, config_key):
        return self._get_config('boolean', config_key)
