import importlib


class App(object):
    def __init__(self):
        pass

    @staticmethod
    def config():
        from helpers import fireconfig
        return fireconfig.FireConfig('./config/config.ini')

    @staticmethod
    def utils():
        from helpers import utils
        return utils.Utils()


class Route(object):
    def __init__(self):
        pass

    @staticmethod
    def get_routes(controller_dir='controllers'):
        fire_routes = dict()
        from routes.route import route_list
        for model_name in route_list:
            model = getattr(importlib.import_module(controller_dir + '.' + model_name), model_name.capitalize())
            fire_routes[model_name] = model
        return fire_routes
