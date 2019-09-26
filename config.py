import os


class config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "whaaaaaaaaat"
    #DATABASE = os.path.join(app.instance_path, "saisie.db")
