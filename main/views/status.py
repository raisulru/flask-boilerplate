from flask import jsonify
from flask_restful import Resource

class StatusView(Resource):
    
    def get(self):
        response = jsonify({"status": "OK"})
        response.status_code = 200
        return response