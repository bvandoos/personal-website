from flask import Flask
from lib.flask.controllers.index import index


def create_app(object_name):
    app = Flask(__name__, static_url_path='')
    app.config.from_object(object_name)
    app.register_blueprint(index)

    return app