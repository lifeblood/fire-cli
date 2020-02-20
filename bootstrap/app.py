from firecli import FireCli, Connection
import sys


class App(FireCli):
    _config_path = './config/config.ini'
    _mysql_section = 'mysql::'

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
    def _get(cls, key):
        return cls.config().get(cls._mysql_section + key)

    @classmethod
    def _get_int(cls, key):
        return cls.config().get_int(cls._mysql_section + key)

    @classmethod
    def db(cls):
        return Connection(host=cls._get('host'), port=cls._get_int('port'), user=cls._get('user'),
                          pwd=cls._get('password'), schema=cls._get('db'))

    @classmethod
    def rpclient(cls, endpoint):
        from firecli.rpc import Rpc
        c = Rpc.rpyc_client(endpoint)
        return c


class Route(FireCli):
    _controller_dir = 'app.controllers'
    _rpc_dir = 'app.rpc'

    def __init__(self):
        super(Route, self).__init__()

    @staticmethod
    def usage():
        print('main.py usage:')
        print('-h: print help message.')
        print('-rpc: run rpc with daemon')
        print('default: run fire cli program')

    @staticmethod
    def rpc_usage():
        print('rpc.py usage:')
        print('-h: print help message.')
        print('default: run fire rpc program')

    @classmethod
    def run_fire(cls):
        super(Route, cls).init_fire(cls._controller_dir)

    @classmethod
    def run_rpc(cls):
        try:
            class_name = sys.argv[1]
            if class_name == '-h':
                cls.rpc_usage()
            else:
                super(Route, cls).init_rpc(cls._rpc_dir, class_name, endpoint=App.config().get('rpc::endpoint'))
        except (IndexError, ValueError) as e:
            cls.rpc_usage()
            sys.exit("Get rpc class name error: {}".format(e))

    @classmethod
    def run(cls):
        try:
            if sys.argv[1] == '-h':
                cls.usage()
            else:
                cls.run_fire()
        except IndexError:
            cls.usage()
