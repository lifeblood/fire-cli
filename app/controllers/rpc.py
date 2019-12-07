import rpyc


class Rpc(rpyc.Service):
    def __init__(self):
        pass

    @staticmethod
    def exposed_hello(name):
        return "Hello, %s" % name
