import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cdmbi'
    MAIL_SUBJECT_PREFIX = '[iEQA]'
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL')
    MAIL_SENDER = ADMIN_EMAIL

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    #TODO: add email info

    MONGO_DBNAME = 'data-dev'


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    MONGO_DBNAME = 'data-test'


class ProductionConfig(Config):
    MONGO_DBNAME = 'data'

config = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig,
        'default': DevelopmentConfig,
    }
