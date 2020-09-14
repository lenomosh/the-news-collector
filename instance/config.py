import os


class Config:
    basedir = os.path.abspath(os.path.dirname(__file__))
    API_KEY = 'fe0577b9a2f64260a0f3286c2467bff2'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SECRET_KEY = 'MURTREDSCXCsretyuio9'

class ProdConfig(Config):
    DEBUG = False


class DevConfig(Config):
    DEBUG = True
