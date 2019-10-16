import fire
from controllers import *
from controllers import CLASS_LIST

FIRE_ROUTES = dict()

for i in CLASS_LIST:
    FIRE_ROUTES[i] = eval(i + '.' + i.capitalize())


# print(FIRE_ROUTES)


if __name__ == '__main__':
    fire.Fire(FIRE_ROUTES)
