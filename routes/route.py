from controllers import class_list
from controllers import *

fire_routes = dict()


for i in class_list:
    fire_routes[i] = eval(i + '.' + i.capitalize())
