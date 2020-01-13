from flask import Flask
'''from flask_mongoengine import MongoEngine
from flask_sqlalchemy import SQLAlchemy
from elasticsearch import Elasticsearch'''
from flask_sqlalchemy import SQLAlchemy

from config import Config
from .celery import make_celery
'''db = MongoEngine()
db = SQLAlchemy()
es = Elasticsearch(host=Config.ELASTICSEARCH_HOST)'''

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    ''' 
    db.init_app(app)
    '''
    db.init_app(app)

    # for relational database you need to create all db first
    with app.app_context():
        # Import any one of your model name here
        from main.models.test_db import User
        db.create_all()
    


    from .api import blue_print
    app.register_blueprint(blue_print, url_prefix='/api/v1')

    return app


app = create_app(Config)

celery = make_celery(app=app)
celery.autodiscover_tasks(
    ['main.tasks'], 
    related_name='tasks', 
    force=True
)
