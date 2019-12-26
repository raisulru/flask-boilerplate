import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

CELERY_IMPORTS = ('main.celery.task')
CELERY_TASK_RESULT_EXPIRES = 30
CELERY_TIMEZONE = 'UTC'

CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml', 'pickle']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERYBEAT_SCHEDULE = {
    'test-running-schedule': {
        'task': 'main.celery.task.test_task',
        'schedule': timedelta(seconds=int(os.getenv('TEST_SCHEDULE_TIME_IN_SECONDS'))),
    }
}
