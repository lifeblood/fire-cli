from bootstrap import app


class Model(object):
    def __init__(self):
        pass

    @staticmethod
    def version():
        print(app.db())
        print(app.db())
        return app.db().get_version()
