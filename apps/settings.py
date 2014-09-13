"""
settings.py

Configuration for Flask app

"""


class Config(object):
    # Set secret key to use session
    SECRET_KEY = "yeobaek-secret-key"
    debug = False


class Production(Config):
    debug = True
    CSRF_ENABLED = False
    ADMIN = "---"
    SQLALCHEMY_DATABASE_URI = 'mysql+gaerdbms:///blog?instance=---:---'
    migration_directory = 'migrations'