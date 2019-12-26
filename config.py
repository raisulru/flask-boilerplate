import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or 'you-will-never-guess'
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CELERY_BROKER_URL = os.getenv('BROKER_URL')
    CELERY_RESULT_BACKEND = os.getenv('RESULT_BACKEND')
    # LOGGER_ENABLED = os.getenv('LOGGER_ENABLED')
    # LOGGER_LEVEL = os.getenv('LOGGER_LEVEL')
    # LOGGER_FILE = os.getenv('LOGGER_FILE')

