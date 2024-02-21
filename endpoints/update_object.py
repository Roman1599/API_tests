import requests
from endpoints.base_endpoint import Endpoint

class UpdateObject(Endpoint):


    def update_by_id(self, obj_id,payload):
        self.responce = requests.put(f'https://api.restful-api.dev/objects/{obj_id}')
        self.responce_json = self.responce.json()

    def check_by_name(self,name):
        assert self.responce_json['name'] == name

