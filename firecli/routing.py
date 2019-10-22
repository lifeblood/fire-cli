import importlib


class Routing(object):
    def __init__(self):
        pass

    @staticmethod
    def _get_class_name(model_name):
        class_name = "".join(model_name.split('.')[1:])
        if class_name == '':
            class_name = model_name
        return class_name

    @classmethod
    def get_routes(cls, controller_dir):
        fire_routes = dict()
        from routes.route import route_dict
        for key in route_dict:
            class_name = cls._get_class_name(route_dict[key])
            fire_routes[key] = getattr(importlib.import_module(controller_dir + '.' + key), class_name)
        return fire_routes
