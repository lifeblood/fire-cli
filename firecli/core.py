import fire
from .routing import Routing
from .database import MySQL
from .rpc import Rpc


class FireCli(object):
    def __init__(self):
        pass

    @classmethod
    def init_fire(cls, controller_dir):
        fire.Fire(Routing.get_routes(controller_dir))

    @classmethod
    def init_rpc(cls, controller_dir, name, endpoint='0.0.0.0:4242'):
        Rpc.rpyc_server(Routing.get_rpc_routes(controller_dir, name), endpoint)


class Connection(object):
    def __init__(self, **kwargs):
        self._db = MySQL.connect(**kwargs)

    def get_version(self):
        try:
            with self._db.cursor() as cursor:
                # Create a new record
                sql = "select version()"
                cursor.execute(sql)
                result = cursor.fetchone()
                return result
            # connection is not autocommit by default. So you must commit to save
            # your changes.

        finally:
            self._db.close()
