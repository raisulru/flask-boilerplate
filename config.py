import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or 'you-will-never-guess'
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CELERY_BROKER_URL = os.getenv('BROKER_URL')
    CELERY_RESULT_BACKEND = os.getenv('RESULT_BACKEND')
    MONGODB_SETTINGS = {
        'host': os.getenv('MONGODB_URI')
    }
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ELASTICSEARCH_HOST = os.getenv('ELASTICSEARCH_HOST')

    # LOGGER_ENABLED = os.getenv('LOGGER_ENABLED')
    # LOGGER_LEVEL = os.getenv('LOGGER_LEVEL')
    # LOGGER_FILE = os.getenv('LOGGER_FILE')

