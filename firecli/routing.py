import importlib
import sys
from routes.route import route_dict, rpc_dict


class Routing(object):
    def __init__(self):
        pass

    @classmethod
    def get_routes(cls, controller_dir):
        fire_routes = dict()
        from routes.route import route_dict
        for key, value in route_dict.items():
            try:
                fire_routes[key] = getattr(importlib.import_module(controller_dir + '.' + key), value)
            except (RuntimeError, TypeError, NameError, ModuleNotFoundError) as e:
                sys.exit("Get route name [{}] error: {}".format(key, e))
        return fire_routes

    @classmethod
    def get_rpc_routes(cls, rpc_dir, name):
        try:
            rpc_route = getattr(importlib.import_module(rpc_dir + '.' + name), rpc_dict[name])
            return rpc_route
        except (RuntimeError, TypeError, NameError, ModuleNotFoundError, KeyError) as e:
            sys.exit("Get rpc route name [{}.{}] error: {}".format(rpc_dir, name, e))
