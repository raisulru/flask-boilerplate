from flask import Blueprint
from flask_restful import Api

blue_print = Blueprint('api', __name__)
api = Api(blue_print)

from ..api import routes
from ..views import *
