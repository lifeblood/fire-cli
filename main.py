import fire
from bootstrap import route

if __name__ == '__main__':
    fire.Fire(route.get_routes())
