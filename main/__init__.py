from flask import Flask
from config import Config
from .celery import make_celery


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

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
