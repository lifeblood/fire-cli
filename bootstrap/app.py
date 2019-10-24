from firecli import FireCli, Connection


class App(FireCli):

    _config_path = './config/config.ini'

    def __init__(self):
        super(App, self).__init__()

    @classmethod
    def config(cls):
        from helpers import fireconfig
        return fireconfig.FireConfig(cls._config_path)

    @staticmethod
    def utils():
        from helpers import utils
        return utils.Utils()

    @classmethod
    def db(cls):
        _host = cls.config().get('mysql::host')
        _port = cls.config().getint('mysql::port')
        _user = cls.config().get('mysql::user')
        _password = cls.config().get('mysql::password')
        _db = App.config().get('mysql::db')
        return Connection(host=_host, port=_port, user=_user, pwd=_password, schema=_db)


class DB(Connection):
    def __init__(self):
        self._host = App.config().get('mysql::host')
        self._port = App.config().getint('mysql::port')
        self._user = App.config().get('mysql::user')
        self._password = App.config().get('mysql::password')
        self._db = App.config().get('mysql::db')
        super(DB, self).__init__(host=self._host, port=self._port, user=self._user, pwd=self._password, schema=self._db)


class Route(FireCli):
    _controller_dir = 'controllers'

    def __init__(self):
        super(Route, self).__init__()

    @classmethod
    def run(cls):
        super(Route, cls).init(cls._controller_dir)


