
class Endpoint:
    responce = None
    responce_json = None

    def check_responce_is_200(self):
        assert self.responce.status_code == 200