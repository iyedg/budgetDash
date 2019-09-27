import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "whaaaaaaaaat"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
