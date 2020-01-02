# Flask-Boilerplate
A full structured flask-rest-api boilerplate

# Tech we use
- flask = "==1.1.1"
- flask-restful = "==0.3.7"
- python-dotenv = "==0.10.3"
- pytest = "==5.3.2"
- celery = "==4.4.0"
- marshmallow = "==3.3.0"
- redis = "==3.3.11"
- elasticsearch-dsl = "==7.1.0"
- flask-http-response = "==0.0.1.0"
- flask-mongoengine = "==0.9.5"
- flask-sqlalchemy = "==2.4.1"

# How to Run
- Use any virtualenv (We have use Pipenv)
- copy `.env.example` to `.env`
- Change the port whatever you like.
- Rename `your_app.py` to to your actual app name. Then change it to `.env` file
- Install dependencies
- Run `./runserver.sh` in your console.
- Use any kind of database as your need by uncomment the code.
- Check status of app by get request on `http://0.0.0.0:port/api/v1/status`
- If you want to use any celery task then run celery by `celery -A main.celery worker -B -l info`
- Run test by runing `pytest`
