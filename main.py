from bootstrap import route
import click


@click.command()
@click.option('--rpc', '-r', is_flag=True, help='Start ZeroRPC tcp server')
@click.argument('name', required=False)
@click.argument('cmd', required=False)
def init(rpc, name, cmd):
    if rpc:
        route.run_rpc(name)
    else:
        route.run_fire()


if __name__ == '__main__':
    init()
