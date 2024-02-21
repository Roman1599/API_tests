import requests
from endpoints.base_endpoint import Endpoint


class CreateObject(Endpoint):


    def new_object(self, payload):
        self.responce = requests.post('https://api.restful-api.dev/objects', json=payload).json()
        self.responce_json = self.responce.json()

    def check_name(self,name):
        assert self.responce_json['name'] == name

