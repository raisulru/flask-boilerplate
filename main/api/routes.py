from ..api import api
from ..views import StatusView

api.add_resource(StatusView, '/status')
