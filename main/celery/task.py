from main import celery

@celery.task()
def test_task():
    print('Succesfully run celery schedule')
