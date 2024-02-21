import requests
from endpoints.base_endpoint import Endpoint

class GetObject(Endpoint):


    def get_by_id(self, obj_id):
        self.responce = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
        self.responce_json = self.responce.json()

    def check_by_id(self,obj_id):
        assert self.responce_json['id'] == obj_id


    def check_responce_is_404(self):
        assert self.responce.status_code == 404