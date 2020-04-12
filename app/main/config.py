import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres://%s:%s@%s:%s/%s' % (os.environ['AUTH_DB_USER'],
                                                            os.environ['AUTH_DB_PASS'],
                                                            os.environ['AUTH_DB_URL'],
                                                            os.environ['AUTH_DB_PORT'],
                                                            'auth_dev')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgres://%s:%s@%s:%s/%s' % (os.environ['AUTH_DB_USER'],
                                                            os.environ['AUTH_DB_PASS'],
                                                            os.environ['AUTH_DB_URL'],
                                                            os.environ['AUTH_DB_PORT'],
                                                            'auth_test')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://%s:%s@%s:%s/%s' % (os.environ['AUTH_DB_USER'],
                                                            os.environ['AUTH_DB_PASS'],
                                                            os.environ['AUTH_DB_URL'],
                                                            os.environ['AUTH_DB_PORT'],
                                                            'auth_prod')


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
