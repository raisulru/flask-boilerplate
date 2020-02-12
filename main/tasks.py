from main import celery

@celery.task
def test_task():
    print('On call task')

@celery.task
def schedule_task():
    print('schedule task')