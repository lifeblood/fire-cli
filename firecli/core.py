import fire
from .routing import Routing


class FireCli(object):
    def __init__(self):
        self._controller_dir = 'controllers'

    def init(self):
        fire.Fire(Routing.get_routes(self._controller_dir))

