import os


class Config(object):

    FLASK_PORT = os.environ.get("FLASK_PORT", 5000)