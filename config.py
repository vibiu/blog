import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRRT_KEY') or 'vibiu_s_screat'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass


class ProductConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATA_BASE') or 'sqlite:////' + os.path.join(basedir, 'data.sqlite')


config = {
    'product': ProductConfig,
    'default': ProductConfig
}
