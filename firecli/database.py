import abc
import six


@six.add_metaclass(abc.ABCMeta)
class DbInterface(object):
    @abc.abstractmethod
    def connect(self):
        pass


class MySQL(DbInterface):

    @staticmethod
    def connect(**kwargs):
        import pymysql.cursors
        host = kwargs['host']
        port = kwargs['port']
        user = kwargs['user']
        pwd = kwargs['pwd']
        schema = kwargs['schema']
        conn = pymysql.connect(host=host,
                               port=port,
                               user=user,
                               password=pwd,
                               db=schema,
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.SSDictCursor)

        # cursor = conn.cursor()

        return conn
        # return conn is not None and cursor is not None




