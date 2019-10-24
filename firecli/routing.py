import importlib


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
