from flask_restful import Resource
from flask_http_response import success, result, error
from main.tasks import test_task
"""from elasticsearch_dsl import Search
"""
'''from main import es
'''

class StatusView(Resource):
    
    def get(self):
        test_task.delay()
        return success.return_response('Hi this is flask boilerplate', 200)


''' For elastic search query and view '''
"""class ElasticSearchView(Resource):
    
    def get(self):
        s = Search(using=es, index="workers")
        s = s.execute()
        arr = []
        for hit in s:
            dic = {
                'score': hit.meta.score, 
                'name': hit.name
            }
            arr.append(dic)
        return result.return_response(arr, 200)"""