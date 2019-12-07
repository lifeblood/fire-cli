import importlib
import sys
from routes.route import route_dict


class Routing(object):
    def __init__(self):
        pass

    @classmethod
    def get_routes(cls, controller_dir):
        fire_routes = dict()
        from routes.route import route_dict
        for key, value in route_dict.items():
            fire_routes[key] = getattr(importlib.import_module(controller_dir + '.' + key), value)
        return fire_routes

    @classmethod
    def get_rpc_routes(cls, controller_dir, name):
        try:
            rpc_route = getattr(importlib.import_module(controller_dir + '.' + name), route_dict[name])
            return rpc_route
        except (RuntimeError, TypeError, NameError) as e:
            sys.exit("Get rpc route name [{}] error: {}".format(name, e))
