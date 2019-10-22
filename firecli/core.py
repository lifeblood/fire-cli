import fire
from .routing import Routing


class FireCli(object):
    def __init__(self):
        pass

    @classmethod
    def init(cls, controller_dir):
        fire.Fire(Routing.get_routes(controller_dir))

