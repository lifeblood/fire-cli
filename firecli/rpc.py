

class Rpc(object):
    def __init__(self):
        pass

    @staticmethod
    def _get_hostname(endpoint):
        return endpoint.split(':')[0]

    @staticmethod
    def _get_port(endpoint):
        return int(endpoint.split(':')[1])

    @staticmethod
    def zerorpc_server(rpc_service, endpoint='0.0.0.0:4242'):
        import zerorpc
        s = zerorpc.Server(rpc_service)
        s.bind('tcp://' + endpoint)
        print('Running ZeroRPC: {}'.format(rpc_service))
        print('Serving on: {}'.format(endpoint))
        s.run()

    @staticmethod
    def zerorpc_client(endpoint):
        import zerorpc
        c = zerorpc.Client()
        c.connect('tcp://' + endpoint)
        return c

    @classmethod
    def rpyc_server(cls, rpc_service, endpoint='0.0.0.0:4242'):
        from rpyc.utils.server import ThreadedServer
        server = ThreadedServer(rpc_service, port=cls._get_port(endpoint), hostname=cls._get_hostname(endpoint))
        print('Running RPyC: {}'.format(rpc_service))
        print('Serving on: {}'.format(endpoint))
        server.start()

    @classmethod
    def rpyc_client(cls, endpoint):
        import rpyc
        conn = rpyc.connect(cls._get_hostname(endpoint), cls._get_port(endpoint))
        return conn.root

